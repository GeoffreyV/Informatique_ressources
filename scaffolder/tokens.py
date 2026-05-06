from __future__ import annotations
from pathlib import Path
from typing import Dict
from .util import slug, two_digit
from .types_map import DocType

def base_placeholders() -> Dict[str, str]:
    return {
        "__SEM_CODE__": "",
        "__SEM_TITLE__": "",
        "__SEQ_NUM__": "",
        "__SEQ_TITLE__": "",
        "__T_NUM__": "",
        "__T_TITLE__": "",
        "__DOC_TITLE__": "",
        "__DOC_TYPE__": "",  # tp / td / c / ds / qcm
    }

def merge_tokens(*dicts: Dict[str, str]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for d in dicts:
        out.update(d)
    return out

def tokens_semestre(code: str, title: str) -> Dict[str, str]:
    name_token = {
        "SX": code,
        "SemestreTemplate": slug(title) if title else "Semestre",
    }
    ph = base_placeholders()
    ph["__SEM_CODE__"] = code
    ph["__SEM_TITLE__"] = title or "Semestre"
    ph["__DOC_TITLE__"] = ph["__SEM_TITLE__"]
    return merge_tokens(name_token, ph)

def tokens_sequence(num: int, title: str) -> Dict[str, str]:
    n = two_digit(num)
    name_token = {
        "SeqXX": f"Seq{n}",
        "SemestreTemplate": "Semestre",
        "SequenceTemplate": slug(title) if title else f"Seq{n}",
    }
    ph = base_placeholders()
    ph["__SEQ_NUM__"] = n
    ph["__SEQ_TITLE__"] = title or f"Seq{n}"
    ph["__DOC_TITLE__"] = ph["__SEQ_TITLE__"]
    return merge_tokens(name_token, ph)

def tokens_T(num: int, title: str, doctype: DocType) -> Dict[str, str]:
    n = two_digit(num)
    name_token = {
        "TXX": f"{doctype.prefix}{n}",
        "template": slug(title) if title else f"{doctype.prefix}{n}",
        "TXX_template": f"{doctype.prefix}{n}_{slug(title) if title else doctype.prefix + n}",
    }
    ph = base_placeholders()
    ph["__T_NUM__"] = n
    ph["__T_TITLE__"] = title or f"{doctype.prefix}{n}"
    ph["__DOC_TITLE__"] = ph["__T_TITLE__"]
    ph["__DOC_TYPE__"] = doctype.key
    return merge_tokens(name_token, ph)
