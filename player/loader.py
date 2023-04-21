# 調整の関数
def clean(user_input):
    if user_input.endswith("\"") and user_input.startswith("\""):
        user_input = user_input.strip('"')
        return user_input
    else:
        return user_input


# 読み込みの関数
def check_ext(user_input):
    if user_input.endswith(".mid"):
        ext = "mid"
        return ext
    if user_input.endswith(".midi"):
        ext = "mid"
        return ext
    if user_input.endswith(".mp3"):
        ext = "pyg"
        return ext
    if user_input.endswith(".wav"):
        ext = "pyg"
        return ext
    if user_input.endswith(".ogg"):
        ext = "pyg"
        return ext
