_TEMPLATE = [
    'Hello beautiful',
    'Looking extra sharp today',
]

_OPERATIONS = {
    'gnr': {
        'name': 'General',
        'note': "Display is either 'emoji' or 'plain'",
        'display': 'plain',
        '.positive_emoji': "U+2705",
        '.negative_emoji': "U+274C"
    },
    'ks': {
        'name': 'Kill Switch',
        'note': 'Do not abuse Kill Switch! May lower performance!',
        'key_trigger': 'c+0',
        'stat': 0,
    },
    'qi': {
        'name': 'Quick Insert',
        'note': 'Remember to set Kill Switch on before use!',
        '.selected': 0,
        'selected': '',
        'key_scroll_up': 'c+[',
        'key_scroll_down': 'c+]',
        'key_trigger': 'c+3',
        'key_action': 't',
        'random_selection': 0,
        'stat': 0,
    },
}

_SEPERATOR = f"===========================<"

op = _OPERATIONS


def getTm():
    return _TEMPLATE


def setTm(value):
    global _TEMPLATE

    if isinstance(value, list) and value:
        _TEMPLATE = value
