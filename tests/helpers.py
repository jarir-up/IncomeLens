from pathlib import Path

from pakkifile.registry.files import load_registry
from pakkifile.registry.model import RegistryEntry


def islamabad_study() -> RegistryEntry:
    """The tracer's entry: German Embassy Islamabad, Study visa (D)."""
    return next(
        e
        for e in load_registry(Path("registry-data")).entries
        if e.authority.name == "German Embassy Islamabad" and e.application.purpose == "study"
    )
