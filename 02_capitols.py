def main():
    capitols = open("./capitols.txt", "r")
    State_to_Capitol = {}
    Capitol_to_State = {}

    for line in capitols:
        temp = []
        temp = line.split(",")
        State_to_Capitol[temp[0].lower()] = temp[1]
        Capitol_to_State[temp[1].lower()] = temp[0]

    condition = True
    while condition:
        user_input = input("Ready: ").lower()

        if user_input == "done":
            condition = False
        else:
            match_found = False
            for item in State_to_Capitol:
                if item == user_input:
                    print (State_to_Capitol[item])
                    match_found = True
            if not(match_found): 
                for item in Capitol_to_State:
                    if item == user_input:
                        print (Capitol_to_State[item])
            if not(match_found):
                print("nil")
    capitols.close()
main()