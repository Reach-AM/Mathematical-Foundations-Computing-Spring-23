import math
import matplotlib.pyplot as plt

# Lista de todas las combinaciones posibles de dos digitos en 
# hexadecimal, que representan la agrupación de 8 bits o 1 byte.
# E.g. 00 = 0000 0000, 01 = 0000 0001, 02 = 0000 0010
#      ...
#      FE = 1111 1110, FF = 1111 1111.

hex_chars = [format(i, 'x') for i in range(16)]
bytes_arr = []
for i in range(len(hex_chars)):
    for j in range(len(hex_chars)):
        bytes_arr.append(hex_chars[i]+hex_chars[j])

# Función para extraer los datos de un archivo, exrtraidos en binario
# y guardados en una lista por cada byte de información.
# E.g. Hola Mundo! -> 01001000 01101111 01101100 01100001 00100000
#                     01001101 01110101 01101110 01100100 01101111
#                     00100001 -> 48 6F 6C 61 20 4D 75 6E 64 6F 21

def extract_data(file):
    f = open(file, 'rb')
    bin = f.read().hex()
    f.close()
    return [bin[i:i+2] for i in range(0, len(bin), 2)]

# Función para calcular la Entropía (H) de Shannon en la información

def shannon(file, data):
    print(data)
    # Creamos un array con 256 espacios en 0. Aquí se guardará la
    # cantidad que se repite cada elemento de la combinación de bytes

    bytes_prob = [0] * len(bytes_arr)
    for b in data:
        bytes_prob[bytes_arr.index(b)] += 1

    # Eliminamos los valores de 0, pues significa que no tienen ninguna 
    # probabilidad de aparecer, por lo que no aportan información.
    
    while bytes_prob.count(0) > 0:
        rm = bytes_prob.index(0)
        bytes_prob.pop(rm)
        bytes_arr.pop(rm)

    # Calculamos la probabilidad de cada byte de aparecer dividiendo el
    # número de sus ocurrencias entre la cantidad total de bytes en la
    # fuente de información.

    for bp in range(len(bytes_prob)):
            bytes_prob[bp] /= len(data)

    # Calculamos la entropía de la fuente, utilizando la formula de Shannon:
    #                  n
    #           H(f) = Σ   p(x_i) * log_2 [p(x_i)]
    #                i = i 

    entropy = 0
    for bp in bytes_prob:
        entropy += bp * math.log2(1/bp)

    # Bar Plot of the frequencies of each byte, only with the bytes that
    # have a probability > 0.

    plt.figure(figsize=(len(bytes_prob)*0.115,4))
    plt.bar(range(len(bytes_prob)), bytes_prob)

    plt.xticks(range(len(bytes_prob)), bytes_arr, rotation = 90, fontsize = 6)
    plt.yticks(fontsize = 8)
    plt.xlabel('Byte', fontsize = 8)
    plt.ylabel('Probability', fontsize = 8)
    plt.title('Entropía en ' + file.split('.', 1)[0])
    plt.subplots_adjust(left=0.08, right=0.98, bottom=0.115, top=0.915)
    plt.margins(0.01)
    plt.show()

    return entropy

file = 'fmc2.txt'
bin = extract_data(file)
print(shannon(file, bin))