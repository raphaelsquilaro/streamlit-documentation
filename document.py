# 🐍 Guia de Comandos Streamlit

Aplicação web desenvolvida em **Python + Streamlit** com o objetivo de apresentar, de forma prática e interativa, os principais comandos e componentes do Streamlit.

O projeto foi desenvolvido como material de **aprendizado e consulta**, permitindo visualizar a explicação de cada comando juntamente com exemplos de código e seu resultado na interface.

---

## 👨‍💻 Autor

**Raphael Campos Squilaro**

Projeto: **Learning Streamlit**

---

## 📚 Sobre o projeto

Este projeto é um guia interativo para quem está começando a trabalhar com **Streamlit**.

A aplicação possui um menu lateral que permite navegar entre diferentes categorias de comandos.

Cada seção apresenta:

- 📖 Explicação do comando
- 💻 Exemplo de código
- 🖥️ Demonstração do componente
- 🧩 Aplicações práticas
- 📊 Exemplos de dados e gráficos

A proposta é aprender Streamlit através de exemplos executáveis, em vez de apenas consultar documentação.

---

## 🚀 Funcionalidades

O projeto apresenta exemplos das seguintes funcionalidades:

### 🏠 Início

Introdução ao Streamlit e exemplo básico de uma aplicação.

Exemplo:

```python
import streamlit as st

st.title("Minha aplicação")
st.write("Olá, mundo!")
```

---

### 📝 Textos

Demonstra os principais comandos utilizados para apresentar textos:

- `st.title()`
- `st.header()`
- `st.subheader()`
- `st.write()`
- `st.markdown()`
- `st.code()`
- `st.caption()`

---

### 🔘 Botões e entradas

Exemplos de componentes de interação com o usuário:

- `st.button()`
- `st.text_input()`
- `st.number_input()`
- `st.selectbox()`
- `st.checkbox()`

Exemplo:

```python
nome = st.text_input("Digite seu nome")

if nome:
    st.write(f"Olá, {nome}!")
```

---

### 📐 Layout

Demonstra recursos para organização da interface:

- `st.columns()`
- `st.tabs()`
- `st.expander()`
- `st.divider()`

Exemplo:

```python
col1, col2 = st.columns(2)

with col1:
    st.write("Coluna 1")

with col2:
    st.write("Coluna 2")
```

---

### 📊 Dados e gráficos

Integração com **Pandas** e recursos de visualização do Streamlit.

São apresentados:

- `st.dataframe()`
- `st.metric()`
- `st.line_chart()`
- `st.bar_chart()`
- `st.area_chart()`

Exemplo:

```python
import pandas as pd

df = pd.DataFrame({
    "Produto": ["A", "B", "C"],
    "Vendas": [100, 200, 150]
})

st.dataframe(df)
```

---

### 💬 Mensagens

Exemplos de mensagens para comunicação com o usuário:

- `st.success()`
- `st.info()`
- `st.warning()`
- `st.error()`

Exemplo:

```python
st.success("Operação concluída!")
st.info("Esta é uma informação.")
st.warning("Atenção!")
st.error("Ocorreu um erro!")
```

---

### 📁 Arquivos

Demonstração de upload de arquivos utilizando:

```python
st.file_uploader()
```

O exemplo permite trabalhar com arquivos como:

- CSV
- XLSX
- PDF

Exemplo:

```python
arquivo = st.file_uploader(
    "Escolha um arquivo",
    type=["csv", "xlsx", "pdf"]
)

if arquivo:
    st.success(f"Arquivo recebido: {arquivo.name}")
```

---

### 🧩 Componentes

Apresentação de outros componentes úteis:

- `st.divider()`
- `st.image()`
- `st.progress()`
- `st.spinner()`

---

### ⚙️ Configuração

Exemplo de configuração da aplicação através de:

```python
st.set_page_config(
    page_title="Meu aplicativo",
    page_icon="🚀",
    layout="wide"
)
```

Também é apresentado o uso da barra lateral:

```python
with st.sidebar:
    st.title("Menu")
```

---

### 🚀 Exemplo completo

A última seção apresenta um pequeno **Dashboard de Vendas**, combinando diversos recursos apresentados durante o guia.

O dashboard utiliza:

- Métricas
- DataFrame
- Gráfico de barras
- Layout com colunas
- Títulos e subtítulos

---

## 🛠️ Tecnologias utilizadas

O projeto utiliza:

| Tecnologia | Utilização |
|---|---|
| 🐍 Python | Linguagem principal |
| 🎈 Streamlit | Desenvolvimento da interface web |
| 🐼 Pandas | Manipulação de dados |
| 📝 Markdown | Documentação e formatação |

---

## 📋 Pré-requisitos

Antes de executar o projeto, é necessário ter o **Python** instalado.

Recomenda-se utilizar um ambiente virtual para manter as dependências do projeto isoladas.

Verifique a instalação do Python:

```bash
python --version
```

Ou:

