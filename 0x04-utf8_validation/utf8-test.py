#!/usr/bin/python3
"""
UTF-8 validation file
"""


def validUTF8(data):
    """
    Method determines if data represents a valid UTF-8 encoding.
    """

    # Count for the number of consecutive 1's in the most significant bits
    num_bytes = 0

    for byte in data:
        # If a byte starts with '10', it must be part of a multi-byte sequence.
        if num_bytes > 0:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1
        else:
            # Count the number of consecutive 1's in the most significant bits
            mask = 0b10000000
            while byte & mask:
                num_bytes += 1
                mask >>= 1

            # Check for invalid number of bytes
            if num_bytes == 1 or num_bytes > 4:
                return False

            # For single-byte characters (ASCII), num_bytes is 0
            if num_bytes == 0:
                continue

        # Check if the next 'num_bytes' bytes are part of a multi-byte sequence
        if len(data) < num_bytes:
            return False
        for i in range(num_bytes):
            if (data[i+1] >> 6) != 0b10:
                return False
        # Move to the next character
        data = data[num_bytes:]

    return num_bytes == 0
