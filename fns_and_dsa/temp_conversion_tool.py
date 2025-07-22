FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) *FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32

temp_value = int(input("Enter the temperature to convert: "))
temp_choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
if temp_choice == 'f':
    fahrenheit = temp_value
    print(f"{fahrenheit} °F is {convert_to_celsius(fahrenheit)} °C")
elif temp_choice == 'c':
    celsius = temp_value
    print(f"{celsius} °C is {convert_to_fahrenheit(celsius)} °F")
else:
    print("Invalid temperature. Please enter a numeric value. ")