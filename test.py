import tkinter as tk

class CustomSlider:
    def __init__(self, master, from_=0, to=1, length=200, initial_value=0.5, command=None):
        self.master = master
        self.from_ = from_
        self.to = to
        self.length = length
        self.command = command
        
        # Canvasを作成
        self.canvas = tk.Canvas(master, width=self.length, height=50)
        self.canvas.pack(pady=20)
        
        # スライダーの背景（トラック）を描画
        self.track = self.canvas.create_line(10, 25, self.length - 10, 25, width=6, fill="gray")
        
        # つまみの作成
        self.knob = self.canvas.create_oval(10, 10, 30, 30, fill="blue", outline="blue")
        
        # 初期つまみ位置
        self.set_value(initial_value)
        
        # マウスドラッグイベントをバインド
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        
    def set_value(self, value):
        # 値をスケールに合わせて位置に変換
        x = (value - self.from_) / (self.to - self.from_) * (self.length - 20) + 10
        self.canvas.coords(self.knob, x - 10, 10, x + 10, 30)
        if self.command:
            self.command(value)
        
    def on_drag(self, event):
        # ドラッグ中に新しい位置にスライダーを更新
        x = max(10, min(event.x, self.length - 10))  # スライダーの範囲を制限
        value = (x - 10) / (self.length - 20) * (self.to - self.from_) + self.from_
        self.set_value(value)
        
    def on_release(self, event):
        # ドラッグが終わった後
        pass


def on_volume_change(value):
    print(f"Volume: {value:.2f}")

# メインウィンドウ
root = tk.Tk()
root.title("Custom Slider")

# スライダーの作成
slider = CustomSlider(root, from_=0, to=1, initial_value=0.5, command=on_volume_change)

# Tkinterメインループ
root.mainloop()
