from abc import ABC, abstractmethod

import numpy as np


class Container(ABC):
    @abstractmethod
    def take(self, rows: tuple[int, int]) -> np.ndarray:
        pass
