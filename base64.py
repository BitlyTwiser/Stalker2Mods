"""Convert Hex string to Base64"""
import base64

HEX_STRING = '<insert-sha-key-here'

print(base64.b64encode(bytearray.fromhex(HEX_STRING)))
