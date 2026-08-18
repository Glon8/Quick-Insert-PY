from data.helpers import config_parse, read_file
from data.values import op
from data.quick_insert import qi_prot, qi_switch
from data.visuals import render
from data.killswitch import ks_switch

from pynput.keyboard import Controller as K, Listener as kL, HotKey

k = K()


# ===================================< CONTROL PANNEL
def control_panel():
    while True:
        if op['ks']['stat']:
            qi_prot()


# ===================================< MAIN
def main():
    config_parse(read_file('config.json'))

    qi = op['qi']

    # \/===================================< HOTKEYS SETTINGS
    hotkeys = [
        HotKey(HotKey.parse(op['ks']['key_trigger']), ks_switch),
        HotKey(HotKey.parse(qi['key_trigger']), qi_switch),
    ]

    def on_press(key):
        for thing in hotkeys:
            thing.press(key)

    def on_release(key):
        for thing in hotkeys:
            thing.release(key)

    # /\===================================< HOTKEYS SETTINGS

    render()

    with kL(on_press=on_press, on_release=on_release):
        control_panel()


# ===================================< MAIN START
if __name__ == '__main__':
    main()
