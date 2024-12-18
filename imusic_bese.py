
import pygame
import time 
import tkinter.ttk as ttk 
from tkinter import *
from tkinter import filedialog 
from animate_i2con import animate_i2con  
from mutagen.wave import WAVE 

root = Tk()
root.title('iSongs Music Media Player')
gif_path = r'image\music\base\bese_icon\ico.gif'
animate_i2con(root, gif_path)
root.geometry("860x650") # root.geometry("860x350") ,  root.geometry("860x400")
pygame.mixer.init()
# Crab Song Legth Time Info
def play_time():
    # Check for double timing.
    if stopped:
        return

    current_time = pygame.mixer.music.get_pos() /1000
    # slider_label.config(text=f'Sider:{int(my_slider.get())} and Song Pos: {int(current_time)}')
    status_bar.config(text=current_time)
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))
    song_culrrent = song_box.get(ACTIVE) 
    songlcurrnt = fr'C:/Users/PC/Desktop/ミュージックプレーヤー/音楽プレーヤ2/audio/song_imusic_song/music_song/{song_culrrent}.wav'  #songlcurrnt = fr'C:/Users/user/wav/{song_culrrent}.wav' 
    song_mut = WAVE(songlcurrnt)
    global song_length
    song_length = song_mut.info.length


    converted_current_length = time.strftime('%M:%S', time.gmtime(song_length)) 

    current_time += 1


    if int(my_slider.get()) ==   int(song_length):
        status_bar.config(text=f'Time Elapsed:  {converted_current_length} ')
        # pass

    elif paused:
        pass
    elif int(my_slider.get()) == int(current_time ):
        # slider basn't been moved
        slider_position = int(song_length)
        # current_time += 1
        my_slider.config(to=slider_position,  value=int(current_time))

    # if int(my_slider.get()) == int(current_time ):
    #     # slider basn't been moved
    #     slider_position = int(song_length)
    #     # current_time += 1
    #     my_slider.config(to=slider_position,  value=int(current_time))

    else:
        #slider HAS been moved!
        slider_position = int(song_length)
        # current_time += 1
        my_slider.config(to=slider_position,  value=int(my_slider.get()))

        converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get()))) 

        status_bar.config(text=f'Time Elapsed:  {converted_current_time}  of  {converted_current_length} ')

        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)
 


    # status_bar.config(text=f'Time Elapsed:  {converted_current_time}  of  {converted_current_length} ')
 
    # my_slider.config(value=int(current_time))

    # slider_position = int(song_length)
    # # current_time += 1
    # my_slider.config(to=slider_position,  value=int(current_time))
    # my_slider.config(to=slider_position,  value=0)
    # fake_label = Label(root, text=int(current_time))
    # fake_label.pack(pady=10)
    status_bar.after(1000, play_time)


def add_song():
    song = filedialog.askopenfilenames(initialdir=r'audio\song_imusic_song\music_song', title= "All_Add Many Songs To Playlist(沢山及び数多く複数の曲をプレイリストから追加できることをする)", filetypes=(("wav Files", "*.wav"),  ))#"choose A song(曲選択パターン　A　１曲単体ずつ選ぶこと)", filetypes=(("wav Files", "*.wav"),  )) #song = filedialog.askopenfilename(initialdir=r'audio\song_music_song\music_song', title= "choose A song(曲選択パターン　A　１曲単体ずつ選ぶこと)", filetypes=(("wav Files", "*.wav"),  ))
    print(song) 
    song = song.replace("C:/Users/PC/Desktop/ミュージックプレーヤー/音楽プレーヤ2/audio/song_imusic_song/music_song/", "") #song = song.replace("C:/Users/user/wav/", "")
    song = song.replace(".wav", "")
    song_box.insert(END, song)
def  add_many_songs():
    songs = filedialog.askopenfilenames(initialdir=r'audio\song_imusic_song\music_song', title= "choose A song(曲選択パターン　A　１曲単体ずつ選ぶこと)", filetypes=(("wav Files", "*.wav"),  )) # songs = filedialog.askopenfilenames(initialdir=r'audio\song_music_song\music_song', title= "choose A song(曲選択パターン　A　１曲単体ずつ選ぶこと)", filetypes=(("wav Files", "*.wav"),  ))
    for song in songs:
        song = song.replace("C:/Users/PC/Desktop/ミュージックプレーヤー/音楽プレーヤ2/audio/song_imusic_song/music_song/", "")  # song = song.replace("C:/Users/user/wav/", "")
        song = song.replace(".wav", "")
        song_box.insert(END, song)
