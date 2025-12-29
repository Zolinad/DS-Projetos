# Auditoria Financeira e Detecção de Anomalia com AI:

## Sobre o Projeto
Este projeto é uma ferramenta de **Auditoria Automatizada** desenvolvida para detectar fraudes, erros operacionais e gastos atípicos em bases de dados financeiras.

Utilizando o algoritmo de Machine Learning não-supervisionado **Isolation Forest**, o sistema analisa centenas de transações e isola geometricamente aquelas que desviam do padrão estatístico da organização, permitindo uma gestão baseada em exceção.

## Funcionalidades
* **Detecção Automática:** O usuário não precisa definir regras (ex: "gasto > 5000"). O modelo aprende sozinho o que é normal e alerta o que foge do padrão.
* **Ajuste de Sensibilidade:** Controle deslizante para definir o rigor da auditoria (Contamination Rate).
* **Painel de Investigação:** Lista detalhada das transações suspeitas com ID, Departamento e Valor.
* **Visualização Temporal:** Gráfico interativo que destaca os outliers em vermelho ao longo do tempo.

## Lógica e Aplicabilidade (Transfer Learning)
A técnica de Detecção de Anomalias (Anomaly Detection) aqui aplicada é fundamental para transparência e eficiência em diversos setores:

1.  **Compliance Corporativo:** Auditoria de despesas de viagem e cartões corporativos.
2.  **Indústria:** Detecção de falhas em sensores de máquinas (Manutenção Preditiva).
3.  **Gestão Pública (Educação/Saúde):**
    * Identificação de escolas com consumo de energia/água desproporcional ao número de alunos.
    * Auditoria de custos de merenda escolar (Preço/kg acima da média de mercado).
    * Detecção de inconsistências na folha de pagamento.

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Frontend:** Streamlit
* **Machine Learning:** Scikit-Learn (Ensemble Isolation Forest)
* **Visualização:** Plotly Express
