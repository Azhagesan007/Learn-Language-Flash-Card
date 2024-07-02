from tkinter import *
import pandas
import json
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
data_words = None
cho = None


def front_card(cho1):
    canvas.itemconfig(images, image=f_photos)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=data_words["French"][cho1])
    window.after(3000, back_card, cho)


def back_card(cho1):
    canvas.itemconfig(images, image=b_photos)
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=data_words["English"][cho1])


def create_file():
    with open(file=".\\data\\remaining_words.json", mode="w") as file:
        data = pandas.read_csv(".\\data\\french_words.csv")
        data1 = data.to_dict()
        json.dump(data1, file, indent=4)


def flash_card():
    global data_words, cho
    try:
        with open(file=".\\data\\remaining_words.json", mode="r") as file:
            data_words = json.load(file)
    except FileNotFoundError:
        create_file()
        flash_card()
    else:
        choice_list = [n for n in data_words["French"]]
        cho = choice(choice_list)
        print(cho)
        front_card(cho)


def clicked_right():
    del data_words["French"][cho]
    del data_words["English"][cho]
    with open(file=".\\data\\remaining_words.json", mode="w") as file:
        json.dump(data_words, file, indent=4)
    flash_card()


def clicked_wrong():
    flash_card()


window = Tk()
window.title("Flashing Card")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
# window.minsize(width=1000, height=1000)

canvas = Canvas()
canvas.config(width=800, height=526, highlightthickness=0, bg= BACKGROUND_COLOR)
f_photos = PhotoImage(file=".\\images\\card_front.png")
b_photos = PhotoImage(file=".\\images\\card_back.png")
r_photos = PhotoImage(file=".\\images\\right.png")
w_photos = PhotoImage(file=".\\images\\wrong.png")
images = canvas.create_image(400, 263)

title_text = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

wrong_button = Button(image=w_photos, bg=BACKGROUND_COLOR, borderwidth=0, command=clicked_wrong)
right_button = Button(image=r_photos, bg=BACKGROUND_COLOR, borderwidth=0, command=clicked_right)

canvas.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

flash_card()


window.mainloop()
