# 1. მოცემული 3 მთელი a, b, c ̸= 0 რიცხვებისთვის მოძებნეთ a და
# b რიცხვებს შორის მოხვედრილი c რიცხვის ჯერადი რიცხვების
# რაოდენობა ყველა შესაძლო ვარიანტისთვის. თუ რომელიმე
# a, b-დან ჯერადია c-ს, მაშინ ჩათვალეთ შესაბამისი საზღვარი.
# მოიფიქრეთ ამოცანის ამოხსნის ალგორითმი, დაწერეთ და გაუშვით პროგრამა 
# ციკლის და რეკურსიის (აგრეთვე range) კონსტრუქციის გამოყენების გარეშე.


def count_multiples(a, b, c, current):
    if current > b:
        return 0
    if current % c == 0:
        return 1 + count_multiples(a, b, c, current + c)
    return count_multiples(a, b, c, current + c)

def find_multiples(a, b, c):
    if a % c == 0:
        first_multiple = a
    else:
        first_multiple = a + (c - a % c)
    
    return count_multiples(a, b, c, first_multiple)

a = int(input("შეიყვანეთ a: "))
b = int(input("შეიყვანეთ b: "))
c = int(input("შეიყვანეთ c: "))

result = find_multiples(a, b, c)
print(f"c-ით ჯერადი რიცხვების რაოდენობა a და b შორის: {result}")
