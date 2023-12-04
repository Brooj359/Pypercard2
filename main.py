"""
This simple app demonstrates how cards can automatically advance to another
card after a certain amount of time. The auto_advance can either be a string
containing the name of the next card, or a function to call that returns the
name of the next card.
"""
from pypercard import App, Card




# Create the app while ensuring the counter is reset.

carousel_app = App(
    name="PyperCard carousel", datastore={"counter": 0},
)


# This is what is used as ex:
# @carousel_app.transition("card2", "click", "reset")
# def reset(app, card):
#     return "card1"

@carousel_app.transition("card1", "click", "end_journey")
def end_journey(app, card):
    return "card2"

@carousel_app.transition("card1", "click", "go_to_3")
def go_to_3(app, card):
    return "card3"

@carousel_app.transition("card3", "click", "go_to_4")
def go_to_4(app, card):
    return "card4"

@carousel_app.transition("card4", "click", "go_to_5")
def go_to_5(app, card):
    return "card5"

@carousel_app.transition("card4", "click", "go_to_6")
def go_to_6(app, card):
    return "card6"

@carousel_app.transition("card4", "click", "go_to_7")
def go_to_7(app, card):
    return "card7"

@carousel_app.transition("card5", "click", "go_to_8")
def go_to_8(app, card):
    return "card8"

@carousel_app.transition("card5", "click", "go_to_9")
def go_to_9(app, card):
    return "card9"

@carousel_app.transition("card6", "click", "go_to_11")
def go_to_11(app, card):
    return "card11"

@carousel_app.transition("card6", "click", "go_to_12")
def go_to_12(app, card):
    return "card12"

@carousel_app.transition("card6", "click", "go_to_13")
def go_to_13(app, card):
    return "card13"

@carousel_app.transition("card9", "click", "go_to_8")
def go_to_8(app, card):
    return "card8"

@carousel_app.transition("card8", "click", "go_to_10")
def go_to_10(app, card):
    return "card10"

@carousel_app.transition("card10", "click", "go_to_14")
def go_to_14(app, card):
    return "card14"

@carousel_app.transition("card10", "click", "go_to_15")
def go_to_15(app, card):
    return "card15"
























@carousel_app.transition("card2", "click", "again")
def again(app, card):
    return "card1"

@carousel_app.transition("card11", "click", "again")
def again(app, card):
    return "card1"

@carousel_app.transition("card12", "click", "again")
def again(app, card):
    return "card1"

@carousel_app.transition("card13", "click", "again")
def again(app, card):
    return "card1"

carousel_app.start("card1")



