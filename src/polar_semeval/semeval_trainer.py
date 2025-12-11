from transformers import Trainer
from typing import Callable
from .semeval_config import SemEvalConfig
import pandas as pd

import os
import zipfile

class SemEvalTrainer:
    def __init__(self, training_fn: Callable | None = None,
                 trainer: Trainer | None = None,
                 semeval_config: SemEvalConfig | None = None,):
        self.trainer = trainer
        self.config = semeval_config
        self.training_fn = training_fn

    def _zipdir(self, path, ziph):
    # ziph is zipfile handle
        for root, _, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file), 
                           os.path.relpath(os.path.join(root, file), 
                                           os.path.join(path, '..')))


    def train(self):
        if self.training_fn is not None:
            self.training_fn(self.trainer)

        else:
            raise Exception("Type None is not callable")

    def evaluate(self) -> dict[str, float]:
        if self.trainer is not None:
            eval_results = self.trainer.evaluate()
            return eval_results
        else:
            raise Exception("No trainer initialised")

    def save_predictions(self,semeval_config: SemEvalConfig, dataframe: pd.DataFrame):
        subtask_path, prediction_file = semeval_config.to_submission_path()
         

        if not os.path.exists(subtask_path):
            os.mkdir(subtask_path)

        try:

            dataframe.to_csv(f'{subtask_path}/{prediction_file}')
        except Exception:
            print(f'Error creating {prediction_file}')
            


    def prepare_for_submission(self, semeval_config: SemEvalConfig) -> None:
        try:
            subtask_path, _  = semeval_config.to_submission_path()

            with zipfile.ZipFile(f'subtask_{semeval_config.subtask}.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
                self._zipdir(subtask_path, zipf)

        except Exception:
            print(f'Error archiving for subtask {semeval_config.subtask}')




