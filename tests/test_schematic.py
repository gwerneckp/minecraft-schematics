# tests/test_minecraft_schematic.py

from os import path

import nbtlib as nbt
import numpy as np

from pyschematic import Block, Schematic

# Test data
all_blocks = 'newblocks.schem'
all_blocks_directory = path.join(path.dirname(__file__), "schematics", all_blocks)

# Block class tests


def test_block_type():
    block_data = "minecraft:redstone_wire[east=none,north=side,power=0,south=side,west=none]"
    block = Block(block_data)
    assert block.type == "minecraft:redstone_wire"

def test_block_properties():
    block_data = "minecraft:redstone_wire[east=none,north=side,power=0,south=side,west=none]"
    block = Block(block_data)
    properties = block.properties
    assert properties == {
        "east": "none",
        "north": "side",
        "power": "0",
        "south": "side",
        "west": "none"
    }

def test_block_raw_properties():
    block_data = "minecraft:redstone_wire[east=none,north=side,power=0,south=side,west=none]"
    block = Block(block_data)
    assert block.raw_properties == "east=none,north=side,power=0,south=side,west=none"

# Schematic class tests
def test_schematic_load():
    schematic = Schematic().load(all_blocks_directory)
    assert isinstance(schematic.raw, nbt.Compound)

def test_schematic_blocks_shape():
    schematic = Schematic().load(all_blocks_directory)
    schematicnbt = nbt.load(all_blocks_directory)
    expected_width = schematicnbt["Width"]
    expected_height = schematicnbt["Height"]
    expected_length = schematicnbt["Length"]

    blocks = schematic.blocks
    assert blocks.shape == (expected_width, expected_height, expected_length)

def test_schematic_blocks():
    schematic = Schematic().load(all_blocks_directory)
    print(schematic.blocks)
    assert schematic.blocks[0, 0, 0] == Block("minecraft:packed_ice")