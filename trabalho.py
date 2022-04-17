#!/usr/bin/env python
# coding: utf-8


# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


#OBS.: Coloquei uma flag com o nome de retirarDadosPote como False, para melhor avaliação do jogo, se ela estiver True, 
#toda rodada será removido os dados sorteados do pote.


from random import randint, choice

class Zombie_Dice():

    def pegar_dado(self, dadoSorteado):
        if dadoSorteado == ("C", "P", "C", "T", "P", "C"):
            corDado = "Verde"
        elif dadoSorteado == ("T", "P", "C", "T", "P", "C"):
            corDado = "Amarelo"
        else:
            corDado = "Vermelho"

        return corDado

    def remove_dado_lista(self, listaDados, dadoSorteado):

        listaDados.remove(dadoSorteado)
        return listaDados

    def lancar_dados(self, listaDados, num_lancamentos, retirarDadosPote):

        coresSorteadas = []
        dadosSorteados = []

        for i in range(0, num_lancamentos):
            #numSorteado = randint(0, 12)
            #dadoSorteado = listaDados[numSorteado]

            if len(listaDados) != 0:
                dadoSorteado = choice(listaDados)
            else:
                break

            corDado = self.pegar_dado(dadoSorteado)

            coresSorteadas.append(corDado)    
            dadosSorteados.append(dadoSorteado)

            if retirarDadosPote:
                listaDados = self.remove_dado_lista(listaDados, dadoSorteado)

        return listaDados, coresSorteadas, dadosSorteados

    def mostrar_dados(self, coresSorteadas):
            print("As cores sorteadas foram: ", coresSorteadas)

    def mostrar_score(self, cerebros, tiros):
        print("Score atual: ")
        print("Cérebros: ", cerebros)
        print("Tiros: ", tiros)

    def inicializar_novo_turno(self, jogadorAtual):
        jogadorAtual = jogadorAtual + 1
        tiros = 0
        cerebros = 0
        passos = 0

        return jogadorAtual, tiros, cerebros, passos

    def mostrar_faces_sorteadas(self, dadosSorteados, cerebros, tiros, passos):

        print("As faces sorteadas foram: ")

        for dadoSorteado in dadosSorteados:

            numFaceDado = randint(0, 5)

            if dadoSorteado[numFaceDado] == "C":
                print("CÉREBRO - (Você comeu um cérebro)")
                cerebros = cerebros + 1

            elif dadoSorteado[numFaceDado] == "T":
                print("TIRO - (Você levou um tiro)")
                tiros = tiros + 1

            else:
                print("PASSOS - (Uma vítima escapou)")
                passos = passos + 1

        return dadosSorteados, cerebros, tiros, passos

    def inicializar_dados(self):
        dadoVerde = ("C", "P", "C", "T", "P", "C")
        dadoAmarelo = ("T", "P", "C", "T", "P", "C")
        dadoVermelho = ("T", "P", "T", "C", "P", "T")

        listaDados = [
            dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
            dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
            dadoVermelho, dadoVermelho, dadoVermelho
            ]

        return listaDados

    def mostrar_dados_pote(self, listaDados):

            print("Dados no pote: ")
            [print(dado) for dado in listaDados]

    def mostra_resultado(self, resultados):

        print("Os resultados foram: ")
        [print(resultado) for resultado in resultados]
        print("\n")

        maior_num_cerebros = -1
        vencedor = ""

        for resultado in resultados:

            if resultado['Cerebros'] > maior_num_cerebros:
                vencedor = resultado['Jogador']
                maior_num_cerebros = resultado['Cerebros']

        print("O vencedor foi " + vencedor + " com " + str(maior_num_cerebros) + " cerebros")


    def deseja_continuar_turno(self):
            continuarTurno = input("AVISO: Você deseja continuar jogando dados? (s = sim, n = não)")
            return continuarTurno


ZD = Zombie_Dice()
        
print("ZOMBIE DICE (Protótipo Semana 4)")
print("Seja bem vindo ao jogo Zombie Dice!")

numJogadores = 0

while(numJogadores < 2):
    numJogadores = input("Escreva a quantidade de jogadores: ")
    numJogadores = int(numJogadores)
    
    if numJogadores < 2:
        print("AVISO: Você precisa de pelo menos 2 jogadores! \n")
        
        
listaJogadores = []
resultados = []

for i in range(numJogadores):
    
    jogador = input("Informe o nome do jogador " + str(i) + ": ")
    listaJogadores.append(jogador)
    
#dadoVerde = "CPCTPC"
#dadoAmarelo = "TPCTPC"
#dadoVermelho = "TPTCPT"



listaDados = ZD.inicializar_dados()
retirarDadosPote = True
    
    
print("Iniciando o jogo...")

jogadorAtual = 0
dadosSorteados = []
tiros = 0
cerebros = 0
passos = 0

while(True):
    
    print("Turno do jogador " + listaJogadores[jogadorAtual])
    coresSorteadas = []
    
            
        
    listaDados, coresSorteadas, dadosSorteados = ZD.lancar_dados(listaDados, 3, retirarDadosPote)    
        
    ZD.mostrar_dados_pote(listaDados)
    ZD.mostrar_dados(coresSorteadas)
    
    

    dadosSorteados, cerebros, tiros, passos = ZD.mostrar_faces_sorteadas(dadosSorteados, cerebros, tiros, passos)
    
        
    ZD.mostrar_score(cerebros, tiros)
    
    
    
    continuarTurno = ZD.deseja_continuar_turno()
    
    if len(listaDados) == 0:
        print("Não há mais dados no pote")
        print("Finalizando protótipo do jogo...")
        break
        
    
    if continuarTurno == "n":
        
        resultados.append({'Jogador': listaJogadores[jogadorAtual], 'Cerebros': cerebros})
        jogadorAtual, tiros, cerebros, passos = ZD.inicializar_novo_turno(jogadorAtual)
        
        if jogadorAtual == len(listaJogadores):
            print("Finalizando protótipo do jogo...")
            break
            
    else:
        print("Iniciando mais uma rodada do turno atual...")
        dadosSorteados = []
    
    
ZD.mostra_resultado(resultados)