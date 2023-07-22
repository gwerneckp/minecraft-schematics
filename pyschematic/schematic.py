from os import strerror
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

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Block):
            return self.raw == __value.raw
        else:
            return False


class Schematic():
    def __init__(self):
        """Representation of a Minecraft schematic."""
        self.raw = None

    def load(self, path: str, force=False):
        """Load the schematic from a file.

        Args:
            path (str): The path to the schematic file.
            force (bool, optional): Force loading the schematic even if it is an incompatible version. Defaults to False. (Not recommended as it may cause unintended errors.)

        Returns:
            Schematic: The current instance of the Schematic class.

        Raises:
            FileNotFoundError: If the file does not exist.
            nbt.lib.MalformedFileError: If the file cannot be loaded due to a parsing error.
            Exception: If the schematic is an incompatible version and force is False.
        """
        try:
            self.raw = nbt.load(path)
            if (not force):
                match self.raw['Version']:
                    case None:
                        raise Exception(
                            "Version not found. This is likely due to an old version of the schematic format which this library does not support. Check out https://github.com/cbs228/nbtschematic for a library that supports version 1.")
                    case 1:
                        raise Exception(
                            "Version 1 is not supported as it is an old version of the schematic format. Check out https://github.com/cbs228/nbtschematic for a library that supports version 1.")
                    case 2:
                        pass
                    case _:
                        raise Exception(
                            f"This library does not fully support the version {self.raw['Version']} of the schematic format. Use force=True to force loading the schematic. This may cause unintended errors.")

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
    def palette(self) -> np.array:
        """A 1D numpy array containing all unique blocks in the schematic.

        The index of each block in the list is the ID of the block in the schematic,
        which can be used to find out which block is at a certain position in block_data.

        Note: It is generally recommended to use the 'blocks' property to access individual blocks with their properties instead of using the palette.

        Returns:
            np.array: An array containing the unique blocks in the schematic.
        """

        result = np.array([None] * len(self.raw['Palette']))
        for blockdata in self.raw['Palette']:
            result[self.raw['Palette'][blockdata]] = Block(blockdata)

        return result
    
    @property
    def palette_max(self) -> np.int8:
        
        # If the palette max is not set, we can infer it from the length of the palette
        return self.raw['PaletteMax'] or len(self.palette)

    @property
    def palette_max(self) -> np.int8:
        """The maximum index value for the block palette in the schematic.

        This value represents the highest ID of a block in the schematic or the number of unique blocks in the schematic's block palette.

        Returns:
            np.int8: The maximum index value for the block palette in the schematic.
        """

        # If the palette max is not set, we can infer it from the length of the palette
        return self.raw['PaletteMax'] or len(self.palette)


    @property
    def offset_x(self) -> np.int8:
        """np.short: The offset of the schematic in the x direction."""
        return np.short(self.raw['Offset'][0])

    @property
    def offset_y(self) -> np.int8:
        """np.short: The offset of the schematic in the y direction."""
        return np.short(self.raw['Offset'][1])

    @property
    def offset_z(self) -> np.int8:
        """np.short: The offset of the schematic in the z direction."""
        return np.short(self.raw['Offset'][2])

    @property
    def offset(self) -> Tuple[np.int8, np.int8, np.int8]:
        """Tuple: The offset of the schematic in (x, y, z)."""
        return self.offset_x, self.offset_y, self.offset_z

    @property
    def metadata(self) -> dict:
        """dict: A dictionary containing the metadata of the schematic."""
        return self.raw['Metadata']

    @property
    def worldedit_offset_x(self) -> np.int8:
        """np.short: The worldedit WEOffsetX of the schematic."""
        return np.int8(self.metadata.get('WEOffsetX'))

    @property
    def worldedit_offset_y(self) -> np.int8:
        """np.short: The worldedit WEOffsetY of the schematic."""
        return np.int8(self.metadata.get('WEOffsetY'))

    @property
    def worldedit_offset_z(self) -> np.int8:
        """np.short: The worldedit WEOffsetZ of the schematic."""
        return np.int8(self.metadata.get('WEOffsetZ'))

    @property
    def worldedit_offset(self) -> Tuple[np.int8, np.int8, np.int8]:
        """Tuple: The worldedit WEOffset of the schematic in (WEOffsetX, WEOffsetY, WEOffsetZ)."""
        return self.worldedit_offset_x, self.worldedit_offset_y, self.worldedit_offset_z
    
    @property
    def data_version(self) -> np.int8:
        """np.int8: The data version of the schematic. This is the ID of the Minecraft version the schematic was created in."""
        return np.int8(self.raw['DataVersion'])