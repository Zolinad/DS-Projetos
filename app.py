import streamlit as st

# 1. Configuração inicial (Sempre a primeira linha de comando st)
st.set_page_config(layout="wide", page_title="Portfólio de Data Science - Danilo A. F.") [cite: 1, 2]

# 2. IDENTIFICAÇÃO NO TOPO DA SIDEBAR
# Isso garante que seu nome apareça acima de qualquer outra coisa na lateral
st.sidebar.title("Danilo Azevedo Figueiredo") [cite: 1]
st.sidebar.write("Cientista de Dados") [cite: 2]

# Badges de contato logo abaixo do nome
st.sidebar.markdown("""
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/danilo-a-fig) [cite: 4]
    [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Zolinad) [cite: 6]
""")

st.sidebar.divider()
st.sidebar.markdown("### Navegação do Portfólio 👇")

# 3. CONFIGURAÇÃO DA NAVEGAÇÃO (Aparecerá abaixo dos seus contatos)
pg = st.navigation([
    st.Page("projeto-1-churn/app_churn.py", title="1. Predição de Churn", icon="👥"), [cite: 36]
    st.Page("projeto-2-geomarketing/app_geo.py", title="2. Geomarketing", icon="🗺️"), [cite: 37]
    st.Page("projeto-3-auditoria/app_audit.py", title="3. Auditoria Financeira", icon="🛡️"), [cite: 38]
    st.Page("projeto-4-dashboard-kpi/app_kpi.py", title="4. Dashboard Estratégico", icon="📈"), [cite: 39]
    st.Page("projeto-5-logistica/app_logist.py", title="5. Logística Real", icon="📦"), [cite: 40]
])

# 4. Execução do App
pg.run()
