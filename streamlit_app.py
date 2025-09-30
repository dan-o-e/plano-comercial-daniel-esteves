import pandas as pd
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, text
import sys
import os
import re
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configurações de conexão
# Prioridade: Streamlit secrets > Variáveis de ambiente > Valores padrão
def get_db_config():
    try:
        # Tenta usar Streamlit secrets primeiro
        if hasattr(st, 'secrets') and 'database' in st.secrets:
            return {
                'host': st.secrets['database'].get('host', 'localhost'),
                'port': st.secrets['database'].get('port', 5433),
                'user': st.secrets['database'].get('user', 'postgres'),
                'password': st.secrets['database'].get('password', 'postgres'),
                'database': st.secrets['database'].get('database', 'base_btg')
            }
        else:
            # Usa variáveis de ambiente ou valores padrão
            return {
                'host': os.getenv('DB_HOST', 'localhost'),
                'port': int(os.getenv('DB_PORT', 5433)),
                'user': os.getenv('DB_USER', 'postgres'),
                'password': os.getenv('DB_PASSWORD', 'postgres'),
                'database': os.getenv('DB_NAME', 'base_btg')
            }
    except:
        # Fallback para desenvolvimento local
        return {
            'host': 'localhost',
            'port': 5433,
            'user': 'postgres',
            'password': 'postgres',
            'database': 'base_btg'
        }

def get_engine():
    """Cria conexão SQLAlchemy com o banco de dados"""
    DB_CONFIG = get_db_config()
    connection_string = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    return create_engine(connection_string)

@st.cache_data
def load_data():
    """Carrega dados do banco PostgreSQL"""
    try:
        engine = get_engine()
        query = "SELECT * FROM export"
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        st.error(f"Erro ao conectar com o banco de dados: {e}")
        return pd.DataFrame()

def format_currency(value):
    """Formata valores em moeda brasileira"""
    if pd.isna(value) or value is None:
        return "R$ 0,00"
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def format_number(value):
    """Formata números inteiros"""
    if pd.isna(value) or value is None:
        return "0"
    return f"{int(value):,}".replace(",", ".")

