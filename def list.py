friends = ["Zulu", "Dennis", "Yannick", "Robust"]
lucky_numbers = [33, 29, 468, 4, 62]

def handle():

    friends.sort()

    print("When " + friends[0] + " comes over " + friends[2] + " gets jealous")



handle()

def opinion(lucky_numbers):

    lucky_numbers.sort()
    friends.sort()
    lucky_numbers.extend(friends)

    print(lucky_numbers)

    print(lucky_numbers[4])

opinion(lucky_numbers)

num1 = input("What is 100 + 100?: ")
num2 = 200

if int(num1) == num2:

    print("Correct!")

else:

    print("Wrong!")


def character_names(name):

    print("hello " + name)

character_names("Beth")
