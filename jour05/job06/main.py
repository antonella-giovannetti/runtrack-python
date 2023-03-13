def notes(list_notes):
    new_list_notes = []
    for i in list_notes:
        if i < 40:
            new_list_notes.append(i)
        elif i % 5 >= 3:
            new_list_notes.append(i + 5 - i % 5)
        else:
            new_list_notes.append(i)
    return new_list_notes

print(notes([80, 40, 83, 82, 38]))