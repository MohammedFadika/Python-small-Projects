# Define the Caesar cipher function
def caesar(message, offset):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
    
            encrypted_text += alphabet[new_index]
    
    # Print the original and encrypted messages
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

caesar('Hello Zaira', 3) # offset = 3
caesar('Hello Zaira', 13) # offset = 14
