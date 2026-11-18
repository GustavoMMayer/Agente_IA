import ollama

instrucao = "Você é um agente de IA especifico para atender a nossos clientes e fornecedores da nossa oficina mecanica."

print("Agente Pronto!! Digite SAIR para encerrarmos a aplicacao")

while True:
    pergunta = input("\nVoce: ")
    if pergunta.lower() == "sair":
        print("Encerrando a aplicacao...")
        break

    resposta = ollama.chat(model="llama3.2", messages=[
        {"role": "system", "content": instrucao},
        {"role": "user", "content": pergunta}
        ])

    print("Agente: ", resposta['message']['content'])