import random

from .visuals import render
from .values import op, getTm
from .helpers import state_of, switch


# ===================================< SCROLL
def scroll(dir):
    qi = op['qi']

    if dir not in ('up', 'down') or not op['ks']['stat'] or qi['random_selection']:
        return

    pointer = 1 if dir == 'up' else -1

    tm = getTm()
    # scrolling
    new_slc_var = state_of(pointer + qi['.selected'])

    qi['.selected'] = new_slc_var if new_slc_var is not None else 0

    slc_var = qi['.selected']
    # editing selected
    if tm:
        tm_var = tm[slc_var]

        if qi['selected'] != tm_var:
            qi['selected'] = tm_var

            render()
    else:
        qi['selected'] = 'Hello beautiful'

        render()


# ===================================< SCROLL UP
def scroll_up():
    scroll('up')


# ===================================< SCROLL DOWN
def scroll_down():
    scroll('down')


# ===================================< RANDOM SWITCH
def random_switch():
    if not op['ks']['stat']:
        return

    switch(op['qi'], 'random_selection')

    render()


# ===================================< RANDOM SELECTION
def random_selection():
    qi = op['qi']

    if not op['ks']['stat'] or not qi['stat'] or not qi['random_selection']:
        return

    tm = getTm()

    qi['.selected'] = random.randint(0, len(tm) - 1)
    qi['selected'] = tm[qi['.selected']]
