# Rewin - React + Vite + Tailwind Setup Tool

![Rewin Logo](rewin_logo.png)

Rewin is a lightweight GUI application built with Python and CustomTkinter that automates the setup of a React project with Vite and Tailwind CSS (version 4). It simplifies the process of creating a modern web development environment with a single click.

## Features
- Quickly set up a React project with Vite and Tailwind CSS v4.
- Select a directory for your project.
- Automatically configures `tailwind.config.js`, `vite.config.js`, and `index.css`.
- Launches the development server and provides a clickable link to view your project.
- Clean and modern UI with technology logos (React, Vite, Tailwind).

## Prerequisites
Before using Rewin, ensure you have the following installed:
- **Python 3.7+**: [Download Python](https://www.python.org/downloads/)
- **Node.js and npm**: [Download Node.js](https://nodejs.org/) (includes npm)
- A modern operating system (Windows, macOS, or Linux).

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/rewin.git
   cd rewin
2. **Install Python Dependencies: Install the required Python packages using pi**:
    pip install customtkinter Pillow

customtkinter: For the GUI framework.
Pillow: For image handling in the UI.
Place Logo Files: Ensure the following image files are in the root directory of the project:
rewin_logo.png (200x100 pixels recommended)
react_logo.png (50x50 pixels recommended)
vite_logo.png (50x50 pixels recommended)
tailwind_logo.png (50x50 pixels recommended)
Alternatively, you can provide your own logos and adjust the sizes in the code.

Usage
Run the Application:
bash
Wrap
Copy
python rewin.py

This launches the Rewin GUI.
Steps to Create a Project:
Enter a project name in the text field (defaults to "my-app").
Click "Select directory" to choose where the project will be created.
Click "Create project" to generate the React + Vite + Tailwind setup.
Once successful, a clickable "Project link" will appear—click it to open http://localhost:5173 in your browser.
Close the Application:
Close the window to terminate the app and stop the development server (if running).
Project Structure
After running Rewin, your new project will include:

A Vite-based React app.
Tailwind CSS v4 integrated via npm.
Configuration files (tailwind.config.js, vite.config.js, src/index.css) pre-set for immediate use.

Screenshots
(Add screenshots here once available)

Example:

Main UI with logo and input fields.
Successful project creation with link.
Known Issues
Image Loading: The current code uses ctk.Image, which is incorrect. It should use PIL.Image from the Pillow library. Update the code as follows:
python
Wrap
Copy
from PIL import Image
self.logo = ctk.CTkImage(light_image=Image.open("rewin_logo.png"), size=(200, 100))
This will be fixed in the next release.
Font Cutoff: The "y" in "No directory selected" may be slightly cut off—adjust the label height or padding if needed.
Contributing
Contributions are welcome! Please:

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.
License
This project is licensed under the MIT License—see the LICENSE file for details.

Acknowledgments
Built with CustomTkinter.
Uses Vite, React, and Tailwind CSS.
Inspired by the need for a fast, GUI-based web project setup tool.
text
Wrap
Copy

### Notes:
1. **Repository URL**: Replace `https://github.com/yourusername/rewin.git` with your actual GitHub repository URL once you create it.
2. **Logo Files**: The README assumes the logo files are included. If you don’t want to include them, mention they’re optional or provide placeholders (like the emoji fallbacks in the code).
3. **Screenshots**: You can add screenshots by taking images of the running app and uploading them to the repo (e.g., in a `screenshots/` folder), then linking them like `![UI](screenshots/main_ui.png)`.
4. **License File**: If you want to use the MIT License, create a `LICENSE` file in your repo with the standard MIT text.
5. **Code Fix**: The README highlights the `ctk.Image` issue and suggests the `PIL.Image` fix, aligning with our earlier discussion. You should update your code accordingly before uploading to GitHub.

### Steps to Upload to GitHub:
1. **Fix the Code**: Update all `ctk.Image` calls to use `from PIL import Image` and `Image.open()` as shown in my previous responses.
2. **Create the Repo**:
   - Go to GitHub, click "New repository," name it (e.g., "rewin"), and initialize it with a README (you can overwrite it later).
   - Follow the instructions to push your local code:
     ```bash
     git init
     git add .
     git commit -m "Initial commit"
     git remote add origin https://github.com/yourusername/rewin.git