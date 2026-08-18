#Chinese Zodiac Calculator

#To get user's input  
birth_year = input("Enter your birth year: ")  

#To validate user's input  
try:  
  birth_year = int(birth_year)  
except ValueError:  
  print("Invalid input! Please enter a whole number.")  
  exit()  

if birth_year < 1900:  
  print("Invalid Year, it should not be earlier than 1900.")  
  exit()  

#To define zodiac order  
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
  "Pig (猪 / Zhū)",  
]  

#To calculate index  
year_difference = birth_year - 1900  
sign_index = year_difference % 12  
result = zodiac_signs[sign_index]  

#To get output  
print(f"Your Chinese Zodiac Sign is: {result}") 

<img width="1408" height="881" alt="ALMAZAN_CS3-Output" src="https://github.com/user-attachments/assets/633f2bef-7865-4e49-83e3-40aac43f0bdd" />
