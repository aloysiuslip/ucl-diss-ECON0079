# Traverse tex/writing/references-main.bib
# For any entry which is not [article, book, inproceedings, inbook, incollection]
# check the author field
# If the author field is in a single brace {} then modify it to be in double braces {{}}

import os
import re
from pathlib import Path

curr_dir = Path(__file__).parent
bib_path = curr_dir / ".." / "tex" / "writing" / "references_main.bib"

allowed_types = {"article", "book", "inproceedings", "inbook", "incollection"}

with open(bib_path, "r", encoding="utf-8") as f:
    content = f.read()

# Match each BibTeX entry
entry_pattern = re.compile(
    r"@(?P<type>\w+)\s*\{(?P<key>[^,]+),(?P<body>.*?)\n\}",
    re.DOTALL
)

def fix_entry(match):
    entry_type = match.group("type").lower()
    body = match.group("body")

    if entry_type in allowed_types:
        return match.group(0)

    # Match an author field whose entire value is enclosed in a single pair
    # of braces, e.g. author = {John Smith}
    print(f"Fixing entry of type '{entry_type}' with key '{match.group('key')}'")
    author_pattern = re.compile(
        r"(?P<prefix>\bauthor\s*=\s*)\{(?P<author>[^{}]*)\}",
        re.IGNORECASE
    )

    body = author_pattern.sub(
        lambda m: f"{m.group('prefix')}{{{{{m.group('author')}}}}}",
        body,
        count=1
    )

    return f"@{match.group('type')}{{{match.group('key')},{body}\n}}"


new_content = entry_pattern.sub(fix_entry, content)

with open(bib_path, "w", encoding="utf-8") as f:
    f.write(new_content)
