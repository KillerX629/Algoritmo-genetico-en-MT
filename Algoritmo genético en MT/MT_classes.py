


class maquinaDeTuring():
    def __init__(self):
        self.cinta = []
        self.posicion = 0
        self.estado = 0

    def iniciarCinta(self,cinta):
        self.cinta = cinta
    
    def leerCinta(self):
        return self.cinta[self.posicion]
    
    def escribirCinta(self,valor):
        self.cinta[self.posicion] = valor

    def cambiarEstado(self,stateChange):
        #stateChange =(ValorAEscribir, Direccion, Estado)
        self.escribirCinta(stateChange[0])
        self.posicion += stateChange[1]
        self.estado = stateChange[2]

    #anatomia de estados de transición: [estado, dirección, valor, nuevo estado]
    #cinta ejemplo: [P,n,n,n,n,n,F]


    #estados de transición:[q0,0]=[0,R,q1]
    #explicación: si está en el estado q0, y lee un 0, deja el 0, se mueve a la derecha y cambia de estado a q1

    def estadosDeTransicion(self):
        """el match es un switch de estados de transición, dentro de cada estado de transición hay que
        definir que pasa cuando se lee un valor"""
        match self.estado:
            case 0:
                esEntero = isinstance(self.leerCinta(),int)
                match esEntero:
                    case True:
                        #si lee un entero, esa posición en la cinta tiene un individuo
                        pass
                    case False:
                        #si lee una letra, esa posición en la cinta tiene un caracter especial
                        pass

            
            case _:
                print("Error: estado no reconocido")







"""
class Tape(object):
    
    blank_symbol = " "
    
    def __init__(self,
                 tape_string = ""):
        self.__tape = dict((enumerate(tape_string)))
        # last line is equivalent to the following three lines:
        #self.__tape = {}
        #for i in range(len(tape_string)):
        #    self.__tape[i] = input[i]
        
    def __str__(self):
        s = ""
        min_used_index = min(self.__tape.keys()) 
        max_used_index = max(self.__tape.keys())
        for i in range(min_used_index, max_used_index):
            s += self.__tape[i]
        return s    
   
    def __getitem__(self,index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        self.__tape[pos] = char 

        
class TuringMachine(object):
    
    def __init__(self, 
                 tape = "", 
                 blank_symbol = " ",
                 initial_state = "",
                 final_states = None,
                 transition_function = None):
        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__blank_symbol = blank_symbol
        self.__current_state = initial_state
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)
        
    def get_tape(self): 
        return str(self.__tape)
    
    def step(self):
        char_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, char_under_head)
        if x in self.__transition_function:
            y = self.__transition_function[x]
            self.__tape[self.__head_position] = y[1]
            if y[2] == "R":
                self.__head_position += 1
            elif y[2] == "L":
                self.__head_position -= 1
            self.__current_state = y[0]

    def final(self):
        if self.__current_state in self.__final_states:
            return True
        else:
            return False

"""

