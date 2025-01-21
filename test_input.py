import time
from ti_system import *

while True:
    key = get_key()
    if key != '':
        print(key)

    if key == 'esc':
        break

    time.sleep(1)

print('Exiting.')