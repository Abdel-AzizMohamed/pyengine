"""Define a execption handling moudle"""


def data_check(data, data_type):
    """
    Check for data type/value

    Arguments:
        data: data to check for
        data_type: expected given data type
    """
    if data is None:
        raise ValueError("Invalid Value, Missing data")

    if not isinstance(data, data_type):
        raise TypeError("Invalid Type, Wrong datatype")
