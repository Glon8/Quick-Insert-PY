from .visuals import render
from .values import op, getTm
from .helpers import switch, key_press, verify_selected

from pynput.keyboard import Key


# ===================================< QUICK INSERT
def qi_switch():
    ks = op['ks']['stat']

    switch(op['qi'], 'stat')

    if ks:
        render()


def qi_prot():
    qi = op['qi']
    slc = qi['selected']
    stt = qi['stat']

    if slc != getTm()[qi['.selected']]:
        verify_selected()

    if slc == None or slc == '':
        qi['selected'] = 'Hello beautiful'

    if stt:
        render()

        key_press(qi['key_action'], 178, 250)

        for char in slc:
            if stt == 0:
                break

            key_press(char, 178, 250)

        key_press(Key.enter, 178, 250)

        qi['stat'] = 0

        render()