```bash
python3 --version
```

---

## 📦 Instalação

### 1. Clone o projeto

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Entre na pasta:

```bash
cd nome-do-projeto
```

---

### 2. Crie um ambiente virtual

No Windows:

```bash
python -m venv .venv
```

Ative o ambiente:

```bash
.venv\Scripts\activate
```

No Linux/macOS:

```bash
python3 -m venv .venv
```

Ative:

```bash
source .venv/bin/activate
```

---

### 3. Instale as dependências

Instale o Streamlit e o Pandas:

```bash
pip install streamlit pandas
```

Ou, caso o projeto possua um arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando o projeto

É importante executar uma aplicação Streamlit utilizando o comando `streamlit run`.

Execute:

```bash
streamlit run pagina.py
```

Ou:

```bash
python -m streamlit run pagina.py
```

Depois da inicialização, o Streamlit disponibilizará a aplicação localmente, normalmente em:

```text
http://localhost:8501
```

---

## ⚠️ Importante

Não execute a aplicação utilizando:

```bash
python pagina.py
```

Aplicações Streamlit devem ser iniciadas através de:

```bash
streamlit run pagina.py
```

ou:

```bash
python -m streamlit run pagina.py
```

Executar diretamente com `python` pode gerar mensagens como:

```text
missing ScriptRunContext
```

e:

```text
Session state does not function when running a script without `streamlit run`
```

Essas mensagens acontecem porque a aplicação não foi iniciada através do mecanismo de execução do Streamlit.

---

## ⚠️ Cuidado com o nome dos arquivos

Evite criar um arquivo chamado:

```text
streamlit.py
```

Isso pode causar conflito com a biblioteca oficial:

```python
import streamlit as st
```

Por exemplo, prefira:

```text
pagina.py
guia_streamlit.py
app.py
```

em vez de:

```text
streamlit.py
```

---

## 📁 Estrutura sugerida

Uma estrutura simples para o projeto:

```text
learning-streamlit/
│
├── pagina.py
├── README.md
├── requirements.txt
├── .gitignore
└── .venv/
```

O diretório `.venv/` normalmente não deve ser enviado para o Git.

---

## 📄 requirements.txt

Para registrar as principais dependências do projeto, crie um arquivo chamado:

```text
requirements.txt
```

Com:

```text
streamlit
pandas
```

Depois, qualquer pessoa poderá instalar as dependências utilizando:

```bash
pip install -r requirements.txt
```

---

## 🎯 Objetivos de aprendizado

Este projeto tem como objetivos praticar:

- Fundamentos do Streamlit
- Criação de interfaces web utilizando Python
- Componentes interativos
- Layout de aplicações
- Entrada de dados
- Manipulação de DataFrames
- Criação de gráficos
- Upload de arquivos
- Dashboards
- Organização de aplicações Streamlit

---

## 🔮 Possíveis melhorias futuras

Algumas funcionalidades que podem ser adicionadas futuramente:

- 🔎 Pesquisa de comandos
- 📋 Botão para copiar exemplos de código
- 📚 Mais comandos do Streamlit
- 🎨 Temas personalizados
- 🌙 Modo claro/escuro
- 📊 Mais exemplos de gráficos
- 🤖 Exemplos de integração com Inteligência Artificial
- 🗂️ Separação da aplicação em múltiplas páginas
- 📱 Melhor adaptação para dispositivos móveis
- 🧪 Área para testar pequenos códigos
- 📖 Links para a documentação oficial

---

## 📖 Conceito principal

A estrutura básica de uma aplicação Streamlit pode ser resumida em:

```python
import streamlit as st

st.set_page_config(
    page_title="Minha aplicação",
    page_icon="🐍"
)

st.title("Minha aplicação")

st.write("Olá, mundo!")
```

A partir dessa estrutura, novos componentes podem ser adicionados para criar aplicações cada vez mais completas.

---

## 📌 Comandos apresentados

Resumo dos principais comandos utilizados no projeto:

```text
st.set_page_config()
st.title()
st.header()
st.subheader()
st.write()
st.markdown()
st.code()
st.caption()

st.button()
st.text_input()
st.number_input()
st.selectbox()
st.checkbox()

st.columns()
st.tabs()
st.expander()
st.divider()
st.sidebar

st.dataframe()
st.metric()
st.line_chart()
st.bar_chart()
st.area_chart()

st.success()
st.info()
st.warning()
st.error()

st.file_uploader()
st.image()
st.progress()
st.spinner()
```

---

## 👨‍💻 Sobre o projeto

Este projeto faz parte do processo de aprendizado em **Python, Streamlit e desenvolvimento de aplicações interativas**.

A aplicação foi construída com foco educacional, permitindo experimentar os principais recursos do Streamlit em uma única interface.

---

## 📜 Licença

Este projeto pode ser utilizado para fins de estudo, aprendizado e experimentação.

---

**🐍 Learning Streamlit — Raphael Campos Squilaro**
