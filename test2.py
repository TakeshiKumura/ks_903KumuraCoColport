import tkinter as tk

class VolumeSlider:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Volume Slider")

        self.canvas = tk.Canvas(root, width=300, height=50)
        self.canvas.pack(padx=10, pady=10)

        # スライダーの背景（進行バー）
        self.canvas.create_rectangle(10, 20, 290, 30, fill="lightgray", outline="gray")
        
        # つまみ部分を描画
        self.slider = self.canvas.create_oval(140, 10, 160, 30, fill="blue", outline="blue")

        # 音量を管理する変数
        self.volume = 0.5
        self.update_slider_position(self.volume)

        # スライダーの動きを追跡するためのイベントバインディング
        self.canvas.bind("<B1-Motion>", self.on_slider_motion)
        self.canvas.bind("<ButtonRelease-1>", self.on_slider_release)

    def update_slider_position(self, volume):
        """音量に基づいてスライダーの位置を更新"""
        x = 10 + (290 * volume)  # 音量に基づいて位置を計算
        self.canvas.coords(self.slider, x - 10, 10, x + 10, 30)
        self.change_slider_color(volume)  # 音量に基づいて色を変更

    def change_slider_color(self, volume):
        """音量に基づいてスライダーのつまみの色を変更"""
        r = int((1 - volume) * 255)  # 音量が低いほど赤に近づく
        b = int(volume * 255)        # 音量が高いほど青に近づく
        color = f'#{r:02x}{0:02x}{b:02x}'  # 赤紫から青紫へのグラデーションカラー
        self.canvas.itemconfig(self.slider, fill=color, outline=color)

    def on_slider_motion(self, event):
        """スライダーを動かして音量を変更"""
        x = event.x
        if 10 <= x <= 290:
            self.volume = (x - 10) / 290  # スライダー位置に基づいて音量を計算
            self.update_slider_position(self.volume)
            print(f"Volume: {self.volume:.2f}")

    def on_slider_release(self, event):
        """スライダーを離した時に音量の変更を確定"""
        print(f"Volume adjusted to: {self.volume:.2f}")


if __name__ == "__main__":
    root = tk.Tk()
    slider = VolumeSlider(root)
    root.mainloop()
