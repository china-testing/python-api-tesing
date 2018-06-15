from tkinter import *

class TempConverter(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        parent.title("Temperature Converter")
        self.grid(row=0, column=0, padx=80, pady=60)
        self.fahr = DoubleVar()
        self.fahr.set(32)
        self.cels = StringVar()
        self.refresh(0)
        self.create_widgets()
        
    def create_widgets(self):
        self.cels_lbl = Label(self, textvariable=self.cels)
        self.cels_lbl.grid(row=0, column=0, pady=30,
                           columnspan=2)
        self.f_lbl = Label(self, text="deg F:")
        self.f_lbl.grid(row=1, column=0, pady=10, sticky=E)
        self.f_scl = Scale(self, variable=self.fahr, to=500,
                           from_=-100, command=self.refresh,
                           length=400, orient=HORIZONTAL)
        self.f_scl.grid(row=1, column=1, padx=10, pady=10)
        self.quit = Button(self, text="Quit", padx=20,
                           pady=5, command=self.parent.quit)
        self.quit.grid(row=2, column=1, sticky=E, padx=10,
                       pady=30)

    def refresh(self, _):
        f = self.fahr.get()
        c = (5/9)*(f - 32)
        self.cels.set("{:.2f} deg C".format(c))

root = Tk()
gui = TempConverter(root)
root.mainloop()
