#dec to bin
def dec_to_bin():
    curr = int(input("value:").strip())

    result = []
    while(True):       
        if(curr % 2 == 0):
            result.insert(0, 0)
        else:
            result.insert(0, 1)
            
        curr = int(curr/2)

        if(curr == 0):
            r = range(10 - len(result))
            for i in r:
                result.insert(0, 0)

            print(result)
            break


#bin to dec
def bin_to_dec():
    inp = "10100"
    tokens = list(inp)
    multiplier = 1
    result = 0
    for i in tokens:
        if(i == '1'):
            result = result + multiplier
        multiplier = multiplier * 2

    print(result)
