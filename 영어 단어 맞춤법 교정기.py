from textblob import TextBlob
from tkinter import*
from tkinter import messagebox
from tkinter import font

window = Tk()
window.title("영어 단어 맞춤법 교정기")
window.geometry("640x480")

fontE = font.Font(size=16)
fontB = font.Font(size = 12)
fontH = font.Font(size = 15)

ent = Entry(window, width = 12, font = fontE)
ent.pack(pady=70)

misspelled = []
wrongHis = {}

def enter():
    misspelled.insert(0,ent.get())
    for word in misspelled:
        if word == str(TextBlob(word).correct()):
            message=messagebox.showinfo("검사 결과","교정할 철자가 없습니다.")
        else:
            message=messagebox.showinfo("검사 결과",f"올바른 철자 : {str(TextBlob(word).correct())}")
            wrongHis[str(TextBlob(word).correct())]=word
    del misspelled[0]

def click():
    dialog=Toplevel()
    dialog.title("지금까지 틀린 단어")
    dialog.geometry('480x360')
    for key in wrongHis:
        message = Message(dialog, text="Corrected word: {} \nYour word: {}".format(key, wrongHis[key]), font = fontH,aspect = 450)
        message.pack(pady=10)

Button(text="enter", command = enter, width = 6, height = 1,font = fontB).pack()
Button(text="지금까지 틀린 단어 보기", command = click,width=20,height=1,font = fontB).pack(pady=50)

window.mainloop()
        
