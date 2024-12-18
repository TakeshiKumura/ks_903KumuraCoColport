# imusic_beta.py
# -*- coding: utf-8 -*-
import pygame
import time 
import tkinter.ttk as ttk 
from tkinter import *
from tkinter import filedialog 
from tkinter import PhotoImage
from tkinter import Menu
from dl_music import ISongsKS_903DownloaderApp
from animate_i2con import animate_i2con  
from mutagen.wave import WAVE 

import sys

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
animate_i2con(root, gif_path)
root.geometry("860x500") 
pygame.mixer.init()
# def play_time():
#     if stopped:
#         return
#     current_time = pygame.mixer.music.get_pos() /1000
#     status_bar.config(text=current_time)
#     converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))
#     song_culrrent = song_box.get(ACTIVE) 
#     # songlcurrnt = fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{song_culrrent}.wav'  #songlcurrnt = fr'C:/Users/user/wav/{song_culrrent}.wav' 
#     songlcurrnt = get_resource_path(fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{songlcurrnt}.wav')

#     song_mut = WAVE(songlcurrnt)
#     global song_length
#     song_length = song_mut.info.length
#     converted_current_length = time.strftime('%M:%S', time.gmtime(song_length)) 
#     current_time += 1
#     if int(my_slider.get()) ==   int(song_length):
#         status_bar.config(text=f'Time Elapsed:  {converted_current_length} ')
#     elif paused:
#         pass
#     elif int(my_slider.get()) == int(current_time ):
#         slider_position = int(song_length)
#         my_slider.config(to=slider_position,  value=int(current_time))
#     else:
#         slider_position = int(song_length)
#         my_slider.config(to=slider_position,  value=int(my_slider.get()))

#         converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get()))) 

#         status_bar.config(text=f'Time Elapsed:  {converted_current_time}  of  {converted_current_length} ')

#         next_time = int(my_slider.get()) + 1
#         my_slider.config(value=next_time)
#     status_bar.after(1000, play_time)

def play_time():
    if stopped:
        return

    current_time = pygame.mixer.music.get_pos() / 1000  # 再生中の経過時間
    status_bar.config(text=current_time)
    
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))
    
    # 選択されている曲を取得
    song_current = song_box.get(ACTIVE)  
    
    # 曲のパスを取得 (get_resource_path を使う)
    # song_current_path = get_resource_path(fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{song_current}.wav')
    song_current_path = fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{song_current}.wav'
    
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
    # song_path = get_resource_path(f"audio/song_imusic_song/music_song/{song}.wav")
    
    # 曲のパスを表示
    # print("リソースのパス:", song_path)
    
    # 曲名をGUIに追加（例: `song_box` がリストボックスのようなウィジェットである場合）
    song_box.insert(END, song)

def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir=r'audio\song_imusic_song\music_song', title= "All_Add Many Songs To Playlist(沢山及び数多く複数の曲をプレイリストから追加できることをする)", filetypes=(("wav Files", "*.wav"),  )) # [CMDS:Ctrl+Shift+A@参照]", filetypes=(("wav Files", "*.wav"),  ))#"choose A song(曲選択パターン　A　１曲単体ずつ選ぶこと)", filetypes=(("wav Files", "*.wav"),  )) #song = filedialog.askopenfilename(initialdir=r'audio\song_music_song\music_song', title= "choose A song(曲選択パターン　A　１曲単体ずつ選ぶこと)", filetypes=(("wav Files", "*.wav"),  ))
    #  songs = filedialog.askopenfilenames(initialdir=r'audio\song_imusic_song\music_song', title= "choose A song(曲選択パターン　A　１曲単体ずつ選ぶこと)", filetypes=(("wav Files", "*.wav"),  )) # songs = filedialog.askopenfilenames(initialdir=r'audio\song_music_song\music_song', title= "choose A song(曲選択パターン　A　１曲単体ずつ選ぶこと)", filetypes=(("wav Files", "*.wav"),  ))
    # それぞれの選択された曲に対して処理を行う
    print("選択した曲のリスト:", songs)

    # 複数選択された曲に対して処理を行う
    for song in songs:
        # フルパスからファイル名部分を抽出
        song_name = song.replace("C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/", "")
        song_name = song_name.replace(".wav", "")
        
        # EXE化後に正しいリソースパスを取得するために get_resource_path を使う
        # song_path = get_resource_path(f"audio/song_imusic_song/music_song/{song_name}.wav")
        
        # 曲のリソースパスを表示
        # print("曲のリソースパス:", song_path)
        
        # 曲名をGUIのリストボックスに追加（例: `song_box` がリストボックスのようなウィジェットである場合）
        song_box.insert(END, song_name)
