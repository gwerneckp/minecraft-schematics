import nbtlib as nbt
import numpy as np

def nbt_to_numpy(compound) -> dict:
    """Converts an nbtlib Compound to a dictionary with numpy data types.

    This method recursively converts an nbtlib Compound object into a dictionary, replacing
    certain nbtlib types with their corresponding numpy data types to facilitate compatibility
    and easy data manipulation.

    Args:
        nbt_obj (nbtlib.Compound or nbtlib.List): The nbtlib object to convert.            

    Returns:
        dict: The converted dictionary.

    Notes:
        The mapping of base types in the nbtlib Compound to their corresponding associated nbt tags is as follows:

        +-------------------+---------------------------------------------------------+
        |     Base type     |                   Associated nbt tags                   |
        +===================+=========================================================+
        | ``int``           | :class:`Byte` :class:`Short` :class:`Int` :class:`Long` |
        +-------------------+---------------------------------------------------------+
        | ``float``         | :class:`Float` :class:`Double`                          |
        +-------------------+---------------------------------------------------------+
        | ``str``           | :class:`String`                                         |
        +-------------------+---------------------------------------------------------+
        | ``numpy.ndarray`` | :class:`ByteArray` :class:`IntArray` :class:`LongArray` |
        +-------------------+---------------------------------------------------------+
        | ``list``          | :class:`List`                                           |
        +-------------------+---------------------------------------------------------+
        | ``dict``          | :class:`Compound`                                       |
        +-------------------+---------------------------------------------------------+
    """

    iterator = compound.items() if isinstance(
        compound, nbt.Compound) else enumerate(compound)

    result = {}
    for key, value in iterator:
        if isinstance(value, nbt.Byte):
            result[key] = np.int8(value)
        elif isinstance(value, nbt.Short):
            result[key] = np.int16(value)
        elif isinstance(value, nbt.Int):
            result[key] = np.int32(value)
        elif isinstance(value, nbt.Long):
            result[key] = np.int64(value)
        elif isinstance(value, nbt.Float):
            result[key] = np.float32(value)
        elif isinstance(value, nbt.Double):
            result[key] = np.float64(value)
        elif isinstance(value, nbt.String):
            result[key] = str(value)
        elif isinstance(value, nbt.ByteArray):
            result[key] = np.array(value, dtype=np.int8)
        elif isinstance(value, nbt.IntArray):
            result[key] = np.array(value, dtype=np.int32)
        elif isinstance(value, nbt.LongArray):
            result[key] = np.array(value, dtype=np.int64)
        elif isinstance(value, nbt.List):
            result[key] = nbt_to_numpy(value)
        elif isinstance(value, nbt.Compound):
            result[key] = nbt_to_numpy(value)
        else:
            result[key] = value

    return result
