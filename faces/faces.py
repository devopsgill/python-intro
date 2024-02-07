#This turns prompts the user and turns an emoitcon string into an emoji by calling a function
def main():
    text = input("Write Here: ")
    convert(text)
    
#This is the function that converts the string into an emoji
def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    print(text)


main()