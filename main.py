import webbrowser
from pynput.keyboard import Key,Controller
keyboard = Controller()

webbrowser.open_new('https://youtu.be/-DbYwRO8ojo')
while True:

    for i in range(10):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)




