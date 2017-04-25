#Personagens do jogo 
import json

with open('base_inicial.json') as arquivo:
    personagem = json.load(arquivo)


                      
import random
import os
clear = lambda: os.system('cls')
import sys, time
def timer(text, delay):
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
        self.vd=self.vd_default
        adversario.vd=adversario.vd_default
    def batalha(self,adversario):
        delay=0.04
        while self.vd>0 and adversario.vd>0:

            lucky_factor=randint(1,3)
            if lucky_factor==1:
               adversario.vd=adversario.vd-(self.at-adversario.df*0.8)
            if lucky_factor==2:
                adversario.vd=adversario.vd-(self.at*1.2-adversario.df)
            if lucky_factor==3:          
                adversario.vd=adversario.vd-(self.at-adversario.df)
            if adversario.vd<=0:
                resultado=timer("\n   Parabéns, seu {} venceu a batalha contra o selvagem {} ".format(self.nome,adversario.nome),delay)  
                adversario.Insperdex()
                self.Evoluir(adversario) 
                self.reset(adversario) 
                print("\n",self.exp)
                break

            lucky_factor=randint(1,3)
            if lucky_factor==1:
                self.vd=self.vd-(adversario.at-self.df*0.8)
            if lucky_factor==2:
                self.vd=self.vd-(adversario.at*1.2-self.df)
            if lucky_factor==3:
                self.vd=self.vd-(adversario.at-self.df)
            if self.vd<=0:
                resultado=timer("\n    Poxa vida, {} perdeu a batalha para o selvagem {}. Ele irá se recuperar em poucos segundos".format(self.nome,adversario.nome),delay)
                self.reset(adversario)
                break   
            

        return resultado
        
    def Insperdex (adversario):
        delay=0.04
        if adversario.nome in insperdex:
            mensagem=""
        if adversario.nome not in insperdex:
            insperdex.append(adversario.nome)
            mensagem=timer("\n\n    {} nunca havia sido visto mas agora foi adicionado a sua Insperdex".format(adversario.nome),delay)
        
    def Evoluir(self,adversario):
        delay=0.8

        if self.exp<40:
            self.exp=self.exp+adversario.dif
            if self.exp>=40 and self.exp<80:
                clear()
                print("Espere um momento",end=" ")
                print(timer(".....",delay))
                clear()
                print("\n\n    Uau , parece que seu {} evoluiu para o estagio 2 ".format(self.nome))
                self.est=2
            
        elif self.exp>40 and self.exp<80:
            self.exp=self.exp+adversario.dif
            if self.exp>=80 and self.exp<130:
                clear()
                print("Espere um momento",end=" ")
                print(timer(".....",delay))
                clear()
                print("\n\n    Uau , parece que seu {} evoluiu para o estagio 3 ".format(self.nome))
                self.est=3 
            
        elif self.exp>80 and self.exp<130:
            self.exp=self.exp+adversario.dif
            if self.exp>=130 and self.exp<190:
                clear()
                print("Espere um momento",end=" ")
                print(timer(".....",delay))
                clear()
                print("\n\n    Uau , parece que seu {} evoluiu para o estagio 4 ".format(self.nome))
                self.est=4
                   
        elif self.exp>130 and self.exp<190:
            self.exp=self.exp+adversario.dif
            if self.exp>=190 and self.exp<260:
                clear()
                print("Espere um momento",end=" ")
                print(timer(".....",delay))
                clear()
                print("\n\n    Uau , parece que seu {} evoluiu para o estagio 5 ".format(self.nome))
                self.est=5
            
        

insperdex=[]

from random import randint
clear()
delay=0.06
print (timer("\n\nOlá, seja bem vindo ao Inspermon !\n\n",delay))
print (timer("Os personagens disponíveis são:\nDennis Dj\nKaique Fogo no rabo \nTyranaRafa \nAriel da 99 \nVAITHOMAS \nMano Hugo",delay))
while True:
    while True:
        seupersonagem=str(input(timer("Escolha um Inspermon para começar sua jornada: ",delay)))   #escolha do jogador
        if seupersonagem in personagem:
                          
            seupersonagem=Inspermon(personagem,seupersonagem)
            
            
            print(timer("\n  Pronto agora só jogar\n",delay))
            insperdex.append(seupersonagem.nome)
            #clear()
            break
        else:
            print(timer("\nEsse inspermon não existe...\n",delay))
            continue
    while True:
        menu=timer("\n\nMenu Inicial:\n   1-JOGAR\n   2-INSPERDEX\n   3-SAIR\n\n",delay)
        menu_choice=int(input(menu)) 
        clear()
        if menu_choice==1:
            while True:
                
                escolha=int(input(timer("\nVocê deseja passear(0) ou dormir(1)?\n\n",delay)))
                clear()
                if escolha==0:
                    adversario= random.choice(list(personagem.keys())) #escolha um personagem aleatório
                    print(timer("\n  Um salvagem {} apareceu...".format(adversario),delay))
                    adversario=Inspermon(personagem,adversario)
                    batalhar=int(input("\n    Deseja enfrenta-lo?\nSim(0)\nNão(1)\n\n"))
                    if batalhar==0:

                        resultado_batalha= seupersonagem.batalha(adversario)   
                        print(resultado_batalha)
                        
                        
                        
                    elif batalhar==1 :
                        sorteio=randint(1,4)
                        if sorteio==1:
                            print (timer("\n {} conseguiu fugir de forma segura!".format(seupersonagem.nome),delay))
                        if sorteio==2 or sorteio==3 or sorteio==4:
                            print (timer("\n {} não conseguiu fugir de forma segura!".format(seupersonagem.nome).delay))
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
                if escolha==1 :  
                    print("\nBom descanso!\n")
                    break
               
        if menu_choice==2:
            print (timer("Aqui está todos inspermons achados até o momento.",delay))
            print(insperdex)
            '''
            novopersonagem=input(timer("Escolha um personagem de seu insperdex para usar em uma batalha\n    "))
            seupersonagem=novopersonagem
            '''

        if menu_choice==3:
            print (timer("Volte Sempre!",delay))
            quit()   


                
            
        