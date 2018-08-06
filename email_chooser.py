



def getParagraph(selection):
    switcher = {
        1: para1,
        2: para2,
        3: para3,
        4: para4,
        5: para5,
        6: para6,
        7: para7,
        8: para8,
        9: para9,
    }
    return switcher.get(selection)
