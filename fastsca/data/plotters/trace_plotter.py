from typing import Union

import matplotlib.pyplot as plt

from fastsca.data.containers.hdf5_container import Hdf5Container
from fastsca.domain.plotter import Plotter


class TracePlotter(Plotter):

    def __init__(self, container: Hdf5Container):
        self._container = container

    def plot(self, value:  Union[int, tuple[int, int]]):
        if isinstance(value, int):
            ar = self._container.take(rows=(value, value+1))
        elif isinstance(value, tuple) and len(value) == 2 and all(isinstance(item, int) for item in value):
            ar = self._container.take(rows=value)
        else:
            assert False, 'wrong value type'
        plt.plot(ar.T)
        plt.show()
