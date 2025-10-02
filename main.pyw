from plotter import Plotter, PlotAlgorithm

import sys
import os
import tkinter as tk
from tkinter import ttk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class PlotFrame(ttk.Frame):
  def __init__(self, root, plotter : Plotter, algorithm : PlotAlgorithm):
    super().__init__(root)

    self.plotter = plotter
    self.algorithm = algorithm
    
    self.fig = Figure(figsize=(10, 10), dpi=100)
    self.ax = self.fig.add_subplot()
    self.line, = self.ax.plot([], [])
    self.canvas = FigureCanvasTkAgg(self.fig, master=self)
    self.canvas.draw()
    self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

  def render(self, a):
    x, y, title = self.plotter.get_plot_data(a, self.algorithm)

    self.line.set_xdata(x)
    self.line.set_ydata(y)
    self.ax.set_xticks(range(0, len(a), 1))
    self.ax.set_yticks(range(-1, 2, 1))
    self.ax.tick_params(axis="x", labelcolor="w")
    self.ax.grid(True, linestyle="--", color="lightgray", alpha=0.7)
    self.ax.set_title(title)
    self.ax.relim()
    self.ax.autoscale_view()
    self.canvas.draw_idle()

class App(tk.Tk):
  def __init__(self):
    super().__init__()

    # window settings
    
    self.geometry("950x570")
    self.title("code lines (by baamwiss)")
    self.iconbitmap(default=self.resource_path("GATITO.ico"))

    # theme
    
    self.style = ttk.Style(self)
    self.style.theme_use("xpnative")
    #self.style.theme_use("winnative")

    self.top_container = ttk.Frame(self)
    self.top_container.pack(side="top", fill="x", expand=False, padx="10", pady="10")

    self.l_entry = ttk.Label(self.top_container, text="Entrada ")
    self.l_entry.pack(side="left")
    
    self.entry_text = tk.StringVar()
    self.entry_text.trace_add("write", self.on_entry_text_change)
    self.tb_entry = ttk.Entry(self.top_container, textvariable=self.entry_text)
    self.tb_entry.pack(side="left", fill="x", expand=True)

    self.main_container = ttk.Frame(self) # bg="blue"
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

    row_spacing = 2
    col_spacing = 2

    self.rnzl_plot = PlotFrame(self.main_container, self.plotter, PlotAlgorithm.RNZL)
    self.rnzl_plot.grid(row=0, column=0, pady=row_spacing, padx=col_spacing, sticky="nsew")
    self.rnzl_plot.render(self.input)
    self.plots.append(self.rnzl_plot)

    self.rnzi_plot = PlotFrame(self.main_container, self.plotter, PlotAlgorithm.RNZI)
    self.rnzi_plot.grid(row=0, column=1, pady=row_spacing, padx=col_spacing, sticky="nsew")
    self.rnzi_plot.render(self.input)
    self.plots.append(self.rnzi_plot)

    self.bami_plot = PlotFrame(self.main_container, self.plotter, PlotAlgorithm.BAMI)
    self.bami_plot.grid(row=0, column=2, pady=row_spacing, padx=col_spacing, sticky="nsew")
    self.bami_plot.render(self.input)
    self.plots.append(self.bami_plot)

    self.man_plot = PlotFrame(self.main_container, self.plotter, PlotAlgorithm.MAN)
    self.man_plot.grid(row=1, column=0, pady=row_spacing, padx=col_spacing, sticky="nsew")
    self.man_plot.render(self.input)
    self.plots.append(self.man_plot)

    self.pter_plot = PlotFrame(self.main_container, self.plotter, PlotAlgorithm.PTER)
    self.pter_plot.grid(row=1, column=1, pady=row_spacing, padx=col_spacing, sticky="nsew")
    self.pter_plot.render(self.input)
    self.plots.append(self.pter_plot)

    self.cd_plot = PlotFrame(self.main_container, self.plotter, PlotAlgorithm.CD)
    self.cd_plot.grid(row=1, column=2, pady=row_spacing, padx=col_spacing, sticky="nsew")
    self.cd_plot.render(self.input)
    self.plots.append(self.cd_plot)

  def is_valid_binary(self, text):
    if not text:
      return True
    
    for char in text:
      if char != '0' and char != '1':
        return False
      
    return True
  
  def on_entry_text_change(self, *args):
    text = self.entry_text.get()

    # only allow 0s and 1s
    if self.is_valid_binary(text) == False:
      self.entry_text.set(text[:-1])
      return

    self.input = [int(text[i]) for i in range(0, len(text))]

    for plot in self.plots:
      plot.render(self.input)

  def resource_path(self, relative_path):
    try:
      base_path = sys._MEIPASS
    except Exception:
      base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
  app = App()

  app.mainloop()