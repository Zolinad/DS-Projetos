import streamlit as st

# Configuração da Página Principal
st.set_page_config(layout="wide", page_title="Portfólio de Data Science - Danilo A. F.")

st.sidebar.markdown("### Navegação do Portfólio")

# Definição das Páginas (Ajustar o caminho "projeto-X/nome_do_arquivo.py")
# O primeiro argumento é o caminho do arquivo, o segundo é o título que aparece no menu

pg = st.navigation([
    st.Page("projeto-1-churn/app_churn.py", title="1. Predição de Churn", icon="👥"),
    st.Page("projeto-2-geomarketing/app_geo.py", title="2. Geomarketing", icon="🗺️"),
    st.Page("projeto-3-auditoria/app_audit.py", title="3. Auditoria Financeira", icon="🛡️"),
    st.Page("projeto-4-dashboard-kpi/app_kpi.py", title="4. Dashboard Estratégico", icon="📈"),
    st.Page("projeto-5-logistica/app_logist.py", title="5. Logística Real", icon="📦"),
])

# Rodar a navegação
pg.run()
