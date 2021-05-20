def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


def boolean():


    is_male = False
    is_tall = True

    if is_male and is_tall:
        print("You are a God amongst men")
    elif is_male and not (is_tall):
        print("You are only a small God")
    elif not (is_male) and is_tall:
        print("You are tall me bruddah")
    else:
        print("You lose")


boolean()
