#  BUILDING TRAVIS!

known_user = [ "Tanishq","Ajay","Abhi","Rushi","Om","Joe"]

while True:
    print("HI! MY NAME IS TRAVIS")
    name = input("WHAT IS YOUR NAME?:").strip().capitalize()

    if name in known_user:
        print("HELLO! {}.".format(name))

        remove = input("WOULD YOU LIKE TO BE REMOVED FROM THE SYSTEM (Y/N)?:").strip().lower()
        if remove == "y":
            known_user.remove(name)
        elif remove == "n":
            print("AWW..I DON'T WANT TO LEAVE YOU EITHER!")

    else:
        print("HMM....... I YOU ARE NOT INTO MY MEMORY {}.".format(name))
        add = input("WOULD YOU LIKE TO BE ADDED TO MY MEMORY(Y/N)?:").strip().lower()

        if add == "y":
            known_user.append(name)
            print(known_user)
        elif add == "n":
            print("OKAY....LIKE I CARE!")
