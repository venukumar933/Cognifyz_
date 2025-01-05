temp = float(input("Enter the temperature: "))
# Temperature conversion
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()
if unit == 'C':
    # Convert Celsius to Fahrenheit
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {fahrenheit}°F")
elif unit == 'F':
    # Convert Fahrenheit to Celsius
    celsius = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {celsius}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
