from plotter import Plotter, PlotAlgorithm

import tkinter as tk
from PIL import Image, ImageTk

class PlotFrame(tk.Frame):
  def __init__(self, root, plotter : Plotter, algorithm : PlotAlgorithm, bg : str):
    super().__init__(root, bg=bg)

    self.plotter = plotter
    self.algorithm = algorithm
    
    self.buffer = None
    self.image_raw = Image.new("RGBA", (100, 100), (0, 0, 0, 0))
    self.image = ImageTk.PhotoImage(image=self.image_raw)
    
    self.l_image = tk.Label(self, image=self.image)
    self.l_image.pack(side="top", fill="both", expand=True)

  def render(self, a):
    self.buffer = self.plotter.get_plot(a, self.algorithm)
    self.image_raw = Image.open(self.buffer)
    
    new_image = ImageTk.PhotoImage(self.image_raw)
    
    self.l_image.config(image=new_image)
    self.image = new_image

class App(tk.Tk):
  def __init__(self):
    super().__init__()

    # window settings
    self.geometry("950x570")
    self.title("code lines (by baamwiss)")
    self.iconbitmap("GATITO.ico")

    # TODO: theme

    self.top_container = tk.Frame(self)
    self.top_container.pack(side="top", fill="x", expand=False, padx="10", pady="10")

    self.l_entry = tk.Label(self.top_container, text="Entrada ")
    self.l_entry.pack(side="left")

    #validation_cmd = (self.register(self.validate_text), '%P')
    
    self.entry_text = tk.StringVar()
    self.entry_text.trace_add("write", self.on_entry_text_change)
    self.tb_entry = tk.Entry(self.top_container, textvariable=self.entry_text)
    self.tb_entry.pack(side="left", fill="x", expand=True)

    self.main_container = tk.Frame(self) # bg="blue"
    self.main_container.pack(side="top", fill="both", expand=True, padx="10", pady="0 10")
    self.main_container.grid_rowconfigure(0, weight=1)
    self.main_container.grid_rowconfigure(1, weight=1) 
    self.main_container.grid_columnconfigure(0, weight=1)
    self.main_container.grid_columnconfigure(1, weight=1)
    self.main_container.grid_columnconfigure(2, weight=1)

    # plotter frames
    
    self.plotter = Plotter()
    self.plots = []
    self.input = []

    self.rnzl_plot = PlotFrame(self.main_container, self.plotter, PlotAlgorithm.RNZL, "red")
    self.rnzl_plot.grid(row=0, column=0, sticky="nsew")
    self.rnzl_plot.render(self.input)
    self.plots.append(self.rnzl_plot)

    self.rnzi_plot = PlotFrame(self.main_container, self.plotter, PlotAlgorithm.RNZI, "red")
    self.rnzi_plot.grid(row=0, column=1, sticky="nsew")
    self.rnzi_plot.render(self.input)
    self.plots.append(self.rnzi_plot)

    self.bami_plot = PlotFrame(self.main_container, self.plotter, PlotAlgorithm.BAMI, "red")
    self.bami_plot.grid(row=0, column=2, sticky="nsew")
    self.bami_plot.render(self.input)
    self.plots.append(self.bami_plot)

    self.man_plot = PlotFrame(self.main_container, self.plotter, PlotAlgorithm.MAN, "red")
    self.man_plot.grid(row=1, column=0, sticky="nsew")
    self.man_plot.render(self.input)
    self.plots.append(self.man_plot)

    self.pter_plot = PlotFrame(self.main_container, self.plotter, PlotAlgorithm.PTER, "red")
    self.pter_plot.grid(row=1, column=1, sticky="nsew")
    self.pter_plot.render(self.input)
    self.plots.append(self.pter_plot)

    self.cd_plot = PlotFrame(self.main_container, self.plotter, PlotAlgorithm.CD, "red")
    self.cd_plot.grid(row=1, column=2, sticky="nsew")
    self.cd_plot.render(self.input)
    self.plots.append(self.cd_plot)

  # we should only allow binary 0s and 1s
  def is_valid_text(self, text):
    #print("validate! -> ", text)

    if not text:
      return True
    
    for char in text:
      if char != '0' and char != '1':
        return False
      
    return True
  
  def on_entry_text_change(self, *args):
    text = self.entry_text.get()

    if self.is_valid_text(text) == False:
      # self.entry_text.set(text[0:len(text) - 2])
      return

    self.input = [int(text[i]) for i in range(0, len(text))]

    for plot in self.plots:
      print(self.input, plot.algorithm)
      plot.render(self.input)

if __name__ == "__main__":
  app = App()

  app.mainloop()