import random
pass1 =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', '0', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','0', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', '', 'Z', 
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        '!', '@', '#', '$', '%', '^', '&', '*', ')']
# declaring the empty string
password = ""
# loop to generate the random password of the length entered by the iserx in range(16):
for i in range(16):
    password = password + random.choices(pass1)[0]
print(password)

