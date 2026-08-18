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
        'key_trigger': 'c+3',
        'key_action': 't',
        'stat': 0,
    },
}

_SEPERATOR = f"===========================<"

op = _OPERATIONS
