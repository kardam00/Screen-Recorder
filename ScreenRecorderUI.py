# Python screen recorder UI
from tkinter import *
from ScreenRecorder import record


def close():
    screen_recorder.destroy()


# Define the user interface for Screen Recorder
screen_recorder = Tk()
screen_recorder.geometry('400x300')
screen_recorder.title('Screen Recorder')

bg_img = PhotoImage(file='black.png')

# Show image using label
label1 = Label(screen_recorder, image=bg_img, bd=0)
label1.pack()

# Create and place the components
title_label = Label(screen_recorder, text="Screen Recorder", font=('Ubuntu Mono', 16),foreground='white', bg='#000000')
title_label.place(relx=0.5, rely=0.1, anchor=CENTER)
info_label = Label(screen_recorder, text="Enter 'e' to exit screen recording", foreground='white', bg='#000000')
info_label.place(relx=0.5, rely=0.3, anchor=CENTER)
screen_button = Button(screen_recorder, text='Record Screen', fg='#ffffff', bg='#000000', command=record, relief=RAISED)
screen_button.place(relx=0.5, rely=0.6, anchor=CENTER)
close_button = Button(screen_recorder, text='Close', fg='#ffffff', bg='#000000', command=close, relief=RAISED)
close_button.place(relx=0.5, rely=0.9, anchor=CENTER)

screen_recorder.mainloop()
