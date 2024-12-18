import yt_dlp
import traceback
from animate_i2con import animate_i2con  # animate_icon関数をインポート
from tkinter import *
from tkinter import messagebox, ttk
from tkinter import Tk, Label, TOP

def display_status_message(message, delay=2000):
    # Create the label with a specific font size
    # font_size = 9  # You can change this to your desired font size
    # percentage_label.config(text=message, font=("Arial", font_size))
    percentage_label.config(text=message, font=font_nano)
    percentage_label.pack(pady=5, side=TOP)  # Show the label
    root.update_idletasks()
    # root.after(delay, lambda: percentage_label.pack_forget())
    # Hide the label after the specified delay and revert the font
    root.after(delay, hide_and_revert_font)


def hide_and_revert_font():
    percentage_label.pack_forget()
    percentage_label.config(font=font_medium)

# メインウィンドウの作成
root = Tk()
root.title("iSongs Downloaders Marketer Music Stores")  # ウィンドウのタイトル
# root.iconbitmap(r'image\music\base\bese_icon\codemy.ico')# アイコン読み込み
# GIFファイルのパスアイコン読み込み
gif_path = r'image\music\base\bese_icon\ico.gif'
# アニメーションを適用アイコン読み込み
animate_i2con(root, gif_path)
root.geometry("500x300")  # ウィンドウのサイズ (幅x高さ)

# フォントとサイズの設定
font_large = ('Arial', 14)  # 大きなフォント
font_medium = ('Arial', 12)  # 中くらいのフォント
font_small = ('Arial', 10)   # 小さなフォント
font_nano = ('Arial', 9)   # 超小さなフォント



# パーセンテージ表示ラベル
percentage_label = Label(root, text="進行中: 0%", font=font_medium)
percentage_label.pack(pady=5, side=TOP, anchor="n")  # Ensure it's at the top
# Example call to the function
display_status_message("Loading...", delay=2000)

# システムを閉じる
def close_window(event=None):
    animate_window_close()  # Run animation before closing the window
# def close_window(event):
    # Finally destroy the window
    # root.destroy()

def animate_window_close():
    # Create a temporary button to simulate the "×" button click animation
    temp_button = Button(root, text="×", relief=SUNKEN, bg='red', fg='white', font=font_large)
    temp_button.place(x=472, y=-0)  # Place the button at a specific location
    root.update_idletasks()  # Update the GUI
    root.after(100, lambda: (temp_button.config(relief=RAISED, bg='SystemButtonFace', fg='black'), root.update_idletasks()))  # Reset button relief and color
    root.after(200, lambda: (temp_button.place_forget(), root.destroy()))  # Remove button and close window after delay

# 進行状況バーの作成
progressbar = ttk.Progressbar(root, style="green.Horizontal.TProgressbar", mode='determinate')

def update_progress_bar(d):
    if d['status'] == 'downloading':
        percent = d.get('downloaded_bytes') / d.get('total_bytes') * 100
        progressbar['value'] = percent
        percentage_label.config(text=f"進行中: {int(percent)}%")
        root.update_idletasks()  # Update the GUI


# スタイルの設定
style = ttk.Style()
style.configure("green.Horizontal.TProgressbar",
                thickness=20,  # バーの厚さ
                troughcolor='lightgrey',  # バーの背景色
                background='green')  # バーの色


def reset_progress():
    progressbar['value'] = 0  # Reset progress bar
    percentage_label.config(text="進行中: 0%")  # Reset label text
    progressbar.pack(pady=10)  # Ensure progress bar is displayed
    percentage_label.pack(pady=5, side=TOP)  # Ensure percentage label is displayed
    root.update_idletasks()  # Update the GUI

def hide_progress():
    percentage_label.pack_forget()  # Hide the percentage label
    progressbar.pack_forget()  # Hide the progress bar


def sanitize_filename(filename):
    """Sanitize the filename to remove or replace invalid characters."""
    # Define invalid characters for filenames
    invalid_chars = '<>:"/\\|?*'
    sanitized = ''.join(c for c in filename if c not in invalid_chars)
    return sanitized

