from tkinter import *
import tkinter as tk
import pygame
import os
import sys
import random
import time
pygame.init()

pygame.mixer.init()
a = 0
class music():
    song = os.listdir("C:\\Users\\pjpan\\Music\\")[a]
    pygame.mixer.music.load(f"C:\\Users\\pjpan\\Music\\{song}")
    def aaa():
        print(a)
    def nexxt():
        global a
        a+=1
        song = os.listdir("C:\\Users\\pjpan\\Music\\")[a]
        pygame.mixer.music.load(f"C:\\Users\\pjpan\\Music\\{song}")
        pygame.mixer.music.play()
        lab1.config(text=song)
        root.update()
    def prev():
        global a
        a -= 1
        song = os.listdir("C:\\Users\\pjpan\\Music\\")[a]
        pygame.mixer.music.load(f"C:\\Users\\pjpan\\Music\\{song}")
        pygame.mixer.music.play()
        lab1.config(text=song)
        root.update()
    def play():

        pygame.mixer.music.play()

    def pause():
        pygame.mixer.music.pause()

    def vol_up():
        vol1 = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume((vol1 + 0.1))
    def vol_down():
        vol1 = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume((vol1-0.1))


root = Tk()
root.minsize(815,100)
root.title("Music Player")
lab1 = Label(text=music.song, width=100)
btn1 = Button(root,text="play", command=music.play)
btn2 = Button(root,text="pause", command=music.pause)
btn3 = Button(root, text="volume up", command=music.vol_up)
btn4 = Button(root, text="volume down", command=music.vol_down)
btn5 = Button(root,text="next", command=music.nexxt)
btn6 = Button(root,text="prev", command=music.prev)
lab1.grid(row = 0, column = 1, pady = 2)
btn1.grid(row = 1, column = 1, pady = 2)
btn2.grid(row = 2, column = 1, pady = 2)
btn3.grid(row = 3, column = 2, pady = 2)
btn4.grid(row = 3, column = 0, pady = 2)
btn5.grid(row = 1, column = 2, pady = 2)
btn6.grid(row = 1, column = 0, pady = 2)
root.mainloop()

