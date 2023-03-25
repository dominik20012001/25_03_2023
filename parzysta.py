def rokPrzestepny(rok):
    int(input)
    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
        return True
    return False

