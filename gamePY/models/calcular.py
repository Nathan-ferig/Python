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
        return f'Valor 1: {self.__valor1} \nValor 2: {self.__valor2} \nDificuldade: {self.__dificuldade} \nOperação: {op}'

    @property
    def _gerar_valor(self: object) -> int:
        if self.__dificuldade == 1:
            return randint(0,10)
        elif self.__dificuldade == 2:
            return randint(0,100)
        elif self.__dificuldade == 3:
            return randint(0,1000)
        elif self.__dificuldade == 4:
            return randint(0,10000)
        else:
            return randint(0,100000)
 
    @property
    def _gerar_resultado(self: object) -> int:
        if self.__operacao == 1: # sum
            return self.__valor1 + self.__valor2
        elif self.__operacao == 2: # subtract
            return self.__valor1 - self.__valor2
        else: # multiply
            return self.__valor1 * self.__valor2

    @property
    def _op_simbolo(self: object) -> str:
        if self.__operacao == 1: # sum
            return '+'
        elif self.__operacao == 2: # subtract
            return '-'
        else: # multiply
            return '*'

    def _checar_resultado(self: object, resposta: int) -> bool:
        certo: bool = False

        if self.__resultado == resposta:
            print('Resposta certa!')
            certo = True
        else:
            print('Resposta errada!')
        
        print(f'{self.__valor1} {self._op_simbolo} {self.__valor2} = {self.resultado}')
        return certo

    def _mostrar_operacao(self: object) -> None:
        print(f'{self.__valor1} {self._op_simbolo} {self.__valor2} = ?')
