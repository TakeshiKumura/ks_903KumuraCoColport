# imusic_beta.py
# -*- coding: utf-8 -*-
import pygame
import time 
import sys
import tkinter.ttk as ttk 
from tkinter import *
from tkinter import filedialog 
from tkinter import PhotoImage
from animate_i4con import animate_i4con  
from mutagen.wave import WAVE 
# リソースのパスを取得する関数
def get_resource_path(relative_path):
    # EXE化後のリソースを参照するためのパスの設定
    if getattr(sys, 'frozen', False):
        # PyInstallerで実行されている場合
        base_path = sys._MEIPASS  # PyInstallerで実行されている場合
    else:
        # 開発環境で実行されている場合
        base_path = sys.argv[0]  # スクリプトのパス
    # base_path と relative_path を手動で結合
    return base_path + '\\' + relative_path  # Windowsのパス区切りを手動で指定
# 音楽のメタデータを取得する関数（mutagenを使用）
def get_audio_metadata(file_path):
    audio = WAVE(file_path)
    return audio.info  # 音声ファイルの情報（長さ、ビットレートなど）
root = Tk()
root.title('iSongs Music Media Player')
gif_path = r'image\music\base\bese_icon\ico.gif'
animate_i4con(root, gif_path)
root.geometry("860x500") 
pygame.mixer.init()
def play_time():
    if stopped:
        return
    current_time = pygame.mixer.music.get_pos() / 1000  # 再生中の経過時間
    status_bar.config(text=current_time) 
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))
    # 選択されている曲を取得
    song_current = song_box.get(ACTIVE)  
    # 曲のパスを取得 (get_resource_path を使う)
    song_current_path = get_resource_path(fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{song_current}.wav')  
    # 曲の情報を取得（WAVEオブジェクトなどを使って曲の長さを取得）
    song_mut = WAVE(song_current_path)  # 必要に応じてライブラリを確認・変更  
    global song_length
    song_length = song_mut.info.length
    converted_current_length = time.strftime('%M:%S', time.gmtime(song_length))  # 曲の長さを表示 
    current_time += 1  # 1秒進める（更新するため）
    # 経過時間とスライダーを管理
    if int(my_slider.get()) == int(song_length):
        # 曲が終了した場合
        status_bar.config(text=f'Time Elapsed: {converted_current_length} ')
    elif paused:
        # 一時停止中の場合
        pass
    elif int(my_slider.get()) == int(current_time):
        # スライダーの位置を現在の時間に合わせる
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(current_time))
    else:
        # スライダーを更新し、経過時間を表示
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(my_slider.get()))  
        converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))
        status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_current_length}') 
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)
    # 1秒ごとに `play_time` を再実行
    status_bar.after(1000, play_time)
def add_song():
    song = filedialog.askopenfilename(initialdir=r'audio\song_imusic_song\music_song', title= "choose A song(曲選択パターン　A　１曲単体ずつ選ぶこと) ", filetypes=(("wav Files", "*.wav"),  )) # [CMDS:Ctrl+Shift+O@参照]", filetypes=(("wav Files", "*.wav"),  )) #song = filedialog.askopenfilename(initialdir=r'audio\song_music_song\music_song', title= "choose A song(曲選択パターン　A　１曲単体ずつ選ぶこと)", filetypes=(("wav Files", "*.wav"),  ))
    print("選択した曲のパス:", song)
    # パスが選択されなかった場合
    if not song:
        print("ファイルが選択されませんでした")
        return 
    # パスの正規化（すべてスラッシュに変換）
    song = song.replace("\\", "/")
    # パスの一部を削除して、ファイル名を取り出す
    song = song.replace("C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/", "") #song = song.replace("C:/Users/user/wav/", "")
    song = song.replace(".wav", "")
    # EXE化後に正しいリソースパスを取得するために get_resource_path を使う
    song_path = get_resource_path(f"audio/song_imusic_song/music_song/{song}.wav") 
    # 曲のパスを表示
    print("リソースのパス:", song_path)
    # 曲名をGUIに追加（例: `song_box` がリストボックスのようなウィジェットである場合）
    song_box.insert(END, song)
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir=r'audio\song_imusic_song\music_song', title= "All_Add Many Songs To Playlist(沢山及び数多く複数の曲をプレイリストから追加できることをする)", filetypes=(("wav Files", "*.wav"),  )) # [CMDS:Ctrl+Shift+A@参照]", filetypes=(("wav Files", "*.wav"),  ))#"choose A song(曲選択パターン　A　１曲単体ずつ選ぶこと)", filetypes=(("wav Files", "*.wav"),  )) #song = filedialog.askopenfilename(initialdir=r'audio\song_music_song\music_song', title= "choose A song(曲選択パターン　A　１曲単体ずつ選ぶこと)", filetypes=(("wav Files", "*.wav"),  ))
    # songs = filedialog.askopenfilenames(initialdir=r'audio\song_imusic_song\music_song', title= "choose A song(曲選択パターン　A　１曲単体ずつ選ぶこと)", filetypes=(("wav Files", "*.wav"),  )) # songs = filedialog.askopenfilenames(initialdir=r'audio\song_music_song\music_song', title= "choose A song(曲選択パターン　A　１曲単体ずつ選ぶこと)", filetypes=(("wav Files", "*.wav"),  ))
    # それぞれの選択された曲に対して処理を行う
    print("選択した曲のリスト:", songs)
    # 複数選択された曲に対して処理を行う
    for song in songs:
        # フルパスからファイル名部分を抽出
        song_name = song.replace("C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/", "")
        song_name = song_name.replace(".wav", "")       
        # EXE化後に正しいリソースパスを取得するために get_resource_path を使う
        song_path = get_resource_path(f"audio/song_imusic_song/music_song/{song_name}.wav")  
        # 曲のリソースパスを表示
        print("曲のリソースパス:", song_path)      
        # 曲名をGUIのリストボックスに追加（例: `song_box` がリストボックスのようなウィジェットである場合）
        song_box.insert(END, song_name)

