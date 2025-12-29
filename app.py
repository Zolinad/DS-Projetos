import streamlit as st

# 1. Configuração inicial
st.set_page_config(layout="wide", page_title="Portfólio de Data Science - Danilo A. F.")

# 2. TRUQUE PARA O TOPO: st.logo 
# O st.logo é o ÚNICO componente que fica acima do menu de navegação
# Vamos usar um link de imagem transparente ou seu próprio avatar do GitHub para abrir espaço
st.logo("https://github.com/Zolinad.png", link="https://github.com/Zolinad")

# 3. IDENTIFICAÇÃO NA SIDEBAR
with st.sidebar:
    st.markdown(f"## Danilo Azevedo Figueiredo")
    st.markdown("### Cientista de Dados")
    
    # Contatos imediatamente após o nome
    st.markdown("""
        [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/danilo-a-fig)
        [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Zolinad)
    """)
    st.divider()

# 4. NAVEGAÇÃO
pg = st.navigation({
    "Projetos": [
        st.Page("projeto-1-churn/app_churn.py", title="1. Predição de Churn", icon="👥"),
        st.Page("projeto-2-geomarketing/app_geo.py", title="2. Geomarketing", icon="🗺️"),
        st.Page("projeto-3-auditoria/app_audit.py", title="3. Auditoria Financeira", icon="🛡️"),
        st.Page("projeto-4-dashboard-kpi/app_kpi.py", title="4. Dashboard Estratégico", icon="📈"),
        st.Page("projeto-5-logistica/app_logist.py", title="5. Logística Real", icon="📦"),
    ]
})

pg.run()