def play():
    global stopped
    stopped = False
    song = song_box.get(ACTIVE)
    song = fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{song}.wav'  # song = fr'C:/Users/user/wav/{song}.wav'   
    # song = get_resource_path(fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{song}.wav')

    pygame.mixer.music.load(song) 
    pygame.mixer.music.play(loops=-1)
    play_time()
    current_volume = pygame.mixer.music.get_volume()
    current_volume = current_volume * 100
    # if int(current_volume) < 1:
    #     volume_meter.config(image=vol0)
    # elif int(current_volume) > 0 and int(current_volume) <= 12.5:
    #     volume_meter.config(image=vol1)
    # elif int(current_volume) > 12.5 and int(current_volume) <= 25:
    #     volume_meter.config(image=volas1)
    # elif int(current_volume) >= 25 and int(current_volume) <= 37.5:
    #         volume_meter.config(image=vol2)
    # elif int(current_volume) >= 37.5 and int(current_volume) <= 50:
    #         volume_meter.config(image=volas2)
    # elif int(current_volume) >= 50 and int(current_volume) <= 62.5:
    #         volume_meter.config(image=vol3)
    # elif int(current_volume) >= 62.5 and int(current_volume) <= 75:
    #         volume_meter.config(image=volas3)
    # elif int(current_volume) >= 75 and int(current_volume) <= 87.5:
    #         volume_meter.config(image=vol4)
    # elif int(current_volume) >= 87.5 and int(current_volume) <= 100:
    #         volume_meter.config(image=volas4)

    if int(current_volume) < 1:
        volume_meter.config(image=volas4)
    elif int(current_volume) > 0 and int(current_volume) <= 12.5:
        volume_meter.config(image=vol4)
    elif int(current_volume) > 12.5 and int(current_volume) <= 25:
        volume_meter.config(image=volas3)
    elif int(current_volume) >= 25 and int(current_volume) <= 37.5:
            volume_meter.config(image=vol3)
    elif int(current_volume) >= 37.5 and int(current_volume) <= 50:
            volume_meter.config(image=volas2)
    elif int(current_volume) >= 50 and int(current_volume) <= 62.5:
            volume_meter.config(image=vol2)
    elif int(current_volume) >= 62.5 and int(current_volume) <= 75:
            volume_meter.config(image=volas1)
    elif int(current_volume) >= 75 and int(current_volume) <= 87.5:
            volume_meter.config(image=vol1)
    elif int(current_volume) >= 87.5 and int(current_volume) <= 100:
            volume_meter.config(image=vol0)



# # 音楽を再生する関数
# def play():
#     global stopped
#     stopped = False

#     # 曲の選択
#     song = song_box.get(ACTIVE)
#     song = get_resource_path(fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{song}.wav')

#     # 曲をロードして再生
#     pygame.mixer.music.load(song)
#     pygame.mixer.music.play(loops=-1)  # 無限ループで再生

#     # 再生時間を表示する関数を呼び出す
#     play_time()

#     # 現在の音量を取得してパーセントに変換
#     current_volume = pygame.mixer.music.get_volume() * 100

#     # 音量に基づいてボリュームメーターを更新
#     if int(current_volume) < 1:
#         volume_meter.config(image=volas4)
#     elif int(current_volume) <= 12.5:
#         volume_meter.config(image=vol4)
#     elif int(current_volume) <= 25:
#         volume_meter.config(image=volas3)
#     elif int(current_volume) <= 37.5:
#         volume_meter.config(image=vol3)
#     elif int(current_volume) <= 50:
#         volume_meter.config(image=volas2)
#     elif int(current_volume) <= 62.5:
#         volume_meter.config(image=vol2)
#     elif int(current_volume) <= 75:
#         volume_meter.config(image=volas1)
#     elif int(current_volume) <= 87.5:
#         volume_meter.config(image=vol1)
#     elif int(current_volume) <= 100:
#         volume_meter.config(image=vol0)



            
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
    songll = fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{songl}.wav'  # songll = fr'C:/Users/user/wav/{songl}.wav'   
    # songll = get_resource_path(fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{songl}.wav')

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
    songll = fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{songl}.wav'  # songll = fr'C:/Users/user/wav/{songl}.wav' 
    # songll = get_resource_path(fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)audio/song_imusic_song/music_song/{songl}.wav')
    #  songll = get_resource_path(fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{songl}.wav')

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
    song = f'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{song}.wav'
    #  song = get_resource_path(fr'C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song/{song}.wav')

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




