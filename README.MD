# Monitoramento de Poluição Oceânica

Este projeto utiliza programação dinâmica para otimizar a alocação de sensores subaquáticos e a coleta de dados sobre a poluição oceânica. O objetivo é identificar áreas críticas de poluição e priorizar ações de monitoramento e resposta.

## Estrutura do Projeto
1. **Código em Python** (arquivo .py ou .ipynb)
2. **README.md** (este arquivo)
3. **Referências**

## Instruções
- O código contém funções para calcular a distância entre pontos e encontrar a distribuição ótima dos sensores.
- Dados fictícios são usados para simulação.
- Execute o código para ver a alocação ótima dos sensores.

## Complexidade dos Algoritmos
1. **Função `calcular_distancia`**:
   - Complexidade: O(1) - Operação constante, pois o cálculo da distância entre dois pontos não depende do tamanho da entrada.

2. **Função `inicializar_tabelas`**:
   - Complexidade: O(n * m) - Onde `n` é o número de sensores e `m` é o número de regiões. Inicializar uma tabela de tamanho `n * m` é uma operação linear em relação ao número de elementos.

3. **Função `atualizar_tabelas`**:
   - Complexidade: O(m) - Onde `m` é o número de regiões. Para cada par sensor-região, percorremos as regiões anteriores para encontrar a melhor distribuição.

4. **Função `encontrar_distribuicao_otima`**:
   - Complexidade: O(n * m^2) - Onde `n` é o número de sensores e `m` é o número de regiões. A função realiza uma dupla iteração sobre sensores e regiões, e dentro dela, percorre as regiões anteriores.

## Referências
- Livro: "Introduction to Algorithms" de Cormen, Leiserson, Rivest, e Stein.
- Artigo: "Dynamic Programming for Monitoring Pollution in Marine Environments" publicado no Journal of Environmental Monitoring.