def main():
    st.set_page_config(
        page_title="Plano Comercial Daniel Esteves",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("📊 Plano Comercial Daniel Esteves")
    st.markdown("---")

    # Carrega os dados
    df = load_data()
    
    if df.empty:
        st.error("Não foi possível carregar os dados do banco de dados.")
        st.stop()

    # Remove linhas com PL total nulo e converte para float
    df_clean = df.dropna(subset=['pl_total']).copy()
    df_clean['pl_total'] = pd.to_numeric(df_clean['pl_total'], errors='coerce')
    df_clean = df_clean.dropna(subset=['pl_total'])

    # ============ SEÇÃO 1: PREMISSAS INICIAIS ============
    st.header("1º Passo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Premissas Iniciais")
        
        # Cálculos das premissas
        pl_atual = df_clean['pl_total'].sum()
        qtde_clientes = len(df_clean)
        ticket_medio = pl_atual / qtde_clientes if qtde_clientes > 0 else 0
        
        # Exibe as métricas em cards
        st.metric(
            label="PL Atual",
            value=format_currency(pl_atual)
        )
        
        st.metric(
            label="Qtde Total Clientes Ativos Atuais",
            value=format_number(qtde_clientes)
        )
        
        st.metric(
            label="Ticket Médio Atual",
            value=format_currency(ticket_medio)
        )

    with col2:
        st.subheader("🎯 Objetivos e Desafios")
        
        # Inputs do usuário
        horizonte_meses = st.number_input(
            "Horizonte de Análise (meses)",
            min_value=1,
            max_value=60,
            value=3,
            step=1
        )
        
        pl_projetado = st.number_input(
            "PL Projetado",
            min_value=0.0,
            value=5000000.0,
            step=100000.0,
            format="%.2f"
        )
        
        st.metric(
            label="Horizonte de Análise (meses)",
            value=f"{horizonte_meses} meses"
        )
        
        st.metric(
            label="PL Projetado",
            value=format_currency(pl_projetado)
        )

    st.markdown("---")

    # ============ SEÇÃO 2: ANÁLISE - CAPTAÇÃO E ATIVAÇÃO ============
    st.subheader("📊 Análise - Captação e Ativação")
    
    # Cálculos de captação
    captacao_periodo = pl_projetado - pl_atual
    captacao_mensal = captacao_periodo / horizonte_meses if horizonte_meses > 0 else 0
    captacao_semanal = captacao_mensal / 4
    captacao_diaria = captacao_mensal / 20

    # Exibe os resultados em colunas
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Captação no período",
            value=format_currency(captacao_periodo),
            delta=f"Diferença: {format_currency(captacao_periodo)}"
        )
    
    with col2:
        st.metric(
            label="Captação mensal",
            value=format_currency(captacao_mensal)
        )
    
    with col3:
        st.metric(
            label="Captação semanal",
            value=format_currency(captacao_semanal)
        )
    
    with col4:
        st.metric(
            label="Captação diária (20 dias)",
            value=format_currency(captacao_diaria)
        )

    st.markdown("---")

    # ============ SEÇÃO 3: GRÁFICOS E ANÁLISES ============
    st.subheader("📈 Análises Visuais")
    
    # Gráfico de distribuição do PL por cliente
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de barras - Top 10 clientes por PL
        top_10_clientes = df_clean.nlargest(10, 'pl_total')
        
        fig_bar = px.bar(
            top_10_clientes,
            x='nome',
            y='pl_total',
            title='Top 10 Clientes por Patrimônio Líquido',
            labels={'pl_total': 'PL Total (R$)', 'nome': 'Cliente'}
        )
        fig_bar.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        # Gráfico de pizza - Distribuição por estado
        df_estados = df_clean.groupby('estado')['pl_total'].sum().reset_index()
        df_estados = df_estados.sort_values('pl_total', ascending=False).head(10)
        
        fig_pie = px.pie(
            df_estados,
            values='pl_total',
            names='estado',
            title='Distribuição do PL por Estado (Top 10)'
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown("---")

    # ============ SEÇÃO 4: PROJEÇÃO MENSAL ============
    st.subheader("📅 Projeção Mensal")
    
    # Cria dados para projeção mensal
    meses = []
    pl_projecao = []
    pl_atual_temp = pl_atual
    
    for i in range(horizonte_meses + 1):
        if i == 0:
            meses.append(f"Atual")
            pl_projecao.append(pl_atual)
        else:
            meses.append(f"Mês {i}")
            pl_atual_temp += captacao_mensal
            pl_projecao.append(pl_atual_temp)
    
    # Cria DataFrame para o gráfico
    df_projecao = pd.DataFrame({
        'Período': meses,
        'PL Projetado': pl_projecao
    })
    
    # Gráfico de linha da projeção
    fig_line = px.line(
        df_projecao,
        x='Período',
        y='PL Projetado',
        title='Projeção de Crescimento do Patrimônio Líquido',
        markers=True
    )
    fig_line.update_layout(
        yaxis_title='PL (R$)',
        xaxis_title='Período'
    )
    st.plotly_chart(fig_line, use_container_width=True)

    # Tabela de projeção
    st.subheader("📋 Tabela de Projeção")
    df_projecao_display = df_projecao.copy()
    df_projecao_display['PL Projetado'] = df_projecao_display['PL Projetado'].apply(format_currency)
    st.dataframe(df_projecao_display, use_container_width=True)

    st.markdown("---")

    # ============ SEÇÃO 5: RESUMO EXECUTIVO ============
    st.subheader("📊 Resumo Executivo")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info(f"""
        **Situação Atual:**
        - PL Total: {format_currency(pl_atual)}
        - Clientes Ativos: {format_number(qtde_clientes)}
        - Ticket Médio: {format_currency(ticket_medio)}
        """)
    
    with col2:
        st.success(f"""
        **Meta Estabelecida:**
        - PL Projetado: {format_currency(pl_projetado)}
        - Prazo: {horizonte_meses} meses
        - Crescimento: {format_currency(captacao_periodo)}
        """)
    
    with col3:
        st.warning(f"""
        **Metas de Captação:**
        - Mensal: {format_currency(captacao_mensal)}
        - Semanal: {format_currency(captacao_semanal)}
        - Diária: {format_currency(captacao_diaria)}
        """)

    # ============ SEÇÃO 6: LISTA DE CLIENTES PARA CAPTAÇÃO ============
    st.markdown("---")
    st.subheader("📋 Lista de Clientes para Captação")
    
    # Opções para os dropdowns
    opcoes_origem = [
        "Família", "Relacionamento", "Indicação", "Redes Sociais", 
        "Palestras", "Alunos", "Já é Cliente", "Redes de Networking"
    ]
    
    opcoes_acao = [
        "Marcar 1ª Reunião", "Marcar 2ª Reunião", "Reunião de Acompanhamento",
        "Abrir Conta", "Trocar Assessoria", "Pedir TED", "Fazer STVM"
    ]
    
    opcoes_status = ["Quente", "Morno", "Frio"]
    
    # Inicializa session state para a lista de clientes
    if 'lista_captacao' not in st.session_state:
        # Pega os 20 primeiros clientes como exemplo
        clientes_exemplo = df_clean.head(20).copy()
        st.session_state.lista_captacao = []
        
        for i, (_, cliente) in enumerate(clientes_exemplo.iterrows(), 1):
            st.session_state.lista_captacao.append({
                'numero': i,
                'nome': cliente['nome'] if pd.notna(cliente['nome']) else f'Nome{i}',
                'pl_milhoes': round(cliente['pl_total'] / 1000000, 2),
                'planejado_migracao': 0.5,  # valor padrão
                'origem': 'Já é Cliente',  # valor padrão alterado
                'acao': 'Reunião de Acompanhamento',  # valor padrão alterado
                'status': 'Quente'  # valor padrão
            })
    
    # Controles para adicionar/remover clientes
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        if st.button("➕ Adicionar Cliente"):
            novo_numero = len(st.session_state.lista_captacao) + 1
            st.session_state.lista_captacao.append({
                'numero': novo_numero,
                'nome': f'Nome{novo_numero}',
                'pl_milhoes': 5.0,
                'planejado_migracao': 0.5,
                'origem': 'Já é Cliente',
                'acao': 'Reunião de Acompanhamento',
                'status': 'Quente'
            })
            st.rerun()
    
    with col2:
        if st.button("🔄 Resetar Lista"):
            del st.session_state.lista_captacao
            st.rerun()
    
    with col3:
        total_planejado = sum([cliente['planejado_migracao'] for cliente in st.session_state.lista_captacao])
        st.metric("Total Planejado:", f"R$ {total_planejado:.2f}M")
    
    # Função para definir cor da linha baseada no status
    def get_row_color(status):
        if status == "Quente":
            return "background-color: #ffe6e6; color: #000000"  # Vermelho claro com texto preto
        elif status == "Morno":
            return "background-color: #fff8dc; color: #000000"  # Amarelo claro com texto preto
        else:  # Frio
            return "background-color: #e8f5e8; color: #000000"  # Verde claro com texto preto
    
    # Tabela editável
    st.markdown("### 📊 Tabela de Clientes")
    
    # Headers da tabela
    col_header = st.columns([0.5, 2, 1.2, 1.5, 1.8, 1.8, 1.5, 0.5])
    headers = ["#", "Nome", "PL (milhões)", "Planejado Migração", "Origem", "Ação", "Status da Captação", ""]
    
    for i, header in enumerate(headers):
        with col_header[i]:
            st.markdown(f"**{header}**")
    
    # Linhas da tabela
    for i, cliente in enumerate(st.session_state.lista_captacao):
        # Aplica cor baseada no status
        status_color = get_row_color(cliente['status'])
        
        # Container com cor de fundo
        with st.container():
            st.markdown(f'<div style="{status_color}; padding: 10px; border-radius: 5px; margin: 5px 0;">', 
                       unsafe_allow_html=True)
            
            cols = st.columns([0.5, 2, 1.2, 1.5, 1.8, 1.8, 1.5, 0.5])
            
            with cols[0]:
                st.write(f"**{cliente['numero']}**")
            
            with cols[1]:
                novo_nome = st.text_input(
                    "Nome", 
                    value=cliente['nome'], 
                    key=f"nome_{i}",
                    #label_visibility="collapsed"
                )
                st.session_state.lista_captacao[i]['nome'] = novo_nome
            
            with cols[2]:
                novo_pl = st.number_input(
                    "PL", 
                    value=cliente['pl_milhoes'], 
                    min_value=0.0, 
                    step=0.1, 
                    format="%.2f",
                    key=f"pl_{i}",
                    #label_visibility="collapsed"
                )
                st.session_state.lista_captacao[i]['pl_milhoes'] = novo_pl
            
            with cols[3]:
                novo_planejado = st.number_input(
                    "Planejado", 
                    value=cliente['planejado_migracao'], 
                    min_value=0.0, 
                    step=0.1, 
                    format="%.2f",
                    key=f"planejado_{i}",
                    #label_visibility="collapsed"
                )
                st.session_state.lista_captacao[i]['planejado_migracao'] = novo_planejado
            
            with cols[4]:
                nova_origem = st.selectbox(
                    "Origem", 
                    opcoes_origem, 
                    index=opcoes_origem.index(cliente['origem']),
                    key=f"origem_{i}",
                    #label_visibility="collapsed"
                )
                st.session_state.lista_captacao[i]['origem'] = nova_origem
            
            with cols[5]:
                nova_acao = st.selectbox(
                    "Ação", 
                    opcoes_acao, 
                    index=opcoes_acao.index(cliente['acao']),
                    key=f"acao_{i}",
                    #label_visibility="collapsed"
                )
                st.session_state.lista_captacao[i]['acao'] = nova_acao
            
            with cols[6]:
                novo_status = st.selectbox(
                    "Status", 
                    opcoes_status, 
                    index=opcoes_status.index(cliente['status']),
                    key=f"status_{i}",
                    #label_visibility="collapsed"
                )
                st.session_state.lista_captacao[i]['status'] = novo_status
            
            with cols[7]:
                if st.button("🗑️", key=f"delete_{i}", help="Remover cliente"):
                    st.session_state.lista_captacao.pop(i)
                    # Renumera os clientes
                    for j, cliente_restante in enumerate(st.session_state.lista_captacao):
                        cliente_restante['numero'] = j + 1
                    st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Botão para exportar dados
    if st.button("📥 Exportar Lista para Excel"):
        df_export = pd.DataFrame(st.session_state.lista_captacao)
        df_export.columns = ['#', 'Nome', 'PL (milhões)', 'Planejado Migração', 'Origem', 'Ação', 'Status da Captação']
        
        # Converte para Excel em memória
        from io import BytesIO
        output = BytesIO()
        
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df_export.to_excel(writer, sheet_name='Lista_Captacao', index=False)
        
        excel_data = output.getvalue()
        
        st.download_button(
            label="⬇️ Download Excel",
            data=excel_data,
            file_name=f"lista_captacao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    # Resumo da lista
    st.markdown("---")
    st.subheader("📈 Resumo da Lista de Captação")
    
    col1, col2, col3, col4 = st.columns(4)
    
    # Calcula estatísticas
    total_clientes = len(st.session_state.lista_captacao)
    total_pl_atual = sum([cliente['pl_milhoes'] for cliente in st.session_state.lista_captacao])
    total_planejado = sum([cliente['planejado_migracao'] for cliente in st.session_state.lista_captacao])
    
    # Conta por status
    status_counts = {}
    for status in opcoes_status:
        status_counts[status] = len([c for c in st.session_state.lista_captacao if c['status'] == status])
    
    with col1:
        st.metric("Total de Clientes", total_clientes)
        st.metric("PL Atual Total", f"R$ {total_pl_atual:.2f}M")
    
    with col2:
        st.metric("Planejado Total", f"R$ {total_planejado:.2f}M")
        st.metric("Diferença", f"R$ {total_planejado - total_pl_atual:.2f}M")
    
    with col3:
        st.metric("🔥 Quentes", status_counts['Quente'])
        st.metric("🟡 Mornos", status_counts['Morno'])
    
    with col4:
        st.metric("❄️ Frios", status_counts['Frio'])
        if total_clientes > 0:
            conversion_rate = (status_counts['Quente'] / total_clientes) * 100
            st.metric("Taxa Quente", f"{conversion_rate:.1f}%")

    # ============ SEÇÃO 7: VISUALIZAÇÃO DA TABELA FINAL ============
    st.markdown("---")
    st.subheader("📋 Visualização Final da Lista")
    
    if st.session_state.lista_captacao:
        # Cria DataFrame para exibição
        df_display = pd.DataFrame(st.session_state.lista_captacao)
        df_display = df_display.rename(columns={
            'numero': '#',
            'nome': 'Nome',
            'pl_milhoes': 'PL (milhões)',
            'planejado_migracao': 'Planejado Migração',
            'origem': 'Origem',
            'acao': 'Ação',
            'status': 'Status da Captação'
        })
        
        # Função para aplicar cores às linhas
        def highlight_status(row):
            if row['Status da Captação'] == 'Quente':
                return ['background-color: #ffe6e6; color: #000000'] * len(row)
            elif row['Status da Captação'] == 'Morno':
                return ['background-color: #fff8dc; color: #000000'] * len(row)
            else:  # Frio
                return ['background-color: #e8f5e8; color: #000000'] * len(row)
        
        # Aplica formatação e exibe a tabela
        styled_df = df_display.style.apply(highlight_status, axis=1)
        st.dataframe(styled_df, width="stretch", hide_index=True)
        
        # Cálculo do total
        total_atual = df_display['PL (milhões)'].sum()
        total_planejado = df_display['Planejado Migração'].sum()
        
        st.markdown(f"""
        **Totais:**
        - PL Atual Total: R$ {total_atual:.2f} milhões
        - Planejado Total: R$ {total_planejado:.2f} milhões
        - Crescimento Esperado: R$ {total_planejado - total_atual:.2f} milhões
        """)
    else:
        st.info("Nenhum cliente na lista. Clique em 'Adicionar Cliente' para começar.")

    # ============ SIDEBAR COM FILTROS ============
    st.sidebar.header("🔍 Filtros")
    
    # Filtro por estado
    estados_disponiveis = ['Todos'] + sorted(df_clean['estado'].dropna().unique().tolist())
    estado_selecionado = st.sidebar.selectbox("Estado:", estados_disponiveis)
    
    # Filtro por faixa de PL
    pl_min = st.sidebar.number_input("PL Mínimo:", min_value=0.0, value=0.0)
    pl_max = st.sidebar.number_input("PL Máximo:", min_value=0.0, value=float(df_clean['pl_total'].max()))
    
    # Aplica filtros
    df_filtered = df_clean.copy()
    if estado_selecionado != 'Todos':
        df_filtered = df_filtered[df_filtered['estado'] == estado_selecionado]
    
    df_filtered = df_filtered[
        (df_filtered['pl_total'] >= pl_min) & 
        (df_filtered['pl_total'] <= pl_max)
    ]
    
    # Mostra estatísticas dos dados filtrados
    st.sidebar.subheader("📈 Dados Filtrados")
    st.sidebar.metric("Clientes:", len(df_filtered))
    st.sidebar.metric("PL Total:", format_currency(df_filtered['pl_total'].sum()))
    if len(df_filtered) > 0:
        st.sidebar.metric("Ticket Médio:", format_currency(df_filtered['pl_total'].mean()))

if __name__ == "__main__":
    main()