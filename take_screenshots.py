import pyautogui
import time
import os

# Create a folder to store the screenshots
folder = "screenshots"
if not os.path.exists(folder):
    os.makedirs(folder)

# Take screenshots every second for 10 seconds
for i in range(10):
    screenshot = pyautogui.screenshot()  # Take a screenshot
    screenshot.save(f"{folder}/screenshot_{i+1}.png")  # Save the screenshot in the folder
    print(f"Screenshot {i+1} saved.")  # Print a message indicating the screenshot was saved
    time.sleep(1)  # Wait for 1 second before taking the next screenshot

print("Finished taking screenshots!")
