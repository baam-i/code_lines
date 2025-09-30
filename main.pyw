import tkinter as tk

class App(tk.Tk):
  def __init__(self):
    super().__init__()

    # window settings
    self.geometry("400x300")
    self.title("code lines (by baamwiss)")

    # TODO: theme


if __name__ == "__main__":
  app = App()

  app.mainloop()