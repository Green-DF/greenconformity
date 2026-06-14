import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Configuração da Página do seu Site
st.set_page_config(page_title="GreenConformity - Gestão Ambiental", layout="wide")

st.title("🌱 Plataforma GreenConformity")
st.subheader("Painel Sênior de Conformidade Ambiental e Certificação")
st.markdown("---")

# 2. Simulando o Banco de Dados com as informações de 2024 que você enviou
dados = {
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'Misto / Reciclado (m³)': [13, 2, 3, 4, 24, 5, 4, 8, 4, 6, 1, 3],
    'URE (m³)': [2, 2, 8, 20, 31, 10, 6, 8, 16, 13, 7, 3]
}
df = pd.DataFrame(dados)

# 3. Criando a interface em colunas no site
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📋 Dados Tabulados da Obra")
    st.write("Estes dados serão extraídos automaticamente dos PDFs no futuro:")
    # Mostra a tabela interativa na tela do site
    st.dataframe(df, use_container_width=True)

with col2:
    st.markdown("### 📊 Gráfico de Desempenho Operacional")
    
    # Gerando o gráfico sobreposto para renderizar na página web
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df['Mês'], df['Misto / Reciclado (m³)'], color='#2e7d32', marker='o', linewidth=2.5, label='Misto/Reciclado')
    ax.plot(df['Mês'], df['URE (m³)'], color='#d32f2f', marker='s', linewidth=2.5, label='URE')
    ax.set_ylabel('Quantidade de Caçambas / Volume')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()
    
    # Exibe o gráfico de forma nativa no site
    st.pyplot(fig)

st.markdown("---")
st.info("💡 Próximo Módulo: Ativação do botão de Upload de PDFs com inteligência artificial para leitura de Notas Fiscais e MTRs.")
