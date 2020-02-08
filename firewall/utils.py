def dec_to_bin(dec):
    """

    Args:
        dec(string): A number in base 10

    Returns:
        binary(string): Binary equivalent of dec
    """

    binary = bin(int(dec))
    return binary[2:].zfill(8)
