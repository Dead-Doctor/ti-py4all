import msvcrt

def get_key():
    if msvcrt.kbhit():
        # while msvcrt.kbhit():
        c = msvcrt.getch()
        if c in b'\000\xe0':
            c = msvcrt.getch()
        
        # top: missing 'scratchpad', 'center', 'home', 'doc', 'menu', 'var'
        if c == b'\x1b':
            return 'esc'
        if c == b'\t':
            return 'tab'
        if c == b'H':
            return 'up'
        if c == b'K':
            return 'left'
        if c == b'P':
            return 'down'
        if c == b'M':
            return 'right'
        if c == b'\x08' or c == b'S':
            return 'del'
        # left: missing 'trig', 'square', 'exp', '10power'
        if c in b'=^()':
            return c.decode()
        # center
        if c in b'01234567890.-':
            return c.decode()
        # right (backslash available through shift): missing 'template', 'cat', '−'
        if c in b'*/\\+':
            return c.decode()
        if c == b'\r':
            return 'enter'
        # bottom: missing weird 'E', 'pi', '?!', 'return', 'uppercase-letters'
        if c in b',abcdefghijklmnopqrstuvwxyz ':
            return c.decode()
        # only available through usb keyboard
        if c in b'!"$%&[]{}?`~#\';:_<>|@':
            return c.decode()
        return 'ERR: ' + str(c)
    return ''