# 音楽を再生する関数
def play():
    global stopped
    stopped = False
    # 曲の選択
    song = song_box.get(ACTIVE)
    song = get_resource_path(fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{song}.wav')
    # 曲をロードして再生
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=-1)  # 無限ループで再生
    # 再生時間を表示する関数を呼び出す
    play_time()
    # 現在の音量を取得してパーセントに変換
    current_volume = pygame.mixer.music.get_volume() * 100
    # 音量に基づいてボリュームメーターを更新
    if int(current_volume) < 1:
        volume_meter.config(image=volas4)
    elif int(current_volume) <= 12.5:
        volume_meter.config(image=vol4)
    elif int(current_volume) <= 25:
        volume_meter.config(image=volas3)
    elif int(current_volume) <= 37.5:
        volume_meter.config(image=vol3)
    elif int(current_volume) <= 50:
        volume_meter.config(image=volas2)
    elif int(current_volume) <= 62.5:
        volume_meter.config(image=vol2)
    elif int(current_volume) <= 75:
        volume_meter.config(image=volas1)
    elif int(current_volume) <= 87.5:
        volume_meter.config(image=vol1)
    elif int(current_volume) <= 100:
        volume_meter.config(image=vol0)            
global stopped
stopped = False    
def stop():
    status_bar.config(text='')
    my_slider.config(value=0)
    pygame.mixer.music.stop() 
    song_box.select_clear(ACTIVE) 
    status_bar.config(text='停止中: 曲を停止させました')
    status_bar.after(2000, lambda: status_bar.config(text=''))
    global stopped
    stopped = True
def next_song():
    status_bar.config(text='')
    my_slider.config(value=0)
    next_one = song_box.curselection()
    print(next_one) 
    print(next_one[0])
    next_one = next_one[0]+1
    songl = song_box.get(next_one)
    print(songl)
    songll = get_resource_path(fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{songl}.wav')
    pygame.mixer.music.load(songll) 
    pygame.mixer.music.play(loops=-1)
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one,  last=None)
def previous_song():
    status_bar.config(text='')
    my_slider.config(value=0)
    next_one = song_box.curselection()
    print(next_one) 
    print(next_one[0]) 
    next_one = next_one[0]-1 
    songl = song_box.get(next_one)
    print(songl)
    songll = get_resource_path(fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{songl}.wav')
    pygame.mixer.music.load(songll) 
    pygame.mixer.music.play(loops=-1)
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one,  last=None)
def delete_song():
    stop()
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()
def delete_all_songs():
    stop()
    song_box.delete(0, END)
    pygame.mixer.music.stop()
