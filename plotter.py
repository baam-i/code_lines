import io
from enum import Enum
import matplotlib.pyplot as plt

class PlotAlgorithm(Enum):
    RNZL = 1,
    RNZI = 2,
    BAMI = 3,
    PTER = 4,
    MAN = 5,
    CD = 6

class Plotter:
    def __init__(self):
        pass

    def show_plot(self, x, y, title, x_ticks):
        p_width = 300
        p_height = 180
        dpi = 100

        fig, ax = plt.subplots(figsize=(p_width/dpi, p_height/dpi), dpi=dpi)

        ax.plot(x,y)

        ax.set_xticks(range(0,x_ticks,1))
        ax.set_yticks(range(-1,2,1))
        ax.grid(True, linestyle="--", color="lightgray", alpha=0.7)
        
        plt.xticks(color="w")
        plt.title(title)
        
        plt.show()

    def get_rnzl_plot_data(self, a):
        x = []
        y = []

        last_state = 0

        for i, valor in enumerate(a):
            if last_state == valor:
                x.append(i)
                y.append(valor)
            else:
                x.append(i)
                y.append(last_state)
                x.append(i)
                y.append(valor)

            last_state = valor

        x.append(len(a))
        y.append(last_state)

        return x, y, "NRZ-L"

    def get_rnzi_plot_data(self, a):
        x = []
        y = []

        last_state = 0
        
        for i, valor in enumerate(a):
            if valor == 1:
                x.append(i)
                y.append(last_state)
                x.append(i)
                y.append(not last_state)
                last_state = not last_state
            else:
                y.append(last_state)
                x.append(i)


        x.append(len(a))
        y.append(last_state)

        return x, y, "NRZ-I"

    def get_b_ami_plot_data(self, a):
        x = []
        y = []
        
        last_state = 0
        polaridad = -1
        # 01001100011
        for i, valor in enumerate(a):
            if valor == 1:        
                polaridad = -polaridad    
                x.append(i)
                y.append(last_state)            
                x.append(i)
                y.append(polaridad)

                last_state = polaridad
            else:
                x.append(i)
                y.append(last_state)
                x.append(i)
                y.append(0)

                last_state = 0


        x.append(len(a))
        y.append(last_state)

        return x, y, "B-AMI"

    def get_p_ter_plot_data(self, a):
        x = []
        y = []

        last_state = 1
        polaridad = -1
        
        for i, valor in enumerate(a):
            x.append(i)
            y.append(last_state)

            if valor == 0:        
                polaridad = -polaridad    
                            
                x.append(i)
                y.append(polaridad)

                last_state = polaridad
            else:
                x.append(i)
                y.append(0)

                last_state = 0

        x.append(len(a))
        y.append(last_state)

        return x, y, "P-TER"

    def get_man_plot_data(self, a):
        x = []
        y = []

        last_state = 1

        x.append(-0)
        y.append(last_state)

        for i, valor in enumerate(a):
            if valor == last_state:
                x.append(i)
                y.append(last_state)
                x.append(i)
                y.append(not last_state)

                last_state = not last_state
        
            i += 0.5  
            
            x.append(i)
            y.append(last_state)

            if 0:
                x.append(i)
                y.append(0)
            else:
                x.append(i)
                y.append(1)

            x.append(i)
            y.append(valor)
            
            last_state = valor

        x.append(len(a))
        y.append(last_state)

        return x, y, "Manchester"
        
    def get_cd_plot_data(self, a):
        x = []
        y = []

        last_state = 1
        
        for i, valor in enumerate(a):
            if valor == 0: # si es cero tenemobs dos transiciones en el mismo periodo :p
                x.append(i)
                y.append(last_state)
                
                last_state = not last_state # transicion del inicio
                x.append(i)
                y.append(last_state)
            else: 
                x.append(i)
                y.append(last_state)
                        
            i += 0.5  
            
            x.append(i)
            y.append(last_state)

            last_state = not last_state
            x.append(i)
            y.append(last_state)

            i += 0.5  

            x.append(i)
            y.append(last_state)

        return x, y, "Diferencial"
        
    def get_plot_data(self, a, algorithm : PlotAlgorithm):
        if algorithm == PlotAlgorithm.RNZL: return self.get_rnzl_plot_data(a)
        if algorithm == PlotAlgorithm.RNZI: return self.get_rnzi_plot_data(a)
        if algorithm == PlotAlgorithm.BAMI: return self.get_b_ami_plot_data(a)
        if algorithm == PlotAlgorithm.PTER: return self.get_p_ter_plot_data(a)
        if algorithm == PlotAlgorithm.MAN: return self.get_man_plot_data(a)
        if algorithm == PlotAlgorithm.CD: return self.get_cd_plot_data(a)

def main():
    a = [1,0,1,0,0,1,1,1,0,0,1]

    plotter = Plotter()
    
    x, y, title = plotter.get_p_ter_plot_data(a)


    plotter.show_plot(x, y, title, len(a))
    for i, b in enumerate(a):
        plotter.text(i+0.5, 1.2, str(b), ha='center')
    
if __name__ == "__main__":
    main()