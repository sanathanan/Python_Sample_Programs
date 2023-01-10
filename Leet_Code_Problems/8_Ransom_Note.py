"""


"""

def ransom_note_problem(ransom_note,magazine):
    # Counting the number of each characters in 'ransom_note' and 'magazine' using dictionary.
    ransom_dict = {}
    magazine_dict = {}

    flag= False

    for i in ransom_note:
        if i not in ransom_dict:
            ransom_dict[i] = 1
        else:
            ransom_dict[i] += 1

    for i in magazine:
        if i not in magazine_dict:
            magazine_dict[i] = 1
        else:
            magazine_dict[i] += 1

    print("Ransom Note: ", ransom_dict)
    print("Magazine: ", magazine_dict)

    # Iterating 'ransom_note' and checking that particular character present in magazine
    # and also checking how many times that particular character present compared to 'ransom_note'.
    for i in ransom_note:
        if i in magazine_dict and magazine_dict[i] >= ransom_dict[i]:
            flag = True
        else:
            flag = False

    return flag

ransom_note = 'aabb'
magazine = 'aabbb'

result = ransom_note_problem(ransom_note,magazine)
print(result)