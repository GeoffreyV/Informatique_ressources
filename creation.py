#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import shutil
import sys
from pathlib import Path
import re
from typing import Dict, Iterable

TEXT_EXTS = {".tex", ".md", ".txt", ".sty", ".cls", ".bib", ".gitignore"}
DEFAULT_TEMPLATE_ROOT = Path("templates")  # changez si besoin

def slug(s: str) -> str:
    # Nom "propre" pour dossiers: espaces -> _, retire accents simples
    import unicodedata
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^\w\-\.]+", "_", s, flags=re.UNICODE)
    s = re.sub(r"_+", "_", s).strip("_")
    return s

def assert_exists(p: Path, kind="path"):
    if not p.exists():
        sys.exit(f"[ERREUR] {kind} introuvable: {p}")

def safe_mkdir(p: Path, force: bool = False):
    if p.exists():
        if force:
            return
        else:
            sys.exit(f"[ERREUR] Le dossier existe déjà: {p}\n"
                     f"        Utilisez --force ou choisissez un autre nom.")
    p.mkdir(parents=True, exist_ok=True)

def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # binaire ou autre encodage : on ne remplace pas
        return None  # type: ignore # signal: ne pas toucher

def write_text(path: Path, content: str):
    path.write_text(content, encoding="utf-8", newline="\n")

def replace_tokens_in_string(s: str, tokens: Dict[str, str]) -> str:
    # remplace clés entières (pas regex) en ordre décroissant de longueur pour éviter recollisions
    for k in sorted(tokens.keys(), key=len, reverse=True):
        s = s.replace(k, tokens[k])
    return s

def should_edit_text_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTS

def copy_and_render(
    src: Path,
    dst: Path,
    tokens: Dict[str, str],
    dry_run: bool = False,
):
    """
    Copie un arbre en remplaçant les jetons dans noms ET contenus texte.
    """
    if not src.exists():
        sys.exit(f"[ERREUR] Modèle introuvable: {src}")

    for item in src.rglob("*"):
        rel = item.relative_to(src)

        # Remplacements de jetons sur chaque segment du chemin
        parts = [replace_tokens_in_string(p, tokens) for p in rel.parts]
        target = dst.joinpath(*parts)

        if item.is_dir():
            if dry_run:
                print(f"[DRY] mkdir  {target}")
            else:
                target.mkdir(parents=True, exist_ok=True)
            continue

        # Fichier
        if dry_run:
            print(f"[DRY] copy   {item} -> {target}")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, target)

        # Remplacement dans le contenu si texte
        if should_edit_text_file(target):
            content = read_text(target)
            if content is not None:
                new_content = replace_tokens_in_string(content, tokens)
                if not dry_run:
                    write_text(target, new_content)

def two_digit(n: int) -> str:
    if n < 0 or n > 99:
        sys.exit("[ERREUR] Les indices attendus sont entre 0 et 99.")
    return f"{n:02d}"

def gather_tokens_for_semestre(code: str, title: str) -> Dict[str, str]:
    # SX -> S1, etc.
    return {
        "SX": code,
        "SemestreTemplate": slug(title) if title else "Semestre",
    }

def gather_tokens_for_sequence(seq: int, title: str) -> Dict[str, str]:
    n = two_digit(seq)
    return {
        "SeqXX": f"Seq{n}",
        "SemestreTemplate": "Semestre",  # utile si présent dans noms
        "SequenceTemplate": slug(title) if title else f"Seq{n}",
    }

def gather_tokens_for_tp(tp: int, title: str) -> Dict[str, str]:
    n = two_digit(tp)
    return {
        "TPXX": f"TP{n}",
        "TPTemplate": slug(title) if title else f"TP{n}",
    }

def gather_tokens_for_cours(num: int, title: str) -> Dict[str, str]:
    n = two_digit(num)
    return {
        "CoursXX": f"Cours{n}",
        "CoursTemplate": slug(title) if title else f"Cours{n}",
    }

