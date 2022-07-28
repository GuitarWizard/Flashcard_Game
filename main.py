from tkinter import *
import pandas
import random

# Note - There is a known bug in this file: Clicking the buttons before the timer
# runs out messes with the count down

# timer = None
# TIME = 4

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Times New Roman", 18, "italic")
QUESTION_FONT = ("Times New Roman", 20, "bold")

# note: you can add images to buttons like this:
# my_image = PhotoImage(file="path/to/image_file.png"
# button = Button(image=my_image, highlightthickness=0)

data = pandas.read_csv("Bokmal_words.csv")

reoriented_dict = data.to_dict(orient="records")


# def new_card():
#
#     global current_card
#     canvas.itemconfig(card_title, text="English", fill="black")
#     current_card = random.choice(reoriented_dict)
#     canvas.itemconfig(card_word, text=current_card["English"], fill= "black")
#     canvas.itemconfig(clock, fill="black")
#     canvas.itemconfig(canvas_image, image=flashcard_front)
#     canvas.itemconfig(card_title, text="Bokmål")
#     canvas.itemconfig(card_word, text=current_card["Bokmål"])
#     count_down(TIME)
#
# def count_down(count):
#
#     if count > 0:
#         global timer
#         timer = window.after(1000, count_down, count - 1)
#         canvas.itemconfig(clock, text=count)
#     else:
#         canvas.itemconfig(card_title, text="English", fill="white")
#         canvas.itemconfig(card_word, text=current_card["English"], fill="white")
#         canvas.itemconfig(clock, text=count, fill="white")
#         canvas.itemconfig(canvas_image, image=flashcard_back)

current_card = {}
to_learn_dict= {"Bokmal":"English"}


def words_to_learn():
    global to_learn_dict
    to_learn_dict.update({current_card["Bokmal"]:current_card["English"]})
    norwegian_word = current_card["Bokmal"]
    english_word = current_card["English"]
    print(to_learn_dict)
    next_card()

    with open("study_list.txt", mode='a') as study_file:
        study_file.write(f"{norwegian_word} : {english_word}\n")




def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(reoriented_dict)
    canvas.itemconfig(canvas_image, image=flashcard_front)
    canvas.itemconfig(card_title, text="Bokmål", fill="black")
    canvas.itemconfig(card_word, text=current_card["Bokmal"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=flashcard_back)

def quit_game():
    # dataframe = pandas.DataFrame(to_learn_dict, index=[0])
    # print("\n")
    #
    # print(dataframe)
    # print("\n")
    #
    # study_list = dataframe.to_dict(orient="dict")
    # print("Study list:\n")
    # print(study_list)
    # study_list.remove("")
    # study_list=pandas.DataFrame(study_list).transpose()
    #
    # study_list.to_csv("study_list.csv")
    print(to_learn_list)


# -------------UI SETUP _________________________
window = Tk()
window.title("Learn Bokmål")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=800, height=600)
flip_timer = window.after(3000, func=flip_card)

# ------------FLASHCARD----------------------------
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_front = PhotoImage(file="images/card_front.png")
flashcard_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=flashcard_front)
canvas.grid(columnspan=2, column=0, row=0)

card_title = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="", font=QUESTION_FONT)

# clock = canvas.create_text(400, 400, text="5", font=LANGUAGE_FONT)


# ------------BUTTONS----------------------------
correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
correct_button.grid(column=0, row=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=words_to_learn)
wrong_button.grid(column=1, row=2)

# exit_button = Button(text="Save study list\n and exit", highlightthickness=0, command=quit_game)
# exit_button.grid(column = 0, row =3)


next_card()
# count_down(TIME)

window.mainloop()
