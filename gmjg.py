#Personagens do jogo
personagem={"Dennis Dj": {"Poder de ataque":15,
                          "Nível de defesa":5,
                          "Pontos de vida":100},
            "Kaique Fogo no Rabo":{"Poder de ataque":20,
                                   "Nível de defesa":8,
                                  "Pontos de vida":40},
            "TyranaRafa":{"Poder de ataque":18,
                          "Nível de defesa":10,
                          "Pontos de vida":50},
            "Arielda99":{"Poder de ataque":8,
                         "Nível de defesa":6,
                         "Pontos de vida":35},
            "VAI THOMAS":{"Poder de ataque":25,
                         "Nível de defesa":6,
                         "Pontos de vida":45},
            "Mano Hugo":{"Poder de ataque":18,
                        "Nível de defesa":7,
                        "Pontos de vida":48},
            "Renan Descartes":{"Poder de ataque":11,
                               "Nível de defesa":6,
                               "Pontos de vida":45}}
            
import random
import os
clear = lambda: os.system('cls')

def batalha(seupersonagem,adversario):
    from random import randint
    ataquead=personagem[adversario]["Poder de ataque"]     
    ataqueseu=personagem[seupersonagem]["Poder de ataque"] 
    defesaad=personagem[adversario]["Nível de defesa"]
    defesaseu=personagem[seupersonagem]["Nível de defesa"] 
    vidaad=personagem[adversario]["Pontos de vida"]
    vidaseu=personagem[seupersonagem]["Pontos de vida"]

    while vidaad>0 and vidaseu>0:
        lucky_factor=randint(1,3)
        if lucky_factor==1:
            vidaad=vidaad-(ataqueseu-defesaad*0.8)
        if lucky_factor==2:
            vidaad=vidaad-(ataqueseu*1.2-defesaad) 
        if lucky_factor==3:          
            vidaad=vidaad-(ataqueseu-defesaad)
        
        if vidaad<=0:
            resultado="\n   Parabéns, seu {} venceu a batalha contra {}".format(seupersonagem,adversario)
            
        lucky_factor=randint(1,3)    
        if lucky_factor==1:
            vidaseu=vidaseu-(ataquead-defesaseu*0.8)
        if lucky_factor==2:
            vidaseu=vidaseu-(ataquead*1.2-defesaseu)
        if lucky_factor==3:
            vidaseu=vidaseu-(ataquead-defesaseu)
        
        if vidaseu<=0:
            resultado="\n   Poxa vida,seu {} perdeu a batalha para {}. Ele irá se recuperar em poucos segundos".format(seupersonagem,adversario)
            
    return resultado
'''
def batalha_usuarios(usuario,jogadorad):

  return
'''

def Insperdex (adversario):
    achado=""
    if adversario not in insperdex:
        insperdex.append(adversario)
        achado="\n\n        {} nunca havia sido visto mas agora foi adicionado a sua Insperdex".format(adversario)
    return achado
'''
def salvar ():

    return
'''


clear()
print("\n\nOlá, seja bem vindo ao Inspermon !\n\n")
while True:
    while True:
        seupersonagem=str(input("Escolha um Inspermon para começar sua jornada: "))   #escolha do jogador
        if seupersonagem in personagem:
            print("\n  Pronto agora só jogar\n")
            insperdex=[seupersonagem]
            break
        else:
            print("\nEsse inspermon não existe...\n") 
            continue
           
    while True:
        menu="\n\nMenu Inicial:\n   1-JOGAR\n   2-INSPERDEX\n   3-SAIR\n\n"
        menu_choice=int(input(menu))   
        clear()
        if menu_choice==1:
            while True:
                
                escolha=str(input("\nVocê deseja passear ou dormir?  "))
                if escolha=="Passear" or escolha=="passear" or escolha=="PASSEAR":
                    adversario= random.choice(list(personagem.keys())) #escolha um personagem aleatório
                    print("\n  Um salvagem {} apareceu...".format(adversario))
                    batalhar=str(input("\n    Deseja enfrenta-lo?  "))
                    if batalhar=="sim" or batalhar=="Sim" or batalhar=="SIM":
                        resultado= batalha(seupersonagem,adversario)   
                        print(resultado) 
                    elif batalhar=="NÃO" or batalhar=="não" or batalhar=="Não" :
                        print("\n {} conseguiu fugir de forma segura!".format(seupersonagem))
                        continue 
                    check_insperdex=Insperdex(adversario)
                    print(check_insperdex)
                '''    
                if escolha==procurar jogadores:
                    jogadorad=random.choice(list(jogadores.keys()))
                    print("\nUm ousado {} quer batalhar com você...".format(jogadorad)) 
                    batalhar=str(input("\n    Deseja enfrenta-lo?  ")) 
                    if batalhar=="sim" or batalhar=="Sim" or batalhar=="SIM":
                        resultado= batalha_usuarios(usuario,jogadorad)   
                        print(resultado) 
                    elif batalhar=="NÃO" or batalhar=="não" or batalhar=="Não" :
                        print("\n Você ignorou {}!".format(jogadorad))
                        continue  
                '''          
                if escolha=="dormir" or escolha=="Dormir" or escolha=="DORMIR" :  
                    print("\nBom descanso!\n")
                    break
               
        if menu_choice==2:
            print("Aqui está todos inspermons achados até o momento.")
            print(insperdex)
            clear()
        if menu_choice==3:
            print("Volte Sempre!")
            quit()            
