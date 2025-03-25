import tkinter as tk
from tkinter import filedialog

class TextReaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Reader App")
        self.root.geometry("800x600")

        # Create menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Create file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Create text area
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill=tk.BOTH, expand=1)

    def open_file(self):
        # Open file dialog
        file_path = filedialog.askopenfilename(title="Select Text File", filetypes=[("Text Files", "*.txt")])

        if file_path:
            # Read file content
            with open(file_path, "r") as file:
                content = file.read()

            # Display file content in text area
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextReaderApp(root)
    root.mainloop()
