def main():
    capitols = open("./capitols.txt", "r")
    array = {}

    for line in capitols:
        temp = []
        temp = line.split(",")
        array[temp[0]] = temp[1]
        
    for i in array:
        print(array[i])
    #print(array)

main()