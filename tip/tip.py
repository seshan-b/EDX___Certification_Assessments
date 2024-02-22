def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d[1:]) # Use Python Sub String


def percent_to_float(p):
    return float(p[:-1]) / 100 # Use Python Sub String



main()
