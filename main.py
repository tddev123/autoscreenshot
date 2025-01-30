from fastapi import FastAPI
import pyautogui
import time
import os
from fastapi.responses import FileResponse

app = FastAPI()

# Create a folder to store the screenshots
folder = "screenshots"
if not os.path.exists(folder):
    os.makedirs(folder)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/take_screenshots/")
def take_screenshots():
    # Take screenshots every second for 10 seconds
    for i in range(10):
        screenshot = pyautogui.screenshot()  # Take a screenshot
        screenshot.save(f"{folder}/screenshot_{i+1}.png")  # Save the screenshot in the folder
        print(f"Screenshot {i+1} saved.")  # Print a message indicating the screenshot was saved
        time.sleep(1)  # Wait for 1 second before taking the next screenshot

    return {"message": "10 screenshots taken and saved!", "folder": folder}

@app.get("/download_screenshot/{filename}")
def download_screenshot(filename: str):
    file_path = os.path.join(folder, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return {"message": "File not found."}
