# 🎯 CursorSnap

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg) ![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg) ![Downloads](https://img.shields.io/github/downloads/Aryan-git-byte/CursorSnap/total.svg) ![Release](https://img.shields.io/github/v/release/Aryan-git-byte/CursorSnap.svg) ![Stars](https://img.shields.io/github/stars/Aryan-git-byte/CursorSnap.svg)

**Save and restore your mouse cursor position with global hotkeys**

[Download Latest Release](https://github.com/Aryan-git-byte/CursorSnap/releases) • [Report Bug](https://github.com/Aryan-git-byte/CursorSnap/issues) • [Request Feature](https://github.com/Aryan-git-byte/CursorSnap/issues)

![CursorSnap Demo](https://via.placeholder.com/600x300/0078ff/ffffff?text=CursorSnap+Demo)

---

## ✨ Features

- 🖱️ **Save Mouse Position** - Capture your cursor location instantly
- ⚡ **Quick Restore** - Jump back to saved position with a hotkey
- 🎮 **Global Hotkeys** - Works across all applications
- 🪟 **System Tray** - Minimal, non-intrusive interface
- 🎨 **Clean GUI** - Simple and intuitive controls
- 🚀 **Lightweight** - Minimal resource usage
- 🔒 **Always Available** - Runs in background

---

## 🎮 Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl + Win + C | 💾 Save cursor position |
| Ctrl + Win + R | 🔄 Restore cursor position |
| Ctrl + Win + W | ❌ Quit application |

---

## 📥 Installation

### Option 1: Download Executable (Recommended)

1. Go to [Releases](https://github.com/Aryan-git-byte/CursorSnap/releases)
2. Download the latest `CursorSnap.exe`
3. Run the executable - no installation needed!

### Option 2: Run from Source

```bash
# Clone the repository
git clone https://github.com/Aryan-git-byte/CursorSnap.git
cd CursorSnap

# Install dependencies
pip install -r requirements.txt

# Run the application
python cursorsnap.py
```

---

## 🔧 Requirements

```
pyautogui>=0.9.53
keyboard>=0.13.5
pystray>=0.19.4
Pillow>=9.0.0
```

---

## 🚀 Usage

1. **Launch CursorSnap** - The app runs in the system tray
2. **Save Position** - Move your cursor and press Ctrl + Win + C
3. **Restore Position** - Press Ctrl + Win + R to return
4. **Access GUI** - Click the tray icon to show/hide the control window

### Use Cases

- 🎨 **Designers** - Quickly return to specific tool locations
- 💻 **Developers** - Navigate between IDE panels efficiently
- 🎮 **Gamers** - Save important screen positions
- 📊 **Data Entry** - Speed up repetitive workflows
- 🖥️ **Multi-Monitor** - Jump between screens instantly

---

## 🖼️ Screenshots

### Main Window
![Main Window](https://via.placeholder.com/280x250/ffffff/000000?text=Main+Window)

### System Tray
![System Tray](https://via.placeholder.com/200x100/ffffff/000000?text=System+Tray)

---

## 🛠️ Building from Source

To create your own executable:

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --onefile --windowed --icon=icon.ico cursorsnap.py
```

The executable will be in the `dist` folder.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🔨 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🎉 Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with [PyAutoGUI](https://pyautogui.readthedocs.io/)
- Icons by [Pillow](https://python-pillow.org/)
- System tray by [pystray](https://github.com/moses-palmer/pystray)

---

## 💬 Support

Having issues? Got questions?

- 📧 Email: aryan17550@gmail.com
- 💬 [Open an Issue](https://github.com/Aryan-git-byte/CursorSnap/issues)
- ⭐ Star this repo if you find it useful!

---

**Made with ❤️ by [Aryan](https://github.com/Aryan-git-byte)**

If you find this tool helpful, consider giving it a ⭐!

