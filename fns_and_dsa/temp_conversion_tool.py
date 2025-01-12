FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FAHRENHEIT_OFFSET
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR, FAHRENHEIT_OFFSET
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Hmm, that doesn't look like a valid number. Please enter a numeric value for the temperature.")
        return
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()

    if unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(temperature , "°C is " ,result ,"°F")
    elif unit == "F":
        result = convert_to_celsius(temperature)
        print(temperature ,"°F is",result ,"°C")
    else:
        print("Oops! It seems like you entered an invalid unit. Please enter either 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
