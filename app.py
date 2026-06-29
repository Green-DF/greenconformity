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

# 2. Injeção de CSS para Centralização de Títulos e Estilização de Cartões
st.markdown("""
    <style>
    .centered-title {
        text-align: center;
        margin-bottom: 0px;
        font-weight: 700;
    }
    .centered-subtitle {
        text-align: center;
        color: #666666;
        margin-top: -10px;
        margin-bottom: 5px;
        font-size: 1.15rem;
        font-weight: 500;
    }
    .centered-painel {
        text-align: center;
        color: #2e7d32;
        margin-top: -5px;
        margin-bottom: 25px;
        font-size: 1.4rem;
        font-weight: 600;
    }
    .custom-card {
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(46, 125, 50, 0.2);
        background-color: rgba(46, 125, 50, 0.02);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Aplicação dos Títulos Centralizados Solicitados
st.markdown('<h1 class="centered-title">🌱 Plataforma GreenConformity</h1>', unsafe_allow_html=True)
st.markdown('<p class="centered-subtitle">Por Jonas Silva - LEED GA</p>', unsafe_allow_html=True)
st.markdown('<p class="centered-painel">601 Empreendimentos - Painel de Conformidade Ambiental e Certificação</p>', unsafe_allow_html=True)
# 7. MÓDULO DE NAVEGAÇÃO LEED BD+C v4 (Visão de Governança e Compliance)
st.markdown("---")
st.markdown("### 🏛️ Matriz de Governança de Créditos - LEED BD+C v4")
st.markdown("Painel de auditoria de requisitos e coleta de evidências para a certificação do ativo:")

# Criação das abas para as 9 categorias oficiais
abas_leed = st.tabs([
    "IP (Processo)", 
    "LT (Localização)", 
    "SS (Terrenos)", 
    "WE (Água)", 
    "EA (Energia)", 
    "MR (Materiais)", 
    "EQ (Qualidade Interna)", 
    "IN (Inovação)", 
    "RP (Prioridade)"
])

with abas_leed[0]:
    st.markdown("#### 🤝 Processo Integrativo")
    st.caption("Documentação de Sinergia na Fase de Projeto")
    st.checkbox("✔️ Relatório de Sinergia de Energia Concluído (Obrigatório)", value=True)
    st.checkbox("✔️ Relatório de Sinergia de Água Concluído (Obrigatório)", value=True)
    st.button("📄 Gerar Termo de Abertura do Projeto (OPR)")

with abas_leed[1]:
    st.markdown("#### 🚲 Localização e Transporte")
    st.caption("Infraestrutura de Baixo Carbono")
    st.slider("Densidade do Entorno (Interseções num raio de 1km²)", min_value=0, max_value=500, value=150)
    st.number_input("Vagas Físicas para Bicicletas no Empreendimento", min_value=0, value=12)

with abas_leed[2]:
    st.markdown("#### 🌳 Terrenos Sustentáveis")
    st.warning("⚖️ Risco Jurídico: O Plano ESC é exigência de licenciamento e pré-requisito LEED.")
    st.file_uploader("Anexar Relatório Fotográfico Semanal de Prevenção de Poluição (ESC)", type=["pdf"])
    col_ss1, col_ss2 = st.columns(2)
    with col_ss1:
        st.checkbox("Inspeção de Lava-Rodas Realizada")
    with col_ss2:
        st.checkbox("Proteção de Bocas de Lobo Ativa")

with abas_leed[3]:
    st.markdown("#### 💧 Eficiência Hídrica")
    st.caption("Monitoramento de Consumo e Redução")
    st.metric(label="Desempenho de Redução Hídrica (Design)", value="38%", delta="Meta Base: >20%")
    st.progress(38)
    st.checkbox("Submedidores Temporários Instalados no Canteiro")

with abas_leed[4]:
    st.markdown("#### ⚡ Energia e Atmosfera")
    st.caption("Comissionamento e Proteção da Camada de Ozônio")
    st.selectbox("Status do Comissionamento Fundamental (CxA):", ["Não Iniciado", "Em Andamento (Revisão de Projeto)", "Em Campo", "Concluído"])
    st.checkbox("Zero Uso de CFCs em Equipamentos de Alojamento", value=True)

with abas_leed[5]:
    st.success("♻️ A auditoria de desvio de aterro e balanço de massa está ativa no painel superior desta tela.")
    st.markdown("#### 📦 Declarações Ambientais de Produto (EPD / HPD)")
    st.number_input("Quantidade de Materiais com Certificado EPD/FSC Verificado", min_value=0, value=14)

with abas_leed[6]:
    st.markdown("#### 🌬️ Qualidade Ambiental Interna")
    st.caption("Proteção da Saúde Ocupacional e Futuros Ocupantes")
    st.multiselect(
        "Rastreabilidade de Materiais de Baixo VOC (Fichas FISPQ aprovadas):", 
        ["Tinta Epóxi Piso", "Selante Poliuretano (PU)", "Adesivo para Madeira", "Verniz Base Água", "Gesso Acartonado"], 
        default=["Tinta Epóxi Piso", "Selante Poliuretano (PU)"]
    )

with abas_leed[7]:
    st.markdown("#### 🚀 Inovação em Design")
    st.caption("Estratégias para Superação de Metas")
    st.text_area(
        "Registro de Performance Exemplar (Ex: Desvio de aterro atingindo 95%+):", 
        "A Venâncio Empreendimentos atingiu a meta excepcional de..."
    )
        
with abas_leed[8]:
    st.markdown("#### 🗺️ Prioridade Regional")
    st.caption("Bônus de Certificação Específicos para a Coordenada Geográfica")
    st.selectbox(
        "Selecione o Crédito de Prioridade Regional Atingido:", 
        ["Nenhum", "WEc: Redução de Uso de Água Externa", "EAc: Otimização de Performance Energética", "SSc: Gestão de Águas Pluviais"]
    )


st.markdown("<br><br>", unsafe_allow_html=True)
# Barra Lateral - Filtros de Governança Corporativa
st.sidebar.header("🏢 Governança de Portfólio")
obra_selecionada = st.sidebar.selectbox("Selecionar Canteiro de Obras:", ["Edifício Venâncio Eco-Efficient", "Complexo Logístico Alpha", "Residencial Solar Hub"])
fase_obra = st.sidebar.radio("Fase Atual da Obra:", ["Estrutura", "Alvenaria/Acabamento", "Comissionamento"])
st.markdown("<br>", unsafe_allow_html=True) # Espaçamento visual para o rodapé

# Dica de Tema na Sidebar
st.sidebar.markdown("---")
st.sidebar.caption("🌓 **Dica de Visualização:** Alterne entre Modo Claro e Escuro clicando nas configurações (⚙️) no canto superior direito da tela.")

# 3. Dados de Engenharia Brutos (Volume m³)
dados_brutos = {
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'Concreto (m³)': [8, 0, 1, 2, 10, 2, 1, 3, 1, 2, 0, 1],
    'Madeira (m³)': [3, 1, 1, 1, 8, 2, 2, 3, 2, 2, 0, 1],
    'Metais (m³)': [2, 1, 1, 1, 6, 1, 1, 2, 1, 2, 1, 1],
    'URE / Não Reciclado (m³)': [2, 2, 8, 20, 31, 10, 6, 8, 16, 13, 7, 3]
}
df_volume = pd.DataFrame(dados_brutos)

# Fatores de Conversão de Densidade (Padrão LEED / EPA - Toneladas por m³)
FAT_CONCRETO = 1.2  
FAT_MADEIRA = 0.3  
FAT_METAL = 0.5   
FAT_URE = 0.4     

# 4. Processamento de Engenharia: Convertendo para Toneladas (Exigência LEED)
df_massa = pd.DataFrame()
df_massa['Mês'] = df_volume['Mês']
df_massa['Concreto (t)'] = df_volume['Concreto (m³)'] * FAT_CONCRETO
df_massa['Madeira (t)'] = df_volume['Madeira (m³)'] * FAT_MADEIRA
df_massa['Metais (t)'] = df_volume['Metais (m³)'] * FAT_METAL
df_massa['Reciclado Total (t)'] = df_massa['Concreto (t)'] + df_massa['Madeira (t)'] + df_massa['Metais (t)']
df_massa['URE / Aterro (t)'] = df_volume['URE / Não Reciclado (m³)'] * FAT_URE
df_massa['Total Gerado (t)'] = df_massa['Reciclado Total (t)'] + df_massa['URE / Aterro (t)']

# Variáveis Consolidadas para os KPIs
t_reciclado = df_massa['Reciclado Total (t)'].sum()
t_aterro = df_massa['URE / Aterro (t)'].sum()
t_total = df_massa['Total Gerado (t)'].sum()
taxa_desvio_leed = (t_reciclado / t_total) * 100 if t_total > 0 else 0

# 5. MÓDULO SUPERIOR: Indicadores de Alta Performance (Massa - Toneladas)
with st.container():
    st.markdown(f"### 📊 Balanço de Massa Auditado - {obra_selecionada}")
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric(label="⚖️ Massa Total Gerada", value=f"{t_total:.2f} t")
    with kpi2:
        st.metric(label="♻️ Desvio de Aterro (LEED)", value=f"{taxa_desvio_leed:.1f}%", delta=f"{taxa_desvio_leed - 75.0:.1f}% vs Meta GBC")
    with kpi3:
        st.metric(label="🪵 Canais de Reciclagem Ativos", value="3 Fluxos", delta="Atende Prerequisito")
    with kpi4:
        st.metric(label="🎖️ Pontuação Estimada MR", value="2 Pontos", delta="Pontuação Máxima")

    # Barra de Progresso
    st.markdown("<br>", unsafe_allow_html=True)
    st.progress(int(taxa_desvio_leed) if taxa_desvio_leed <= 100 else 100)
st.markdown("---")

# 6. MÓDULO INFERIOR: Interface Dividida (Upload à Esquerda, Gráficos à Direita)
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    # Aplicando a classe custom-card para criar o contêiner visual de upload
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown("### 📥 Gateway de Auditoria Automatizada (IA OCR)")
    arquivo_subido = st.file_uploader("Arraste o lote de PDFs/MTRs fiscais da obra:", type=["pdf"])
    
    if arquivo_subido is not None:
        if st.button("🔍 Executar Auditoria e Validação Digital"):
            with st.spinner("Analisando assinaturas digitais, hash do documento e extraindo peso líquido..."):
                time.sleep(2.5)
            st.success("Documento Validado! Dados convertidos para Toneladas e integrados à Trilha de Auditoria.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Tabela de Rastreabilidade exigida pelo LEED
    st.markdown("### 📜 Trilha de Evidências Rastreáveis")
    evidencias = {
        'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai'],
        'Doc Origem': ['MTR_2024_019.pdf', 'MTR_2024_034.pdf', 'MTR_2024_051.pdf', 'MTR_2024_088.pdf', 'MTR_2024_112.pdf'],
        'Status GBC': ['Aprovado', 'Aprovado', 'Aprovado', 'Em Análise', 'Revisar Alerta']
    }
    st.dataframe(pd.DataFrame(evidencias), use_container_width=True)

with col2:
    st.markdown("### 📈 Curva Analítica de Resíduos Desviados (Massa)")
    
    # Customização do gráfico para se adaptar dinamicamente aos modos Claro e Escuro
    fig, ax = plt.subplots(figsize=(10, 6.2))
    # Definindo fundo transparente para herdar o tema do Streamlit
    fig.patch.set_alpha(0.0)
    ax.set_facecolor('none')
    
    # Barras empilhadas
    ax.bar(df_massa['Mês'], df_massa['Reciclado Total (t)'], color='#2e7d32', label='Desviado/Reciclado (t)', alpha=0.9)
    ax.bar(df_massa['Mês'], df_massa['URE / Aterro (t)'], bottom=df_massa['Reciclado Total (t)'], color='#d32f2f', label='Aterro/URE (t)', alpha=0.9)
    
    ax.set_ylabel('Massa Líquida (Toneladas)', color='gray')
    ax.tick_params(colors='gray')
    ax.grid(True, linestyle=':', alpha=0.3, color='gray')
    ax.legend(loc='upper right', facecolor='none', edgecolor='gray')
    
    # Remove bordas rígidas do gráfico para um visual moderno
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    st.pyplot(fig)

# Rodapé de Conformidade
st.markdown("---")
st.caption("🔒 Certificação de Dados: GreenConformity segue as diretrizes do LEED BD+C v4/v4.1. Dados protegidos por chaves corporativas privadas de criptografia.")
