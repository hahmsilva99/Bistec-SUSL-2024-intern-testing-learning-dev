from pynput import keyboard


def fix_current_line():
    pass

def fix_selection():
    pass


def on_f9():
    fix_current_line()

def on_f10():
    fix_selection()

with keyboard.GlobalHotKeys({
        '<101>':on_f9,
        '<109>':on_f10 }) as h:
    h.join()
