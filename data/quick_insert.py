from .visuals import render
from .values import op, getTm
from .helpers import switch, key_press, verify_selected, disturbance
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

    key_press(qi['key_action'], int(qi['.min_delay'] + disturbance()), int(qi['.max_delay'] + disturbance()))

    for char in slc:
        if qi['stat'] == 0:
            break

        key_press(char, int(qi['.min_delay'] + disturbance()), int(qi['.max_delay'] + disturbance()))

    key_press(Key.enter, int(qi['.min_delay'] + disturbance()), int(qi['.max_delay'] + disturbance()))

    qi['stat'] = 0

    _SOFT_LOCK = False

    render()
