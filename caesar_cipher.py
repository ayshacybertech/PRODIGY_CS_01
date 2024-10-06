# Caesar Cipher Encryption and Decryption

# Function to encrypt the message
def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char
    return encrypted_message

# Function to decrypt the message
def decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_message += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_message += char
    return decrypted_message

# Main program
def main():
    print("Caesar Cipher Program")
    choice = input("Would you like to (e)ncrypt or (d)ecrypt a message? ").lower()

    if choice == 'e':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        print("Encrypted Message: ", encrypt(message, shift))

    elif choice == 'd':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        print("Decrypted Message: ", decrypt(message, shift))

    else:
        print("Invalid choice! Please choose 'e' for encrypt or 'd' for decrypt.")

if __name__ == "__main__":
    main()
