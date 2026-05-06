from dataclasses import dataclass

@dataclass(frozen=True)
class DocType:
    key: str      # 'tp', 'td', 'c', 'ds', 'qcm'
    prefix: str   # 'TP', 'TD', 'C', 'DS', 'QCM'

TYPES = {
    "tp": DocType("tp", "TP"),
    "td": DocType("td", "TD"),
    "c":  DocType("c",  "C"),
    "ds": DocType("ds", "DS"),
    "qcm":DocType("qcm","QCM"),
}
