import streamlit as st

# 1. Configuração de página
st.set_page_config(layout="wide", page_title="Portfólio de Data Science - Danilo A. F.")

# 2. CONTEÚDO MANUAL NA SIDEBAR (Isso aparecerá acima da navegação)
with st.sidebar:
    st.markdown("## Danilo Azevedo Figueiredo")
    st.markdown("### Cientista de Dados")
    
    # Seus contatos conforme constam no currículo
    st.markdown("""
        [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/danilo-a-fig)
        [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Zolinad)
    """)
    st.divider()
    st.markdown("### Navegação do Portfólio 👇")

# 3. CONFIGURAÇÃO DA NAVEGAÇÃO
# Esta lista reflete os projetos do seu repositório e currículo
pg = st.navigation({
    "Menu": [
        st.Page("projeto-1-churn/app_churn.py", title="1. Predição de Churn", icon="👥"),
        st.Page("projeto-2-geomarketing/app_geo.py", title="2. Geomarketing", icon="🗺️"),
        st.Page("projeto-3-auditoria/app_audit.py", title="3. Auditoria Financeira", icon="🛡️"),
        st.Page("projeto-4-dashboard-kpi/app_kpi.py", title="4. Dashboard Estratégico", icon="📈"),
        st.Page("projeto-5-logistica/app_logist.py", title="5. Logística Real", icon="📦"),
    ]
})

# 4. Execução
pg.run()
