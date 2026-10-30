from pathlib import Path

from pakkifile.registry.files import load_registry
from pakkifile.registry.model import Registry, RegistryEntry

REGISTRY: Registry = load_registry(Path("registry-data"))
ISLAMABAD = "German Embassy Islamabad"
KARACHI = "Consulate General of Germany, Karachi"


def entry(authority: str, purpose: str) -> RegistryEntry:
    return next(
        e
        for e in REGISTRY.entries
        if e.authority.name == authority and e.application.purpose == purpose
    )


def islamabad_study() -> RegistryEntry:
    """The tracer's entry."""
    return entry(ISLAMABAD, "study")
