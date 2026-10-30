"""Render pages from the shared Jinja2 templates (ADR-0039)."""

from jinja2 import Environment, PackageLoader, select_autoescape

from pakkifile.registry.model import RegistryEntry

_env = Environment(
    loader=PackageLoader("pakkifile.web", "templates"),
    autoescape=select_autoescape(),
)


def render_checklist(entry: RegistryEntry) -> str:
    return _env.get_template("checklist.html").render(entry=entry)
