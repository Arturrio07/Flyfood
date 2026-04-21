# Flyfood
# 🚁 FlyFood  
### Otimização de Rotas para Drones

---

## 📖 Apresentação

Com o aumento do trânsito nas grandes cidades, soluções tradicionais de delivery se tornam cada vez menos eficientes. Pensando nisso, o projeto **FlyFood** propõe o uso de drones para realizar entregas de forma mais rápida e inteligente.

Nesse cenário, os drones saem de um ponto de origem carregando múltiplos pedidos e precisam entregá-los em diferentes locais da cidade, retornando ao ponto inicial ao final do percurso.

---

## 🎯 Objetivo

O objetivo deste projeto é desenvolver um algoritmo capaz de determinar a **melhor rota possível** para um drone realizar todas as entregas, **minimizando** a distância total percorrida.

A solução busca otimizar o uso da bateria e tornar o processo de entrega mais eficiente.

---

## 🧠 Desafio

O principal desafio consiste em definir a ordem ideal de visita aos pontos de entrega, considerando que:

- O drone parte de um ponto de origem (R)
- Deve visitar todos os pontos de entrega (A, B, C, ...)
- Precisa retornar ao ponto de origem ao final
- Só pode se mover na horizontal ou vertical (sem diagonais)
- O objetivo é minimizar o custo total do trajeto

Esse problema é uma variação do clássico problema de otimização conhecido como **Problema do Caixeiro Viajante (TSP)**.

---

## 📂 Representação da Matriz

Para abstrair as questões de localização e coordenadas reais (como GPS), utilizamos uma matriz para representar os pontos da cidade.

### 🗺️ Exemplo
```

+---+---+---+---+---+
| 0 | 0 | 0 | 0 | D |
+---+---+---+---+---+
| 0 | A | 0 | 0 | 0 |
+---+---+---+---+---+
| 0 | 0 | 0 | 0 | C |
+---+---+---+---+---+
| R | 0 | B | 0 | 0 |
+---+---+---+---+---+

```


### 📍 Interpretação

- O ponto superior esquerdo é o **(0,0)** e não contém entrega  
- O ponto **A** está em **(1,1)**  
- O ponto **B** está em **(3,2)**  
- O ponto **C** está em **(2,4)**  
- O ponto **D** está em **(0,4)**  
- O ponto **R** em **(3,0)** representa a **origem e retorno do drone**

Por convenção, o drone sempre:
- Parte de `R`
- Realiza todas as entregas
- Retorna para `R` ao final

---

Essa matriz define o ambiente de navegação do drone, onde ele só pode se mover horizontalmente ou verticalmente.

---


### 🧠 Método

- O algoritmo implementado adota a busca exaustiva por forca bruta: gera todas as permutações possíveis da sequência de pontos de entrega e avalia o custo total de cada rota, selecionando a de menor distância acumulada. Essa estratégia garante a obtenção da solução ótima, ao custo de complexidade fatorial O(n!).

### 📂 Noção Matemática

- O espaço de entregas e modelado como um grafo G = (V, E), onde os vértices V representam os pontos de entrega e a origem, e as arestas E tem pesos dados pela distância de Manhattan. Para dois pontos P1 = (r1, c1) e P2 = (r2, c2):
D(P1, P2) = |r1 - r2| + |c1 - c2|

Essa métrica e adequada para ambientes urbanos ortogonais, como quarteões de cidades, onde o deslocamento diagonal não é possível. No código do FlyFood, essa função esta implementada em utils.py:
return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


### 👥 Participantes

- Artur Rio
- Diego Luiz
- Lucas Guerra
- Pedro Poroca
