from random import randint

class Calcular:

    def __init__(self: object, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: float = self._gerar_valor
        self.__valor2: float = self._gerar_valor
        self.__operacao: int = randint(1,3) # 1 = sum, 2 = subtract, 3 = multiply
        self.__resultado: float = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self: object) -> str:
        op: str = ''
        if self.__operacao == 1:
            op = 'Somar'
        elif self.__operacao == 2:
            op = 'Subtrair'
        elif self.__operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operacao desconhecida'
        return f'Valor 1 {self.__valor1} \nValor 2 {self.__valor2} \nDificuldade: {self.__dificuldade} \nOperação: {op}'

    @property
    def _gerar_valor(self: object) -> int:
        pass

    @property
    def _gerar_resultado(self: object) -> int:
        pass

    @property
    def _checar_resultado(self: object, resposta: int) -> bool:
        pass

    @property
    def _mostra_operacao(self: object) -> None:
        pass