# Add Songs メニュー作成
def show_add_song_menu(event=None):
    add_song_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Add Songs (曲のリストを追加する) [CMND:Ctrl+A@参照]", menu=add_song_menu)
    add_song_menu.add_command(label="Add One Song To Playlist (一つずつ曲をプレイリストから追加する) [CMDS:Ctrl+Shift+O@参照]", command=add_song)
    add_song_menu.add_command(label="Add Many Songs To Playlist (沢山及び数多く複数の曲をプレイリストから追加できることをする) [CMDS:Ctrl+Shift+A@参照]", command=add_many_songs)
    add_song_menu.add_command(label="Add New Songs To Buying Downloaders (新規の曲を購入してプレイリストに登録する) [CMDS:Ctrl+Shift+G@参照]", command=new_song_dl)
    add_song_menu.add_command(label="PC to MusicPlayer to Peer to Peer Upload (PCの曲を無線で音楽プレーヤーに転送して取り入れる) [CMDS:Ctrl+Shift+R@参照]", command=ptp_song)
    add_song_menu.post(event.x_root, event.y_root)  # マウス位置にメニューを表示

# Remove Songs メニュー作成
def show_remove_song_menu(event=None):
    remove_song_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Remove Songs (プレイリストをボックスから消去する) [CMND:Ctrl+B@参照]", menu=remove_song_menu)
    remove_song_menu.add_command(label="Delete A Song From Playlist (追加したプレイリストから一つずつボックスから消去する) [CMDS:Ctrl+Shift+P@参照]", command=delete_song)
    remove_song_menu.add_command(label="Delete All Songs From Playlist (追加したプレイリストをすべてボックスから消去する) [CMDS:Ctrl+Shift+B@参照]", command=delete_all_songs)
    remove_song_menu.post(event.x_root, event.y_root)  # マウス位置にメニューを表示

# Hand Tracking Move Songs メニュー作成
def show_handtrakingmove_menu(event=None):
    handtrakingmove_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Hand Tracking Move Songs (指文字から操作する) [CMND:Ctrl+H@参照]", menu=handtrakingmove_menu)
    handtrakingmove_menu.add_command(label="Auto Hand Tracking Move Songs Startup Control Panel (指文字操作コントロールパネル起動する) [CMDS:Ctrl+Shift+H@参照]", command=hands_track)
    handtrakingmove_menu.add_command(label="Enable Face Recognition Security Lock (顔認証安全ロックを有効にする) [CMDS:Ctrl+Shift+F@参照]", command=fase_track)
    handtrakingmove_menu.post(event.x_root, event.y_root)  # マウス位置にメニューを表示

# Help メニュー作成
def show_help_menu(event=None):
    help_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Help (この概要について) [CMND:Ctrl+Q@参照]", menu=help_menu)
    help_menu.add_command(label="How To Use Manual (使い方についてご説明) [CMDS:Ctrl+Shift+Q@参照]", command=help_gaids)
    help_menu.post(event.x_root, event.y_root)  # マウス位置にメニューを表示

    


