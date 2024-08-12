import tkinter as tk
from tkinter import ttk
import requests
from html.parser import HTMLParser

class Browser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Browser")
        self.geometry("800x600")

        # Create a frame for the address bar
        self.address_bar_frame = tk.Frame(self)
        self.address_bar_frame.pack(fill="x")

        # Create an entry field for the URL
        self.url_entry = tk.Entry(self.address_bar_frame, width=50)
        self.url_entry.pack(side="left", fill="x", expand=True)

        # Create a button to navigate to the URL
        self.go_button = tk.Button(self.address_bar_frame, text="Go", command=self.navigate)
        self.go_button.pack(side="left")

        # Create a frame for the web page
        self.web_page_frame = tk.Frame(self)
        self.web_page_frame.pack(fill="both", expand=True)

        # Create a text widget to display the web page
        self.web_page_text = tk.Text(self.web_page_frame)
        self.web_page_text.pack(fill="both", expand=True)

    def navigate(self):
        url = self.url_entry.get()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        response = requests.get(url)
        self.display_web_page(response.text)

    def display_web_page(self, html):
        self.web_page_text.delete(1.0, "end")
        self.web_page_text.insert("end", html)

if __name__ == "__main__":
    browser = Browser()
    browser.mainloop()
