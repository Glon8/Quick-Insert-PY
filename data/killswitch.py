from .values import op
from .helpers import switch
from .visuals import render
from .helpers import config_parse_reread, read_file


# ===================================< KILL SWITCH
def ks_switch():
    ks = op['ks']
    op['qi']['stat'] = 0

    switch(ks, 'stat')

    if ks['stat']:
        config_parse_reread(read_file('config.json'))

    render()
