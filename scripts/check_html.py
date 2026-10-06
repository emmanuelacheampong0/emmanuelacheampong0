"""Check local HTML links and duplicate IDs in the small static demos."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
PAGES = [ROOT / "index.html"] + sorted((ROOT / "games").rglob("*.html")) + sorted((ROOT / "research").rglob("*.html")) + sorted((ROOT / "projects").rglob("*.html"))


class PageAudit(HTMLParser):
    def __init__(self, path: Path) -> None:
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids: set[str] = set()
        self.errors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        element_id = attributes.get("id")
        if element_id:
            if element_id in self.ids:
                self.errors.append(f"duplicate id #{element_id}")
            self.ids.add(element_id)

        target = attributes.get("href") or attributes.get("src")
        if not target:
            return
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith("//") or not parsed.path:
            return
        destination = ((ROOT / parsed.path.lstrip("/")) if parsed.path.startswith("/") else (self.path.parent / parsed.path)).resolve()
        if destination.is_dir():
            destination = destination / "index.html"
        if not destination.exists():
            self.errors.append(f"missing local link: {target}")


def main() -> int:
    failures: list[str] = []
    for page in PAGES:
        audit = PageAudit(page)
        try:
            audit.feed(page.read_text(encoding="utf-8"))
        except (OSError, UnicodeError) as error:
            failures.append(f"{page.relative_to(ROOT)}: cannot read: {error}")
            continue
        failures.extend(f"{page.relative_to(ROOT)}: {error}" for error in audit.errors)

    if failures:
        print("HTML checks failed:")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1
    print(f"Checked {len(PAGES)} HTML pages: local links exist and IDs are unique.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
