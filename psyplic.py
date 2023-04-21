try:
    # ライブラリをインポート
    import sys
    import player.mid
    import player.pyg
    import player.loader

    # ライブラリの設定
    mid = player.mid
    pyg = player.pyg
    loader = player.loader

    # 引数の確認
    if len(sys.argv) > 1:
        args_status = True
        filepath = sys.argv[1]
    else:
        args_status = False

    # 音楽再生の関数
    def psyplic():
        while True:
            user_input = input("ファイルパスを絶対パスで入力してください。: ")
            if user_input == "":
                continue
            else:
                user_input = loader.clean(user_input)
                ext = loader.check_ext(user_input)
                if ext == "mid":
                    mid.play(user_input)
                    psyplic()
                if ext == "pyg":
                    pyg.play(user_input)
                    psyplic()

    # 引数から再生する関数
    def psyplic_cmd(user_input):
        user_input = loader.clean(user_input)
        ext = loader.check_ext(user_input)
        if ext == "mid":
            print(f"{user_input}を再生します。")
            mid.play(user_input)
            sys.exit()
        if ext == "pyg":
            print(f"{user_input}を再生します。")
            pyg.play(user_input)
            sys.exit()

    # 実行する
    if args_status == True:
        psyplic_cmd(filepath)
    else:
        psyplic()
except KeyboardInterrupt:
    sys.exit()