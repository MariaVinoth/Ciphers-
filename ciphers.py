import string

ceasar = '1'
vigenere = '2'
transp_ciph = '3'
encrypt = '1'
cipher_text = []
plain_text = []
trans_ciph= []
trans_ciph_result = []


#Ceasar cipher
def ceasar_cipher(inp_string,key,enc_dec):
    c_key = int(key)
    if enc_dec == encrypt:
        decrypt = False
    else:
        decrypt = True

    if decrypt: # for decryption the key value is negated
        c_key = - c_key

    for i in inp_string:
        if i not in alphabets_fwd: # for non-alpahabet elements for ex space,comma,..
            cipher_text.append(i)
        else:
            indx = alphabets_fwd.index(i)
            ciph_indx = indx + c_key
            if ciph_indx >= len(alphabets_fwd):   #if the index greater than 26(no.of alpahbets) then start reading from first
                ciph_indx = ciph_indx - len(alphabets_fwd)
            cipher_text.append(alphabets_fwd[ciph_indx])

    cipher_string = ''.join(cipher_text)
    print(cipher_string)

#Vigenere Cipher Encryption
def vig_encryp(v_key):
    for i in range(str_length):
        pt_indx = alphabets_fwd.index(inp_string[i])
        k_indx = alphabets_fwd.index(v_key[i])
        ciph_indx = (pt_indx + k_indx) #get the index of both the characters of key and text compute the cipher index
        if ciph_indx > len(alphabets_fwd):
            ciph_indx = ciph_indx - len(alphabets_fwd)
        cipher_text.append(alphabets_fwd[ciph_indx])

    cipher_string = ''.join(cipher_text)
    print(cipher_string)

#Vigenere Cipher Decryption
def vig_decryp(v_key):
    for i in range(str_length):
        ct_indx = alphabets_fwd.index(inp_string[i])
        k_indx = alphabets_fwd.index(v_key[i])
        plain_indx = (ct_indx - k_indx) #get the index of both the characters of key and text compute the cipher index
        plain_text.append(alphabets_fwd[plain_indx])

    plain_string = ''.join(plain_text)
    print(plain_string)

#Transpositional Cipher Encryption
def transp_encryp(trans_inp_str,trans_key,inp_str_leng):
    temp_str = []
    n = 0

    #to get the count for splitting the string ex 6rows 5 columns, 5rows 5 columns
    if remainder != 0:
        item_cont_len = (inp_str_leng // max(trans_key)) + 1
    else:
        item_cont_len = max(trans_key)

    for i in range(max(trans_key)):
        a = n
        for j in range(item_cont_len):
            temp_str.append(trans_inp_str[a])
            a += max(trans_key) #next element's index
        trans_ciph.append(temp_str)
        temp_str = []
        n += 1

    #Arranging the list as per the key
    for i in range(len(trans_key)):
        ind = trans_key[i] - 1
        for j in range(item_cont_len):
            trans_ciph_result.append(trans_ciph[ind][j])

    trans_cipher_string = ''.join(trans_ciph_result)

    trans_cipher_string = str.replace(trans_cipher_string, ' ', '%')
    print(trans_cipher_string)

#Transpositional Cipher Decryption
def transp_decryp(trans_inp_str,trans_key,inp_str_leng):
    rearanged_list = []
    temp_str = []
    count = 0

    # to get the count for splitting the string ex 6rows 5 columns, 5rows 5 columns
    split = (inp_str_leng // max(trans_key))

    #split and get the characters in the list
    for i in trans_inp_str:
        if count < (split-1):
            temp_str.append(i)
            count += 1
        else:
            temp_str.append(i)
            trans_ciph.append(temp_str)
            temp_str = []
            count = 0

    # Arranging the list as per the key
    for i in range(len(trans_key)):
        ind = trans_key.index(i + 1)
        rearanged_list.append(trans_ciph[ind])

    item_cont_len = len(trans_ciph[0])

    #getting back the plain text
    for i in range(item_cont_len):
        for j in range(len(rearanged_list)):
            trans_ciph_result.append(rearanged_list[j][i])

    trans_decipher_string = ''.join(trans_ciph_result)

    trans_decipher_string = str.replace(trans_decipher_string, '%', ' ')
    print(trans_decipher_string)


#main portion - get the input from the user and call the respective function

print("Pick a method to encrypt/decrypt your input: \n 1.Ceasar Cipher \n 2.Vigenere Cipher \n 3.Transposition Cipher")
cipher_method = input()
inp_string = input("Enter the input text:").lower()
key = input("Enter the key:")
print("Pick the operation: \n 1.Encrypt \n 2.Decrypt")
enc_dec = input()

alphabets_fwd = list(string.ascii_lowercase)

if cipher_method == ceasar:
    ceasar_cipher(inp_string, key, enc_dec)

elif cipher_method == vigenere:
    v_key = list(key)
    if len(inp_string) > len(v_key):
        difference = len(inp_string) - len(v_key)
        for i in range(difference):
            v_key.append(v_key[i])
    str_length = len(inp_string)
    if enc_dec == encrypt:
        vig_encryp(v_key)
    else:
        vig_decryp(v_key)

elif cipher_method == transp_ciph:
    global temp_str
    temp_str = []
    trans_key = key
    trans_inp_str = inp_string
    trans_key = trans_key.split(',')
    trans_key = [int(i) for i in trans_key]
    inp_str_leng = len(trans_inp_str)
    remainder = inp_str_leng % max(trans_key)
    if remainder != 0:
        for i in range(max(trans_key) - remainder):
            trans_inp_str += '%'
    if enc_dec == encrypt:
        transp_encryp(trans_inp_str,trans_key,inp_str_leng)
    else:
        transp_decryp(trans_inp_str,trans_key,inp_str_leng)
