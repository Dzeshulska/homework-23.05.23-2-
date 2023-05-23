window_area_adult = 3
window_area_children = 1
window_area_rooms = 5

book = "2-1-1".split("-")

book_in_numbers = map(lambda number: int(number), book)

adult, children, rooms = book_in_numbers

if adult > window_area_adult:
    while adult > window_area_adult:
        adult = adult - 1
        print(adult)

else:
    while adult < window_area_adult:   
        adult = adult + 1   
        print(adult)