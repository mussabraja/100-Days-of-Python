
from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self,quiz_brain):
        self.window = Tk()
        self.window.title('Quizzler by Mussab')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.quiz = quiz_brain
        self.image_tick = PhotoImage(file="images/true.png")
        self.image_cross = PhotoImage(file="images/false.png")
        self.canvas = Canvas(width=300,height=250,bg='white',highlightthickness=0)
        self.text = self.canvas.create_text(
            150, 125,
            width=280,
            text=self.quiz.next_question(),
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.button_tick = Button(image=self.image_tick)
        self.button_tick.grid(column=0,row=2)
        self.button_cross =Button(image=self.image_cross)
        self.button_cross.grid(column=1,row=2)
        self.canvas.grid(column=0,row=1,columnspan=2)
        self.window.mainloop()
