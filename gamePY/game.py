from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [ 1, 2, 3 ou 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc._mostrar_operacao()

    resultado: int = int(input())

    if calc._checar_resultado(resultado):
        pontos += 1
        print(f'Voceê ganhou um ponto. \nAgora você tem {pontos} ponto(s).')
    else:
        print(f'Você não ganhou nenhum ponto nessa rodada. \nQue pena!')

    continuar: int = 0
    while not (continuar == 1 or continuar == 2):
        continuar = int(input('Deseja continuar no jogo? [1 - Sim, 2 - Não]: '))

    if continuar == 1:
        jogar(pontos)
    else: 
        print(f'Você finalizou o jogo com {pontos} ponto(s).')
        print('See you later!')

if __name__ == '__main__':
    main()