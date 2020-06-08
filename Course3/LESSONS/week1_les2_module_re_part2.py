import re

nicknames = ['sjdhfih123', 'ffweiufhe_efww2', 'erieri@!_323', 'Йiruiu123123', '213123123(']
reg = re.compile(r'^\w+$', re.ASCII)
for nick in nicknames:
    valid = 'not '
    if reg.match(nick):
        valid = ''
    print(f'Nickname: {nick} is {valid}valid')

def find_all_digits(text):
    exp = r'\d+'
    return re.findall(exp, text)

print(find_all_digits('a123b45с6d'))