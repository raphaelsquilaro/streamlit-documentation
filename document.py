# Author: Raphael Campos Squilaro
# Project: Learning streamlit

# ============================================================
# IMPORTAÇÃO DAS BIBLIOTECAS
# ============================================================

import streamlit as st
import pandas as pd

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Guia de Comandos Streamlit",
    page_icon="🐍",
    layout="wide"
)

# ============================================================
# ESTILO
# ============================================================

st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 0;
    }

    .subtitle {
        font-size: 20px;
        color: #777;
        margin-top: 0;
    }

    .command-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #f5f5f5;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# MENU LATERAL
# ============================================================

st.sidebar.title("🐍 Streamlit")

st.sidebar.markdown(
    "### Guia de comandos"
)

pagina = st.sidebar.radio(
    "Navegação",
    [
        "🏠 Início",
        "📝 Textos",
        "🔘 Botões e entradas",
        "📐 Layout",
        "📊 Dados e gráficos",
        "💬 Mensagens",
        "📁 Arquivos",
        "🧩 Componentes",
        "⚙️ Configuração",
        "🚀 Exemplo completo"
    ]
)


# ============================================================
# INÍCIO
# ============================================================

if pagina == "🏠 Início":

    st.markdown(
        '<p class="main-title">🐍 Guia de Streamlit</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle">Aprenda os principais comandos do Streamlit '
        'de forma prática e interativa.</p>',
        unsafe_allow_html=True
    )

    st.divider()

    st.header("O que é Streamlit?")

    st.write("""
    Streamlit é um framework Python utilizado para criar aplicações web
    interativas de maneira rápida, especialmente para projetos de dados,
    dashboards, inteligência artificial e protótipos.
    """)

    st.info(
        "A ideia principal do Streamlit é transformar código Python "
        "em uma interface web sem precisar escrever HTML, CSS e JavaScript."
    )

    st.header("🚀 Como começar")

    st.code(
        "pip install streamlit",
        language="bash"
    )

    st.code(
        "streamlit run app.py",
        language="bash"
    )

    st.header("Estrutura básica")

    st.code(
        '''import streamlit as st

st.title("Minha aplicação")
st.write("Olá, mundo!")''',
        language="python"
    )

    st.success(
        "Crie um arquivo chamado app.py e execute "
        "`streamlit run app.py` no terminal."
    )


# ============================================================
# TEXTOS
# ============================================================

elif pagina == "📝 Textos":

    st.title("📝 Comandos para textos")

    st.write(
        "O Streamlit possui vários comandos para apresentar "
        "informações na tela."
    )

    st.subheader("st.title()")

    st.write("Cria o título principal da página.")

    st.code(
        'st.title("Meu Dashboard")',
        language="python"
    )

    st.title("Meu Dashboard")

    st.divider()

    st.subheader("st.header()")

    st.write("Cria um cabeçalho de seção.")

    st.code(
        'st.header("Vendas")',
        language="python"
    )

    st.header("Vendas")

    st.divider()

    st.subheader("st.subheader()")

    st.write("Cria um título menor dentro de uma seção.")

    st.code(
        'st.subheader("Vendas por mês")',
        language="python"
    )

    st.subheader("Vendas por mês")

    st.divider()

    st.subheader("st.write()")

    st.write(
        "É um dos comandos mais versáteis do Streamlit. "
        "Pode exibir texto, números, objetos e outros elementos."
    )

    st.code(
        'st.write("Olá, Streamlit!")',
        language="python"
    )

    st.write("Olá, Streamlit!")

    st.divider()

    st.subheader("st.markdown()")

    st.write("Permite utilizar Markdown.")

    st.code(
        '''st.markdown(
    "**Texto em negrito** e *texto em itálico*"
)''',
        language="python"
    )

    st.markdown(
        "**Texto em negrito** e *texto em itálico*"
    )

    st.divider()

    st.subheader("st.code()")

    st.write("Exibe código formatado.")

    st.code(
        '''def saudacao(nome):
    return f"Olá, {nome}!"''',
        language="python"
    )

    st.divider()

    st.subheader("st.caption()")

    st.write("Exibe um texto pequeno, normalmente utilizado como observação.")

    st.code(
        'st.caption("Última atualização: hoje")',
        language="python"
    )

    st.caption("Última atualização: hoje")


# ============================================================
# BOTÕES E ENTRADAS
# ============================================================

