def distancia(p1, p2):
    """Calcula a distância de Manhattan (horizontal + vertical)."""
    # p1 e p2 são tuplas (linha, coluna)
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def ler_matriz(caminho_arquivo):
    """Lê o arquivo e retorna o ponto de origem 'R' e um dicionário de entregas."""
    pontos_entrega = {}
    origem = None
    
    with open(caminho_arquivo, "r") as f:
        linhas = f.readlines()
        # A primeira linha contém as dimensões da matriz (ex: 4 5) [cite: 31]
        dimensoes = linhas[0].split()
        
        # Percorre o restante das linhas para encontrar os pontos [cite: 32-35]
        for r, linha in enumerate(linhas[1:]):
            conteudo = linha.strip()
            for c, char in enumerate(conteudo.split()):
                if char == 'R':
                    origem = (r, c)
                elif char != '0':
                    pontos_entrega[char] = (r, c)
                    
    return origem, pontos_entrega