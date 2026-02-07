#!/usr/bin/env python3
"""Generate styled HTML resume from profile.toml for DOCX conversion."""

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:  # pragma: no cover
    try:
        import tomli as tomllib  # Python <=3.10 backport
    except ModuleNotFoundError as e:  # pragma: no cover
        raise ModuleNotFoundError(
            "Missing TOML parser. Use Python 3.11+ (tomllib) or install 'tomli'."
        ) from e
from pathlib import Path

# Blog theme colors
TEAL = "#037171"
GREEN = "#2a7f62"
DARKGREEN = "#03312e"
BLUE = "#0066BB"
FG = "#1d1d1d"
LIGHT_GRAY = "#666666"


def included_in(item, target: str) -> bool:
    """Return True if item is explicitly included for the target output."""
    if not isinstance(item, dict):
        return False
    return target in item.get("included_in", [])


def filter_included(items, target: str):
    return [x for x in items if included_in(x, target)]


def main():
    profile_path = Path(__file__).parent.parent / "data" / "profile.toml"
    with open(profile_path, "rb") as f:
        profile = tomllib.load(f)

    p = profile["personal"]
    bio = profile["bio"]
    skills = profile["skills"]
    target = "resume"

    html = []
    
    # Basic HTML structure with embedded styles
    html.append("""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body {
    font-family: Calibri, Arial, sans-serif;
    font-size: 11pt;
    color: """ + FG + """;
    line-height: 1.4;
    max-width: 8in;
    margin: 0 auto;
}
h1 {
    color: """ + TEAL + """;
    font-size: 22pt;
    margin: 0 0 4pt 0;
    text-align: center;
}
h2 {
    color: """ + GREEN + """;
    font-size: 12pt;
    text-transform: uppercase;
    border-bottom: 2pt solid """ + GREEN + """;
    padding-bottom: 2pt;
    margin: 14pt 0 8pt 0;
}
h3 {
    color: """ + DARKGREEN + """;
    font-size: 11pt;
    margin: 10pt 0 2pt 0;
}
a {
    color: """ + BLUE + """;
    text-decoration: none;
}
.tagline {
    text-align: center;
    font-style: italic;
    color: """ + LIGHT_GRAY + """;
    margin: 0 0 6pt 0;
}
.contact {
    text-align: center;
    font-size: 10pt;
    margin: 0 0 10pt 0;
}
.meta {
    font-size: 10pt;
    color: """ + LIGHT_GRAY + """;
    margin: 0 0 4pt 0;
}
strong {
    color: """ + DARKGREEN + """;
}
ul {
    margin: 4pt 0 0 0;
    padding-left: 20pt;
}
li {
    margin-bottom: 4pt;
}
.skills p {
    margin: 2pt 0;
}
.pub-list {
    padding-left: 20pt;
}
.pub-list li {
    margin-bottom: 6pt;
}
</style>
</head>
<body>
""")

    # Header
    html.append(f'<h1>{p["name"]}</h1>')
    html.append(f'<p class="tagline">{bio["tagline"]}</p>')
    html.append(f'<p class="contact">{p["location"]} | <a href="mailto:{p["email"]}">{p["email"]}</a> | {p["phone"]} | <a href="{p["github"]}">github.com/ecurtin2</a></p>')

    # Skills
    html.append("<h2>Skills</h2>")
    html.append('<div class="skills">')
    for group in skills.get("groups", []):
        items = [it.get("name", "") for it in filter_included(group.get("items", []), target) if isinstance(it, dict) and it.get("name")]
        if not items:
            continue
        label = group.get("label", "Skills")
        html.append(f'<p><strong>{label}:</strong> {", ".join(items)}</p>')
    html.append("</div>")

    # Experience
    MONTHS = ("", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

    def fmt_date(d):
        if d == "present":
            return "Present"
        if len(d) >= 7:
            return f"{MONTHS[int(d[5:7])]} {d[:4]}"
        return d[:4]

    def fmt_year(d):
        if d == "present":
            return "Present"
        return d[:4]

    def short_role_title(title: str, all_titles: list[str]) -> str:
        suffix = " Applied Scientist"
        if all(t.endswith(suffix) for t in all_titles):
            if title.endswith(suffix):
                return title[: -len(suffix)]
        return title

    html.append("<h2>Experience</h2>")
    for job in filter_included(profile.get("experience", []), target):
        if "roles" in job:
            roles = filter_included(job.get("roles", []), target)
            if not roles:
                continue

            current = next((r for r in roles if r.get("end_date") == "present"), roles[-1])
            prev = [r for r in roles if r is not current]
            all_titles = [r.get("title", "") for r in roles]

            html.append(f'<h3>{current["title"]} – {job["company"]}</h3>')
            html.append(f'<p class="meta">{fmt_year(current["start_date"])} – {fmt_year(current["end_date"])}, {job["location"]}</p>')

            if prev:
                prev_bits = []
                for r in reversed(prev):
                    t = short_role_title(r.get("title", ""), all_titles).strip()
                    prev_bits.append(f'{t} ({fmt_year(r["start_date"])}–{fmt_year(r["end_date"])})')
                html.append(f'<p class="meta">Previously: {" • ".join(prev_bits)}</p>')

            html.append("<ul>")
            for highlight in filter_included(job.get("highlights", []), target):
                html.append(f'<li>{highlight.get("text", "")}</li>')
            html.append("</ul>")
        else:
            start_year = job["start_date"][:4]
            end_year = "Present" if job["end_date"] == "present" else job["end_date"][:4]
            html.append(f'<h3>{job["title"]} – {job["company"]}</h3>')
            html.append(f'<p class="meta">{start_year} – {end_year}, {job["location"]}</p>')
            html.append("<ul>")
            for highlight in filter_included(job.get("highlights", []), target):
                html.append(f'<li>{highlight.get("text", "")}</li>')
            html.append("</ul>")

    # Education
    html.append("<h2>Education</h2>")
    for edu in filter_included(profile.get("education", []), target):
        html.append(f'<h3>{edu["degree"]}, {edu["institution"]}</h3>')
        if "focus" in edu:
            html.append(f'<p>Focus: {edu["focus"]}</p>')
        if "thesis" in edu:
            minor = f'. {edu["minor"]} Minor.' if "minor" in edu else ""
            html.append(f'<p>Thesis: {edu["thesis"]}{minor}</p>')
        if "technologies" in edu:
            html.append(f'<p>Technologies: {", ".join(edu["technologies"])}</p>')

    # Publications
    html.append("<h2>Publications</h2>")
    html.append('<ol class="pub-list">')
    for pub in filter_included(profile.get("publications", []), target):
        authors = ", ".join(pub["authors"])
        title = pub["title"]
        if "doi" in pub:
            title = f'<a href="https://doi.org/{pub["doi"]}">{title}</a>'
        cite = f'{authors}, "{title}," <em>{pub["venue"]}</em>'
        if "volume" in pub:
            cite += f", vol. {pub['volume']}"
        if "issue" in pub:
            cite += f", no. {pub['issue']}"
        if "page" in pub:
            cite += f", p. {pub['page']}"
        if "pages" in pub:
            cite += f", pp. {pub['pages']}"
        cite += f", {pub['year']}."
        html.append(f"<li>{cite}</li>")
    html.append("</ol>")

    html.append("</body></html>")

    print("\n".join(html))


if __name__ == "__main__":
    main()
