"""Checklist pages. Imports only the registry, so the site build stays free of applicant data (R-22)."""

from collections.abc import Mapping

from pakkifile.registry.model import RegistryEntry, Source
from pakkifile.web.templates import env


def render_checklist(entry: RegistryEntry, sources: Mapping[str, Source]) -> str:
    return env.get_template("checklist.html").render(entry=entry, sources=sources)
