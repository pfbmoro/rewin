from PIL import Image
import customtkinter as ctk
import os
import subprocess
import sys
import webbrowser
import time

class RewinApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rewin - React + Tailwind 4 Setup")
        self.root.geometry("500x400")
        self.root.configure(fg_color="#F5F5F5")

        # Bind window close event
        self.root.protocol("WM_DELETE_WINDOW", self.close_app)

        # Logo and tagline
        try:
            self.logo = ctk.CTkImage(light_image=Image.open("rewin_logo.png"), size=(192, 51))
            self.logo_label = ctk.CTkLabel(root, image=self.logo, text="")
            self.logo_label.pack(pady=10)
        except Exception as e:
            print(f"Error loading Rewin logo: {e}")
            self.logo_label = ctk.CTkLabel(root, text="Rewin", font=("Arial", 24, "bold"))
            self.logo_label.pack(pady=5)
        
        self.tagline = ctk.CTkLabel(root, text="Lightning-fast React Environment Setup", font=("Arial", 10, "normal"), text_color="#777")
        self.tagline.pack(pady=5)

        # Project name input
        self.label = ctk.CTkLabel(root, text="Enter your project name...", font=("Arial", 12), text_color="#777")
        self.label.pack(pady=10)
        
        self.entry = ctk.CTkEntry(root, width=300, height=40, font=("Arial", 12), fg_color="white", border_color="#DDD", border_width=2)
        self.entry.pack(pady=5)
        self.entry.insert(0, "my-app")

        # Button frame
        button_frame = ctk.CTkFrame(root, fg_color="#F5F5F5")
        button_frame.pack(pady=10)

        self.select_btn = ctk.CTkButton(button_frame, text="Select directory", command=self.select_directory, 
                                       fg_color="#007BFF", hover_color="#0056B3", corner_radius=10)
        self.select_btn.pack(side=ctk.LEFT, padx=5)

        self.create_btn = ctk.CTkButton(button_frame, text="Create project", command=self.create_project, 
                                       fg_color="#FF4500", hover_color="#CC3700", corner_radius=10)
        self.create_btn.pack(side=ctk.LEFT, padx=5)

        self.close_btn = ctk.CTkButton(button_frame, text="Close", command=self.close_app, 
                                      fg_color="#DC3545", hover_color="#A52834", corner_radius=10)
        self.close_btn.pack(side=ctk.LEFT, padx=5)

        # Directory status
        self.dir_label = ctk.CTkLabel(root, text="No directory selected", font=("Arial", 12), text_color="#333", height=20)
        self.dir_label.pack(pady=10)

        self.selected_dir = None

        # Status label
        self.status = ctk.CTkLabel(root, text="", font=("Arial", 10), text_color="#333")
        self.status.pack(pady=5)

        # Link label
        self.link_label = ctk.CTkLabel(root, text="", font=("Arial", 10), text_color="#007BFF", cursor="hand")
        self.link_label.pack(pady=5)
        self.link_label.bind("<Button-1>", lambda e: self.open_link())
        self.link_url = ""

        # Initialize dev_process
        self.dev_process = None

    def select_directory(self):
        self.selected_dir = ctk.filedialog.askdirectory(title="Select Project Directory")
        if self.selected_dir:
            self.dir_label.configure(text=f"Selected: {self.selected_dir}", text_color="#007BFF")
        else:
            self.dir_label.configure(text="No directory selected", text_color="#333")

    def open_link(self):
        if self.link_url:
            webbrowser.open(self.link_url)

    def create_project(self):
        project_name = self.entry.get().strip()
        if not project_name:
            ctk.CTkMessageBox.show_error("Error", "Please enter a project name!")
            return
        if not self.selected_dir:
            ctk.CTkMessageBox.show_error("Error", "Please select a directory!")
            return

        self.status.configure(text="Creating project... Please wait.", text_color="#007BFF")
        self.link_label.configure(text="")  # Clear previous link
        self.root.update()

        project_path = os.path.join(self.selected_dir, project_name)

        try:
            # Check if npm is installed
            subprocess.run(["npm", "--version"], check=True, capture_output=True)

            # Initialize new React project with Vite
            os.chdir(self.selected_dir)
            subprocess.run(f"npm create vite@latest {project_name} -- --template react", 
                         shell=True, check=True, capture_output=True)
            
            # Change into project directory
            os.chdir(project_name)

            # Install Tailwind CSS and Vite plugin
            subprocess.run("npm install tailwindcss @tailwindcss/vite", 
                         shell=True, check=True, capture_output=True)

            # Write vite.config.js with Tailwind plugin
            with open("vite.config.js", "w") as f:
                f.write('''import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [react(), tailwindcss()],
})
''')

            # Write tailwind.config.js
            with open("tailwind.config.js", "w") as f:
                f.write('''/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
}
''')

            # Update src/index.css with Tailwind import
            with open("src/index.css", "w") as f:
                f.write('@import "tailwindcss";\n')

            # Ensure index.css is imported in main.jsx
            main_file = "src/main.jsx"
            if os.path.exists(main_file):
                with open(main_file, "r") as f:
                    content = f.read()
                
                # Add import if it doesn't exist
                if "import './index.css'" not in content:
                    import_pos = content.find("import React from 'react'")
                    if import_pos != -1:
                        new_content = content[:import_pos] + "import './index.css';\n" + content[import_pos:]
                        with open(main_file, "w") as f:
                            f.write(new_content)

            # Start the dev server in the background
            self.dev_process = subprocess.Popen(["npm", "run", "dev"], 
                                              stdout=subprocess.PIPE, 
                                              stderr=subprocess.PIPE)
            
            # Wait briefly to ensure server starts
            time.sleep(2)
            
            if self.dev_process.poll() is None:  # Check if process is still running
                self.link_url = "http://localhost:5173"
                self.status.configure(text=f"Success! Project '{project_name}' created at:\n{project_path}", 
                                    text_color="#007BFF")
                self.link_label.configure(text="Project link")
            else:
                raise Exception("Development server failed to start")

        except subprocess.CalledProcessError as e:
            self.status.configure(text=f"Error: {e.stderr.decode() if e.stderr else 'Command failed'}", 
                                text_color="#FF0000")
        except FileNotFoundError:
            self.status.configure(text="Error: npm not found. Please install Node.js.", 
                                text_color="#FF0000")
        except Exception as e:
            self.status.configure(text=f"Error: {str(e)}", text_color="#FF0000")

    def close_app(self):
        if self.dev_process and self.dev_process.poll() is None:
            self.dev_process.terminate()  # Stop the dev server if running
        self.root.quit()  # Close the app

def main():
    root = ctk.CTk()
    app = RewinApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()