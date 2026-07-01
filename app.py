import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

# 1. Configuração de Alta Performance da Página
st.set_page_config(
    page_title="GreenConformity Enterprise - LEED BD+C", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Injeção de CSS
st.markdown("""
    <style>
    .centered-title { text-align: center; font-weight: 700; }
    .centered-subtitle { text-align: center; color: #666666; font-size: 1.15rem; }
    .centered-painel { text-align: center; color: #2e7d32; font-size: 1.4rem; font-weight: 600; }
    .custom-card { padding: 20px; border-radius: 10px; border: 1px solid rgba(46, 125, 50, 0.2); background-color: rgba(46, 125, 50, 0.02); }
    </style>
""", unsafe_allow_html=True)

# Headers
st.markdown('<h1 class="centered-title">🌱 Plataforma GreenConformity</h1>', unsafe_allow_html=True)
st.markdown('<p class="centered-subtitle">Por Jonas Silva - LEED GA</p>', unsafe_allow_html=True)
st.markdown('<p class="centered-painel">601 Empreendimentos - Painel de Conformidade Ambiental e Certificação</p>', unsafe_allow_html=True)

# 3. MÓDULO ARC-INSPIRED: ENGINE DE SCORE
st.markdown("---")
col_arc1, col_arc2, col_arc3 = st.columns([1, 2, 1])
with col_arc2:
    st.markdown("### 🎯 Score de Performance GreenConformity (ARC-Engine)")
    st.metric(label="Pontuação Geral de Certificação", value="78.5 pts", delta="+2.5 vs último mês")
    st.progress(0.785)
    st.caption("Acompanhamento contínuo baseado nas diretrizes LEED v4.1 O+M")
st.markdown("---")

# 4. Dados de Configuração
categorias = {
    "Integrative Process (IP)": {"budget": 10000, "spent": 4000, "cert": {'Gold': 50, 'Silver': 30, 'Platinum': 20}},
    "Location and Transportation (LT)": {"budget": 20000, "spent": 12000, "cert": {'Gold': 40, 'Silver': 40, 'Platinum': 20}},
    "Sustainable Sites (SS)": {"budget": 50000, "spent": 32000, "cert": {'Gold': 30, 'Silver': 30, 'Platinum': 40}},
    "Water Efficiency (WE)": {"budget": 30000, "spent": 15000, "cert": {'Gold': 60, 'Silver': 20, 'Platinum': 20}},
    "Energy and Atmosphere (EA)": {"budget": 80000, "spent": 75000, "cert": {'Gold': 20, 'Silver': 20, 'Platinum': 60}},
    "Materials and Resources (MR)": {"budget": 120000, "spent": 85000, "cert": {'Gold': 25, 'Silver': 25, 'Platinum': 50}},
    "Indoor Environmental Quality (EQ)": {"budget": 40000, "spent": 20000, "cert": {'Gold': 40, 'Silver': 40, 'Platinum': 20}},
    "Innovation (IN)": {"budget": 15000, "spent": 5000, "cert": {'Gold': 33, 'Silver': 33, 'Platinum': 34}},
    "Regional Priority (RP)": {"budget": 10000, "spent": 2000, "cert": {'Gold': 50, 'Silver': 25, 'Platinum': 25}}
}

# 5. Módulo de Navegação
st.markdown("### 🏛️ Matriz de Governança de Créditos - LEED BD+C v4")
abas_leed = st.tabs(list(categorias.keys()))

def renderizar_aba(nome):
    data = categorias[nome]
    st.markdown(f"#### 🎯 {nome} - Painel de Performance")
    c1, c2, c3 = st.columns([1, 1, 1])
    
    with c1:
        fig, ax = plt.subplots(figsize=(2.5, 2.5))
        ax.pie(data['cert'].values(), labels=data['cert'].keys(), autopct='%1.0f%%', colors=['#FFD700', '#C0C0C0', '#E5E4E2'], startangle=90)
        ax.set_title("Nível de Certificação")
        st.pyplot(fig)
        plt.close(fig) # Correção: evita vazamento de memória
        
    with c2:
        st.write("📈 Tendência de Performance (6 meses):")
        df_trend = pd.DataFrame({'Meses': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'], 'Score': [60, 65, 70, 68, 75, 78]})
        st.line_chart(df_trend.set_index('Meses'))
        
    with c3:
        st.write("💰 Orçamento de Conformidade:")
        st.progress(data['spent'] / data['budget'])
        st.caption(f"Executado: R$ {data['spent']:,.2f}")
        with st.expander("📂 Documentos e Checklist"):
            st.file_uploader(f"Upload {nome}", type=["pdf"], key=f"up_{nome}")
            st.checkbox(f"Requisito atingido", key=f"ch_{nome}")

for i, nome in enumerate(categorias.keys()):
    with abas_leed[i]:
        renderizar_aba(nome)

# 6. Sidebar e Cálculos de Engenharia
st.sidebar.header("🏢 Governança de Portfólio")
obra_selecionada = st.sidebar.selectbox("Selecionar Canteiro de Obras:", ["Edifício Venâncio Eco-Efficient", "Complexo Logístico Alpha", "Residencial Solar Hub"])
fase_obra = st.sidebar.radio("Fase Atual da Obra:", ["Estrutura", "Alvenaria/Acabamento", "Comissionamento"])

# Cálculos (Massa)
dados_brutos = {'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'Concreto (m³)': [8, 0, 1, 2, 10, 2, 1, 3, 1, 2, 0, 1],
    'Madeira (m³)': [3, 1, 1, 1, 8, 2, 2, 3, 2, 2, 0, 1],
    'Metais (m³)': [2, 1, 1, 1, 6, 1, 1, 2, 1, 2, 1, 1],
    'URE / Não Reciclado (m³)': [2, 2, 8, 20, 31, 10, 6, 8, 16, 13, 7, 3]}
df_massa = pd.DataFrame(dados_brutos)
# (Cálculos mantidos conforme original)
t_reciclado = (df_massa['Concreto (m³)']*1.2 + df_massa['Madeira (m³)']*0.3 + df_massa['Metais (m³)']*0.5).sum()
t_total = t_reciclado + (df_massa['URE / Não Reciclado (m³)'] * 0.4).sum()
taxa = (t_reciclado / t_total) * 100 if t_total > 0 else 0

st.markdown("---")
st.markdown(f"### 📊 Balanço de Massa Auditado - {obra_selecionada}")
k1, k2, k3, k4 = st.columns(4)
k1.metric("⚖️ Massa Total", f"{t_total:.2f} t")
k2.metric("♻️ Desvio de Aterro", f"{taxa:.1f}%")
k3.metric("🪵 Canais Ativos", "3 Fluxos")
k4.metric("🎖️ Pontuação MR", "2 Pontos")

st.markdown("---")
# Gateway e Rodapé (Mantidos)
st.caption("🔒 Certificação de Dados: GreenConformity segue as diretrizes do LEED BD+C v4/v4.1.")
