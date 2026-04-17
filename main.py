from utils import ler_matriz
from algoritmo import forca_bruta

def main():
    try:
        # Tenta ler o arquivo de entrada conforme o formato do PDF [cite: 30]
        origem, entregas = ler_matriz("Flyfood/input.txt")
        
        if origem is None:
            print("Erro: Ponto de origem 'R' não encontrado no arquivo.")
            return

        # Executa a busca pela melhor rota
        sequencia, custo = forca_bruta(origem, entregas)
        
        # A resposta deve ser a sequência de pontos (string) [cite: 36]
        print(f"Melhor sequência: {sequencia}")
        print(f"Custo total (dronômetros): {custo}")
        
    except FileNotFoundError:
        print("Erro: Arquivo 'input.txt' não encontrado.")

if __name__ == "__main__":
    main()