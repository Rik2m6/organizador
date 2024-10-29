#importação das classes usadas.
from tkinter import *  ## Biblioteca nativa do python para criar interfaces graficas.
from database.conect import Database

#Classe principal onde está sendo criado os componentes da interface gráfica.
class Application():
    def __init__(self):
        # Adicionando a janela principal ao código.
        self.main = main
        
        # Conectar ao banco de dados ao iniciar a aplicação
        self.connect()  

        # Chamando cada método da classe.
        self.main_canvas()  # Método para configurar a janela principal.
        self.frame_tela()  # Método que cria cada frame da tela.
        self.criando_botoes()  # Adiciona botões aos frames.

        # Configurar o evento de fechamento da janela
        self.main.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Loop principal.
        main.mainloop()

    # Métodos da classe:
    def main_canvas(self):
        self.main.title("Muts'sen")  # Título da página que remete ao nome do time.
        self.main.geometry("800x600")  # Tamanho da janela que é 800 por 600.
        self.main.resizable(False, False)  # Fixando um tamanho e não permitindo alterações.
        self.main.configure(background="#f8faca")  # Alterando a cor da tela de fundo.

    def frame_tela(self):
        # Primeiro frame que é responsável por acomodar as informações dos tipos de cada classificação dos times.
        self.frame_list_times = Frame(self.main, highlightbackground='black', highlightthickness=1)  # Criando o frame.
        self.frame_list_times.place(x=10, y=10, width=200, height=360)  # Configurando o tamanho da tela.

        # Segundo frame que é responsável pela listagem de cada jogador do time.
        self.frame_list_atleta = Frame(self.main, highlightbackground='black', highlightthickness=1)  # Criando o frame.
        self.frame_list_atleta.place(x=220, y=10, width=570, height=580)  # Configurando o tamanho da tela.

    def criando_botoes(self):
        self.connect()
        titulo = Label(self.frame_list_times, text="Times", font=("default", 20))  # Objetivo do frame
        titulo.place(relx=0.04, rely=0.025)  # Posição do texto.

        # Código provisório enquanto não é realizada a conexão com o banco de dados
        list_time = [{'nome': 'Faixa etária livre'}, {'nome': 'Sub 16'}]

        arrays = []  # Lista para registrar os botões criados.
        posicao = 0.14  # Posição do primeiro botão.

        # Laço de repetição que cria o botão com base nos dados
        for i in list_time:  # Percorre cada item da lista:
            for arquivo in i.items():
                self.botao = Button(self.frame_list_times, text=arquivo[1], bd=0, highlightthickness=0, anchor='w', font=("default", 10))  # Criando o botão.
                self.botao.place(relx=0.12, rely=posicao, width=120, height=20)  # Posicionando e especificando o tamanho dos botões.
                posicao += 0.08  # Alterando a posição de referência para os botões não se sobreporem.
                arrays.append(self.botao)  # Registrando o botão.

    def connect(self):
        self.bd = Database("muttsen", "root", "mysql", "localhost")
        self.bd.connect()

    def disconnect(self):
        if hasattr(self, 'bd'):
            self.bd.disconnect()

    def on_closing(self):
        self.disconnect()  # Chama o método de desconexão
        self.main.destroy()  # Fecha a janela

# Inicializando a biblioteca no objeto que será a tela principal.
main = Tk()

# Chamando a classe.
Application()
