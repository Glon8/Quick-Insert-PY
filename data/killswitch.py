import json

from .values import op, getTm, setTm
from .helpers import switch, verify_selected
from .visuals import render
from .helpers import config_parse_reread, read_file, write_file, getDir


# ===================================< KILL SWITCH
def ks_switch():
    ks = op['ks']
    op['qi']['stat'] = 0

    switch(ks, 'stat')

    if ks['stat']:
        config_parse_reread(read_file('config.json'))

        content = read_file('templates.json')

        if content:
            try:
                setTm(json.loads(content))
            except json.JSONDecodeError:
                write_file(getDir(), 'templates.json', getTm())
        else:
            write_file(getDir(), 'templates.json', getTm())

        verify_selected()
    else:
        write_file(getDir(), 'templates.json', getTm())

    render()
