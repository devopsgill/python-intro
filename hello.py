#This program takes a function calld Main and ask your name and prints hello

def main():
    name = input("What's your name?")
    hello(name)

def hello(to="world"):
    print("hello,",to)

main()

