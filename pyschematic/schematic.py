from typing import List, Tuple

import nbtlib as nbt
import numpy as np


class Block():
    def __init__(self, blockdata: str):
        """Representation of a block in the Minecraft schematic.

        Args:
            blockdata (str): The raw block data in the format 'block_type[properties]'.
        """

    @property
    def type(self) -> str:
        """str: The type of the block without properties."""

    @property
    def properties(self) -> dict:
        """dict: A dictionary containing the properties of the block."""

    @property
    def raw_properties(self) -> str:
        """str: The raw properties of the block without the block type."""

    def __repr__(self) -> str:
        """Return a string representation of the block."""

    def __str__(self) -> str:
        """Return a human-readable string representation of the block."""


class Schematic():
    def __init__(self):
        """Representation of a Minecraft schematic."""

    def load(self, path: str):
        """Load the schematic from a file.

        Args:
            path (str): The path to the schematic file.

        Returns:
            Schematic: The current instance of the Schematic class.
        """

    @property
    def size(self) -> Tuple[np.short, np.short, np.short]:
        """Tuple: The size of the schematic in (width, height, length)."""

    @property
    def width(self) -> np.short:
        """np.short: The width of the schematic."""

    @property
    def height(self) -> np.short:
        """np.short: The height of the schematic."""

    @property
    def length(self) -> np.short:
        """np.short: The length of the schematic."""

    @property
    def blocks(self) -> np.ndarray:
        """np.ndarray: A 3D numpy array representing the blocks in the schematic."""