def gather_tokens_for_td(num: int, title: str) -> Dict[str, str]:
    n = two_digit(num)
    return {
        "TDXX": f"TD{n}",
        "TDTemplate": slug(title) if title else f"TD{n}",
    }

def parse_args():
    p = argparse.ArgumentParser(
        description="Générateur d'ossatures (Semestre / Séquence / TP / Cours / TD) pour LaTeX."
    )
    p.add_argument("--templates", type=Path, default=DEFAULT_TEMPLATE_ROOT,
                   help="Racine des modèles (par défaut: ./templates)")
    p.add_argument("--dest", type=Path, default=Path.cwd(),
                   help="Dossier de destination (par défaut: dossier courant)")
    p.add_argument("--dry-run", action="store_true", help="Afficher sans écrire")
    p.add_argument("--force", action="store_true", help="Ne pas arrêter si dossiers existent déjà")

    sub = p.add_subparsers(dest="cmd", required=True)

    # semestre
    sp = sub.add_parser("semestre", help="Créer un semestre à partir de SX_SemestreTemplate")
    sp.add_argument("code", help="Code semestre (ex: S1, S2, S3...)")
    sp.add_argument("titre", nargs="?", default="", help="Nom lisible du semestre (optionnel)")

    # sequence
    sq = sub.add_parser("sequence", help="Créer une séquence dans un semestre")
    sq.add_argument("semestre_path", type=Path, help="Chemin du semestre cible (ex: S1_GEII/)")
    sq.add_argument("num", type=int, help="Numéro de séquence (ex: 1)")
    sq.add_argument("titre", nargs="?", default="", help="Titre de séquence (optionnel)")

    # tp
    tp = sub.add_parser("tp", help="Créer un TP dans une séquence")
    tp.add_argument("sequence_path", type=Path, help="Chemin de la séquence cible (ex: S1/Seq01_Intro/)")
    tp.add_argument("num", type=int, help="Numéro de TP (ex: 1)")
    tp.add_argument("titre", nargs="?", default="", help="Titre de TP (optionnel)")

    # cours
    cr = sub.add_parser("cours", help="Créer un Cours dans une séquence")
    cr.add_argument("sequence_path", type=Path, help="Chemin de la séquence cible")
    cr.add_argument("num", type=int, help="Numéro de Cours")
    cr.add_argument("titre", nargs="?", default="", help="Titre de Cours (optionnel)")

    # td
    td = sub.add_parser("td", help="Créer un TD dans une séquence")
    td.add_argument("sequence_path", type=Path, help="Chemin de la séquence cible")
    td.add_argument("num", type=int, help="Numéro de TD")
    td.add_argument("titre", nargs="?", default="", help="Titre de TD (optionnel)")

    return p.parse_args()

