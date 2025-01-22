from threading import Thread, main_thread
from queue import Queue
import tkinter as tk

_initialized = False
_window = None
_q = Queue()

_width = 318
_height = 212

def _rgb_to_hex(color):
    """Converts RGB values (0-255) to a hexadecimal color string."""
    r = max(0, min(255, color[0]))
    g = max(0, min(255, color[1]))
    b = max(0, min(255, color[2]))
    return f"#{r:02x}{g:02x}{b:02x}"

def _init():
    global _initialized

    if _initialized:
        return
    _initialized = True

    loop = Thread(target=_run)
    loop.start()

def _run():
    global _window
    _window = tk.Tk()
    _window.title('TI-NSPIRE Emulator (Running...)')
    _window.geometry(str(_width) + 'x' + str(_height))
    _window.resizable(False, False)
    _canvas = tk.Canvas(_window)
    _canvas.pack(fill=tk.BOTH)
    # _root.bind('<KeyPress>', _key_event_press)
    # _root.bind('<KeyRelease>', _key_event_release)
    # _root.protocol("WM_DELETE_WINDOW", _close_event)

    finished = False
    color = (0, 0, 0)

    while True:
        try:
            _window.update_idletasks()
            _window.update()
        except:
            break

        if not finished and not main_thread().is_alive():
            _window.title('TI-NSPIRE Emulator (Done)')
            finished = True

        if not _q.empty():
            event = _q.get_nowait()

            if event[0] == 'set_color':
                color = event[1]

            elif event[0] == 'fill_rect':
                x, y, w, h = event[1]
                _canvas.create_rectangle(x, y, x + w, y + h, fill=_rgb_to_hex(color), outline='')

            elif event[0] == 'draw_text':
                x, y, text = event[1]
                _canvas.create_text((x, y), text=text, fill=_rgb_to_hex(color), anchor='sw')
            else:
                print('Not implemented yet!')

def _fire_event(name, params):
    _q.put((name, params))

def get_screen_dim():
    _init()
    return _width, _height

def use_buffer():
    _init()
    print('Not implemented yet!')

def paint_buffer():
    _init()
    print('Not implemented yet!')

def set_color(red, green, blue):
    _init()
    _fire_event('set_color', (red, green, blue))

def fill_rect(x, y, w, h):
    _init()
    _fire_event('fill_rect', (x, y, w, h))

def draw_text(x, y, text):
    _init()
    _fire_event('draw_text', (x, y, text))