from pathlib import Path

import h5py
import numpy as np

from fastsca.domain.container import Container


class Hdf5Container(Container):

    def __init__(self, path: Path, traces_key='traces'):
        self._path = path
        self._traces_key = traces_key

    def take(self, rows: tuple[int, int]) -> np.ndarray:
        with h5py.File(self._path, 'r') as hf:
            return hf[self._traces_key][rows[0]:rows[1], :]