global paused
paused = False  
paused_position = 0  
def pause(is_paused):
    global paused, paused_position
    if paused:
        start_playing_from_position(paused_position)  
        pygame.mixer.music.unpause()
        status_bar.config(text='再生中: 曲を再生しています')          
        paused = False  
        status_bar.after(2000, lambda: status_bar.config(text='先ほどの停止した位置から再開させます'))
        status_bar.after(4000, lambda: status_bar.config(text=''))
    else: 
        paused_position = get_current_position() 
        pygame.mixer.music.pause()  
        status_bar.config(text='一時停止中: 曲を一時停止させました')  
        paused = True  
        status_bar.after(2000, lambda: status_bar.config(text=''))
def get_current_position():
    return pygame.mixer.music.get_pos() // 1000
def start_playing_from_position(position):
        pygame.mixer.music.play(start=position)  
def slide(x):
    song = song_box.get(ACTIVE)
    # song = f'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{song}.wav'
    song = get_resource_path(fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{song}.wav')
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=-1, start=int(my_slider.get()))
# 長押し判定のための変数
key_hold_timer = {"left": None, "right": None}  # タイマーIDを保持
key_pressed = {"left": False, "right": False}
def skip_song(direction):
    """
    再生位置を4秒進めたり戻したりする関数。
    `direction`は "left" または "right" を指定。
    """
    # 現在の再生位置を取得
    current_position = pygame.mixer.music.get_pos() / 1000  # ミリ秒を秒に変換
    # 再生位置を更新
    if direction == "left":
        new_position = max(0, current_position - 4)  # 4秒戻る
    elif direction == "right":
        new_position = min(song_length, current_position + 4)  # 4秒進む
    pygame.mixer.music.set_pos(new_position)  # 再生位置を直接指定
    my_slider.set(new_position)  # スライダーも更新
    status_bar.config(text=f'経過時間: {time.strftime("%M:%S", time.gmtime(new_position))} / {time.strftime("%M:%S", time.gmtime(song_length))}')
    # キーがまだ押されている場合、再びこの関数を呼び出す
    if key_pressed[direction]:
        key_hold_timer[direction] = root.after(1000, skip_song, direction)
def on_key_press(event):
    """
    矢印キーが押された時の処理。
    長押しかどうかを判定するため、タイマーを設定する。
    """
    direction = "left" if event.keysym == "Left" else "right"
    if not key_pressed[direction]:
        key_pressed[direction] = True
        # 500ms（0.5秒）後に長押し処理を開始
        key_hold_timer[direction] = root.after(500, skip_song, direction)
def on_key_release(event):
    """
    矢印キーが離された時の処理。
    短押しか長押しかで動作を分ける。
    """
    direction = "left" if event.keysym == "Left" else "right"
    key_pressed[direction] = False
    # 長押しタイマーをキャンセル
    if key_hold_timer[direction] is not None:
        root.after_cancel(key_hold_timer[direction])
        key_hold_timer[direction] = None
    # 短押しの場合は即座に4秒スキップ
    if not key_pressed["left"] and not key_pressed["right"]:
        skip_song(direction)
# メニューを表示するための関数
def show_add_song_menu(event):
    add_song_menu.post(event.x_root, event.y_root)
def show_remove_song_menu(event):
    remove_song_menu.post(event.x_root, event.y_root)
def show_handtrakingmove_menu(event):
    handtrakingmove_menu.post(event.x_root, event.y_root)
def show_Help_menu(event):
    Help_menu.post(event.x_root, event.y_root)
# キーボード操作を追加
def setup_keyboard_shortcuts():
    root.bind("<space>", lambda event: pause(paused))  # スペースキーで一時停止/再開
    root.bind("<Right>", lambda event: next_song())  # →キーで次の曲
    root.bind("<Left>", lambda event: previous_song())  # ←キーで前の曲
    root.bind("<Return>", lambda event: play())  # Enterキーで再生
    root.bind("<BackSpace>", lambda event: stop())  # バックスペースキーで停止
        # メニュー関連のショートカット
      #  メニュー自体表示
    root.bind("<Control-A>", show_add_song_menu)  
    root.bind("<Control-B>", show_remove_song_menu)
    root.bind("<Control-H>", show_handtrakingmove_menu)  
    root.bind("<Control-Q>", show_Help_menu)
      # メニューの中身    
    root.bind("<Control-Shift-O>", lambda event: add_song())  # Ctrl + Shift + O
    root.bind("<Control-Shift-A>", lambda event: add_many_songs())  # Ctrl + Shift + A
    root.bind("<Control-Shift-G>", lambda event: new_song_dl())  # Ctrl + Shift + G
    root.bind("<Control-Shift-R>", lambda event: ptp_song())  # Ctrl + Shift + R
    root.bind("<Control-Shift-P>", lambda event: delete_song())  # Ctrl + Shift + P
    root.bind("<Control-Shift-B>", lambda event: delete_all_songs())  # Ctrl + Shift + B
    root.bind("<Control-Shift-H>", lambda event: hands_track())  # Ctrl + Shift + H
    root.bind("<Control-Shift-F>", lambda event: fase_track())  # Ctrl + Shift + F
    root.bind("<Control-Shift-Q>", lambda event: help_gaids())  # Ctrl + Shift + Q  
    # Page Up と Page Down に音量の増減を割り当てます。Volume control via Page Up and Page Down
    root.bind("<Prior>", lambda event: change_volume(0.01))  # Page Upで音量+1% Page Up to increase volume by 1%
    root.bind("<Next>", lambda event: change_volume(-0.01))  # Page Downで音量-1% Page Down to decrease volume by 1%  
    # キーのバインド
    root.bind("<Left>", on_key_press)  # 左矢印キーを押した時
    root.bind("<Right>", on_key_press)  # 右矢印キーを押した時
    root.bind("<KeyRelease-Left>", on_key_release)  # 左矢印キーを離した時
    root.bind("<KeyRelease-Right>", on_key_release)  # 右矢印キーを離した時
