def exibir_readme(caminho_readme):
    with open(caminho_readme, "r", encoding="utf-8") as f:
        conteudo = f.read()
    
    # Criamos um "Expander" (menu retrátil) para o README não ocupar a tela toda
    with st.expander("📖 Sobre este Projeto (Documentação)", expanded=True):
        st.markdown(conteudo)

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# --- 1. GERAR DADOS FICTÍCIOS (Para funcionar sem baixar nada) ---
# Criados 200 clientes falsos para o treinamento do modelo
np.random.seed(42)
n_linhas = 200

data = {
    'Meses_de_Contrato': np.random.randint(1, 48, n_linhas),
    'Valor_Mensalidade': np.random.randint(50, 150, n_linhas),
    'Numero_Reclamacoes': np.random.randint(0, 5, n_linhas)
}
df = pd.DataFrame(data)

# Criada a resposta (para Quem cancelou) baseada em uma regra lógica
# Regra: Se reclamou mais de 2 vezes OU paga caro e é cliente novo -> Cancela (1)
df['Cancelou'] = np.where(
    (df['Numero_Reclamacoes'] > 2) | 
    ((df['Valor_Mensalidade'] > 100) & (df['Meses_de_Contrato'] < 6)), 
    1, 0
)

# --- 2. TREINAR O MODELO ---
X = df[['Meses_de_Contrato', 'Valor_Mensalidade', 'Numero_Reclamacoes']]
y = df['Cancelou']

modelo = RandomForestClassifier(n_estimators=50, random_state=42)
modelo.fit(X, y)

# --- 3. A TELA DO APLICATIVO ---
st.title("Sistema de Predição de Churn")
st.markdown("Este modelo usa um algoritmo de aprendizagem de máquina para prever a probabilidade de um cliente cancelar o seu contrato (Churn).")
st.info("Utilize os controles abaixo para simular o perfil do cliente e verificar a retenção.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Simular Perfil do Cliente")
    # Sliders
    meses = st.slider("Tempo de Casa (Meses)", 1, 48, 12)
    valor = st.slider("Valor da Mensalidade ($)", 50, 150, 80)
    reclamacoes = st.slider("Número de Reclamações", 0, 5, 0)
    
    botao = st.button("Calcular Probabilidade", type="primary")

with col2:
    if botao:
        # Prepara os dados do usuário para o modelo
        entrada = pd.DataFrame([[meses, valor, reclamacoes]], 
                             columns=['Meses_de_Contrato', 'Valor_Mensalidade', 'Numero_Reclamacoes'])
        
        # O modelo faz a previsão
        probabilidade = modelo.predict_proba(entrada)[0][1] # Pega a chance de ser 1 (Sim)
        
        st.subheader("Resultado da Análise:")
        st.metric(label="Risco Calculado", value=f"{probabilidade:.0%}")
        
        if probabilidade > 0.6:
            st.error("🚨 RISCO ALTO: Tendência de Cancelamento.")
            st.write("**Ação Recomendada:** Entrar em contato para oferecer desconto ou upgrade.")
        else:
            st.success("RISCO BAIXO: Cliente Fidelizado.")
            st.write("**Situação:** O cliente apresenta comportamento estável.")
