def main():
    capitols = open("./capitols.txt", "r")
    State_to_Capitol = {}
    Capitol_to_State = {}

    for line in capitols:
        temp = []
        temp = line.split(",")
        State_to_Capitol[temp[0].lower()] = temp[1][0:(len(temp[1])-1)]
        Capitol_to_State[temp[1][0:(len(temp[1])-1)].lower()] = temp[0]
        print(State_to_Capitol)
        print(Capitol_to_State)

    condition = True
    while condition:
        user_input = input("Ready: ").lower()

        if user_input == "done":
            condition = False

        else:
            if user_input in State_to_Capitol:
                print(State_to_Capitol[user_input])
                
            elif user_input in Capitol_to_State:
                    print (Capitol_to_State[user_input])
            else:
                print("nil")


    capitols.close()
main()