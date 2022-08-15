import random


simon_says_list = {
    "Simon says": ["sit", "stand", "walk", "swim", "waddle", "yawn", "sing", "roll over"]}


says = random.choice(list(simon_says_list.keys()))
action = random.choice(simon_says_list[action])


print(says)
print(action)

player = input("What did Simon say? Enter: ")


if player == simon:
    print("Correct!"),
    action = random.choice(list(simon_says_list.keys()))
    simon = random.choice(simon_says_list[action])
    print(says)
    print(action)
    player = input("player: ")

if player == simon:
    print("Correct!"),
    action = random.choice(list(simon_says_list.keys()))
    simon = random.choice(simon_says_list[action])
    print(says)
    print(action)
    player = input("player: ")

if player == simon:
    print("Correct!"),
    action = random.choice(list(simon_says_list.keys()))
    simon = random.choice(simon_says_list[action])
    print(says)
    print(action)
    player = input("player: ")

if player == simon:
    print("Correct!"),
    action = random.choice(list(simon_says_list.keys()))
    simon = random.choice(simon_says_list[action])
    print(says)
    print(action)
    player = input("player: ")

if player == simon:
    print("Correct!"),
    action = random.choice(list(simon_says_list.keys()))
    simon = random.choice(simon_says_list[action])
    print(says)
    print(action)
    player = input("player: ")
    print("Correct! You won simon says!")



else:
   print("Wrong! Simon didn't say that")
   print("Game Ends")
