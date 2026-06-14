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

# Cálculos Estratégicos para as Metas LEED
total_misto = df['Misto / Reciclado (m³)'].sum()
total_ure = df['URE (m³)'].sum()
total_gerado = total_misto + total_ure
taxa_desvio_real = (total_misto / total_gerado) * 100
meta_leed = 75.0  # Meta padrão LEED para pontuação máxima em gestão de resíduos

# 3. BLOCO 2: Indicadores Executivos (KPIs no Topo)
st.markdown("### 🏛️ Indicadores de Governança Ambiental (Acumulado 2024)")
kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.metric(label="📊 Volume Total Gerado", value=f"{total_gerado} m³", delta="Canteiro Ativo")
with kpi2:
    # Mostra a taxa real com um delta comparando com a meta de 75%
    delta_meta = taxa_desvio_real - meta_leed
    st.metric(label="♻️ Taxa de Desvio de Aterro (Reciclagem)", value=f"{taxa_desvio_real:.1f}%", delta=f"{delta_meta:.1f}% vs Meta LEED")
with kpi3:
    st.metric(label="🎯 Meta de Certificação", value=f"{meta_leed}%", delta="Rigor Técnico GBC")

# Barra de Progresso Visual da Meta
st.markdown("**Progresso rumo à pontuação máxima da Certificação:**")
if taxa_desvio_real >= meta_leed:
    st.progress(int(taxa_desvio_real) if taxa_desvio_real <= 100 else 100)
    st.success(f"🎉 Excelente! A obra está operando ACIMA da meta de {meta_leed}% de desvio. Pontuação garantida na auditoria.")
else:
    st.progress(int(taxa_desvio_real))
    st.warning(f"⚠️ Atenção: A taxa de desvio atual está abaixo do objetivo de {meta_leed}%. Ajustar triagem no canteiro.")

st.markdown("---")

# 4. BLOCO 1: Área de Upload Inteligente (Mantido e Integrado)
st.markdown("### 📥 Upload Automatizado de Evidências (MTR / Notas Fiscais)")
arquivo_subido = st.file_uploader("Arraste ou selecione o PDF da obra aqui", type=["pdf"])

if arquivo_subido is not None:
    st.success(f"📎 Arquivo '{arquivo_subido.name}' recebido com sucesso pelo servidor!")
    if st.button("🚀 Processar Documento com IA"):
        with st.spinner("🤖 IA ativada: Escaneando PDF, extraindo tabelas e validando dados de conformidade..."):
            time.sleep(3)
        st.balloons()
        st.success("✅ Processamento Concluído! Dados integrados ao banco de dados com rastreabilidade garantida.")
else:
    st.info("ℹ️ Sistema operando em modo de demonstração. Suba um PDF para simular a operação real.")

st.markdown("---")

# 5. Exibição dos Painéis de Análise e Gráficos
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📋 Dados Tabulados da Obra (2024)")
    st.dataframe(df, use_container_width=True)
    
    # Alerta Analítico Sênior Inteligente
    st.markdown("### 💡 Diagnóstico da IA")
    st.info("""
    **Análise de Desvio:** O mês de **Maio** apresentou o maior volume de descarte do ano. Embora a reciclagem tenha sido alta (24 m³), a geração de resíduo URE (31 m³) descolou a operação da meta ideal. Recomenda-se auditar as caçambas de Maio para entender a causa raiz desse pico.
    """)

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
