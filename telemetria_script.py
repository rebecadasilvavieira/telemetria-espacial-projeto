import random

def verificar_decolagem(telemetria):
    """
    Verifica se os dados de telemetria estão dentro das faixas seguras estabelecidas.
    Retorna (bool, str) -> (Sucesso, Mensagem)
    """
    # Definição das faixas seguras que estabeleci para a missão
    FAIXAS = {
        "temp_interna": (15, 35),
        "temp_externa": (-50, 100),
        "integridade": 1,
        "energia": 80,
        "pressao": (200, 350),
        "modulos": 1
    }

    # Verificação individual de cada parâmetro crítico
    if not (FAIXAS["temp_interna"][0] <= telemetria["temp_interna"] <= FAIXAS["temp_interna"][1]):
        return False, f"ABORTADA: Temperatura interna ({telemetria['temp_interna']}°C) fora da faixa segura."
    
    if not (FAIXAS["temp_externa"][0] <= telemetria["temp_externa"] <= FAIXAS["temp_externa"][1]):
        return False, f"ABORTADA: Temperatura externa ({telemetria['temp_externa']}°C) fora da faixa segura."
    
    if telemetria["integridade"] != FAIXAS["integridade"]:
        return False, "ABORTADA: Integridade estrutural comprometida (0)."
    
    if telemetria["energia"] < FAIXAS["energia"]:
        return False, f"ABORTADA: Níveis de energia ({telemetria['energia']}%) abaixo do mínimo de 80%."
    
    if not (FAIXAS["pressao"][0] <= telemetria["pressao"] <= FAIXAS["pressao"][1]):
        return False, f"ABORTADA: Pressão dos tanques ({telemetria['pressao']} bar) fora da faixa segura."
    
    if telemetria["modulos"] != FAIXAS["modulos"]:
        return False, "ABORTADA: Módulos críticos não operacionais (0)."

    return True, "PRONTO PARA DECOLAR"

def simular_leitura_dados():
    """
    Simula a leitura de dados de telemetria com valores aleatórios para teste do sistema.
    """
    return {
        "temp_interna": round(random.uniform(10, 40), 2),
        "temp_externa": round(random.uniform(-60, 120), 2),
        "integridade": random.choice([0, 1, 1, 1, 1]), # 80% de chance de estar íntegro
        "energia": round(random.uniform(70, 100), 2),
        "pressao": round(random.uniform(180, 380), 2),
        "modulos": random.choice([0, 1, 1, 1, 1, 1]) # 83% de chance de estar operacional
    }

if __name__ == "__main__":
    print("="*50)
    print("   SISTEMA DE VERIFICAÇÃO DE TELEMETRIA ESPACIAL")
    print("="*50)
    
    # Realizei a simulação de 5 leituras para validar o algoritmo
    for i in range(1, 6):
        print(f"\n>>> Simulação #{i}:")
        dados = simular_leitura_dados()
        print(f"Dados capturados pelos sensores: {dados}")
        
        sucesso, mensagem = verificar_decolagem(dados)
        
        if sucesso:
            # Saída em verde para sucesso (se o terminal suportar cores)
            print(f"STATUS FINAL: \033[92m{mensagem}\033[0m")
        else:
            # Saída em vermelho para falha
            print(f"STATUS FINAL: \033[91m{mensagem}\033[0m")
    
    print("\n" + "="*50)
    print("   VERIFICAÇÃO CONCLUÍDA")
    print("="*50)
