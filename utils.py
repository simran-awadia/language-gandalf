import re


def strtobool(val):
    """Convert a string representation of truth to true (1) or false (0).
    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.

    This is part of distutils.util for python 3.11 but is deprecated past 3.12 so
    moving this code over to allow for easier upgrades
    """
    val = re.sub(r"[^A-Za-z]", '', val).lower()
    if val in ("y", "yes", "t", "true", "on", "1", "vrai"):
        return 1
    elif val in ("n", "no", "f", "false", "off", "0", "faux"):
        return 0
    else:
        raise ValueError("invalid truth value %r" % (val,))

