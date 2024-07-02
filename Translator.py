from tkinter import *
from tkinter import ttk
# to make translator we have to import google translator 
from googletrans import Translator,LANGUAGES

def change(text,src,dest):
    src1=src
    dest1=dest
    trans=Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    source_data = combo_source.get()
    destination_data = dest_source.get()
    message = source.get(1.0,'end')
    return_message = change(message,src=source_data,dest=destination_data)
    dest.delete(1.0,'end')
    dest.insert('end',return_message)

win = Tk()
win.title('TRANSLATOR')
win.geometry("500x500")  #--> graphic kaisa dikay dega width x length
win.config(bg='#8fd2eb')

label1 =Label(win , text='Translator',font=('Times New Roman',20,'bold'),fg='#083e52',bg='#2d96bd')
label1.place(x=90 , y=20 , height=40 , width=300)

frame1 =Frame(win).pack(side='bottom')
label2 =Label(win , text='Enter Text',font=('Times New Roman',20,'bold'),fg='#2d2f30',bg='#8fd2eb')
label2.place(x=90 , y=90 , height=30 , width=300)

source =Text(frame1,font=("Times New Roman",16,'bold'),wrap='word',bg='#c6e8f5')
source.place(x=10,y=130,height=80,width=480)

list_text = list(LANGUAGES.values())
list_text1 = [i.title() for i in list_text]
label_1 =Label(frame1 , text='Entered Text is',fg='#2d2f30',bg='#8fd2eb')
label_1.place(x=20 , y=230 , height=25 , width=130)
combo_source = ttk.Combobox(frame1,value = list_text1,state='readonly')
combo_source.place(x=20,y=250,height=25,width=130)
combo_source.set("English")

button1 =Button(frame1,text="Translate",relief='raised',command = data)
button1.place(x=160,y=250,height=25,width=175)

label_2 =Label(frame1 , text='Translate Text To',fg='#2d2f30',bg='#8fd2eb')
label_2.place(x=345 , y=230 , height=25 , width=130)
dest_source = ttk.Combobox(frame1,value = list_text1,state='readonly')
dest_source.place(x=345,y=250,height=25,width=130)
dest_source.set("English")

label3 =Label(win , text='Translated Text',font=('Times New Roman',20,'bold'),fg='#2d2f30',bg='#8fd2eb')
label3.place(x=90 , y=300 , height=30 , width=300)

dest =Text(frame1,font=("Times New Roman",16,'bold'),wrap='word',bg='#c6e8f5')
dest.place(x=10,y=340,height=80,width=480)

win.mainloop()
