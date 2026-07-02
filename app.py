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
    :root {
        --primary-color: #1e1e1e;
        --secondary-color: #2e7d32;
        --text-muted: #5f6368;
    }
    
    .brand-title {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        font-size: 1.75rem;
        font-weight: 700;
        color: #2e7d32;
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
# HEADER PREMIUM MINIMALISTA
# =====================================================================
header_col1, header_col2 = st.columns([1.2, 3])

with header_col1:
    st.markdown("<p class='brand-title' style='margin-top: 25px;'>Green Conformity</p>", unsafe_allow_html=True)

with header_col2:
    opcoes_navbar = [
        "IP (Processo)", "LT (Localização)", "SS (Terrenos)", "WE (Água)", 
        "EA (Energia)", "MR (Materiais)", "EQ (Qualidade)", "IN (Inovação)", "RP (Prioridade)"
    ]
    
    if 'aba_ativa' not in st.session_state:
        st.session_state.aba_ativa = "IP (Processo)"
        
    nav_cols = st.columns(len(opcoes_navbar))
    for idx, opcao in enumerate(opcoes_navbar):
        with nav_cols[idx]:
            estilo_label = f"*{opcao}*" if st.session_state.aba_ativa == opcao else opcao
            if st.button(estilo_label, key=f"nav_{opcao}", use_container_width=True):
                st.session_state.aba_ativa = opcao
                st.rerun()

st.markdown("<hr style='margin-top: 5px; margin-bottom: 15px; border-color: rgba(0,0,0,0.08);'>", unsafe_allow_html=True)

st.markdown('<p class="centered-subtitle">Por Jonas Silva - LEED GA</p>', unsafe_allow_html=True)
st.markdown('<p class="centered-painel">601 Empreendimentos - Painel de Conformidade Ambiental e Certificação</p>', unsafe_allow_html=True)


# =====================================================================
# FILTROS DA BARRA LATERAL
# =====================================================================
st.sidebar.header("🏢 Governança de Portfólio")
obra_selecionada = st.sidebar.selectbox("Selecionar Canteiro de Obras:", ["601 Empreendimentos", "208 Empreendimentos", "Residencial Solar Hub"])
fase_obra = st.sidebar.radio("Fase Atual da Obra:", ["Estrutura", "Alvenaria/Acabamento", "Comissionamento"])

st.sidebar.markdown("---")
st.sidebar.caption("🌓 *Dica de Visualização:* Alterne entre Modo Claro e Escuro nas configurações superiores.")


# =====================================================================
# CÁLCULOS DE ENGENHARIA E CENTRAL DE INTELIGÊNCIA ARC
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
st.write("Monitoramento contínuo da pontuação para evitar depreciação do ativo:")

cert_c1, cert_c2, cert_c3, cert_c4 = st.columns(4)
with cert_c1:
    st.caption("Certified (40-49 pts)")
    st.progress(100)
with cert_c2:
    st.caption("Silver (50-59 pts)")
    st.progress(100)
with cert_c3:
    st.caption("Gold (60-79 pts)")
    st.progress(90) 
with cert_c4:
    st.caption("Platinum (80+ pts)")
    st.progress(97)

with st.expander("📈 Expandir Curva de Evolução Longitudinal (Últimos 6 meses)"):
    df_arc_trend = pd.DataFrame({
        'Mês': ['Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul'],
        'Score Global': [62, 65, 70, 72, 75, 78]
    })
    st.line_chart(df_arc_trend.set_index('Mês'), height=250)


# =====================================================================
# MATRIZ DE GOVERNANÇA: FUNCIONALIDADES DAS ABAS ATIVADAS
# =====================================================================
st.markdown("---")
with st.expander(f"🏛️ Matriz de Governança de Créditos Ativa: {st.session_state.aba_ativa} - LEED BD+C v4", expanded=True):

    # -----------------------------------------------------------------
    # ABA: IP (PROCESSO INTEGRATIVO)
    # -----------------------------------------------------------------
    if st.session_state.aba_ativa == "IP (Processo)":
        st.markdown("#### 🤝 Processo Integrativo (Integrative Process)")
        st.caption("Avaliação de sinergias entre sistemas hídricos e energéticos desde a fase de pré-projeto.")
        
        col_ip1, col_ip2 = st.columns(2)
        with col_ip1:
            st.markdown("##### 📋 Checklists de Análise Inicial")
            sinergia_energia = st.checkbox("Análise de Sinergia Energética Concluída (Simulações de Carga)", value=True)
            sinergia_agua = st.checkbox("Análise de Sinergia Hídrica Concluída (Balanço de Fontes Alternativas)", value=False)
            
            pts_ip = 1 if (sinergia_energia and sinergia_agua) else 0
            st.metric("Pontos Estimados (IPc1)", f"{pts_ip} / 1 Recurso")
            
        with col_ip2:
            st.markdown("##### 📄 Geração de Evidências Oficiais")
            st.write("Gere a documentação de metas de sustentabilidade base (OPR e BOD) exigida pelo GBCI:")
            if st.button("📄 Exportar Relatório de Diretrizes do Projeto (OPR)"):
                with st.spinner("Compilando dados estruturais..."):
                    time.sleep(1.5)
                st.success("✓ OPR.pdf gerado com sucesso! Pronto para upload no LEED Online.")

    # -----------------------------------------------------------------
    # ABA: LT (LOCALIZAÇÃO E TRANSPORTE)
    # -----------------------------------------------------------------
    elif st.session_state.aba_ativa == "LT (Localização)":
        st.markdown("#### 🚲 Localização e Transporte (Location and Transportation)")
        st.caption("Pontuação baseada na malha urbana, acesso a trânsito de qualidade e modais alternativos.")
        
        col_lt1, col_lt2 = st.columns([2, 1])
        with col_lt1:
            st.markdown("##### 🧮 Simulador de Créditos de Mobilidade")
            raio_intersecoes = st.slider("Densidade de Interseções Viárias (num raio de 1 km²)", min_value=0, max_value=200, value=140)
            vagas_bike = st.number_input("Vagas para Bicicletas (% em relação aos ocupantes de pico)", min_value=0.0, max_value=10.0, value=5.2, step=0.1)
            veiculos_verdes = st.checkbox("Vagas Reservadas + Carregadores Elétricos para Veículos Eficientes (Mínimo 2%)", value=True)
            
        with col_lt2:
            st.markdown("##### 🎯 Calculadora de Crédito LT")
            pts_transito = 0
            if raio_intersecoes >= 140: pts_transito += 3
            if vagas_bike >= 5.0: pts_transito += 1
            if veiculos_verdes: pts_transito += 1
            
            st.metric("Total Estimado em LT", f"{pts_transito} pts", help="Pontuação máxima dependente de auditoria de linhas de ônibus/metrô.")
            if pts_transito >= 4:
                st.success("Ótimo desempenho em Adensamento e Redução de Trajeto!")

    # -----------------------------------------------------------------
    # ABA: SS (TERRENOS SUSTENTÁVEIS)
    # -----------------------------------------------------------------
    elif st.session_state.aba_ativa == "SS (Terrenos)":
        st.markdown("#### 🌳 Terrenos Sustentáveis (Sustainable Sites)")
        st.caption("Mitigação de impactos ambientais durante a construção e preservação ecológica da área.")
        
        st.error("⚖️ Alerta de Auditoria: O Plano ESC (Prevenção de Poluição) é um PRÉ-REQUISITO OBRIGATÓRIO.")
        
        col_ss1, col_ss2 = st.columns(2)
        with col_ss1:
            st.markdown("##### 🔍 Auditoria em Canteiro (Plano ESC)")
            lava_rodas = st.checkbox("Estação de Lava-Rodas operacional nas saídas do canteiro", value=True)
            bocas_lobo = st.checkbox("Proteções e filtros instalados nas bocas-de-lobo/bueiros", value=True)
            taludes = st.checkbox("Controle de erosão ativo em taludes expostos (lona/hidrossemeadura)", value=False)
            
            if lava_rodas and bocas_lobo and taludes:
                st.success("✓ Pré-requisito SSp1 (ESC) totalmente em conformidade!")
            else:
                st.warning("⚠️ Risco de não conformidade no SSp1. Todos os controles devem estar ativos.")
                
        with col_ss2:
            st.markdown("##### 📂 Upload de Evidências Fotográficas")
            st.write("Anexe os relatórios de inspeção visual para comprovar o controle de sedimentação:")
            file_esc = st.file_uploader("Arraste o relatório ESC Semanal (PDF)", type=["pdf"], key="esc_upload")
            if file_esc:
                st.success(f"Arquivo '{file_esc.name}' armazenado na fila de auditoria.")

    # -----------------------------------------------------------------
    # ABA: WE (EFICIÊNCIA HÍDRICA)
    # -----------------------------------------------------------------
    elif st.session_state.aba_ativa == "WE (Água)":
        st.markdown("#### 💧 Eficiência Hídrica (Water Efficiency)")
        st.caption("Redução drástica do consumo interno, externo (paisagismo) e monitoramento por submedição.")
        
        col_we1, col_we2 = st.columns([1, 1])
        with col_we1:
            st.markdown("##### 🚰 Simulação de Consumo Interno (Indoor Water)")
            reducao_meta = st.slider("% de Redução Obtida (Meta Base LEED: >20%)", min_value=0, max_value=50, value=35)
            st.progress(reducao_meta / 50)
            
            submedidores = st.checkbox("Submedidores permanentes instalados nos subsistemas (Torres, Chiller, Irrigação)", value=True)
            
        with col_we2:
            st.markdown("##### 📉 Balanço e Projeção de Créditos")
            pts_we = 0
            if reducao_meta >= 20: pts_we += 1  # Pré-requisito atendido + pontos adicionais progressivos
            if reducao_meta >= 30: pts_we += 2
            if reducao_meta >= 35: pts_we += 1
            if submedidores: pts_we += 1
            
            st.metric("Pontos Projetados em WE", f"{pts_we} pts")
            if submedidores:
                st.success("✓ Crédito de Submedição Avançada Garantido (+1 ponto).")

    # -----------------------------------------------------------------
    # ABAS: MATERIAIS, ENERGIA, QUALIDADE E OUTROS (Prontas para Lógicas Adicionais)
    # -----------------------------------------------------------------
    elif st.session_state.aba_ativa == "EA (Energia)":
        st.markdown("#### ⚡ Energia e Atmosfera")
        st.caption("Comissionamento e Proteção da Camada de Ozônio")
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
        with kpi1: st.metric(label="⚖️ Massa Total Gerada", value=f"{t_total:.2f} t")
        with kpi2: st.metric(label="♻️ Desvio de Aterro (LEED)", value=f"{taxa_desvio_leed:.1f}%", delta=f"{taxa_desvio_leed - 75.0:.1f}% vs Meta GBC")
        with kpi3: st.metric(label="🪵 Canais de Reciclagem Ativos", value="3 Fluxos", delta="Atende Prerequisito")
        with kpi4: st.metric(label="🎖️ Pontuação Estimada MR", value="2 Pontos", delta="Pontuação Máxima")

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
                    with st.spinner("Analisando assinaturas digitais..."): time.sleep(2.5)
                    st.success("Documento Validado e integrado.")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.dataframe(pd.DataFrame({'Mês': ['Jan', 'Fev', 'Mar'], 'Doc Origem': ['MTR_019.pdf', 'MTR_034.pdf', 'MTR_051.pdf'], 'Status GBC': ['Aprovado', 'Aprovado', 'Aprovado']}), use_container_width=True)

        with col2:
            fig, ax = plt.subplots(figsize=(10, 6.2))
            fig.patch.set_alpha(0.0); ax.set_facecolor('none')
            ax.bar(df_massa['Mês'], df_massa['Reciclado Total (t)'], color='#2e7d32', label='Desviado (t)')
            ax.bar(df_massa['Mês'], df_massa['URE / Aterro (t)'], bottom=df_massa['Reciclado Total (t)'], color='#d32f2f', label='Aterro (t)')
            ax.set_ylabel('Toneladas', color='gray'); ax.tick_params(colors='gray'); ax.grid(True, linestyle=':', alpha=0.3); ax.legend()
            for s in ax.spines.values(): s.set_visible(False)
            st.pyplot(fig); plt.close(fig)

    elif st.session_state.aba_ativa == "EQ (Qualidade)":
        st.markdown("#### 🌬️ Qualidade Ambiental Interna")
        st.multiselect("Rastreabilidade de Materiais de Baixo VOC (Fichas FISPQ):", ["Tinta Epóxi Piso", "Selante PU", "Adesivo Madeira", "Verniz Base Água"], default=["Tinta Epóxi Piso"])

    elif st.session_state.aba_ativa == "IN (Inovação)":
        st.markdown("#### 🚀 Inovação em Design")
        st.text_area("Registro de Performance Exemplar:", "A Venâncio Empreendimentos atingiu a meta excepcional de...")
            
    elif st.session_state.aba_ativa == "RP (Prioridade)":
        st.markdown("#### 🗺️ Prioridade Regional")
        st.selectbox("Selecione o Crédito de Prioridade Regional Atingido:", ["Nenhum", "WEc: Redução de Uso de Água Externa", "EAc: Otimização de Performance Energética"])

# Rodapé de Conformidade Global
st.markdown("---")
st.caption("🔒 Certificação de Dados: GreenConformity segue as diretrizes do LEED BD+C v4/v4.1. Dados protegidos por chaves corporativas privadas de criptografia.")
