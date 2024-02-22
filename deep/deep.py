def check_great_question_answer(answer):


    return_answer = answer.lower() # Convert to lower case

    if return_answer == "42" or "forty-two" in return_answer or "forty two" in return_answer:
        return "Yes"
    else:
        return "No"


def main():

    user_answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

    # Check the user's answer
    result = check_great_question_answer(user_answer)
    print(result)


# Run
main()
