def to_roman_numeral(roman_numeral):
    decimal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    
    numero = ''
    
    i = 0
    
    while roman_numeral > 0:
        for _ in range(roman_numeral//decimal[i]):
            numero += roman[i]
            roman_numeral -= decimal[i]
        i += 1
    return numero