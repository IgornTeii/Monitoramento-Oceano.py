import numpy as np
import unittest

def calcular_distancia(ponto1, ponto2):
    """
    Calcula a distância euclidiana entre dois pontos.
    
    :param ponto1: Coordenadas do ponto 1 (x, y)
    :param ponto2: Coordenadas do ponto 2 (x, y)
    :return: Distância euclidiana entre ponto1 e ponto2
    """
    # Complexidade: O(1) - Operação constante
    return np.sqrt((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)

def inicializar_tabelas(num_sensores, num_regioes):
    """
    Inicializa as tabelas de programação dinâmica e de regiões monitoradas.
    
    :param num_sensores: Número de sensores
    :param num_regioes: Número de regiões
    :return: Tabela DP e tabela de regiões monitoradas
    """
    # Complexidade: O(n * m) - Onde n é o número de sensores e m é o número de regiões
    dp = [[0 for _ in range(num_regioes + 1)] for _ in range(num_sensores + 1)]
    regioes_monitoradas = [[[] for _ in range(num_regioes + 1)] for _ in range(num_sensores + 1)]
    return dp, regioes_monitoradas

def atualizar_tabelas(sensor_idx, regiao_idx, sensores, regioes, capacidade_sensores, dp, regioes_monitoradas):
    """
    Atualiza as tabelas DP e de regiões monitoradas para um sensor e região específicos.
    
    :param sensor_idx: Índice do sensor
    :param regiao_idx: Índice da região
    :param sensores: Lista de coordenadas dos sensores
    :param regioes: Lista de coordenadas das regiões a serem monitoradas
    :param capacidade_sensores: Capacidade máxima de cada sensor
    :param dp: Tabela DP
    :param regioes_monitoradas: Tabela de regiões monitoradas
    """
    # Complexidade: O(m) - Onde m é o número de regiões (para cada iteração de sensor e região)
    dp[sensor_idx][regiao_idx] = dp[sensor_idx - 1][regiao_idx]
    regioes_monitoradas[sensor_idx][regiao_idx] = regioes_monitoradas[sensor_idx - 1][regiao_idx][:]
    for k in range(regiao_idx):
        distancia = calcular_distancia(sensores[sensor_idx - 1], regioes[k])
        if distancia <= capacidade_sensores[sensor_idx - 1]:
            if dp[sensor_idx - 1][k] + 1 > dp[sensor_idx][regiao_idx]:
                dp[sensor_idx][regiao_idx] = dp[sensor_idx - 1][k] + 1
                regioes_monitoradas[sensor_idx][regiao_idx] = regioes_monitoradas[sensor_idx - 1][k] + [regioes[k]]

def encontrar_distribuicao_otima(sensores, regioes, capacidade_sensores):
    """
    Encontra a distribuição ótima de sensores usando programação dinâmica.
    
    :param sensores: Lista de coordenadas dos sensores
    :param regioes: Lista de coordenadas das regiões a serem monitoradas
    :param capacidade_sensores: Capacidade máxima de cada sensor (número de regiões que pode monitorar)
    :return: Lista de regiões atribuídas a cada sensor
    """
    num_sensores = len(sensores)
    num_regioes = len(regioes)
    
    dp, regioes_monitoradas = inicializar_tabelas(num_sensores, num_regioes)
    
    for sensor_idx in range(1, num_sensores + 1):
        for regiao_idx in range(1, num_regioes + 1):
            atualizar_tabelas(sensor_idx, regiao_idx, sensores, regioes, capacidade_sensores, dp, regioes_monitoradas)
    
    # Complexidade: O(n * m^2) - Onde n é o número de sensores e m é o número de regiões
    return [regioes_monitoradas[i + 1][num_regioes] for i in range(num_sensores)]

# Dados fictícios
sensores = [(0, 0), (5, 5), (10, 10)]
regioes = [(1, 1), (2, 2), (3, 3), (6, 6), (7, 7), (8, 8)]
capacidade_sensores = [3, 2, 2]  # Quantidade máxima de regiões que cada sensor pode monitorar

# Calcula a distribuição ótima dos sensores
distribuicao_otima = encontrar_distribuicao_otima(sensores, regioes, capacidade_sensores)

# Exibe a distribuição ótima dos sensores
print("Distribuição Ótima de Sensores:")
for i, regioes_sensor in enumerate(distribuicao_otima):
    print(f"Sensor {i + 1}: {regioes_sensor}")

# Testes
class TestMonitoramentoPoluicaoOceano(unittest.TestCase):
    def test_calcular_distancia(self):
        # Testa a função calcular_distancia com pontos conhecidos
        self.assertAlmostEqual(calcular_distancia((0, 0), (3, 4)), 5.0)
        self.assertAlmostEqual(calcular_distancia((1, 1), (4, 5)), 5.0)
        self.assertAlmostEqual(calcular_distancia((2, 2), (5, 6)), 5.0)

    def test_encontrar_distribuicao_otima(self):
        # Testa a função encontrar_distribuicao_otima com dados fictícios
        sensores = [(0, 0), (5, 5), (10, 10)]
        regioes = [(1, 1), (2, 2), (3, 3), (6, 6), (7, 7), (8, 8)]
        capacidade_sensores = [3, 2, 2]  # Quantidade máxima de regiões que cada sensor pode monitorar

        distribuicao_otima = encontrar_distribuicao_otima(sensores, regioes, capacidade_sensores)

        # Verifica se o resultado é uma lista
        self.assertIsInstance(distribuicao_otima, list)
        # Verifica se a lista contém três elementos (um para cada sensor)
        self.assertEqual(len(distribuicao_otima), 3)
        # Verifica se cada elemento na lista é uma lista (de regiões)
        for regioes_sensor in distribuicao_otima:
            self.assertIsInstance(regioes_sensor, list)

if __name__ == "__main__":
    # Executa os testes
    unittest.main()