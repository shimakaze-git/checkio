import re


# def checkio(data):
#     import re
#     if len(data)<10:
#         return False
#     if not re.search('[0-9]', data):
#         return False
#     if not re.search('[a-z]', data):
#         return False
#     if not re.search('[A-Z]', data):
#         return False
#     return True


def checkio(data: str) -> bool:
    if 10 <= len(data) <= 64:
        return True if re.match(r'((?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{10,})', data) else False
    else:
        return False

if __name__ is '__main__':

    assert checkio('A1213pokl') is False, "1st example"
    assert checkio('bAse730onE4') is True, "2nd example"
    assert checkio('asasasasasasasaas') is False, "3rd example"
    assert checkio('QWERTYqwerty') is False, "4th example"
    assert checkio('123456123456') is False, "5th example"
    assert checkio('QwErTy911poqqqq') is True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