def ytdownload(ID, ID2=None):
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
        'outtmpl': 'C:/Users/user/wav/%(title)s.%(ext)s',  # Use title for output path
        'progress_hooks': [update_progress_bar] , # Add progress hook to track progress
        'noplaylist': True,  # Ensure we're only downloading one video   
    }

    

    reset_progress()  # Reset progress before starting new download
    progressbar.start()  # Start progress bar

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract information without downloading
            info = ydl.extract_info(url, download=False)
            title = sanitize_filename(info.get('title', 'default_title' ,))
            
            # Update output path with the sanitized title
            # output_path = f'audio/song_imusic_song/music_song/{title}.wav'
            # C:/Users/user/wav/ 
            output_path = f' C:/Users/user/wav/{title}.wav'
            # Download the video
            ydl_opts['outtmpl'] = output_path
            ydl = yt_dlp.YoutubeDL(ydl_opts)
            ydl.download([url])
        
        # Print the output path after the download is complete
        print(f"Download completed. Output file is saved at: {output_path}")

       
        percentage_label.config(text="進行中済み: 完了しました")
        messagebox.showinfo("成功", "ダウンロードが成功しました！")
        percentage_label.config(text="完了済み: ダウンロードが完了!!終了ました!!!")
    except Exception as e:
        progressbar.stop()  # Stop the progress bar
        hide_progress()  # Hide the progress bar and percentage label
        messagebox.showerror("エラー", f"エラーが発生しました: {e}であるため再度やり直ししてください!!")
        display_status_message("進行中  ＥＲＲＯＲ: エラーが発生しました。ダウンロード進行を緊急停止しました。")
        print("エラーの詳細:")
        traceback.print_exc()
    finally:
        # Stop progress bar and ensure the GUI updates
        progressbar.stop()
        root.update_idletasks()
        root.after(3000, lambda: percentage_label.pack_forget())  # Hide the label after 3 seconds

def downloadpush(event=None):
    ids = TextBox1.get().split('  ')
    if len(ids) == 2:
        hide_progress()  # Hide any existing progress bar and label
        reset_progress()  # Display the progress bar and label
        ID, ID2 = ids
        ytdownload(ID, ID2)
        TextBox1.delete(0, END)  # Clear the text box after download
        TextBox1.insert(0, "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:")
        TextBox1.config(fg='grey', bg='white')  # Reset text color and background
        # Ensure the cursor is at the start if it's a placeholder
        if TextBox1.get() == "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:":
            move_cursor_to_start()  # Move cursor to the start
    else:
        messagebox.showwarning("入力エラー", "IDを'2回スペースで区切って下さい'で区切って入力してください")

def move_cursor_to_start(event=None):
    TextBox1.icursor(0)  # Move cursor to the start of the text box

def TextBox1_on_key_press(event):
    if TextBox1.get() == "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:":
        TextBox1.delete(0, END)
        TextBox1.config(fg='black')
        

def TextBox1_on_focus(event):
    if TextBox1.get() == "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:":
        TextBox1.config(bg='lightyellow')  # Change text color and background when focused
    move_cursor_to_start(event)  # Ensure cursor is at the start

def TextBox1_on_focusout(event):
    if TextBox1.get() == '':
        TextBox1.insert(0, "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:")
        TextBox1.config(fg='grey', bg='white')  # Reset text color and background




def on_enter_key(event):
    Button1.config(relief=SUNKEN)  # Simulate button press by changing relief to SUNKEN
    root.after(100, lambda: Button1.invoke())  # Invoke button command after a short delay
    root.after(200, lambda: Button1.config(relief=RAISED))  # Reset button relief after a short delay

# テキストボックスの作成
TextBox1 = Entry(root, width=50, fg='grey', bg='white', font=font_small)
TextBox1.insert(0, "YOUTUBE_MUSIC_ID_&&_List_ID_User Name:")  # プレースホルダーテキスト
TextBox1.bind('<FocusIn>', TextBox1_on_focus)
TextBox1.bind('<ButtonRelease-1>', move_cursor_to_start)  # Use ButtonRelease-1 to ensure cursor moves after click
TextBox1.bind('<FocusOut>', TextBox1_on_focusout)
TextBox1.bind('<Return>', downloadpush)  # Enterキーでdownloadpush関数を呼び出す
# ボタンをエンターキーにバインド
TextBox1.bind('<Return>', on_enter_key)


on_key_press_id = TextBox1.bind('<KeyPress>', TextBox1_on_key_press)

# パーセンテージ表示ラベルの表示位置を確保
percentage_label.pack_forget()  # 初期状態ではラベルを非表示

# テキストボックスを表示
TextBox1.pack(pady=20)

# ダウンロードボタンの作成
Button1 = Button(root, text="音楽のダウンロードを開始", command=downloadpush)

Button1.pack()


# # ウィンドウの閉じるボタン（バツ印）をカスタム処理
# root.protocol("WM_DELETE_WINDOW", close_window)

# ウィンドウの閉じるボタン（バツ印）をカスタム処理
# root.protocol("WM_DELETE_WINDOW", close_window)


# `q`キーでウィンドウを閉じる
root.bind('<q>', close_window)
# Tkinterのイベントループ開始
root.mainloop()