# Function to change volume and update the slider
def change_volume(amount):
    # Get the current volume (from 0.0 to 1.0)
    current_volume = pygame.mixer.music.get_volume()
    # new_volume = max(0.0, min(1.0, current_volume + amount))  # Clamp to the range [0, 1]
    new_volume = max(0.0, min(1.0, current_volume - amount))  # Clamp to the range [0, 1]
    # Set the new volume
    pygame.mixer.music.set_volume(new_volume)
    # Update the volume meter and volume_slider to reflect the new volume
    volume(new_volume)  # Update the volume display (meter)
    volume_slider.set(new_volume)  # Sync the volume slider with the volume change
# Updated volume function to sync volume slider
def volume(x=None):
    # Convert x to float if it's not None
    if x is not None:
        x = float(x)
        pygame.mixer.music.set_volume(x)  
    current_volume = pygame.mixer.music.get_volume() * 100  
    if current_volume < 1:
        volume_meter.config(image=volas4)
    elif current_volume <= 12.5:
        volume_meter.config(image=vol4)
    elif current_volume <= 25:
        volume_meter.config(image=volas3)
    elif current_volume <= 37.5:
        volume_meter.config(image=vol3)
    elif current_volume <= 50:
        volume_meter.config(image=volas2)
    elif current_volume <= 62.5:
        volume_meter.config(image=vol2)
    elif current_volume <= 75:
        volume_meter.config(image=volas1)
    elif current_volume <= 87.5:
        volume_meter.config(image=vol1)
    else:
        volume_meter.config(image=vol0)
def new_song_dl():
     pass
def ptp_song():
     pass
def hands_track():
     pass
def fase_track():
     pass
def help_gaids():
     pass
