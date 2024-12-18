import subprocess
import glob

def create_exe():
    # 対象のディレクトリ
    music_directory = "C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song"
    
    # globを使って.wavファイルをリスト化
    wav_files = glob.glob(f"{music_directory}/*.wav")
    print("Found WAV files:", wav_files)
    
    # --add-data のオプションを動的に生成
    add_data_options = []
    for wav_file in wav_files:
        # ファイル名を取得
        wav_filename = wav_file.split("\\")[-1]  # Windowsパスの区切りでファイル名を取得
        destination_path = f"audio/song_imusic_song/music_song/{wav_filename}"
        add_data_options.append(f"{wav_file};{destination_path}")  # 修正: 'path1;path2' 形式に

    # PyInstallerのコマンドをリストとして作成
    command = [
        "pyinstaller",
        "--onefile",      # 単一のEXEファイルにまとめる
        "--noconsole",    # コンソールウィンドウを表示しない
        "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\bese_icon\\ico.gif;image/music/base/bese_icon",  # GIFファイルをバンドル
        "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\back50.png;image/music/base",  # back50.pngファイルをバンドル
        "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\forward50.png;image/music/base",  # forward50.pngファイルをバンドル
        "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\play50.png;image/music/base",  # play50.pngファイルをバンドル
        "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\pause50.png;image/music/base",  # pause50.pngファイルをバンドル
        "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\stop50.png;image/music/base",  # stop50.pngファイルをバンドル
        "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume0.png;image/music/base",  # volume0.pngファイルをバンドル
        "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume1.png;image/music/base",  # volume1.pngファイルをバンドル
        "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume1a.png;image/music/base",  # volume1a.pngファイルをバンドル
        "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume2.png;image/music/base",  # volume2.pngファイルをバンドル
        "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume2a.png;image/music/base",  # volume2a.pngファイルをバンドル
        "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume3.png;image/music/base",  # volume3.pngファイルをバンドル
        "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume3a.png;image/music/base",  # volume3a.pngファイルをバンドル
        "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume4.png;image/music/base",  # volume4.pngファイルをバンドル
        "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume4a.png;image/music/base",  # volume4a.pngファイルをバンドル
    ] + [f"--add-data={option}" for option in add_data_options]  # 動的に生成した --add-data を追加
    
    command.append("imusic_beta01.py")  # メインのPythonスクリプト

    try:
        # コマンドを実行
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='cp932',  # Windows用エンコーディング
            shell=True         # コマンドをシェルで実行
        )

        # 実行結果を表示
        if result.returncode == 0:
            print("EXEファイルの作成が成功しました！")
        else:
            print(f"エラーが発生しました:\n{result.stderr}")
            print("標準出力:\n", result.stdout)

    except FileNotFoundError:
        print("エラー: PyInstallerが見つかりませんでした。インストールを確認してください。")
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")

if __name__ == "__main__":
    create_exe()




# import subprocess
# import glob

# def create_exe():
#     # 対象のディレクトリ
#     music_directory = "C:/Users/PC/Desktop/ミュージックプレーヤー(正式版)/audio/song_imusic_song/music_song"
    
#     # globを使って.wavファイルをリスト化
#     wav_files = glob.glob(f"{music_directory}/*.wav")
#     print("Found WAV files:", wav_files)
    
#     # --add-data のオプションを動的に生成
#     add_data_options = []
#     for wav_file in wav_files:
#         # ファイル名を取得
#         wav_filename = wav_file.split("\\")[-1]  # Windowsパスの区切りでファイル名を取得
#         destination_path = f"audio/song_imusic_song/music_song/{wav_filename}"
#         add_data_options.append(f'"{wav_file}";{destination_path}')
   


#     # PyInstallerのコマンドをリストとして作成
#     command = [
#         "pyinstaller",
#         "--onefile",      # 単一のEXEファイルにまとめる
#         "--noconsole",    # コンソールウィンドウを表示しない
#         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\bese_icon\\ico.gif;image/music/base/bese_icon",  # GIFファイルをバンドル
#         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\back50.png;image/music/base",  # back50.pngファイルをバンドル
#         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\forward50.png;image/music/base",  # forward50.pngファイルをバンドル
#         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\play50.png;image/music/base",  # play50.pngファイルをバンドル
#         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\pause50.png;image/music/base",  # pause50.pngファイルをバンドル
#         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\stop50.png;image/music/base",  # stop50.pngファイルをバンドル



