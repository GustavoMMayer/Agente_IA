import ollama

# 1. Instrução detalhada com a identidade, regras e dados da oficina
instrucao = """
Você é o assistente virtual da 'Oficina Mecânica AutoTech'.
Seu objetivo é atender dois públicos de forma educada, direta e objetiva:

1. CLIENTES:
- Serviços oferecidos: Troca de óleo, revisão geral, freios, suspensão, alinhamento, balanceamento e diagnóstico eletrônico.
- Horário de funcionamento: Segunda a Sexta, das 08h às 18h. Sábados das 08h às 12h.
- Endereço: Rua das Engrenagens, 123 - Centro.
- Como agir: Pergunte sempre o modelo, ano do veículo e qual problema está acontecendo. Nunca invente preços exatos; informe que um mecânico fará o orçamento presencialmente ou após avaliação.

2. FORNECEDORES (Autopeças e insumos):
- Como agir: Peça o nome da empresa, o CNPJ e qual peça ou catálogo estão oferecendo. Informe que o setor de compras analisa propostas de segunda a quinta, das 14h às 17h, pelo e-mail compras@autotech.com.

Regra geral: Identifique logo no início se você está falando com um cliente ou um fornecedor, caso a pessoa não deixe claro. Seja simpático e use respostas curtas.
"""

# 2. Lista para guardar o histórico da conversa (Memória do Agente)
historico_mensagens = [
    {"role": "system", "content": instrucao}
]

print("=== Atendimento Oficina AutoTech Iniciado ===")
print("Digite SAIR a qualquer momento para encerrar.\n")

while True:
    pergunta = input("Você: ")
    
    if pergunta.lower() == "sair":
        print("Encerrando o atendimento. Até logo!")
        break
        
    # Evita enviar mensagens vazias se você apertar Enter sem querer
    if not pergunta.strip():
        continue

    # Adiciona a fala do usuário na memória
    historico_mensagens.append({"role": "user", "content": pergunta})

    print("Agente digitando...")

    # Envia TODO o histórico para o Ollama, permitindo que ele lembre do contexto
    resposta = ollama.chat(model="llama3.2", messages=historico_mensagens)
    
    texto_resposta = resposta['message']['content']
    
    # Guarda a resposta do agente na memória para as próximas perguntas
    historico_mensagens.append({"role": "assistant", "content": texto_resposta})

    print(f"\nAgente: {texto_resposta}\n")
    print("-" * 50)
