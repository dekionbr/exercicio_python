class Pa:
    def __init__(self, termo1, razao):
        self.termo1 = termo1
        self.razao = razao

    def calcular(self):
        termo1 = int(self.termo1)
        razao = int(self.razao)
        for n in range(1, 11):
            termo_geral = termo1+((n-1)*razao)
            print(f'{n}º termo geral: {termo_geral}')

