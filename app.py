import streamlit as st

# Configuração da Página Principal
st.set_page_config(layout="wide", page_title="Portfólio de Data Science - Danilo A. F.")

# --- BARRA LATERAL: IDENTIFICAÇÃO E CONTATOS ---
st.sidebar.title("Danilo Azevedo Figueiredo")
st.sidebar.write("Cientista de Dados")

# Selos de contato (Badges) para facilitar o clique
st.sidebar.markdown("""
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/danilo-a-fig)
    [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Zolinad)
""")

st.sidebar.divider()
st.sidebar.markdown("### Navegação do Portfólio 👇")

# --- CONFIGURAÇÃO DA NAVEGAÇÃO ---
pg = st.navigation([
    st.Page("projeto-1-churn/app_churn.py", title="1. Predição de Churn", icon="👥"),
    st.Page("projeto-2-geomarketing/app_geo.py", title="2. Geomarketing", icon="🗺️"),
    st.Page("projeto-3-auditoria/app_audit.py", title="3. Auditoria Financeira", icon="🛡️"),
    st.Page("projeto-4-dashboard-kpi/app_kpi.py", title="4. Dashboard Estratégico", icon="📈"),
    st.Page("projeto-5-logistica/app_logist.py", title="5. Logística Real", icon="📦"),
])

# Rodar a navegação
pg.run()
