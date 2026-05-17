#!/usr/bin/env python3
"""
Atomize Marethar EN: split entity H3 sections into individual files.
Merges part2 overview + part5 deep lore per entity.
"""
import re
import shutil
from pathlib import Path

BASE = Path("C:/Users/utente/Documents/GitHub/marethar_en")


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def extract_h3_sections(filepath):
    """
    Parse a markdown file and extract all H3 sections.
    Returns:
      pre_content: text before the first H3
      sections: OrderedDict of {h3_title: body_without_h3_header}
    """
    content = read_file(filepath)
    lines = content.split("\n")

    pre_lines = []
    sections = {}
    section_order = []
    current_title = None
    current_lines = []
    in_h3 = False

    for line in lines:
        # Match H3 but not H4
        if re.match(r"^### [^#]", line):
            if current_title is not None:
                body = "\n".join(current_lines).strip()
                # Strip trailing --- separator
                body = re.sub(r"\n---\s*$", "", body).strip()
                sections[current_title] = body
            current_title = line[4:].strip()
            section_order.append(current_title)
            current_lines = []
            in_h3 = True
        elif not in_h3:
            pre_lines.append(line)
        else:
            current_lines.append(line)

    if current_title is not None:
        body = "\n".join(current_lines).strip()
        body = re.sub(r"\n---\s*$", "", body).strip()
        sections[current_title] = body

    pre_content = "\n".join(pre_lines).strip()
    return pre_content, sections, section_order


def demote_h4_to_h2(content):
    """Demote #### headers to ## in content."""
    lines = content.split("\n")
    result = []
    for line in lines:
        if line.startswith("#### "):
            line = "## " + line[5:]
        result.append(line)
    return "\n".join(result)


def extract_subtitle(body):
    """Extract italic subtitle from first line of body if present."""
    lines = body.split("\n")
    if lines and re.match(r"^\*[^*].+[^*]\*$", lines[0].strip()):
        subtitle = lines[0].strip()
        rest = "\n".join(lines[1:]).strip()
        return subtitle, rest
    return None, body


def build_entity_file(display_name, p2_body, p5_body, extended_section_title="## Extended Profile"):
    """Build merged entity file content."""
    subtitle, p2_body = extract_subtitle(p2_body)
    p2_body = demote_h4_to_h2(p2_body)

    content = f"# {display_name}\n\n"
    if subtitle:
        content += f"{subtitle}\n\n"
    content += p2_body.strip()
    if p5_body and p5_body.strip():
        content += f"\n\n---\n\n{extended_section_title}\n\n"
        content += p5_body.strip()
    content += "\n"
    return content


# ============================================================
# CULTURES
# ============================================================

CULTURE_MAP = [
    # (p2_title, p5_title, display_name, filename)
    ("Aridonians",   "Aridonia",   "Aridonians",   "aridonians.md"),
    ("Aurelians",    "Aurelia",    "Aurelians",     "aurelians.md"),
    ("Lysandrians",  "Lysandria",  "Lysandrians",   "lysandrians.md"),
    ("Orethians",    "Orethia",    "Orethians",     "orethians.md"),
    ("Thalassians",  "Thalassia",  "Thalassians",   "thalassians.md"),
    ("Naharim",      "Naharim",    "Naharim",       "naharim.md"),
]


def build_cultures():
    print("\n=== Cultures ===")
    _, p2_secs, _ = extract_h3_sections(BASE / "en/part2/02_culture.md")
    _, p5_secs, _ = extract_h3_sections(BASE / "en/part5/01_culture.md")
    out_dir = BASE / "en/cultures"

    for p2_name, p5_name, display_name, filename in CULTURE_MAP:
        p2_body = p2_secs.get(p2_name, "")
        p5_body = p5_secs.get(p5_name, "")
        content = build_entity_file(display_name, p2_body, p5_body)
        write_file(out_dir / filename, content)
        print(f"  + en/cultures/{filename}")


# ============================================================
# NATIONS
# ============================================================

NATION_MAP = [
    # (p2_title, p5_title, display_name, filename)
    ("The Republic of Premia",      "Republic of Premia",      "Republic of Premia",      "republic-of-premia.md"),
    ("The Diarchy of Ashania",      "Diarchy of Ashania",      "Diarchy of Ashania",      "diarchy-of-ashania.md"),
    ("The Empire of Linia",         "Empire of Linia",         "Empire of Linia",         "empire-of-linia.md"),
    ("The Republic of Meshdad",     "Republic of Meshdad",     "Republic of Meshdad",     "republic-of-meshdad.md"),
    ("The Grand Duchy of Hamania",  "Grand Duchy of Hamania",  "Grand Duchy of Hamania",  "grand-duchy-of-hamania.md"),
    ("The City-State of Allasia",   "City-State of Allasia",   "City-State of Allasia",   "city-state-of-allasia.md"),
    ("The Rashian Empire",          "Rashian Empire",          "Rashian Empire",           "rashian-empire.md"),
    ("The Kingdom of Vallan",       "Kingdom of Vallan",       "Kingdom of Vallan",        "kingdom-of-vallan.md"),
    ("The Empire of Doria",         "Dorian Empire",           "Empire of Doria",          "empire-of-doria.md"),
    ("The Principality of Dajilia", "Principality of Dajilia", "Principality of Dajilia",  "principality-of-dajilia.md"),
    ("The Rhithian League",         "Rhithian League",         "Rhithian League",          "rhithian-league.md"),
]


