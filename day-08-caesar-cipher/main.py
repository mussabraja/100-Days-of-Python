import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text,shift_amount):
    if direction == 'encode':
        cipher_text = ''
        for letters in original_text:
            if letters in alphabet:
                index = alphabet.index(letters)
                new_index = index + shift_amount
                new_index = new_index % 26
                cipher_alphabet = alphabet[new_index]
                cipher_text += cipher_alphabet
            else:
                cipher_text += letters
        print(cipher_text)
    elif direction == 'decode':
        decipher_text = ''
        for letters in original_text:
            if letters in alphabet:
                index = alphabet.index(letters)
                reverse_index = (-1) * shift_amount
                index = (index + reverse_index) % 26
                decipher_alphabet = alphabet[index]
                decipher_text += decipher_alphabet
            else:
                decipher_text += letters
        print(decipher_text)

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift)

    restart = input("Do you want to continue? Yes or No ").lower()

    if restart == "no":
        should_continue = False
        print("GoodBye!")





