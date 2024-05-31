from datetime import datetime

# Classe Quarto (Wesley)
class Quarto:
    def init(self, numero, tipo, capacidade, preco, disponibilidade=True):
        self.numero = numero
        self.tipo = tipo
        self.capacidade = capacidade
        self.preco = preco
        self.disponibilidade = disponibilidade
        self.reservas = []

    def reservar(self, check_in, check_out, ocupantes):
        if self.disponibilidade and ocupantes <= self.capacidade:
            self.reservas.append({"check_in": check_in, "check_out": check_out, "ocupantes": ocupantes})
            self.disponibilidade = False
            return True
        return False

    def liberar(self):
        self.disponibilidade = True
        self.reservas.clear()

    def verificar_disponibilidade(self, data_inicio, data_fim):
        for reserva in self.reservas:
            if not (reserva["check_out"] < data_inicio or reserva["check_in"] > data_fim):
                return False
        return True

# Classe Auditorio (Rian)
class Auditorio:
    def init(self, capacidade, preco_por_hora, disponibilidade=True):
        self.capacidade = capacidade
        self.preco_por_hora = preco_por_hora
        self.disponibilidade = disponibilidade
        self.reservas = []

    def reservar(self, data, hora_inicio, hora_fim, participantes):
        if self.disponibilidade and participantes <= self.capacidade:
            self.reservas.append({"data": data, "hora_inicio": hora_inicio, "hora_fim": hora_fim, "participantes": participantes})
            self.disponibilidade = False
            return True
        return False

    def liberar(self):
        self.disponibilidade = True
        self.reservas.clear()

    def verificar_disponibilidade(self, data, hora_inicio, hora_fim):
        for reserva in self.reservas:
            if reserva["data"] == data and not (reserva["hora_fim"] <= hora_inicio or reserva["hora_inicio"] >= hora_fim):
                return False
        return True

# Classe Refeicao (Alex)
class Refeicao:
    def __init__(self, nome, descricao, preco, horario_disponibilidade):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.horario_disponibilidade = horario_disponibilidade
        self.agendamentos = []

    def agendar(self, data, horario):
        self.agendamentos.append({"data": data, "horario": horario})


# Funções para gerar relatórios (Paulo)
def gerar_relatorio_ocupacao(quartos):
    relatorio = []
    for quarto in quartos:
        relatorio.append({"numero": quarto.numero, "reservas": len(quarto.reservas)})
    return relatorio

def gerar_relatorio_faturamento(quartos, auditorio):
    faturamento = 0
    for quarto in quartos:
        faturamento += quarto.preco * len(quarto.reservas)
    faturamento += auditorio.preco_por_hora * len(auditorio.reservas)
    return faturamento

# Função para controle de acesso (simplificado) (Vinicius)
def controle_de_acesso(usuario, permissao):
    permissoes = {
        "administrador": ["cadastrar", "reservar", "remover", "relatorios"],
        "funcionario": ["reservar", "remover"],
        "hospede": ["reservar"]
    }
    return permissao in permissoes.get(usuario, [])