elif pagina == "🔘 Botões e entradas":

    st.title("🔘 Botões e campos de entrada")

    st.write(
        "Esses componentes permitem que o usuário interaja "
        "com sua aplicação."
    )

    st.subheader("st.button()")

    st.write("Cria um botão.")

    st.code(
        '''if st.button("Clique aqui"):
    st.success("Você clicou no botão!")''',
        language="python"
    )

    if st.button("Clique aqui"):
        st.success("Você clicou no botão!")

    st.divider()

    st.subheader("st.text_input()")

    st.write("Cria um campo para entrada de texto.")

    st.code(
        'nome = st.text_input("Digite seu nome")',
        language="python"
    )

    nome = st.text_input("Digite seu nome")

    if nome:
        st.write(f"Olá, {nome}!")

    st.divider()

    st.subheader("st.number_input()")

    st.write("Permite que o usuário informe um número.")

    st.code(
        '''idade = st.number_input(
    "Digite sua idade",
    min_value=0,
    max_value=120
)''',
        language="python"
    )

    idade = st.number_input(
        "Digite sua idade",
        min_value=0,
        max_value=120
    )

    st.write("Valor:", idade)

    st.divider()

    st.subheader("st.selectbox()")

    st.write("Cria uma lista de opções.")

    st.code(
        '''opcao = st.selectbox(
    "Escolha uma opção",
    ["Python", "Java", "JavaScript"]
)''',
        language="python"
    )

    opcao = st.selectbox(
        "Escolha uma opção",
        ["Python", "Java", "JavaScript"]
    )

    st.write("Você escolheu:", opcao)

    st.divider()

    st.subheader("st.checkbox()")

    st.code(
        'aceito = st.checkbox("Aceito os termos")',
        language="python"
    )

    aceito = st.checkbox("Aceito os termos")

    if aceito:
        st.success("Opção selecionada!")


# ============================================================
# LAYOUT
# ============================================================

