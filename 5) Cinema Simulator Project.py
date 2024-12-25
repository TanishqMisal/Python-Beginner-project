# CINEMA SIMULATOR PROJECT

movie = {
    "Animal":[18,10],
    "Dunki":[12,10],
    "Salaar":[14,10],
    "Sambahadur":[14,5]
    }

while True:

    choice = input("WHAT FILM WOULD YOU LIKE TO WATCH?:").strip().title()

    if choice in movie:
        age = int(input("ENTER YOU AGE:").strip())

        if age >= movie[choice][0]:

            if movie[choice][1] > 0:
                print("ENJOY YOUR FILM")
                movie[choice][1] = movie[choice][1] - 1
                print(movie)
            else:
                print("SORRY, THE TICKETS ARE SOLD OUT")
        else:
            print("YOUR AGE IS NOT INFO AS PER THE MOVIE GUIDELINES")
        
    else:   
        print("SORRY! WE ARE NOT FILMING THAT YET.")
