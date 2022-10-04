import pyperclip
import googletrans
import gtts
import playsound
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter import ttk
import os


def voice():
            running = True
            while running:
                i=1
                gtt = gtts.gTTS(mainsss.text)
                gtt.save(f'{os.getcwd()}/Voices/{mainsss.text[0:4]}.mp3')
                if os.path.exists(f"{os.getcwd()}/Voices/{mainsss.text}.mp3"):
                    running=False
                print(mainsss.text)
                playsound.playsound(f'{os.getcwd()}/Voices/{mainsss.text[0:4]}.mp3')
                
                i+=1
def copys():
        return pyperclip.copy(mainsss.text)
        
def trans():
    global disable
    global e1
    global destss
    global mainsss
    global translated
    if len(translate.get())<3:
        tmsg.showinfo("Error","Please Enter a word with atlest 4 alphabets")
    else:
        mains = googletrans.Translator()
        mainsss = mains.translate(f"{translate.get()}",dest=destss)
        e1.delete(0,"end")
        e1.insert(0,mainsss.text)
        disable = disable.replace(DISABLED,"normal")
        but1 = Button(root,text="Copy",bg="#E33E5A",fg="white",font="Roboto 15",relief=FLAT,state=disable,command=copys)
        but1.place(x=320,y=410)
        but2 = Button(root,text="Voice",bg="#E33E5A",fg="white",font="Roboto 15",relief=FLAT,state=disable,command=voice)
        but2.place(x=550,y=410)
        if destss == "ko":
             disable = disable.replace("normal",DISABLED,)
             but2 = Button(root,text="Voice",bg="gray",fg="white",font="Roboto 15",relief=FLAT,state=disable,command=voice)
             but2.place(x=550,y=410)
        elif destss =="ur":
             disable = disable.replace("normal",DISABLED,)
             but2 = Button(root,text="Voice",bg="gray",fg="white",font="Roboto 15",relief=FLAT,state=disable,command=voice)
             but2.place(x=550,y=410)
        elif destss == "ar":
             disable = disable.replace("normal",DISABLED,)
             but2 = Button(root,text="Voice",bg="gray",fg="white",font="Roboto 15",relief=FLAT,state=disable,command=voice)
             but2.place(x=550,y=410)
        elif destss == "sd":
             disable = disable.replace("normal",DISABLED,)
             but2 = Button(root,text="Voice",bg="gray",fg="white",font="Roboto 15",relief=FLAT,state=disable,command=voice)
             but2.place(x=550,y=410)
        elif destss == "zh-cn":
             disable = disable.replace("normal",DISABLED,)
             but2 = Button(root,text="Voice",bg="gray",fg="white",font="Roboto 15",relief=FLAT,state=disable,command=voice)
             but2.place(x=550,y=410)
        elif destss == "vi":
             disable = disable.replace("normal",DISABLED,)
             but2 = Button(root,text="Voice",bg="gray",fg="white",font="Roboto 15",relief=FLAT,state=disable,command=voice)
             but2.place(x=550,y=410)
        elif destss == "hi":
             disable = disable.replace("normal",DISABLED,)
             but2 = Button(root,text="Voice",bg="gray",fg="white",font="Roboto 15",relief=FLAT,state=disable,command=voice)
             but2.place(x=550,y=410)
        elif destss == "ta":
             disable = disable.replace("normal",DISABLED,)
             but2 = Button(root,text="Voice",bg="gray",fg="white",font="Roboto 15",relief=FLAT,state=disable,command=voice)
             but2.place(x=550,y=410)
        elif destss == "ja":
             disable = disable.replace("normal",DISABLED,)
             but2 = Button(root,text="Voice",bg="gray",fg="white",font="Roboto 15",relief=FLAT,state=disable,command=voice)
             but2.place(x=550,y=410)
        
def q1():
    global destss
    destss="fr"
def q2():
    global destss
    destss="uz"
def q3():
    global destss
    destss="it"
def q4():
    global destss
    destss="sv"
