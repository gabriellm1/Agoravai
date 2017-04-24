#Personagens do jogo 
import json

with open('jason_motherfucker.json') as arquivo:
    personagem = json.load(arquivo)


                      
import random
import os
clear = lambda: os.system('cls')
import sys, time
def timer(text, delay=0.04):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    a=""
    return a
    
class Inspermon:
    def __init__(self,dicionario,inspermon):
        self.nome=inspermon
        self.at=dicionario[inspermon]["Poder de ataque"]
        self.df=dicionario[inspermon]["Nivel de defesa"]
        self.vd=dicionario[inspermon]["Pontos de vida"]
        self.est=dicionario[inspermon]["Estagio"]
        self.exp=dicionario[inspermon]["Experiencia"]
        self.vd_default=dicionario[inspermon]["Pontos de vida"]
        self.dif=dicionario[inspermon]["Dificuldade"]
    def reset(self,adversario):
        self.vd+=self.vd_default-self.vd
        adversario.vd+=adversario.vd_default-adversario.vd
    def batalha(self,adversario):
        
        while self.vd>0 and adversario.vd>0:

            lucky_factor=randint(1,3)
            if lucky_factor==1:
               adversario.vd=adversario.vd-(self.at-adversario.df*0.8)
            if lucky_factor==2:
                adversario.vd=adversario.vd-(self.at*1.2-adversario.df)
            if lucky_factor==3:          
                adversario.vd=adversario.vd-(self.at-adversario.df)
            if adversario.vd<=0:
                resultado=timer("\n   Parabéns, seu {} venceu a batalha contra {} ".format(self.nome,adversario.nome))
                self.reset(adversario)
                   
            
                adversario.Insperdex()  
                break

            lucky_factor=randint(1,3)
            if lucky_factor==1:
                self.vd=self.vd-(adversario.at-self.df*0.8)
            if lucky_factor==2:
                self.vd=self.vd-(adversario.at*1.2-self.df)
            if lucky_factor==3:
                self.vd=self.vd-(adversario.at-self.df)
            if self.vd<=0:
                resultado=timer("\n    Poxa vida, {} perdeu a batalha para {}. Ele irá se recuperar em poucos segundos".format(self.nome,adversario.nome))
                self.reset(adversario)
                break   
            

        return resultado
        
    def Insperdex (adversario):
        if adversario.nome in insperdex:
            mensagem=""
        if adversario.nome not in insperdex:
            insperdex.append(adversario.nome)
            mensagem=timer(("\n\n    {} nunca havia sido visto mas agora foi adicionado a sua Insperdex".format(adversario.nome)))
        
    #def Evoluir():



insperdex=[]

from random import randint
clear()
print (timer("\n\nOlá, seja bem vindo ao Inspermon !\n\n"))
print (timer("Os personagens disponíveis são:\nDennis Dj\nKaique Fogo no rabo \nTyranaRafa \nAriel da 99 \nVAITHOMAS \nMano Hugo"))
while True:
    while True:
        seupersonagem=str(input(timer("Escolha um Inspermon para começar sua jornada: ")))   #escolha do jogador
        if seupersonagem in personagem:
                          
            seupersonagem=Inspermon(personagem,seupersonagem)
            
            
            print(timer("\n  Pronto agora só jogar\n"))
            insperdex.append(seupersonagem.nome)
            #clear()
            break
        else:
            print(timer("\nEsse inspermon não existe...\n"))
            continue
    while True:
        menu=timer("\n\nMenu Inicial:\n   1-JOGAR\n   2-INSPERDEX\n   3-SAIR\n\n")
        menu_choice=int(input(menu)) 

        if menu_choice==1:
            while True:
                
                escolha=str(input(timer("\nVocê deseja passear ou dormir?  ")))
                clear()
                if escolha=="Passear" or escolha=="passear" or escolha=="PASSEAR":
                    adversario= random.choice(list(personagem.keys())) #escolha um personagem aleatório
                    print(timer("\n  Um salvagem {} apareceu...".format(adversario)))
                    adversario=Inspermon(personagem,adversario)
                    batalhar=str(input("\n    Deseja enfrenta-lo?  "))
                    if batalhar=="sim" or batalhar=="Sim" or batalhar=="SIM":

                        resultado_batalha= seupersonagem.batalha(adversario)   
                        print(resultado_batalha)
                        
                        
                        
                    elif batalhar=="NÃO" or batalhar=="não" or batalhar=="Não" :
                        sorteio=randint(1,4)
                        if sorteio==1:
                            print (timer("\n {} conseguiu fugir de forma segura!".format(seupersonagem.nome)))
                        if sorteio==2 or sorteio==3 or sorteio==4:
                            print (timer("\n {} não conseguiu fugir de forma segura!".format(seupersonagem.nome)))
                            seupersonagem.vd=seupersonagem.vd-(adversario.at-seupersonagem.df)
                            resultado_batalha= seupersonagem.batalha(adversario)   
                            print(resultado_batalha)
                            
                            
                        continue
                    '''    
                    check_insperdex=Insperdex(adversario)
                    print(check_insperdex)
                    '''
                    
                    

                    
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
            print (timer("Aqui está todos inspermons achados até o momento."))
            print(insperdex)
            '''
            novopersonagem=input(timer("Escolha um personagem de seu insperdex para usar em uma batalha\n    "))
            seupersonagem=novopersonagem
            '''

        if menu_choice==3:
            print (timer("Volte Sempre!"))
            quit()   


                
            
        