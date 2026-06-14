import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

# 1. Configuração de Alta Performance da Página
st.set_page_config(page_title="GreenConformity - Gestão Ambiental", layout="wide")

st.title("🌱 Plataforma GreenConformity")
st.subheader("Painel Sênior de Conformidade Ambiental e Certificação")
st.markdown("---")

# 2. Estrutura de Dados Base (Dados de 2024 da Obra)
dados_padrao = {
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'Misto / Reciclado (m³)': [13, 2, 3, 4, 24, 5, 4, 8, 4, 6, 1, 3],
    'URE (m³)': [2, 2, 8, 20, 31, 10, 6, 8, 16, 13, 7, 3]
}
df = pd.DataFrame(dados_padrao)

# 3. BLOCO 1: Área de Upload Inteligente
st.markdown("### 📥 Upload Automatizado de Evidências (MTR / Notas Fiscais)")
st.write("Suba os relatórios mensais de resíduos ou notas de caçambas em formato PDF. A IA fará a leitura e a tabulação automática.")

# Criando o componente de upload na tela
arquivo_subido = st.file_uploader("Arraste ou selecione o PDF da obra aqui", type=["pdf"])

if arquivo_subido is not None:
    st.success(f"📎 Arquivo '{arquivo_subido.name}' recebido com sucesso pelo servidor!")
    
    # Botão para ativar o processamento simulado da IA
    if st.button("🚀 Processar Documento com IA"):
        with st.spinner("🤖 IA ativada: Escaneando PDF, extraindo tabelas e validando dados de conformidade..."):
            time.sleep(3) # Simula o tempo de processamento do robô
        st.balloons() # Efeito visual de sucesso
        st.success("✅ Processamento Concluído! Dados integrados ao banco de dados com rastreabilidade garantida.")
else:
    st.info("ℹ️ Sistema operando em modo de demonstração. Suba um PDF para simular a operação real.")

st.markdown("---")

# 4. Exibição dos Painéis de Análise
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📋 Dados Tabulados da Obra (2024)")
    st.write("Histórico consolidado após auditoria digital:")
    st.dataframe(df, use_container_width=True)

with col2:
    st.markdown("### 📊 Gráfico de Desempenho Operacional")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df['Mês'], df['Misto / Reciclado (m³)'], color='#2e7d32', marker='o', linewidth=2.5, label='Misto/Reciclado (m³)')
    ax.plot(df['Mês'], df['URE (m³)'], color='#d32f2f', marker='s', linewidth=2.5, label='URE (m³)')
    ax.set_ylabel('Volume / Quantidade de Caçambas')
    ax.set_xlabel('Meses do Ano')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc='upper right')
    
    st.pyplot(fig)
