import requests

name = input("Enter your name: ")
length = len(name)

if 4 <= length <= 40:
    url = f"https://uzby.com/api.php?min={length}&max={length}"
    try:
        new_name = requests.get(url).text.strip()
        print(f"Your in-game name is: {new_name}")
    except:
        print("Something went wrong generating your name.")
else:
    print("Name must be between 4 and 40 characters.")

