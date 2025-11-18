import pyautogui
import keyboard
import sys
import threading
import ctypes
import tkinter as tk
from tkinter import ttk
from pystray import Icon, Menu, MenuItem
from PIL import Image


# Hide console
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

saved_position = None
tray_icon = None


# -----------------------------
# Core functions
# -----------------------------
def save_position():
    global saved_position
    saved_position = pyautogui.position()
    update_gui()


def restore_position():
    global saved_position
    if saved_position:
        pyautogui.moveTo(saved_position.x, saved_position.y, duration=0.2)


def quit_all(icon=None, item=None):
    try:
        if tray_icon:
            tray_icon.stop()
    except:
        pass

    try:
        app.destroy()
    except:
        pass

    sys.exit(0)


# -----------------------------
# GUI Setup
# -----------------------------
def hide_window():
    app.withdraw()

def build_gui():
    global position_label, app

    app = tk.Tk()
    app.title("Mouse Saver")
    app.geometry("280x250")
    app.resizable(False, False)

    # Remove from taskbar
    app.attributes('-toolwindow', True)
    app.attributes('-topmost', False)

    # Override close button → hide instead of exit
    app.protocol("WM_DELETE_WINDOW", hide_window)

    ttk.Label(app, text="Mouse Saver", font=("Segoe UI", 12, "bold")).pack(pady=5)

    position_label = ttk.Label(app, text="Saved: None", font=("Segoe UI", 10))
    position_label.pack(pady=4)

    ttk.Button(app, text="Save Position", command=save_position).pack(pady=2)
    ttk.Button(app, text="Restore Position", command=restore_position).pack(pady=2)

    # Quit at the bottom
    ttk.Button(app, text="Quit App", command=quit_all).pack(pady=8)

    return app



def update_gui():
    if saved_position:
        position_label.config(text=f"Saved: {saved_position.x}, {saved_position.y}")
    else:
        position_label.config(text="Saved: None")


# -----------------------------
# Tray Icon
# -----------------------------
def toggle_gui(icon, item):
    if app.state() == "normal":
        app.withdraw()
    else:
        app.deiconify()


def create_tray():
    global tray_icon

    img = Image.new("RGB", (16, 16), (0, 120, 255))

    tray_icon = Icon(
        "MouseSaver",
        img,
        menu=Menu(
            MenuItem("Show/Hide Window", toggle_gui),
            MenuItem("Quit", quit_all)
        )
    )

    tray_icon.run()


# -----------------------------
# Hotkeys
# -----------------------------
def hotkey_listener():
    keyboard.add_hotkey('ctrl+windows+c', save_position)
    keyboard.add_hotkey('ctrl+windows+r', restore_position)
    keyboard.add_hotkey('ctrl+windows+w', quit_all)
    keyboard.wait()


# -----------------------------
# Main Logic
# -----------------------------
app = build_gui()

# Start tray in a separate thread
threading.Thread(target=create_tray, daemon=True).start()

# Start hotkeys in a thread
threading.Thread(target=hotkey_listener, daemon=True).start()

# Show GUI on startup
app.mainloop()
