produtos = []
comando = ''

while True:
    print(" FORMULÁRIO DE CADASTRO ".center(40, '='))
    produto = {
        'nome': input("Nome: "),
        'preco': float(input("Preço: ")),
        'descricao': input("Descrição: "),
        'disponibilidade': input("Disponibilidade (S/N): ")
    }
    produto['disponibilidade'] = produto['disponibilidade'].upper()

    if produto['disponibilidade'] not in ['S', 'N']:
        print("Disponibilidade inválida. Insira S ou N.")
        continue
    if produto['preco'] < 0:
        print("Preço inválido. Insira um valor maior ou igual a zero.")
        continue

    produtos.append(produto)

    comando = input("Produto cadastrado com sucesso!\n"
                    "Deseja cadastrar outro produto? (S/N): ").upper()
    
    if comando == 'N':
        break
    elif comando == 'S':
        continue
    else:
        comando = input("Comando inválido. Insira S ou N: ").upper()

produtos_ordem_preco = sorted(produtos, key=lambda produto: produto['preco'])

print(" LISTAGEM ".center(30, '='))
print("NOME".ljust(20) + "PREÇO".ljust(10))
print('-'*30)
for produto in produtos_ordem_preco:
    print(f"{produto['nome']}".ljust(20) + f"R$ {produto['preco']:.2f}".ljust(10))
    print(
        "Descrição:\n"
        f"{produto['descricao']}"
        )
    print('-'*30)