# # import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

def animate_i2con(root, gif_path, size=(256, 256)):  # サイズを256x256に設定
    # GIFをフレームに分割し、指定サイズにリサイズ
    gif = Image.open(gif_path)
    frames = [ImageTk.PhotoImage(frame.convert("RGBA").resize(size, Image.LANCZOS)) for frame in ImageSequence.Iterator(gif)]

    # アニメーションの更新間隔（ミリ秒）
    animation_speed = 100  # 例えば100msごとに更新

    def update_icon(ind=0):
        # ウィンドウのアイコンを設定
        root.tk.call('wm', 'iconphoto', root._w, frames[ind])
        ind = (ind + 1) % len(frames)  # 次のフレームに移動
        root.after(animation_speed, update_icon, ind)  # 定義した速度でアイコンを更新

    # アニメーションを開始
    update_icon()

# import sys
# from PIL import Image, ImageTk

# def animate_i2con(root, gif_path, size=(256, 256)):  # サイズを256x256に設定
#     # EXE化後にリソース（ico.gif）を参照する方法
#     if getattr(sys, 'frozen', False):
#         # PyInstallerで実行されている場合
#         base_path = sys._MEIPASS
#     else:
#         # 開発環境で実行されている場合
#         base_path = sys.argv[0]  # これにより現在のスクリプトパスを取得

#     # GIFファイルのパスを組み立てる
#     gif_path = base_path + '\\' + gif_path  # 相対パスをフルパスに組み立て

#     # GIFをフレームに分割し、指定サイズにリサイズ
#     gif = Image.open(gif_path)
#     frames = [ImageTk.PhotoImage(frame.convert("RGBA").resize(size, Image.LANCZOS)) for frame in ImageSequence.Iterator(gif)]

#     # アニメーションの更新間隔（ミリ秒）
#     animation_speed = 100  # 例えば100msごとに更新

#     def update_icon(ind=0):
#         # ウィンドウのアイコンを設定
#         root.tk.call('wm', 'iconphoto', root._w, frames[ind])
#         ind = (ind + 1) % len(frames)  # 次のフレームに移動
#         root.after(animation_speed, update_icon, ind)  # 定義した速度でアイコンを更新

#     # アニメーションを開始
#     update_icon()


# import sys
# from PIL import Image, ImageTk, ImageSequence

# def animate_i2con(root, gif_path, size=(256, 256)):  # サイズを256x256に設定
#     # EXE化後にリソース（ico.gif）を参照する方法
#     if getattr(sys, 'frozen', False):  # PyInstallerで実行されている場合
#         base_path = sys._MEIPASS  # バンドルされたリソースのパス
#     else:
#         base_path = ''  # 開発環境では不要

#     # GIFファイルのパスを組み立てる
#     gif_path = base_path + '\\' + gif_path  # バンドルされたパスを指定

#     # GIFをフレームに分割し、指定サイズにリサイズ
#     gif = Image.open(gif_path)
#     frames = [ImageTk.PhotoImage(frame.convert("RGBA").resize(size, Image.LANCZOS)) for frame in ImageSequence.Iterator(gif)]

#     # アニメーションの更新間隔（ミリ秒）
#     animation_speed = 100  # 例えば100msごとに更新

#     def update_icon(ind=0):
#         # ウィンドウのアイコンを設定
#         root.tk.call('wm', 'iconphoto', root._w, frames[ind])
#         ind = (ind + 1) % len(frames)  # 次のフレームに移動
#         root.after(animation_speed, update_icon, ind)  # 定義した速度でアイコンを更新

#     # アニメーションを開始
#     update_icon()



# import sys
# from PIL import Image, ImageTk, ImageSequence

# def animate_i2con(root, gif_path, size=(256, 256)):  # サイズを256x256に設定
#     # EXE化後にリソース（ico.gif）を参照する方法
#     if getattr(sys, 'frozen', False):
#         # PyInstallerで実行されている場合、sys._MEIPASSを使用
#         base_path = sys._MEIPASS
#     else:
#         # 開発環境で実行されている場合、スクリプトが置かれているディレクトリを参照
#         base_path = sys.argv[0]  # これにより現在のスクリプトパスを取得

#     # GIFファイルのパスを組み立てる
#     gif_path = base_path + '\\' + gif_path  # 相対パスをフルパスに組み立て

#     # GIFをフレームに分割し、指定サイズにリサイズ
#     gif = Image.open(gif_path)
#     frames = [ImageTk.PhotoImage(frame.convert("RGBA").resize(size, Image.LANCZOS)) for frame in ImageSequence.Iterator(gif)]

#     # アニメーションの更新間隔（ミリ秒）
#     animation_speed = 100  # 例えば100msごとに更新

#     def update_icon(ind=0):
#         # ウィンドウのアイコンを設定
#         root.tk.call('wm', 'iconphoto', root._w, frames[ind])
#         ind = (ind + 1) % len(frames)  # 次のフレームに移動
#         root.after(animation_speed, update_icon, ind)  # 定義した速度でアイコンを更新

#     # アニメーションを開始
#     update_icon()
