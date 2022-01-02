import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class Sgf2Split:
    """Object to split the sgf file"""
    def __init__(self, file_path, path_dir, new_name, starting_number=1, length_number=2, player_white="White",
                 player_black="Black"):
        self.path_dir = path_dir
        self.new_name = new_name
        self.starting_number = starting_number
        self.length_number = length_number
        self.player_white = player_white
        self.player_black = player_black
        self.header = f"(;GM[1]FF[4]CA[UTF-8]AP[Inari Sgf_splitter 0.1]ST[2]RU[Japanese]SZ[19]KM[0.00]PW[{player_white}]PB[{player_black}]"

        with open(file_path, 'r') as f:
            self.sgf = f.read()
        self.variation = self.split()
        self.saving_new_file()

    def split(self):
        """Splitting the string of the sgf file and putting all the variation
        into self.variation"""
        # On travaille sur le sgf.
        variation = self.sgf.split("(;")
        del variation[0:2]
        return variation
        # self.number_variation = len(self.variation)

    def saving_new_file(self):
        """Saving all the new variation into a new file.sgf"""
        for i in self.variation:
            with open(f"{self.path_dir}/{self.new_name}{str(self.starting_number).zfill(self.length_number)}.sgf",
                      "w+") as new_f:
                new_f.write(self.header + "" + i + ")")
                self.starting_number += 1


class App(ttk.Frame):
    """Class object that start the app"""
    def __init__(self, master=None):
        master.title("Inari Sgf splitter, version 0.1")
        master.geometry("600x200")

        # s = tk.ttk.Style()
        # s.configure('My.TFrame', background='red') , style="My.TFrame"

        # Setting the frame with master as root (the Tk() obj). Sticky option doesn't work if no Tk() obj.
        super().__init__(master, relief="ridge", padding=10)
        self.grid(column=0, row=0, sticky="n, s, e, w")

        self.set_file()
        self.set_dir()

        self.new_name_label = tk.ttk.Label(self, text="Sgf_prefix:")
        self.new_name_label.grid(column=0, row=5)

        self.new_name_contents = tk.StringVar()
        self.new_name_contents.set("No new name")
        self.new_name_entry = tk.ttk.Entry(self, textvariable=self.new_name_contents)
        self.new_name_entry.grid(column=1, row=5)

        self.starting_number_label = tk.ttk.Label(self, text="Premier chiffre:")
        self.starting_number_label.grid(column=3, row=5)

        self.starting_number_contents = tk.StringVar()
        self.starting_number_contents.set("01")
        self.starting_number_entry = tk.ttk.Entry(self, textvariable=self.starting_number_contents)
        self.starting_number_entry.grid(column=4, row=5)

        self.start_process_button = tk.ttk.Button(self, text="Start splitting", command=self.start_process)
        self.start_process_button.grid(column=1, row=6)

        # Setting the parameter so that the windows and the frame are dynamic
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

    def start_process(self):
        Sgf2Split(self.pathfile.get(), self.path_save_dir.get(), self.new_name_entry.get(), int(self.starting_number_contents.get()))
        new = tk.Message(text="Fini!")
        new.grid()

    def set_file(self):
        """Function to set up all the button and label to ask the file
        with whom were are going to work."""
        # Setting up the instructions in case it is not clear.
        self.instruction = tk.ttk.Label(self, text="Please select the file:")
        self.instruction.grid(column=0, row=0, columnspan=2, sticky="n, s, e, w", padx=5, pady=5)

        # Setting up the Button with the filedialog option & the result in a Label
        self.pathfile = tk.StringVar()
        self.pathfile.set("No file selected")
        self.file_search = tk.ttk.Button(self, text="File:", command=self.find_file)
        self.file_search.grid(column=0, row=1, padx=5, pady=5)
        self.label_path = tk.ttk.Label(self, textvariable=self.pathfile, justify="center")
        self.label_path.grid(column=1, row=1, sticky="e, w", padx=5, pady=5)

    def set_dir(self):
        """Function to set up all the button and label to ask the directory
        were we are going to save all the file."""
        # Setting up the instructions for the directory in case it is not clear.
        self.instruction_dir = tk.ttk.Label(self, text="Please select the directory where we'll save the new sgf:")
        self.instruction_dir.grid(column=0, row=2, columnspan=2, sticky="n, s, e, w", padx=5, pady=5)

        # Setting up the Button to create a directory:
        self.path_save_dir = tk.StringVar()
        self.path_save_dir.set("No directory selected")
        self.dir_search = tk.ttk.Button(self, text="Save in:", command=self.find_dir)
        self.dir_search.grid(column=0, row=3, padx=5, pady=5)
        self.label_dir = tk.ttk.Label(self, textvariable=self.path_save_dir, justify="right")
        self.label_dir.grid(column=1, row=3, sticky=" e, w", padx=5, pady=5)

    def find_file(self):
        """ Function to ask the file that has to be work on."""
        try:
            self.pathfile.set(filedialog.askopenfilename())
        except ValueError:
            print("There is ValueError")
            pass

    def find_dir(self):
        """ Function to ask the file that has to be work on."""
        try:
            self.path_save_dir.set(filedialog.askdirectory())
        except ValueError:
            print("There is ValueError")
            pass


def main():
    root = tk.Tk()
    myapp = App(root)
    myapp.mainloop()


if __name__ == '__main__':
    main()