# キーボード操作を追加
def setup_keyboard_shortcuts():
    # root.bind("<space>", lambda event: pause(paused))  # スペースキーで一時停止/再開
    # root.bind("<Right>", lambda event: next_song())  # →キーで次の曲
    # root.bind("<Left>", lambda event: previous_song())  # ←キーで前の曲
    # root.bind("<Return>", lambda event: play())  # Enterキーで再生
    # root.bind("<BackSpace>", lambda event: stop())  # バックスペースキーで停止


    # 深み効果をバインドする
    root.bind("<Left>", lambda event: (add_depth(back_button), previous_song())) # ←キーで前の曲
    root.bind("<KeyRelease-Left>", lambda event: remove_depth(back_button))      # ←キーで前の曲(深みアニメーション)

    root.bind("<Right>", lambda event: (add_depth(forward_button), next_song())) # →キーで次の曲
    root.bind("<KeyRelease-Right>", lambda event: remove_depth(forward_button))  # →キーで次の曲(深みアニメーション)

    root.bind("<Return>", lambda event: (add_depth(play_button), play()))        # Enterキーで再生     
    root.bind("<KeyRelease-Return>", lambda event: remove_depth(play_button))    # Enterキーで再生(深みアニメーション) 
    root.bind("<space>", lambda event: (add_depth(pause_button), pause(None)))  # スペースキーで一時停止/再開
    root.bind("<KeyRelease-space>", lambda event: remove_depth(pause_button))   # スペースキーで一時停止/再開(深みアニメーション)


    root.bind("<BackSpace>", lambda event: (add_depth(stop_button), stop()))    # バックスペースキーで停止
    root.bind("<KeyRelease-BackSpace>", lambda event: remove_depth(stop_button)) # バックスペースキーで停止(深みアニメーション)

    #     # メニュー関連のショートカット
      #  メニュー自体表示
      # ショートカットキーをバインド
    root.bind("<Control-A>", lambda event: show_add_song_menu(event))
    root.bind("<Control-B>", lambda event: show_remove_song_menu(event))
    root.bind("<Control-H>", lambda event: show_handtrakingmove_menu(event))
    root.bind("<Control-Q>", lambda event: show_help_menu(event))
    # root.bind("<Control-A>", show_add_song_menu)  
    # root.bind("<Control-B>", show_remove_song_menu)
    # root.bind("<Control-H>", show_handtrakingmove_menu)  
    # root.bind("<Control-Q>", show_Help_menu)
    #   # メニューの中身    
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
    # root.bind("<Left>", on_key_press)  # 左矢印キーを押した時
    # root.bind("<Right>", on_key_press)  # 右矢印キーを押した時
    # root.bind("<KeyRelease-Left>", on_key_release)  # 左矢印キーを離した時
    # root.bind("<KeyRelease-Right>", on_key_release)  # 右矢印キーを離した時

    
    # root.bind("<Prior>", lambda event: volume(0.01))  # Page Upで音量+1%
    # root.bind("<Next>", lambda event: volume(-0.01))  # Page Downで音量-1%

# 音量変更関数
def change_volume(amount):
    current_volume = pygame.mixer.music.get_volume()
    new_volume = max(0.0, min(1.0, current_volume + amount))
    pygame.mixer.music.set_volume(new_volume)
    volume(new_volume)
    volume_slider.set(new_volume)

    # スライダー色を変更
    change_slider_color(new_volume)  # 音量に基づいて色を変える

# 音量表示関数
def volume(x=None):
    if x is not None:
        pygame.mixer.music.set_volume(x)  # 音量設定

    current_volume = pygame.mixer.music.get_volume() * 100

    if current_volume < 1:
        volume_meter.config(image=vol0)
    elif current_volume <= 12.5:
        volume_meter.config(image=vol1)
    elif current_volume <= 25:
        volume_meter.config(image=volas1)
    elif current_volume <= 37.5:
        volume_meter.config(image=vol2)
    elif current_volume <= 50:
        volume_meter.config(image=volas2)
    elif current_volume <= 62.5:
        volume_meter.config(image=vol3)
    elif current_volume <= 75:
        volume_meter.config(image=volas3)
    elif current_volume <= 87.5:
        volume_meter.config(image=vol4)
    else:
        volume_meter.config(image=volas4)

# スライダーの動きに応じて音量を変更する関数
def on_slider_motion(event):
    new_volume = volume_slider.get()
    pygame.mixer.music.set_volume(new_volume)
    volume(new_volume)
    print(f"Volume changed to: {new_volume:.2f}")
    change_slider_color(new_volume)

# スライダーのつまみ部分の色を音量に基づいて変更
def change_slider_color(volume_value):
    r = int((1 - volume_value) * 255)  # 音量が低いほど赤に近づく
    b = int(volume_value * 255)        # 音量が高いほど青に近づく
    color = f'#{r:02x}{0:02x}{b:02x}'  # 赤紫から青紫へのグラデーションカラー

    # スライダーのスタイルを変更
    style.configure("Custom.Horizontal.TScale", sliderlength=30, foreground=color)


