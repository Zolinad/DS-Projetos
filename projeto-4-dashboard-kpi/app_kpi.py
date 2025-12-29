import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuração
st.set_page_config(layout='wide', page_title="Dashboard de Vendas")

# --- 1. GERAR DADOS SINTÉTICOS (Varejo Nacional) ---
@st.cache_data
def gerar_dados_vendas():
    np.random.seed(42)
    rows = 1000
    
    # Hierarquia: Região -> Gerente -> Categoria
    regioes = ['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste']
    categorias = ['Eletrônicos', 'Móveis', 'Eletrodomésticos', 'Decoração']
    
    data = {
        'Data': pd.date_range('2023-01-01', periods=rows, freq='D'),
        'Região': np.random.choice(regioes, rows),
        'Categoria': np.random.choice(categorias, rows),
        # Vendas variando entre 100 e 5000
        'Vendas': np.random.randint(100, 5000, rows),
        # Margem de lucro entre 5% e 30%
        'Margem_Lucro': np.random.uniform(0.05, 0.30, rows)
    }
    
    df = pd.DataFrame(data)
    
    # Calcular Lucro em R$
    df['Lucro'] = df['Vendas'] * df['Margem_Lucro']
    
    # Criar um "Score de Qualidade" (0 a 10) baseado na margem (Para simular uma nota)
    df['Score_Qualidade'] = (df['Margem_Lucro'] * 100) / 3 
    # Normalizando para ficar parecido com uma nota 0-10
    
    return df

# --- 2. INTERFACE E LÓGICA ---
st.title("📈 Dashboard Estratégico de Vendas & KPIs")
st.markdown("Monitoramento de performance hierárquica: Região > Categoria > Rentabilidade.")

df = gerar_dados_vendas()

# Sidebar (Filtros Hierárquicos)
st.sidebar.header("Filtros de Gestão")
filtro_regiao = st.sidebar.multiselect("Filtrar Região", df['Região'].unique(), default=df['Região'].unique())
filtro_categoria = st.sidebar.multiselect("Filtrar Categoria", df['Categoria'].unique(), default=df['Categoria'].unique())

# Aplicar Filtros
df_filtrado = df[
    (df['Região'].isin(filtro_regiao)) & 
    (df['Categoria'].isin(filtro_categoria))
]

# --- 3. KPIs (Indicadores Chave) ---
total_vendas = df_filtrado['Vendas'].sum()
total_lucro = df_filtrado['Lucro'].sum()
media_score = df_filtrado['Score_Qualidade'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Faturamento Total", f"R$ {total_vendas:,.2f}")
col2.metric("Lucro Líquido", f"R$ {total_lucro:,.2f}")
# O Score muda de cor se for baixo (meta < 6.0)
col3.metric("Score de Qualidade (Média)", f"{media_score:.1f}/10.0", 
            delta=f"{media_score - 6.0:.1f} vs Meta",
            delta_color="normal")

st.divider()

# --- 4. GRÁFICOS ESTRATÉGICOS ---

col_charts1, col_charts2 = st.columns(2)

with col_charts1:
    st.subheader("Performance por Região")
    # Gráfico de Barras: Comparativo de Vendas
    fig_bar = px.bar(
        df_filtrado.groupby('Região')[['Vendas']].sum().reset_index(),
        x='Região', 
        y='Vendas',
        color='Vendas',
        title="Volume de Vendas (Ranking Regional)",
        color_continuous_scale='Blues'
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col_charts2:
    st.subheader("Qualidade vs. Volume")
    # Gráfico de Dispersão: Vendas x Score (Onde estamos vendendo mal?)
    # Agrupar por Categoria para ver quem performa melhor
    df_cat = df_filtrado.groupby('Categoria').agg({'Vendas':'sum', 'Score_Qualidade':'mean'}).reset_index()
    
    fig_scatter = px.scatter(
        df_cat,
        x='Vendas',
        y='Score_Qualidade',
        size='Vendas',
        color='Categoria',
        text='Categoria',
        title="Matriz de Desempenho (Qualidade x Volume)",
        labels={'Score_Qualidade': 'Score de Qualidade (0-10)', 'Vendas': 'Volume Vendido R$'}
    )
    # Adicionar linha de corte (Meta)
    fig_scatter.add_hline(y=6.0, line_dash="dot", annotation_text="Meta de Qualidade", annotation_position="bottom right")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Tabela Detalhada
st.subheader("📋 Detalhamento Operacional")
st.dataframe(df_filtrado.sort_values(by='Data', ascending=False).head(50), use_container_width=True)

st.info("""
**Análise de Negócio:**
* **Eixo Y do Gráfico de Bolhas:** Representa a eficiência (Margem/Qualidade).
* **Barra Lateral:** Permite o detalhamento e filtragem dos dados.
""")

#---------------------------------------
st.divider() # Uma linha visual para separar o App da documentação

# 2. DOCUMENTAÇÃO (Vem no final)
PATH_README = "projeto-1-churn/README.md"

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
