from __future__ import annotations
from pathlib import Path
import re
import sys
import unicodedata
from typing import Dict, Optional

TEXT_EXTS = {".tex", ".md", ".txt", ".sty", ".cls", ".bib", ".gitignore"}

def slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^\w\-\.]+", "_", s, flags=re.UNICODE)
    s = re.sub(r"_+", "_", s).strip("_")
    return s

def assert_exists(p: Path, kind: str = "path") -> None:
    if not p.exists():
        sys.exit(f"[ERREUR] {kind} introuvable: {p}")

def safe_mkdir(p: Path, force: bool = False) -> None:
    if p.exists():
        if force:
            return
        sys.exit(f"[ERREUR] Le dossier existe déjà: {p}\n        Utilisez --force ou choisissez un autre nom.")
    p.mkdir(parents=True, exist_ok=True)

def read_text(path: Path) -> Optional[str]:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None

def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8", newline="\n")

def replace_tokens_in_string(s: str, tokens: Dict[str, str]) -> str:
    for k in sorted(tokens.keys(), key=len, reverse=True):
        s = s.replace(k, tokens[k])
    return s

def should_edit_text_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTS

def two_digit(n: int) -> str:
    if n < 0 or n > 99:
        sys.exit("[ERREUR] Les indices attendus sont entre 0 et 99.")
    return f"{n:02d}"

def next_index_in(parent: Path, regex: re.Pattern[str]) -> int:
    max_n = 0
    if not parent.exists():
        return 1
    for child in parent.iterdir():
        if not child.is_dir():
            continue
        m = regex.match(child.name)
        if m:
            try:
                n = int(m.group(1))
                if n > max_n:
                    max_n = n
            except ValueError:
                pass
    return max_n + 1 if max_n >= 0 else 1
