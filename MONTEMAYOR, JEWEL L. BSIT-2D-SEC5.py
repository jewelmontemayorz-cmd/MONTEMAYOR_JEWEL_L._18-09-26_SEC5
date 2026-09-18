import sys
import math
import random
import functools

print = functools.partial(print, flush=True)

# Helper Functions
def get_floats(prompt):
    while True:
        try:
            print(prompt, end=" ", flush=True)
            sys.stdout.flush()
            return float(input())
        except ValueError:
            print("Invalid input. Please type a number (e.g., 6.9).")
        except EOFError:
            print("\n No input received. Exiting program.")
            raise SystemExit

def get_int(prompt):
    while True:
        try:
            print(prompt, end=" ", flush=True)
            sys.stdout.flush()
            return int(input())
        except ValueError:
            print("Invalid input. Please type a number (e.g., 6, 9).")
        except EOFError:
            print("\n No input received. Exiting program.")
            raise SystemExit            

def safe_input(prompt):
    while True:
        try:
            print(prompt, end=" ", flush=True)
            sys.stdout.flush()
            return input()
        except ValueError:
            print("Invalid input. Please type a number (e.g., 6, 9).")
        except EOFError:
            print("\n No input received. Exiting program.")
            raise SystemExit            

def pause():
    safe_input("\n Press ENTER to return to the menu....")

def print_header(title):
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)

# SECTION 1: Trigonometric Functions
def trig_menu():
    while True:
        print_header("Trigo Functions")
        print("""1. Show values of pi
2. Convert degrees->radians
3. Convert radians->degrees
4. Compute sin, cos, tan of any angle
5. Compute asin, acos, atan of a value (-1 to 1 for asin/cos)
0. Back to the Menu
""")
        choice = safe_input("Enter your Choice: ").strip()

        if choice == "1":
            print(f"\nmath.pi = {math.pi}")
        elif choice == "2":
            deg = get_floats("Enter an angle in degrees: ")
            rad = math.radians(deg)
            print(f"\n{deg} degrees = {rad} radians")
        elif choice == "3":
            rad = get_floats("Enter an angle in radians: ")
            deg = math.degrees(rad)
            print(f"\n{rad} radians = {deg} degrees")    
        elif choice == "4":
            deg = get_floats("Enter an angle in degrees: ")
            rad = math.radians(deg)
            print(f"\nAngle = {deg} degrees ({rad} radians)")
            print(f"sin({deg}) = {math.sin(rad)}")
            print(f"cos({deg}) = {math.cos(rad)}")
            print(f"tan({deg}) = {math.tan(rad)}") 
        elif choice == "5":
            val = get_floats("Enter Value: ")
            print()
            try:
                print(f"asin({val}) = {math.asin(val)} radians ({math.degrees(math.asin(val))} degrees)")
            except ValueError:
                print("asin(x) needs -1 <= x <= 1. Skipped.")
            try:
                print(f"acos({val}) = {math.acos(val)} radians ({math.degrees(math.acos(val))} degrees)")            
            except ValueError:
                print("acos(x) needs -1 <= x <= 1. Skipped.")
            try:
                print(f"atan({val}) = {math.atan(val)} radians ({math.degrees(math.atan(val))} degrees)")
            except ValueError:
                print("atan error.")
        elif choice == "0":
            break
        else:
            print("\nInvalid choice.")
        
        pause()

# SECTION 2: Hyperbolic Functions
def hyper_menu():
    while True:
        print_header("Hyperbolic Functions")
        print("""1. Compute sinh, cosh, tanh of a value
2. Compute asinh, acosh, atanh of a value
0. Back to the Menu
""")
        choice = safe_input("Enter your Choice: ").strip()

        if choice == "1":
            val = get_floats("Enter a number: ")
            print(f"\nsinh({val}) = {math.sinh(val)}")
            print(f"cosh({val}) = {math.cosh(val)}")
            print(f"tanh({val}) = {math.tanh(val)}")
        elif choice == "2":
            val = get_floats("Enter a number: ")
            print()
            print(f"asinh({val}) = {math.asinh(val)}")
            try:
                print(f"acosh({val}) = {math.acosh(val)}")
            except ValueError:
                print("acosh(x) needs x >= 1. Skipped.")
            try:
                print(f"atanh({val}) = {math.atanh(val)}")
            except ValueError:
                print("atanh(x) needs -1 < x < 1. Skipped.")
        elif choice == "0":
            break
        else:
            print("\nInvalid choice.")

        pause()

