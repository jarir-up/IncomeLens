"""Confidence in a requirement, from source authority, recency and agreement (ADR-0007).

Confidence applies to requirements, never to outcomes (ADR-0011).
"""

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Literal

from pakkifile.registry.model import Requirement, Source, SourceAuthority

Level = Literal["High", "Medium", "Low"]

# GLOSSARY "Source authority", highest first.
AUTHORITY_WEIGHT: Mapping[SourceAuthority, Decimal] = {
    "official_checklist": Decimal("1.00"),
    "consulate_page": Decimal("0.90"),
    "service_provider_page": Decimal("0.70"),
    "agent": Decimal("0.40"),
    "community_story": Decimal("0.20"),
}
# (maximum age in days, factor); anything older gets STALE.
RECENCY = ((365, Decimal("1.0")), (730, Decimal("0.8")), (1095, Decimal("0.6")))
STALE = Decimal("0.4")
AGREEMENT_BONUS = Decimal("0.05")
WEAK_CONFLICT_COST = Decimal("0.05")
HIGH = Decimal("0.80")
MEDIUM = Decimal("0.50")


@dataclass(frozen=True)
class Confidence:
    score: Decimal
    level: Level


def _recency(source: Source, as_of: date) -> Decimal:
    age = (as_of - (source.published or source.last_verified)).days
    return next((factor for limit, factor in RECENCY if age <= limit), STALE)


def _strength(source: Source, as_of: date) -> Decimal:
    return AUTHORITY_WEIGHT[source.source_authority] * _recency(source, as_of)


def confidence(req: Requirement, sources: Mapping[str, Source], as_of: date) -> Confidence:
    supporting = sorted(
        (_strength(sources[c.source], as_of) for c in req.citations if c.stance == "supports"),
        reverse=True,
    )
    conflicting = [
        _strength(sources[c.source], as_of) for c in req.citations if c.stance == "conflicts"
    ]
    top = supporting[0]
    score = min(top + AGREEMENT_BONUS * (len(supporting) - 1), Decimal("1"))
    score -= WEAK_CONFLICT_COST * sum(1 for s in conflicting if s < top)
    if any(s >= top for s in conflicting):
        score /= 2
    score = score.quantize(Decimal("0.01"))
    level: Level = "High" if score >= HIGH else "Medium" if score >= MEDIUM else "Low"
    return Confidence(score, level)
