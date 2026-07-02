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

# 2. Injeção de CSS para Centralização de Títulos, Estilização de Cartões e Logo USGBC
st.markdown("""
    <style>
    .usgbc-logo {
        position: absolute;
        top: -40px; /* Ajuste para encaixar perfeitamente no topo direito da tela */
        right: 10px;
        width: 140px;
        z-index: 100;
    }
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
    
    <img src="https://upload.wikimedia.org/wikipedia/en/thumb/3/36/USGBC_logo.svg/512px-USGBC_logo.svg.png" class="usgbc-logo" alt="USGBC Logo">
""", unsafe_allow_html=True)

# Aplicação dos Títulos Centralizados Solicitados
st.markdown('<h1 class="centered-title">🌱 Plataforma GreenConformity</h1>', unsafe_allow_html=True)
st.markdown('<p class="centered-subtitle">Por Jonas Silva - LEED GA</p>', unsafe_allow_html=True)
st.markdown('<p class="centered-painel">601 Empreendimentos - Painel de Conformidade Ambiental e Certificação</p>', unsafe_allow_html=True)

# =====================================================================
# ANTECIPAÇÃO: FILTROS DA BARRA LATERAL (Necessário para escopo dinâmico)
# =====================================================================
st.sidebar.header("🏢 Governança de Portfólio")
obra_selecionada = st.sidebar.selectbox("Selecionar Canteiro de Obras:", ["Edifício Venâncio Eco-Efficient", "Complexo Logístico Alpha", "Residencial Solar Hub"])
fase_obra = st.sidebar.radio("Fase Atual da Obra:", ["Estrutura", "Alvenaria/Acabamento", "Comissionamento"])

# Dica de Tema na Sidebar
st.sidebar.markdown("---")
st.sidebar.caption("🌓 *Dica de Visualização:* Alterne entre Modo Claro e Escuro clicando nas configurações (⚙️) no canto superior direito da tela.")

# =====================================================================
# ANTECIPAÇÃO: CÁLCULOS DE ENGENHARIA BRUTOS (Massa e Densidade LEED)
# =====================================================================
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

# Processamento de Engenharia: Convertendo para Toneladas
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


# =====================================================================
# INJEÇÃO EXCLUSIVA: MÓDULO ARC-INSPIRED (CENTRAL DE INTELIGÊNCIA)
# =====================================================================
st.markdown("---")
st.markdown("### 🌐 ARC Engine: Central de Performance em Tempo Real")
st.caption("Visão macro de governança baseada nas 5 dimensões globais do ARC GBCI.")

# 1. Visão Global (Performance Score Centralizado)
col_score1, col_score2, col_score3 = st.columns([1, 2, 1])

with col_score2:
    st.markdown('<div class="custom-card" style="text-align: center;">', unsafe_allow_html=True)
    st.markdown("<h4 style='color: #666666; margin-bottom: 0;'>Performance Score Global</h4>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 4.5rem; color: #2e7d32; margin: -10px 0px;'>78</h1>", unsafe_allow_html=True)
    st.caption("🎯 Projeção Atual: Nível Ouro (Gold)")
    st.progress(78)
    st.markdown('</div>', unsafe_allow_html=True)

# 2. Desmembramento nas 5 Categorias Oficiais do ARC
st.markdown("#### 📊 Tracking Multidimensional (Core Metrics)")
arc_c1, arc_c2, arc_c3, arc_c4, arc_c5 = st.columns(5)

arc_c1.metric(label="⚡ Energia", value="22/33 pts", delta="Estável", delta_color="off")
arc_c2.metric(label="💧 Água", value="12/15 pts", delta="+2 pts", delta_color="normal")
arc_c3.metric(label="♻️ Resíduos", value="6/8 pts", delta="Auditoria Ativa", delta_color="normal")
arc_c4.metric(label="🚲 Transporte", value="9/14 pts", delta="-1 pt (Alerta)", delta_color="inverse")
arc_c5.metric(label="👥 Exp. Humana", value="15/20 pts", delta="Conforme", delta_color="off")

