import os
import time
import platform

from rich.console import Console

from .values import op, _SEPERATOR
from .helpers import unicode_convert

console = Console()


# ===================================< VISUALS
def render():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    general = op['gnr']

    pos = 'on' if general['display'] == 'plain' else unicode_convert(general[".positive_emoji"])
    neg = 'off' if general['display'] == 'plain' else unicode_convert(general[".negative_emoji"])

    for key, values in op.items():
        for att, stat in values.items():
            if not att.startswith('.'):
                if att == 'name':
                    console.print(_SEPERATOR + ' ' + str(stat))
                elif (att == 'key_action' or
                      att == 'key_trigger' or
                      att == 'key_scroll_up' or
                      att == 'key_scroll_down' or
                      att == 'key_random_selection' or
                      att == 'selected' or
                      att == 'note' or
                      att == 'display'):
                    console.print(f"{att} : {stat}")
                else:
                    console.print(f"{att} : {pos if stat else neg}")
