import yt_dlp
import traceback
from animate_i2con import animate_i2con  # animate_icon関数をインポート
from tkinter import *
from tkinter import messagebox, ttk

class ISongsKS_903DownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("iSongs Downloader Marketer Music Stores")
        self.root.geometry("500x300")
        self.setup_fonts()
        self.create_widgets()
        self.bind_events()

    def setup_fonts(self):
        self.font_large = ('Arial', 14)
        self.font_medium = ('Arial', 12)
        self.font_small = ('Arial', 10)
        self.font_nano = ('Arial', 9)

    def create_widgets(self):
        # アニメーションを適用
        gif_path = r'image\music\base\bese_icon\ico.gif'
        animate_i2con(self.root, gif_path)

        # 進行状況ラベル
        self.percentage_label = Label(self.root, text="進行中: 0%", font=self.font_medium)
        self.percentage_label.pack_forget()  # 初期状態では非表示

        # テキストボックス
        self.textbox = Entry(self.root, width=50, fg='grey', bg='white', font=self.font_small)
        self.textbox.insert(0, "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:")
        self.textbox.pack(pady=20)

        # ダウンロードボタン
        self.download_button = Button(self.root, text="音楽のダウンロードを開始", command=self.download_push)
        self.download_button.pack()

        # 進行状況バー
        self.progressbar = ttk.Progressbar(self.root, style="green.Horizontal.TProgressbar", mode='determinate')
        self.setup_styles()

    def setup_styles(self):
        style = ttk.Style()
        style.configure("green.Horizontal.TProgressbar", thickness=20, troughcolor='lightgrey', background='green')

    def bind_events(self):
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        self.root.bind('<q>', self.close_window)
        self.textbox.bind('<FocusIn>', self.on_focus)
        self.textbox.bind('<FocusOut>', self.on_focus_out)
        self.textbox.bind('<Return>', self.on_enter_key)
        self.textbox.bind('<KeyPress>', self.on_key_press)
        self.textbox.bind('<ButtonRelease-1>', self.move_cursor_to_start)

    def display_status_message(self, message, delay=2000):
        self.percentage_label.config(text=message, font=self.font_nano)
        self.percentage_label.pack(pady=5, side=TOP)
        self.root.update_idletasks()
        self.root.after(delay, self.hide_and_revert_font)

    def hide_and_revert_font(self):
        self.percentage_label.pack_forget()
        self.percentage_label.config(font=self.font_medium)

    def update_progress_bar(self, d):
        if d['status'] == 'downloading':
            percent = d.get('downloaded_bytes') / d.get('total_bytes') * 100
            self.progressbar['value'] = percent
            self.percentage_label.config(text=f"進行中: {int(percent)}%")
            self.root.update_idletasks()

    def reset_progress(self):
        self.progressbar['value'] = 0
        self.percentage_label.config(text="進行中: 0%")
        self.progressbar.pack(pady=10)
        self.percentage_label.pack(pady=5, side=TOP)
        self.root.update_idletasks()

    def hide_progress(self):
        self.percentage_label.pack_forget()
        self.progressbar.pack_forget()

    def sanitize_filename(self, filename):
        invalid_chars = '<>:"/\\|?*'
        return ''.join(c for c in filename if c not in invalid_chars)

    def ytdownload(self, ID, ID2=None):
        url = f'https://music.youtube.com/watch?v={ID}{ID2}'
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav', 'preferredquality': '192',}],
            'outtmpl': 'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/%(title)s.%(ext)s',
            # 'outtmpl': 'C:/Users/user/wav/%(title)s.%(ext)s',
            
            'progress_hooks': [self.update_progress_bar],
            'noplaylist': True,
        }

        self.reset_progress()
        self.progressbar.start()

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                title = self.sanitize_filename(info.get('title', 'default_title'))
                # output_path = f'C:/Users/user/wav/{title}.wav'
                # C:\Users\PC\Desktop\ミュージックプレーヤー(正式版)\audio\song_imusic_song
                # output_path = f'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{title}.wav'
                output_path = f'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{title}.%(ext)s'

                ydl_opts['outtmpl'] = output_path
                ydl = yt_dlp.YoutubeDL(ydl_opts)
                ydl.download([url])

            self.percentage_label.config(text="進行中済み: 完了しました")
            messagebox.showinfo("成功", "ダウンロードが成功しました！")
        except Exception as e:
            self.progressbar.stop()
            self.hide_progress()
            messagebox.showerror("エラー", f"エラーが発生しました: {e}")
            self.display_status_message("進行中  ＥＲＲＯＲ: エラーが発生しました。ダウンロード進行を緊急停止しました。")
            traceback.print_exc()
        finally:
            self.progressbar.stop()
            self.root.update_idletasks()
            self.root.after(3000, self.percentage_label.pack_forget)

    def download_push(self, event=None):
        ids = self.textbox.get().split('  ')
        if len(ids) == 2:
            self.hide_progress()
            self.reset_progress()
            ID, ID2 = ids
            self.ytdownload(ID, ID2)
            self.textbox.delete(0, END)
            self.textbox.insert(0, "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:")
            self.textbox.config(fg='grey', bg='white')
        else:
            messagebox.showwarning("入力エラー", "IDを'2回スペースで区切って下さい'で区切って入力してください")

    def on_focus(self, event):
        if self.textbox.get() == "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:":
            self.textbox.config(bg='lightyellow')
        self.move_cursor_to_start(event)

    def on_focus_out(self, event):
        if self.textbox.get() == '':
            self.textbox.insert(0, "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:")
            self.textbox.config(fg='grey', bg='white')

    def on_key_press(self, event):
        if self.textbox.get() == "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:":
            self.textbox.delete(0, END)
            self.textbox.config(fg='black')

    def on_enter_key(self, event):
        self.download_button.config(relief=SUNKEN)
        self.root.after(100, self.download_button.invoke)
        self.root.after(200, lambda: self.download_button.config(relief=RAISED))

    def move_cursor_to_start(self, event=None):
        self.textbox.icursor(0)

    def close_window(self, event=None):
        self.root.destroy()


if __name__ == "__main__":
    #  root = Tk()
    #root = Toplevel()
    # app = ISongsKS_903DownloaderApp(root)
    # root.mainloop()
    ISongsKS_903DownloaderApp()

