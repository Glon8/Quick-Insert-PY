from .visuals import render
from .values import op,getTm
from .helpers import state_of

# ===================================< SCROLL UP
def scroll_up():
    if not op['ks']['stat']:
        return

    qi = op['qi']
    tm = getTm()
    # scrolling up
    new_slc_var = state_of(1 + qi['.selected'])

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


# ===================================< SCROLL DOWN

def scroll_down():
    if not op['ks']['stat']:
        return

    qi = op['qi']
    tm = getTm()
    # scrolling down
    new_slc_var = state_of(-1 + qi['.selected'])

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