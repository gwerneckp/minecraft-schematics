# PySchematic - Minecraft Schematic Library

PySchematic is a Python library for working with Minecraft schematic files. It provides a simple and convenient way to read and process schematic files used in Minecraft.

The library is based on the Minecraft Schematic format version 2.

## Features

- Load Minecraft schematic files (.schematic) and read their contents.
- Access schematic size and dimensions (width, height, length).
- Get block data as a 3D numpy array representing the blocks in the schematic.
- Access individual blocks' information, including type and properties.

## Installation

To install PySchematic, you can use pip:

```bash
pip install pyschematic
```

## Usage

Here's a quick guide on how to use the PySchematic library:

### Schematic Class

The `Schematic` class is the main class of the library. It is used to load schematic files with the `load` method and access the schematic's data.

```python
from pyschematic import Schematic

schematic = Schematic().load('path/to/your/schematic_file.schematic')

print(schematic.size)     # Output: (3, 4, 5)
print(schematic.width)    # Output: 3
print(schematic.height)   # Output: 4
print(schematic.length)   # Output: 5

# Get block data as a 3D numpy array
blocks = schematic.blocks
print(blocks.shape)      # Output: (3, 4, 5)
print(blocks[0, 0, 0])   # Output: Block(minecraft:redstone_wire[east=none,north=side,power=0,south=side,west=none])

# Get the positions of each block as their schematic id in a 1D numpy array
block_data = schematic.block_data
print(block_data)        # Output: [1, 2, 1, 1, 1, 3...]

# Get the offset of the schematic
offset = schematic.offset
print(offset)            # Output: (15, 3, 4)

# Or for the WorldEdit offset
we_offset = schematic.worldedit_offset
print(we_offset)         # Output: (15, 3, 4)

# Get additional metadata (if available)
metadata = schematic.metadata
print(metadata)          # Output: { 'Metadata_key_1': 'Metadata_value_1', ... }
```

**Note**: The schematic loading process will verify the schematic's version and raise an exception if it is not compatible with version 2. To force loading the schematic (not recommended), you can pass `force=True` to the `load` method.

## Requirements

- Python 3.10+
- numpy
- nbtlib

## Contributing

If you have any suggestions, bug reports, or feature requests, please feel free to open an issue or submit a pull request on [GitHub](https://github.com/gwerneckpaiva/pyschematic).

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---
*This project is based on the Minecraft Schematic format version 2.*

**Author**: Gabriel Werneck Paiva

**Email**: gwerneckpaiva@gmail.com

**GitHub**: [Your GitHub Profile](https://github.com/gwerneckpaiva/)