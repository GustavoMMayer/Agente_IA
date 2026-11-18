# 🔧 Agente de IA - Oficina Mecânica AutoTech

Assistente virtual simples desenvolvido em Python para realizar o primeiro atendimento de **clientes** e **fornecedores** da Oficina Mecânica AutoTech diretamente pelo terminal, utilizando inteligência artificial local com o **Ollama**.

## 🎯 Funcionalidades

* **Atendimento Direcionado:** Identifica automaticamente se o usuário é um cliente (buscando serviços ou orçamentos) ou um fornecedor (oferecendo peças e insumos).
* **Memória de Contexto:** Mantém o histórico da conversa ativa na sessão atual, permitindo diálogos contínuos sem perder informações já mencionadas (como modelo e ano do veículo).
* **Execução 100% Local:** Roda diretamente na máquina do usuário sem depender de APIs pagas ou envio de dados para a nuvem.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Ollama** (execução local de modelos LLM)
* **Modelo de IA:** `llama3.2`
* **Biblioteca Python:** `ollama`

## 📋 Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado em sua máquina:

1. [Python 3](https://python.org) instalado.
2. [Ollama](https://ollama.com) instalado e em execução.
3. O modelo `llama3.2` baixado localmente. Para baixar, execute no terminal:
   ```bash
   ollama pull llama3.2
   ```

## 🚀 Como Instalar e Executar

1. **Clone ou baixe este repositório** para o seu computador.

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Instale a biblioteca do Ollama:**
   ```bash
   python -m pip install ollama
   ```

4. **Execute o agente no terminal:**
   ```bash
   python Agente_IA.py
   ```

5. **Interaja com o assistente:** Digite sua mensagem no terminal e pressione `Enter`. Para finalizar o programa, digite `SAIR`.

## 📁 Estrutura do Projeto

```text
Agente_IA/
│
├── Agente_IA.py    # Código principal do agente com regras de negócio e memória
└── README.md       # Documentação do projeto
```

## 🔮 Próximos Passos (Evoluções Futuras)

* [ ] Criação de interface gráfica web utilizando Streamlit.
* [ ] Registro automático de atendimentos e contatos de fornecedores em arquivo CSV/planilha.
* [ ] Integração com catálogo básico de peças e tabela de serviços.

