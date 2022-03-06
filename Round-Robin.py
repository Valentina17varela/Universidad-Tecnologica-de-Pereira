
def findWaitng(process, n, burst, wordtime,quantum):
    memory_burst = [0] * n
    
    for i in range(n):
        memory_burst[i] = burst[i]
        
    t = 0
    
    
    while(1):
        done = True
        
        for i in range(n):
            
            if (memory_burst[i] > 0):
                done = False
                
                if (memory_burst[i] > quantum):
                    
                    t += quantum
                    
                    memory_burst[i] -= quantum
                
                else:
                    
                    t = t + memory_burst[i]
                    
                    wordtime[i] = t - burst[i]
                    
                    memory_burst[i] = 0
                    
                    
        if (done == True):
            break
        
        
def findAround(process, n, burst, wordtime, tab):
    for i in range(n):
        tab[i] = burst[i] + wordtime[i]


def findTime(process, n, burst, quantum):
    
    wordtime = [0] * n
    tab = [0] * n
    
    findWaitng(process, n, burst, wordtime, quantum)
    
    findAround(process, n, burst, wordtime, tab)
    
    print("Procesos tiempo de llegada","    Tiempo de rafaga","    tiempo de espera"
          "   Tiempo Ejecutado")
    total_wordTime= 0
    total_tab = 0
    
    for i in range(n):
        total_wordTime = total_wordTime + wordtime[i]
        total_tab = total_tab = tab[i]
        print(" ", i + 1, "\t\t", burst[i],
              "\t\t", wordtime[i], "\t\t",tab[i])
        
    print("Tiempo Aproximado de Espera = %.5f "%(total_wordTime/n))
    print("Timepo en Ciclos = %.5f"%(total_tab/n))
    
    
if __name__ == "__main__":
    quantum = 2
    n = 3
    proc = [1 , 2, 3]
    burst_time = [10, 5, 8]
    
    
    findTime(proc, n, burst_time, quantum)   
    
    
    
            