def play():
    #  Set Stopped Variable To False So Song Can Play.
    #  Set Stopped Variable To False So Song Can Play.
      #  Set Stopped Variable To False So Song Can Play.
      #
    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume)
    #  Set Stopped Variable To False So Song Can Play.
    global stopped
    stopped = False
    song = song_box.get(ACTIVE)
    song = fr'C:/Users/PC/Desktop/ミュージックプレーヤー/音楽プレーヤ2/audio/song_imusic_song/music_song/{song}.wav'  # song = fr'C:/Users/user/wav/{song}.wav'   
    pygame.mixer.music.load(song) 
    pygame.mixer.music.play(loops=-1)
    play_time()
    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume)

    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume)
    
    # Get current volume
    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume * 100)


    # Get current volume
    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume * 100)

    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume)
    # slider_position = int(song_length)
    # my_slider.config(to=slider_position, value=0)

    # Get current Volume
    current_volume = pygame.mixer.music.get_volume()
    # Times by 100 to make it ease
    # Times by 100 to make it easier to work with. 
    current_volume = current_volume * 100
    # slider_label.config(text=current_volume * 100)

    # Get current Volume
    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume * 100)

    # Change Volume Meter Picture
    if int(current_volume) < 1:
        volume_meter.config(image=vol0)
    # elif int(current_volume) >0
    # elif int(current_volume) > an
    # elif int(current_volume) > and
    # elif int(current_volume) > and int(current_volume)
    elif int(current_volume) > 0 and int(current_volume) <= 12.5:
        volume_meter.config(image=vol1)
    # elif:
    elif int(current_volume) > 12.5 and int(current_volume) <= 25:
        volume_meter.config(image=volas1)
    # elif:
    elif int(current_volume) >= 25 and int(current_volume) <= 37.5:
            volume_meter.config(image=vol2)
        # elif:
    elif int(current_volume) >= 37.5 and int(current_volume) <= 50:
            volume_meter.config(image=volas2)
        # elif:
    elif int(current_volume) >= 50 and int(current_volume) <= 62.5:
            volume_meter.config(image=vol3)
        # elif:
    elif int(current_volume) >= 62.5 and int(current_volume) <= 75:
            volume_meter.config(image=volas3)
        # elif:
    elif int(current_volume) >= 75 and int(current_volume) <= 87.5:
            volume_meter.config(image=vol4)
        # elif:
    elif int(current_volume) >= 87.5 and int(current_volume) <= 100:
            volume_meter.config(image=volas4)
        # elif:


    




    
# Stop playing current song
global stopped
stopped = False    
def stop():
    # Reset Slider and Status Bar
    status_bar.config(text='')
    # StopSong From Playing
    my_slider.config(value=0)
    pygame.mixer.music.stop() 
    song_box.select_clear(ACTIVE) 
    status_bar.config(text='停止中: 曲を停止させました')
    # Clear The Status Bar
    status_bar.after(2000, lambda: status_bar.config(text=''))

    # Set StopVariable To True
    global stopped
    stopped = True
    
    # これにて音楽プレーヤー全コード完了とする

# Play The Next Song in the pliaylist 
def next_song():
    # Reset Slider and Status Bar
    status_bar.config(text='')
    # StopSong From Playing
    my_slider.config(value=0)
    
    next_one = song_box.curselection()
    print(next_one) 
    print(next_one[0])
    next_one = next_one[0]+1
    songl = song_box.get(next_one)
    print(songl)
    songll = fr'C:/Users/PC/Desktop/ミュージックプレーヤー/音楽プレーヤ2/audio/song_imusic_song/music_song/{songl}.wav'  # songll = fr'C:/Users/user/wav/{songl}.wav'   
    pygame.mixer.music.load(songll) 
    pygame.mixer.music.play(loops=-1)
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one,  last=None)
def previous_song():
    # Reset Slider and Status Bar
    status_bar.config(text='')
    # StopSong From Playing
    my_slider.config(value=0)
    
    next_one = song_box.curselection()
    print(next_one) 
    print(next_one[0]) 
    next_one = next_one[0]-1 
    songl = song_box.get(next_one)
    print(songl)
    songll = fr'C:/Users/PC/Desktop/ミュージックプレーヤー/音楽プレーヤ2/audio/song_imusic_song/music_song/{songl}.wav'  # songll = fr'C:/Users/user/wav/{songl}.wav' 
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
    # song_length
    # slider_label.config(text=f'{int(my_slider.get())}  of {int(song_length)}') # slider_label.config(text=f'{int(my_slider.get())}  of {song_length}')
    song = song_box.get(ACTIVE)
    song = f'C:/Users/PC/Desktop/ミュージックプレーヤー/音楽プレーヤ2/audio/song_imusic_song/music_song/{song}.wav'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=-1, start=int(my_slider.get()))
    
    # pygame.mixer.music.load(song)
    # pygame.mixer.music.play(loops=0, start=int(my_slider.get()))



