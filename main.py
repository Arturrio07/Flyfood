from utils import ler_matriz
from algoritmo import forca_bruta
import time

inicio = time.perf_counter()

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

fim = time.perf_counter()

tempo_total = fim - inicio 
print(f"O algoritmo levou {tempo_total:.6f} segundos para ser executado.") #Printa o tempo de execução do código, com 6 casas decímais