# # スライダーの色を音量に基づいて変更
# def change_slider_color(volume_value):
#     # 音量に応じた色を選択
#     r = int((1 - volume_value) * 255)  # 音量が低いほど赤に近づく
#     b = int(volume_value * 255)        # 音量が高いほど青に近づく
#     color = f'#{r:02x}{0:02x}{b:02x}'  # 赤紫から青紫へのグラデーションカラー

#     # スライダーの色を変更（tk.Scale）
#     volume_slider.config(troughcolor=color)  # 進行バーの色を変更
#     volume_slider.config(activebackground=color)  # アクティブ部分の色を変更


# # 音量変更関数
# def change_volume(amount):
#     # 現在の音量を取得
#     current_volume = pygame.mixer.music.get_volume()

#     # 音量を増減させた新しい値を計算（スライダー方向逆転処理）
#     new_volume = max(0.0, min(1.0, current_volume + amount))

#     # 音量変更があれば設定
#     pygame.mixer.music.set_volume(new_volume)

#     # 音量メーターとスライダーを更新
#     volume(new_volume)
#     volume_slider.set(new_volume)

#     # # スライダー色を変更
#     # change_slider_color("purple")  # 音量変更時に紫に変更
#     # スライダー色を変更
#     change_slider_color(new_volume)  # 音量に基づいて色を変える


#     print(f"Volume changed to: {new_volume:.2f}")

# # 音量表示関数
# def volume(x=None):
#     if x is not None:
#         pygame.mixer.music.set_volume(x)  # 音量設定

#     # 現在の音量をパーセントで取得
#     current_volume = pygame.mixer.music.get_volume() * 100

#     # 音量メーターを現在の音量に合わせて更新
#     if current_volume < 1:
#         volume_meter.config(image=vol0)
#     elif current_volume <= 12.5:
#         volume_meter.config(image=vol1)
#     elif current_volume <= 25:
#         volume_meter.config(image=volas1)
#     elif current_volume <= 37.5:
#         volume_meter.config(image=vol2)
#     elif current_volume <= 50:
#         volume_meter.config(image=volas2)
#     elif current_volume <= 62.5:
#         volume_meter.config(image=vol3)
#     elif current_volume <= 75:
#         volume_meter.config(image=volas3)
#     elif current_volume <= 87.5:
#         volume_meter.config(image=vol4)
#     else:
#         volume_meter.config(image=volas4)

# # スライダーの動きに応じて音量を変更する関数
# # def on_slider_motion(event):
# #     # スライダーの現在の値を取得して音量を設定（逆に反映する）
# #     new_volume = volume_slider.get()  # スライダー値そのまま使う（上が最小0, 下が最大1）
# #     pygame.mixer.music.set_volume(new_volume)  # 音量を設定
# #     volume(new_volume)  # 音量メーターを更新
# #     print(f"Volume changed to: {new_volume:.2f}")  # デバッグ出力

# # # # スライダー色を変更
# # #     change_slider_color("purple")  # 音量変更時に紫に変更
# #     # スライダー色を変更
# #     change_slider_color(new_volume)  # 音量に基づいて色を変える

# # # スライダーの色を変更する関数
# # def change_slider_color(color):
# #     volume_slider.config(fg=color)  # スライダーの色を指定の色に変更



# # # スライダーの色を音量に基づいて変更
# # def change_slider_color(volume_value):
# #     # 音 スライダーの色を音量に基づいて変更
# # スライダーの動きに応じて音量を変更する関数
# def on_slider_motion(event):
#     # スライダーの現在の値を取得して音量を設定（逆に反映する）
#     new_volume = volume_slider.get()  # スライダー値そのまま使う（上が最小0, 下が最大1）
#     pygame.mixer.music.set_volume(new_volume)  # 音量を設定
#     volume(new_volume)  # 音量メーターを更新
#     print(f"Volume changed to: {new_volume:.2f}")  # デバッグ出力

#     # スライダー色を変更
#     change_slider_color(new_volume)  # 音量に基づいて色を変える