elif pagina == "📐 Layout":

    st.title("📐 Layout")

    st.write(
        "O Streamlit possui componentes para organizar "
        "os elementos da página."
    )

    st.subheader("st.columns()")

    st.write("Cria colunas.")

    st.code(
        '''col1, col2 = st.columns(2)

with col1:
    st.write("Coluna 1")

with col2:
    st.write("Coluna 2")''',
        language="python"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info("Coluna 1")

    with col2:
        st.success("Coluna 2")

    st.divider()

    st.subheader("st.tabs()")

    st.write("Cria abas.")

    st.code(
        '''aba1, aba2 = st.tabs(["Dados", "Gráfico"])

with aba1:
    st.write("Dados")

with aba2:
    st.write("Gráfico")''',
        language="python"
    )

    aba1, aba2 = st.tabs(["Dados", "Gráfico"])

    with aba1:
        st.write("Conteúdo da aba Dados")

    with aba2:
        st.write("Conteúdo da aba Gráfico")

    st.divider()

    st.subheader("st.expander()")

    st.write("Cria uma área que pode ser expandida.")

    st.code(
        '''with st.expander("Clique para abrir"):
    st.write("Conteúdo escondido")''',
        language="python"
    )

    with st.expander("Clique para abrir"):
        st.write("Conteúdo escondido")


# ============================================================
# DADOS E GRÁFICOS
# ============================================================

elif pagina == "📊 Dados e gráficos":

    st.title("📊 Dados e gráficos")

    st.write(
        "O Streamlit funciona muito bem com Pandas e bibliotecas "
        "de análise de dados."
    )

    st.subheader("st.dataframe()")

    st.write("Exibe uma tabela interativa.")

    st.code(
        '''import pandas as pd

df = pd.DataFrame({
    "Produto": ["A", "B", "C"],
    "Vendas": [100, 200, 150]
})

st.dataframe(df)''',
        language="python"
    )

    import pandas as pd

    df = pd.DataFrame({
        "Produto": ["Produto A", "Produto B", "Produto C"],
        "Vendas": [100, 200, 150]
    })

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("st.metric()")

    st.write("Exibe uma métrica ou indicador.")

    st.code(
        'st.metric("Vendas", "R$ 25.000", "+12%")',
        language="python"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Vendas", "R$ 25.000", "+12%")

    with col2:
        st.metric("Clientes", "1.250", "+8%")

    with col3:
        st.metric("Pedidos", "580", "+15%")

    st.divider()

    st.subheader("Gráficos")

    st.write("O Streamlit possui comandos simples para gráficos.")

    st.code(
        '''st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)''',
        language="python"
    )

    st.line_chart(df.set_index("Produto"))

    st.bar_chart(df.set_index("Produto"))


# ============================================================
# MENSAGENS
# ============================================================

elif pagina == "💬 Mensagens":

    st.title("💬 Mensagens")

    st.write(
        "Use mensagens para informar o usuário sobre o estado "
        "de uma operação."
    )

    st.subheader("st.success()")

    st.code(
        'st.success("Operação concluída!")',
        language="python"
    )

    st.success("Operação concluída!")

    st.subheader("st.info()")

    st.code(
        'st.info("Esta é uma informação.")',
        language="python"
    )

    st.info("Esta é uma informação.")

    st.subheader("st.warning()")

    st.code(
        'st.warning("Atenção!")',
        language="python"
    )

    st.warning("Atenção!")

    st.subheader("st.error()")

    st.code(
        'st.error("Ocorreu um erro.")',
        language="python"
    )

    st.error("Ocorreu um erro!")


# ============================================================
# ARQUIVOS
# ============================================================

elif pagina == "📁 Arquivos":

    st.title("📁 Upload de arquivos")

    st.write(
        "Use `st.file_uploader()` para permitir que o usuário "
        "envie arquivos."
    )

    st.code(
        '''arquivo = st.file_uploader(
    "Escolha um arquivo",
    type=["csv", "xlsx", "pdf"]
)

if arquivo:
    st.success("Arquivo recebido!")''',
        language="python"
    )

    arquivo = st.file_uploader(
        "Escolha um arquivo",
        type=["csv", "xlsx", "pdf"]
    )

    if arquivo:
        st.success(
            f"Arquivo recebido: {arquivo.name}"
        )

        st.write(
            "Tamanho:",
            arquivo.size,
            "bytes"
        )


# ============================================================
# COMPONENTES
# ============================================================

elif pagina == "🧩 Componentes":

    st.title("🧩 Outros componentes úteis")

    st.subheader("st.divider()")

    st.write(
        "Cria uma linha horizontal para separar seções."
    )

    st.code(
        "st.divider()",
        language="python"
    )

    st.divider()

    st.subheader("st.image()")

    st.write(
        "Exibe uma imagem."
    )

    st.code(
        '''st.image(
    "imagem.jpg",
    caption="Minha imagem"
)''',
        language="python"
    )

    st.subheader("st.progress()")

    st.write("Cria uma barra de progresso.")

    st.code(
        'st.progress(70)',
        language="python"
    )

    st.progress(70)

    st.subheader("st.spinner()")

    st.write(
        "Mostra uma indicação enquanto uma operação está acontecendo."
    )

    st.code(
        '''with st.spinner("Processando..."):
    # operação
    pass''',
        language="python"
    )


# ============================================================
# CONFIGURAÇÃO
# ============================================================

elif pagina == "⚙️ Configuração":

    st.title("⚙️ Configuração da página")

    st.write(
        "O comando `st.set_page_config()` deve normalmente "
        "ser executado no início da aplicação."
    )

    st.code(
        '''st.set_page_config(
    page_title="Meu aplicativo",
    page_icon="🚀",
    layout="wide"
)''',
        language="python"
    )

    st.subheader("page_title")

    st.write(
        "Define o título exibido na aba do navegador."
    )

    st.subheader("page_icon")

    st.write(
        "Define o ícone da página."
    )

    st.subheader("layout")

    st.write(
        "Pode ser utilizado para definir a largura da aplicação."
    )

    st.code(
        'layout="wide"',
        language="python"
    )

    st.divider()

    st.subheader("Barra lateral")

    st.code(
        '''with st.sidebar:
    st.title("Menu")
    st.button("Início")
    st.button("Configurações")''',
        language="python"
    )

    with st.sidebar:
        st.write("Este conteúdo está na barra lateral.")


# ============================================================
# EXEMPLO COMPLETO
# ============================================================

elif pagina == "🚀 Exemplo completo":

    st.title("🚀 Exemplo completo")

    st.write(
        "Abaixo está um pequeno dashboard combinando "
        "vários comandos do Streamlit."
    )

    st.code(
        '''import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard de Vendas")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Vendas", "R$ 50.000")

with col2:
    st.metric("Clientes", "2.500")

with col3:
    st.metric("Pedidos", "850")

df = pd.DataFrame({
    "Mês": ["Jan", "Fev", "Mar", "Abr"],
    "Vendas": [10000, 15000, 12000, 18000]
})

st.subheader("Vendas por mês")

st.bar_chart(
    df.set_index("Mês")
)

st.dataframe(
    df,
    use_container_width=True
)''',
        language="python"
    )

    st.divider()

    st.subheader("Resultado")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Vendas", "R$ 50.000")

    with col2:
        st.metric("Clientes", "2.500")

    with col3:
        st.metric("Pedidos", "850")

    df = pd.DataFrame({
        "Mês": ["Jan", "Fev", "Mar", "Abr"],
        "Vendas": [10000, 15000, 12000, 18000]
    })

    st.subheader("Vendas por mês")

    st.bar_chart(
        df.set_index("Mês")
    )

    st.dataframe(
        df,
        use_container_width=True
    )


# ============================================================
# RODAPÉ
# ============================================================

st.divider()

st.caption(
    "🐍 Guia de comandos Streamlit — desenvolvido em Python"
)
