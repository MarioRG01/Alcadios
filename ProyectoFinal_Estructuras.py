
#Integrantes del equipo: Ximena Muñoz - Oscar Durán - Mario Rodríguez

from sys import maxsize #número muy grande (infinito)
from random import randint

class Node(object):
    def __init__(self, i_depth, i_playerNum, i_beansRemaining, i_value = 0):
        self.i_depth = i_depth #la profundidad del arbol en la que nos encontramos (disminuye con cada iteración)
        self.i_playerNum = i_playerNum #(+1 or -1)
        self.i_beansRemaining = i_beansRemaining #cantidad de beans que quedan
        self.i_value = i_value #estado del juego: -inf, 0 or +inf
        self.children = []
        self.CreateChildren()
        
    def CreateChildren(self):
        if self.i_depth >= 0: #Si hemos pasado de la profunidad 0 se detiene
            for i in range (1, 4): #Cantidad de beans que se van a quitar
                v = self.i_beansRemaining - i
                self.children.append(Node(self.i_depth - 1,-self.i_playerNum, v, self.RealVal(v))) #Se agrega a la lista de hijos, disminuye la profunidad, cambio de jugador
    
    def RealVal(self, value):
        if (value == 0):
            return maxsize * self.i_playerNum #e.g. bullybot
        elif (value < 0):
            return maxsize * -self.i_playerNum #this bot
        return 0

def MinMax(node, i_depth, i_playerNum):
    if (i_depth == 0) or (abs(node.i_value) == maxsize): #Encontramos la profunidad 0 o la mejor opción?
        return node.i_value #Pasar el mejor nodo a el nodo actual
    
    i_bestValue = maxsize * -i_playerNum #Jugador Postivo
    
    for i in range(len(node.children)):
        child = node.children[i]
        i_val = MinMax(child, i_depth - 1, -i_playerNum)
        if (abs(maxsize * i_playerNum - i_val) < abs(maxsize * i_playerNum - i_bestValue)):
            i_bestValue = i_val #Encontrar y guardar el mejor valor en esta variable
            
    
    return i_bestValue
 
def WinCheck(i_beans, i_playerNum):
    if i_beans <= 0:
        print ("*"*30)
        if i_playerNum > 0:
            if i_beans == 0:
                print ("\t¡Tú ganaste!")
            else:
                print ("\t¡Demasiados Frijoles, tú perdiste!")
        else:
            if i_beans == 0:
                print ("\t¡La computadora ganó!")
            else:
                print ("\tLa computadora la regó")
        print ("*"*30)
        return 0
    return 1

def WinCheck2(i_beans, i_playerNum):
    if i_beans <= 0:
        print ("*"*30)
        if i_playerNum > 0:
            if i_beans == 0:
                print ("\t¡La computadora 1 ganó")
            else:
                print ("\t¡Demasiados Frijoles, tú perdiste!")
        else:
            if i_beans == 0:
                print ("\t¡La computadora 2 ganó!")
            else:
                print ("\tLa computadora la regó")
        print ("*"*30)
        return 0
    return 1

def WinCheck404(i_beans, i_playerNum):
    if i_beans <= 0:
        print ("*"*30)
        if i_playerNum > 0:
            if i_beans == 0:
                print ("\tEntra para ver los resultados...:")
            else:
                print ("\tEntra para ver los resultados...: ")
        else:
            if i_beans == 0:
                print ("\tEntra para ver los resultados...: ")
            else:
                print ("\tEntra para ver los resultados...: ")
        print ("*"*30)
        return 0
    return 1       



