import os
import threading
from time import sleep
import tkinter as tk
from downloadcar import Download
import chardet



lista_arquivos = os.listdir("cidades")
lista_cidades = []
lista_estados = []
for c in lista_arquivos:
    # Lê o arquivo com a codificação correta
    with open("cidades/"+c, "r") as txt:
        lista = txt.readlines()
        for z in lista:
            cidade = z.split('###')
            cidade = cidade[0]
            lista_cidades.append(cidade)
        lista_estados.append(lista_cidades)
        lista_cidades = []




estados_cidades = {
    "Todos os estados" : [],
    "AC": lista_estados[0],
    "AL": lista_estados[1],
    "AM": lista_estados[2],
    "AP": lista_estados[3],
    "BA": lista_estados[4],
    "CE": lista_estados[5],
    "DF": lista_estados[6],
    "ES": lista_estados[7],
    "GO": lista_estados[8],
    "MA": lista_estados[9],
    "MG": lista_estados[10],
    "MS": lista_estados[11],
    "MT": lista_estados[12],
    "PA": lista_estados[13],
    "PB": lista_estados[14],
    "PE": lista_estados[15],
    "PI": lista_estados[16],
    "PR": lista_estados[17],
    "RJ": lista_estados[18],
    "RN": lista_estados[19],
    "RO": lista_estados[20],
    "RR": lista_estados[21],
    "RS": lista_estados[22],
    "SC": lista_estados[23],
    "SE": lista_estados[24],
    "SP": lista_estados[25],
    "TO": lista_estados[26],
}

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.cidade = []
        self.estado = ""
        self.oestado = ""
        self.estados = []
        self.codigo = []
        self.master = master
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.estado_var = tk.StringVar(self)
        self.estado_var.set("Selecione um estado")
        self.estado_menu = tk.OptionMenu(self, self.estado_var, *estados_cidades.keys(), command=self.update_cidade_menu)
        self.estado_menu.pack()

        self.cidade_var = tk.StringVar(self)
        self.cidade_var.set("Selecione uma cidade")
        self.cidade_menu = tk.OptionMenu(self, self.cidade_var, "")
        self.cidade_menu.pack()

        self.confirm_button = tk.Button(self, text="Adicionar", command=self.print_estado_cidade)
        self.confirm_button.pack()

        self.confirm_button = tk.Button(self, text="Confirmar", command=self.gerar_arquivos)
        self.confirm_button.pack()

    def update_cidade_menu(self, estado):
        cidades = estados_cidades[estado]
        self.cidade_menu.children["menu"].delete(0, "end")
        for cidade in cidades:
            self.cidade_menu.children["menu"].add_command(label=cidade, command=lambda cid=cidade: self.cidade_var.set(cid))

    def print_estado_cidade(self):
        estado = self.estado_var.get()
        cidade = self.cidade_var.get()
        if estado == "Todos os estados":
            count = 0
            for c in estados_cidades.keys():
                if count != 0:
                    estado = str(c)
                    with open("cidades/"+estado+".txt",'r') as txt: 
                        lista = txt.readlines()
                        count = 0
                        for z in lista:
                            if count != 0:   
                                linha = z.split('###')
                                cidadez = linha[0]
                                codigo = linha[1].replace("\n","")
                                self.codigo.append(codigo)
                                self.cidade.append(estado+"_"+cidadez)
                            count += 1
                count += 1
            print("FIM")
        else:
            with open("cidades/"+estado+".txt",'r') as txt:
                lista = txt.readlines()
                if cidade == "Todas as cidades\n" and estado not in self.estados:
                    self.estados.append(estado)
                    count = 0
                    for z in lista:
                        if count != 0:   
                            linha = z.split('###')
                            cidadez = linha[0]
                            codigo = linha[1].replace("\n","")
                            self.codigo.append(codigo)
                            self.cidade.append(estado+"_"+cidadez)
                        count += 1
                elif(estado not in self.estados):
                
                    count = 0
                    for z in lista:
                        if count != 0:
                            linha = z.split('###')
                            cidadez = linha[0]
                            codigo = linha[1].replace("\n","")
                            if cidade == cidadez:
                                self.codigo.append(codigo)
                                self.cidade.append(estado+"_"+cidade)
                                break
                        count += 1
    


    def gerar_arquivos(self):
        print(self.cidade)
        download = Download()
        count = 1
        for c in range(0,len(self.codigo)):
            threading.Thread(target=download.iniciar(int(self.codigo[c]),self.cidade[c])).start()
            print("--->>> PROXIMO <<<---")
            count += 1
            if count == 100:
                count = 0
                sleep(10)
        self.codigo = []
        self.cidade = []
        self.estados = []

            
                


root = tk.Tk()
app = Application(master=root)
app.mainloop()


