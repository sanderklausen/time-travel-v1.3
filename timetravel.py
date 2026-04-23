import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import random

class TimeTravelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Travel v1.3")
        self.root.geometry("1020x680")
        self.root.resizable(False, False)
        
        # Set background color
        self.root.configure(bg='#ECE9D8')
        
        # Create main container with blue border
        main_frame = tk.Frame(root, bg='#4169e1', relief='solid', bd=3)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # Image area at top
        self.image_frame = tk.Frame(main_frame, bg='#ECE9D8', height=280)
        self.image_frame.pack(fill=tk.X, padx=15, pady=15)
        
        # Load and display image
        self.load_and_display_image()
        
        # Settings section
        settings_frame = tk.Frame(main_frame, bg='#ECE9D8', relief='solid', bd=2)
        settings_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        
        # Settings title
        settings_title = tk.Label(settings_frame, text="Settings", font=("Arial", 12, "bold"), bg='#ECE9D8')
        settings_title.pack(anchor='w', padx=20, pady=(10, 15))
        
        # Date section
        date_frame = tk.Frame(settings_frame, bg='#ECE9D8')
        date_frame.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        tk.Label(date_frame, text="Date", font=("Arial", 10), bg='#ECE9D8').pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Label(date_frame, text="D", font=("Arial", 10), bg='#ECE9D8').pack(side=tk.LEFT, padx=(5, 2))
        day_combo = ttk.Combobox(date_frame, values=[str(i) for i in range(1, 32)], width=3, state='readonly')
        day_combo.pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Label(date_frame, text="M", font=("Arial", 10), bg='#ECE9D8').pack(side=tk.LEFT, padx=(5, 2))
        month_combo = ttk.Combobox(date_frame, values=[str(i) for i in range(1, 13)], width=3, state='readonly')
        month_combo.pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Label(date_frame, text="Y", font=("Arial", 10), bg='#ECE9D8').pack(side=tk.LEFT, padx=(5, 2))
        year_entry = tk.Entry(date_frame, width=8)
        year_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Label(date_frame, text="CE", font=("Arial", 10), bg='#ECE9D8').pack(side=tk.LEFT, padx=(5, 2))
        ce_combo = ttk.Combobox(date_frame, values=["CE", "BCE"], width=4, state='readonly')
        ce_combo.pack(side=tk.LEFT)
        
        # Sqwimble slider section
        sqwimble_frame = tk.Frame(settings_frame, bg='#ECE9D8')
        sqwimble_frame.pack(fill=tk.X, padx=20, pady=(0, 15), anchor='e')
        
        tk.Label(sqwimble_frame, text="Sqwimble", font=("Arial", 10), bg='#ECE9D8').pack(side=tk.LEFT, padx=(0, 20))
        
        slider_frame = tk.Frame(sqwimble_frame, bg='#ECE9D8')
        slider_frame.pack(side=tk.LEFT)
        
        tk.Label(slider_frame, text="-100", font=("Arial", 8), bg='#ECE9D8').pack(side=tk.LEFT, padx=(0, 5))
        sqwimble_slider = ttk.Scale(slider_frame, from_=-100, to=100, orient=tk.HORIZONTAL, length=100)
        sqwimble_slider.set(0)
        sqwimble_slider.pack(side=tk.LEFT, padx=5)
        tk.Label(slider_frame, text="100", font=("Arial", 8), bg='#ECE9D8').pack(side=tk.LEFT, padx=(5, 0))
        
        # Location section
        location_frame = tk.Frame(settings_frame, bg='#ECE9D8')
        location_frame.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        tk.Label(location_frame, text="Location", font=("Arial", 10), bg='#ECE9D8').pack(side=tk.LEFT, padx=(0, 20))
        
        lat_long_frame = tk.Frame(location_frame, bg='#ECE9D8')
        lat_long_frame.pack(side=tk.LEFT)
        
        tk.Label(lat_long_frame, text="Lat.", font=("Arial", 10), bg='#ECE9D8').pack(anchor='w')
        lat_entry = tk.Entry(lat_long_frame, width=30)
        lat_entry.pack(anchor='w', pady=(0, 5))
        
        tk.Label(lat_long_frame, text="Long.", font=("Arial", 10), bg='#ECE9D8').pack(anchor='w')
        long_entry = tk.Entry(lat_long_frame, width=30)
        long_entry.pack(anchor='w')
        
        # Checkboxes section
        checkboxes_frame = tk.Frame(settings_frame, bg='#ECE9D8')
        checkboxes_frame.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        deterministic_var = tk.BooleanVar()
        deterministic_check = tk.Checkbutton(checkboxes_frame, text="Deterministic", variable=deterministic_var, bg='#ECE9D8', font=("Arial", 10))
        deterministic_check.pack(side=tk.LEFT, padx=(0, 40))
        
        assume_form_var = tk.BooleanVar(value=True)
        assume_form_check = tk.Checkbutton(checkboxes_frame, text="Assume Form", variable=assume_form_var, bg='#ECE9D8', font=("Arial", 10))
        assume_form_check.pack(side=tk.LEFT)
        
        # Start button
        button_frame = tk.Frame(settings_frame, bg='#ECE9D8')
        button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        
        start_button = tk.Button(button_frame, text="Start", font=("Arial", 12), width=12, height=2, 
                                 bg='#f0f0f0', relief='raised', bd=2, command=self.start_time_travel)
        start_button.pack(pady=10)
    
    def load_and_display_image(self):
        """Load image in background thread to avoid freezing the UI"""
        def load_image():
            try:
                # Load bush.png
                img_path = "bush.png"
                try:
                    img = Image.open(img_path)
                except:
                    # Create a placeholder image if file doesn't exist
                    img = Image.new('RGB', (520, 280), color='#cccccc')
                
                # Resize to fit the frame
                img = img.resize((520, 280), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                
                # Display in label
                img_label = tk.Label(self.image_frame, image=photo, bg='#ECE9D8')
                img_label.image = photo  # Keep a reference
                img_label.pack(fill=tk.BOTH, expand=True)
            except Exception as e:
                print(f"Error loading image: {e}")
        
        thread = threading.Thread(target=load_image, daemon=True)
        thread.start()
    
    def start_time_travel(self):
        """Make the Start button do something funny!"""
        def wiggle_and_flash():
            original_x = self.root.winfo_x()
            original_y = self.root.winfo_y()
            
            # Shake the window 10 times
            for i in range(10):
                shake_x = random.randint(-15, 15)
                shake_y = random.randint(-15, 15)
                self.root.geometry(f"+{original_x + shake_x}+{original_y + shake_y}")
                self.root.update()
                self.root.after(50)
            
            # Reset position
            self.root.geometry(f"+{original_x}+{original_y}")
            
            # Flash the background colors dramatically
            colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff', '#ECE9D8']
            for color in colors * 2:
                self.root.configure(bg=color)
                self.root.update()
                self.root.after(100)
            
            # Reset to original color
            self.root.configure(bg='#ECE9D8')
        
        # Run in background thread so it doesn't block UI
        thread = threading.Thread(target=wiggle_and_flash, daemon=True)
        thread.start()


def main():
    """Main entry point for the Time Travel application."""
    root = tk.Tk()
    app = TimeTravelApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
