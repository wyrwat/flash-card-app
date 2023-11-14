from tkinter import *
from tkmacosx import Button
from copy import copy
from PIL import Image, ImageTk

BG_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BG_COLOR)


def right_btn():
    pass


# UI
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BG_COLOR)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 266, image=card_front)
french_side = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))
french_word = canvas.create_text(400, 253, text="temp", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=1, row=1, columnspan=2)

right_img_pil = Image.open("images/right.png")
wrong_img_pil = Image.open("images/wrong.png")

right_img = ImageTk.PhotoImage(right_img_pil)
wrong_img = ImageTk.PhotoImage(wrong_img_pil)

right_bt = Button(image=right_img, highlightbackground=BG_COLOR, highlightthickness=0, bg=BG_COLOR, borderless=1,
                  borderwidth=3, takefocus=0, focuscolor='')
wrong_bt = Button(image=wrong_img, highlightbackground=BG_COLOR, highlightthickness=0, bg=BG_COLOR, borderless=1,
                  borderwidth=3, takefocus=0, focuscolor='')
right_bt.grid(column=1, row=2)
wrong_bt.grid(column=2, row=2)


window.mainloop()
