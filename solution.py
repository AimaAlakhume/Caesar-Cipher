def caesarCipher(s, k):
    low_alpha = 'abcdefghijklmnopqrstuvwxyz'
    up_alpha = low_alpha.upper()

    encrypted = ''

    for letter in s:
        if letter.isalpha():
            if letter.islower():
                new_ind = low_alpha.find(letter) + k
                if new_ind > 25:
                    multiple_of_26 = (new_ind // 26)*26
                    encrypted += low_alpha[new_ind - multiple_of_26]
                else:
                    encrypted += low_alpha[new_ind]

            else:
                new_ind = up_alpha.find(letter) + k
                if new_ind > 25:
                    multiple_of_26 = (new_ind // 26) * 26
                    encrypted += up_alpha[new_ind - multiple_of_26]
                else:
                    encrypted += up_alpha[new_ind]
        else:
            encrypted += letter

    return encrypted
