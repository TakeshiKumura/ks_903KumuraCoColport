import tkinter as tk
from tkinter import ttk

def on_slider_motion(event):
    """スライダーの動きに基づいて音量を変更"""
    volume = volume_slider.get()  # 現在のスライダー位置を取得
    print(f"Volume: {volume:.2f}")  # 現在の音量を表示
    change_slider_color(volume)  # 色を変更する関数を呼び出し

def change_slider_color(volume):
    """音量に基づいてスライダーのつまみの色を変更"""
    r = int((1 - volume) * 255)  # 音量が低いほど赤に近づく
    b = int(volume * 255)        # 音量が高いほど青に近づく
    color = f'#{r:02x}{0:02x}{b:02x}'  # 赤紫から青紫へのグラデーションカラー
    style.configure("TScale", troughcolor=color, sliderrelief="flat")

root = tk.Tk()
root.title("Volume Slider")

# スタイルを設定
style = ttk.Style()
style.configure("TScale",
                thickness=20,   # スライダーの幅
                sliderlength=40,  # つまみの長さ
                )

# 音量スライダー（垂直方向）
volume_frame = tk.Frame(root)
volume_frame.pack(padx=20, pady=20)

# volume_slider = ttk.Scale(volume_frame, from_=1, to=0, command=on_slider_motion, length=165, style="TScale")
# volume_slider.set(0.5)  # 初期音量50%
# volume_slider.pack(pady=10)


root.mainloop()

__init__

ks903imusicsongs()
