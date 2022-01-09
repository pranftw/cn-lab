import math

def hex2bin(hex_word):
    bin_val = []
    for i in range(len(hex_word)):
        try:
            bin_val+=dec2bin(int(hex_word[i]))
        except:
            bin_val+=dec2bin(10+ord(hex_word[i]) - ord('A'))
    return bin_val

def new_bin(bin_len):
    bin_val = []
    for _ in range(bin_len):
        bin_val.append(0)
    return bin_val

def dec2bin(dec_val):
    bin_val = []
    while(dec_val!=1 and dec_val!=0):
        bin_val = [dec_val%2] + bin_val
        dec_val = int(dec_val / 2)
    if(dec_val==1):
        bin_val = [1] + bin_val
    return pad_zeros(bin_val)

def pad_zeros(bin_val):
    padded_val = new_bin(4-len(bin_val)) + bin_val
    return padded_val

def str2bin(word):
    bin_rep = new_bin(len(word))
    for i in range(len(word)):
        bin_rep[i] = int(word[i])
    return bin_rep

def bit_multiply(bin_val, bit):
    multiplied = []
    for i in range(len(bin_val)):
        if bin_val[i]==bit:
            multiplied.append(bin_val[i])
        else:
            multiplied.append(0)
    return multiplied

def validate_word(word):
    validation = True
    for i in range(len(word)):
        try:
            if int(word[i]) not in [0,1]:
                validation = False
                break
        except:
            validation = False
            break
    return validation

def xor(word1, word2):
    xord = new_bin(len(word1))
    for i in range(len(word1)):
        if word1[i]==word2[i]:
            xord[i] = 0
        else:
            xord[i] = 1
    return xord

def sum(word):
    sum = 0
    for i in range(len(word)):
        sum+=word[i]
    return sum

def divide(codeword, polynomial):
    start_idx = 0
    quotient = []
    remainder = codeword[start_idx:start_idx+len(polynomial)-1]
    start_idx+=len(remainder)
    while(start_idx+1<=len(codeword)):
        remainder.append(codeword[start_idx])
        if remainder[0]==1:
            quotient.append(1)
        else:
            quotient.append(0)
        remainder = xor(remainder, bit_multiply(polynomial, quotient[-1]))
        remainder = remainder[1:]
        start_idx+=1
    return remainder

def check(codeword, polynomial):
    remainder = divide(codeword, polynomial)
    if sum(remainder)==0:
        return True
    return False

if __name__=='__main__':
    # remainder_bits = int(input("Enter the number of bits in remainder: "))
    # dataword = input("Enter the dataword: ")
    # polynomial = input("Enter the polynomial: ")
    remainder_bits = 3
    dataword = "9"
    polynomial = "1011"
    # if not(validate_word(dataword)):
    #     print("Invalid dataword!")
    #     exit()
    # if not(validate_word(polynomial)):
    #     print("Invalid polynomial!")
    #     exit()
    # dataword = str2bin(dataword)
    dataword = hex2bin(dataword)
    remainder = new_bin(remainder_bits)
    polynomial = str2bin(polynomial)
    codeword = dataword + remainder
    remainder = divide(codeword, polynomial)
    print(remainder)
    print(check(dataword+remainder, polynomial))

