#Chinese Zodiac Calculator  

birth_year = input("Enter your birth year: ")  

try:  
    birth_year = int(birth_year)  
except ValueError:
    print("Invalid input! Please enter a whole number.")  
    exit()

if birth_year < 1900:  
    print("Invalid Year, it should not be earlier than 1900.")  
    exit()

zodiac_signs = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]

year_difference = birth_year - 1900
sign_index = year_difference % 12
result = zodiac_signs[sign_index]

print(f"Your Chinese Zodiac Sign is: {result}")

<img width="1408" height="881" alt="ALMAZAN_CS3-Output" src="https://github.com/user-attachments/assets/71a300ec-b0bb-4a00-b69f-445bdedf52fd" />
