from .schematic_v2 import SchematicV2
import nbtlib as nbt
from .schematic_schema import SchematicSchema


class Schematic(SchematicSchema):
    def __init__(self):
        """Representation of a Minecraft schematic."""
        super().__init__()

    @staticmethod
    def load(path: str, force=False):
        """Load the schematic from a file.

        Args:
            path (str): The path to the schematic file.
            force (bool, optional): Force loading the schematic even if it is an incompatible version. Defaults to False. (Not recommended as it may cause unintended errors.)

        Returns:
            Schematic: An instance of the Schematic class.

        Raises:
            FileNotFoundError: If the file does not exist.
            nbt.lib.MalformedFileError: If the file cannot be loaded due to a parsing error.
            Exception: If the schematic is an incompatible version and force is False.
        """
        try:
            raw = nbt.load(path)
            if not force:
                match raw.get("Version"):
                    case None:
                        raise Exception(
                            "Version not found. This is likely due to an old version of the schematic format which this library does not support. Check out https://github.com/cbs228/nbtschematic for a library that supports version 1."
                        )
                    case 1:
                        raise Exception(
                            "Version 1 is not supported as it is an old version of the schematic format. Check out https://github.com/cbs228/nbtschematic for a library that supports version 1."
                        )
                    case 2:
                        s = SchematicV2()
                        s.raw = raw

                    case _:
                        raise Exception(
                            f"This library does not fully support the version {raw.get('Version')} of the schematic format. Use force=True to force loading the schematic. This may cause unintended errors."
                        )

        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {path}") from e
        except nbt.lib.MalformedFileError as e:
            raise nbt.lib.MalformedFileError(f"Error loading schematic: {path}") from e
        return s
