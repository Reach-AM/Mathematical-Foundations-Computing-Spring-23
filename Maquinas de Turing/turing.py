
class TuringMachine:
    # Definición de la Máquina de Turing:
    '''
        Q: El número de estados está definido en delta
        ∑: Asumimos que sólo se aceptan '0's y '1's
        Γ: Asumimos que la cinta únicamente contiene
           ∑ U {'_'}
        ⊔: Asumimos que es el simbolo '_' ∈ Γ
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
    def __init__(self, program, input, qs=0, qf='H'):
        self.state = str(qs)
        self.final = str(qf)

        for i,x in enumerate(input):
            self.tape[i] = x

        for line in program.splitlines():
            if line[0] == '#': continue
            s, h, s1, w, d = line.split(' ')
            self.delta[s,h] = (s1, w, d)
    
    # Esta función se encarga de llevar a cabo cada
    # paso del programa, uno a la vez
    def step(self):
        if self.state != self.final:
            if self.head not in self.tape:
                self.tape[self.head] = '_'
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

    # Esta función ejecuta el programa cargado
    # en la Máquina de Turing
    def run(self, max=9999):
       i = 0
       # Prevenimos un loop infinito
       while self.state != 'H' and i < max:
           self.step()
           i += 1
       self.printTape()

# Programa para realizar el complemento:
#input = '11111111111111111111111111111111111111'
#program = open('complemento.txt').read()

# Programa para realizar una suma:
input = '10001_10'
program = open('suma.txt').read()

tm = TuringMachine(program, input)
tm.run()