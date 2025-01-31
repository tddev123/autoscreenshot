import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab
import time
import threading
from fastapi import FastAPI



# Initialize FastAPI
app = FastAPI()
# Global variable to control the screenshot process
stop_event = threading.Event()

@app.get("/")
# Function to take screenshots with a specified delay
def take_screenshots(num_screenshots, delay):
    for i in range(num_screenshots):  # Take the specified number of screenshots
        if stop_event.is_set():  # Check if the stop button was pressed
            status_label.config(text="Screenshot process stopped!", fg="red")
            break
        
        # Capture the screen
        screenshot = ImageGrab.grab()
        
        # Save the screenshot with a unique filename
        filename = f"screenshot_{i+1}.png"
        screenshot.save(filename)
        
        # Update the label to show the status and counter
        status_label.config(text=f"Saved {filename} ({i+1}/{num_screenshots})", fg="blue")
        
        # Wait for the specified delay before taking the next screenshot
        time.sleep(delay)
    
    # Final confirmation message
    if not stop_event.is_set():
        status_label.config(text=f"All {num_screenshots} screenshots saved!", fg="green")
    else:
        status_label.config(text="Screenshot process stopped!", fg="red")
    
    # Re-enable the start button and reset the stop event
    screenshot_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    stop_event.clear()

# Function to start the screenshot process in a separate thread
def start_screenshot_thread():
    # Get the selected number of screenshots and delay
    num_screenshots = int(num_screenshots_var.get())
    delay = float(delay_var.get())
    
    # Disable the start button and enable the stop button
    screenshot_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    
    # Start the screenshot process in a new thread
    threading.Thread(target=take_screenshots, args=(num_screenshots, delay), daemon=True).start()

# Function to stop the screenshot process
def stop_screenshot_process():
    stop_event.set()  # Signal the thread to stop
    stop_button.config(state=tk.DISABLED)  # Disable the stop button

# Create the main window
window = tk.Tk()
window.title("Screenshot App")
window.geometry("600x350")  # Larger window size
window.configure(bg="#f0f0f0")  # Light gray background

# Create a label for instructions
instruction_label = tk.Label(
    window,
    text="Select options and click the button to start",
    font=("Arial", 14, "bold"),
    bg="#f0f0f0",
    fg="#333333"  # Dark gray text
)
instruction_label.pack(pady=20)

# Create a frame for the dropdown menus
dropdown_frame = tk.Frame(window, bg="#f0f0f0")
dropdown_frame.pack()

# Dropdown menu for the number of screenshots
num_screenshots_label = tk.Label(
    dropdown_frame,
    text="Number of Screenshots:",
    font=("Arial", 12),
    bg="#f0f0f0",
    fg="#333333"
)
num_screenshots_label.grid(row=0, column=0, padx=10, pady=15)  # Increased padding
num_screenshots_var = tk.StringVar(value="5")  # Default value
num_screenshots_dropdown = ttk.Combobox(
    dropdown_frame,
    textvariable=num_screenshots_var,
    font=("Arial", 12),
    state="readonly",
    width=20  # Increased width
)
num_screenshots_dropdown['values'] = list(range(1, 101))  # Options from 1 to 100
num_screenshots_dropdown.grid(row=0, column=1, padx=10, pady=15)  # Increased padding

# Dropdown menu for the delay between screenshots
delay_label = tk.Label(
    dropdown_frame,
    text="Delay Between Screenshots (seconds):",
    font=("Arial", 12),
    bg="#f0f0f0",
    fg="#333333"
)
delay_label.grid(row=1, column=0, padx=10, pady=15)  # Increased padding
delay_var = tk.StringVar(value="1.0")  # Default value
delay_dropdown = ttk.Combobox(
    dropdown_frame,
    textvariable=delay_var,
    font=("Arial", 12),
    state="readonly",
    width=20  # Increased width
)
delay_dropdown['values'] = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]  # Options from 0.5 to 5 seconds
delay_dropdown.grid(row=1, column=1, padx=10, pady=15)  # Increased padding

# Create a frame to hold the buttons
button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack(pady=20)

# Create a button to start screenshots
screenshot_button = tk.Button(
    button_frame,
    text="Start Screenshots",
    command=start_screenshot_thread,
    font=("Arial", 14, "bold"),
    bg="#4CAF50",  # Green background
    fg="white",    # White text
    padx=20,
    pady=10,
    bd=0,
    activebackground="#45a049"  # Darker green when clicked
)
screenshot_button.pack(side=tk.LEFT, padx=10)

# Create a button to stop screenshots
stop_button = tk.Button(
    button_frame,
    text="Stop",
    command=stop_screenshot_process,
    font=("Arial", 14, "bold"),
    bg="#FF5733",  # Red background
    fg="white",    # White text
    padx=20,
    pady=10,
    bd=0,
    state=tk.DISABLED,
    activebackground="#e64a19"  # Darker red when clicked
)
stop_button.pack(side=tk.LEFT, padx=10)

# Create a label for status updates
status_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    bg="#f0f0f0",
    fg="#333333"
)
status_label.pack(pady=20)

# Run the application
window.mainloop()

    
