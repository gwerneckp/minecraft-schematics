from abc import ABC, abstractmethod
from typing import Tuple
import numpy as np


class SchematicSchema(ABC):
    def __init__(self):
        """Representation of a Minecraft schematic."""
        self.raw = None

    @property
    @abstractmethod
    def size(self) -> Tuple[np.short, np.short, np.short]:
        """The size of the schematic in (width, height, length)."""
        pass

    @property
    @abstractmethod
    def width(self) -> np.short:
        """The width of the schematic."""
        pass

    @property
    @abstractmethod
    def height(self) -> np.short:
        """The height of the schematic."""
        pass

    @property
    @abstractmethod
    def length(self) -> np.short:
        """The length of the schematic."""
        pass

    @property
    @abstractmethod
    def blocks(self):
        """A 3D numpy array representing the blocks in the schematic."""
        pass

    @property
    @abstractmethod
    def block_entities(self):
        """Get a list of all block entities in the schematic."""
        pass

    @property
    @abstractmethod
    def offset_x(self):
        """The offset of the schematic in the x direction."""
        pass

    @property
    @abstractmethod
    def offset_y(self):
        """The offset of the schematic in the y direction."""
        pass

    @property
    @abstractmethod
    def offset_z(self):
        """The offset of the schematic in the z direction."""
        pass

    @property
    @abstractmethod
    def offset(self):
        """The offset of the schematic in (x, y, z)."""
        pass

    @property
    @abstractmethod
    def metadata(self):
        """A dictionary containing the metadata of the schematic."""
        pass

    @property
    @abstractmethod
    def data_version(self):
        """The data version of the schematic."""
        pass