#  Create  Volume Functions
def volume(x):#current_volume = pygame.mixer.music.get_volume()):
    pygame.mixer.music.set_volume(volume_slider.get())
     

    # Get current Volume
    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume * 100)

    # Get current Volume
    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume * 100)

    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume* )

    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume)

    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume)


    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume)
    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume)
    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume)
    # slider_label.config(text=current_volume)
    # # slider_label.config(text=current_volume)
    # slider_label.config(textcurrent_volume)
    # slider_label.config(texcurrent_volume)
    # slider_label.config(tecurrent_volume)
    # slider_label.config(tescurrent_volume)
    # slider_label.config(tesxcurrent_volume)
    # slider_label.config(tesxscurrent_volume)
    # slider_label.config(tesxcurrent_volume)
    # slider_label.config(tcurrent_volume)
    # slider_label.config(tcurrent_volume)
    # slider_label.config(current_volume)
    # slider_label.config(current_volume)
    # slider_label.config()
    # slider_label.config
    # slider_label.confi
    # slider_label.conf
    # slider_label.confg
    # slider_label.confgi()
    # slider_label.confgi
    # slider_label
    # current_volume = pygame.mixer.music.get_volume()
    # current_volume = pygame.mixer.music.get_
    # current_volume = pygame.mixer.music
    # current_volume = pygame.mixer.music,
    # current_volume = pygame.mixer.music.
    # current_volume = pygame.mixer.m
    # current_volume =
    # current_volume =- 
    # pygame.mixer.music.set_volume(volume_slider.get())
    # pygame.mixer.music.set_volume()
    # pygame.mixer.music.set_vol
    # pygame.mixer.music.set_vlum
    # pygame.micer.music.set_vlum
    # pygame.micer.music.set
    # pygame.mixer.music.set_vlum
    # # pass

    # #  Create  Volume Functions
    # def volume():
    #     pass


    # Get current Volume
    current_volume = pygame.mixer.music.get_volume()
    # Times by 100 to make it ease
    # Times by 100 to make it easier to work with. 
    current_volume = current_volume * 100
    # slider_label.config(text=current_volume * 100)

    # Get current Volume
    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume * 100)

    # Change Volume Meter Picture
    if int(current_volume) < 1:
        volume_meter.config(image=vol0)
    # elif int(current_volume) >0
    # elif int(current_volume) > an
    # elif int(current_volume) > and
    # elif int(current_volume) > and int(current_volume)
    elif int(current_volume) > 0 and int(current_volume) <= 12.5:
        volume_meter.config(image=vol1)
    # elif:
    elif int(current_volume) > 12.5 and int(current_volume) <= 25:
        volume_meter.config(image=volas1)
    # elif:
    elif int(current_volume) >= 25 and int(current_volume) <= 37.5:
            volume_meter.config(image=vol2)
        # elif:
    elif int(current_volume) >= 37.5 and int(current_volume) <= 50:
            volume_meter.config(image=volas2)
        # elif:
    elif int(current_volume) >= 50 and int(current_volume) <= 62.5:
            volume_meter.config(image=vol3)
        # elif:
    elif int(current_volume) >= 62.5 and int(current_volume) <= 75:
            volume_meter.config(image=volas3)
        # elif:
    elif int(current_volume) >= 75 and int(current_volume) <= 87.5:
            volume_meter.config(image=vol4)
        # elif:
    elif int(current_volume) >= 87.5 and int(current_volume) <= 100:
            volume_meter.config(image=volas4)
        # elif:


    # # elif:
    # elif int(current_volume) > 0 and int(current_volume) <= 25:
    #         volume_meter.config(image=vol2)
    #     # elif:
    # elif int(current_volume) > 0 and int(current_volume) <= 25:
    #         volume_meter.config(image=vol3)
    #     # elif:
    # elif int(current_volume) > 0 and int(current_volume) <= 25:
    #         volume_meter.config(image=vol4)
    #     # elif:

# Create Play list( Mast:Master Frame ):
master_frame = Frame(root)
master_frame.pack(pady=20)#*

