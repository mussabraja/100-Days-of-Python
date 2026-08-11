from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")

ay = df.to_dict(orient='records')


window = Tk()
window.title("Flash Card Program by Mussab Raja")
window.config(padx=100,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526,bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

#Front Image and Canvas
front_image = PhotoImage(file="images/card_front.png")
front_image_canvas = canvas.create_image(400,263,image = front_image)

#Right and Wrong Images for Button
my_image_right = PhotoImage(file="images/right.png")
my_image_wrong = PhotoImage(file="images/wrong.png")


def random_word():
    ran_word = random.choice(ay)
    return ran_word
card = random_word()
def next_word():
    global card, timer
    window.after_cancel(timer)
    card = random_word()
    canvas.itemconfig(front_image_canvas, image=front_image)
    canvas.itemconfig(word_text_french, text=card["French"],fill='black')
    canvas.itemconfig(French_title, text="French", fill="black")
    timer = window.after(3000,flip)

def flip():
    canvas.itemconfig(front_image_canvas, image=back_image)
    canvas.itemconfig(word_text_french,text=card["English"])
    canvas.itemconfig(French_title,text="English",fill='white')

timer = window.after(3000,flip)

# ay = df.to_dict(orient='records')
# print(ay)
def is_known():
    global card
    ay.remove(card)
    next_word()
    pandas.DataFrame(ay).to_csv("data/words_to_learn.csv", index=False)






#
back_image = PhotoImage(file="images/card_back.png")
#back_image_canvas = canvas.create_image(400,263,image = back_image)

#French Words and Title
word_text_french = canvas.create_text(400,263,text="Word",fill='black',font=("Arial",35,"bold"))
canvas.itemconfig(word_text_french,text=card["French"])
French_title = canvas.create_text(450,150,text="French",fill='black',font=("Arial",35,"bold"))

#Right Button
button_right = Button(image=my_image_right,highlightthickness=0,command=is_known)
button_right.grid(row=1,column=1)

#Wrong Button
button_wrong = Button(image=my_image_wrong,highlightthickness=0,command=next_word)
button_wrong.grid(row=1,column=0)


window.mainloop()
