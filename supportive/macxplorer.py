import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

class FileBrowser:
    def __init__(self, root):
        self.root = root
        self.root.title("File Browser")
        self.current_path = os.path.expanduser("~")  # Start in the user's home directory
        self.selected_item = None

        # Create a listbox to display files and directories
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox.bind('<Double-Button-1>', self.open_selected_item)
        self.listbox.bind('<<ListboxSelect>>', self.update_selected_item)

        # Create a scrollbar for the listbox
        scrollbar = tk.Scrollbar(root)
        scrollbar.pack(side=tk.LEFT, fill=tk.BOTH)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        # Create buttons for copy, cut, rename
        self.copy_button = tk.Button(root, text="Copy", command=self.copy_item)
        self.copy_button.pack()
        self.cut_button = tk.Button(root, text="Cut", command=self.cut_item)
        self.cut_button.pack()
        self.rename_button = tk.Button(root, text="Rename", command=self.rename_item)
        self.rename_button.pack()

        # Create a preview label
        self.preview_label = tk.Label(root, text="Preview Here")
        self.preview_label.pack()

        # Create a button to change the current directory
        self.change_dir_button = tk.Button(root, text="Change Directory", command=self.change_directory)
        self.change_dir_button.pack()

        # Populate the listbox with initial directory contents
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in os.listdir(self.current_path):
            self.listbox.insert(tk.END, item)

    def open_selected_item(self, event):
        if self.selected_item:
            selected_item_path = os.path.join(self.current_path, self.selected_item)
            if os.path.isdir(selected_item_path):
                self.current_path = selected_item_path
                self.update_listbox()
            else:
                # Display a simple preview (you can enhance this for various file types)
                self.preview_label.config(text=f"Previewing: {self.selected_item}")

    def update_selected_item(self, event):
        if self.listbox.curselection():
            self.selected_item = self.listbox.get(self.listbox.curselection())

    def copy_item(self):
        if not self.selected_item:
            return

        src = os.path.join(self.current_path, self.selected_item)
        dest = filedialog.askdirectory(initialdir=self.current_path)

        if dest:
            dest = os.path.join(dest, self.selected_item)
            try:
                if os.path.isfile(src):
                    shutil.copy2(src, dest)
                elif os.path.isdir(src):
                    shutil.copytree(src, dest)
                self.update_listbox()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to copy: {str(e)}")

    def cut_item(self):
        if not self.selected_item:
            return

        src = os.path.join(self.current_path, self.selected_item)
        dest = filedialog.askdirectory(initialdir=self.current_path)

        if dest:
            dest = os.path.join(dest, self.selected_item)
            try:
                if os.path.isfile(src):
                    shutil.move(src, dest)
                elif os.path.isdir(src):
                    shutil.move(src, dest)
                self.update_listbox()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to cut: {str(e)}")

    def rename_item(self):
        if not self.selected_item:
            return

        new_name = simpledialog.askstring("Rename", f"Enter new name for {self.selected_item}:", parent=self.root)
        if new_name:
            src = os.path.join(self.current_path, self.selected_item)
            dest = os.path.join(self.current_path, new_name)
            try:
                os.rename(src, dest)
                self.update_listbox()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to rename: {str(e)}")

    def change_directory(self):
        new_dir = filedialog.askdirectory(initialdir=self.current_path)
        if new_dir:
            self.current_path = new_dir
            self.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileBrowser(root)
    root.mainloop()
