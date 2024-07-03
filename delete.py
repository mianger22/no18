import keyboard
import time
import pyautogui

banned_word = "порн"
typed_chars = []

def on_press(event):
    global typed_chars
    
    # Добавить символ в список
    typed_chars.append(event.name)
    
    # Проверить, завершено ли слово
    if ''.join(typed_chars[-len(banned_word):]) == banned_word:
        for _ in range(len(banned_word)):
            print("Слово введено")
            pyautogui.press('backspace')  # Удалить символы
        del typed_chars[:]  # Очистить список символов
    
    if len(typed_chars) > len(banned_word):
        typed_chars.pop(0)  # Удаляем самый старый символ, чтобы ограничить длину списка

keyboard.on_press(on_press)

print("Мониторинг ввода. Нажмите Ctrl+C для выхода.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Программа завершена.")