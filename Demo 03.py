from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.title('kate')
root.geometry('700x499')

img = ImageTk.PhotoImage(Image.open('Voice ASSISTANT KATE(1).jpg'))
panel = Label(root, image=img)
panel.pack(side='right', fill='both', expand='no')


uT = StringVar()
uT.set('Your Virtual Assistant')
uF = LabelFrame(root, text='Kate', font=('Railways',24, 'bold'))
uF.pack(fill='both',expand='yes')

top = Message(uF, textvariable=uT, bg='black', fg='white')
top.config(font=('Century Gothic', 15, 'bold'))
top.pack(side='top', fill='both', expand='no')

btn = Button(root, text='Run',  font=('railways',10,'bold'),bg='red',fg='white').pack(fill='x',expand='no')
btn2 = Button(root, text='Close', font=('railways',10,'bold'),bg='blue',fg='white', command=root.destroy).pack(fill='x',expand='no')

root.mainloop()


