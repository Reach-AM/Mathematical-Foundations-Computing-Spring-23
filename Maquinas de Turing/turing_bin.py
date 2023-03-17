
class TuringMachine:
    # Definición de la Máquina de Turing:
    '''
        Pare este caso, tenemos que códificar
        los símbolos necesarios, por lo que
        0 -> 00
        1 -> 01
        # -> 10
        * -> 11
    '''
    delta = {}
    state = ''
    final = ''
    
    # Las otras dos partes de la máquina, es decir,
    # la cinta y la cabeza.
    tape = {}
    head = 0
   
    # Inicializamos la máquina de Turing con los
    # parámetros especificados
    def __init__(self, program, input, head = 0, qs=0, qf='H'):
        self.head = head
        self.state = str(qs)
        self.final = str(qf)

        for i,x in enumerate(input):
            self.tape[i] = x
        self.decode()

        for line in program.splitlines():
            if line[0] == '#': continue
            s, h, s1, w, d = line.split(' ')
            self.delta[s,h] = (s1, w, d)
    
    # Esta función se encarga de llevar a cabo cada
    # paso del programa, uno a la vez
    def step(self):
        if self.state != self.final:
            if self.head not in self.tape:
                self.tape[self.head] = '0'
            r = self.tape[self.head]
            action = self.delta[(self.state, r)]

            self.printTape(self.state)
            if action:
                s1, w, d = action
                self.tape[self.head] = w
                if d != '*':
                    self.head = self.head + (1 if d == 'R' else -1)
                self.state = s1

    # Esta función nos permite ver la cinta y la
    # cabeza de una manera más visual
    def printTape(self, s = ' '):
        sorted_keys = sorted(self.tape.keys())
        tape = ''
        for key in sorted_keys:
            if(key == self.head): tape+='['
            if(key == self.head+1): tape+=']'
            tape += self.tape[key]
        print(s,tape)
    
    # Esta función se encarga de decodificar
    # la cinta para tener un resultado más
    # legible
    def decode(self):
        sorted_keys = sorted(self.tape.keys())
        tape = ''
        for key in sorted_keys:
            if key % 2 == 0:
                if self.tape[key] == '0':
                    if self.tape[key+1] == '0':
                        tape += '0'
                    if self.tape[key+1] == '1':
                        tape += '1'
                if self.tape[key] == '1':
                    if self.tape[key+1] == '0':
                        tape += '#'
                    if self.tape[key+1] == '1':
                        tape += '*'
            else: continue
        print(tape)

    # Esta función ejecuta el programa cargado
    # en la Máquina de Turing
    def run(self, max=9999):
       i = 0
       # Prevenimos un loop infinito
       while self.state != 'H' and i < max:
           self.step()
           i += 1
       self.decode()

# Programa para hace suma Unaria:
#input = '*1111011*'
input = '110101010100010111'
program = open('bin_UnarySum.txt').read()

# Programa para hace suma Unaria:
#input = '*1010100*'
# input = '110100010001000011'
# program = open('bin_Complemento.txt').read()


tm = TuringMachine(program, input,2)
tm.run()