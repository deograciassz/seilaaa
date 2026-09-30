import json

class Status:
    def informar_status(self):
        status = input("Termino a tarefa?: ")
        print("ae sim vc falou que:", status)

Status().informar_status()

class Pessoa:
    def __init__(self, nome):
        self.casa = "naosei"  # atributo
        self.nome = nome # atributo
        def apresentar(self):
            print(f"o morador {self.nome} terminou uma tarefa")

    def tarefa(self):
        print(f"o morador {self.nome} terminou a tarefa")

pessoa = Pessoa("enexistente")
pessoa.tarefa()

class Lista:
    lista_tarefas = ["lavar a louça", "varrer", "arrumar a cama"]

tarefas = input("digite uma nova tarefa: ")
print("tarefas:", tarefas)

tarefa = []

jsonS = [
    {
        "pessoa" : pessoa,
        "tarefa" : tarefa
    } for tarefa in tarefas

]

def criar_json(jsostring):
    with open (file =  "tarefas.json", mode= 'w') as file:
        file.write(json.dumps(tarefas, indent=4))

def loadJson():
    with open(file= "tarefas.json", mode ='r') as file:
        return json.load(file)

    loadJson()