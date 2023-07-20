import keyboard
import pygame
import tkinter as tk
from PIL import Image, ImageTk
from threading import Thread

# Pygame モジュールを初期化
pygame.mixer.init()

# 再生したい音声ファイルを設定（ここでは "power.mp3"）
sound = pygame.mixer.Sound('power.mp3')

def play_sound(e):
    # キーが'esc'でない場合のみ再生
    if e.name != 'esc':
        sound.play()

# すべてのキー入力で play_sound 関数を呼び出す
keyboard.on_press(callback=play_sound)

# 画像を表示するための関数
def display_image():
    window = tk.Tk()
    img = Image.open("kinnikun.jpg")
    tk_img = ImageTk.PhotoImage(img)
    tk.Label(window, image=tk_img).pack()
    window.mainloop()

# 'display_image'関数を別スレッドで実行
t = Thread(target=display_image)
t.start()

# 'esc'キーが押されるまで待つ（'esc'が押されるとプログラムが終了する）
keyboard.wait('esc')
