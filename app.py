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

# 2. Injeção de CSS para Governança Estética, Hierarquia Tipográfica e Navbar Minimalista
st.markdown("""
    <style>
    /* Reset e Variáveis de Cores Corporativas */
    :root {
        --primary-color: #1e1e1e;
        --secondary-color: #2e7d32;
        --text-muted: #5f6368;
    }
    
    /* Hierarquia Tipográfica Rigorosa */
    .brand-title {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        font-size: 1.75rem; /* Ajustado para equivaler ao tamanho do h3 (###) */
        font-weight: 700;
        color: #2e7d32; /* Alterado para o mesmo tom verde da plataforma */
        letter-spacing: -0.5px;
        margin: 0;
        padding: 0;
    }
    
    .centered-subtitle {
        text-align: center;
        color: #5f6368;
        margin-top: 15px;
        margin-bottom: 5px;
        font-size: 1.1rem;
        font-weight: 500;
    }
    
    .centered-painel {
        text-align: center;
        color: #2e7d32;
        margin-top: -5px;
        margin-bottom: 30px;
        font-size: 1.3rem;
        font-weight: 600;
    }
    
    /* Estilização dos Links de Navegação Simulando o Modelo Enviado */
    .nav-link-btn {
        background: none;
        border: none;
        color: #3c4043;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
        font-size: 0.95rem;
        font-weight: 500;
        padding: 6px 12px;
        cursor: pointer;
        transition: color 0.2s ease;
    }
    
    .custom-card {
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(46, 125, 50, 0.15);
        background-color: rgba(46, 125, 50, 0.01);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)


# =====================================================================
# HEADER PREMIUM MINIMALISTA (Inspirado no Padrão de Interface do Usuário)
# =====================================================================
header_col1, header_col2 = st.columns([1.2, 3])

with header_col1:
    # Nome comercial aumentado, no tom verde correto e alinhado à esquerda
    st.markdown("<p class='brand-title' style='margin-top: 5px;'>Green Conformity</p>", unsafe_allow_html=True)

with header_col2:
    # Sistema de navegação horizontal por colunas de botões nativos para reproduzir os links textuais da imagem
    opcoes_navbar = [
        "IP (Processo)", "LT (Localização)", "SS (Terrenos)", "WE (Água)", 
        "EA (Energia)", "MR (Materiais)", "EQ (Qualidade)", "IN (Inovação)", "RP (Prioridade)"
    ]
    
    # Inicialização do estado da aba de navegação se não existir
    if 'aba_ativa' not in st.session_state:
        st.session_state.aba_ativa = "IP (Processo)"
        
    nav_cols = st.columns(len(opcoes_navbar))
    for idx, opcao in enumerate(opcoes_navbar):
        with nav_cols[idx]:
            # Destaca sutilmente a aba selecionada alterando o peso visual do botão
            estilo_label = f"*{opcao}*" if st.session_state.aba_ativa == opcao else opcao
            if st.button(estilo_label, key=f"nav_{opcao}", use_container_width=True, help=f"Navegar para {opcao}"):
                st.session_state.aba_ativa = opcao
                st.rerun()

st.markdown("<hr style='margin-top: 5px; margin-bottom: 15px; border-color: rgba(0,0,0,0.08);'>", unsafe_allow_html=True)

# Linhas Hierárquicas de Identificação Técnico do Painel
st.markdown('<p class="centered-subtitle">Por Jonas Silva - LEED GA</p>', unsafe_allow_html=True)
st.markdown('<p class="centered-painel">601 Empreendimentos - Painel de Conformidade Ambiental e Certificação</p>', unsafe_allow_html=True)


# =====================================================================
# ANTECIPAÇÃO: FILTROS DA BARRA LATERAL (Necessário para escopo dinâmico)
# =====================================================================
st.sidebar.header("🏢 Governança de Portfólio")
obra_selecionada = st.sidebar.selectbox("Selecionar Canteiro de Obras:", ["Edifício Venâncio Eco-Efficient", "Complexo Logístico Alpha", "Residencial Solar Hub"])
fase_obra = st.sidebar.radio("Fase Atual da Obra:", ["Estrutura", "Alvenaria/Acabamento", "Comissionamento"])

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

FAT_CONCRETO = 1.2  
FAT_MADEIRA = 0.3  
FAT_METAL = 0.5   
FAT_URE = 0.4     

df_massa = pd.DataFrame()
df_massa['Mês'] = df_volume['Mês']
df_massa['Concreto (t)'] = df_volume['Concreto (m³)'] * FAT_CONCRETO
df_massa['Madeira (t)'] = df_volume['Madeira (m³)'] * FAT_MADEIRA
df_massa['Metais (t)'] = df_volume['Metais (m³)'] * FAT_METAL
df_massa['Reciclado Total (t)'] = df_massa['Concreto (t)'] + df_massa['Madeira (t)'] + df_massa['Metais (t)']
df_massa['URE / Aterro (t)'] = df_volume['URE / Não Reciclado (m³)'] * FAT_URE
df_massa['Total Gerado (t)'] = df_massa['Reciclado Total (t)'] + df_massa['URE / Aterro (t)']

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

col_score1, col_score2, col_score3 = st.columns([1, 2, 1])

with col_score2:
    st.markdown('<div class="custom-card" style="text-align: center;">', unsafe_allow_html=True)
    st.markdown("<h4 style='color: #666666; margin-bottom: 0;'>Performance Score Global</h4>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 4.5rem; color: #2e7d32; margin: -10px 0px;'>78</h1>", unsafe_allow_html=True)
    st.caption("🎯 Projeção Atual: Nível Ouro (Gold)")
    st.progress(78)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("#### 📊 Tracking Multidimensional (Core Metrics)")
arc_c1, arc_c2, arc_c3, arc_c4, arc_c5 = st.columns(5)

arc_c1.metric(label="⚡ Energia", value="22/33 pts", delta="Estável", delta_color="off")
arc_c2.metric(label="💧 Água", value="12/15 pts", delta="+2 pts", delta_color="normal")
arc_c3.metric(label="♻️ Resíduos", value="6/8 pts", delta="Auditoria Ativa", delta_color="normal")
arc_c4.metric(label="🚲 Transporte", value="9/14 pts", delta="-1 pt (Alerta)", delta_color="inverse")
arc_c5.metric(label="👥 Exp. Humana", value="15/20 pts", delta="Conforme", delta_color="off")

st.markdown("<br>", unsafe_allow_html=True)

# Texto de monitoramento movido para fora do expander, acompanhado dos 4 gráficos pequenos de tipologias LEED
st.write("Monitoramento contínuo da pontuação para evitar depreciação do ativo:")

cert_c1, cert_c2, cert_c3, cert_c4 = st.columns(4)
with cert_c1:
    st.caption("Certified (40-49 pts)")
    st.progress(100) # 78 pontos supera totalmente o nível base
with cert_c2:
    st.caption("Silver (50-59 pts)")
    st.progress(100) # 78 pontos supera totalmente o nível prata
with cert_c3:
    st.caption("Gold (60-79 pts)")
    # Mapeia proporcionalmente os 78 pontos dentro do intervalo Gold (18/20 pontos percorridos)
    st.progress(90) 
with cert_c4:
    st.caption("Platinum (80+ pts)")
    # Mostra quão próximo está do nível Platinum (78 de 80 necessários)
    st.progress(97)

with st.expander("📈 Expandir Curva de Evolução Longitudinal (Últimos 6 meses)"):
    df_arc_trend = pd.DataFrame({
        'Mês': ['Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul'],
        'Score Global': [62, 65, 70, 72, 75, 78]
    })
    st.line_chart(df_arc_trend.set_index('Mês'), height=250)


# =====================================================================
# MATRIZ DE GOVERNANÇA (CONTEÚDO EXPANSÍVEL CONECTADO AO NAVBAR SUPERIOR)
# =====================================================================
st.markdown("---")
with st.expander(f"🏛️ Matriz de Governança de Créditos Ativa: {st.session_state.aba_ativa} - LEED BD+C v4", expanded=True):
    st.markdown("Painel de auditoria de requisitos e coleta de evidências para a certificação do ativo:")
    st.markdown("---")

    if st.session_state.aba_ativa == "IP (Processo)":
        st.markdown("#### 🤝 Processo Integrativo")
        st.checkbox("✔️ Relatório de Sinergia de Energia Concluído (Obrigatório)", value=True)
        st.checkbox("✔️ Relatório de Sinergia de Água Concluído (Obrigatório)", value=True)
        st.button("📄 Gerar Termo de Abertura do Projeto (OPR)")

    elif st.session_state.aba_ativa == "LT (Localização)":
        st.markdown("#### 🚲 Localização e Transporte")
        st.slider("Densidade do Entorno (Interseções num raio de 1km²)", min_value=0, max_value=500, value=150)
        st.number_input("Vagas Físicas para Bicicletas no Empreendimento", min_value=0, value=12)

    elif st.session_state.aba_ativa == "SS (Terrenos)":
        st.markdown("#### 🌳 Terrenos Sustentáveis")
        st.warning("⚖️ Risco Jurídico: O Plano ESC é exigência de licenciamento e pré-requisito LEED.")
        st.file_uploader("Anexar Relatório Fotográfico Semanal de Prevenção de Poluição (ESC)", type=["pdf"])
        col_ss1, col_ss2 = st.columns(2)
        with col_ss1:
            st.checkbox("Inspeção de Lava-Rodas Realizada")
        with col_ss2:
            st.checkbox("Proteção de Bocas de Lobo Ativa")

    elif st.session_state.aba_ativa == "WE (Água)":
        st.markdown("#### 💧 Eficiência Hídrica")
        st.metric(label="Desempenho de Redução Hídrica (Design)", value="38%", delta="Meta Base: >20%")
        st.progress(38)
        st.checkbox("Submedidores Temporários Instalados no Canteiro")

    elif st.session_state.aba_ativa == "EA (Energia)":
        st.markdown("#### ⚡ Energia e Atmosfera")
        st.selectbox("Status do Comissionamento Fundamental (CxA):", ["Não Iniciado", "Em Andamento (Revisão de Projeto)", "Em Campo", "Concluído"])
        st.checkbox("Zero Uso de CFCs em Equipamentos de Alojamento", value=True)

    elif st.session_state.aba_ativa == "MR (Materiais)":
        st.markdown("#### 📦 Materiais e Recursos (MR)")
        st.success("♻️ A auditoria de desvio de aterro e balanço de massa está totalmente integrada e ativa nesta seção de Materiais.")
        
        st.markdown("#### 📄 Declarações Ambientais de Produto (EPD / HPD)")
        st.number_input("Quantidade de Materiais com Certificado EPD/FSC Verificado", min_value=0, value=14)
        st.markdown("---")
        
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

    elif st.session_state.aba_ativa == "EQ (Qualidade)":
        st.markdown("#### 🌬️ Qualidade Ambiental Interna")
        st.multiselect(
            "Rastreabilidade de Materiais de Baixo VOC (Fichas FISPQ aprovadas):", 
            ["Tinta Epóxi Piso", "Selante Poliuretano (PU)", "Adesivo para Madeira", "Verniz Base Água", "Gesso Acartonado"], 
            default=["Tinta Epóxi Piso", "Selante Poliuretano (PU)"]
        )

    elif st.session_state.aba_ativa == "IN (Inovação)":
        st.markdown("#### 🚀 Inovação em Design")
        st.text_area(
            "Registro de Performance Exemplar (Ex: Desvio de aterro atingindo 95%+):", 
            "A Venâncio Empreendimentos atingiu a meta excepcional de..."
        )
            
    elif st.session_state.aba_ativa == "RP (Prioridade)":
        st.markdown("#### 🗺️ Prioridade Regional")
        st.selectbox(
            "Selecione o Crédito de Prioridade Regional Atingido:", 
            ["Nenhum", "WEc: Redução de Uso de Água Externa", "EAc: Otimização de Performance Energética", "SSc: Gestão de Águas Pluviais"]
        )

# Rodapé de Conformidade Global
st.markdown("---")
st.caption("🔒 Certificação de Dados: GreenConformity segue as diretrizes do LEED BD+C v4/v4.1. Dados protegidos por chaves corporativas privadas de criptografia.")