master_frame = Frame(root)
master_frame.pack(pady=10)
song_box = Listbox(master_frame, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
song_box.grid(row=0, column=0) 
# back_btn_img = PhotoImage(file=r'image\music\base\back50.png')
# forward_btn_img = PhotoImage(file=r'image\music\base\forward50.png')
# play_btn_img = PhotoImage(file=r'image\music\base\play50.png')
# pause_btn_img = PhotoImage(file=r'image\music\base\pause50.png')
# stop_btn_img = PhotoImage(file=r'image\music\base\stop50.png')
# 画像ファイルのパスを取得
back_btn_img = PhotoImage(file=get_resource_path(r'image\music\base\back50.png'))
forward_btn_img = PhotoImage(file=get_resource_path(r'image\music\base\forward50.png'))
play_btn_img = PhotoImage(file=get_resource_path(r'image\music\base\play50.png'))
pause_btn_img = PhotoImage(file=get_resource_path(r'image\music\base\pause50.png'))
stop_btn_img = PhotoImage(file=get_resource_path(r'image\music\base\stop50.png'))
global vol0
global vol1
global volas1
global vol2
global volas2
global vol3
global volas3
global vol4
global volas4
# vol0 = PhotoImage(file=r'image\music\base\volume0.png')
# vol1 = PhotoImage(file=r'image\music\base\volume1.png')
# volas1 = PhotoImage(file=r'image\music\base\volume1a.png')
# vol2 = PhotoImage(file=r'image\music\base\volume2.png')
# volas2 = PhotoImage(file=r'image\music\base\volume2a.png')
# vol3 = PhotoImage(file=r'image\music\base\volume3.png')
# volas3 = PhotoImage(file=r'image\music\base\volume3a.png')
# vol4 = PhotoImage(file=r'image\music\base\volume4.png')
# # volas4 = PhotoImage(file=r'image\music\base\volume4a.png')
vol0 = PhotoImage(file=get_resource_path(r'image\music\base\volume0.png'))
vol1 = PhotoImage(file=get_resource_path(r'image\music\base\volume1.png'))
volas1 = PhotoImage(file=get_resource_path(r'image\music\base\volume1a.png'))
vol2 = PhotoImage(file=get_resource_path(r'image\music\base\volume2.png'))
volas2 = PhotoImage(file=get_resource_path(r'image\music\base\volume2a.png'))
vol3 = PhotoImage(file=get_resource_path(r'image\music\base\volume3.png'))
volas3 = PhotoImage(file=get_resource_path(r'image\music\base\volume3a.png'))
vol4 = PhotoImage(file=get_resource_path(r'image\music\base\volume4.png'))
volas4 = PhotoImage(file=get_resource_path(r'image\music\base\volume4a.png'))
controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0, pady=20)
volume_meter = Label(master_frame, image=vol0)
volume_meter.grid(row=2, column=1, padx=40)
volume_frame = LabelFrame(master_frame,  text="Volume")
volume_frame.grid(row=0,  column=1, padx=30)
back_button = Button(controls_frame, image=back_btn_img, borderwidth=0, command=previous_song)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)
back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=0)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)
my_menu = Menu(root)
root.config(menu=my_menu)
# add_song_menu = Menu(my_menu)
# 「Add Songs」メニュー作成
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Add Songs  (曲のリストを追加する) [CMND:Ctrl+A@参照]", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist(一つずつ曲をプレイリストから追加する) [CMDS:Ctrl+Shift+O@参照]", command=add_song)
add_song_menu.add_command(label="All_Add Many Songs To Playlist(沢山及び数多く複数の曲をプレイリストから追加できることをする) [CMDS:Ctrl+Shift+A@参照]", command=add_many_songs)
add_song_menu.add_command(label="Add New Songs To Buyting Downloders(新規の曲を購入してプレイリストに登録する) [CMDS:Ctrl+Shift+G@参照]", command=new_song_dl)
add_song_menu.add_command(label="PC TO MUSICPlayer TO Pear to Pear Upload(PCの曲を無線で音楽プレーヤーに転送して取り入れる) [CMDS:Ctrl+Shift+R@参照]", command=ptp_song)
# remove_song_menu = Menu(my_menu)
# 「Remove Songs」メニュー作成
remove_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Remove Songs(プレイリストをボックスから消去する) [CMND:Ctrl+B@参照]",menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song From Playlist(追加したプレイリストから一つずつボックスから消去する) [CMDS:Ctrl+Shift+P@参照]", command=delete_song)
remove_song_menu.add_command(label="Delete A Song From Playlist(追加したプレイリストをすべてボックスから消去する) [CMDS:Ctrl+Shift+B@参照]", command=delete_all_songs)
# 「Hand Traking Moves」メニュー作成
handtrakingmove_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Hand Traking Move Songs(指文字から操作する) [CMND:Ctrl+H@参照]",menu=handtrakingmove_menu)
handtrakingmove_menu.add_command(label="Auto　Hand Traking Move Songs Startup Contlorl Penal(指文字操作コントロールパネル起動する) [CMDS:Ctrl+Shift+H@参照]", command=hands_track)
handtrakingmove_menu.add_command(label="Enable Face Recognition Security Lock(顔認証安全ロックを有効にする) [CMDS:Ctrl+Shift+F@参照]", command=fase_track)
# 「Helping」メニュー作成
Help_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Help(この概要について) [CMND:Ctrl+Q@参照]",menu=Help_menu)
Help_menu.add_command(label="Auto　How To User　ManuaL(使い方についてご説明) [CMDS:Ctrl+Shift+Q@参照]", command=help_gaids)
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E )
status_bar.pack(fill=X, side=BOTTOM, ipady=2)
my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.grid(row=2,  column=0,  pady=30)
# スライダーの設定
volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, command=volume, length=165)
volume_slider.set(0.5)  # 初期音量50%
volume_slider.pack(pady=10)
# 初期化の最後にショートカット設定を呼び出す
setup_keyboard_shortcuts()
root.mainloop()
