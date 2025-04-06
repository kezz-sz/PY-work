from tkinter import *

janela = Tk()
janela.title("(Un)Dating Simulator")

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

quadrado = Canvas(janela, width=largura_tela, height=altura_tela)
quadrado.pack()

quadrado.create_rectangle(0, 0, largura_tela, altura_tela, fill="black")

janela.mainloop()
