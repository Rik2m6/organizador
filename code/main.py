from tkinter import *

class Application():
    def __init__(self):
        self.main = main
        self.main_canvas()
        self.frame_tela()
        self.criando_botoes()
        main.mainloop()

    def main_canvas(self):

        self.main.title("Muts'sen")
        self.main.geometry("800x600")
        self.main.resizable(False, False)
        self.main.configure(background = "#f8faca")

    def frame_tela(self):

        self.frame_list_times = Frame(self.main, highlightbackground = 'black', highlightthickness = 1)
        self.frame_list_times.place(x = 10, y = 10, width = 200, height= 360)

        self.frame_list_atleta = Frame(self.main, highlightbackground = 'black', highlightthickness = 1)
        self.frame_list_atleta.place(x = 220, y = 10, width = 570, height = 580)

    def criando_botoes(self):

        list_time = [{'nome': 'Faixa etaria livre'}, {'nome': 'Sub 16'}]
        arrays = []
        posicao = 0.08

        for i in list_time:
            for arquivo in i.items():
                self.botao = Button(self.frame_list_times, text = arquivo[1], bd = 0, highlightthickness = 0, anchor = 'w')
                if arrays == []:
                    self.botao.place(relx = 0.05, rely = posicao, width = 120, height = 20)
                    posicao += 0.08
                    arrays.append(self.botao)
                else:
                    self.botao.place(relx = 0.05, rely = posicao, width = 120, height = 20)
                    posicao += 0.08


main = Tk()

Application()