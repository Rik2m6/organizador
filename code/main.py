#importação das classes usadas.
from tkinter import * ## Biblioteca nativa do python para criar interfaces graficas.

#Classe principal aonde esta sendo criado os componentes da interface grafica.
class Application():
    def __init__(self):
        #Adicionando a janela principal ao codigo.
        self.main = main

        #chamando cada metodo da classe.
        self.main_canvas() #Metodo para configurar a janela principal.
        self.frame_tela() #Metodo que cria cada frame da tela.
        self.criando_botoes() #adic. botões aos frames. 

        #Loop principal.
        main.mainloop()

    #Metodos da classe:
    def main_canvas(self):

        self.main.title("Muts'sen") # Titulo da pagina que remete ao no do time.
        self.main.geometry("800x600") #tamanho da janela que é 800 por 600.
        self.main.resizable(False, False) #Fixando um tamanho e não permitindo alterações.
        self.main.configure(background = "#f8faca") #alterando a cor da tela de fundo.

    def frame_tela(self):
        #Primeiro frame que é responsavel por acomodar a informações dos tipo de cada classificação dos times.
        self.frame_list_times = Frame(self.main, highlightbackground = 'black', highlightthickness = 1) #Criando o frame e especificando o configurações da borda.
        self.frame_list_times.place(x = 10, y = 10, width = 200, height= 360) #Configurando o tamanho da tela.

        #segundo frame que é responsavel pela a listagem de cada jogador do time.
        self.frame_list_atleta = Frame(self.main, highlightbackground = 'black', highlightthickness = 1) #Criando o frame e especificando o configurações da borda.
        self.frame_list_atleta.place(x = 220, y = 10, width = 570, height = 580)#Configurando o tamanho da tela.

    def criando_botoes(self):
        #Codigo provisorio enquanto não é realizado a conexão com o banco de dados
        list_time = [{'nome': 'Faixa etaria livre'}, {'nome': 'Sub 16'}]


        arrays = [] #Uma Lista para registrar os botões criados.
        posicao = 0.08 #Posição do primeiro botão.

        #Laço de repetição que ira criar o botão com base nos dados puxado do banco de dados:
        for i in list_time:# Pecorre cada item da lista:
            #Laço de repetição que ira criar os botões percorrendo cada dicinarios lido pela a primeira lista, e tratando os dados como uma lista.
            for arquivo in i.items():
                self.botao = Button(self.frame_list_times, text = arquivo[1], bd = 0, highlightthickness = 0, anchor = 'w') #Criando o primeiro botão mas ainda não adicionando ele a lista arrays.
                if arrays == []: #Uma condicional para verificar se a lista está vazia.

                    self.botao.place(relx = 0.05, rely = posicao, width = 120, height = 20) # Posiciando e especificando o tamanho  dos botôes.
                    posicao += 0.08 #Alterando a posição de referencia para os botôes não se sobreporem.
                    arrays.append(self.botao) #Registrando o botão.
                else:
                    self.botao.place(relx = 0.05, rely = posicao, width = 120, height = 20) # Posiciando e especificando o tamanho  dos botôes.
                    posicao += 0.08 #Alterando a posição de referencia para os botôes não se sobreporem.
                    arrays.append(self.botao) #Registrando o botão.
                    
#Incialiando a biclioteca no objeto que sera a tela principal.
main = Tk()

#chamando a classe.
Application()
