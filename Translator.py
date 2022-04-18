from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox
import pyttsx3

root = Tk()
root.title("Translator")
root.geometry("550x500")
root.resizable(0,0)
root.config(bg = 'light blue')

def both():
    translated_text.delete(1.0, END)

    try:
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_language_key = key

        for key, value in languages.items():
            if (value == translated_combo.get()):
                to_language_key = key

        words = textblob.TextBlob(original_text.get(1.0, END))

        words = words.translate(from_lang=from_language_key, to=to_language_key)

        translated_text.insert(1.0, words)

        voice = pyttsx3.init()

        voice.say(words)

        voice.runAndWait()


    except Exception as e:
        messagebox.showerror("Translator", e)

def translate_it():
    translated_text.delete(1.0, END)

    try:
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_language_key = key

        for key, value in languages.items():
            if (value == translated_combo.get()):
                to_language_key = key

        words = textblob.TextBlob(original_text.get(1.0, END))

        words = words.translate(from_lang=from_language_key, to=to_language_key)

        translated_text.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Translator", e)

def tts():
    translated_text.delete(1.0, END)

    try:
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_language_key = key

        for key, value in languages.items():
            if (value == translated_combo.get()):
                to_language_key = key

        words = textblob.TextBlob(original_text.get(1.0, END))

        words = words.translate(from_lang=from_language_key, to=to_language_key)

        voice = pyttsx3.init()

        voice.say(words)

        voice.runAndWait()

    except Exception as e:
        messagebox.showerror("Translator", e)

def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

languages = googletrans.LANGUAGES
language_list = list(languages.values())

original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)

translated_text = Text(root, height=10, width=40)
translated_text.grid(row=2, column=0, pady=20, padx=10)

original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(26)
translated_combo.grid(row=3, column=0)

both_button = Button(root, text="Translate & Speak", font=(18), fg="black", bg="cyan", command=both)
both_button.grid(row=0, column=1)

translate_button = Button(root, text="Translate", font=(18), fg="black", bg="cyan", command=translate_it)
translate_button.grid(row=1, column=1)

speak_button = Button(root, text="Speak", font=(18), fg="black", bg="cyan", command=tts)
speak_button.grid(row=2, column=1)

clear_button = Button(root, text="CLEAR", fg="black", bg="cyan", command=clear)
clear_button.grid(row=3, column=1)


root.mainloop()