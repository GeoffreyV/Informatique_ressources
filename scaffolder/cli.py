from __future__ import annotations
import argparse
from pathlib import Path
import re
from .util import assert_exists, safe_mkdir, next_index_in
from .core import copy_and_render, choose_T_template
from .tokens import tokens_semestre, tokens_sequence, tokens_T
from .types_map import TYPES, DocType

def cmd_t(args):
    inferred_branch = args.type if args.type else None
    tpl_root = args.templates

    seq_path = args.sequence_path
    assert_exists(seq_path, "séquence cible")

    dtype: DocType = TYPES[args.type]

    if args.auto or args.num is None:
        regex = re.compile(rf"^{dtype.prefix}(\d{{2}})_")
        num = next_index_in(seq_path, regex)
    else:
        num = args.num

    tok = tokens_T(num, args.titre, dtype)
    src = choose_T_template(tpl_root, dtype.prefix, args.titre, inferred_branch)
    assert_exists(src, "modèle T")

    dst = seq_path / f"{tok['TXX_template']}"
    if not args.dry_run:
        safe_mkdir(dst, force=args.force)
    copy_and_render(src, dst, tok, dry_run=args.dry_run)

    generic_tex = dst / "TXX_template.tex"
    if generic_tex.exists():
        main_dst = dst / f"{dtype.prefix}{tok['__T_NUM__']}_{tok['template']}.tex"
        if args.dry_run:
            print(f"[DRY] mv {generic_tex} -> {main_dst}")
        else:
            generic_tex.rename(main_dst)

    print(f"[OK] {dtype.prefix} créé: {dst}")
