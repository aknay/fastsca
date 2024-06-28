import os
from pathlib import Path

from fastsca.data.containers.hdf5_container import Hdf5Container
from fastsca.domain.container import Container

dirPath = os.path.dirname(os.path.realpath(__file__))


def get_aes128_arduino_uno_project_container() -> Container:
    return Hdf5Container(Path(f'{dirPath}/aes128_arduino_uno/aes128_arduino_uno.sx'))
