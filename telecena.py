from random import randint
import time


class Sorteador:
    
    def __init__(self) -> None:
        self.numeros = [i for i in range(1, 61)]

    @staticmethod
    def _cria_lista() -> list[int]:
        lista = []
        for _ in range(60):
            lista.append(0)
        return lista

    def escolhe_valor(self, repeticoes: int, quantidade_numeros: int = 6) -> None:
        for i in range(repeticoes):
            valor_sorteado = self._sorteia_valor()
            self._armazena_valores(valor_sorteado)
            print(f"{i+1}/{repeticoes} | {((i+1)/repeticoes)*100:.2f}%")
        print("valor encontrado!")
        print(self._monta_valor(quantidade_numeros))
    
    @staticmethod
    def _sorteia_valor() -> list[int]:
        valor = []
        for _ in range(6):
            while len(valor) != 6:
                numero_sorteado = randint(1, 60)
                if not numero_sorteado in valor:
                    valor.append(numero_sorteado)
                    valor.sort()
        return valor

    def _armazena_valores(self, valor_sorteado: list[int]) -> None:
        for i in range(6):
            self.numeros[valor_sorteado[i]-1] += 1

    def _monta_valor(self, quantidade_numeros: int) -> list[int]:
        valor_escolhido = []
        for _ in range(quantidade_numeros):
            valor_escolhido.append(self._identifica_maior_nao_repetido(valor_escolhido, self.numeros))
        valor_escolhido.sort()
        return valor_escolhido

    @staticmethod
    def _identifica_maior_nao_repetido(valor: list[int], caracter: list[int]) -> int:
        while True:
            maior = caracter.index(max(caracter))+1
            if maior in valor:
                caracter[maior-1] = 0
                continue
            return maior


if __name__ == "__main__":
    try:
        repeticoes = int(input("repetições: "))
    except:
        repeticoes = 10**10
        print(f"Valor inválido, usando: {repeticoes}")
    try:
        tamanho_resultado = int(input("tamanho resultado: "))
        if tamanho_resultado > 60 or tamanho_resultado < 0:
            raise ValueError
    except:
        tamanho_resultado = 6
        print(f"Valor inválido, usando: {tamanho_resultado}")
    time.sleep(1)
    Sorteador().escolhe_valor(repeticoes, tamanho_resultado)
