# Psyplic
A Simple Music Player

# 引数について
 - Psyplicでは、引数によりファイルを開くことができます。<br>
例)`psyplic.exe C:\Music\example.mp3`<br>
例)`python psyplic.py C:\Music\example.mp3`<br>
 - また、Version 0.2以降では、plsという拡張子のファイルを読み込ませることで、プレイリストを再生できます。
 - plsファイルは、一般的なテキストファイルと同じように記述され、1行につき1ファイルのパスが記述されます。
 - plsファイルの例は、リリースのzipファイルまたはコードの`example_playlist.pls`を参照してください。
 - plsファイルを開くには、引数に指定してください。<br>
例)`psyplic.exe C:\Music\example.pls`<br>
例)`python psyplic.py C:\Music\example.pls`
