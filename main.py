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


#Again cards
@carousel_app.transition("card2", "click", "again")
def again(app, card):
    return "card1"

@carousel_app.transition("card11", "click", "again")
def again(app, card):
    return "card1"

@carousel_app.transition("card12", "click", "again")
def againy(app, card):
    return "card1"

@carousel_app.transition("card13", "click", "again")
def again(app, card):
    return "card1"

@carousel_app.transition("card14", "click", "again")
def again(app, card):
    return "card1"

@carousel_app.transition("card16", "click", "again")
def again(app, card):
    return "card1"

@carousel_app.transition("card18", "click", "again")
def again(app, card):
    return "card1"

@carousel_app.transition("card20", "click", "again")
def again(app, card):
    return "card1"

@carousel_app.transition("card22", "click", "again")
def again(app, card):
    return "card1"

@carousel_app.transition("card23", "click", "again")
def again(app, card):
    return "card1"

@carousel_app.transition("card24", "click", "again")
def again(app, card):
    return "card1"

@carousel_app.transition("card26", "click", "again")
def again(app, card):
    return "card1"

@carousel_app.transition("card31", "click", "again")
def again(app, card):
    return "card1"

@carousel_app.transition("card32", "click", "again")
def again(app, card):
    return "card1"

@carousel_app.transition("card38", "click", "again")
def again(app, card):
    return "card1"

@carousel_app.transition("card40", "click", "again")
def again(app, card):
    return "card1"






#going to 2
@carousel_app.transition("card1", "click", "go_to_2")
def go_to_2(app, card):
    return "card2"

#going to 3
@carousel_app.transition("card1", "click", "go_to_3")
def go_to_3(app, card):
    return "card3"

#going to 4
@carousel_app.transition("card3", "click", "go_to_4")
def go_to_4(app, card):
    return "card4"

#going to 5
@carousel_app.transition("card4", "click", "go_to_5")
def go_to_5(app, card):
    return "card5"

#going to 6
@carousel_app.transition("card4", "click", "go_to_6")
def go_to_6(app, card):
    return "card6"

#going to 7
@carousel_app.transition("card4", "click", "go_to_7")
def go_to_7(app, card):
    return "card7"

#going to 8
@carousel_app.transition("card5", "click", "go_to_8")
def go_to_8(app, card):
    return "card8"

@carousel_app.transition("card7", "click", "go_to_8")
def go_to_8(app, card):
    return "card8"

@carousel_app.transition("card33", "click", "go_to_8")
def go_to_8(app, card):
    return "card8"

@carousel_app.transition("card37", "click", "go_to_8")
def go_to_8(app, card):
    return "card8"


#going to 9
@carousel_app.transition("card8", "click", "go_to_9")
def go_to_9(app, card):
    return "card9"

#going to 10
@carousel_app.transition("card9", "click", "go_to_10")
def go_to_10(app, card):
    return "card10"

#going to 11
@carousel_app.transition("card6", "click", "go_to_11")
def go_to_11(app, card):
    return "card11"

#going to 12
@carousel_app.transition("card6", "click", "go_to_12")
def go_to_12(app, card):
    return "card12"

#going to 13
@carousel_app.transition("card6", "click", "go_to_13")
def go_to_13(app, card):
    return "card13"

#going to 14


#going to 15


#going to 16
@carousel_app.transition("card9", "click", "go_to_16")
def go_to_16(app, card):
    return "card16"

#going to 17
@carousel_app.transition("card7", "click", "go_to_17")
def go_to_17(app, card):
    return "card17"

#going to 18
@carousel_app.transition("card17", "click", "go_to_18")
def go_to_18(app, card):
    return "card18"

#going to 19
@carousel_app.transition("card17", "click", "go_to_19")
def go_to_19(app, card):
    return "card19"

#going to 20
@carousel_app.transition("card19", "click", "go_to_20")
def go_to_20(app, card):
    return "card20"

#going to 21
@carousel_app.transition("card17", "click", "go_to_21")
def go_to_21(app, card):
    return "card21"

@carousel_app.transition("card27", "click", "go_to_21")
def go_to_21(app, card):
    return "card21"


#going to 22
@carousel_app.transition("card21", "click", "go_to_22")
def go_to_22(app, card):
    return "card22"

#going to 23
@carousel_app.transition("card21", "click", "go_to_23")
def go_to_23(app, card):
    return "card23"

#going to 24
@carousel_app.transition("card21", "click", "go_to_24")
def go_to_24(app, card):
    return "card24"

#going to 25
@carousel_app.transition("card10", "click", "go_to_25")
def go_to_25(app, card):
    return "card25"

#going to 26
@carousel_app.transition("card25", "click", "go_to_26")
def go_to_26(app, card):
    return "card26"

#going to 27
@carousel_app.transition("card10", "click", "go_to_27")
def go_to_27(app, card):
    return "card27"

#going to 28
@carousel_app.transition("card5", "click", "go_to_28")
def go_to_28(app, card):
    return "card28"

#going to 29
@carousel_app.transition("card28", "click", "go_to_29")
def go_to_29(app, card):
    return "card29"

#going to 30
@carousel_app.transition("card29", "click", "go_to_30")
def go_to_30(app, card):
    return "card30"

#going to 31
@carousel_app.transition("card29", "click", "go_to_31")
def go_to_31(app, card):
    return "card31"

#going to 32
@carousel_app.transition("card30", "click", "go_to_32")
def go_to_32(app, card):
    return "card32"

#going to 33
@carousel_app.transition("card30", "click", "go_to_33")
def go_to_33(app, card):
    return "card33"

#going to 34
@carousel_app.transition("card28", "click", "go_to_34")
def go_to_34(app, card):
    return "card34"

#going to 35
@carousel_app.transition("card34", "click", "go_to_35")
def go_to_35(app, card):
    return "card35"

#going to 36
@carousel_app.transition("card35", "click", "go_to_36")
def go_to_36(app, card):
    return "card36"

#going to 37
@carousel_app.transition("card35", "click", "go_to_37")
def go_to_37(app, card):
    return "card37"

#going to 38
@carousel_app.transition("card34", "click", "go_to_38")
def go_to_38(app, card):
    return "card38"

#going to 39
@carousel_app.transition("card34", "click", "go_to_39")
def go_to_39(app, card):
    return "card39"

#going to 40
@carousel_app.transition("card39", "click", "go_to_40")
def go_to_40(app, card):
    return "card40"






























































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



