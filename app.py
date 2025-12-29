import streamlit as st

# 1. Configuração de página
st.set_page_config(layout="wide", page_title="Portfólio de Data Science - Danilo A. F.")

# 2. CONTEÚDO DO TOPO DA SIDEBAR (Forçado antes da navegação)
with st.sidebar:
    st.title("Danilo Azevedo Figueiredo")
    st.write("Cientista de Dados")
    
    # Badges de contato imediatamente abaixo do nome
    st.markdown("""
        [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/danilo-a-fig)
        [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Zolinad)
    """)
    st.divider()
    st.markdown("### Navegação do Portfólio 👇")

# 3. CONFIGURAÇÃO DA NAVEGAÇÃO
# O Streamlit vai colocar este menu logo após o último elemento declarado acima
pg = st.navigation([
    st.Page("projeto-1-churn/app_churn.py", title="1. Predição de Churn", icon="👥"),
    st.Page("projeto-2-geomarketing/app_geo.py", title="2. Geomarketing", icon="🗺️"),
    st.Page("projeto-3-auditoria/app_audit.py", title="3. Auditoria Financeira", icon="🛡️"),
    st.Page("projeto-4-dashboard-kpi/app_kpi.py", title="4. Dashboard Estratégico", icon="📈"),
    st.Page("projeto-5-logistica/app_logist.py", title="5. Logística Real", icon="📦"),
], position="sidebar") # Reforça a posição na sidebar

# 4. Execução
pg.run()
