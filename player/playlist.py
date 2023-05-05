# ライブラリの読み込み
import sys
import player.mid
import player.pyg
import player.loader

# ライブラリの設定
mid = player.mid
pyg = player.pyg
loader = player.loader

def load(playlistfilepath):
    with open(playlistfilepath, 'r') as file:
        playlist = file.read().splitlines()
        print(f"{playlistfilepath}を読み込みました。")
        return playlist

def play(playlist):
    filepath = playlist.pop(0)
    filepath = loader.clean(filepath)
    ext = loader.check_ext(filepath)
    if ext == "mid":
        print(f"{filepath}を再生します。")
        mid.play(filepath)
    if ext == "pyg":
        print(f"{filepath}を再生します。")
        pyg.play(filepath)
    if playlist:
        play(playlist)
    else:
        sys.exit()