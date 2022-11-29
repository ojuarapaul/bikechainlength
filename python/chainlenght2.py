# calculador de tamanho de corrente

def main():
    chainstay = float(input('digite o tamanho do chainstain em polegadas, formato decimal - ex: 16.0, 17.5, 18.25 etc: '))
    largercog = int(input('digite o numero de dentes da maior catraca - ex: 42: '))
    chainring = int(input('digite o numero de dentes da sua maior - ou única - coroa - ex:30: '))
    a = (chainstay*2)
    b = (largercog/4)
    c = (chainring/4)
    chainLenght = a + b + c + 1
    start()
    
def start():
    inicio=input('\nVocê deseja o tamanho da corrente em cm [c] ou polegadas [p]?')
    if inicio==('c'):
        centimetros()
    elif inicio==('p'):
        polegadas()
        
def cont():
    brk=input ('\nDeseja continuar? Digite [n] para encerrar ou qualquer tecla para continuar -> ')
    if brk ==('n'):
        print('\nObrigado por usar nosso avançadíssimo sistema de conversão. Have a nice day.')
        print('Esse programa é dedicado a Sil & Teco, que me inspiram em tudo que eu invento.\n')
    else: main()   

def centimetros():
    lenghtCm = (chainLenght)*2.54
    lenghtResto=((lenghtCm)-int(lenghtCm))
    if lenghtResto < (0.50):
        chainLenghtCm = int(lenghtCm)
        print ('\nO tamanho da corrente é',chainLenghtCm,'cm')
    elif lenghtResto >= (0.50):
        chainLenghtCm = int(lenghtCm) + 1
        print ('\nO tamanho da corrente é',chainLenghtCm,'cm')
    print('Se você usa um MissingLink, inclua-o quando for medir a corrente.')
    cont()

def polegadas():
    lenghtResto1=((chainLenght)-int(chainLenght))
    if lenghtResto1 < (0.50):
        chainLenght = int(chainLenght)
        print ('\nO tamanho da corrente é',chainLenght,'polegadas')
    elif lenghtResto1 >= (0.50):
        chainLenght = int(chainLenght) + 1
        print ('\nO tamanho da corrente é',chainLenght,'polegadas')
    print('Se você usa um MissingLink, inclua-o quando for medir a corrente.')
    cont()
 
main()
