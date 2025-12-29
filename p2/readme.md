# 🏢 Corporate Churn Prediction System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)

## 📋 Sobre o Projeto
Este é um projeto de **Business Analytics** focado na retenção de clientes. Desenvolvi uma aplicação web interativa que utiliza Machine Learning para prever a probabilidade de **Churn** (cancelamento de contrato) com base em padrões comportamentais e financeiros.

O objetivo é fornecer aos gestores uma ferramenta simples para simular cenários e identificar perfis de risco antes que o cliente deixe a empresa.

## 🚀 Funcionalidades
* **Geração de Dados Sintéticos:** O sistema não depende de arquivos externos; ele simula uma base de dados realista de telecomunicações para treinamento em tempo real.
* **Modelo Preditivo:** Utiliza o algoritmo **Random Forest Classifier** para classificar o risco.
* **Simulador Interativo:** Interface amigável onde o usuário pode alterar variáveis (mensalidade, chamados ao suporte, tempo de casa) e ver a probabilidade de cancelamento mudar instantaneamente.
* **Diagnóstico Automático:** O sistema sugere ações de retenção (ex: descontos ou upgrade) baseadas no nível de risco calculado.

## 🧠 Lógica e Aplicabilidade (Transfer Learning)
Embora este dashboard esteja configurado para um cenário de **Telecomunicações**, a arquitetura matemática desenvolvida é agnóstica e transferível para outros setores que lidam com análise de risco e evasão:

1.  **Setor Corporativo:** Rotatividade de Funcionários (Turnover).
2.  **Setor Financeiro:** Detecção de Fraudes ou Inadimplência.
3.  **Setor Público / Educação:** Predição de **Evasão Escolar** (substituindo "Fatura" por "Notas" e "Suporte" por "Faltas").

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Frontend:** Streamlit
* **Manipulação de Dados:** Pandas / NumPy
* **Machine Learning:** Scikit-Learn (Random Forest)

## 📦 Como Rodar o Projeto

1. Clone este repositório:
```bash
git clone [https://github.com/SEU-USUARIO/churn-prediction.git](https://github.com/SEU-USUARIO/churn-prediction.git)
