from fastapi import FastAPI
import time
import os
import mss
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

# Create a folder to store the screenshots
folder = "screenshots"
Path(folder).mkdir(parents=True, exist_ok=True)

@app.get("/")
def take_screenshots():
    with mss.mss() as sct:
        # Take screenshots every second for 10 seconds
        for i in range(10):
            screenshot_path = f"{folder}/screenshot_{i+1}.png"
            sct.shot(output=screenshot_path)  # Take a screenshot and save it
            print(f"Screenshot {i+1} saved.")  # Print a message indicating the screenshot was saved
            time.sleep(1)  # Wait for 1 second before taking the next screenshot

    return {"message": "10 screenshots taken and saved!", "folder": folder}


