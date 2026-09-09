import re
from pathlib import Path

curr_dir = Path(__file__).parent
bib_path = curr_dir / ".." / "tex" / "writing" / "references_main.bib"

tasks = [] # options: "fix_authors", "fix_acronyms"

with open(bib_path, "r", encoding="utf-8") as f:
    content = f.read()

new_content = content

if "fix_authors" in tasks:
    # The regex that finds each BibTeX entry
    institution_pattern = re.compile(
        r"@(?P<type>\w+)\s*\{(?P<key>[^,]+),(?P<body>.*?)\n\}",
        re.DOTALL
    )

    human_types = {"article", "book", "inproceedings", "inbook", "incollection", "techReport"}

    def fix_authors(match):
        entry_type = match.group("type").lower()
        body = match.group("body")
        key = match.group("key")

        # The regex that isolates the author field
        author_pattern = re.compile(
            r"(?P<prefix>\bauthor\s*=\s*)\{(?P<author>[^{}]*)\}",
            re.IGNORECASE
        )

        if entry_type not in human_types:
            # 1. ALLOWED TYPES: Apply the institution check (add double braces {{...}})
            print(f"Fixing institution braces for entry '{entry_type}' with key '{key}'")
            body = author_pattern.sub(
                lambda m: f"{m.group('prefix')}{{{{{m.group('author')}}}}}",
                body,
                count=1
            )
        else:
            # 2. NON-ALLOWED TYPES: Apply the author hyphen check (change - to {-})
            print(f"Fixing hyphenated authors for entry '{entry_type}' with key '{key}'")
            body = author_pattern.sub(
                lambda m: f"{m.group('prefix')}{{{re.sub(r'(?<!\{)-(?!\})', '{-}', m.group('author'))}}}",
                body,
                count=1
            )

        return f"@{match.group('type')}{{{key},{body}\n}}"
    
    new_content = institution_pattern.sub(fix_authors, new_content)

if "fix_acronyms" in tasks:
    acronyms_list = [
        "NEG", "UK", "EU", "CPIH", "GDP",
        "DuckDB", "Gemini 3.1 Pro", "Python", "Copilot"
    ]
    acronyms_pattern = re.compile(
        r"(?<!\{)\b(" + "|".join([re.escape(a) for a in acronyms_list]) + r")\b(?!\})"
    )
    def replace_acronyms_in_title(match):
        prefix = match.group("prefix")
        title_text = match.group("title")
        m_match = match.group(2)
        print(f"Fixing match: '{m_match}' with key '{match.group(0)}'")
        # Replace matched acronyms by wrapping them in braces
        new_title = acronyms_pattern.sub(lambda m: f"{{{m_match}}}", title_text)
        return f"{prefix}{new_title}}}"

    # Target ONLY the title fields, safely ignoring the rest of the entry
    title_field_pattern = re.compile(
        r"(?P<prefix>\btitle\s*=\s*\{)(?P<title>[^{}]*)\}", 
        re.IGNORECASE
    )
    
    new_content = title_field_pattern.sub(replace_acronyms_in_title, new_content)

# Run
with open(bib_path, "w", encoding="utf-8") as f:
    f.write(new_content)