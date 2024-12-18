import yt_dlp
import traceback
from tkinter import *
from tkinter import messagebox, ttk


class ks903_Music_downloder_JP:
    def __init__(self, root):
        self.root = root
        self.root.title("iSongs Downloader")
        self.root.geometry("500x300")

        self.placeholder_text = "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:"

        self.font_small = ('Arial', 10)
        self.setup_gui()

    def setup_gui(self):
        self.TextBox1 = Entry(self.root, width=50, fg='grey', bg='white', font=self.font_small)
        self.TextBox1.insert(0, self.placeholder_text)
        self.TextBox1.bind('<FocusIn>', self.TextBox1_on_focus)
        self.TextBox1.bind('<FocusOut>', self.TextBox1_on_focusout)
        self.TextBox1.pack(pady=20)

        self.Button1 = Button(self.root, text="音楽のダウンロードを開始", command=self.downloadpush)
        self.Button1.pack()

        self.percentage_label = Label(self.root, text="進行中: 0%", font=('Arial', 12))
        self.percentage_label.pack(pady=5, side=TOP, anchor="n")

        self.style = ttk.Style()
        self.style.configure("green.Horizontal.TProgressbar", thickness=20, background='green')
        self.progressbar = ttk.Progressbar(self.root, style="green.Horizontal.TProgressbar", mode='determinate')
        self.progressbar.pack(pady=10)

    def TextBox1_on_focus(self, event):
        if self.TextBox1.get() == self.placeholder_text:
            self.TextBox1.delete(0, END)
            self.TextBox1.config(fg='black')

    def TextBox1_on_focusout(self, event):
        if self.TextBox1.get() == '':
            self.TextBox1.insert(0, self.placeholder_text)
            self.TextBox1.config(fg='grey')

    def update_progress_bar(self, d):
        if d['status'] == 'downloading':
            percent = d.get('downloaded_bytes', 0) / d.get('total_bytes', 1) * 100
            self.progressbar['value'] = percent
            self.percentage_label.config(text=f"進行中: {int(percent)}%")
            self.root.update_idletasks()

    def reset_progress(self):
        self.progressbar['value'] = 0
        self.percentage_label.config(text="進行中: 0%")
        self.root.update_idletasks()

    def downloadpush(self):
        ids = self.TextBox1.get().split(' ')
        if len(ids) == 1:
            url = f'https://music.youtube.com/watch?v={ids[0]}'
        elif len(ids) == 2:
            url = f'https://music.youtube.com/watch?v={ids[0]}&list={ids[1]}'
        else:
            messagebox.showwarning("入力エラー", "IDを正しく入力してください。")
            return

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
            'outtmpl': 'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/%(title)s.%(ext)s',
            'progress_hooks': [self.update_progress_bar],
            'noplaylist': True,
        }

        self.reset_progress()
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.percentage_label.config(text="完了済み: ダウンロードが完了しました！")
            messagebox.showinfo("成功", "ダウンロードが成功しました！")
        except Exception as e:
            self.progressbar.stop()
            self.percentage_label.config(text="エラー: ダウンロードに失敗しました。")
            messagebox.showerror("エラー", f"エラーが発生しました: {e}")
            traceback.print_exc()


if __name__ == "__main__":
    root = Tk()
    ks903_Music_downloder_JP(root)
