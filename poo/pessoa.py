class Pessoa:
    def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = None
    
if __name__ == "__main__":
    pessoa = Pessoa()
    pessoa.nome = "Yuri Rodrigues"