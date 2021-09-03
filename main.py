from googletrans import Translator
from tkinter import messagebox
import json
import tkinter
from tkinter import ttk
from gtts import gTTS
import playsound
import glob, os, os.path
import random


def trans():
    translator = Translator()
    given_text = str(input_text.get(1.0, 'end-1c'))
    lang_selected = str(value_inside.get())
    if len(given_text) > 0:
        if lang_selected in l_name:
            lang_code = str(l_code[l_name.index(lang_selected)])
            result = translator.translate(given_text, dest=lang_code)
            output_text.delete(1.0, 'end-1c')
            if str(result.pronunciation) != "None":
                output_text.insert("end-1c", f"{result.text}\n\n\nPronunciation:\n{result.pronunciation}")

                def play():
                    my_text = result.pronunciation
                    language = lang_code
                    obj = gTTS(text=my_text, lang=language, slow=False)
                    mf = str("hello" + str(random.randint(1, 1000)) + ".mp3")
                    obj.save(mf)
                    playsound.playsound(mf)
                    os.remove(mf)
                    file_list = glob.glob(
                        os.path.join(r"C:\Users\windows\Desktop\Projects\Language Translator", "*.mp3"))
                    for fl in file_list:
                        os.remove(fl)
                pronounce = tkinter.Button(text="Pronunciation", bg="#FACE0F", command=play)
                pronounce.grid(column=2, row=2)
            else:
                def play():
                    my_text = result.text
                    language = 'en'
                    obj = gTTS(text=my_text, lang=language, slow=False)
                    mf = str("hello" + str(random.randint(1, 1000)) + ".mp3")
                    obj.save(mf)
                    playsound.playsound(mf)
                    os.remove(mf)
                    file_list = glob.glob(
                        os.path.join(r"C:\Users\windows\Desktop\Projects\Language Translator", "*.mp3"))
                    for fl in file_list:
                        os.remove(fl)
                pronounce = tkinter.Button(text="Pronunciation", bg="#FACE0F", command=play)
                pronounce.grid(column=2, row=2)
                output_text.insert("end-1c", f"{result.text}")
        else:
            messagebox.showinfo(title='oops!', message='Please select a language to translate')
    else:
        messagebox.showinfo(title='Error', message='Please enter text to translate')


with open("lang.json", "r") as f:
    data = json.load(f)

l_code = [x for x, y in data.items()]
l_name = [y for x, y in data.items()]

# window
window = tkinter.Tk()
window.title('Language Translator')
window.config(padx=50, pady=50, bg="#E8F6EF")
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)

# label
l1 = tkinter.Label(text="Select a Language to Translate", bg="#E8F6EF")
l1.grid(column=0, row=0)
l1.config(pady=10, font=('Arial', 14))
l2 = tkinter.Label(text="→", bg="#E8F6EF")
l2.grid(column=1, row=0)
l2.config(font=('Arial', 30))

# language option
value_inside = tkinter.StringVar(window)
value_inside.set("hindi")
question_menu = ttk.Combobox(window, textvariable=value_inside, values=l_name, width=40)
question_menu.grid(column=2, row=0)

# text area
input_text = tkinter.Text(window, width=30, height=8)
input_text.grid(column=0, row=1)
input_text.config(padx=10, pady=10, font=('Roboto', 18))
output_text = tkinter.Text(window, width=30, height=8)
output_text.grid(column=2, row=1)
output_text.config(padx=10, pady=10, font=('Roboto', 16))

# button
button = tkinter.Button(text="Translate", bg="#FACE0F", command=trans)
button.grid(column=1, row=1, padx=10)
window.mainloop()
