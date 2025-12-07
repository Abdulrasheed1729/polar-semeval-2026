import enum
from dataclasses import dataclass
from pathlib import Path
from typing import Literal
from torch.utils.data import Dataset
import numpy as np

import pandas as pd


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
class SemEvalDataset(Dataset):
    """Container for SemEval dataset that auto-loads data on initialization."""
    subtask: Literal[1, 2, 3]
    lang_key: LanguageType =  LanguageType.ENG
    split: Literal["train", "dev"] = "train"
    base_path: Path | str | None = None
    dataframe: pd.DataFrame | None = None
    
    def __post_init__(self):
        """Load dataset automatically after initialization."""
        if self.subtask not in (1, 2, 3):
            raise ValueError(f"Invalid subtask: {self.subtask}")
        
        # Auto-load the dataset
        # base_path = Path(self.base_path)
        if self.base_path == None:
            package_dir = Path(__file__)
            base_path = package_dir / 'datasets/dev_phase'
        else:
            base_path = Path(self.base_path)

        file_path = base_path / f"subtask{self.subtask}" / self.split / f"{self.lang_key.value}.csv"
        
        if not Path(file_path).exists():
            raise FileNotFoundError(f"Dataset file not found: {file_path}")
        
        dataframe = pd.read_csv(file_path)
        self.texts = np.array(dataframe['text'].tolist())






# def load_all_languages(
#     subtask: Literal[1, 2, 3],
#     split: Literal["train", "dev"] = "train",
#     base_path: Path | str = "datasets/dev_phase"
# ) -> dict[LanguageType, SemEvalData]:
#     """
#     Load datasets for all languages for a specific subtask and split.
#
#     Args:
#         subtask: Subtask number (1, 2, or 3)
#         split: Dataset split ("train" or "dev")
#         base_path: Base path to the datasets directory
#
#     Returns:
#         Dictionary mapping LanguageType to SemEvalData objects
#     """
#     datasets = {}
#     for lang in LanguageType:
#         try:
#             datasets[lang] = SemEvalData(subtask=subtask, lang_key=lang, split=split, base_path=base_path)
#         except FileNotFoundError:
#             # Skip languages that don't have data for this subtask/split
#             continue
#
#     return datasets


