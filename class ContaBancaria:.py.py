class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = []  # Lista para armazenar os extratos
        self.saques_realizados = 0  # Contador de saques diários

    def depositar(self, valor):
        if valor > 0:  # Verificação para garantir que o valor é positivo
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito. O valor deve ser positivo.")

    def sacar(self, valor):
        # Verifica se o saque está dentro das regras
        if valor > 0 and valor <= 500:
            if self.saques_realizados < 3:
                if valor <= self.saldo:
                    self.saldo -= valor
                    self.extrato.append(f"Saque: R$ {valor:.2f}")
                    self.saques_realizados += 1
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                else:
                    print("Saldo insuficiente!")
            else:
                print("Você atingiu o limite de 3 saques diários!")
        else:
            print("Valor inválido para saque ou excede o limite de R$500,00 por saque.")

    def visualizar_extrato(self):
        print("\nExtrato bancário:")
        if not self.extrato:
            print("Nenhuma transação realizada.")
        else:
            for transacao in self.extrato:
                print(transacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print(f"Saques realizados hoje: {self.saques_realizados}/3\n")


# Função principal para interagir com o usuário
def sistema_bancario():
    print("Bem-vindo ao sistema bancário!")
    nome_cliente = input("Digite o seu nome: ")
    conta = ContaBancaria(nome_cliente)

    while True:
        print("\nEscolha uma opção:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Visualizar Extrato")
        print("4 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            try:
                valor = float(input("Digite o valor do depósito: R$ "))
                conta.depositar(valor)
            except ValueError:
                print("Valor inválido. Tente novamente.")
        
        elif opcao == '2':
            try:
                valor = float(input("Digite o valor do saque: R$ "))
                conta.sacar(valor)
            except ValueError:
                print("Valor inválido. Tente novamente.")
        
        elif opcao == '3':
            conta.visualizar_extrato()
        
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Executar o sistema bancário
if __name__ == "__main__":
    sistema_bancario()
