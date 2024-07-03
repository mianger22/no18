import keyboard
import time
import pyautogui

banned_words = ["порн", "эроти", "секс", "мастурб", "дроч", "милф", "инцест", "мачеха", "зрел"]
typed_chars = []

def on_press(event):
    global typed_chars

    # Добавить символ в список
    typed_chars.append(event.name)

    # Проверить, завершено ли запрещенное слово
    for banned_word in banned_words:
        if ''.join(typed_chars[-len(banned_word):]) == banned_word:
            for _ in range(len(banned_word)):
                pyautogui.press('backspace')  # Удалить символы
            del typed_chars[:]  # Очистить список символов
            break

    if len(typed_chars) > max(map(len, banned_words)):
        typed_chars.pop(0)  # Удаляем самый старый символ, чтобы ограничить длину списка

keyboard.on_press(on_press)

print("Мониторинг ввода. Нажмите Ctrl+C для выхода.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Программа завершена.")