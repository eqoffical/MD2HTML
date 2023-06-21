import os
import markdown
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def convert_md_to_html(md_file, html_file):
    try:
        with open(md_file, 'r') as md:
            markdown_text = md.read()

        html = markdown.markdown(markdown_text)

        with open(html_file, 'w') as html_out:
            html_out.write(html)

        messagebox.showinfo("Conversion Complete", f"Markdown to HTML conversion is complete.\nHTML file saved as '{html_file}'")
    except Exception as e:
        messagebox.showerror("Conversion Failed", f"An error occurred during the conversion:\n\n{str(e)}")

def open_file():
    global html_path_var  # Declare html_path_var as a global variable
    md_file = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md")])
    if md_file:
        md_path_var.set(md_file)
        html_path_var = tk.StringVar()  # Create html_path_var as a new StringVar
        html_path_var.set(os.path.splitext(md_file)[0] + ".html")

def convert():
    md_file = md_path_var.get()
    html_file = os.path.splitext(md_file)[0] + ".html"
    
    if md_file:
        # Check if the HTML file already exists
        if os.path.exists(html_file):
            overwrite = messagebox.askyesno("File Already Exists", "The HTML file already exists.\nDo you want to overwrite it?")
            if not overwrite:
                return
        
        convert_md_to_html(md_file, html_file)

# Create the main window
root = tk.Tk()
root.title("Markdown to HTML Converter")

# Create and place the input file widgets
md_path_var = tk.StringVar()
md_label = tk.Label(root, text="Markdown File:")
md_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
md_entry = tk.Entry(root, textvariable=md_path_var, width=30)
md_entry.grid(row=0, column=1, padx=10, pady=10)
md_button = tk.Button(root, text="Browse", command=open_file)
md_button.grid(row=0, column=2, padx=10, pady=10)

# Create and place the convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=1, column=0, columnspan=3, pady=10)

# Run the GUI
root.mainloop()
