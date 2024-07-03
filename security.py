import keyboard

typed_buffer = ""
# Флаг для отслеживания состояния блокировки Enter
enter_blocked = False  
# Список служебных клавиш
non_printable_keys = ['ctrl', 'alt', 'shift', 'enter', 'backspace', 'tab', 'caps lock', 
                      'esc', 'home', 'end', 'insert', 'delete', 'page up', 'page down', 
                      'left arrow', 'right arrow', 'up arrow', 'down arrow', 'left windows', 
                      'alt gr', 'right ctrl', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 
                      'f9', 'f10', 'f11', 'f12', 'print screen']

def on_key(event):
    global typed_buffer, enter_blocked
    if event.event_type == "down" and event.name not in non_printable_keys:
        typed_buffer += event.name
        print("Напечатано:", typed_buffer)
    elif event.event_type == "down" and event.name == 'backspace':
        typed_buffer = typed_buffer[:-1]
        print("Напечатано:", typed_buffer)
    
    # Блокируем Enter
    if typed_buffer == "осел":
        if not enter_blocked:
            keyboard.block_key('enter')
            enter_blocked = True
            print("Enter заблокирован")
    
    # Разблокируем Enter
    elif enter_blocked:
        keyboard.unblock_key('enter')
        enter_blocked = False
        print("Enter разблокирован")

keyboard.hook(on_key)
print("Отправка слов 18+ будет заблокирована...")
keyboard.wait('esc')

# -----------------------------------------------------------------------------------------внизу верно----------------------

# import keyboard

# typed_buffer = ""

# def on_key(event):
#     global typed_buffer
#     if event.event_type == "down" and event.name != 'backspace':
#         typed_buffer += event.name
#         print("Напечатано:", typed_buffer)
#     elif event.event_type == "down" and event.name == 'backspace':
#         typed_buffer = typed_buffer[:-1]
#         print("Напечатано:", typed_buffer)
#     if typed_buffer == "осел":
#         keyboard.block_key('\n')
#         print("Enter заблокирован")
#     elif '\n' in keyboard._hooks:
#         keyboard.unblock_key('\n')
#         print("Enter разблокирован")
# --------------------
# def on_key(event):
#     global typed_buffer
#     if event.name == 'enter':
#         on_enter(event)
#         return
#     elif event.event_type == 'down' and len(event.name) == 1:  # для символов
#         typed_buffer += event.name
#     elif event.name == 'backspace' and event.event_type == 'down':
#         typed_buffer = typed_buffer[:-1]
#     print("Текущий текст:", typed_buffer)
# ------------------------
# keyboard.hook(on_key)
# print("Нажмите любые клавиши (нажмите esc для выхода)")
# keyboard.wait('esc')

# ------------------------------------------------------------------------------------------------------------------

# import keyboard


# import ctypes

# Параметры Message box
# MB_OK = 0
# MB_ICONWARNING = 0x30

# def show_alert_message(message):
#     ctypes.windll.user32.MessageBoxW(0, message, "Alert", MB_OK | MB_ICONWARNING)

# // -----------------------------

# typed_buffer = ""

# def on_enter(event):
#     global typed_buffer
#     if typed_buffer == "осел":
#         keyboard.block_key('\n')
#         typed_buffer = ""
#     else:
#         print(f"Enter pressed with text: {typed_buffer}")

# def on_key(event):
#     global typed_buffer
#     if event.name == 'enter':
#         on_enter(event)
#         return
#     elif event.event_type == 'down' and len(event.name) == 1:  # для символов
#         typed_buffer += event.name
#     elif event.name == 'backspace' and event.event_type == 'down':
#         typed_buffer = typed_buffer[:-1]
#     print("Текущий текст:", typed_buffer)

# keyboard.hook(on_key)
# print("Нажмите любые клавиши (нажмите esc для выхода)")
# keyboard.wait('esc')

# -------------------------------

# def is_forbidden_word_typed(event):
#     global typed_buffer
#     if event.event_type == keyboard.KEY_DOWN:
#         typed_buffer += event.name

#         if "space" in typed_buffer or "\n" in typed_buffer:
#             typed_buffer = ""

#         if forbidden_word in typed_buffer:
#             for ch in forbidden_word:
#                 keyboard.block_key(ch)
#                 keyboard.block_key('space')
#                 keyboard.block_key('\n')
#                 typed_buffer = ""

# keyboard.hook(is_forbidden_word_typed)