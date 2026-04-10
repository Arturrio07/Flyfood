# Flyfood
# 🚁 FlyFood  
### Otimização de Rotas para Drones

---

## 📖 Apresentação

Com o aumento do trânsito nas grandes cidades, soluções tradicionais de delivery se tornam cada vez menos eficientes. Pensando nisso, o projeto **FlyFood** propõe o uso de drones para realizar entregas de forma mais rápida e inteligente.

Nesse cenário, os drones saem de um ponto de origem carregando múltiplos pedidos e precisam entregá-los em diferentes locais da cidade, retornando ao ponto inicial ao final do percurso.

---

## 🎯 Objetivo

O objetivo deste projeto é desenvolver um algoritmo capaz de determinar a **melhor rota possível** para um drone realizar todas as entregas, minimizando a distância total percorrida.

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