# # スライダーの色を音量に基づいて変更
# def change_slider_color(volume_value):
#     # 音量に応じた色を選択
#     r = int((1 - volume_value) * 255)  # 音量が低いほど赤に近づく
#     b = int(volume_value * 255)        # 音量が高いほど青に近づく
#     color = f'#{r:02x}{0:02x}{b:02x}'  # 赤紫から青紫へのグラデーションカラー

#     # Styleを使ってスライダーの色を変更
#     style = ttk.Style()
#     style.configure("TScale",
#                     troughcolor=color,  # バーの色を変更
#                     sliderlength=25)    # スライダーの長さを調整

#     volume_slider.configure(style="TScale")


#     r = int((1 - volume_value) * 255)  # 音量が低いほど赤に近づく
#     b = int(volume_value * 255)        # 音量が高いほど青に近づく
#     color = f'#{r:02x}{0:02x}{b:02x}'  # 赤紫から青紫へのグラデーションカラー
#     volume_slider.config(troughcolor=color)  # スライダーの進行バーの色を変更
#     # volume_slider.config(fg=color)  # スライダーの色を変更


# # Function to change volume and update the slider
# def change_volume(amount):
#     # Get the current volume (from 0.0 to 1.0)
#     current_volume = pygame.mixer.music.get_volume()
#     print(f"Current volume: {current_volume}")  # Debugging output

#     # Calculate the new volume, ensuring it's between 0.0 and 1.0
#     new_volume = max(0.0, min(1.0, current_volume + amount))  # Increase or decrease volume

#     # Set the new volume
#     pygame.mixer.music.set_volume(new_volume)

#     # Update the volume meter and volume_slider to reflect the new volume
#     volume(new_volume)  # Update the volume display (meter)
#     volume_slider.set(new_volume)  # Sync the volume slider with the volume change

#     print(f"Volume changed to: {new_volume:.2f}")  # Debugging output

# # Updated volume function to sync volume slider
# def volume(x=None):
#     if x is not None:
#         x = float(x)  # Ensure the value is a float

#         # Set the new volume directly (no need for inversion)
#         pygame.mixer.music.set_volume(x)

#     # Get the current volume as a percentage (0-100)
#     current_volume = pygame.mixer.music.get_volume() * 100

#     # Update the volume meter based on the current volume
#     if current_volume < 1:
#         volume_meter.config(image=vol0)
#     elif current_volume <= 12.5:
#         volume_meter.config(image=vol1)
#     elif current_volume <= 25:
#         volume_meter.config(image=volas1)
#     elif current_volume <= 37.5:
#         volume_meter.config(image=vol2)
#     elif current_volume <= 50:
#         volume_meter.config(image=volas2)
#     elif current_volume <= 62.5:
#         volume_meter.config(image=vol3)
#     elif current_volume <= 75:
#         volume_meter.config(image=volas3)
#     elif current_volume <= 87.5:
#         volume_meter.config(image=vol4)
#     else:
#         volume_meter.config(image=volas4)

# # Function to change volume and update the slider
# def change_volume(amount):
#     # Get the current volume (from 0.0 to 1.0)
#     current_volume = pygame.mixer.music.get_volume() * 1
#     print(current_volume * 0.1)
#     # new_volume = max(0.0, min(1.0, current_volume + amount))  # Clamp to the range [0, 1]

#     new_volume = max(0.0, min(1.0, current_volume - amount))  # Clamp to the range [0, 1]

#     # Set the new volume
#     pygame.mixer.music.set_volume(new_volume)

#     # Update the volume meter and volume_slider to reflect the new volume
#     volume(new_volume)  # Update the volume display (meter)
#     volume_slider.set(new_volume)  # Sync the volume slider with the volume change

#     # print(f"Volume changed to: {new_volume:.2f}")  # Optional: print the volume for debugging


# # Updated volume function to sync volume slider
# def volume(x=None):
#     # Convert x to float if it's not None
#     if x is not None:
#         x = float(x)
#         # pygame.mixer.music.set_volume(x)
#         # print(1.0- x)
#         # Reverse the volume control: 1 - x
#         c = (1.0 - x)  # Round to 2 decimal places to reduce fluctuations
#         print(c)
        
#         pygame.mixer.music.set_volume(c)
#         # print(1 - x)

    
#     current_volume = pygame.mixer.music.get_volume() * 100  # Get volume as a percentage
    
