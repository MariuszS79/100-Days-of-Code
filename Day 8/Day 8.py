logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
final_message=[]
alphabet=alphabet*1000

def encrypt(message, shift):
    global final_message
    for i in message:
        if i in alphabet:
            order=alphabet.index(i)
            final_message.append(alphabet[order+shift])
    print("Here is your encrypted message: ", *final_message, sep="")
            

def decrypt(message,shift):
    global final_message
    for i in message:
        if i in alphabet:
            order=alphabet.index(i)
            final_message.append(alphabet[order-shift])
    print("Here is your decrypted message: ", *final_message, sep="")

print(logo)
crypt=True
while crypt:
    final_message=[]
    what=str(input("Type 'encode' to encrypt,type 'decode' to decrypt: \n"))
    message=str(input("Type your message: \n"))
    shift=int(input("Type the shift number: \n"))

    if what=="encode":
        encrypt(message, shift)
    else:
        decrypt(message, shift)
    carry_on=input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
    if carry_on=="yes":
        continue
    else:
        print("Goodbye")
        crypt=False
    