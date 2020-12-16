def solution(input_from_question):

    #bottle_size available
    gal_1 = 1
    gal_5 = 5
    gal_7 = 7
    gal_10 = 10

    if input_from_question >= gal_10:
        if (input_from_question % gal_10) == 0:
            min_required = int(input_from_question/gal_10)
        if (input_from_question > 11) & (input_from_question < 15):
            min_required = 1
            remaining = input_from_question - gal_7
            if remaining >= gal_5:
                min_required += 1
                remaining = remaining - gal_5
                if remaining >= gal_1:
                    min_required += (remaining * 1)
        else:
            if (input_from_question % gal_10) != 0:
                min_required = int(input_from_question/gal_10)
                remaining = input_from_question - (min_required * gal_10)
                if ((remaining > gal_7) and (remaining < gal_10)) or (remaining == gal_7):
                    min_required += 1
                    remaining = remaining - gal_7
                    if (remaining > gal_1) or (remaining == gal_1):
                        min_required += (remaining * 1)
                if ((remaining > gal_5) and (remaining < gal_7)) or (remaining == gal_5):
                    min_required += 1
                    remaining = remaining - gal_5
                    if (remaining > gal_1) or (remaining == gal_1):
                        min_required += (remaining * 1)
                if ((remaining > gal_1) and (remaining < gal_5)) or (remaining == gal_1):
                    min_required += (remaining * 1)
                    
    if (input_from_question >= gal_7) and (input_from_question < gal_10):
        if (input_from_question % gal_7) == 0:
            min_required = 1
        if (input_from_question % gal_7) != 0:
            min_required = int(input_from_question/gal_7)
            remaining = input_from_question - gal_7
            if (remaining > gal_1) or (remaining == gal_1):
                min_required += (remaining * 1)

    if (input_from_question >= gal_5) and (input_from_question < gal_7):
        if (input_from_question % gal_5) == 0:
            min_required = 1
        if (input_from_question % gal_5) != 0:
            min_required = int(input_from_question/gal_5)
            remaining = input_from_question - gal_5
            if (remaining > gal_1) or (remaining == gal_1):
                min_required += (remaining * 1)

    if (input_from_question >= gal_1) and (input_from_question < gal_5):
        min_required = (input_from_question * 1)

    return min_required
