from typing import List, Tuple

import nbtlib as nbt
import numpy as np


class Block():
    def __init__(self, blockdata: str):
        self.raw = blockdata
        # minecraft:redstone_wire[east=none,north=side,power=0,south=side,west=none]

    @property
    def type(self) -> str:
        return self.raw.split('[')[0]

    @property
    def properties(self) -> dict:
        properties = {}
        for prop in self.raw.split('[')[1].split(']')[0].split(','):
            key, value = prop.split('=')
            properties[key] = value
        return properties

    @property
    def raw_properties(self) -> str:
        return self.raw.split('[')[1].split(']')[0]

    def __repr__(self) -> str:
        return f'Block({self.raw})'

    def __str__(self) -> str:
        return f'Block({self.raw})'


class Schematic():
    def __init__(self):
        self.raw = None

    def load(self, path: str):
        self.raw = nbt.load(path)
        return self

    @property
    def size(self) -> Tuple[np.short, np.short, np.short]:
        return self.width, self.height, self.length

    @property
    def width(self) -> np.short:
        return np.short(self.raw['Width'])

    @property
    def height(self) -> np.short:
        return np.short(self.raw['Height'])

    @property
    def length(self) -> np.short:
        return np.short(self.raw['Length'])

    @property
    def blocks(self) -> np.ndarray:
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


s = Schematic().load('newblocks.schem')
print(s.blocks)
