import struct


class BasePacket(object):
    """
    A BasePacket is the base class for all Packet types.

    This just creates a few stub methods.
    """

    # Define a default id.
    # Packet IDs are ALWAYS unsigned, so this will never meet.
    id = -1

    # Define a default endianness.
    # This is ">" for network endianness by default.
    _endianness = ">"

    def __init__(self):
        """
        Default init method.
        """
        pass

    def on_creation(self):
        """
        Called just after your packet object is created.
        """
        pass

    def create(self, data: bytes):
        """
        Create a new Packet.
        :param data: The data to use.
        :return: If the creation succeeded or not.
        """
        self.on_creation()


class Packet(BasePacket):
    """
    A standard Packet type.

    This extends from BasePacket, and adds useful details that you'll want to use.
    """

    def __init__(self):
        """
        Create a new Packet type.
        :return:
        """
        super().__init__()
        self._original_data = b""


    def create(self, data: bytes) -> bool:
        """
        Create a new Packet.
        :param data: The data to use.
            This data should have the PacketButterfly header stripped.
        :return:
        """
        self._original_data = data


    def gen(self) -> bytes:
        """
        Generate a new set of data to write to the connection.
        :return:
        """
