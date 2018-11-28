# This program reduces and decodes a coded message and determines if it is a palindrome
# Peterson, Courtney


#This program reduces and decodes a coded message and determines if it is a palindrome


print "This program reduces and decodes a coded message and determines if it is a palindrome"

def strip(encoded):
    reduced_encoded = ""
    for position in range(0, len(encoded)):
        if ord(encoded[position]) >= 97 and ord(encoded[position]) <= 122 \
        or ord(encoded[position]) == 32:
            reduced_encoded = reduced_encoded + encoded[position]
    return reduced_encoded


def decode(reduced_encoded, offset):
    decoded = ""
    for letter in range(0, len(reduced_encoded)):
        if ord(reduced_encoded[letter]) == 32:
            decoded = decoded + reduced_encoded[letter]
        else:
            decoded_letter = ord(reduced_encoded[letter]) - offset
            if decoded_letter <= 96:
                decoded_letter = decoded_letter + 26
            decoded = decoded + chr(decoded_letter)
    return decoded

def palin(decoded):
    fwdstring = ""
    for position in range(0, len(decoded)):
        if decoded[position] != " ":
            fwdstring = fwdstring + decoded[position]
    print fwdstring

    revstring = ""
    for position in range(0, len(fwdstring)):
        revstring = fwdstring[position] + revstring
    print revstring

    if revstring == fwdstring:
        return "It is a palindrome"
    else:
        return "It is not a palindrome"


encoded= raw_input("Enter a encoded string: ")

encoded = encoded.lower()
print "the lower case string is: ", encoded

reduced_encoded = strip(encoded)
print "With the specials stripped out of the string is:", reduced_encoded

offset = int(raw_input("Enter Offset: "))

decoded = decode(reduced_encoded, offset)
print "The decoded string is: ", decoded

print palin(decoded)
