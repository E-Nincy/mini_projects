import requests

location = input("Where are you playing from? ")
url = f"https://wttr.in/{location}?format=j1"
response = requests.get(url)
data = response.json()

desc = data["current_condition"][0]["weatherDesc"][0]["value"]
temp = data["current_condition"][0]["temp_C"]

print(f"The weather in {location}: {desc}, {temp}°C")

if "rain" in desc.lower():
    print("☔ It's raining. Your steps are heavy and your sword is slippery.")
elif "snow" in desc.lower():
    print("❄️ Snow falls quietly. Movement is slowed and visibility is poor.")
elif "sun" in desc.lower() or "clear" in desc.lower():
    print("☀️ The sun fuels your strength. You're energized!")
elif "storm" in desc.lower() or "thunder" in desc.lower():
    print("⚡ A storm rages. You sense danger in the air.")
else:
    print("🌫️ The weather is odd and uncertain. Be cautious.")

