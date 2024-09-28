# Lista de alunos
alunos = []
pendente="Pendente"
hora_aula=60

# Função para exibir todos os alunos
def relatorio_alunos():
        cont = 0
        print("Para aprovação, a média das 4 notas é 7, a frequência deve ser igual ou maior que 75% das 60h aulas obrigatórias da disciplina")
        for aluno in alunos:
            cont+=1
            print(f"{cont}. Nome: {aluno['nome']}, Média: {aluno['media']}, Assistiu: {aluno['aula_frequentada']} aulas, Frequência: {aluno['frequencia']} %, Status: {aluno['status']}")

def adicionar_aluno():
# Verifica se o aluno já está cadastrado:
    nome = input("Digite o nome do aluno: ")

    for aluno in alunos:
        if aluno["nome"] == nome:
            print("Aluno já está cadastrado!")
            return

    alunos.append({'nome': nome, 'aula_frequentada':pendente, 'frequencia':pendente, 'media':pendente, 'status':pendente})
    print(f"Aluno {nome} foi adicionado com sucesso!")
    return

def status_aluno():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    else:
        for aluno in alunos:
            if aluno['frequencia']==pendente:
                status="Pendente"
                aluno['status'] = status
                return
            elif aluno['media']==pendente:
                status = "Pendente"
                aluno['status'] = status
                return
            elif aluno['frequencia']>=75:
                if aluno['media']>=7:
                    status = "Aprovado"
                    aluno['status']=status
                    return
                else:
                    status= "Reprovado por Nota"
                    aluno['status'] = status
                    return
            elif aluno['frequencia']<75:
                status = "Reprovado por Falta"
                aluno['status'] = status
                return
    print("Aluno não encontrado!")

def relatorio_especifico_aluno():
    if not alunos:
        pass
    else:
        perg=-1
        while perg !=0:
            perg = int(input("\nFiltrar os Alunos por:\n"
                             "1. Aprovados\n"
                             "2. Reprovados por Falta\n"
                             "3. Reprovado por Nota\n"
                             "4. Pendente de Dados\n"
                             "0. Sair...\n"
                             "Digite uma opção: \n"))
            if perg ==1:
                cont = 0
                qt_alunos = 0
                for aluno in alunos:
                    qt_alunos += 1
                    if aluno['status']=="Aprovado":
                        cont+=1
                        print(f"{cont}. Nome: {aluno['nome']}, foi {aluno['status']}")
                    elif aluno['status'] != "Aprovado" and qt_alunos > 0:
                        print("\nNão há Alunos Aprovados")
            elif perg==2:
                cont = 0
                qt_alunos = 0
                for aluno in alunos:
                    qt_alunos += 1
                    if aluno['status'] == "Reprovado por Falta":
                        cont += 1
                        print(f"{cont}. Nome: {aluno['nome']}, foi {aluno['status']}")
                    elif aluno['status'] != "Reprovado por Falta" and qt_alunos > 0:
                        print("\nNão há Alunos Reprovados por Falta")
            elif perg==3:
                cont = 0
                qt_alunos = 0
                for aluno in alunos:
                    qt_alunos += 1
                    if aluno['status'] == "Reprovado por Nota":
                        cont += 1
                        print(f"{cont}. Nome: {aluno['nome']}, foi {aluno['status']}")
                    elif aluno['status'] != "Reprovado por Nota" and qt_alunos > 0:
                        print("\nNão há Alunos Reprovados por Nota")
            elif perg==4:
                cont= 0
                qt_alunos= 0
                print("\nRelação de Pendência de Dados:")
                for aluno in alunos:
                    qt_alunos+=1
                    if aluno['status']=="Pendente":
                        cont += 1
                        print(f"{cont}. Nome: {aluno['nome']}, está {aluno['status']} de Dados ")
                    elif aluno['status']!="Pendente" and qt_alunos>0:
                        print("\nNão há Alunos Pendente de Dados")
            else:
                print("Saindo do sistema de Relatorio Especifico Aluno\n")
                break
# Adocionar Frequência dos alunos:
def adicionar_frequencia():
    # Verificar se o aluno já está cadastrado
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    else:
        nome = input("Digite o nome do aluno para ADD FREQUÊNCIA: ")
        for aluno in alunos:
            if aluno["nome"] == nome:
                aula_frequentada = int(input("Digite a frequência do aluno (0h a 60h: "))
                if aula_frequentada >60 or aula_frequentada<0:
                    while aula_frequentada >60 or aula_frequentada<0:
                        aula_frequentada = int(input("Digite a frequência do aluno (0h a 60h: "))
                aluno['aula_frequentada']= aula_frequentada
                frequencia=((aula_frequentada*100)/hora_aula)
                frequencia = round(frequencia, 2)
                aluno["frequencia"] = frequencia
                print("Frequencia adicionada!")
                return
        print("Aluno não encontrado!")
