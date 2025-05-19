from datetime import date

print("Welcome To The World")
print ("")

def reduce_to_single_digit(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

def get_zodiac_sign(day, month):
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"

def get_chinese_zodiac_full(year):
    animals = [
        "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox",
        "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"
    ]
    elements = ["Wood", "Fire", "Earth", "Metal", "Water"]
    polarities = ["Yang", "Yin"]

    animal = animals[year % 12]
    element = elements[(year % 10) // 2]  # Each element lasts 2 years
    polarity = polarities[year % 2]       # Even = Yang, Odd = Yin

    return f"{polarity} {element} {animal}"

# Main program starts here
name = input("Enter your full name: ")
char_count = len(name.replace(" ", ""))  # ignore spaces
numerology_number = reduce_to_single_digit(char_count)

dob = input("Enter your date of birth (dd/mm/yyyy): ")
day, month, year = map(int, dob.split("/"))
zodiac = get_zodiac_sign(day, month)

today = date.today()
age = today.year - year - ((today.month, today.day) < (month, day))
chinese_zodiac = get_chinese_zodiac_full(year)

print ("")
print(f"Hello, {name}, you are {age} years old.")
print(f"Your name has {char_count} characters.")
print(f"Your full name numerology is: {numerology_number}")
print(f"Your Zodiac sign is: {zodiac}")
print(f"Your Chinese Zodiac sign is: {chinese_zodiac}")