def q5():
    global destss
    destss="vi"
def q6():
    global destss
    destss="id"
def q7():
    global destss
    destss="ko"
def q8():
    global destss
    destss="zh-cn"
def q9():
    global destss
    destss="de"
def q10():
    global destss
    destss="ar"
def q11():
    global destss
    destss="tr"
def q12():
      global destss
      destss="ur"
def q13():
      global destss
      destss="hi"
def q14():
      global destss
      destss="sd"
def q15():
      global destss
      destss="ta"
def q16():
      global destss
      destss="ja"
def q17():
      global destss
      destss="en"
def q18():
      global destss
      destss="tl"
def det():
    pass
    
root=Tk()
root.geometry("700x550")
root.title("Language Translator by Bilal")
f1 = Frame(root,width=700,height=410)
f1.pack(pady=60)
Label(f1,text="Language Translator",font="Roboto 30",bg="#1A1B2F",fg="#EFFBFF").pack(expand=True,pady=25)
opt = ttk.Menubutton(root,text="Translate To")
opt.place(x=570,y=100)
opt.menu = Menu(opt,tearoff=0,font="Roboto 15",bg="#162447",fg="#EFFBFF")
opt['menu'] = opt.menu
opt.menu.add_command(label = "Translate to French",command=q1)
opt.menu.add_command(label = "Translate to Uzbek",command=q2)
opt.menu.add_command(label = "Translate to Italian",command=q3)
opt.menu.add_command(label = "Translate to Sewdish",command=q4)
opt.menu.add_command(label = "Translate to Vietnamese",command=q5)
opt.menu.add_command(label = "Translate to Indonasian",command=q6)
opt.menu.add_command(label = "Translate to Korean",command=q7)
opt.menu.add_command(label = "Translate to Chinese",command=q8)
opt.menu.add_command(label = "Translate to German",command=q9)
opt.menu.add_command(label = "Translate to Arabic",command=q10)
opt.menu.add_command(label = "Translate to Turkish",command=q11)
opt.menu.add_command(label = "Translate to Urdu",command=q12)
opt.menu.add_command(label = "Translate to Hindi",command=q13)
opt.menu.add_command(label = "Translate to Sindhi",command=q14)
opt.menu.add_command(label = "Translate to Tamil",command=q15)
opt.menu.add_command(label = "Translate to Japneese",command=q16)
opt.menu.add_command(label = "Translate to English",command=q17)
opt.menu.add_command(label = "Translate to Flipino",command=q18)
disable = DISABLED

opt1 = ttk.Menubutton(root,text="Automatic Detect")
opt1.place(x=30,y=100)
opt1.menu = Menu(opt,tearoff=0,font="Roboto 15",bg="#162447",fg="#EFFBFF")
opt1['menu'] = opt1.menu
# opt1.menu.add_command(label = "Automatic Detect",command=det)
opt1.menu.add_command(label = "Translate From English",command=q17)

translate = Entry(f1,width=410,font="Roboto 30",bg="#1F4068",fg="#EFFBFF")
translate.pack(pady=20)
but = Button(root,text="Translate",bg="#E33E5A",fg="white",font="Roboto 15",relief=FLAT,command=trans)
but.place(x=60,y=410)
but1 = Button(root,text="Copy",bg="gray",fg="white",font="Roboto 15",relief=FLAT,state=disable,command=copys)
but1.place(x=320,y=410)
but2 = Button(root,text="Voice",bg="gray",fg="white",font="Roboto 15",relief=FLAT,state=disable,command=voice)
but2.place(x=550,y=410)
translated= StringVar()
Label(f1,text="Output",font="Roboto 32",fg="#EFFBFF",bg="#1A1B2F").pack(expand=True)
e1 = Entry(f1,width=350,font="Roboto 30",bg="#1F4068",fg="white")

e1.pack(side=BOTTOM,pady=20)
root.config(bg="#1A1B2F")
f1.config(bg="#1A1B2F")
root.resizable(False,False)
root.mainloop()
