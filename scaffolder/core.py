from __future__ import annotations
from pathlib import Path
from typing import Dict, Optional
import re
import sys
from .util import (
    assert_exists,
    safe_mkdir,
    replace_tokens_in_string,
    should_edit_text_file,
    read_text,
    write_text,
    next_index_in,
    slug,
)

def copy_and_render(src: Path, dst: Path, tokens: Dict[str, str], dry_run: bool = False) -> None:
    if not src.exists():
        sys.exit(f"[ERREUR] Modèle introuvable: {src}")

    for item in src.rglob("*"):
        rel = item.relative_to(src)
        parts = [replace_tokens_in_string(p, tokens) for p in rel.parts]
        target = dst.joinpath(*parts)

        if item.is_dir():
            if dry_run:
                print(f"[DRY] mkdir  {target}")
            else:
                target.mkdir(parents=True, exist_ok=True)
            continue

        if dry_run:
            print(f"[DRY] copy   {item} -> {target}")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            from shutil import copy2
            copy2(item, target)

        if should_edit_text_file(target):
            content = read_text(target)
            if content is not None:
                new_content = replace_tokens_in_string(content, tokens)
                if not dry_run:
                    write_text(target, new_content)

def choose_T_template(tpl_root: Path, doctype_prefix: str, title: str | None, branch: Optional[str]) -> Path:
    roots: list[Path] = []
    if branch:
        b = tpl_root / "branches" / branch
        if b.exists():
            roots.append(b)
    roots.append(tpl_root)

    candidates_rel = []
    if title:
        candidates_rel.append(
            Path("SX_SemestreTemplate") / "SeqXX_SemestreTemplate" / f"{doctype_prefix}XX_{slug(title)}"
        )
    candidates_rel.append(
        Path("SX_SemestreTemplate") / "SeqXX_SemestreTemplate" / f"{doctype_prefix}XX_template"
    )
    candidates_rel.append(
        Path("SX_SemestreTemplate") / "SeqXX_SemestreTemplate" / "TXX_template"
    )

    for root in roots:
        for rel in candidates_rel:
            cand = root / rel
            if cand.exists():
                return cand

    search_info = "\n".join(str(root / r) for root in roots for r in candidates_rel)
    sys.exit(
        "[ERREUR] Aucun modèle trouvé pour ce document.\n"
        "Chemins testés (du plus spécifique au plus générique):\n" + search_info
    )