#         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume0.png;image/music/base",  # volume0.pngファイルをバンドル
#         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume1.png;image/music/base",  # volume1.pngファイルをバンドル
#         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume1a.png;image/music/base",  # volume1a.pngファイルをバンドル
#         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume2.png;image/music/base",  # volume2.pngファイルをバンドル
#         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume2a.png;image/music/base",  # volume2a.pngファイルをバンドル
#         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume3.png;image/music/base",  # volume3.pngファイルをバンドル
#         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume3a.png;image/music/base",  # volume3a.pngファイルをバンドル
#         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume4.png;image/music/base",  # volume4.pngファイルをバンドル
#         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume4a.png;image/music/base",  # volume4a.pngファイルをバンドル
#         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\audio\\song_imusic_song\\music_song\\*.wav;audio/song_imusic_song/music_song",


#         # "imusic_beta.py"  # メインのPythonスクリプト
#     ] + [f"--add-data={option}" for option in add_data_options]  # 動的に生成した --add-data を追加
    
#     command.append("imusic_beta.py")  # メインのPythonスクリプト

#     try:
#         # コマンドを実行
#         result = subprocess.run(
#             command,
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#             text=True,
#             encoding='cp932',  # Windows用エンコーディング
#             shell=True         # コマンドをシェルで実行
#         )

#         # 実行結果を表示
#         if result.returncode == 0:
#             print("EXEファイルの作成が成功しました！")
#         else:
#             print(f"エラーが発生しました:\n{result.stderr}")
#             print("標準出力:\n", result.stdout)

#     except FileNotFoundError:
#         print("エラー: PyInstallerが見つかりませんでした。インストールを確認してください。")
#     except Exception as e:
#         print(f"予期しないエラーが発生しました: {e}")

# if __name__ == "__main__":
#     create_exe()


    
    
# # def create_exe():
# #     # PyInstallerのコマンドをリストとして作成
# #     command = [
# #         "pyinstaller",
# #         "--onefile",      # 単一のEXEファイルにまとめる
# #         "--noconsole",    # コンソールウィンドウを表示しない
# #         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\bese_icon\\ico.gif;image/music/base/bese_icon",  # GIFファイルをバンドル
# #         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\back50.png;image/music/base",  # back50.pngファイルをバンドル
# #         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\forward50.png;image/music/base",  # forward50.pngファイルをバンドル
# #         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\play50.png;image/music/base",  # play50.pngファイルをバンドル
# #         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\pause50.png;image/music/base",  # pause50.pngファイルをバンドル
# #         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\stop50.png;image/music/base",  # stop50.pngファイルをバンドル



# #         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume0.png;image/music/base",  # volume0.pngファイルをバンドル
# #         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume1.png;image/music/base",  # volume1.pngファイルをバンドル
# #         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume1a.png;image/music/base",  # volume1a.pngファイルをバンドル
# #         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume2.png;image/music/base",  # volume2.pngファイルをバンドル
# #         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume2a.png;image/music/base",  # volume2a.pngファイルをバンドル
# #         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume3.png;image/music/base",  # volume3.pngファイルをバンドル
# #         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume3a.png;image/music/base",  # volume3a.pngファイルをバンドル
# #         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume4.png;image/music/base",  # volume4.pngファイルをバンドル
# #         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\image\\music\\base\\volume4a.png;image/music/base",  # volume4a.pngファイルをバンドル
# #         "--add-data", "C:\\Users\\PC\\Desktop\\ミュージックプレーヤー(正式版)\\audio\\song_imusic_song\\music_song\\*.wav;audio/song_imusic_song/music_song",


# #         "imusic_beta.py"  # メインのPythonスクリプト
# #     ]

# #     try:
# #         # コマンドを実行
# #         result = subprocess.run(
# #             command,
# #             stdout=subprocess.PIPE,
# #             stderr=subprocess.PIPE,
# #             text=True,
# #             encoding='cp932',  # Windows用エンコーディング
# #             shell=True         # コマンドをシェルで実行
# #         )

# #         # 実行結果を表示
# #         if result.returncode == 0:
# #             print("EXEファイルの作成が成功しました！")
# #         else:
# #             print(f"エラーが発生しました:\n{result.stderr}")
# #             print("標準出力:\n", result.stdout)

# #     except FileNotFoundError:
# #         print("エラー: PyInstallerが見つかりませんでした。インストールを確認してください。")
# #     except Exception as e:
# #         print(f"予期しないエラーが発生しました: {e}")

# # if __name__ == "__main__":
# #     create_exe()


