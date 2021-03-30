import random
import PySimpleGUI as Sg


class SimuladorDeDado:
    def __init__(self):
        self.num = random.randint(1, 6)
        # Layout
        layout = [
            [Sg.Text('Jogar o dado?')],
            [Sg.Button('Sim'), Sg.Button('Não')]
        ]
        self.janela = Sg.Window('Simulador de Dado', layout=layout)
        self.eventos, self.valores = self.janela.read()

    def iniciar(self):
        try:
            return lambda: self.eventos == 'sim', print(self.num) \
                if self.eventos == 'Sim' else print('Digite sim da próxima vez para gerar um valor')
        except:
            print('Ocorreu um erro ao recerber sua resposta')


teste = SimuladorDeDado()
teste.iniciar()
