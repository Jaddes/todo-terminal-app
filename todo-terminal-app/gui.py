import tkinter as tk
from tkinter import ttk
from todo import ToDoList

class ToDoAppGUI:
    def __init__(self, master):
        self.master = master
        self.todo_list = ToDoList()
        master.title("Bobi List")
        master.geometry("600x600")
        master.resizable(True, True) 
        master.configure(bg="#1a1a2e")
        
        for i in range(3):
            master.rowconfigure(i, weight=1)
        master.columnconfigure(0, weight=1)
        
        #Cyberpunk style
        font_style = ("Consolas", 14)
        neon_cyan = "#00ffff"
        accent_purple = "#ff00ff"
        background = "#1a1a2e"
        input_bg = "#162447"
        
        # Top Navigation
        top_bar = tk.Frame(master, bg=background)
        top_bar.grid(row=0, column=0, sticky="new", padx=10, pady=(10, 0))
        top_bar.columnconfigure(0, weight=1)
        top_bar.columnconfigure(1, weight=0)
        
        # Left button - Sign In
        left_buttons = tk.Frame(top_bar, bg=background)
        left_buttons.grid(row=0, column=0, sticky="w")

        sign_in_btn = tk.Button(left_buttons, text="Sign In", command=self.sign_in_placeholder,
                                bg=input_bg, fg=neon_cyan, relief="flat", font=("Consolas", 10),
                                activebackground=accent_purple, activeforeground="black")
        sign_in_btn.pack(side="left", padx=5)
        
        # Right button menu
        right_buttons = tk.Frame(top_bar, bg=background)
        right_buttons.grid(row=0, column=1, sticky="e")

        stats_btn = tk.Button(right_buttons, text="📊", command=self.stats_placeholder,
                              bg=input_bg, fg=neon_cyan, relief="flat", font=("Consolas", 12),
                              activebackground=accent_purple, activeforeground="black", width=3)
        stats_btn.pack(side="left", padx=5)

        settings_btn = tk.Button(right_buttons, text="⚙️", command=self.settings_placeholder,
                                 bg=input_bg, fg=neon_cyan, relief="flat", font=("Consolas", 12),
                                 activebackground=accent_purple, activeforeground="black", width=3)
        settings_btn.pack(side="left", padx=5)
        
        # Title
        self.label = tk.Label(master, text="Boki To-Do", font=("Consolas", 20, "bold"), fg=neon_cyan, bg=background)
        self.label.grid(row=0, column=0, pady=10, sticky="n")
        
        # Input frame (entry + dugme)
        input_frame = tk.Frame(master, bg=background)
        input_frame.grid(row=1, column=0, sticky="ew", padx=10)
        input_frame.columnconfigure(0, weight=4)
        input_frame.columnconfigure(1, weight=1)

        self.entry = tk.Entry(input_frame, bg="#1a1a1a", fg=neon_cyan, insertbackground=neon_cyan, font=font_style, relief="flat")
        self.entry.grid(row=0, column=0, sticky="ew", padx=(0, 5), pady=5)

        self.add_button = tk.Button(input_frame, text="➕ ADD", command=self.add_task_placeholder,
                                    fg=accent_purple, bg=input_bg, activebackground="#ffcc00",
                                    activeforeground=neon_cyan, font=("Consolas", 12), relief="flat")
        self.add_button.grid(row=0, column=1, sticky="ew", pady=5)
        
        
        
        
        # Task frame
        self.task_frame = tk.Frame(master, bg=background)
        self.task_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        
        # Scroll + Canvas za buduci prikaz vise zadataka
        self.canvas = tk.Canvas(self.task_frame, bg=background, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.task_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg=background)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        
        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Placeholder poruka
        self.placeholder = tk.Label(self.scrollable_frame, text="🚀 (tasks will appear here)",
                                    fg=neon_cyan, bg=background, font=("Consolas", 12))
        self.placeholder.pack()
        
    def add_task_placeholder(self):
        print("Kliknuto: Dodaj zadatak (funkcionalnost još nije implementirana)")
    
    def sign_in_placeholder(self):
        print("Kliknuto: Sign In (placeholder za login)")

    def stats_placeholder(self):
        print("Kliknuto: Statistika (placeholder za izveštaje)")

    def settings_placeholder(self):
        print("Kliknuto: Podešavanja (placeholder za settings meni)")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoAppGUI(root)
    root.mainloop()
    
