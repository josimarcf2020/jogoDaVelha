import random

def velha():
    print("       |       |       ")
    print("   1   |   2   |   3   ")
    print("       |       |       ")
    print("-------+-------+-------")
    print("       |       |       ")
    print("   4   |   5   |   6   ")
    print("       |       |       ")
    print("-------+-------+-------")
    print("       |       |       ")
    print("   7   |   8   |   9   ")
    print("       |       |       ")
    print()
    

def jogando(j):
    print("       |       |       ")
    print("   "+j[0]+"   |   "+j[1]+"   |   "+j[2]+"   ")
    print("       |       |       ")
    print("-------+-------+-------")
    print("       |       |       ")
    print("   "+j[3]+"   |   "+j[4]+"   |   "+j[5]+"   ")
    print("       |       |       ")
    print("-------+-------+-------")
    print("       |       |       ")
    print("   "+j[6]+"   |   "+j[7]+"   |   "+j[8]+"   ")
    print("       |       |       ")
    

velha()


while True:
    
    resp = input("Vamos jogar uma partidinha(S/N)?")

    if(resp == "N" or resp =="n"):
        print("Obrigado pela companhia... Não tarde a voltar! Bye")
        break
    else:
        print()
        print("Meu jogo, minhas regras... Eu começo!")   

        jogadas = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        comp = random.randrange(1, 9, 1)-1
        
        jogadas[comp] = "X"
        
        jogando(jogadas) 
        
        print()   
        
        pos = input("Sua vez! Informe uma posição para jogar...")
        
        while True:
            if(pos in jogadas):
                break
            print("Posição INVÁLIDA")
            pos = input("Informe uma NOVA posição para jogar...")
    
        jogadas[int(pos)-1] = "O"
        
        jogando(jogadas)
    
    