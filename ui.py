from tkinter import Canvas, Label, Tk, Button, PhotoImage

FONT = ("Arial", 20, "italic")
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self) -> None:
        self.score = 0
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,background=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125, text="Placeholder Text", font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text=f"Score: {self.score}", background=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.true_image = PhotoImage(file=r"images\true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        self.false_image = PhotoImage(file=r"images\false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()