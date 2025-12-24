import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Painel Royalties AM", layout="wide")

# DADOS SIMULADOS
data = {
    'municipio': ['Coari', 'Município A (Liminar)', 'Tefé', 'Município B (Liminar)', 'Codajás'],
    'ranking': [1, 2, 3, 4, 5],
    'grupo': ['ANP', 'Liminar', 'ANP', 'Liminar', 'ANP'],
    'arrecadacao_total': [150000000.00, 85000000.00, 60000000.00, 45000000.00, 30000000.00],
    'tem_portal': ['Sim', 'Não', 'Sim', 'Parcial', 'Sim'],
    'maior_beneficiario_tipo': ['Obras', 'Advocacia', 'Saúde', 'Advocacia', 'Obras'],
    'pagou_inss_irregular': ['Não', 'Sim', 'Não', 'Sim', 'Não'],
    'perc_educacao': [70, 5, 76, 0, 75],
    'perc_saude': [20, 5, 25, 0, 26],
    'analise_texto': ["Ok.", "Suspeita.", "Ok.", "Risco.", "Ok."]
}
df = pd.DataFrame(data)

def plot_compliance(educacao, saude):
    outros = 100 - (educacao + saude)
    if outros < 0: outros = 0
    fig = go.Figure(data=[go.Pie(labels=['Educação','Saúde','Outros'], values=[educacao, saude, outros])])
    fig.update_layout(height=250, margin=dict(t=0, b=0, l=0, r=0))
    return fig

st.title("Rastreador de Royalties - Amazônia")
view = st.sidebar.radio("Ver:", ["Ranking", "Detalhes"])

if view == "Ranking":
    st.header("Ranking dos Top 5")
    st.dataframe(df)
else:
    cidade = st.sidebar.selectbox("Cidade:", df['municipio'])
    linha = df[df['municipio'] == cidade].iloc[0]
    st.metric("Receita", f"R$ {linha['arrecadacao_total']:,.2f}")
    st.plotly_chart(plot_compliance(linha['perc_educacao'], linha['perc_saude']))