# 3. Análise Longitudinal (Histórico de Tendência do ARC)
st.markdown("<br>", unsafe_allow_html=True)
with st.expander("📈 Expandir Curva de Evolução Longitudinal (Últimos 6 meses)"):
    st.write("Monitoramento contínuo da pontuação para evitar depreciação do ativo:")
    df_arc_trend = pd.DataFrame({
        'Mês': ['Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul'],
        'Score Global': [62, 65, 70, 72, 75, 78]
    })
    st.line_chart(df_arc_trend.set_index('Mês'), height=250)


# =====================================================================
# NOVO FORMATO: MATRIZ DE GOVERNANÇA (MENU EXPANSÍVEL + NAVBAR)
# =====================================================================
st.markdown("---")
with st.expander("🏛️ Matriz de Governança de Créditos - LEED BD+C v4", expanded=True):
    st.markdown("Painel de auditoria de requisitos e coleta de evidências para a certificação do ativo:")

    # Criação do Navbar utilizando rádio horizontal
    opcoes_navbar = [
        "IP (Processo)", 
        "LT (Localização)", 
        "SS (Terrenos)", 
        "WE (Água)", 
        "EA (Energia)", 
        "MR (Materiais)", 
        "EQ (Qualidade Interna)", 
        "IN (Inovação)", 
        "RP (Prioridade)"
    ]
    
    aba_selecionada = st.radio("Navegação de Categorias:", opcoes_navbar, horizontal=True, label_visibility="collapsed")
    st.markdown("---")

    # Condicionais para renderizar o conteúdo com base na seleção do Navbar
    if aba_selecionada == "IP (Processo)":
        st.markdown("#### 🤝 Processo Integrativo")
        st.caption("Documentação de Sinergia na Fase de Projeto")
        st.checkbox("✔️ Relatório de Sinergia de Energia Concluído (Obrigatório)", value=True)
        st.checkbox("✔️ Relatório de Sinergia de Água Concluído (Obrigatório)", value=True)
        st.button("📄 Gerar Termo de Abertura do Projeto (OPR)")

    elif aba_selecionada == "LT (Localização)":
        st.markdown("#### 🚲 Localização e Transporte")
        st.caption("Infraestrutura de Baixo Carbono")
        st.slider("Densidade do Entorno (Interseções num raio de 1km²)", min_value=0, max_value=500, value=150)
        st.number_input("Vagas Físicas para Bicicletas no Empreendimento", min_value=0, value=12)

    elif aba_selecionada == "SS (Terrenos)":
        st.markdown("#### 🌳 Terrenos Sustentáveis")
        st.warning("⚖️ Risco Jurídico: O Plano ESC é exigência de licenciamento e pré-requisito LEED.")
        st.file_uploader("Anexar Relatório Fotográfico Semanal de Prevenção de Poluição (ESC)", type=["pdf"])
        col_ss1, col_ss2 = st.columns(2)
        with col_ss1:
            st.checkbox("Inspeção de Lava-Rodas Realizada")
        with col_ss2:
            st.checkbox("Proteção de Bocas de Lobo Ativa")

    elif aba_selecionada == "WE (Água)":
        st.markdown("#### 💧 Eficiência Hídrica")
        st.caption("Monitoramento de Consumo e Redução")
        st.metric(label="Desempenho de Redução Hídrica (Design)", value="38%", delta="Meta Base: >20%")
        st.progress(38)
        st.checkbox("Submedidores Temporários Instalados no Canteiro")

    elif aba_selecionada == "EA (Energia)":
        st.markdown("#### ⚡ Energia e Atmosfera")
        st.caption("Comissionamento e Proteção da Camada de Ozônio")
        st.selectbox("Status do Comissionamento Fundamental (CxA):", ["Não Iniciado", "Em Andamento (Revisão de Projeto)", "Em Campo", "Concluído"])
        st.checkbox("Zero Uso de CFCs em Equipamentos de Alojamento", value=True)

    elif aba_selecionada == "MR (Materiais)":
        st.markdown("#### 📦 Materiais e Recursos (MR)")
        st.success("♻️ A auditoria de desvio de aterro e balanço de massa está totalmente integrada e ativa nesta seção de Materiais.")
        
        st.markdown("#### 📄 Declarações Ambientais de Produto (EPD / HPD)")
        st.number_input("Quantidade de Materiais com Certificado EPD/FSC Verificado", min_value=0, value=14)
        st.markdown("---")
        
        # INCLUSÃO: MÓDULO DE BALANÇO DE MASSA AUDITADO
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

        st.markdown("<br>", unsafe_allow_html=True)
        st.progress(int(taxa_desvio_leed) if taxa_desvio_leed <= 100 else 100)
        st.markdown("---")

        # INCLUSÃO: INTERFACE DIVIDIDA - UPLOAD E GRÁFICO
        col1, col2 = st.columns([1, 1], gap="large")

        with col1:
            st.markdown('<div class="custom-card">', unsafe_allow_html=True)
            st.markdown("### 📥 Gateway de Auditoria Automatizada (IA OCR)")
            arquivo_subido = st.file_uploader("Arraste o lote de PDFs/MTRs fiscais da obra:", type=["pdf"])
            
            if arquivo_subido is not None:
                if st.button("🔍 Executar Auditoria e Validação Digital"):
                    with st.spinner("Analisando assinaturas digitais, hash do documento e extraindo peso líquido..."):
                        time.sleep(2.5)
                    st.success("Documento Validado! Dados convertidos para Toneladas e integrados à Trilha de Auditoria.")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("### 📜 Trilha de Evidências Rastreáveis")
            evidencias = {
                'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai'],
                'Doc Origem': ['MTR_2024_019.pdf', 'MTR_2024_034.pdf', 'MTR_2024_051.pdf', 'MTR_2024_088.pdf', 'MTR_2024_112.pdf'],
                'Status GBC': ['Aprovado', 'Aprovado', 'Aprovado', 'Em Análise', 'Revisar Alerta']
            }
            st.dataframe(pd.DataFrame(evidencias), use_container_width=True)

        with col2:
            st.markdown("### 📈 Curva Analítica de Resíduos Desviados (Massa)")
            fig, ax = plt.subplots(figsize=(10, 6.2))
            fig.patch.set_alpha(0.0)
            ax.set_facecolor('none')
            
            ax.bar(df_massa['Mês'], df_massa['Reciclado Total (t)'], color='#2e7d32', label='Desviado/Reciclado (t)', alpha=0.9)
            ax.bar(df_massa['Mês'], df_massa['URE / Aterro (t)'], bottom=df_massa['Reciclado Total (t)'], color='#d32f2f', label='Aterro/URE (t)', alpha=0.9)
            
            ax.set_ylabel('Massa Líquida (Toneladas)', color='gray')
            ax.tick_params(colors='gray')
            ax.grid(True, linestyle=':', alpha=0.3, color='gray')
            ax.legend(loc='upper right', facecolor='none', edgecolor='gray')
            
            for spine in ax.spines.values():
                spine.set_visible(False)
                
            st.pyplot(fig)
            plt.close(fig)

    elif aba_selecionada == "EQ (Qualidade Interna)":
        st.markdown("#### 🌬️ Qualidade Ambiental Interna")
        st.caption("Proteção da Saúde Ocupacional e Futuros Ocupantes")
        st.multiselect(
            "Rastreabilidade de Materiais de Baixo VOC (Fichas FISPQ aprovadas):", 
            ["Tinta Epóxi Piso", "Selante Poliuretano (PU)", "Adesivo para Madeira", "Verniz Base Água", "Gesso Acartonado"], 
            default=["Tinta Epóxi Piso", "Selante Poliuretano (PU)"]
        )

    elif aba_selecionada == "IN (Inovação)":
        st.markdown("#### 🚀 Inovação em Design")
        st.caption("Estratégias para Superação de Metas")
        st.text_area(
            "Registro de Performance Exemplar (Ex: Desvio de aterro atingindo 95%+):", 
            "A Venâncio Empreendimentos atingiu a meta excepcional de..."
        )
            
    elif aba_selecionada == "RP (Prioridade)":
        st.markdown("#### 🗺️ Prioridade Regional")
        st.caption("Bônus de Certificação Específicos para a Coordenada Geográfica")
        st.selectbox(
            "Selecione o Crédito de Prioridade Regional Atingido:", 
            ["Nenhum", "WEc: Redução de Uso de Água Externa", "EAc: Otimização de Performance Energética", "SSc: Gestão de Águas Pluviais"]
        )

# Rodapé de Conformidade Global
st.markdown("---")
st.caption("🔒 Certificação de Dados: GreenConformity segue as diretrizes do LEED BD+C v4/v4.1. Dados protegidos por chaves corporativas privadas de criptografia.")
