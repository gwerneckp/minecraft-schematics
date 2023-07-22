# tests/test_minecraft_schematic.py

from os import path
import json
import nbtlib as nbt
import numpy as np

from pyschematic import Block, Schematic

# Test data
all_blocks = 'newblocks.schem'
all_blocks_directory = path.join(
    path.dirname(__file__), "schematics", all_blocks)

house = 'house.schem'
house_directory = path.join(path.dirname(__file__), "schematics", house)

block_entities = 'block_entities_test.schem'
block_entities_directory = path.join(
    path.dirname(__file__), "schematics", block_entities)

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


def test_offset():
    schematic = Schematic().load(house_directory)
    assert schematic.offset == (-6, 36, 24)


def test_worldedit_offset():
    schematic = Schematic().load(house_directory)
    assert schematic.worldedit_offset == (-10, -1, 8)


def test_palette():
    schematic = Schematic().load(house_directory)
    assert schematic.palette[0] == Block("minecraft:water[level=0]")


def test_palette_max():
    schematic = Schematic().load(house_directory)
    assert schematic.palette_max == 69


def test_block_entities():
    schematic = Schematic().load(block_entities_directory)
    assert json.loads(schematic.block_entities[0]['front_text']['messages'][1])['text'] == 'Hello world'