# Create Playlist Box
song_box = Listbox(master_frame, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
# song_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
song_box.grid(row=0, column=0) #pady=20)
# song_box.pack() #pady=20)

# song_box = Listbox(master_frame, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
# # song_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
# song_box.pack() #pady=20)
# song_box.pack() #pady=20)

back_btn_img = PhotoImage(file=r'image\music\base\back50.png')
forward_btn_img = PhotoImage(file=r'image\music\base\forward50.png')
play_btn_img = PhotoImage(file=r'image\music\base\play50.png')
pause_btn_img = PhotoImage(file=r'image\music\base\pause50.png')
stop_btn_img = PhotoImage(file=r'image\music\base\stop50.png')

# Define Volume Control Images
# global volume
# volume
global vol0
global vol1
global volas1
global vol2
global volas2
# global vol32
# global vol3
# global vol
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

# vol3 

# Define Volume Control Images
# vol2 -


# Define Volume Control Images


# Define Volume Control Images


# Define Volume Control Images

# Define Volume C


# Create Player Control Frame

controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0, pady=20)







# Create Volume Metetre as Create Volume Meter Fra as Create Volume Meter Frame as Create Volume Meter Fram as Create Volume Meter 
# Create Volume Meter Fram
# Create Volume Meter 
# volume_meter = Label(mester_frame, image=vol4)
# volume_meter = Label(msster_frame, image=vol4)
# volume_meter = Label(master_frame, image=vol4)
volume_meter = Label(master_frame, image=vol0)
volume_meter.grid(row=1, column=1, padx=10)
# volume_ 
# volume_frame as volume_meter as volume_meter.grid() as volume_ as volume_meter.grid(row=1, )
# volume_meter.grid(row=1, )
# volume_meter.grid(row=1, column)
# volume_meter.grid(row=1, column=)
# volume_meter.grid(row=1, column=1)
# volume_meter.grid(row=1, column=1)
# volume_meter.grid(row=1, column=1, padx=)
# volume_meter.grid(row=1, column=1, padx=10)
# volume_meter.grid(row=1, column=1, padx=10)
# Create Volume Metetre as Create Volume Meter Fra as Create Volume Meter Frame as Create Volume Meter Fram as Create Volume Meter 
# Create Volume Meter Fram
# Create Volume Meter 
# volume_meter = Label(mast)


# Create Volume Metetre as Create Volume Meter Fra as Create Volume Meter Frame as Create Volume Meter Fram as Create Volume Meter 
# Create Volume Meter Fram
# Create Volume Meter 
# volume_meter = Label()


# Create Volume Metetre as Create Volume Meter Fra as Create Volume Meter Frame as Create Volume Meter Fram as Create Volume Meter 
# Create Volume Meter Fram
# Create Volume Meter 
# volume_meter = Label()

# Create Volume Metetre as Create Volume Meter Fra as Create Volume Meter Frame as Create Volume Meter Fram as Create Volume Meter 
# Create Volume Meter Fram
# Create Volume Meter 
# volume_meter = Label()

# Create Volume Metetre as Create Volume Meter Fra as Create Volume Meter Frame as Create Volume Meter Fram as Create Volume Meter 
# Create Volume Meter Fram
# Create Volume Meter 
# volume_meter = Laeb



# Create Volume Metetre as Create Volume Meter Fra as Create Volume Meter Frame as Create Volume Meter Fram as Create Volume Meter 
# Create Volume Meter Fram
# Create Volume Meter 
# volume_meter = Laeb

# #  Create Volume Label Frame
volume_frame = LabelFrame(master_frame,  text="Volume")
volume_frame.grid(row=0,  column=1, padx=30)


# #  Create Volume Label Frame
# volume_frame = LabelFrame(master_frame,  text="Volume")
# volume_frame.grid(row=0,  column=1, padx=20)

# #  Create Volume Label Frame
# volume_frame = LabelFrame(master_frame,  text="Volume")
# volume_frame.grid(row=0,  column=1, padx-)


# #  Create Volume Label Frame
# volume_frame = LabelFrame(master_frame,  text="Volume")
# volume_frame.grid(row=0,  column=1)



#  Create Volume Lan as Lagh
#  Create Volume Lan as Lagh as Lagb
#  Create Volume Lagb as Lab
# #  Create Volume Label Frame
# volume_frame = LabelFrame()


# # Create Player Control Frame

# controls_frame = Frame(master_frame)
# controls_frame.grid(row=1, column=0)

# # Create Player Control Frame

# controls_frame = Frame(master_frame)
# controls_frame.pack()

