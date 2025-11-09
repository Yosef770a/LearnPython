def secret(letter:str, decipher: bool = False):
    try:
        a_z = list(map(chr, range(ord('a'), ord('z')+1)))
        A_Z = list(map(chr, range(ord('A'), ord('Z')+1)))
        z_a = sorted(list(a_z), reverse=True)
        Z_A = sorted(list(A_Z), reverse=True)
        if letter in a_z:
            if decipher:
                return a_z[z_a.index(letter)]
            else:
                return z_a[a_z.index(letter)]
        else:
            if decipher:
                return A_Z[Z_A.index(letter)]
            else:
                return Z_A[A_Z.index(letter)]
            
    except ValueError:
        return letter

selection_menu = input("For writing enter 1, for reading enter 2: ")

if selection_menu == "1":
    with open("secret.txt", "w") as f:
        message_content = input("Please write your encrypted message: ")
        encrypted_message = []
        message_content = list(message_content)
        for i in message_content:
            # print(i)
            encrypted_message.append(secret(i))
            # print(encrypted_message)

        f.write("".join(encrypted_message))

elif selection_menu == "2":
    decrypted_content = []
    with open("test.txt", "r") as f:
        for i in list(f.read()):
            decrypted_content.append(secret(i, True))
        print("".join(decrypted_content))

        


