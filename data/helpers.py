import copy
import os
import sys
import json
import time
import random

from pathlib import Path
from pynput.keyboard import Controller as K

from .values import op, getTm

k = K()


# ===================================< SWITCH
# dic - dictionary to use
# key - from the dictionary to flip
def switch(dic, key):
    dic[key] = 1 - dic[key]


# ===================================< KEY PRESS
# key - to press
# delay - between press and release
def key_press(key, min_delay, max_delay):
    k.press(key)

    timeout = random.randint(min_delay, max_delay) / 1000
    time.sleep(timeout)

    k.release(key)


# ===================================< FILES COUNT
def files_count(file_path):
    return sum(len(files) for _, _, files in os.walk(file_path))


# ===================================< GET DIRECTORY
def getDir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(os.path.abspath(sys.executable))

    return str(Path(__file__).resolve().parent.parent)


# ===================================< WRITE FILE
def write_file(file_path, file_name, data):
    if not isinstance(file_path, str) or not os.path.exists(file_path):
        return None

    with open(f'{file_path}/{file_name}', 'w') as file:
        json.dump(data, file, indent=4)


# ===================================< READ FILE
# file_path - to read from
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None


# ===================================< CONFIG PARSER
# string - to pars in to config
def config_parse(string):
    if string == '' or string is None:
        write_file(getDir(), 'config.json', op)
        return

    config_pack = json.loads(string)

    for name, value in config_pack.items():
        for key, val in value.items():
            if key != 'name' or name == 'ks':
                op[name][key] = val


# ===================================< CONFIG PARSER ON REREAD
# string - to pars in to config
def config_parse_reread(string):
    if string == '' or string is None:
        return

    config_pack = json.loads(string)

    copy_op = copy.deepcopy(op)
    copy_op['ks'].pop('stat')

    copy_conf = copy.deepcopy(config_pack)
    copy_conf['ks'].pop('stat')

    if copy_op == copy_conf:
        return

    valid_keys = ['display', '.positive_emoji', '.negative_emoji', 'key_trigger', 'path_from', 'path_to',
                  'self_replace']

    for name, value in config_pack.items():
        for key, val in value.items():
            if key in valid_keys and op[name][key] != val and name != 'ks':
                op[name][key] = val

    verify_selected()

# ===================================< UNICODE CONVERT

def unicode_convert(unicode):
    return chr(int(unicode[2:], 16))


# ===================================< VERIFY SELECTED (qi)
def verify_selected():
    qi = op['qi']
    tm = getTm()

    slc_var = qi['.selected']
    new_slc = tm[slc_var]

    if tm and len(tm) > slc_var >= 0:
        if qi['selected'] != new_slc:
            qi['selected'] = new_slc
    else:
        qi['.selected'] = 0

        if not tm:
            qi['selected'] = 'Hello beautiful'
        else:
            qi['selected'] = new_slc


# ===================================< STATE OF X (qi)
def state_of(x):
    tm = getTm()

    if not tm or not isinstance(x, int):
        return None

    return x % len(tm)
