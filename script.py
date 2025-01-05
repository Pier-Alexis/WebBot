import webbrowser
import time
import os

# Function to clear the command prompt
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Clean the command prompt
clear_console()

# Ask for the URL
url = input("Enter the URL (starting with http or https) : ").strip()
while not url.startswith("http"):
    print("Invalid URL. Retry with a valid one.")
    url = input("Enter the URL again : ").strip()

# Ask for time
try:
    duration = int(input("Time between each URL opening: "))
    if duration < 0:
        raise ValueError("Time have to be positive.")
except ValueError as e:
    print(f"Error : {e}. Fix the value at default (five seconds).")
    duration = 5

# Ask for how much time will the URL open
try:
    times = int(input("Number of time the URL will open : "))
    if times <= 0:
        raise ValueError("The number have to be > 1.")
except ValueError as e:
    print(f"Erreur : {e}. Fix the number of time at default (1).")
    times = 1

# Confirm parameters
clear_console()
print(f"URL : {url}")
print(f"Time between each opening URL : {duration} seconds")
print(f"How much time : {times}")
input("Press enter to start...")

# Opening the URL
for x in range(times):
    print(f"Ouverture {x + 1}/{times} : {url}")
    webbrowser.open_new(url)
    time.sleep(duration)

print("Script finished. All the URL got opened.")
