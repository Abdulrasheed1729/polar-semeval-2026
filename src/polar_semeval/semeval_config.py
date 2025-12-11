from typing import Literal, Tuple
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

    def to_submission_path(self) -> Tuple[str, str]:
        """Convert the configs to match the required submission file tree"""
        subtask_path = f'subtask_{self.subtask}'
        prediction_file = f'pred_{self.lang_key.value}.csv'

        return subtask_path, prediction_file

