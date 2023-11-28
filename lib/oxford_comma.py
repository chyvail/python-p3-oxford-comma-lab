def oxford_comma(items):
    if (len(items) == 1):
        return " ".join(items)
    elif (len(items) == 2):
        return " and ".join(items)
    elif(len(items) == 3):
        and_element = "and "+ items[2]
        items.insert(2,and_element)
        items.pop()
        three_items = ", ".join(items)
        return three_items
    else:
        and_element = "and " + items[len(items)-1]
        items.insert(len(items)-1,and_element)
        items.pop()
        more_than_three = ", ".join(items)
        return more_than_three


print(oxford_comma(["kiwi", "durian", "starfruit", "mangos", "dragon fruits", "lychees", "pomelos"]))