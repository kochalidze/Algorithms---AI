# 1. მოცემული 3 მთელი a, b, c ̸= 0 რიცხვებისთვის მოძებნეთ a და
# b რიცხვებს შორის მოხვედრილი c რიცხვის ჯერადი რიცხვების
# რაოდენობა ყველა შესაძლო ვარიანტისთვის. თუ რომელიმე
# a, b-დან ჯერადია c-ს, მაშინ ჩათვალეთ შესაბამისი საზღვარი.
# მოიფიქრეთ ამოცანის ამოხსნის ალგორითმი, დაწერეთ და გაუშვით პროგრამა 
# ციკლის და რეკურსიის (აგრეთვე range) კონსტრუქციის გამოყენების გარეშე.


def nums(a,b,c):
    for i in range(a,b):
        print(i % c == 0)

nums(10, 20, 5)