import matplotlib.pyplot as plt

def do_plot(x,y,title, x_ticks):
    
    fig, ax = plt.subplots()
    
    ax.plot(x,y)

    ax.set_xticks(range(0,x_ticks,1))
    ax.set_yticks(range(-1,2,1))
    plt.xticks(color="w")
    plt.title(title)

    ax.grid(True, linestyle="--", color="lightgray", alpha=0.7)
    plt.show()

def RNZL(a):
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

    do_plot(x, y, "non-return to zero level", len(a))

def RNZI(a):
    x = []
    y = []

    last_state = 0
    # 01001100011
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

    do_plot(x, y, "non-return to zero inverted", len(a))

def B_AMI(a):
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

    do_plot(x, y, "bipolar AMI", len(a))

def P_TER(a):
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

    do_plot(x, y, "bipolar AMI", len(a))

def MAN(a):
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

    do_plot(x, y, "Miunich", len(a))
    
def CD(a):
    x = []
    y = []
    
        
def main():
    a = [0,1,0,0,1,1,0,0,0,1,1]
    # RNZL(a)
    # RNZI(a)
    # B_AMI(a)
    # P_TER(a)
    MAN(a)
    
if __name__ == "__main__":
    main()