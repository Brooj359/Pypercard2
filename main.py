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





@carousel_app.transition("card2", "click", "again")
def again(app, card):
    return "card1"

carousel_app.start("card1")



