class Block:
    def __init__(self, blockdata: str, block_entity: dict = None):
        """Representation of a block in the Minecraft schematic.

        Args:
            blockdata (str): The raw block data in the format 'block_type[properties]'.
        """
        self.raw = blockdata
        self.block_entity: dict = block_entity

    @property
    def type(self) -> str:
        """str: The type of the block without properties."""
        return self.raw.split("[")[0]

    @property
    def properties(self) -> dict:
        """dict: A dictionary containing the properties of the block."""
        properties = {}
        for prop in self.raw.split("[")[1].split("]")[0].split(","):
            key, value = prop.split("=")
            properties[key] = value

        if self.block_entity:
            properties["block_entity"] = self.block_entity

        return properties

    @property
    def raw_properties(self) -> str:
        """str: The raw properties of the block without the block type."""
        return self.raw.split("[")[1].split("]")[0]

    def add_block_entity(self, block_entity: dict):
        self.block_entity = block_entity

    def __repr__(self) -> str:
        return f"Block({self.raw}, {self.block_entity})"

    def __str__(self) -> str:
        return f"Block({self.raw}, {self.block_entity})"

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Block):
            return self.raw == __value.raw
        else:
            return False
