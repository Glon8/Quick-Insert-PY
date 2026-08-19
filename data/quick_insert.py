from .visuals import render
from .values import op, getTm
from .helpers import switch, key_press, verify_selected
from .selection import random_selection

from pynput.keyboard import Key

_SOFT_LOCK = False


# ===================================< QUICK INSERT
def qi_switch():
    if op['ks']['stat']:
        switch(op['qi'], 'stat')


def qi_prot():
    global _SOFT_LOCK

    qi = op['qi']

    if not qi['stat'] or _SOFT_LOCK:
        return

    _SOFT_LOCK = True

    tm = getTm()

    if len(tm) < qi['.selected'] or qi['selected'] != getTm()[qi['.selected']] and not qi['random_selection']:
        verify_selected()
    elif qi['random_selection']:
        random_selection()

        render()

    slc = qi['selected']

    if slc == None or slc == '':
        qi['selected'] = 'Hello beautiful'

    key_press(qi['key_action'], 178, 250)

    for char in slc:
        if qi['stat'] == 0:
            break

        key_press(char, 178, 250)

    key_press(Key.enter, 178, 250)

    qi['stat'] = 0

    _SOFT_LOCK = False

    render()
