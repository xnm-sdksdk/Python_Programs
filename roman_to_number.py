    
values = {    
    'M':1000,
    'CM':900,
    'D':500,
    'CD':400,
    'C':100,
    'XC':90,
    'L':50,
    'XL':40,
    'X':10,
    'IX':9,
    'V':5,
    'IV':4,
    'I':1,
}
    

def from_roman_numeral(roman_num):
    sum = 0
    for i in range (len(roman_num) -1):
        letter = roman_num[i]
        number = roman_num[i + 1]
        if values[letter] < values[number]:
            sum -= values[letter]
        else:
            sum += values[letter]
    sum += values[roman_num[-1]]
    return sum