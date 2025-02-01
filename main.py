class OitoRainhas:
    def __init__(self, tamanho=8):
        self.tamanho = tamanho
        self.solucao = []
    
    def resolver(self):
        self.solucao = []
        tabuleiro = [-1] * self.tamanho  # Vetor representando a coluna onde a rainha está posicionada em cada linha
        self.__backtracking(0, tabuleiro)

        if not self.solucao:
            print("Nenhuma solução encontrada.")
        else:
            self.__imprimir_solucoes()
    
    def __backtracking(self, linha, tabuleiro):
        """
        Algoritmo de backtracking que posiciona as rainhas no tabuleiro.
        :param linha: Índice da linha atual onde se tenta posicionar uma rainha.
        :param tabuleiro: Vetor que armazena a posição das rainhas em cada linha.
        """
        if linha == self.tamanho:
            self.solucao.append(tabuleiro[:])
            return

        for coluna in range(self.tamanho):
            if self.__pode_colocar(linha, coluna, tabuleiro):
                tabuleiro[linha] = coluna
                self.__backtracking(linha + 1, tabuleiro)
                tabuleiro[linha] = -1  # Backtrack

    def __pode_colocar(self, linha, coluna, tabuleiro):
        """
        Verifica se uma rainha pode ser colocada na posição (linha, coluna).
        :param linha: Linha onde a rainha será posicionada.
        :param coluna: Coluna onde a rainha será posicionada.
        :param tabuleiro: Estado atual do tabuleiro.
        :return: True se a posição for válida, False caso contrário.
        """
        for i in range(linha):
            if tabuleiro[i] == coluna or abs(tabuleiro[i] - coluna) == abs(i - linha):
                return False
        return True
    
    def __imprimir_solucoes(self):
        print(f"\nForam encontradas {len(self.solucao)} soluções para o problema das 8 Rainhas.\n")
        for solucao in self.solucao:
            for linha in range(self.tamanho):
                linha_str = [" . "] * self.tamanho
                linha_str[solucao[linha]] = " Q "
                print("".join(linha_str))
            print("\n" + "-" * (self.tamanho * 3) + "\n")

# Execução do algoritmo
if __name__ == "__main__":
    jogo = OitoRainhas()
    jogo.resolver()
