import tkinter as tk
from tkinter import *
from tkinter import messagebox
from data import morse_alphabet

class App:
    def trancelate(self):
        """Перевод введенную строку в код Морзе"""
        self.string = ""
        self.value = self.input.get(1.0, END)

        for letter in self.value[::1]:
            try:
                self.string += f" {morse_alphabet[letter]}"
            except KeyError as error_message:
                messagebox.showinfo(title="Ошибка ввода",
                                       message=f"Строка содержит не верный символ - {error_message}.\n "
                                                "Используйте для ввода буквы русского алфавита,"
                                                "числа и знаки препинания.")
                break
        self.output.delete(1.0, END)
        self.output.insert(END,f"{self.string}")
    def delete(self):
        """Очистка полей ввода и вывода"""
        self.input.delete(1.0, END)
        self.output.delete(1.0, END)


    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Morse-converter")
        self.window.minsize(width=300, height=300)
        self.window.config(width=500, height=500, padx=20, pady=20)
        self.text_label = tk.Label(text="Текст", font=("Arial", 24, "bold"))
        self.text_label.grid(row=1, column=3)
        self.input = Text(width=80, height=5)
        self.input.grid(row=2, column=2, columnspan=5)
        self.input.focus()
        self.translate_button = Button(text="Перевести", command=self.trancelate, width=15, height=2)
        self.translate_button.grid(row=3, column=2, padx=10, pady=10)
        self.translate_button.config(bg="#85c74c")
        self.delete_button = Button(text="Очистить", command=self.delete, width=15, height=2)
        self.delete_button.config(bg="#e04848")
        self.delete_button.grid(row=3, column=4, padx=10, pady=10)
        self.morse_label = tk.Label(text="Морзе", font=("Arial", 24, "bold"))
        self.morse_label.grid(row=4, column=3)
        self.output = Text(width=80, height=5)
        self.output.grid(row=5, column=2, columnspan=3)
        self.window.mainloop()












