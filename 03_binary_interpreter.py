#dec to bin
def dec_to_bin():
    #curr = int(input("value:").strip())
    curr = 7

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

            return result


#bin to dec
def bin_to_dec():
    #inp = "10100"
    inp = "1111111001"
    tokens = list(inp)
    tokens = sign(tokens)

    multiplier = 1
    result = 0
    for i in reversed(tokens):
        if(i == 1):
            result = int(result) + int(multiplier)
        multiplier = multiplier * 2

    return result

def sign(binar):
    #Reverse:
    bin_reversed = []
    for token in binar:
        token = int(token)
        if (token == 0):
            bin_reversed.append(1)
        else:
            bin_reversed.append(0)

    #plus 1
    bin_sum = []
    add_one = True
    for token in reversed(bin_reversed):
        value = token
        if(token == 1 and add_one):
            value = 0
        if(token == 0 and add_one):
            value = 1
            add_one = False
            #Careful!! it is possible to have result 1111 and never set add_one to False.
            #that is because we must first check if their is one 0 available.
        
        #don't have to do anything when add_one isn't applicable, because curr is entered
        bin_sum.insert(0, value)

    return bin_sum


print("Decimal  to signed binary:")
print(sign(dec_to_bin()))
print("")
print("Signed binary to Decimal:")
print(bin_to_dec())
