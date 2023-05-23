import tkinter
from tkinter import ttk


class UI:
    screen = tkinter.Tk()
    entries = []

    screen.title("Testing")
    screen.geometry("600x200")
    screen.iconbitmap("fav-icon.png")

    def __init__(self):
        self.inputs = []

    def get_inputs_data(self, inputs):
        for entry_data in inputs:
            for key, value in entry_data.items():
                self.entries.append({key: value.get()})

        self.screen.quit()

    def fill_enries(self, entries):
        # TODO : change logic into this function
        ttk.Label(
            text="There is programm for booking.com. Goal of its just test form on the main page of booking.").pack()

        for entry_name in entries:
            print(entry_name)
            lable = ttk.Label(self.screen, text=entry_name)
            entry = ttk.Entry()

            self.inputs.append({entry_name: entry})

            lable.pack()
            entry.pack()

        submit_btn = ttk.Button(
            text="Submit", command=lambda: self.get_inputs_data(self.inputs))

        submit_btn.pack()

        self.screen.mainloop()

        return self.entries