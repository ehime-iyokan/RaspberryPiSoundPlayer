from pyPS4Controller.controller import Controller
import pygame.mixer
import time
import os
from mutagen.wave import WAVE as wav

wav_list = [
    [
        "001_.wav",
        "002_.wav",
        "003_.wav",
    ],
    [
        "004_.wav",
        "005_.wav",
        "006_.wav",
    ],
]

sampleWavFilePath = os.path.join(os.path.dirname(__file__), 'wavfiles', wav_list[0][0])
pygame.mixer.init(frequency = wav(sampleWavFilePath).info.sample_rate)

def audioOut(filename):
    wavFilePath = os.path.join(os.path.dirname(__file__), 'wavfiles', filename)
    pygame.mixer.music.load(wavFilePath)
    pygame.mixer.music.play(1)

class MyController(Controller):    
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_left_arrow_press(self):
        audioOut(wav_list[0][0])
        print("%s", wav_list[0][0])

    def on_up_arrow_press(self):
        audioOut(wav_list[0][1])
        print("%s", wav_list[0][1])

    def on_right_arrow_press(self):
        audioOut(wav_list[0][2])
        print("%s", wav_list[0][2])

    def on_square_press(self):
        audioOut(wav_list[1][0])
        print("%s", wav_list[1][0])

    def on_triangle_press(self):
        audioOut(wav_list[1][1])
        print("%s", wav_list[1][1])

    def on_circle_press(self):
        audioOut(wav_list[1][2])
        print("%s", wav_list[1][2])

    def on_x_press(self):
        print("audio cancel")
        pygame.mixer.music.stop()


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen(timeout=1800)
