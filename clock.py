import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")
root.resizable(False, False)

# Time label
label = tk.Label(root, font=("Helvetica", 40), fg="black")
label.pack(pady=20)

# Function to update the time every second
def update_time():
    current_time = time.strftime("%H:%M:%S")  # 24-hour format
    label.config(text=current_time)
    root.after(1000, update_time)  # update every 1 sec

update_time()  # start the clock
root.mainloop()
