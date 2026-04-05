import struct

def _hex(byte):
    hex_chars = '0123456789abcdef'
    result = hex_chars[byte // 16] + hex_chars[byte % 16]
    return result

class data_string(bytes):
    def __new__(cls, src_data):
        if isinstance(src_data, str):
            # Encode from string if initialized with string representation
            src_data = src_data.encode('latin-1')
        return super().__new__(cls, src_data)

    def __repr__(self):
        result_list = ["b'"]

        for c in self:
            hex_char = _hex(c)
            result_list.append(r'\x' + hex_char)
        result_list.append("'")

        return ''.join(result_list)