def main():
    args = parse_args()
    tpl_root = args.templates
    dest_root = args.dest
    assert_exists(tpl_root, "templates")

    if args.cmd == "semestre":
        # Dossier modèle : SX_SemestreTemplate
        src = tpl_root / "SX_SemestreTemplate"
        assert_exists(src, "modèle semestre")
        tokens = gather_tokens_for_semestre(args.code, args.titre)
        dst_name = f"{tokens['SX']}_{tokens['SemestreTemplate']}"
        dst = dest_root / dst_name
        if not args.dry_run:
            safe_mkdir(dst, force=args.force)
        copy_and_render(src, dst, tokens, dry_run=args.dry_run)
        print(f"[OK] Semestre créé: {dst}")

    elif args.cmd == "sequence":
        src = tpl_root / "SX_SemestreTemplate" / "SeqXX_SemestreTemplate"
        assert_exists(src, "modèle séquence")
        sem_path = args.semestre_path
        assert_exists(sem_path, "semestre cible")
        tokens = gather_tokens_for_sequence(args.num, args.titre)
        dst_name = f"{tokens['SeqXX']}_{tokens['SequenceTemplate']}"
        dst = sem_path / dst_name
        if not args.dry_run:
            safe_mkdir(dst, force=args.force)
        copy_and_render(src, dst, tokens, dry_run=args.dry_run)
        print(f"[OK] Séquence créée: {dst}")

    elif args.cmd == "tp":
        src = tpl_root / "SX_SemestreTemplate" / "SeqXX_SemestreTemplate" / "TPXX_TPTemplate"
        assert_exists(src, "modèle TP")
        seq_path = args.sequence_path
        assert_exists(seq_path, "séquence cible")
        tokens = gather_tokens_for_tp(args.num, args.titre)
        dst_name = f"{tokens['TPXX']}_{tokens['TPTemplate']}"
        dst = seq_path / dst_name
        if not args.dry_run:
            safe_mkdir(dst, force=args.force)
        copy_and_render(src, dst, tokens, dry_run=args.dry_run)
        print(f"[OK] TP créé: {dst}")

    elif args.cmd == "cours":
        # Vous pouvez créer un modèle "CoursXX_CoursTemplate" dans SeqXX si besoin.
        src = (tpl_root / "CoursXX_CoursTemplate")
        if not src.exists():
            print("[INFO] Aucun modèle de cours dédié trouvé. Création d’un dossier simple.")
            # fallback: dossier + fichier .tex minimal
            seq_path = args.sequence_path
            assert_exists(seq_path, "séquence cible")
            tokens = gather_tokens_for_cours(args.num, args.titre)
            dst = seq_path / f"{tokens['CoursXX']}_{tokens['CoursTemplate']}"
            if args.dry_run:
                print(f"[DRY] mkdir  {dst}")
                print(f"[DRY] write {dst/(tokens['CoursXX'] + '.tex')}")
            else:
                dst.mkdir(parents=True, exist_ok=True)
                tex_name = f"{tokens['CoursXX']}.tex"
                (dst / "sources").mkdir(exist_ok=True)
                write_text(dst / tex_name, f"\\documentclass{{article}}\n\\input{{../preamble.tex}}\n\\begin{{document}}\n\\section*{{{tokens['CoursTemplate']}}}\nContenu…\n\\end{{document}}\n")
            print(f"[OK] Cours créé: {dst}")
        else:
            seq_path = args.sequence_path
            assert_exists(seq_path, "séquence cible")
            tokens = gather_tokens_for_cours(args.num, args.titre)
            dst = seq_path / f"{tokens['CoursXX']}_{tokens['CoursTemplate']}"
            if not args.dry_run:
                safe_mkdir(dst, force=args.force)
            copy_and_render(src, dst, tokens, dry_run=args.dry_run)
            print(f"[OK] Cours créé: {dst}")

    elif args.cmd == "td":
        src = (tpl_root / "TDXX_TDTemplate")
        if not src.exists():
            print("[INFO] Aucun modèle de TD dédié trouvé. Création d’un dossier simple.")
            seq_path = args.sequence_path
            assert_exists(seq_path, "séquence cible")
            tokens = gather_tokens_for_td(args.num, args.titre)
            dst = seq_path / f"{tokens['TDXX']}_{tokens['TDTemplate']}"
            if args.dry_run:
                print(f"[DRY] mkdir  {dst}")
                print(f"[DRY] write {dst/(tokens['TDXX'] + '.tex')}")
            else:
                dst.mkdir(parents=True, exist_ok=True)
                tex_name = f"{tokens['TDXX']}.tex"
                (dst / "sources").mkdir(exist_ok=True)
                write_text(dst / tex_name, f"\\documentclass{{article}}\n\\input{{../preamble.tex}}\n\\begin{{document}}\n\\section*{{{tokens['TDTemplate']}}}\nExercices…\n\\end{{document}}\n")
            print(f"[OK] TD créé: {dst}")
        else:
            seq_path = args.sequence_path
            assert_exists(seq_path, "séquence cible")
            tokens = gather_tokens_for_td(args.num, args.titre)
            dst = seq_path / f"{tokens['TDXX']}_{tokens['TDTemplate']}"
            if not args.dry_run:
                safe_mkdir(dst, force=args.force)
            copy_and_render(src, dst, tokens, dry_run=args.dry_run)
            print(f"[OK] TD créé: {dst}")

if __name__ == "__main__":
    main()
