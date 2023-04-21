# ライブラリをインポート
import mido

# ライブラリを設定

# 再生の関数
def play(path):
    midi = mido.get_output_names()
    midi_device_list = midi
    port = mido.open_output(midi_device_list[0])
    mid = mido.MidiFile(path)
    for msg in mid.play():
        port.send(msg)