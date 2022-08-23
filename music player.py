import pygame #используется для создания видео-игр
import tkinter as tkr #используется для разработки GUI
from tkinter.filedialog import askdirectory #диалог между файлами и папками
import os #взаимодействие с OS

music_player = tkr.Tk() #создаём окно программы
music_player.title("Music Player") #даём имя
music_player.geometry("900x700") #устанавливаем размеры

directory = askdirectory() #в переменную directory отправляем данные о нужной нам папке
os.chdir(directory)
song_list = os.listdir() #записываем их в список

play_list = tkr.Listbox(music_player, font="Georgia 12 bold", bg="yellow", selectmode=tkr.SINGLE) #украшаем наш лист песен
for item in song_list: #выводим наши данные
    pos = 0
    play_list.insert(pos, item)
    pos += 1
#воспроизведением и загрузкой звуков у нас отвечает pygame
pygame.init()
pygame.mixer.init()
#создаём команды воспроизведения, остановки, паузы и снятия паузы, чтобы управлять проигрывателем
def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()
#пользуемся tkinter для создания кнопок в интерфейсе
Button1 = tkr.Button(music_player, width=5, height=3, font="Georgia 12 bold", text="play", command=play, bg="blue", fg="white")
Button2 = tkr.Button(music_player, width=5, height=3, font="Georgia 12 bold", text="stop", command=stop, bg="red", fg="white")
Button3 = tkr.Button(music_player, width=5, height=3, font="Georgia 12 bold", text="pause", command=pause, bg="purple", fg="white")
Button4 = tkr.Button(music_player, width=5, height=3, font="Georgia 12 bold", text="unpause", command=unpause, bg="green", fg="white")
#добавляем переменные, которые позволят видеть песню в верхней части экрана
var = tkr.StringVar() 
song_title = tkr.Label(music_player, font="Georgia 12 bold", textvariable=var)
#пакуем модули
song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
play_list.pack(fill="both", expand="yes")

music_player.mainloop() #запускаем предложение
