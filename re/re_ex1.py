import re

text = "+375295170293 fghjserg  sg seh erg vov_an@tut.by tyjktr hrgrtty ghrhtyjt rthtjkktrjeh rtgrgtkjyukyuhde " \
       "+375295170293 drthtrj ert srthrsth sdgsd shy56tsko.v@gm.ail.com"

tel_pattern = r"\B\+\d{10,12}\b"
tel = re.findall(tel_pattern, text)
print(tel)

e_mail_pattern = r"\b([a-zA-Z][\w._]+@[\w._]+[.][\w]+)\b"
email = re.findall(e_mail_pattern, text)
print(email)
