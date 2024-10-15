abc = "абвгдеёжзийклмнопрстуфхцчщъыьэюя1234567890qwertyuiopasdfghjklzxcvbnmАБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧЩЪЫЬЭЮЯQWERTYUIOPASDFGHJKLZXCVBNM!*/-+@#%$№ ."
abc_arr, new_arr = list(abc), list(abc)

import window.cwin_1
import linecache

def GenerateKey(ip, port):

    import random
    for i in new_arr * random.randint(5, 15):
        elemein_1 = int(random.randint(0, 136))
        elemein_2 = int(random.randint(0, 136))

        new_arr[elemein_1], new_arr[elemein_2] = new_arr[elemein_2], new_arr[elemein_1]
    key = ""

    for i in new_arr:
        key = f'{key}{i}'

    file1 = open('YourProfile.txt', 'w')
    print(str(key))
    file1.write(str(key))
    file1.close()

    file2 = open('UIProfile.txt', 'w')
    file2.write('')
    file2.close()

    file3 = open('UIProfile.txt', 'a')
    file3.write(f'{ip}IOIOI')
    file3.write(f'{port}IOIOI')
    file3.write(f'{key}')
    file3.close()

    return key

def EnCode(text):
    file = open('UIProfile.txt')
    content = file.readlines()
    file.close()
    content = str(content)
    content = content.strip("['").split('IOIOI')
    key = content[2]
    Cyp = ''
    text_Cyp = list(text)
    for i in text_Cyp:
        for sim in abc_arr:
            if i == sim:
                index = abc_arr.index(sim)
                Cyp = f'{Cyp}{key[index]}'
    return Cyp
    # return cyp

def DeCode(text):
    DeCyp = ''
    file = open('YourProfile.txt')
    line = file.readlines()
    key = list(line[0])
    file.close()
    text = list(text)
    for i in text:
        for sim in key:
            if i == sim:
                index = key.index(i)
                DeCyp = f'{DeCyp}{abc_arr[index]}'

    return DeCyp
