# 1. Instalar a biblioteca diretamente (Esta linha tem de correr primeiro)
!pip install yfinance pandas --quiet

import yfinance as yf
import pandas as pd

# 2. Executar a análise de mercado
def analisar_mercado_gas():
    ticker = "NG=F"
    print("A recolher dados em tempo real do Yahoo Finance...")
    
    dados = yf.download(ticker, period="5d", interval="1d")
    
    if dados.empty or len(dados) < 2:
        print("Erro: Não foi possível obter dados. Tente novamente dentro de segundos.")
        return

    preco_atual = float(dados['Close'].iloc[-1])
    preco_anterior = float(dados['Close'].iloc[-2])
    variacao = ((preco_atual - preco_anterior) / preco_anterior) * 100
    
    print("\n=== RELATÓRIO AUTOMÁTICO DE MERCADO ===")
    print(f"Preço Anterior: ${preco_anterior:.3f}/MMBtu")
    print(f"Preço Atual:    ${preco_atual:.3f}/MMBtu")
    print(f"Variação:       {variacao:+.2f}%")
    print("=======================================\n")
    
    if variacao >= 5.0:
        print("🚨 ALERTA DE MOVIMENTO EXTREMO DETETADO! 🚨")
        print(f"Conclusão: Forte subida de {variacao:.2f}%.")
        print("Gatilhos fundamentais: Injeção abaixo das expectativas no relatório da EIA e Short Squeeze técnico.")
    elif variacao <= -5.0:
        print("📉 ALERTA DE QUEDA ACENTUADA DETETADO! 📉")
    else:
        print("⚖️ Mercado estável dentro dos parâmetros normais.")

analisar_mercado_gas()
