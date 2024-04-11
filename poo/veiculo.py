class Veiculo:

    def __init__(self,descricao):
        self.descricao = descricao

    def get_descricao(self):
        return self.descricao
    
def main():
    obj1 = Veiculo("Prisma")
    print(f"Descrição: {obj1.get_descricao()}")

if __name__ == "__main__":
    main()