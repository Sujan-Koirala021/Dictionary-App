"""
This is a simple dictionary app made using tkinter
"""


from tkinter import *
from PyDictionary import PyDictionary
import customtkinter

root = customtkinter.CTk()

root.title('Easy Dictionary')
root.geometry('600x550')
root.iconbitmap('dictionary_icon.ico')

# Custom Tkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


def searchOperation():
    # Clear result box just after submission
    resultBox.delete(1.0, END)

    dictionary = PyDictionary()                         # Create an instance

    # type(meaning) -> dictionary
    meaning = dictionary.meaning(searchBox.get())

    # Find keys and values in meaning(i.e dictionary)
    for key, value in meaning.items():
        resultBox.insert(END, f'{key}\n')
        for values in value:
            resultBox.insert(END, f'->  {values}\n\n')


myFrame = customtkinter.CTkFrame(root, width=600)
myFrame.pack(pady=20, padx=10)

searchBox = customtkinter.CTkEntry(
    myFrame, width=200, height=30, text_font=('Helvetica', 16))
searchBox.grid(row=0, column=0, padx=50, pady=20)

searchButton = customtkinter.CTkButton(
    myFrame, text="Search", command=searchOperation)
searchButton.grid(row=0, column=1, padx=50)

resultBox = Text(root, height=25, width=65)
resultBox.pack()

root.mainloop()
