"""
PARTNER file

"""
def encoder(password):
    encoded_password = ""
    for i in range(len(password)):
        temp = int(password[i])
        temp += 3
        encoded_password += str(temp)[-1]
    return encoded_password

def decoder(encoded_password):
    decoded_password = ""
    for i in range(len(encoded_password)):
        temp = int(encoded_password[i])
        if temp <3:
            temp = temp+10-3
        else:
            temp -= 3
        decoded_password += str(abs(temp))
    return decoded_password


if __name__ == "__main__":
    # print(encoder("00009962"))
    # print(decoder("33332295"))
    # print(encoder("12345555"))
    # print(decoder("45678888"))
    encoded_password = ""

    while True:
        print("Menu Menu,\n-------------,\n1. Encode,\n2. Decode,\n3. Quit")
        option = int(input("Please enter an option:"))
        if option == 1:
            password= input("Please enter your password to encode:")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!")

        elif option == 2:
            password_after_decoded = decoder(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {password_after_decoded}.")

        else:
            break

        #change something