def build_nations():
    print("\n=== Nations ===")
    _, p2_secs, _ = extract_h3_sections(BASE / "en/part2/05_nations.md")
    _, p5_secs, _ = extract_h3_sections(BASE / "en/part5/02_nations.md")
    out_dir = BASE / "en/nations"

    for p2_name, p5_name, display_name, filename in NATION_MAP:
        p2_body = p2_secs.get(p2_name, "")
        p5_body = p5_secs.get(p5_name, "")
        content = build_entity_file(display_name, p2_body, p5_body, "## Detailed Data")
        write_file(out_dir / filename, content)
        print(f"  + en/nations/{filename}")

    # Nations Relations Matrix
    matrix_body = p5_secs.get("Nations Relations Matrix", "")
    if matrix_body:
        content = f"# Nations Relations Matrix\n\n{matrix_body.strip()}\n"
        write_file(out_dir / "nations-relations.md", content)
        print("  + en/nations/nations-relations.md")


# ============================================================
# RELIGIONS
# ============================================================

RELIGION_MAP = [
    # (p2_title, p5_title, display_name, filename)
    ("The Sect of Shahin",               "Sect of Shahin",       "Sect of Shahin",       "sect-of-shahin.md"),
    ("The Faith of Shemshahva",          "Faith of Shemshahva",  "Faith of Shemshahva",  "faith-of-shemshahva.md"),
    ("The Cult of Carthara",             "Cult of Carthara",     "Cult of Carthara",      "cult-of-carthara.md"),
    ("The Golat Tradition",              "Golat Tradition",      "Golat Tradition",        "golat-tradition.md"),
    ("The Gods of Ralertis",             "Gods of Ralertis",     "Gods of Ralertis",       "gods-of-ralertis.md"),
    ("The Spirits of Thalaran",          "Spirits of Thalaran",  "Spirits of Thalaran",   "spirits-of-thalaran.md"),
    ("The Druidic Orders of Dimilalica", "Druids of Dimilalica", "Druidic Orders of Dimilalica", "druids-of-dimilalica.md"),
]

RELIGION_P5_ONLY = [
    ("Marethan Atheism",        "Marethan Atheism",        "marethan-atheism.md"),
    ("Faith of Pulbium",        "Faith of Pulbium",        "faith-of-pulbium.md"),
    ("Faith of Tudeshkhast",    "Faith of Tudeshkhast",    "faith-of-tudeshkhast.md"),
    ("Sect of the Victory Bull","Sect of the Victory Bull","sect-of-the-victory-bull.md"),
]

RELIGION_CROSS_CUTTING = [
    ("Heresies, Syncretisms, Alternative Currents", "heresies-and-syncretisms.md"),
    ("What Is True, and for Whom?",                  "what-is-true.md"),
]


def build_religions():
    print("\n=== Religions ===")
    _, p2_secs, _ = extract_h3_sections(BASE / "en/part2/03_religions.md")
    _, p5_secs, _ = extract_h3_sections(BASE / "en/part5/03_religions.md")
    out_dir = BASE / "en/religions"

    for p2_name, p5_name, display_name, filename in RELIGION_MAP:
        p2_body = p2_secs.get(p2_name, "")
        p5_body = p5_secs.get(p5_name, "")
        content = build_entity_file(display_name, p2_body, p5_body)
        write_file(out_dir / filename, content)
        print(f"  + en/religions/{filename}")

    for p5_name, display_name, filename in RELIGION_P5_ONLY:
        p5_body = p5_secs.get(p5_name, "")
        if p5_body:
            content = f"# {display_name}\n\n{p5_body.strip()}\n"
            write_file(out_dir / filename, content)
            print(f"  + en/religions/{filename}")

    for p2_name, filename in RELIGION_CROSS_CUTTING:
        body = p2_secs.get(p2_name, "")
        if body:
            # Demote #### to ## in cross-cutting sections too
            body = demote_h4_to_h2(body)
            content = f"# {p2_name}\n\n{body.strip()}\n"
            write_file(out_dir / filename, content)
            print(f"  + en/religions/{filename}")


# ============================================================
# RELICS
# ============================================================

RELIC_SKIP = {"How to Use Them in Play"}


def build_relics():
    print("\n=== Relics ===")
    pre_content, sections, order = extract_h3_sections(BASE / "en/part3/02_relics.md")
    out_dir = BASE / "en/relics"

    for title in order:
        body = sections[title]
        if title in RELIC_SKIP:
            content = f"# {title}\n\n{body.strip()}\n"
            write_file(out_dir / "relics-how-to-use.md", content)
            print("  + en/relics/relics-how-to-use.md")
        else:
            slug = re.sub(r"[^a-z0-9\s]", "", title.lower())
            slug = re.sub(r"\s+", "-", slug.strip())
            filename = slug + ".md"
            content = f"# {title}\n\n{body.strip()}\n"
            write_file(out_dir / filename, content)
            print(f"  + en/relics/{filename}")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    build_cultures()
    build_nations()
    build_religions()
    build_relics()
    print("\nDone! 40 entity files created.")
