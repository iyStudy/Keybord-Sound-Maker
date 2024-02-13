import keyboard
import pygame
import tkinter as tk
from PIL import Image, ImageTk
from threading import Thread

# Pygame モジュールを初期化
pygame.mixer.init()

# 再生したい音声ファイルを設定
sound = pygame.mixer.Sound('power.mp3')

# Tkinterウィンドウをグローバル変数として扱う
window = None

def play_sound(e):
    global window
    # キーが'esc'の場合、Tkinterウィンドウを閉じてプログラムを終了
    if e.name == 'esc':
        if window:
            window.destroy()
        return

    sound.play()

# すべてのキー入力で play_sound 関数を呼び出す
keyboard.on_press(callback=play_sound)

# 画像を表示するための関数
def display_image():
    global window
    window = tk.Tk()
    img = Image.open("kinnikun.jpg")
    tk_img = ImageTk.PhotoImage(img)
    tk.Label(window, image=tk_img).pack()
    window.mainloop()

# 'display_image'関数を別スレッドで実行
t = Thread(target=display_image)
t.start()
