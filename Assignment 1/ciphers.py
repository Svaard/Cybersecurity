import re
import string

ciphertext = "Y adem iecu ev oek mekbt vehwuj je seccudj oekh setu, ie jxyi yi q hucydtuh je we rqsa qdt seccudj uluho iydwbu bydu ed oekh setu. Oek ixekbt ru qrbu je unfbqyd uluho iydwbu bydu ev setu, iydsu oek muhu jxu edu mxe mheju jxyi setu. Y xefu oek tytd'j jho jhqdibqjydw jxyi ro xqdt vyhij, iydsu yj mekbt fherqrbo jqau oek q sekfbu xekhi. Jxyi yi mxqj secfkjuhi qhu veh qdt oek ixekbt jqau qtlqdjqwu ev jxuc.Yv oek tyt jxyi ro xqdt, oek ixekbt husediytuh huteydw yj ruskqiu teydw yj yd ro xqdt yi yduvvysyudjqdt jxqj'i mxo jxyi junj yi ie bedw. Qbie, jxyi qiiywcudj sqbbi veh q icqbb fojxed fhewhqc. Edu mqo ev ieblydw jxyi yi kiydw ijhydw.cqaujhqdi() qdt mxybu yj yi huseccudtut; yj yi dej dusuiiqhybo jxu edbo efjyed oek xqlu. Yv oek tyt kiut cqaujhqdi(), fbuqiu unfbqyd je cu xem yj mehai qdt Y qc ikhu oek xqt je kiu .jhqdibqju qi mubb, ie unfbqyd xem jxqj mehai qi mubb. Edu bqij jxydw, unfbqyd xem oek qssekdjut veh ifusyqb sxqhqsjuhi? iksx qi ',.()?:) [ifqsui], ujs' . Y Xefu oek xqt vkd mehaydw jxyi ekj :)."
pattern = re.compile('[a-zA-Z]')

#Going to try frequency analysis using count of each character that will be stored in this dictionary
alphabet = dict.fromkeys(string.ascii_lowercase,0)

for c in ciphertext:
    if re.match(pattern, c):
        alphabet[c.lower()] += 1
    else:
        continue

print(alphabet)
