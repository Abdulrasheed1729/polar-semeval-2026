from transformers import Trainer
from typing import Callable
from .semeval_config import SemEvalConfig

class SemEvalTrainer:
    def __init__(self, training_fn: Callable | None = None,
                 trainer: Trainer | None = None,
                 semeval_config: SemEvalConfig | None = None,):
        self.trainer = trainer
        self.config = semeval_config
        self.training_fn = training_fn



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

