"""FERENGI utilities."""

from lzma import LZMADecompressor


ROA = '/usr/share/roa.xz'


def roa():
    """Print rules of acquisition."""

    with open(ROA, 'rb') as file:
        compressed_data = file.read()

    decompressor = LZMADecompressor()
    uncompressed_data = decompressor.decompress(compressed_data)
    return uncompressed_data.decode()
