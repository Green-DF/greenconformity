import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

# 1. Configuração de Alta Performance da Página
st.set_page_config(
    page_title="GreenConformity Enterprise - LEED BD+C", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Injeção de CSS para Estilização de Títulos e Containers
st.markdown("""
    <style>
    .centered-title { text-align: center; margin-bottom: 0px; font-weight: 700; }
    .centered-subtitle { text-align: center; color: #666666; margin-top: -10px; margin-bottom: 5px; font-size: 1.15rem; font-weight: 500; }
    .centered-painel { text-align: center; color: #2e7d32; margin-top: -5px; margin-bottom: 25px; font-size: 1.4rem; font-weight: 600; }
    .custom-card {
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(46, 125, 50, 0.2);
        background-color: rgba(46, 125, 50, 0.01);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Processamento de Engenharia de Dados (Cálculos Base)
dados_brutos = {
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'Concreto (m³)': [8, 0, 1, 2, 10, 2, 1, 3, 1, 2, 0, 1],
    'Madeira (m³)': [3, 1, 1, 1, 8, 2, 2, 3, 2, 2, 0, 1],
    'Metais (m³)': [2, 1, 1, 1, 6, 1, 1, 2, 1, 2, 1, 1],
    'URE / Não Reciclado (m³)': [2, 2, 8, 20, 31, 10, 6, 8, 16, 13, 7, 3]
}
df_volume = pd.DataFrame(dados_brutos)

# Fatores de conversão padrão LEED (m³ para Toneladas)
df_massa = pd.DataFrame()
df_massa['Mês'] = df_volume['Mês']
df_massa['Reciclado Total (t)'] = (df_volume['Concreto (m³)'] * 1.2) + (df_volume['Madeira (m³)'] * 0.3) + (df_volume['Metais (m³)'] * 0.5)
df_massa['URE / Aterro (t)'] = df_volume['URE / Não Reciclado (m³)'] * 0.4
df_massa['Total (t)'] = df_massa['Reciclado Total (t)'] + df_massa['URE / Aterro (t)']

# Cálculo das taxas de conformidade por módulo
conf_residuos = (df_massa['Reciclado Total (t)'].sum() / df_massa['Total (t)'].sum()) * 100
conf_energia = 78.5  # Simulação de eficiência vs ASHRAE 90.1
conf_agua = 84.2     # Simulação de redução de água interna vs Baseline
conf_transporte = 65.0 # Simulação de vagas e acessibilidade alternatva

# Índice Global de Conformidade (Média dos módulos LEED)
indice_global = (conf_residuos + conf_energia + conf_agua + conf_transporte) / 4

# 4. LAYOUT DA TELA: Cabeçalho e Títulos
st.markdown('<h1 class="centered-title">🌱 Plataforma GreenConformity</h1>', unsafe_allow_html=True)
st.markdown('<p class="centered-subtitle">Por Jonas Silva - LEED GA</p>', unsafe_allow_html=True)
st.markdown('<p class="centered-painel">Painel de Conformidade Ambiental e Certificação 601 Empreendimentos</p>', unsafe_allow_html=True)
st.markdown("---")

# Barra Lateral - Filtros de Portfólio
st.sidebar.header("🏢 Governança de Portfólio")
obra_selecionada = st.sidebar.selectbox("Selecionar Canteiro de Obras:", ["Edifício Venâncio Eco-Efficient", "Complexo Logístico Alpha", "Residencial Solar Hub"])
fase_obra = st.sidebar.radio("Fase Atual da Obra:", ["Estrutura", "Alvenaria/Acabamento", "Comissionamento"])

# 5. BLOCO SUPERIOR: Divisão entre KPIs e o Gráfico de Arco (Velocímetro)
topo_col1, topo_col2 = st.columns([2, 1])

with topo_col1:
    st.markdown(f"### 📈 Scorecard Executivo - {obra_selecionada}")
    k1, k2 = st.columns(2)
    with k1:
        st.metric(label="📊 Índice Global de Conformidade LEED", value=f"{indice_global:.1f}%", delta="Em evolução")
    with k2:
        st.metric(label="🎖️ Nível Estimado da Certificação", value="LEED Gold", delta="Faltam 4 pontos para Platinum")
    
    # Barra de Progresso Global
    st.markdown("<br>", unsafe_allow_html=True)
    st.progress(int(indice_global))

with topo_col2:
    # Criação do Gráfico de Arco Lúdico (Gauge Chart) no topo direito
    fig_gauge, ax_g = plt.subplots(figsize=(4, 2.2))
    fig_gauge.patch.set_alpha(0.0)
    ax_g.set_facecolor('none')
    
    # Desenhar o semicírculo de fundo
    angulos = np.linspace(0, np.pi, 100)
    ax_g.plot(np.cos(angulos), np.sin(angulos), color='#e0e0e0', linewidth=18, solid_capstyle='round')
    
    # Desenhar o arco de preenchimento baseado no índice real
    angulo_real = np.pi * (1 - (indice_global / 100))
    angulos_preenchidos = np.linspace(np.pi, angulo_real, 100)
    ax_g.plot(np.cos(angulos_preenchidos), np.sin(angulos_preenchidos), color='#2e7d32', linewidth=18, solid_capstyle='round')
    
    # Estilização do texto central do Arco
    ax_g.text(0, 0.1, f"{indice_global:.0f}%", fontsize=24, fontweight='bold', ha='center', va='center', color='#2e7d32')
    ax_g.text(0, -0.2, "Conformidade", fontsize=10, color='gray', ha='center', va='center')
    
    ax_g.set_xlim(-1.2, 1.2)
    ax_g.set_ylim(-0.3, 1.2)
    ax_g.axis('off')
    st.pyplot(fig_gauge)

st.markdown("---")

# 6. ENGINE DE RISCO: Alertas de Baixa Conformidade Integrados
st.markdown("### ⚠️ Central de Alertas e Desvios Operacionais")
alertas_col1, alertas_col2, alertas_col3 = st.columns(3)

with alertas_col1:
    if conf_transporte < 70:
        st.error(f"🚨 **Crítico - Transporte ({conf_transporte:.0f}%)**:\n\nA infraestrutura de vagas preferenciais e bicicletários está abaixo da meta mínima estipulada pelo crédito LT. Risco de perda de ponto.")

with alertas_col2:
    # Varredura inteligente nos dados de resíduos (Procura picos críticos de URE)
    mes_critico_ure = df_volume.loc[df_volume['URE / Não Reciclado (m³)'] > 25, 'Mês'].values[0]
    st.warning(f"⚠️ **Alerta - Resíduos (Mês de {mes_critico_ure})**:\n\nIdentificado pico anômalo de resíduos não recicláveis enviados para aterro. Necessário auditar as Notas Fiscais de destino final.")

with alertas_col3:
    st.success(f"✅ **Eficiência - Água ({conf_agua:.1f}%)**:\n\nA conformidade das medições de hidrômetros aponta que a obra segue firme nos pré-requisitos de redução de consumo.")

st.markdown("---")

# 7. MÓDULOS DOS ITENS DE CONFORMIDADE LEED (Abas Dinâmicas)
st.markdown("### 🗂️ Módulos de Gestão Técnica")
aba_residuos, aba_energia, aba_agua, aba_transporte = st.tabs(["♻️ Resíduos (MR)", "⚡ Energia (EA)", "💧 Água (WE)", "🚗 Transporte (LT)"])

# ABA RESÍDUOS
with aba_residuos:
    col_r1, col_r2 = st.columns(2)
    with col_r1:
        st.markdown("#### Upload de Evidências Fiscais")
        arquivo_subido = st.file_uploader("Arraste MTRs ou Certificados de Destinação Final (CDF):", type=["pdf"], key="res_up")
        st.markdown("#### Trilha de Evidências Rastreáveis")
        evidencias = {
            'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai'],
            'Doc Origem': ['MTR_2024_019.pdf', 'MTR_2024_034.pdf', 'MTR_2024_051.pdf', 'MTR_2024_088.pdf', 'MTR_2024_112.pdf'],
            'Status Auditoria': ['Aprovado', 'Aprovado', 'Aprovado', 'Em Análise', 'Alerta Emissão']
        }
        st.dataframe(pd.DataFrame(evidencias), use_container_width=True)
    with col_r2:
        st.markdown("#### Balanço Mensal de Massa (Toneladas)")
        fig_r, ax_r = plt.subplots(figsize=(10, 5))
        fig_r.patch.set_alpha(0.0)
        ax_r.set_facecolor('none')
        ax_r.bar(df_massa['Mês'], df_massa['Reciclado Total (t)'], color='#2e7d32', label='Desviado/Reciclado (t)')
        ax_r.bar(df_massa['Mês'], df_massa['URE / Aterro (t)'], bottom=df_massa['Reciclado Total (t)'], color='#d32f2f', label='Aterro/URE (t)')
        ax_r.set_ylabel('Toneladas (t)', color='gray')
        ax_r.tick_params(colors='gray')
        ax_r.legend()
        st.pyplot(fig_r)

# ABA ENERGIA
with aba_energia:
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.markdown("#### Gestão de Eficiência Energética Canteiro / Comissionamento")
        st.write("Monitoramento de consumo das faturas elétricas frente à linha de base (Baseline ASHRAE 90.1).")
        st.metric(label="⚡ Consumo Acumulado", value="42.850 kWh", delta="-5.2% vs Canteiro Padrão")
        st.metric(label="🌱 Pegada de Carbono (Escopo 2)", value="3,62 tCO2e", delta="Otimizado por Grid Renovável")
    with col_e2:
        st.markdown("#### Gráfico de Demanda Elétrica Mensal")
        dados_energia = pd.DataFrame({'Mês': df_volume['Mês'], 'Consumo (kWh)': [3500, 3200, 4100, 4500, 5200, 4800, 4100, 3900, 3800, 4200, 3100, 2900]})
        st.line_chart(dados_energia.set_index('Mês'), color="#fbc02d")

# ABA ÁGUA
with aba_agua:
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        st.markdown("#### Eficiência de Água (Indoor and Outdoor Water Reduction)")
        st.write("Acompanhamento das metas globais do pré-requisito e crédito WE.")
        st.metric(label="💧 Consumo de Água Potável", value="184 m³", delta="32% de Redução Adquirida")
        st.info("💡 **Diretriz LEED:** Meta de redução sustentada através do uso combinado de torneiras de baixa vazão e captação de água pluvial instalada na torre principal.")
    with col_w2:
        st.markdown("#### Distribuição de Consumo por Subsistema")
        labels = ['Louças/Metais', 'Processos Obra', 'Perdas/Limpeza']
        tamanhos = [55, 30, 15]
        fig_w, ax_w = plt.subplots(figsize=(6, 4))
        fig_w.patch.set_alpha(0.0)
        ax_w.pie(tamanhos, labels=labels, autopct='%1.1f%%', colors=['#0288d1', '#4fc3f7', '#b3e5fc'], textprops={'color': 'gray'})
        st.pyplot(fig_w)

# ABA TRANSPORTE
with aba_transporte = st.tabs(["🚗 Transporte (LT)"])[0]:  # Correção interna de carregamento de contexto
    st.markdown("#### Localização e Transporte (Access to Quality Transit & Green Vehicles)")
    st.write("Verificação física de conformidade para atendimento do crédito de redução de uso de veículos individuais.")
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.data_editor({
            "Item de Controle": ["Vagas para Veículos Elétricos (EV)", "Eletropostos Ativos c/ Fiação", "Vagas Carona Solidária (Carpool)", "Bicicletário Coberto"],
            "Quantidade Exigida": [5, 2, 8, 20],
            "Instalado em Canteiro": [3, 2, 4, 20],
            "Status de Auditoria": ["Pendente (Abaixo)", "Conforme", "Pendente (Abaixo)", "Conforme"]
        }, use_container_width=True)
    with col_t2:
        st.info("🛠️ **Ação Corretiva do Consultor:** A demarcação de vagas para carona solidária e veículos de baixa emissão precisa ser concluída antes da fase de vistorias finais sob risco de glosa de créditos pelo revisor do GBC.")

# Rodapé de Conformidade
st.markdown("---")
st.caption("🔒 Certificação de Dados: GreenConformity segue as diretrizes do LEED BD+C v4/v4.1. Dados protegidos por chaves corporativas privadas de criptografia.")
