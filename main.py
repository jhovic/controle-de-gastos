
import os
from time import sleep

valor_conta = 0
nova_conta = 0



def pause():
    os.system('pause')
    

while True:
    print('-------------------------------')
    print('CONTROLE DE GASTOS')
    print('-------------------------------')
    print("1 - Inserir conta")
    print("2 - Inserir pagamento")
    print("3 - Total devido")
    
    print("0 - Sair")
    print('-------------------------------')

    var_menu = int(input("Digite um valor: "))

    if var_menu == 1:
        nova_conta = int(input("Qual o valor?"))
        print('-------------------------------')
        print("voce inseriu uma conta")
        print('-------------------------------')
        sleep(1)
        pause()
        valor_conta = int(valor_conta) + int(nova_conta)
    
    if var_menu == 2:
        print('-------------------------------')
        print("voce pagou uma conta")
        print('-------------------------------')
        sleep(1)
        pause()
        
    if var_menu == 3:
        print('-------------------------------')
        print("O total devido é: ")
        print(valor_conta)
        print('-------------------------------')
        sleep(1)
        pause()
        
    
    if var_menu == 0:
        break
    



    