if __name__ == '__main__':
        print ("Instrucciones: Elige con cuantos frijoles quieres iniciar (21-25). Elige la cantidad de frijoles que quieres retirar del montón, el jugador que tome el/los último/s frijol/es dejando 0 en el montón, gana")
        i_beanTotal = randint(21,25)
        i_depth = 4
        i_curPlayer = 1
        print ("1-Juegas o 2-Bot?")
        juego = int(input ())
    
        if juego == 1:
          dificultad = int(input("Escoja la dificultad de la IA: "))
          while (i_beanTotal > 0):
                ## TURNO HUMANO
                print ("\n%d beans remain. How many will you pick up?" %i_beanTotal)
                i_choice = int(input("\n1, 2 or 3:                 "))
                if ((i_choice >0 and i_choice<4)):   
                  if ((dificultad > 0 and dificultad < 50)):  
                     i_beanTotal -= int(float(i_choice)) #Guardar la decisión del usuario
                      ## Turno de la computadora
                     if WinCheck(i_beanTotal, i_curPlayer):
                        i_curPlayer *= -1
                        node = Node(i_depth, i_curPlayer, i_beanTotal)
                        bestChoice = -100
                        i_bestValue = -i_curPlayer * maxsize
                        ## Determinar el número de frijoles a quitar
                        for i in range(len(node.children)):
                            n_child = node.children[i]
                            i_val = MinMax(n_child, i_depth, -i_curPlayer)
                            if (abs(i_curPlayer * maxsize - i_val) <= 
                                abs(i_curPlayer * maxsize - i_bestValue)):
                                i_bestValue = i_val
                                bestChoice = i
                        bestChoice = randint(1,3)
                        print ("Comp chooses: " +str(bestChoice) + "\tBased on value: " +str(i_bestValue))
                        i_beanTotal -= bestChoice
                        WinCheck(i_beanTotal, i_curPlayer)
                        i_curPlayer *= -1 #cambiar jugador
                        
                  elif((dificultad > 50 and dificultad < 100)):
                     i_beanTotal -= int(float(i_choice)) #Guardar la decisión del usuario
                      ## Turno de la computadora
                     if WinCheck(i_beanTotal, i_curPlayer):
                        i_curPlayer *= -1
                        node = Node(i_depth, i_curPlayer, i_beanTotal)
                        bestChoice = -100
                        i_bestValue = -i_curPlayer * maxsize
                        ## Determinar el número de frijoles a quitar
                        for i in range(len(node.children)):
                            n_child = node.children[i]
                            i_val = MinMax(n_child, i_depth, -i_curPlayer)
                            if (abs(i_curPlayer * maxsize - i_val) <= 
                                abs(i_curPlayer * maxsize - i_bestValue)):
                                i_bestValue = i_val
                                bestChoice = i
                        bestChoice += 1
                        print ("Comp chooses: " +str(bestChoice) + "\tBased on value: " +str(i_bestValue))
                        i_beanTotal -= bestChoice
                        WinCheck(i_beanTotal, i_curPlayer)
                        i_curPlayer *= -1 #cambiar jugador

                  elif(dificultad == 404):
                     i_beanTotal -= int(float(i_choice)) #Guardar la decisión del usuario
                      ## Turno de la computadora
                     if WinCheck404(i_beanTotal, i_curPlayer):
                        i_curPlayer *= -1
                        node = Node(i_depth, i_curPlayer, i_beanTotal)
                        bestChoice = -100
                        i_bestValue = -i_curPlayer * maxsize
                        ## Determinar el número de frijoles a quitar
                        for i in range(len(node.children)):
                            n_child = node.children[i]
                            i_val = MinMax(n_child, i_depth, -i_curPlayer)
                            if (abs(i_curPlayer * maxsize - i_val) <= 
                                abs(i_curPlayer * maxsize - i_bestValue)):
                                i_bestValue = i_val
                                bestChoice = i
                        bestChoice += 1
                        print ("Comp chooses: " +str(bestChoice) + "\tBased on value: " +str(i_bestValue))
                        i_beanTotal -= bestChoice
                        WinCheck404(i_beanTotal, i_curPlayer)
                        i_curPlayer *= -1 #cambiar jugador

                else:
                    print("Número de frijoles invalido")

          
        elif juego == 2:
            dificultad = int(input("Elija la dificultad de los bots: "))
            while (i_beanTotal > 0):
                ## Comp 1
                print ("\n%d beans remain. How many will you pick up?" %i_beanTotal)
                if (dificultad > 50):
                  if WinCheck2(i_beanTotal, i_curPlayer):
                        i_curPlayer *= -1
                        node = Node(i_depth, i_curPlayer, i_beanTotal)
                        bestChoice = -100
                        i_bestValue = -i_curPlayer * maxsize
                        ## Determinar el número de frijoles a quitar
                        for i in range(len(node.children)):
                            n_child = node.children[i]
                            i_val = MinMax(n_child, i_depth, -i_curPlayer)
                            if (abs(i_curPlayer * maxsize - i_val) <= 
                                abs(i_curPlayer * maxsize - i_bestValue)):
                                i_bestValue = i_val
                                bestChoice = i
                        bestChoice += 1
                        print ("Comp chooses: " +str(bestChoice) + "\tBased on value: " +str(i_bestValue))
                        i_beanTotal -= bestChoice
                        WinCheck2(i_beanTotal, i_curPlayer)
                        i_curPlayer *= -1 #cambiar jugador            "))

                
                ## Comp 2
                  if WinCheck2(i_beanTotal, i_curPlayer):
                      i_curPlayer *= -1
                      node = Node(i_depth, i_curPlayer, i_beanTotal)
                      bestChoice = -100
                      i_bestValue = -i_curPlayer * maxsize
                      ## Determinar el número de frijoles a quitar
                      for i in range(len(node.children)):
                         n_child = node.children[i]
                         i_val = MinMax(n_child, i_depth, -i_curPlayer)
                         if (abs(i_curPlayer * maxsize - i_val) <= 
                             abs(i_curPlayer * maxsize - i_bestValue)):
                             i_bestValue = i_val
                             bestChoice = i
                      bestChoice += 1
                      print ("Comp chooses: " +str(bestChoice) + "\tBased on value: " +str(i_bestValue))
                      i_beanTotal -= bestChoice
                      WinCheck2(i_beanTotal, i_curPlayer)
                      i_curPlayer *= -1 #cambiar 

                elif(dificultad < 50):
                  if WinCheck2(i_beanTotal, i_curPlayer):
                        i_curPlayer *= -1
                        node = Node(i_depth, i_curPlayer, i_beanTotal)
                        bestChoice = -100
                        i_bestValue = -i_curPlayer * maxsize
                        ## Determinar el número de frijoles a quitar
                        for i in range(len(node.children)):
                            n_child = node.children[i]
                            i_val = MinMax(n_child, i_depth, -i_curPlayer)
                            if (abs(i_curPlayer * maxsize - i_val) <= 
                                abs(i_curPlayer * maxsize - i_bestValue)):
                                i_bestValue = i_val
                                bestChoice = i
                        bestChoice = randint(1,3)
                        print ("Comp chooses: " +str(bestChoice) + "\tBased on value: " +str(i_bestValue))
                        i_beanTotal -= bestChoice
                        WinCheck2(i_beanTotal, i_curPlayer)
                        i_curPlayer *= -1 #cambiar jugador            "))

                
                ## Comp 2
                  if WinCheck2(i_beanTotal, i_curPlayer):
                      i_curPlayer *= -1
                      node = Node(i_depth, i_curPlayer, i_beanTotal)
                      bestChoice = -100
                      i_bestValue = -i_curPlayer * maxsize
                      ## Determinar el número de frijoles a quitar
                      for i in range(len(node.children)):
                         n_child = node.children[i]
                         i_val = MinMax(n_child, i_depth, -i_curPlayer)
                         if (abs(i_curPlayer * maxsize - i_val) <= 
                             abs(i_curPlayer * maxsize - i_bestValue)):
                             i_bestValue = i_val
                             bestChoice = i
                      bestChoice = randint(1,3)
                      print ("Comp chooses: " +str(bestChoice) + "\tBased on value: " +str(i_bestValue))
                      i_beanTotal -= bestChoice
                      WinCheck2(i_beanTotal, i_curPlayer)
                      i_curPlayer *= -1 #cambiar 