# #    Update the volume meter based on the current volume
#     if current_volume < 1:
#         volume_meter.config(image=vol0)
#     elif current_volume <= 12.5:
#         volume_meter.config(image=vol1)
#     elif current_volume <= 25:
#         volume_meter.config(image=volas1)
#     elif current_volume <= 37.5:
#         volume_meter.config(image=vol2)
#     elif current_volume <= 50:
#         volume_meter.config(image=volas2)
#     elif current_volume <= 62.5:
#         volume_meter.config(image=vol3)
#     elif current_volume <= 75:
#         volume_meter.config(image=volas3)
#     elif current_volume <= 87.5:
#         volume_meter.config(image=vol4)
#     else:
#         volume_meter.config(image=volas4)


    # # # Update the volume meter based on the current volume
    # if current_volume < 1:
    #     volume_meter.config(image=volas4)
    # elif current_volume <= 12.5:
    #     volume_meter.config(image=vol4)
    # elif current_volume <= 25:
    #     volume_meter.config(image=volas3)
    # elif current_volume <= 37.5:
    #     volume_meter.config(image=vol3)
    # elif current_volume <= 50:
    #     volume_meter.config(image=volas2)
    # elif current_volume <= 62.5:
    #     volume_meter.config(image=vol2)
    # elif current_volume <= 75:
    #     volume_meter.config(image=volas1)
    # elif current_volume <= 87.5:
    #     volume_meter.config(image=vol1)
    # else:
    #     volume_meter.config(image=vol0)

def new_song_dl():
    root = Toplevel()
    ISongsKS_903DownloaderApp(root)
    root.mainloop()
#     new_window = ISongsKS_903DownloaderApp(root) # downloadファイルです 別ウィンドウにアプリケーションクラスをロード
#   # 新しいウィンドウを作成
#     new_window.title("iSongs Downloader Marketer Music Stores")  # タイトル設定
#     new_window.geometry("500x300")  # サイズ設定
#     ISongsKS_903DownloaderApp(root) # downloadファイルです 別ウィンドウにアプリケーションクラスをロード


# ボタンの見た目を変える関数
def add_depth(button):
    button.config(relief="sunken")  # ボタンを沈めた状態にする

def remove_depth(button):
    button.config(relief="flat")  # ボタンを平坦な状態に戻す

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
back_btn_img = PhotoImage(file=r'image\music\base\back50.png')
forward_btn_img = PhotoImage(file=r'image\music\base\forward50.png')
play_btn_img = PhotoImage(file=r'image\music\base\play50.png')
pause_btn_img = PhotoImage(file=r'image\music\base\pause50.png')
stop_btn_img = PhotoImage(file=r'image\music\base\stop50.png')


# 画像ファイルのパスを取得
# back_btn_img = PhotoImage(file=get_resource_path(r'image\music\base\back50.png'))
# forward_btn_img = PhotoImage(file=get_resource_path(r'image\music\base\forward50.png'))
# play_btn_img = PhotoImage(file=get_resource_path(r'image\music\base\play50.png'))
# pause_btn_img = PhotoImage(file=get_resource_path(r'image\music\base\pause50.png'))
# stop_btn_img = PhotoImage(file=get_resource_path(r'image\music\base\stop50.png'))

global vol0
global vol1
global volas1
global vol2
global volas2
global vol3
global volas3
global vol4
global volas4
vol0 = PhotoImage(file=r'image\music\base\volume0.png')
vol1 = PhotoImage(file=r'image\music\base\volume1.png')
volas1 = PhotoImage(file=r'image\music\base\volume1a.png')
vol2 = PhotoImage(file=r'image\music\base\volume2.png')
volas2 = PhotoImage(file=r'image\music\base\volume2a.png')
vol3 = PhotoImage(file=r'image\music\base\volume3.png')
volas3 = PhotoImage(file=r'image\music\base\volume3a.png')
vol4 = PhotoImage(file=r'image\music\base\volume4.png')
volas4 = PhotoImage(file=r'image\music\base\volume4a.png')
# vol0 = PhotoImage(file=get_resource_path(r'image\music\base\volume0.png'))
# vol1 = PhotoImage(file=get_resource_path(r'image\music\base\volume1.png'))
# volas1 = PhotoImage(file=get_resource_path(r'image\music\base\volume1a.png'))
# vol2 = PhotoImage(file=get_resource_path(r'image\music\base\volume2.png'))
# volas2 = PhotoImage(file=get_resource_path(r'image\music\base\volume2a.png'))
# vol3 = PhotoImage(file=get_resource_path(r'image\music\base\volume3.png'))
# volas3 = PhotoImage(file=get_resource_path(r'image\music\base\volume3a.png'))
# vol4 = PhotoImage(file=get_resource_path(r'image\music\base\volume4.png'))
# volas4 = PhotoImage(file=get_resource_path(r'image\music\base\volume4a.png'))

controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0, pady=20)
volume_meter = Label(master_frame, image=vol0)
volume_meter.grid(row=2, column=1, padx=40)
volume_frame = LabelFrame(master_frame,  text="Volume")
volume_frame.grid(row=0,  column=1, padx=30)
# back_button = Button(controls_frame, image=back_btn_img, borderwidth=0, command=previous_song)
# forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song)
# play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
# pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
# stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

# ボタン作成
back_button = Button(controls_frame, image=back_btn_img, borderwidth=0, command=previous_song, relief="flat")
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song, relief="flat")
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play, relief="flat")
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(None), relief="flat")
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop, relief="flat")



# back_button.grid(row=0, column=0, padx=10)
# forward_button.grid(row=0, column=1, padx=0)
# play_button.grid(row=0, column=2, padx=10)
# pause_button.grid(row=0, column=3, padx=10)
# stop_button.grid(row=0, column=4, padx=10)

# ボタン配置
back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
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

# 音量スライダー設定
# volume_slider = Scale(master_frame, from_=1, to=0, orient=VERTICAL, command=on_slider_motion, length=165)
# volume_slider.set(0.5)  # 初期音量を50%に設定
# volume_slider.grid(row=0, column=0, pady=10)

# スライダー用のttk.Scaleウィジェット
style = ttk.Style()
style.configure("Custom.Horizontal.TScale",
                background="gray",  # 背景色（スライダーのトラック部分）
                troughcolor="lightgray",  # スライダーの進行バー部分
                sliderlength=30,  # つまみ部分の長さ
                foreground="blue")  # 初期つまみ部分の色

volume_slider = ttk.Scale(volume_frame, from_=1, to=0, orient=HORIZONTAL, style="Custom.Horizontal.TScale", command=on_slider_motion)
volume_slider.set(0.5)  # 初期音量設定
volume_slider.grid(row=0, column=0, pady=10)

# スライダーの動きを追跡するためにマウスドラッグイベントをバインド
volume_slider.bind("<Motion>", on_slider_motion)



# # スライダーの設定
# volume_slider = ttk.Scale(volume_frame, from_=1, to=0, orient=VERTICAL, command=on_slider_motion, length=165, style="TScale")#command=volume, length=165)
# volume_slider.set(0.5)  # 初期音量50%
# volume_slider.pack(pady=10)


# 初期化の最後にショートカット設定を呼び出す
setup_keyboard_shortcuts()
root.mainloop()


# def volume(x):#current_volume = pygame.mixer.music.get_volume()):
#     pygame.mixer.music.set_volume(volume_slider.get())

#     current_volume = pygame.mixer.music.get_volume()
#     current_volume = current_volume * 100
   
#     if int(current_volume) < 1:
#         volume_meter.config(image=vol0)

#     elif int(current_volume) > 0 and int(current_volume) <= 12.5:
#         volume_meter.config(image=vol1)
  
#     elif int(current_volume) > 12.5 and int(current_volume) <= 25:
#         volume_meter.config(image=volas1)
    
#     elif int(current_volume) >= 25 and int(current_volume) <= 37.5:
#             volume_meter.config(image=vol2)
      
#     elif int(current_volume) >= 37.5 and int(current_volume) <= 50:
#             volume_meter.config(image=volas2)
    
#     elif int(current_volume) >= 50 and int(current_volume) <= 62.5:
#             volume_meter.config(image=vol3)
       
#     elif int(current_volume) >= 62.5 and int(current_volume) <= 75:
#             volume_meter.config(image=volas3)
    
#     elif int(current_volume) >= 75 and int(current_volume) <= 87.5:
#             volume_meter.config(image=vol4)
   
#     elif int(current_volume) >= 87.5 and int(current_volume) <= 100:
#             volume_meter.config(image=volas4)

