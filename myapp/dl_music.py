import yt_dlp
import traceback
from animate_i2con import animate_i2con  # animate_icon関数をインポート
from tkinter import *
from tkinter import messagebox, ttk
from tkinter import Tk, Label, TOP


class ks903_Music_downloder_JP:
   def __init__(self,  root):    


        # メインウィンドウの作成
        # self.root = Tk()
        # メインウィンドウの作成
        self.root = root
        self.root.title("iSongs Downloaders Marketer Music Stores")  # ウィンドウのタイトル
        # root.iconbitmap(r'image\music\base\bese_icon\codemy.ico')# アイコン読み込み
        self.root.geometry("500x300")  # ウィンドウのサイズ (幅x高さ)

        # フォントとサイズの設定
        self.font_large = ('Arial', 14)  # 大きなフォント
        self.font_medium = ('Arial', 12)  # 中くらいのフォント
        self.font_small = ('Arial', 10)   # 小さなフォント
        self.font_nano = ('Arial', 9)   # 超小さなフォント


        # GIFファイルのパスアイコン読み込み
        gif_path = r'image\music\base\bese_icon\ico.gif'
        # アニメーションを適用アイコン読み込み
        animate_i2con(self.root, gif_path)
        
        # GUI要素の設定
        self.percentage_label = Label(self.root, text="進行中: 0%", font=('Arial', 12))
        self.percentage_label.pack(pady=5, side=TOP, anchor="n")

        
        # スタイルの設定
        self.style = ttk.Style()
        self.style.configure("green.Horizontal.TProgressbar",
                        thickness=20,  # バーの厚さ
                        troughcolor='lightgrey',  # バーの背景色
                        background='green')  # バーの色
        
        # テキストボックス
        self.TextBox1 = Entry(self.root, width=50, fg='grey', bg='white', font=self.font_small)
        self.TextBox1.insert(0, "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:")   
        self.TextBox1.bind('<FocusIn>', self.TextBox1_on_focus) # TextBox1_on_focus)
        self.TextBox1.bind('<FocusOut>', self.TextBox1_on_focusout)  # フォーカスアウトイベント TextBox1_on_focusout)
        self.TextBox1.pack(pady=20)


        # ダウンロードボタン
        self.Button1 = Button(self.root, text="音楽のダウンロードを開始", command=downloadpush)
        self.Button1.pack()

        # 閉じる処理
        self.root.protocol("WM_DELETE_WINDOW", close_window)
        self.root.bind('<q>', close_window)

        # イベントループ開始
        self.root.mainloop()

        # パーセンテージ表示ラベル
        # self.percentage_label = Label(self.root, text="進行中: 0%", font=self.font_medium)
        # 進行状況バーの作成
        self.progressbar = ttk.Progressbar(self.root, style="green.Horizontal.TProgressbar", mode='determinate')
        self.progressbar.pack(pady=10)
        # self.percentage_label.pack(pady=5, side=TOP, anchor="n")  # Ensure it's at the top
        # Example call to the function
        # self.display_status_message("Loading...", delay=2000)
        

        # # # 閉じるボタンのカスタム設定
        # # self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        
        # # 他の初期化コード
        # self.TextBox1 = Entry(self.root, width=50, fg='grey', bg='white', font=self.font_small)
        # self.TextBox1.insert(0, "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:")
        # self.TextBox1.pack(pady=20)


        def display_status_message(self,   message,  delay=2000):
            # Create the label with a specific font size
            # font_size = 9  # You can change this to your desired font size
            # percentage_label.config(text=message, font=("Arial", font_size))
            self.percentage_label.config(text=message, font=self.font_nano)
            self.percentage_label.pack(pady=5, side=TOP)  # Show the label
            self.root.update_idletasks()
            # root.after(delay, lambda: percentage_label.pack_forget())
            # Hide the label after the specified delay and revert the font
            self.root.after(delay, hide_and_revert_font)


        def hide_and_revert_font(self):
            self.percentage_label.pack_forget()
            self.percentage_label.config(font=('Arial', 12))#font_medium)

        
        # システムを閉じる
        def close_window(event=None):
            animate_window_close()  # Run animation before closing the window
        # def close_window(event):
            # Finally destroy the window
            # root.destroy()

        def animate_window_close(self):
            # Create a temporary button to simulate the "×" button click animation
            self.temp_button = Button(self.root, text="×", relief=SUNKEN, bg='red', fg='white', font=self.font_large)
            self.temp_button.place(x=472, y=-0)  # Place the button at a specific location
            self.root.update_idletasks()  # Update the GUI
            self.root.after(100, lambda: (self.temp_button.config(relief=RAISED, bg='SystemButtonFace', fg='black'), self.root.update_idletasks()))  # Reset button relief and color
            self.root.after(200, lambda: (self.temp_button.place_forget(), self.root.destroy()))  # Remove button and close window after delay

        
        def update_progress_bar(self, d):
            if d['status'] == 'downloading':
                percent = d.get('downloaded_bytes', 0) / d.get('total_bytes', 1) * 100
                self.progressbar['value'] = percent
                self.percentage_label.config(text=f"進行中: {int(percent)}%")
                self.root.update_idletasks()  # Update the GUI


        

        def reset_progress(self):
            self.progressbar['value'] = 0  # Reset progress bar
            self.percentage_label.config(text="進行中: 0%")  # Reset label text
            self.progressbar.pack(pady=10)  # Ensure progress bar is displayed
            self.percentage_label.pack(pady=5, side=TOP)  # Ensure percentage label is displayed
            self.root.update_idletasks()  # Update the GUI

        def hide_progress(self):
            self.percentage_label.pack_forget()  # Hide the percentage label
            self.progressbar.pack_forget()  # Hide the progress bar


        def sanitize_filename(self, filename):
            """Sanitize the filename to remove or replace invalid characters."""
            # Define invalid characters for filenames
            self.invalid_chars = '<>:"/\\|?*'
            sanitized = ''.join(c for c in filename if c not in self.invalid_chars)
            return sanitized

        def ytdownload(self, ID, ID2=None):
            url = f'https://music.youtube.com/watch?v={ID}{ID2}'
            # url = f'https://music.youtube.com/watch?v={ID}'
            # if ID2:
            #     url += f'&list={ID2}'
            #  output_path = r'audio\song_imusic_song\music_song\{d}.wav'.format(d=ID)  # 出力パスが正しいことを確認してください

            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                    'preferredquality': '192',
                }],
                # 'outtmpl': 'audio/song_imusic_song/music_song/%(title)s.%(ext)s',  # Use title for output path
                #         C:\Users\user\wav
                # 'outtmpl': 'C:/Users/user/wav/%(title)s.%(ext)s',  # Use title for output path
                'outtmpl': 'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/%(title)s.%(ext)s',  # Use title for output path
                'progress_hooks': [update_progress_bar] , # Add progress hook to track progress
                'noplaylist': True,  # Ensure we're only downloading one video   
            }

            

            self.reset_progress()  # Reset progress before starting new download
            self.progressbar.start()  # Start progress bar

            try:
                with yt_dlp.YoutubeDL(self, ydl_opts) as ydl:
                    # Extract information without downloading
                    info = ydl.extract_info(url, download=False)
                    title = sanitize_filename(info.get('title', 'default_title'))
                    
                    # Update output path with the sanitized title
                    # output_path = f'audio/song_imusic_song/music_song/{title}.wav'
                    # C:/Users/user/wav/ 
                    # output_path = f' C:/Users/user/wav/{title}.wav'
                    output_path = f' C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/{title}.wav'
                    
                    
                    # Download the video
                    ydl_opts['outtmpl'] = output_path
                    ydl = yt_dlp.YoutubeDL(ydl_opts)
                    ydl.download([url])
                
                # Print the output path after the download is complete
                print(f"Download completed. Output file is saved at: {output_path}")

            
                self.percentage_label.config(text="進行中済み: 完了しました")
                messagebox.showinfo("成功", "ダウンロードが成功しました！")
                self.percentage_label.config(text="完了済み: ダウンロードが完了!!終了ました!!!")
            except Exception as e:
                self.progressbar.stop()  # Stop the progress bar
                hide_progress()  # Hide the progress bar and percentage label
                messagebox.showerror("エラー", f"エラーが発生しました: {e}であるため再度やり直ししてください!!")
                display_status_message("進行中  ＥＲＲＯＲ: エラーが発生しました。ダウンロード進行を緊急停止しました。")
                print("エラーの詳細:")
                traceback.print_exc()
            finally:
                # Stop progress bar and ensure the GUI updates
                self.progressbar.stop()
                self.root.update_idletasks()
                self.root.after(3000, lambda: self.percentage_label.pack_forget())  # Hide the label after 3 seconds

        def downloadpush(self,  event=None ):
            ids = self.TextBox1.get().split('  ')
            if len(ids) == 2:
                hide_progress()  # Hide any existing progress bar and label
                reset_progress()  # Display the progress bar and label
                ID, ID2 = ids
                ytdownload(ID, ID2)
                self.TextBox1.delete(0, END)  # Clear the text box after download
                self.TextBox1.insert(0, "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:")
                self.TextBox1.config(fg='grey', bg='white')  # Reset text color and background
                # Ensure the cursor is at the start if it's a placeholder
                if self.TextBox1.get() == "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:":
                    move_cursor_to_start()  # Move cursor to the start
            else:
                messagebox.showwarning("入力エラー", "IDを'2回スペースで区切って下さい'で区切って入力してください")

        def move_cursor_to_start(self, event=None):
            self.TextBox1.icursor(0)  # Move cursor to the start of the text box

        def TextBox1_on_key_press(self, event):
            if self.TextBox1.get() == "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:":
                self.TextBox1.delete(0, END)
                self.TextBox1.config(fg='black')
                

        # def TextBox1_on_focus(self, event):
        #     if self.TextBox1.get() == "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:":
        #         self.TextBox1.config(bg='lightyellow')  # Change text color and background when focused
        #     move_cursor_to_start(event)  # Ensure cursor is at the start

        # def TextBox1_on_focusout(self, event):
        #     if self.TextBox1.get() == '':
        #         self.TextBox1.insert(0, "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:")
        #         self.TextBox1.config(fg='grey', bg='white')  # Reset text color and background

        def TextBox1_on_focus(self, event):
            """フォーカスが当たったときの処理"""
        if self.TextBox1.get() == self.placeholder_text:
            self.TextBox1.delete(0, END)
            self.TextBox1.config(fg='black')

        def TextBox1_on_focusout(self, event):
            """フォーカスが外れたときの処理"""
            if self.TextBox1.get() == '':
                self.TextBox1.insert(0, self.placeholder_text)
                self.TextBox1.config(fg='grey')



        def on_enter_key(self, event):
            self.Button1.config(relief=SUNKEN)  # Simulate button press by changing relief to SUNKEN
            self.root.after(100, lambda: self.Button1.invoke())  # Invoke button command after a short delay
            self.root.after(200, lambda: self.Button1.config(relief=RAISED))  # Reset button relief after a short delay

        # テキストボックスの作成
        self.TextBox1 = Entry(self.root, width=50, fg='grey', bg='white', font=self.font_small)
        self.TextBox1.insert(0, "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:")  # プレースホルダーテキスト
        self.TextBox1.bind('<FocusIn>', TextBox1_on_focus)
        self.TextBox1.bind('<ButtonRelease-1>', move_cursor_to_start)  # Use ButtonRelease-1 to ensure cursor moves after click
        self.TextBox1.bind('<FocusOut>', TextBox1_on_focusout)
        self.TextBox1.bind('<Return>', downloadpush)  # Enterキーでdownloadpush関数を呼び出す
        # ボタンをエンターキーにバインド
        self.TextBox1.bind('<Return>', on_enter_key)


        # on_key_press_id = self.TextBox1.bind('<KeyPress>', TextBox1_on_key_press)

        # パーセンテージ表示ラベルの表示位置を確保
        self.percentage_label.pack_forget()  # 初期状態ではラベルを非表示

        # テキストボックスを表示
        self.TextBox1.pack(pady=20)

        # ダウンロードボタンの作成
        self.Button1 = Button(self.root, text="音楽のダウンロードを開始", command=downloadpush)

        self.Button1.pack()


        # # ウィンドウの閉じるボタン（バツ印）をカスタム処理
        # root.protocol("WM_DELETE_WINDOW", close_window)

        # ウィンドウの閉じるボタン（バツ印）をカスタム処理
        # root.protocol("WM_DELETE_WINDOW", close_window)


        # `q`キーでウィンドウを閉じる
        self.root.bind('<q>', close_window)
        # Tkinterのイベントループ開始
        self.root.mainloop()

if __name__ == "__main__":
    ks903_Music_downloder_JP(root)
    