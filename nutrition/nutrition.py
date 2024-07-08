### Breaking down the problem
# Use a conditional with 20 Boolean expressions
# One for each fruit,
# Use a dict to associate a fruit with its calories!
# If k is a str and d is a dict, you can check whether k is a key in d with code like:
# Eg: if k in d:



# 1. Initialize a dictionary called `fruit_calories` with fruit names as keys and their calorie counts as values.
def initialize_fruit_calories():
    fruit_calories = {
        'apple': 52,
        'banana': 89,
        'cherry': 50,
        'date': 282,
        'elderberry': 73,
        'fig': 74,
        'grape': 67,
        'honeydew': 36,
        'kiwi': 61,
        'lemon': 29,
        'mango': 60,
        'nectarine': 44,
        'orange': 47,
        'papaya': 43,
        'quince': 57,
        'raspberry': 52,
        'strawberry': 32,
        'tangerine': 53,
        'ugli fruit': 47,
        'watermelon': 30
    }
    return fruit_calories

# 2. Create a list called `fruits` containing the names of the fruits to check.
def check_fruit_calories(fruit_calories, fruits):
# 3. Loop through each fruit in the `fruits` list:



    for fruit in fruits:
        #    a. Check if the fruit is in the `fruit_calories` dictionary.
        if fruit in fruit_calories:
        #    b. If the fruit is in the dictionary, print the fruit and its calorie count.
            print(f"fruit: {fruit}, calories: {fruit_calories[fruit]}")
        else:
        #    c. If the fruit is not in the dictionary, print that the fruit is not found.
            print(f"fruit: {fruit} is not found")





# 4. Prompt the user for Item Which fruit
def main():
    fruit_calories = initialize_fruit_calories()
    check_fruit_calories(fruit_calories)

    while True:
        user_fruit = input("Which fruit would you like to check? (or type 'exit' to quit): ").lower()
        if user_fruit == 'exit':
            break
        elif user_fruit in fruit_calories:
            print(fruit_calories[user_fruit]")
        else:
            print(f"Sorry, we don't have calorie information for {user_fruit}.")

if __name__ == "__main__":
    main()
