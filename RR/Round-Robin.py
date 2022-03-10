from tabulate import tabulate
import matplotlib.pyplot as plt
from os import environ


def findWaitng(process, n, burst, wordtime,quantum):
    memory_burst = [0] * n
    intervalos = [[]  for i in range(len(process))]
    proceso = 0
    
    for i in range(n):
        memory_burst[i] = burst[i]
        
    t = 0
    

    
    while(1):
        done = True
        
        for i in range(n):
            
            if proceso > len(process) - 1:
                proceso = 0
            
            if (memory_burst[i] > 0):
                done = False
                
                if (memory_burst[i] > quantum):
                    
                    intervalos[proceso].append(t)
                    
                    t += quantum
                    
                    memory_burst[i] -= quantum
                    
                    intervalos[proceso].append(t)
                
                else:
                    
                    intervalos[proceso].append(t)
                    
                    t = t + memory_burst[i]
                    
                    intervalos[proceso].append(t)
                    
                    wordtime[i] = t - burst[i]
                    
                    memory_burst[i] = 0
                    
            proceso += 1        
                               
        if (done == True):
            return intervalos
        
        
def findAround(process, n, burst, wordtime, tab):
    for i in range(n):
        tab[i] = burst[i] + wordtime[i]



def grafica(intervalos):
    
    proceso = 0
    colores = ['','r','b','g']
    for i in intervalos:
        j = 0
        proceso += 1  
        while j <= len(i)-1:
            plt.scatter([i[j],i[j+1]],[proceso,proceso],color=colores[proceso])
            plt.text(i[j],proceso,i[j])
            plt.text(i[j+1],proceso,i[j+1])
            plt.plot([i[j],i[j+1]],[proceso,proceso],color=colores[proceso])
            j += 2    
    plt.ylabel("Procesos")  
    plt.show()
            
        



def findTime(process, n, burst, quantum):
    
    wordtime = [0] * n
    tab = [0] * n
    
    intervalos = findWaitng(process, n, burst, wordtime, quantum)
    
    findAround(process, n, burst, wordtime, tab)
    

    tab_proc = []
    tab_burst = []
    tab_wait = []
    tab_turn = []
    total_wordTime= 0
    total_tab = 0
    
    for i in range(n):
        total_wordTime = total_wordTime + wordtime[i]
        total_tab = total_tab + tab[i]
        tab_proc.append([i+1])
        tab_burst.append(burst[i])
        tab_wait.append(wordtime[i])
        tab_turn.append(tab[i])
        
    
    tabla = {"Processes": tab_proc, "Burst Time": tab_burst, "Waiting Time": tab_wait,"Turn-Around Time": tab_turn}
    
    print(tabulate(tabla, headers='keys', tablefmt='grid'))
        
    print("Tiempo Aproximado de Espera = %.5f "%(total_wordTime/n))
    print("Timepo en Ciclos = %.5f"%(total_tab/n))
    
    grafica(intervalos)
    
def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"    

    
if __name__ == "__main__":
    quantum = 2
    n = 3
    proc = []
    burst_time = []
    
    suppress_qt_warnings()
    print("con quantum = 2, e iteraciones(n) = 3, escoja valores para")
    print("Procesos (se toman como tiempo de llegada)")
    for i in range(n):
        entrada = int(input("proceso: "))
        proc.append(entrada)
    print("\n\n")
    print("Burst time")
    for i in range(n):
        entrada = int(input("burst: "))
        burst_time.append(entrada)
        
    findTime(proc, n, burst_time, quantum)   

    
    
    
            