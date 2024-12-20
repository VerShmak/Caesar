import tkinter as tk
from tkinter import ttk
from collections import Counter

# Шифрование
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def encrypt_text():
    text = text1.get("1.0", tk.END).strip()
    if not text:
        text1.delete("1.0", tk.END)
        text1.insert(tk.END, "Введите текст")
        return
    try:
        shift = int(entry1.get())
    except ValueError:
        ttk.Label(frame1, text = "Неверный шаг").pack(pady=5)
        return
    encrypted_text = caesar_encrypt(text, shift)
    text1.insert(tk.END, f"\n Зашиврованный текст: \n {encrypted_text}")

# Дешифрование
def decrypt_text():
    text = text2.get("1.0", tk.END).strip()
    if not text:
        text2.delete("1.0", tk.END)
        text2.insert(tk.END, "Введите текст")
        return
    try:
        shift = int(entry2.get())
    except ValueError:
        ttk.Label(frame2, text = "Неверный шаг").pack(pady=5)
        return
    decrypted_text = caesar_encrypt(text, -shift)
    text2.insert(tk.END, f"\n Исходный текст: \n {decrypted_text}")

# Взлом кода
def break_caesar_cipher(text):
    #Общепринятые статистические данные частоты встречаемости букв в аглийском языке
    frequencies = {
    'E': 12.7, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97,
    'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25,
    'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36,
    'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29,
    'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10,
    'Z': 0.07
}
    filtered_text = "".join(filter(str.isalpha, text))
    if not filtered_text:
        return "Нет текста", None
    best_shift = 0
    best_score = 0
    best_decryption = ""

    for shift in range(26):
        decrypted_text = caesar_encrypt(filtered_text, -shift)
        letter_counts = Counter(decrypted_text.upper())
        total_letters = sum(letter_counts.values())
        score= sum(
            (count / total_letters) * 100 * frequencies.get(letter, 0)
            for letter, count in letter_counts.items()
        )
        if score > best_score:
            best_score = score
            best_shift = shift
            best_decryption = "".join(caesar_encrypt(text, -shift))

    return best_decryption, best_shift

def break_from_text():
    text = text3.get("1.0", tk.END).strip()
    if not text:
        text3.delete("1.0", tk.END)
        text3.insert(tk.END, "Введите текст для взлома")
        return
    best_decryption, best_shift = break_caesar_cipher(text)
    if best_shift is not None:
        text3.insert(tk.END, f"\n Расшифрованный текст: \n{best_decryption}")
        Shift.config( text = f"{best_shift} шагов потребовалось")
    else:
        Shift.config(text = "Невозможо расшифровать")
    
# РЕАЛИЗАЦИЯ ИНТЕРФЕЙСА
# Создаем окно
window = tk.Tk()
window.title("Шифр Цезаря")
window.geometry("500x500")

# Создадим combobox с вариантами
items = ["Зашифровать", "Расшифровать", "Взломать шифр"]
combobox = ttk.Combobox(window, values = items)
combobox.pack(pady = 10)

# Добавим содержимое для каждой страницы
frame1 = tk.Frame(bg = "lightblue")
frame2 = tk.Frame(bg = "lightgreen")
frame3 = tk.Frame(bg = "lightcoral")

#Страница шифрования
label1 = tk.Label(frame1, text="Зашифровать текст")
label1.pack(pady = 20)
label1_1 = tk.Label(frame1, text="Введите величину шага:")
label1_1.pack(pady = 5)
entry1 = tk.Entry(frame1, width=10)
entry1.pack(pady = 5)
text1 = tk.Text(frame1, height = 10, width = 50)
text1.pack(pady = 5)     
button1 = tk.Button(frame1, text = "Выполнить", command = encrypt_text)
button1.pack(pady = 10)

#Страница дешифрования
label2 = tk.Label(frame2, text = "Расшифровать текст")
label2.pack(pady = 20)
label2_1 = tk.Label(frame2, text = "Введите величину шага:")
label2_1.pack(pady = 5)
entry2 = tk.Entry(frame2, width = 10)
entry2.pack(pady = 5)
text2 = tk.Text(frame2, height = 10, width = 50)
text2.pack(pady = 5)
button2 = tk.Button(frame2, text = "Выполнить", command = decrypt_text)
button2.pack(pady = 10)

#Страница взлома
label3 = tk.Label(frame3, text = "Взломать зашифрованный текст")
label3.pack(pady = 20)
text3 = tk.Text(frame3, height = 10, width = 50)
text3.pack(pady = 10)
button3 = tk.Button(frame3, text = "Выполнить", command = break_from_text)
button3.pack(pady = 10)
Shift = tk.Label(frame3, bg = "lightcoral", text = " ")
Shift.pack(fill = "both", padx = 5, expand=True)

# Начнем с первой страницы
current_frame = frame1
current_frame.pack(fill = "both", expand = True)

def change_page(event):
    global current_frame
    current_frame.pack_forget()
    choice = combobox.get()
    if choice == "Зашифровать":
        current_frame = frame1
    elif choice == "Расшифровать":
        current_frame = frame2
    elif choice == "Взломать шифр":
        current_frame = frame3
    current_frame.pack(fill = "both", expand = True)

combobox.bind("<<ComboboxSelected>>", change_page)

window.mainloop()
