import os.path

from .visuals import render
from .values import op
from .helpers import switch, read_file, key_press, getDir

from pynput.keyboard import Key


# ===================================< QUICK INSERT
def qi_switch():
    ks = op['ks']['stat']

    switch(op['qi'], 'stat')

    if ks:
        render()


def qi_prot():
    qi = op['qi']
    path = os.path.join(getDir(), 'templates.json')
    text = None

    if os.path.exists(path):
        text = read_file('templates.json')
    else:
        with open(path, 'w') as file:
            pass

    if text is None or text == '':
        text = 'Hello There!'

    if qi['stat']:
        render()

        key_press(qi['key_action'], 178, 250)

        for char in text:
            if qi['stat'] == 0:
                break

            key_press(char, 178, 250)

        key_press(Key.enter, 178, 250)

        qi['stat'] = 0

        render()
