import tkinter as tk
from tkinter import messagebox, ttk
import os

# Create a directory to store posts if it doesn't exist
if not os.path.exists("posts"):
    os.makedirs("posts")


class MiniBlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MiniBlog")
        self.root.geometry("500x600")

        # Name
        tk.Label(root, text="Name:").pack(pady=(10, 0))
        self.name_entry = tk.Entry(root, width=50)
        self.name_entry.pack()

        # Title
        tk.Label(root, text="Title:").pack(pady=(10, 0))
        self.title_entry = tk.Entry(root, width=50)
        self.title_entry.pack()

        # Content
        tk.Label(root, text="Content:").pack(pady=(10, 0))
        self.content_text = tk.Text(root, height=10, width=50)
        self.content_text.pack()

        # Buttons
        tk.Button(
            root,
            text="Save Post",
            command=self.save_post,
            bg="green",
            fg="white"
        ).pack(pady=5)

        tk.Button(
            root,
            text="Delete Post",
            command=self.delete_post,
            bg="red",
            fg="white"
        ).pack(pady=5)

        # Post selector
        tk.Label(root, text="Select Post:").pack(pady=(15, 0))
        self.post_listbox = ttk.Combobox(root, state="readonly", width=47)
        self.post_listbox.pack()
        self.post_listbox.bind("<<ComboboxSelected>>", self.load_post)

        self.refresh_post_list()

    def save_post(self):
        name = self.name_entry.get().strip()
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", tk.END).strip()

        if not name or not title or not content:
            messagebox.showerror("Error", "All fields are required!")
            return

        # Make filename safe
        safe_name = name.replace("/", "_").replace("\\", "_")
        safe_title = title.replace("/", "_").replace("\\", "_")

        filename = f"posts/{safe_name}_{safe_title}.txt"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)

            messagebox.showinfo("Success", "Post saved successfully!")
            self.refresh_post_list()

        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")

    def refresh_post_list(self):
        files = sorted(
            [f for f in os.listdir("posts") if f.endswith(".txt")]
        )

        self.post_listbox["values"] = files

    def load_post(self, event=None):
        filename = self.post_listbox.get()

        if not filename:
            return

        try:
            with open(f"posts/{filename}", "r", encoding="utf-8") as f:
                content = f.read()

            # Extract name and title from filename
            file_without_ext = filename[:-4]

            if "_" in file_without_ext:
                name, title = file_without_ext.split("_", 1)
            else:
                name = ""
                title = file_without_ext

            # Fill form fields
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)

            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, title)

            self.content_text.delete("1.0", tk.END)
            self.content_text.insert("1.0", content)

        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_post(self):
        filename = self.post_listbox.get()

        if not filename:
            messagebox.showwarning(
                "Warning",
                "Please select a post to delete."
            )
            return

        confirm = messagebox.askyesno(
            "Delete Post",
            f"Are you sure you want to delete:\n{filename}?"
        )

        if not confirm:
            return

        try:
            os.remove(f"posts/{filename}")

            messagebox.showinfo(
                "Success",
                "Post deleted successfully!"
            )

            # Clear fields
            self.name_entry.delete(0, tk.END)
            self.title_entry.delete(0, tk.END)
            self.content_text.delete("1.0", tk.END)

            self.post_listbox.set("")
            self.refresh_post_list()

        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Could not delete file:\n{e}"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = MiniBlogApp(root)
    root.mainloop()