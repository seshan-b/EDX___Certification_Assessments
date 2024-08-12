import random

cards = ["Jack", "Queen", "King"]

def main():
    print(random.choice(cards, weights=[75, 20, 5], k=2))


main()