# SECTION 3: Exponentiation and Logarithms Functions
def exponent_menu():
    while True:
        print_header("EXPONENTIATION AND LOGARITHMS FUNCTIONS")
        print("""1. Show the value of e
2. Compute exp(x)
3. Compute the natural log, log10, and log2 of a value
4. Compute log(x, base) with a custom base
5. Compute pow(x, y) - built-in vs math.pow
0. Back to Main Menu
""")
        choice = safe_input("Enter your choice: ").strip()

        if choice == "1":
            print(f"\nmath.e = {math.e}")
        elif choice == "2":
            x = get_floats("Enter x: ")
            print(f"\nexp({x}) = e^{x} = {math.exp(x)}")
        elif choice == "3":
            x = get_floats("Enter a positive number x: ")
            try:
                print(f"\nlog({x}) = {math.log(x)}")
                print(f"log10({x}) = {math.log10(x)}")
                print(f"log2({x}) = {math.log2(x)}")
            except ValueError:
                print("Logarithms require x > 0. Please try again.")
        elif choice == "4":
            x = get_floats("Enter x (must be > 0): ")
            b = get_floats("Enter the base b (must be > 0 and != 1): ")
            try:
                print(f"\nlog({x}, base {b}) = {math.log(x, b)}")
            except (ValueError, ZeroDivisionError):
                print("Invalid input for a logarithm with that base.")
        elif choice == "5":
            x = get_floats("Enter the base x: ")
            y = get_floats("Enter the exponent y: ")
            print(f"\nBuilt-in pow({x}, {y}) = {pow(x, y)}")
            print(f"math.pow({x}, {y}) = {math.pow(x, y)}")
            print("(Note: pow() can return an int for integer inputs; math.pow() always returns a float.)")
        elif choice == "0":
            break
        else:
            print("\nInvalid choice.")

        pause()

# SECTION 4: General-Purpose Math Functions
def general_math_menu():
    while True:
        print_header("GENERAL-PURPOSE MATH FUNCTIONS")
        print("""1. Compute ceil, floor, and trunc of a value
2. Compute a factorial
3. Compute the hypotenuse of a right triangle
0. Back to Main Menu
""")
        choice = safe_input("Enter your choice: ").strip()

        if choice == "1":
            val = get_floats("Enter a floating-point number: ")
            print(f"\nmath.ceil({val}) = {math.ceil(val)}")
            print(f"math.floor({val}) = {math.floor(val)}")
            print(f"math.trunc({val}) = {math.trunc(val)}")
        elif choice == "2":
            val = get_int("Enter a non-negative integer: ")
            try:
                print(f"\n{val}! = {math.factorial(val)}")
            except ValueError:
                print("Factorial requires a non-negative integer.")
        elif choice == "3":
            a = get_floats("Enter side a: ")
            b = get_floats("Enter side b: ")
            print(f"\nHypotenuse math.hypot({a}, {b}) = {math.hypot(a, b)}")
        elif choice == "0":
            break
        else:
            print("\nInvalid choice.")

        pause()

# SECTION 5: The Random Module
def random_menu():
    sample_items = ["Apple", "Banana", "Cherry", "Dragonfruit", "Elderberry", "Fig", "Grape"]

    while True:
        print_header("THE RANDOM MODULE")
        print("""1. Set a seed (so results can be repeated)
2. Generate a number with randrange()
3. Generate a number with randint()
4. Pick a random item from a list with choice()
5. Draw several UNIQUE items from a list with sample() (like a lottery)
0. Back to Main Menu
""")
        choice = safe_input("Enter your choice: ").strip()

        if choice == "1":
            seed_val = get_int("Enter an integer seed value: ")
            random.seed(seed_val)
            print(f"\nRandom seed has been set to {seed_val}.")
        elif choice == "2":
            start = get_int("Enter start value: ")
            stop = get_int("Enter stop value (exclusive): ")
            step = get_int("Enter step value: ")
            try:
                res = random.randrange(start, stop, step)
                print(f"\nrandom.randrange({start}, {stop}, {step}) = {res}")
            except ValueError:
                print("Invalid range parameters for randrange().")
        elif choice == "3":
            a = get_int("Enter lower bound (a): ")
            b = get_int("Enter upper bound (b, inclusive): ")
            try:
                res = random.randint(a, b)
                print(f"\nrandom.randint({a}, {b}) = {res}")
            except ValueError:
                print("Lower bound cannot be greater than upper bound.")
        elif choice == "4":
            print(f"\nCurrent list of items: {sample_items}")
            res = random.choice(sample_items)
            print(f"random.choice() picked: {res}")
        elif choice == "5":
            print(f"\nCurrent list of items: {sample_items}")
            k = get_int(f"Enter number of items to pick (1-{len(sample_items)}): ")
            try:
                res = random.sample(sample_items, k)
                print(f"random.sample() selected: {res}")
            except ValueError:
                print(f"Sample size must be between 1 and {len(sample_items)}.")
        elif choice == "0":
            break
        else:
            print("\nInvalid choice.")

        pause()

# MAIN MENU
def main():
    while True:
        print_header("MAIN MENU")
        print("""1. Trigonometric Functions
2. Hyperbolic Functions
3. Exponentiation and Logarithms Functions
4. General-Purpose Math Functions
5. The Random Module
0. Exit Program
""")
        choice = safe_input("Enter your choice: ").strip()

        if choice == "1":
            trig_menu()
        elif choice == "2":
            hyper_menu()
        elif choice == "3":
            exponent_menu()
        elif choice == "4":
            general_math_menu()
        elif choice == "5":
            random_menu()
        elif choice == "0":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
