import re
import string

#our ciphertext
ciphertext = " ﻿Y adem iecu ev oek mekbt vehwuj je seccudj oekh setu, ie jxyi yi q hucydtuh je we rqsa qdt seccudj uluho iydwbu bydu ed oekh setu. Oek ixekbt ru qrbu je unfbqyd uluho iydwbu bydu ev setu, iydsu oek muhu jxu edu mxe mheju jxyi setu. Y xefu oek tytd'j jho jhqdibqjydw jxyi ro xqdt vyhij, iydsu yj mekbt fherqrbo jqau oek q sekfbu xekhi. Jxyi yi mxqj secfkjuhi qhu veh qdt oek ixekbt jqau qtlqdjqwu ev jxuc.Yv oek tyt jxyi ro xqdt, oek ixekbt husediytuh huteydw yj ruskqiu teydw yj yd ro xqdt yi yduvvysyudjqdt jxqj'i mxo jxyi junj yi ie bedw. Qbie, jxyi qiiywcudj sqbbi veh q icqbb fojxed fhewhqc. Edu mqo ev ieblydw jxyi yi kiydw ijhydw.cqaujhqdi() qdt mxybu yj yi huseccudtut; yj yi dej dusuiiqhybo jxu edbo efjyed oek xqlu. Yv oek tyt kiut cqaujhqdi(), fbuqiu unfbqyd je cu xem yj mehai qdt Y qc ikhu oek xqt je kiu .jhqdibqju qi mubb, ie unfbqyd xem jxqj mehai qi mubb. Edu bqij jxydw, unfbqyd xem oek qssekdjut veh ifusyqb sxqhqsjuhi? iksx qi ',.()?:) [ifqsui], ujs' . Y Xefu oek xqt vkd mehaydw jxyi ekj :)."
plaintext = ""

#regex pattern object we will use for the match function later
pattern = re.compile('[a-zA-Z]')

#Going to try frequency analysis using count of each character that will be stored in this dictionary
#create dictionary of letters from alphabet and set each value to 0
alphabet = dict.fromkeys(string.ascii_lowercase,0)

#loop through our ciphertext
for c in ciphertext:
    #if our pattern matches the current character in ciphertext
    if re.match(pattern, c):
        #increment the value of the key that character corresponds to in the dictionary by 1
        alphabet[c.lower()] += 1

index = 0
#already tried most frequent character
#sort our dictionary and get second most frequently used letter in ciphertext
value = sorted(alphabet.values(), reverse=True)[1]

#loop through key value pairs in our dictionary
for char,num in alphabet.items():
    #compare the value in our dict to value of the second most frequent character we stored earlier
    if num == value:
        #store the index of where the most frequently used character is located in our dictionary
        index = list(alphabet.keys()).index(char)

#get how many indices away from letter e most frequent character is and store it in a variable
shift_amt = index - list(alphabet.keys()).index('e')

#loops through our ciphertext again
for c in ciphertext:
    #pattern match again
    if re.match(pattern, c):
        #append the character in our dictionary minus the shift amount to get the decrypted plaintext
        plaintext += list(alphabet)[list(alphabet).index(c.lower()) - shift_amt]
    else:
        #the above if statement only handles letters so handle all spaces and special characters here by just appending them straight to plaintext
        plaintext += c

print(plaintext)