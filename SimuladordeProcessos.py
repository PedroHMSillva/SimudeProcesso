import copy

class SimuladordeProcessos:
    

    def execute(self, processos, quantum):
    

        
        procs = map(list, copy.deepcopy(processos))

        tempo_retorno_total = 0 
        tempo_resposta_total = 0
        tempo_espera_total = 0 

        tempo_inicio = processos[0][0]

        
        tempo_atual = tempo_inicio

        
        soma_duracao = 0

        
        num_processos = len(processos)

        while procs:
            
            while True:
            
                if procs[0][0] < tempo_atual or procs[0][0] == tempo_inicio:
                    break
                else:
                    
                    p = procs[0]
                    procs.pop(0)
                    procs.append(p)

            
            if -1 not in procs[0]:
                procs[0].append(-1) 
                tempo_resposta_total += tempo_atual - procs[0][0]

            
            if procs[0][1] <= quantum:
                tempo_atual += procs[0][1]
                tempo_retorno_total += tempo_atual - procs[0][0] 

                
                for index, proc in enumerate(procs):
                    if index != 0 and proc[0] < tempo_atual:
                        if tempo_atual - proc[0] >= quantum:
                            tempo_espera_total += quantum
                        else:
                            tempo_espera_total += tempo_atual - proc[0]

                procs.pop(0) 

            else:
                procs[0][1] -= quantum 

                tempo_atual += quantum 

                
                for index, proc in enumerate(procs):
                    if index != 0 and proc[0] < tempo_atual:
                        if tempo_atual - proc[0] >= quantum:
                            tempo_espera_total += quantum
                        else:
                            tempo_espera_total += tempo_atual - proc[0]

                
                p = procs[0]
                procs.pop(0)
                procs.append(p)


        
        tempo_retorno_medio = float(tempo_retorno_total) / num_processos

        
        tempo_resposta_medio = float(tempo_resposta_total) / num_processos

        
        tempo_espera_medio = float(tempo_espera_total) / num_processos

        
        tempo_retorno_medio = ("%.1f" % tempo_retorno_medio).replace('.', ',')
        tempo_resposta_medio = ("%.1f" % tempo_resposta_medio).replace('.', ',')
        tempo_espera_medio = ("%.1f" % tempo_espera_medio).replace('.', ',')

       
        return (tempo_retorno_medio, tempo_resposta_medio, tempo_espera_medio)