import tkinter as tk

class VolumeSlider(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.length = 165  # スライダーの長さ
        self.min_volume = 0
        self.max_volume = 1
        self.volume = 0.5  # 初期音量（中央）
        
        # スライダーの背景を描画 (位置を調整)
        self.create_line(20, 0, 20, self.length, width=4, fill="gray")  # x座標を20に固定
        
        # 初期のつまみ（長方形）の位置をスライダーの中央に配置
        knob_center = self.length / 2  # 中央に配置
        # x座標を20に合わせる（つまみの幅を考慮して調整）
        self.knob = self.create_rectangle(10, knob_center - 6, 40, knob_center + 6, fill=self.get_color(self.volume), outline="black")
        
        # マウスでスライダーを動かせるようにする
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_release)
        
    def on_drag(self, event):
        """スライダーのつまみをドラッグで動かす"""
        y = event.y
        # スライダー内に制限
        if 0 <= y <= self.length:
            self.move_knob(y)
            self.volume = 1 - y / self.length  # 上に動くほど音量が高くなる
            print(f"Volume: {self.volume:.2f}")  # 音量を表示
            self.change_knob_color()

    def on_release(self, event):
        """ドラッグを終了したときの処理"""
        self.volume = 1 - event.y / self.length  # 最終音量を更新
        self.change_knob_color()

    def move_knob(self, y):
        """つまみ（長方形）の位置を変更"""
        self.coords(self.knob, 4, y - 2, 10, y + 2)
    
    def get_color(self, volume):
        """音量に基づいて色を変更（赤紫から青紫へのグラデーション）"""
        r = int((1 - volume) * 255)  # 音量が低いほど赤に近づく
        b = int(volume * 255)        # 音量が高いほど青に近づく
        return f'#{r:02x}{0:02x}{b:02x}'  # 赤紫から青紫へのグラデーションカラー

    def change_knob_color(self):
        """音量に基づいてつまみの色を変更"""
        color = self.get_color(self.volume)
        self.itemconfig(self.knob, fill=color)

# メインウィンドウの設定
root = tk.Tk()
root.title("Volume Slider")

# VolumeSlider を作成
volume_slider = VolumeSlider(root, width=40, height=175)
volume_slider.pack(padx=20, pady=20)

root.mainloop()
