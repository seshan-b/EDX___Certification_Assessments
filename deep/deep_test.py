def check_great_question_answer(answer):
    # Convert the answer to lowercase for case-insensitive comparison
    answer_lower = answer.lower()

    # Check if the answer is one of the accepted forms (42, forty-two, forty two)
    if answer_lower == "42" or "forty-two" in answer_lower or "forty two" in answer_lower:
        return "Yes"
    else:
        return "No"



def main():
    # Prompt the user for the answer to the Great Question
    user_answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

    # Check the user's answer and display the result
    result = check_great_question_answer(user_answer)
    print(f"Is the answer correct? {result}")



if __name__ == "__main__":
    main()