# Create Player Control Frame

# controls_frame = Frame(root)
# controls_frame.pack()


# Create player Control Frame = 
# Create player Control Buttons
# Create player Control Buttons
# Create player Control Buttons
# Create player Control Buttons
# Create player Control Buttons
# Create player Control Buttons
# Create player Control Buttons
# Create player Control Buttons
# Create player Control Buttons
# Create player Control Buttons
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

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs  (曲のリストを追加する) ", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist(一つずつ曲をプレイリストから追加する)", command=add_song)

add_song_menu.add_command(label="All_Add Many Songs To Playlist(沢山及び数多く複数の曲をプレイリストから追加できることをする)", command=add_many_songs)

remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs(プレイリストをボックスから消去する)",menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song From Playlist(追加したプレイリストから一つずつボックスから消去する)", command=delete_song)
remove_song_menu.add_command(label="Delete A Song From Playlist(追加したプレイリストをすべてボックスから消去する)", command=delete_all_songs)


# Create Status Bar.
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E )
status_bar.pack(fill=X, side=BOTTOM, ipady=2)



# Create Music Position Slider.
my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)

my_slider.grid(row=2,  column=0,  pady=10)



# Create Music Position Slider .


#  Create Volume  Slider ..

# volume_slider  =




#  Create Volume  Slider ..


volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=325)

volume_slider.pack(pady=10)

#  Create Volume  Slider ..


# #  Create Volume  Slider ..


# volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=325)

# volume_slider.pack()

# #  Create Volume  Slider ..



# #  Create Volume  Slider ..


# volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=325)

# volume_slider.grid()

# #  Create Volume  Slider ..




#  Create Volume  Slider ..


# volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=325)

# volume_slider.pack(row=0,  column=1)

#  Create Volume  Slider ..



#  Create Volume  Slider ..


# volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=325)

# volume_slider.grid(row=0,  column=1)

#  Create Volume  Slider ..




# #  Create Volume  Slider ..


# volume_slider = ttk.Scale(master_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=325)

# volume_slider.grid(row=0,  column=1)

# #  Create Volume  Slider ..


# #  Create Volume  Slider ..


# volume_slider = ttk.Scale(master_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=360)

# volume_slider.grid(row=0,  column=1)

# #  Create Volume  Slider ..



# #  Create Volume  Slider ..


# volume_slider = ttk.Scale(master_frame, from_=0, to=1, orient=VERTICAL, value=1, command=slide, length=360)

# volume_slider.grid(row=0,  column=1)

# #  Create Volume  Slider ..


# #  Create Volume  Slider ..


# volume_slider = ttk.Scale(master_frame, from_=0, to=1, orient=VERTICAL, value=0, command=slide, length=360)

# volume_slider.grid(row=0,  column=1)

# #  Create Volume  Slider ..


# #  Create Volume  Slider ..


# volume_slider = ttk.Scale(master_frame, from_=0, to=1, orient=HORIZONTAL, value=0, command=slide, length=360)

# volume_slider.grid(row=0,  column=1)

# #  Create Volume  Slider ..

# #  Create Volume  Slider ..


# volume_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)

# volume_slider.grid(row=0,  column=1)

# #  Create Volume  Slider ..


# #  Create Volume  Slider ..


# volume_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)

# volume_slider.grid(row=0,  column=1,  pady=10)

# #  Create Volume  Slider ..

# # #  Create Volume  Slider ..


# volume_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)

# volume_slider.grid(row=2,  column=0,  pady=10)

# #  Create Volume  Slider ..


# my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)

# my_slider.grid(row=2,  column=0,  pady=10)

#  Create Temporary Slider Label .





# # Create Music Position Slider.
# my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)

# my_slider.grid(row=2,  column=0,  pady=30)



# # Create Music Position Slider.
# my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)

# my_slider.pack(row=2,  column=0,  pady=30)



# # Create Music Position Slider.
# my_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)

# my_slider.pack(pady=30)

# Create Temporary Slider Label
# slider_label = Label(root,  text="0")
# slider_label.pack(pady=10)


# Create Temporary Slider Label
# slider_label = Label(root,  text="0")
# slider_label.pack(pady=10)


# Create Temporary Slider Label
# slider_label = Label(root,  text="0")
# slider_label.pack(pady=10)




root.mainloop()


#参照項目一覧

#$1 未完了のインストールである場合には次の入力手続きをコマンドプロンとで済ませる事インストールは次のとおりである
# 「pip install mutagen」と入力して官僚とする完了済みでアールをさせる。