# Adicionar notas dos alunos
def adicionar_notas():
    # Verificar se o aluno já está cadastrado
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    else:
        nome = input("Digite o nome do aluno para ADD NOTAS: ")
        for aluno in alunos:
            if aluno["nome"] == nome:
                soma= 0
                cont= 0
                for numero in range(1, 5, 1):
                    cont += 1
                    notas = float(input(f"Digite a {cont}ª nota do aluno: "))
                    while notas > 10 or notas < 0:
                        notas = float(input(f"Digite a {cont}ª nota do aluno (0 a 10): "))
                    soma = soma + notas
                media = soma / 4
                aluno["media"] = media
                print("Alteração realizada\n")
                return
        print("Aluno não encontrado!")
# Função para editar os dados de um aluno
def editar_aluno():
    # Verificar se o aluno já está cadastrado
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    else:
        nome = input("Digite o nome do aluno que deseja EDITAR: ")
        for aluno in alunos:
            if aluno["nome"] == nome:
                perg=-1

                # Menu de opções
                while perg!=0:
                    print("Opções:\n"
                          "0: Finalizar Edição\n"
                          "1: Alterar Nome\n"
                          "2: Alterar Notas\n"
                          "3: Alterar Frequência\n")
                    perg=int(input("Digite alguma das opções: "))
                # Editar Nome do Aluno
                    if perg == 1:
                        aluno["nome"] = input("Digite a novo nome: ")
                        print("Alteração realizada")
                # Editar Notas para EDITAR a Média do Aluno
                    elif perg== 2:
                        if aluno["nome"] == nome:
                            soma = 0
                            cont = 0
                            for numero in range(1, 5, 1):
                                cont += 1
                                notas = float(input(f"Digite a {cont}ª nota do aluno: "))
                                while notas > 10 or notas < 0:
                                    notas = float(input(f"Digite a {cont}ª nota do aluno (0 a 10): "))
                                soma = soma + notas
                            media = soma / 4
                            aluno["media"] = media
                            print("Alteração realizada\n")
                # Editar Frequencia do aluno:
                    elif perg== 3:
                        aula_frequentada = int(input("Digite a frequência do aluno (0h a 60h: "))
                        if aula_frequentada > 60 or aula_frequentada < 0:
                            while aula_frequentada > 60 or aula_frequentada < 0:
                                aula_frequentada = int(input("Digite a frequência do aluno (0h a 60h: "))
                        aluno['aula_frequentada'] = aula_frequentada
                        frequencia = ((aula_frequentada * 100) / hora_aula)
                        frequencia = round(frequencia, 2)
                        aluno["frequencia"] = frequencia
                        print("Frequencia adicionada!")
                    elif perg== 0:
                        print("Edição finalizada!")
                        return
        print("Aluno não encontrado!")

# Função para Remover um Aluno
def remover_aluno():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    else:
        nome = input("Digite o nome do aluno que deseja remover: ")
        for aluno in alunos:
            if aluno["nome"] == nome:
                alunos.remove(aluno)
                print(f"Aluno {nome} foi removido com sucesso!")
                return
    print("Aluno não encontrado!")

# Menu para gerenciar o sistema
def menu():
    opcao=-1
    print("Sistema Acadêmico Iniciado!")
    while opcao != 0:
        print("\n1. Adicionar Alunos")
        print("2. Editar Aluno")
        print("3. Remover aluno")
        print("4. Adicionar Notas")
        print("5. Adicionar Frequência")
        print("6. Relatorio alunos")
        print("7. Relatório Específica")
        print("0. Sair")

        opcao = int(input("Digite uma opção: "))
        print()
        if opcao == 1:
            adicionar_aluno()
        elif opcao == 2:
            editar_aluno()
        elif opcao == 3:
            remover_aluno()
        elif opcao == 4:
            adicionar_notas()
        elif opcao == 5:
            adicionar_frequencia()
        elif opcao == 6:
            status_aluno()
            relatorio_alunos()
        elif opcao == 7:
            status_aluno()
            relatorio_especifico_aluno()
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")
# Executar o menu
menu()