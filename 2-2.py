# Задача на находение следующей даты при указанной в днях разнице
# import datetime
#
# year, month, day = map(int, input(). split())
# x = datetime.date(year, month, day)
# # print(year)
# # print(month)
# # print(day)
# # print(x)
# days = int(input())
# # print(days)
# y = x + datetime.timedelta(days)
# print(str(y.year) + ' ' + str(y.month) + ' ' + str(y.day))


# Расшифровывание файла

import simplecrypt

namei = 1

with open("encrypted.bin", "rb") as inp:
    ciphertext = inp.read()
    ciphertext.strip()
    print(ciphertext)
    with open("passwords.txt", "r") as pasf:
        for line in pasf:
            print(line.strip())
            nameii = str(namei)
            with open(nameii, "w") as out:
                try:
                    plaintext = simplecrypt.decrypt(line.strip(), ciphertext).decode('utf8')
                    out.write(str(plaintext))
                    print(plaintext)
                except(simplecrypt.DecryptionException):
                    pass
            namei = namei + 1
