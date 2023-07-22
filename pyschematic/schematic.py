from typing import List, Tuple

import nbtlib as nbt
import numpy as np


class Block():
    def __init__(self, blockdata: str):
        """Representation of a block in the Minecraft schematic.

        Args:
            blockdata (str): The raw block data in the format 'block_type[properties]'.
        """
        self.raw = blockdata

    @property
    def type(self) -> str:
        """str: The type of the block without properties."""
        return self.raw.split('[')[0]

    @property
    def properties(self) -> dict:
        """dict: A dictionary containing the properties of the block."""
        properties = {}
        for prop in self.raw.split('[')[1].split(']')[0].split(','):
            key, value = prop.split('=')
            properties[key] = value
        return properties

    @property
    def raw_properties(self) -> str:
        """str: The raw properties of the block without the block type."""
        return self.raw.split('[')[1].split(']')[0]

    def __repr__(self) -> str:
        return f'Block({self.raw})'

    def __str__(self) -> str:
        return f'Block({self.raw})'


class Schematic():
    def __init__(self):
        """Representation of a Minecraft schematic."""
        self.raw = None

    def load(self, path: str):
        """Load the schematic from a file.

        Args:
            path (str): The path to the schematic file.

        Returns:
            Schematic: The current instance of the Schematic class.

        Raises:
            FileNotFoundError: If the file does not exist.
            nbt.lib.MalformedFileError: If the file cannot be loaded due to a parsing error.
        """
        try:
            self.raw = nbt.load(path)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {path}") from e
        except nbt.lib.MalformedFileError as e:
            raise nbt.lib.MalformedFileError(
                f"Error loading schematic: {path}") from e
        return self

    @property
    def size(self) -> Tuple[np.short, np.short, np.short]:
        """Tuple: The size of the schematic in (width, height, length)."""
        return self.width, self.height, self.length

    @property
    def width(self) -> np.short:
        """np.short: The width of the schematic."""
        return np.short(self.raw['Width'])

    @property
    def height(self) -> np.short:
        """np.short: The height of the schematic."""
        return np.short(self.raw['Height'])

    @property
    def length(self) -> np.short:
        """np.short: The length of the schematic."""
        return np.short(self.raw['Length'])

    @property
    def blocks(self) -> np.ndarray:
        """np.ndarray: A 3D numpy array representing the blocks in the schematic."""
        # create list with length of last index
        block_data = np.array(self.raw['BlockData'])
        blocks = np.array([None] * len(block_data))
        palette_inversed = np.array([(Block(blockdata), self.raw['Palette'][blockdata])
                                     for blockdata in self.raw['Palette']])

        for block, id_in_schematic in palette_inversed:
            # get positions of all blocks with id_in_schematic in block_data
            positions = np.where(block_data == id_in_schematic)
            # set all blocks at positions to block
            blocks[positions] = block

        return blocks.reshape(self.width, self.height, self.length)

    @property
    def block_data(self) -> np.ndarray:
        """np.ndarray: A 1D numpy array representing the id of each block within the schematic."""
        return np.array(self.raw['BlockData'])
