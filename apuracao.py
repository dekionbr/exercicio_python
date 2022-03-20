class Apuracao:
    def __init__(self, votos):
        self.__votos = votos

    def set_voto(self, voto):
        if(len(self.__votos) < 2):
            self.__votos.append(voto)
        else:
            print('Limite de eleitores atingido!')

    def apurar(self):
        cand1 = self.__votos.count('1')
        cand2 = self.__votos.count('2')
        cand3 = self.__votos.count('3')
        cand4 = self.__votos.count('4')
        brancos = self.__votos.count('0')
        nulos = len(self.__votos) - (cand1+cand2+cand3+cand4+brancos)
        print(f'{cand1} votos para candidato numero 1 - João da Silva')
        print(f'{cand2} votos para candidato numero 2 - José Ramalho')
        print(f'{cand3} votos para candidato numero 3 - Maria Mattos')
        print(f'{cand4} votos para candidato numero 4 - Pedro Américo')
        print(f'{brancos} votos em Branco')
        print(f'{nulos} votos Nulos')
