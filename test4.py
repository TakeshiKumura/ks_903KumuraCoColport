import tkinter as tk

class VolumeSlider:
    def __init__(self, master):
        self.canvas = tk.Canvas(master, width=100, height=300)
        self.canvas.pack(padx=20, pady=20)
        
        # スライダーの背景（進行バー）
        self.bg = self.canvas.create_rectangle(20, 20, 40, 280, fill="gray", outline="gray")
        
        # つまみ部分（初期位置は中央）
        self.slider = self.canvas.create_oval(10, 140, 50, 180, fill="purple", outline="black")
        
        # 初期音量
        self.volume = 0.5
        
        # スライダーの動きを検出するイベントバインド
        self.canvas.bind("<B1-Motion>", self.on_slider_motion)
        self.canvas.bind("<ButtonRelease-1>", self.on_slider_release)
        
    def on_slider_motion(self, event):
        """スライダーの動きに基づいて音量を変更"""
        y = event.y  # マウスのY位置
        if 20 <= y <= 280:
            # つまみのY座標を制限する
            self.canvas.coords(self.slider, 10, y - 20, 50, y + 20)
            # 音量を計算
            self.volume = 1 - (y - 20) / 260  # 音量を0（最下部）から1（最上部）にマッピング
            print(f"Volume: {self.volume:.2f}")  # 現在の音量を表示
            self.change_slider_color()  # 色を変更

    def on_slider_release(self, event):
        """スライダーの移動を終了した際に色を最終的に調整"""
        self.change_slider_color()

    def change_slider_color(self):
        """音量に基づいてスライダーのつまみの色を変更"""
        r = int((1 - self.volume) * 255)  # 音量が低いほど赤に近づく
        b = int(self.volume * 255)        # 音量が高いほど青に近づく
        color = f'#{r:02x}{0:02x}{b:02x}'  # 赤紫から青紫へのグラデーションカラー
        self.canvas.itemconfig(self.slider, fill=color)  # つまみの色を変更

# メインウィンドウ
root = tk.Tk()
root.title("Volume Slider")

# VolumeSlider クラスのインスタンスを作成
volume_slider = VolumeSlider(root)

root.mainloop()
