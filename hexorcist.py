#Init
#Our lookup table
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import random

def to_decimal(number_string, original_base):
    #Validate the base
    if not (2 <= original_base <= 36):
        raise ValueError("original_base must be between 2 and 36")
    s = str(number_string).strip().upper()
    total_value = 0
    power = 0
    for ch in s[::-1]:
        if ch not in digits:
            #Invalid character
            raise ValueError(f"Invalid character '{ch}' for base conversion")
        char_value = digits.index(ch)
        if char_value >= original_base:
            #Invalid digit for the base
            raise ValueError(f"Digit '{ch}' not valid for base {original_base}")
        total_value += char_value * (original_base ** power)
        power += 1
    return total_value


def from_decimal(decimal_number, target_base):
    #Validate the base
    if not (2 <= target_base <= 36):
        raise ValueError("target_base must be between 2 and 36")
    n = int(decimal_number)
    if n == 0:
        #Edge case for zero
        return "0"
    result_string = ""
    while n > 0:
        #Get the remainder
        remainder = n % target_base
        n = n // target_base
        char_to_add = digits[remainder]
        result_string = char_to_add + result_string
    return result_string


if __name__ == "__main__":
    #Greet the user
    print("Welcome to The Hexorcist™\n")
    item=random.randint(0, 4)
    startup_items=["The Power of Math Compels you!", "Whatdoyouwant?","You're looking for a number!", "Why are you using a dedicated base converter? This isn't the 1960s","Let's do base conversions!"]
    print(startup_items[item])
    number_input = input("Enter the number you want to convert: ").strip()
    try:
        original_base = int(input("Enter the number's CURRENT base (2-36): ").strip())
        target_base = int(input("Enter the NEW base you want (2-36): ").strip())
    except ValueError:
        #If the input is not an integer, we'll catch the exception and exit
        print("Base values must be integers.")
        raise SystemExit(1)

    try:
        decimal_value = to_decimal(number_input, original_base)
        converted = from_decimal(decimal_value, target_base)
    except ValueError as e:
        print(str(e))
        raise SystemExit(1)

    print(f"'{number_input.upper()}' (Base-{original_base}) is '{converted}' (Base-{target_base}).")
    
