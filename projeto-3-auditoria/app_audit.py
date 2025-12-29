import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.ensemble import IsolationForest

# Configuração da Página
st.set_page_config(layout='wide', page_title="Auditoria Financeira e Detecção de Anomalia com AI")

# --- 1. GERAR DADOS FINANCEIROS SINTÉTICOS ---
@st.cache_data
def gerar_transacoes():
    np.random.seed(42)
    n_transacoes = 500
    
    # Gerar dados "Normais"
    data = {
        'ID_Transacao': [f'TRX-{i:04d}' for i in range(n_transacoes)],
        'Departamento': np.random.choice(['TI', 'Marketing', 'RH', 'Operações', 'Vendas'], n_transacoes),
        'Categoria': np.random.choice(['Software', 'Viagem', 'Serviços', 'Material de Escritório'], n_transacoes),
        # Valores normais entre 500 e 2000
        'Valor': np.random.normal(1200, 300, n_transacoes), 
        'Data': pd.date_range(start='2024-01-01', periods=n_transacoes, freq='H')
    }
    
    df = pd.DataFrame(data)
    
    # INJETAR ANOMALIAS (FRAUDES/ERROS)
    # Vamos criar 15 transações com valores absurdos ou estranhos
    indices_anomalos = np.random.choice(df.index, 15, replace=False)
    
    # Tornar os valores extremos (ex: R$ 8.000,00 ou R$ 50,00 onde a média é 1200)
    df.loc[indices_anomalos, 'Valor'] = np.random.uniform(5000, 15000, 15)
    
    # Marcar (apenas para nós sabermos a verdade no gráfico, mas o modelo não sabe)
    df['Is_Anomaly_Real'] = 0
    df.loc[indices_anomalos, 'Is_Anomaly_Real'] = 1
    
    return df

# --- 2. MODELAGEM (ISOLATION FOREST) ---
def detectar_anomalias(df, contaminacao):
    # O modelo olha apenas para o 'Valor' neste exemplo simples
    # Em casos reais, olharia Categoria, Hora, etc.
    X = df[['Valor']]
    
    # Isolation Forest: Algoritmo excelente para achar outliers sem treino prévio
    model = IsolationForest(contamination=contaminacao, random_state=42)
    df['Anomaly_Score'] = model.fit_predict(X)
    
    # O modelo retorna -1 para anomalia e 1 para normal
    # Vamos converter para texto para ficar bonito no gráfico
    df['Status'] = df['Anomaly_Score'].apply(lambda x: 'Anomalia Detectada' if x == -1 else 'Normal')
    
    return df

# --- 3. INTERFACE STREAMLIT ---
st.title("🛡️ Corporate Audit AI: Detecção de Fraudes")
st.markdown("""
Sistema de auditoria contínua utilizando **Machine Learning Não-Supervisionado (Isolation Forest)** para identificar gastos corporativos desviantes do padrão (Outliers).
""")

# Carregar dados
df_raw = gerar_transacoes()

# Sidebar de Controles
st.sidebar.header("Painel de Auditoria")
# O usuário define quão sensível é o auditor (1% a 10% de contaminação esperada)
sensibilidade = st.sidebar.slider("Sensibilidade do Auditor (% de Outliers)", 0.01, 0.10, 0.03)

# Executar IA
df_auditado = detectar_anomalias(df_raw.copy(), sensibilidade)
anomalias = df_auditado[df_auditado['Status'] == 'Anomalia Detectada']

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Transações Analisadas", len(df_auditado))
col2.metric("Anomalias Encontradas", len(anomalias), delta_color="inverse")
col3.metric("Valor Total em Risco", f"R$ {anomalias['Valor'].sum():,.2f}")

st.divider()

# GRÁFICO DE DISPERSÃO (SCATTER PLOT)
st.subheader("🔎 Visualização de Dispersão de Gastos")
fig = px.scatter(
    df_auditado, 
    x="Data", 
    y="Valor", 
    color="Status",
    color_discrete_map={'Normal': 'lightgrey', 'Anomalia Detectada': 'red'},
    hover_data=['Departamento', 'Categoria', 'ID_Transacao'],
    title="Monitoramento em Tempo Real (Pontos Vermelhos = Suspeitos)",
    height=500
)
st.plotly_chart(fig, use_container_width=True)

# DETALHAMENTO
col_table1, col_table2 = st.columns([2, 1])

with col_table1:
    st.subheader("📋 Relatório de Transações Suspeitas")
    st.dataframe(
        anomalias[['ID_Transacao', 'Data', 'Departamento', 'Categoria', 'Valor']]
        .sort_values(by='Valor', ascending=False),
        use_container_width=True
    )

with col_table2:
    st.subheader("📊 Ofensores por Depto")
    # Quem está gastando errado?
    fig_bar = px.bar(anomalias['Departamento'].value_counts(), orientation='h', title="Contagem de Anomalias")
    fig_bar.update_layout(showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)

st.info("**Lógica do Algoritmo:** O modelo aprende o padrão de gasto 'comum' (R$ 500 a R$ 2.000). Valores muito acima (ex: R$ 12.000) ou muito discrepantes são isolados geometricamente.")

#-----------------------------------------------------------------
st.divider() # Uma linha visual para separar o App da documentação

# 2. DOCUMENTAÇÃO (Vem no final)
PATH_README = "projeto-1-churn/readme.md"

def exibir_readme(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            conteudo = f.read()
        # Usamos um expander "fechado" para não esticar demais a página
        with st.expander("📖 Detalhes Técnicos e Metodologia (README)", expanded=False):
            st.markdown(conteudo)
    except FileNotFoundError:
        st.error("Documentação não encontrada.")

exibir_readme(PATH_README)
