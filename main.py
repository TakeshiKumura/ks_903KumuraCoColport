import pygame
from tkinter import Tk, Frame, Label, PhotoImage, ttk

# Pygameの初期化
pygame.mixer.init()

# グローバル変数
vol0 = PhotoImage(file=r'image\music\base\volume0.png')
vol1 = PhotoImage(file=r'image\music\base\volume1.png')
volas1 = PhotoImage(file=r'image\music\base\volume1a.png')
vol2 = PhotoImage(file=r'image\music\base\volume2.png')
volas2 = PhotoImage(file=r'image\music\base\volume2a.png')
vol3 = PhotoImage(file=r'image\music\base\volume3.png')
volas3 = PhotoImage(file=r'image\music\base\volume3a.png')
vol4 = PhotoImage(file=r'image\music\base\volume4.png')
volas4 = PhotoImage(file=r'image\music\base\volume4a.png')

# Tkinterのセットアップ
root = Tk()
master_frame = Frame(root)
master_frame.grid(row=0, column=0, padx=20, pady=20)

# 音量メーターを表示するラベル
volume_meter = Label(master_frame, image=vol0)
volume_meter.grid(row=2, column=1, padx=40)

# 音量を調整するための関数
def change_volume(amount):
    # 現在の音量を取得（0.0〜1.0の範囲）
    current_volume = pygame.mixer.music.get_volume()

    # 新しい音量を計算（範囲[0, 1]に収める）
    new_volume = max(0.0, min(1.0, current_volume + amount))

    # 音量を設定
    pygame.mixer.music.set_volume(new_volume)

    # ボリュームメーターとスライダーを更新
    update_volume_meter(new_volume)
    volume_slider.set(new_volume)

def update_volume_meter(volume):
    # 音量に基づいてボリュームメーター画像を更新
    current_volume = volume * 100  # 音量を0～100に変換
    if current_volume < 1:
        volume_meter.config(image=vol0)
    elif current_volume <= 12.5:
        volume_meter.config(image=vol1)
    elif current_volume <= 25:
        volume_meter.config(image=volas1)
    elif current_volume <= 37.5:
        volume_meter.config(image=vol2)
    elif current_volume <= 50:
        volume_meter.config(image=volas2)
    elif current_volume <= 62.5:
        volume_meter.config(image=vol3)
    elif current_volume <= 75:
        volume_meter.config(image=volas3)
    elif current_volume <= 87.5:
        volume_meter.config(image=vol4)
    else:
        volume_meter.config(image=volas4)

# 音量スライダー
volume_slider = ttk.Scale(master_frame, from_=0, to=1, orient="horizontal", length=200, command=lambda v: pygame.mixer.music.set_volume(float(v)))
volume_slider.set(0.5)  # 初期音量50%
volume_slider.grid(row=1, column=1, pady=10)

# 音量変更イベントのバインディング
root.bind("<Prior>", lambda event: change_volume(0.01))  # Page Upで音量+1%
root.bind("<Next>", lambda event: change_volume(-0.01))  # Page Downで音量-1%

# アプリケーションのメインループ
root.mainloop()
