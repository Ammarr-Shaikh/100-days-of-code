
while True:


    alphabets = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]

    direction = input("Type 'encode' to encrypt or 'decode to decrypt. \n" ).lower()
    text = input("Type your message. \n").lower()
    num = int(input("Type the shift number: "))

    def encrypt(original_text , shift_amount):
        encoded = ""
        maxi = len(alphabets)
        for letter in original_text:
            if letter not in alphabets:
                encoded+=letter
                continue
            huh = (alphabets.index(letter) + shift_amount) % maxi

    
            encoded+=alphabets[huh]
  
        print(encoded)

    def decrypt(original_text , shift_amount):
        decoded = ""
        maxi = len(alphabets)
        for letter in original_text:
            if letter not in alphabets:
                decoded+=letter
                continue
            huh = (alphabets.index(letter) - shift_amount) % maxi

    
            decoded+=alphabets[huh]
  
        print(decoded)

    
    def caesar_cipher():
        if direction == "encode":
            encrypt(text,num)
        elif direction== "decode":
            decrypt(text,num)
        else:
            print("invalid input")

    caesar_cipher()
    ok = input("Type 'yes' if you wanna continue or 'no' to end: ")
    if ok != "yes":
        break