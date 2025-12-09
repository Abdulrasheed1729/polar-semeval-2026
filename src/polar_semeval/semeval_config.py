from typing import Literal
from dataclasses import dataclass
import enum

class LanguageType(enum.Enum):
    AMH = "amh"
    ARB = "arb"
    BEN = "ben"
    DEU = "deu"
    ENG = "eng"
    FAS = "fas"
    HAU = "hau"
    HIN = "hin"
    ITA = "ita"
    KHM = "khm"
    MYA = "mya"
    NEP = "nep"
    ORI = "ori"
    PAN = "pan"
    POL = "pol"
    RUS = "rus"
    SPA = "spa"
    SWA = "swa"
    TEL = "tel"
    TUR = "tur"
    URD = "urd"
    ZHO = "zho"


@dataclass
class SemEvalConfig:
    subtask: Literal[1, 2, 3]
    lang_key: LanguageType = LanguageType.ENG

