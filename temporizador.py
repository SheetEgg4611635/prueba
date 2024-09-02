from hashlib import scrypt
import time
from webbrowser import get

def temporizador(segundos):
    while segundos:
        mins, secs = divmod(segundos, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        segundos -= 1

    print('¡Tiempo completo!')