# Menu interativo (Victor Fernando)
def menu():
    quartos = []
    auditorio = None

    while True:
        print("\n--- Sistema de Gestão de Hostel ---")
        print("1. Cadastrar quarto")
        print("2. Reservar quarto")
        print("3. Verificar disponibilidade de quarto")
        print("4. Remover quarto")
        print("5. Listar todos os quartos")
        print("6. Cadastrar auditório")
        print("7. Reservar auditório")
        print("8. Verificar disponibilidade de auditório")
        print("9. Cadastrar refeição")
        print("10. Agendar refeição")
        print("11. Gerar relatório de ocupação")
        print("12. Gerar relatorio de faturamento")
        print("13. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero = int(input("Número do quarto: "))
            tipo = input("Tipo (solteiro, casal, compartilhado): ")
            capacidade = int(input("Capacidade: "))
            preco = float(input("Preço por noite: "))
            disponibilidade = input("Disponibilidade (sim/não): ").lower() == "sim"
            quartos.append((numero, tipo, capacidade, preco, disponibilidade))
            print("Quarto cadastrado com sucesso!")

        elif opcao == "2":
            numero = int(input("Número do quarto a reservar: "))
            check_in = input("Data de check-in (AAAA-MM-DD): ")
            check_out = input("Data de check-out (AAAA-MM-DD): ")
            ocupantes = int(input("Número de ocupantes: "))
            quarto = next((q for q in quartos if q.numero == numero), None)
            if quarto and quarto.reservar(check_in, check_out, ocupantes):
                print("Quarto reservado com sucesso!")
            else:
                print("Não foi possível reservar o quarto.")

        elif opcao == "3":
            numero = int(input("Número do quarto a verificar: "))
            data_inicio = input("Data de início (AAAA-MM-DD): ")
            data_fim = input("Data de fim (AAAA-MM-DD): ")
            quarto = next((q for q in quartos if q.numero == numero), None)
            if quarto and quarto.verificar_disponibilidade(data_inicio, data_fim):
                print("Quarto disponível no período.")
            else:
                print("Quarto não disponível no período.")

        elif opcao == "4":
            numero = int(input("Número do quarto a remover: "))
            quartos = [q for q in quartos if q.numero != numero]
            print("Quarto removido com sucesso!")

        elif opcao == "5":
            print("Listagem de todos os quartos:")
            for quarto in quartos:
                print(vars(quarto))

        elif opcao == "6":
            capacidade = int(input("Capacidade do auditório: "))
            preco_por_hora = float(input("Preço por hora: "))
            disponibilidade = input("Disponibilidade (sim/não): ").lower() == "sim"
            auditorio = (capacidade, preco_por_hora, disponibilidade)
            print("Auditório cadastrado com sucesso!")

        elif opcao == "7":
            if auditorio:
                data = input("Data da reserva (AAAA-MM-DD): ")
                hora_inicio = input("Hora de início (HH:MM): ")
                hora_fim = input("Hora de fim (HH:MM): ")
                participantes = int(input("Número de participantes: "))
                if auditorio.reservar(data, hora_inicio, hora_fim, participantes):
                    print("Auditório reservado com sucesso!")
                else:
                    print("Não foi possível reservar o auditório.")
            else:
                print("Nenhum auditório cadastrado.")

        elif opcao == "8":
            if auditorio:
                data = input("Data da reserva (AAAA-MM-DD): ")
                hora_inicio = input("Hora de início (HH:MM): ")
                hora_fim = input("Hora de fim (HH:MM): ")
                if auditorio.verificar_disponibilidade(data, hora_inicio, hora_fim):
                    print("Auditório disponível no período.")
                else:
                    print("Auditório não disponível no período.")
            else:
                print("Nenhum auditório cadastrado.")

        elif opcao == "9":
            nome = input("Nome da refeição: ")
            descricao = input("Descrição: ")
            preco = float(input("Preço: "))
            horario_disponibilidade = input("Horário de disponibilidade: ")
            refeicao = Refeicao(nome, descricao, preco, horario_disponibilidade)
            print("Refeição cadastrada com sucesso!")

        elif opcao == "10":
            nome = input("Nome da refeição a agendar: ")
            data = input("Data (AAAA-MM-DD): ")
            horario = input("Horário (HH:MM): ")
            refeicao.agendar(data, horario)
            print("Refeição agendada com sucesso!")

        elif opcao == "11":
            relatorio = gerar_relatorio_ocupacao(quartos)
            print("Relatório de Ocupação:")
            for item in relatorio:
                print(item)

        elif opcao == "12":
            faturamento = gerar_relatorio_faturamento(quartos, auditorio)
            print(f"Faturamento total: R${faturamento}")

        elif opcao == "13":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Início do programa
menu()