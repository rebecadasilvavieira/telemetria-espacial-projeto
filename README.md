# Projeto de Telemetria Espacial - Verificação de Decolagem

Este projeto simula um sistema de telemetria para veículos espaciais, capaz de decidir entre "PRONTO PARA DECOLAR" ou "DECOLAGEM ABORTADA" com base em parâmetros críticos de segurança.

🚀 Funcionalidades
- **Monitoramento de Telemetria**: Leitura de temperatura, pressão, energia e integridade.
- **Algoritmo de Decisão**: Lógica baseada em faixas seguras predefinidas.
- **Simulação em Python**: Script para testar diferentes cenários de voo.
- **Análise Energética**: Cálculo de autonomia e perdas.

📊 Parâmetros de Segurança
| Parâmetro | Descrição | Faixa Segura |
| :--- | :--- | :--- |
| Temperatura Interna | Calor nos sistemas eletrônicos e cabine. | 15°C a 35°C |
| Temperatura Externa | Calor da fuselagem e ambiente externo. | -50°C a 100°C |
| Integridade Estrutural | Status dos sensores de tensão e fissuras. | 1 (Íntegro) |
| Níveis de Energia | Carga das baterias principais. | > 80% |
| Pressão dos Tanques | Pressão do combustível e oxidante. | 200 a 350 bar |
| Status Módulos Críticos | Sistemas de navegação e comunicação. | 1 (Operacional) |


🛠️ Como Clonar e Executar
Para rodar este projeto em sua máquina local, siga os passos abaixo:

1. **Clonar o Repositório**:
   Abra o seu terminal (CMD ou PowerShell) e digite:
   ```bash
   git clone https://github.com/rebecadasilvavieira/telemetria-espacial-projeto
   ```
2. **Entrar na Pasta do Projeto**:
   ```bash
   cd telemetria-espacial-projeto
   ```
3. **Executar o Script**:
   Certifique-se de ter o Python 3 instalado e execute:
   ```bash
   python telemetria_script.py
   ```
4. **Executar via Notebook**:
   Caso prefira, você também pode abrir o arquivo `telemetria_notebook.ipynb` em um ambiente Jupyter Notebook ou VS Code para visualizar a execução passo a passo.

📸 Exemplo de Execução
```text
--- SISTEMA DE VERIFICAÇÃO DE TELEMETRIA ---
Simulação #1:
Dados lidos: {'temp_interna': 22.87, 'temp_externa': 115.29, 'integridade': 1, 'energia': 83.41, 'pressao': 206.05, 'modulos': 1}
RESULTADO: ABORTADA: Temperatura externa (115.29°C) fora da faixa segura.

Simulação #2:
Dados lidos: {'temp_interna': 17.24, 'temp_externa': -7.5, 'integridade': 1, 'energia': 82.63, 'pressao': 345.83, 'modulos': 1}
RESULTADO: PRONTO PARA DECOLAR
```

📝 Licença
Este projeto foi desenvolvido para fins educacionais.
