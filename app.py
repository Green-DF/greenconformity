import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

# 1. CONFIGURAÇÃO DE LIDERANÇA E DESIGN
st.set_page_config(
    page_title="GreenConformity Global | 601 Empreendimentos", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. INJEÇÃO DE DESIGN DE ELITE (CSS)
st.markdown("""
    <style>
    /* Estilização Geral e Fontes */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    /* Centralização e Design de Cabeçalho */
    .header-container { text-align: center; padding: 20px 0 40px 0; }
    .main-title { font-size: 3.2rem; font-weight: 800; color: #1B5E20; letter-spacing: -1px; margin-bottom: 0px; }
    .leed-ga { font-size: 1.2rem; font-weight: 500; color: #666; margin-top: -10px; text-transform: uppercase; letter-spacing: 2px; }
    .painel-601 { font-size: 1.5rem; font-weight: 600; color: #2E7D32; background: rgba(46, 125, 50, 0.1); padding: 10px 20px; border-radius: 50px; display: inline-block; margin-top: 15px; }

    /* Estilização de Cartões e Métricas */
    [data-testid="stMetricValue"] { font-size: 2.2rem !important; font-weight: 700 !important; color: #2E7D32 !important; }
    .stMetric { background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 15px; border: 1px solid rgba(46, 125, 50, 0.1); box-shadow: 0 4px 15px rgba(0,0,0,0.05); }

    /* Alertas Estilizados */
    .alert-box { padding: 15px; border-radius: 12px; margin-bottom: 10px; border-left: 5px solid; }
    .alert-critical { background: #FFEBEE; border-color: #D32F2F; color: #C62828; }
    .alert-warning { background: #FFFDE7; border-color: #FBC02D; color: #F57F17; }
    .alert-success { background: #E8F5E9; border-color: #2E7D32; color: #1B5E20; }

    /* Abas de Design Fino */
    .stTabs [data-baseweb="tab-list"] { gap: 30px; }
    .stTabs [data-baseweb="tab"] { height: 50px; font-weight: 600; font-size: 1.1rem; border-radius: 10px 10px 0 0; }
    </style>
""", unsafe_allow_html=True)

# 3. ENGINE DE CÁLCULOS TÉCNICOS (LEED BD+C)
dados_brutos = {
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'Concreto (m³)': [8, 0, 1, 2, 10, 2, 1, 3, 1, 2, 0, 1],
    'Madeira (m³)': [3, 1, 1, 1, 8, 2, 2, 3, 2, 2, 0, 1],
    'Metais (m³)': [2, 1, 1, 1, 6, 1, 1, 2, 1, 2, 1, 1],
    'URE (m³)': [2, 2, 8, 20, 31, 10, 6, 8, 16, 13, 7, 3]
}
df_vol = pd.DataFrame(dados_brutos)
# Conversão para Toneladas
massa_rec = (df_vol['Concreto (m³)']*1.2) + (df_vol['Madeira (m³)']*0.3) + (df_vol['Metais (m³)']*0.5)
massa_ure = df_vol['URE (m³)']*0.4
conf_res = (massa_rec.sum() / (massa_rec.sum() + massa_ure.sum())) * 100
conf_ene, conf_agu, conf_tra = 78.5, 84.2, 65.0
indice_global = (conf_res + conf_ene + conf_agu + conf_tra) / 4

# 4. HEADER CENTRALIZADO (MARCA JONAS SILVA / 601)
st.markdown(f"""
    <div class="header-container">
        <h1 class="main-title">🌱 Plataforma GreenConformity</h1>
        <p class="leed-ga">Por Jonas Silva - LEED GA</p>
        <p class="painel-601">Painel de Conformidade Ambiental e Certificação 601 Empreendimentos</p>
    </div>
""", unsafe_allow_html=True)

# 5. DASHBOARD EXECUTIVO (KPIs + GAUGE)
st.sidebar.image("https://www.usgbc.org/sites/default/files/leed-ga-logo.png", width=100)
st.sidebar.header("🗺️ Navegação Global")
obra = st.sidebar.selectbox("Canteiro Ativo:", ["Edifício Venâncio Eco-Efficient", "Alpha Log", "Solar Hub"])

col_kpi, col_gauge = st.columns([2, 1])

with col_kpi:
    st.markdown("### 🏆 Performance de Certificação")
    k1, k2, k3 = st.columns(3)
    k1.metric("Índice Global", f"{indice_global:.1f}%", "Top 1% Mundial")
    k2.metric("Nível Atual", "LEED GOLD", "+4 pts para Platinum")
    k3.metric("Créditos Concluídos", "34 / 45", "Avançado")
    st.progress(int(indice_global))

with col_gauge:
    # Gauge Chart Minimalista
    fig_g, ax_g = plt.subplots(figsize=(4, 2.5))
    fig_g.patch.set_alpha(0.0)
    ang = np.linspace(0, np.pi, 100)
    ax_g.plot(np.cos(ang), np.sin(ang), color='#e0e0e0', lw=15, solid_capstyle='round')
    ax_g.plot(np.cos(np.linspace(np.pi, np.pi*(1-indice_global/100), 100)), 
              np.sin(np.linspace(np.pi, np.pi*(1-indice_global/100), 100)), color='#2E7D32', lw=15, solid_capstyle='round')
    ax_g.text(0, 0.15, f"{indice_global:.0f}%", fontsize=28, fontweight='bold', ha='center', color='#1B5E20')
    ax_g.axis('off')
    st.pyplot(fig_g)

# 6. CENTRAL DE ALERTAS INTELIGENTES
st.markdown("---")
a1, a2, a3 = st.columns(3)
with a1:
    if conf_tra < 70:
        st.markdown(f'<div class="alert-box alert-critical"><b>🚨 CRÍTICO: TRANSPORTE ({conf_tra:.0f}%)</b><br>Déficit em vagas verdes e acessibilidade. Risco de glosa de crédito.</div>', unsafe_allow_html=True)
with a2:
    st.markdown(f'<div class="alert-box alert-warning"><b>⚠️ ALERTA: RESÍDUOS</b><br>Pico de URE identificado em Maio (31m³). Auditoria recomendada.</div>', unsafe_allow_html=True)
with a3:
    st.markdown(f'<div class="alert-box alert-success"><b>✅ EFICIÊNCIA: ÁGUA ({conf_agu:.1f}%)</b><br>Redução de consumo interno superando a Baseline em 32%.</div>', unsafe_allow_html=True)

# 7. MÓDULOS DE CONFORMIDADE (WORKSPACE)
st.markdown("### 🗂️ Workspace de Certificação BD+C")
tab_mr, tab_ea, tab_we, tab_lt = st.tabs(["♻️ Matérias e Recursos", "⚡ Energia e Atmosfera", "💧 Eficiência de Água", "🚗 Localização e Transporte"])

# --- TAB RESÍDUOS ---
with tab_mr:
    col_up, col_vis = st.columns([1, 1], gap="large")
    with col_up:
        st.markdown("#### 🛡️ Blindagem de Evidências (MR)")
        st.file_uploader("Upload de Notas Fiscais e MTRs (PDF):", type=["pdf"], key="mr_up", help="Arquivos serão auditados via IA OCR.")
        st.dataframe(pd.DataFrame({
            'Data': ['15/01','22/02','10/03'], 'Documento': ['MTR_001.pdf','MTR_045.pdf','CDF_088.pdf'], 'Status': ['Validado','Validado','Em Análise']
        }), use_container_width=True)
    with col_vis:
        st.markdown("#### Fluxo de Massa (Toneladas)")
        fig_mr, ax_mr = plt.subplots(figsize=(10, 5))
        fig_mr.patch.set_alpha(0.0)
        ax_mr.bar(df_vol['Mês'], massa_rec, color='#2E7D32', label='Reciclado (t)')
        ax_mr.bar(df_vol['Mês'], massa_ure, bottom=massa_rec, color='#C62828', label='Aterro (t)')
        ax_mr.legend()
        st.pyplot(fig_mr)

# --- TAB ENERGIA ---
with tab_ea:
    col_up, col_vis = st.columns([1, 1], gap="large")
    with col_up:
        st.markdown("#### ⚡ Monitoramento Energético (EA)")
        st.file_uploader("Faturas de Energia Elétrica e Relatórios de Comissionamento:", type=["pdf", "csv"], key="ea_up")
        st.metric("Consumo Acumulado", "42.850 kWh", "-5.2% vs Baseline")
    with col_vis:
        st.markdown("#### Curva de Demanda Operacional")
        st.line_chart(pd.DataFrame({'kWh': [3500, 3200, 4100, 4500, 5200, 4800, 4100, 3900, 3800, 4200, 3100, 2900]}, index=df_vol['Mês']))

# --- TAB ÁGUA ---
with tab_we:
    col_up, col_vis = st.columns([1, 1], gap="large")
    with col_up:
        st.markdown("#### 💧 Balanço Hídrico (WE)")
        st.file_uploader("Leituras de Hidrômetros e Datasheets de Metais:", type=["pdf"], key="we_up")
        st.info("💡 Meta LEED: Redução sustentada em 32% vs Baseline ASHRAE.")
    with col_vis:
        st.markdown("#### Distribuição de Uso Interno")
        fig_we, ax_we = plt.subplots(figsize=(6, 4))
        fig_we.patch.set_alpha(0.0)
        ax_we.pie([55, 30, 15], labels=['Metais', 'Processos', 'Perdas'], autopct='%1.1f%%', colors=['#0288D1','#4FC3F7','#B3E5FC'])
        st.pyplot(fig_we)

# --- TAB TRANSPORTE ---
with tab_lt:
    col_up, col_vis = st.columns([1, 1], gap="large")
    with col_up:
        st.markdown("#### 🚗 Localização e Transporte (LT)")
        st.file_uploader("Evidências Fotográficas e Mapas de Entorno:", type=["pdf", "jpg"], key="lt_up")
        st.warning("🚨 Requisito Pendente: Vagas Preferenciais (Carpool) não sinalizadas.")
    with col_vis:
        st.markdown("#### Checklist de Conformidade LT")
        st.table(pd.DataFrame({
            "Critério": ["Vagas EV", "Bicicletários", "Acesso Trânsito", "Vagas Carona"],
            "Meta": [5, 20, "1/4 mi", 8], "Real": [3, 20, "0.2 mi", 4], "Status": ["⚠️","✅","✅","❌"]
        }))

# RODAPÉ
st.markdown("---")
st.caption("🔒 GreenConformity Cloud: Blindagem de Dados em conformidade com LEED BD+C v4.1 e LGPD. 601 Empreendimentos - Excelência Mundial.")
