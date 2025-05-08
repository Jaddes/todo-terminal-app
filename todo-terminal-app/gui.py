import tkinter as tk
from tkinter import ttk, messagebox
from todo import ToDoList
from PIL import Image, ImageTk
import os

class KGBAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("TASK CONTROL CENTER")
        self.root.geometry("700x600")
        self.root.configure(bg="#0d0d0d")
        self.todo_list = ToDoList()
        
        # Theme colors
        self.bg_main = "#1a1a1a"
        self.bg_panel = "#2b2b2b"
        self.accent_red = "#992222"
        self.text_soft = "#cccccc"
        self.kgb_font = ("Courier New", 13)

        self.show_login_screen()

    def show_login_screen(self):
        self.login_frame = tk.Frame(self.root, bg=self.bg_panel)
        self.login_frame.pack(expand=True)

        tk.Label(self.login_frame, text="🔐 KGB AUTHORIZATION REQUIRED 🔐", fg=self.accent_red,
                 bg=self.bg_main, font=("Courier New", 18, "bold")).pack(pady=20)

        self.code_entry = tk.Entry(self.login_frame, show="*", font=self.kgb_font, bg="#333333",
                                   fg=self.text_soft, insertbackground=self.text_soft)
        self.code_entry.pack(pady=10)
        self.code_entry.focus()
        
        # Bind Enter key to login
        self.code_entry.bind("<Return>", lambda event: self.verify_code())

        tk.Button(self.login_frame, text="ENTER", command=self.verify_code,
                  font=self.kgb_font, bg=self.accent_red, fg="white",
                  activebackground="#8b0000", relief="flat").pack(pady=10)

    def verify_code(self):
        code = self.code_entry.get()
        if code == "KGB123":
            self.login_frame.destroy()
            self.build_interface()
        else:
            messagebox.showerror("ACCESS DENIED", "Incorrect authorization code.")

    def build_interface(self):
        paned = tk.PanedWindow(self.root, sashrelief="flat", bg=self.bg_main)
        paned.pack(fill="both", expand=True)
        
        # Folders panel
        self.folder_panel = tk.Frame(paned, width=200, height=600, bg=self.bg_panel)
        self.folder_panel.pack_propagate(False)
        self.folder_panel.bind("<Configure>", self.resize_folder_background)
        paned.add(self.folder_panel)  # make sure this isn't called twice


        # 🧱 Add and resize background image to fill the entire panel
        self.original_bg = Image.open("assets/drawer_bg.png")  # store original image
        self.drawer_bg = ImageTk.PhotoImage(self.original_bg.resize((200, 600)))
        self.drawer_bg_label = tk.Label(self.folder_panel, image=self.drawer_bg, bg=self.bg_panel)
        self.drawer_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.drawer_bg_label.lower()# send it to background

        # Now place label above image
        self.folder_title = tk.Label(self.folder_panel, text="📁 FOLDERS", bg=self.bg_panel,
                                    fg=self.text_soft, font=("Courier New", 14, "bold"))
        self.folder_title.place(x=10, y=10)

        # List frame
        self.folder_list_frame = tk.Frame(self.folder_panel, bg=self.bg_panel)
        self.folder_list_frame.place(x=0, y=50, width=200, height=550)

        paned.add(self.folder_panel)

        # Right task panel
        self.task_panel = tk.Frame(paned, bg=self.bg_main)
        paned.add(self.task_panel)

        header = tk.Label(self.task_panel, text="🛰 TASK CONTROL CENTER",
                          font=("Courier New", 20, "bold"), fg=self.text_soft,
                          bg=self.bg_main)
        header.pack(pady=10)

        input_frame = tk.Frame(self.task_panel, bg=self.bg_main)
        input_frame.pack(padx=10, pady=5, fill="x")

        self.task_entry = tk.Entry(input_frame, font=self.kgb_font, bg="#333333",
                                   fg=self.accent_red, insertbackground=self.accent_red)
        self.task_entry.pack(side="left", expand=True, fill="x", padx=(0, 10))
        self.task_entry.bind("<Return>", lambda e: self.add_task())

        tk.Button(input_frame, text="ADD OPERATION", command=self.add_task,
                  font=self.kgb_font, bg=self.accent_red, fg="white",
                  activebackground="#8b0000", relief="flat").pack(side="right")

        # Scrollable task frame
        self.task_frame = tk.Frame(self.task_panel, bg=self.bg_main)
        self.task_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.canvas = tk.Canvas(self.task_frame, bg=self.bg_main, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.task_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg=self.bg_main)

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.placeholder = tk.Label(self.scrollable_frame, text="🗂 No active operations",
                                    font=self.kgb_font, fg=self.text_soft, bg=self.bg_main)
        self.placeholder.pack()

        self.load_folder_buttons()

    def load_folder_buttons(self):
        project_dir = "projects"
        os.makedirs(project_dir, exist_ok=True)
        files = [f for f in os.listdir(project_dir) if f.endswith(".json")]

        for widget in self.folder_list_frame.winfo_children():
            widget.destroy()

        if not files:
            tk.Label(self.folder_list_frame, text="(No projects found)", bg=self.bg_panel,
                    fg="#666666", font=self.kgb_font).pack(padx=10, pady=10)
            return

        for file in files:
            name = os.path.splitext(file)[0]
            btn = tk.Button(
                self.folder_list_frame,
                text=f"📁 {name}",
                font=self.kgb_font,
                bg="#00000000",
                fg=self.text_soft,
                activebackground="#553333",
                borderwidth=0,
                highlightthickness=0,
                relief="flat",
                anchor="w",
                padx=12
            )
            btn.pack(fill="x", padx=10, pady=1)

            self.add_tooltip(btn, name)  # ✅ Now that btn is created

            
    def add_tooltip(self, widget, text):
        def on_enter(event):
            self.tooltip = tk.Toplevel()
            self.tooltip.overrideredirect(True)
            self.tooltip.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
            label = tk.Label(self.tooltip, text=text, bg="yellow", fg="black", relief="solid", borderwidth=1)
            label.pack()

        def on_leave(event):
            if hasattr(self, 'tooltip'):
                self.tooltip.destroy()

        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)


    def load_project(self, filename):
        full_path = os.path.join("projects", filename)
        self.todo_list.load_from_file(full_path)
        self.current_file = full_path
        self.refresh_tasks()

    def add_task(self):
        if not self.current_file:
            messagebox.showinfo("No File Selected", "Please select a folder (project) first.")
            return

        title = self.task_entry.get().strip()
        if not title:
            return

        self.todo_list.add_task(title)
        self.todo_list.save_to_file(self.current_file)
        self.task_entry.delete(0, tk.END)

        if self.placeholder:
            self.placeholder.destroy()
            self.placeholder = None

        self.refresh_tasks()

    def refresh_tasks(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        active_tasks = [t for t in self.todo_list.tasks if not t.completed]

        if not active_tasks:
            self.placeholder = tk.Label(self.scrollable_frame, text="🗂 No active operations",
                                        font=self.kgb_font, fg=self.text_soft, bg=self.bg_main)
            self.placeholder.pack()
            return

        for idx, task in enumerate(active_tasks, start=1):
            row = tk.Frame(self.scrollable_frame, bg=self.bg_main)
            row.pack(fill="x", pady=3)

            label = tk.Label(row, text=f"OPERATION: {task.title}",
                             font=self.kgb_font, bg=self.bg_main, fg=self.text_soft, anchor="w")
            label.pack(side="left", expand=True, fill="x", padx=10)

            done_button = tk.Button(row, text="✅ DECLASSIFIED", command=lambda i=idx: self.complete_task(i),
                                    font=self.kgb_font, bg=self.accent_red, fg="white",
                                    relief="flat", activebackground="#b30000")
            done_button.pack(side="right", padx=5)

    def complete_task(self, index):
        active_tasks = [t for t in self.todo_list.tasks if not t.completed]
        if index - 1 < len(active_tasks):
            task = active_tasks[index - 1]
            task.mark_completed()
            if self.current_file:
                self.todo_list.save_to_file(self.current_file)
            self.refresh_tasks()

    def resize_folder_background(self, event):
        new_width = event.width
        new_height = event.height
        resized = self.original_bg.resize((new_width, new_height))
        self.drawer_bg = ImageTk.PhotoImage(resized)
        self.drawer_bg_label.config(image=self.drawer_bg)
        self.drawer_bg_label.image = self.drawer_bg  # prevent garbage collection


if __name__ == "__main__":
    root = tk.Tk()
    app = KGBAppGUI(root)
    root.mainloop()
