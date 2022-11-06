import os
from playsound import playsound
import time
from pygame import mixer
import enumerare
from mutagen.mp3 import MP3
timp = 0
k = 0
ora = 45
pauza = 10
mixer.init()
# folder path

print(enumerare.count,"fisiere")
run = True
while run:
    for i in range(enumerare.count):
        while i:
            time.sleep(2) # se verifica valorile la fiecare 6 secunde
            now = time.gmtime()
            if (now[3] == 16 ):
                if (now[4] % 2 != 0):
                    for j in range(3):
                        playsound(f'Music/{j+k}.mp3')
                        audio = MP3(f'Music/{i + k}.mp3')
                        timp += int(audio.info.length)
                        if (timp > 600):
                            audio2 = MP3(f'Music/{i + k - 1}.mp3')
                            timp2 = int(audio2.info.length)
                            mixer.music.load(f'Music/{i + k}.mp3')
                            mixer.music.play()
                            time.sleep(600 - timp2)
                            print("nu este DEOC BINE")
                    k=k+3
                    i=0
