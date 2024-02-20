def emotion(emoji):
    # Replace :) with a smiling face emoji
    emoji = text.replace(":)", "😊")

    # Replace :( with a sad face emoji
    emoji = text.replace(":(", "😞")

    return emoji



print(emotion())
