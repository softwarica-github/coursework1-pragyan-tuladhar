import requests
from tkinter import *
from tkinter import messagebox
from urllib.parse import urlparse
from tkinter import filedialog
import unittest
from unittest.mock import patch, Mock


def enumerate_website():
    url = url_entry.get()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response_text = response.text
            # Perform desired web enumeration tasks here
            result_text.delete(1.0, END)  # Clear previous results
            result_text.insert(END, response_text)
        else:
            messagebox.showerror("Error", "Unable to retrieve data from the website.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", str(e))


def file():
    output = "This is a file menu.\n"


def save(result):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(result)
                message_box1("Save", "Result saved successfully.")
        except Exception as e:
            message_box2("Error", "Error occurred while saving the result.")
    else:
        message_box3("Save", "Save operation canceled.")


def message_box1(title, message):
    messagebox.showinfo("", f"Result saved successfully.")


def message_box2(title, message):
    messagebox.showinfo("", f"Error occurred while saving the result.")


def message_box3(title, message):
    messagebox.showinfo("", f"Save operation cancelled.")


def helps():
    messagebox.showinfo("Help", "This program performs web enumeration to gather information about a target website.\n\nInstructions:\n1. Enter the target URL in the input field.\n2. Click the 'Start Enumeration' button to initiate the enumeration process.\n3. The program will gather information such as subdomains, open ports, and directory listings.\n4. The results will be displayed in the output area.\n\nFor any questions or support, please refer to the documentation or contact our support team.")


def exits():
    root.destroy()


def information_gathering():
    url = url_entry.get()
    parsed_url = urlparse(url)
    result_text.delete(1.0, END)  # Clear previous results
    result_text.insert(END, "Information Gathering:\n")
    result_text.insert(END, "Scheme: " + parsed_url.scheme + '\n')
    result_text.insert(END, "Netloc: " + parsed_url.netloc + '\n')
    result_text.insert(END, "Path: " + parsed_url.path + '\n')
    result_text.insert(END, "Params: " + parsed_url.params + '\n')
    result_text.insert(END, "Query: " + parsed_url.query + '\n')
    result_text.insert(END, "Fragment: " + parsed_url.fragment + '\n')


class WebEnumerationTool(unittest.TestCase):
    def Test_Enum_success(self):
        with patch(requests.get) as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.text = "Success"
            mock_get.return_value = mock_response

            url_entry.insert(0, url_entry.get())
            enumerate_website()
            self.assertEqual(result_text.get(1.0, END), "Success\n")

    def test_enum_failure(self):
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 404
            mock_get.return_value = mock_response

            url_entry.insert(0, url_entry.get())
            enumerate_website()

            self.assertEqual(result_text.get(1.0, END), "")


if __name__ == '__main__':
    unittest.main()


# main window
root = Tk()
root.title("Web Enumeration Tool")

# Menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=lambda: save("Enumeration result"))
menu_bar.add_command(label="Help", command=helps)
menu_bar.add_command(label="Exit", command=exits)


# Labels
Label(text="WEB ENUMERATION TOOL", fg="blue", font=("Sans Serif", 32, "bold")).pack()

# URL entry field
url_label = Label(root, text="URL:")
url_label.pack()
url_entry = Entry(root)
url_entry.pack()

# Enumerate button
enumerate_button = Button(root, text="Enumerate", command=enumerate_website)
enumerate_button.pack()

# Result text box
result_label = Label(root, text="Result:")
result_label.pack()
result_text = Text(root)
result_text.pack()

# Scrollbar for the result text box
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
result_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=result_text.yview)

# Radio buttons
var = IntVar()

radio_frame = Frame(root)
radio_frame.pack()

Label(text="Enumeration Type:").pack(anchor=S)
Radiobutton(text="Information Gathering", variable=var, value=2, command=information_gathering).pack()


root.mainloop()
