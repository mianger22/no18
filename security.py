import keyboard
import ctypes

# Параметры Message box
MB_OK = 0
MB_ICONWARNING = 0x30

def show_alert_message(message):
    ctypes.windll.user32.MessageBoxW(0, message, "Alert", MB_OK | MB_ICONWARNING)

forbidden_word = "порно"
typed_buffer = ""

def is_forbidden_word_typed(event):
    global typed_buffer
    if event.event_type == keyboard.KEY_DOWN:
        typed_buffer += event.name

        if "space" in typed_buffer or "\n" in typed_buffer:
            typed_buffer = ""

        if forbidden_word in typed_buffer:
            for ch in forbidden_word:
                keyboard.block_key(ch)
                keyboard.block_key('space')
                keyboard.block_key('\n')
                typed_buffer = ""

keyboard.hook(is_forbidden_word_typed)

show_alert_message("При вводе слов 18+ клавиатура будет заблокирована. Чтобы возобновить работу, необходимо стереть запрещённое слово и нажать ctrl+c")
keyboard.wait('ctrl+c')