# ANOYING Baby Conversation Simulator

print("THIS A BABY SIMULATOR WHO IS GOINING TO ASK YOU WHY AGAIN AND AGAIN TO BREAK THE LOOP YOU SHOULD TYPE (just because)")


from random import choice

questions = ["Q:Why IS THE SKY BLUE?:","Q:WHY DO WE EAT FOOD?:","Q:WHY DO FISH LIVE IN WATER?:"]

question = choice(questions)
answer = input(question).lower().strip()

while answer != "just because":
    answer = input("WHY?:").strip().lower()

print("OHH...I WAS JUST CURIOUS")
