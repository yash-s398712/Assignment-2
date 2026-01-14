# Question 1 – File Encryption and Decryption

def decrypt_char(ch, shift1, shift2):
    if ch.islower():
        pos = ord(ch) - ord('a')

        # possible original from a–m rule
        candidate1 = (pos - (shift1 * shift2)) % 26
        orig1 = chr(candidate1 + ord('a'))

        # possible original from n–z rule
        candidate2 = (pos + (shift1 + shift2)) % 26
        orig2 = chr(candidate2 + ord('a'))

        # choose the one that encrypts back correctly
        if encrypt_char(orig1, shift1, shift2) == ch:
            return orig1
        else:
            return orig2

    elif ch.isupper():
        pos = ord(ch) - ord('A')

        # possible original from A–M rule
        candidate1 = (pos + shift1) % 26
        orig1 = chr(candidate1 + ord('A'))

        # possible original from N–Z rule
        candidate2 = (pos - (shift2 ** 2)) % 26
        orig2 = chr(candidate2 + ord('A'))

        if encrypt_char(orig1, shift1, shift2) == ch:
            return orig1
        else:
            return orig2

    else:
        return ch

def encrypt_file(shift1, shift2):
    with open("raw_text.txt", "r") as infile, open("encrypted_text.txt", "w") as outfile:
        for line in infile:
            encrypted_line = ""
            for ch in line:
                encrypted_line += encrypt_char(ch, shift1, shift2)
            outfile.write(encrypted_line)


def decrypt_file(shift1, shift2):
    with open("encrypted_text.txt", "r") as infile, open("decrypted_text.txt", "w") as outfile:
        for line in infile:
            decrypted_line = ""
            for ch in line:
                decrypted_line += decrypt_char(ch, shift1, shift2)
            outfile.write(decrypted_line)


def verify_decryption():
    with open("raw_text.txt", "r") as original, open("decrypted_text.txt", "r") as decrypted:
        if original.read() == decrypted.read():
            print("Decryption successful")
        else:
            print("Decryption failed")


def main():
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    encrypt_file(shift1, shift2)
    decrypt_file(shift1, shift2)
    verify_decryption()


main()
