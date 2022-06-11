from materias import *


class Aluno:
    def __init__(self, id: int, nome: str, fluxo: int, coeficiente: float, materias_atuais: list, materias_pagas: list,
                 pendencias: list, etapa: int):
        self.id = id
        self.nome = nome  # Geralt of Rivia, James Howlett...
        self.fluxo = fluxo  # padrão (4), calouro (3), formando (2), individual (1)
        self.coeficiente = coeficiente  # 8.5
        self.materias_atuais = materias_atuais  # ["COMP359","COMP360","COMP361","COMP362","COMP363"]
        self.materias_pagas = materias_pagas  # ["COMP359","COMP360","COMP361","COMP362","COMP363"]
        self.pendencias = pendencias
        self.etapa = etapa


class Pedido:
    def __init__(self, aluno: Aluno, insercao: str = None, remocao: str = None):
        self.aluno = aluno
        self.insercao = insercao
        self.remocao = remocao


ajuste_lista = []
matriculados = [
    Aluno(444, 'João Pedro Vasconcelos', 1, 8.0, ["COMP372", "CC1965", "CC1962"],
          ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363", "COMP364", "COMP365", "COMP366"], ["COMP367"], 1),
    Aluno(333, 'Ana Clara Lima', 4, 6.0, ["COMP368", "COMP369", "COMP370", "COMP371"],
          ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363", "COMP364", "COMP365", "COMP366", "COMP367"], [], 1),
    Aluno(777, 'Geralt de Rivia', 2, 3.0, ["TCC1", "TCC2", "TCC3", "COMP407", "COMP409", "COMP410"],
          ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363", "COMP364", "COMP365", "COMP366", "COMP367", "COMP368",
           "COMP369", "COMP370", "COMP371", "COMP372", "COMP373", "COMP374", "COMP376", "COMP378", "COMP379", "COMP380",
           "COMP381", "COMP382", "COMP386", "COMP387", "COMP389", "COMP390", "COMP391", "COMP392", "COMP393", "COMP394",
           "COMP395", "COMP396", "COMP397", "COMP398", "COMP399", "COMP400", "COMP401"], [], 1)
]
id = 0
cadastrados = [
    Aluno(111, 'José Henrique da Silva', 1, 6.0, [],
          ["COMP359", "COMP365", "COMP360", "COMP361", "COMP362", "COMP363", "COMP365", "COMP366", "COMP367"],
          ["COMP364"], 0),
    Aluno(222, 'Maria Carla de Andrade', 4, 7.5, [],
          ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363", "COMP365", "COMP366", "COMP364", "COMP367"], [], 0),
    Aluno(555, 'Bruce Wayne Batman', 4, 10.0, [],
          ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363", "COMP365", "COMP366", "COMP364", "COMP367"], [], 0),
    Aluno(666, 'Lucifer Morningstar', 2, 9.0, [],
          ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363", "COMP364", "COMP365", "COMP366", "COMP367", "COMP368",
           "COMP369", "COMP370", "COMP371", "COMP372", "COMP373", "COMP374", "COMP376", "COMP378", "COMP379", "COMP380",
           "COMP381", "COMP382", "COMP386", "COMP387", "COMP389", "COMP390", "COMP391", "COMP392", "COMP393", "COMP394",
           "COMP395", "COMP396", "COMP397", "COMP398", "COMP399", "COMP400", "COMP401"], [], 0),
    Aluno(888, 'José Henrique da Silva', 4, 6.0, [],
          ["COMP359", "COMP365", "COMP360", "COMP361", "COMP362", "COMP363", "COMP365", "COMP366", "COMP367"],
          ["COMP364"], 0),
]


def matricula():
    print("Processo de matrícula iniciado.")
    w = 0
    while w < 10:
        if w == 4: print("Limite de entradas inválidas atingido. Processo de matrícula encerrado."); return

        q = input("É calouro? (s = sim / n = não): ").lower()
        if q == 's':
            nome = input("Insira o seu nome: ").strip()
            nome = nome[0].upper() + nome[1:]

            if len(nome) == 0 or nome.isspace() or not all(i.isalpha() or i.isspace() for i in nome):
                print("Entrada inválida.")
                w += 1
            else:
                global id
                id += 1
                calouro = Aluno(id, nome, 3, 10.0, ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363"], [], [], 0)

                for i in range(len(calouro.materias_atuais)):
                    if calouro.materias_atuais[i] in grade_CC:
                        if (grade_CC[calouro.materias_atuais[i]].ocupado == grade_CC[
                            calouro.materias_atuais[i]].limite):
                            print("A matéria inserida está cheia.")
                            return
                        else:
                            grade_CC[calouro.materias_atuais[i]].ocupado += 1
                matriculados.append(calouro)
                print("Matrícula efetuada.")
                return
        elif q == 'n':
            if cadastrados == []:
                print("Não há matriculas para realizar.")
                return
            try:
                num = int(input("Insira o número da sua matrícula: "))
            except ValueError:
                print("entrada invalida")
                return
            check = 0
            for i in range(len(cadastrados)):
                if cadastrados[i].id == num:
                    aluno = cadastrados[i]
                    check = 1
                    break
            if check == 0:
                if matriculados != []:
                    for j in range(len(matriculados)):
                        if matriculados[j].id == num:
                            print("\n\nVocê já está matriculado!")
                            if matriculados[j].fluxo == 3:
                                print("Você é calouro e foi leviano para com o sistema.\n\n")
                            return
                print("\n\nO aluno não consta no sistema.\n\n")
            else:
                for j in cadastrados:
                    if (aluno.fluxo < j.fluxo):
                        print("\nAguarde os alunos de prioridade maior fazerem a matrícula.")
                        return

                if aluno.fluxo == 2:
                    print("Você é formando.")
                    aluno.materias_atuais = ["TCC1", "TCC2", "TCC3"]
                    print("As matérias de TCC foram adicionadas.")

                x = 0
                y = 0
                count = 0
                for materia in grade_CC:
                    if (materia in aluno.materias_pagas) or (materia in aluno.materias_atuais):
                        continue
                    else:
                        print("\033[1m" + materia + "\033[0m" + ":", grade_CC[materia].nome, end=" || ")
                        count += 1
                        if count % 4 == 0:
                            print("")
                while True:
                    if x == 4 or y == 4: print(
                        "Limite de entradas inválidas atingido. Processo de matrícula encerrado."); break
                    if len(aluno.materias_atuais) == 10:
                        aluno.etapa += 1
                        matriculados.append(aluno)
                        cadastrados.remove(aluno)
                        print("Limite de materias atingido.")
                        print("Matrícula efetuada.")
                        return

                    if len(aluno.materias_atuais) < 3:
                        sel = input("Selecione uma matéria para se matricular: ").upper()
                    else:
                        while True:
                            sel = input(
                                "Selecione uma matéria para se matrícular (para encerrar, insira 'e'): ").upper()
                            if sel == 'E':
                                aluno.etapa += 1
                                matriculados.append(aluno)
                                cadastrados.remove(aluno)
                                print("Matrícula efetuada.")
                                return
                            else:
                                break
                    if sel in grade_TCC:
                        print("essa matéria é exclusiva para alunos Formandos.")
                        y += 1
                    elif sel not in mat_lista:
                        print("A matéria informada não se encontra no sistema.")
                        y += 1
                    else:
                        if sel in aluno.materias_pagas:  # Checa se o aluno já pagou a matéria.
                            print("Você já pagou essa matéria.")
                        elif sel in aluno.materias_atuais:
                            print("Você já está pagando essa materia.")
                        elif sel in grade_CC:
                            conflito = 0
                            for i in range(len(aluno.materias_atuais)):
                                if aluno.materias_atuais[i] in grade_TCC:
                                    continue
                                for j in range(len(grade_CC[aluno.materias_atuais[i]].horario)):
                                    for k in range(len(grade_CC[sel].horario)):
                                        if grade_CC[aluno.materias_atuais[i]].horario[j] == grade_CC[sel].horario[k]:
                                            conflito = 1
                                            print("Horários conflitantes.")
                                            break
                                    if conflito == 1:
                                        break
                                if conflito == 1:
                                    break
                            if conflito == 1:
                                continue
                            print(grade_CC[sel].nome)
                            if grade_CC[sel].ocupado == grade_CC[sel].limite:
                                print("Matéria cheia.")
                                return
                            check = 0
                            if grade_CC[sel].pre_requisitos != []:
                                for i in range(len(grade_CC[sel].pre_requisitos)):
                                    if not grade_CC[sel].pre_requisitos[i] in aluno.materias_pagas:
                                        print(
                                            "Não cumpre os pré-requisitos para ingressar na matéria. Você precisa pagar:")
                                        print(*grade_CC[sel].pre_requisitos, sep=' ')
                                        check = 1
                                        break
                            if check == 1:
                                continue

                            # remover de pendencias
                            if sel in aluno.pendencias:
                                aluno.pendencias.remove(sel)

                            aluno.materias_atuais.append(sel)
                            grade_CC[sel].ocupado += 1
                            print(len(aluno.materias_atuais))
                        else:
                            print("A matéria informada não se encontra no sistema.")
                            x += 1
            return
        else:
            print("Entrada inválida!")
            w += 1


def confirmar_Reajustes(ajuste_lista):
    if ajuste_lista == []:
        print("Não há reajustes para realizar!")
        return ajuste_lista
    # ordernar por coeficiente
    for i in range(len(ajuste_lista) - 1, 0, -1):  # The total number of passes,bubbles: i
        for j in range(i):  # The total number of iterations: j
            if ajuste_lista[j].aluno.coeficiente > ajuste_lista[j + 1].aluno.coeficiente:
                ajuste_lista[j], ajuste_lista[j + 1] = ajuste_lista[j + 1], ajuste_lista[j]  # swap elements
    # printar lista
    for pedido in ajuste_lista:
        # Trocas
        if pedido.insercao != None and pedido.remocao != None:
            print("Reajustando troca")
            if (pedido.remocao in grade_externa):
                grade_externa[pedido.remocao].ocupado -= 1
            else:
                grade_CC[pedido.remocao].ocupado -= 1
            if pedido.remocao in grade_CC and grade_CC[pedido.remocao].tipo == 0:
                pedido.aluno.fluxo = 1
            pedido.aluno.materias_atuais.remove(pedido.remocao)

            if (pedido.insercao in grade_externa):
                if grade_externa[pedido.insercao].ocupado == grade_externa[pedido.insercao].limite:
                    print("matéria cheia! não vai ser possivel fazer a troca!")
                    print("Lamentamos muito parceiro :/ : ", pedido.aluno.nome)
                    continue
                grade_externa[pedido.insercao].ocupado += 1
            else:
                if grade_CC[pedido.insercao].ocupado == grade_CC[pedido.insercao].limite:
                    print("matéria cheia! não vai ser possivel fazer a troca!")
                    print("Lamentamos muito parceiro :/ : ", pedido.aluno.nome)
                    continue
                grade_CC[pedido.insercao].ocupado += 1
            pedido.aluno.materias_atuais.append(pedido.insercao)
        # Remoções
        elif pedido.insercao == None and pedido.remocao != None:
            print("Reajustando Remoção")
            if (pedido.remocao in grade_externa):
                grade_externa[pedido.remocao].ocupado -= 1
            else:
                grade_CC[pedido.remocao].ocupado -= 1

            if pedido.remocao in grade_CC and grade_CC[pedido.remocao].tipo == 0:
                pedido.aluno.fluxo = 1
            pedido.aluno.materias_atuais.remove(pedido.remocao)
        # Inserções
        else:
            print("Reajustando Inserção")
            if (pedido.insercao in grade_externa):
                if grade_externa[pedido.insercao].ocupado == grade_externa[pedido.insercao].limite:
                    print("matéria cheia! não vai ser possivel fazer a troca!")
                    print("Lamentamos muito parceiro :/ : ", pedido.aluno.nome)
                    continue
                grade_externa[pedido.insercao].ocupado += 1
            else:
                if grade_CC[pedido.insercao].ocupado == grade_CC[pedido.insercao].limite:
                    print("matéria cheia! não vai ser possivel fazer a troca!")
                    print("Lamentamos muito parceiro :/ : ", pedido.aluno.nome)
                    continue
                grade_CC[pedido.insercao].ocupado += 1
            pedido.aluno.materias_atuais.append(pedido.insercao)
        print(f"{pedido.aluno.nome}: {pedido.aluno.coeficiente}")
        pedido = '*'
        print("Reajustado!")
    result = filter(lambda val: val != '*', ajuste_lista)
    print("Reajustes efetivados!!")
    return list(result)


def ajuste_reajuste(tipo: int):
    if tipo == 1:
        print("Processo de Reajuste iniciado.")
    else:
        print("Processo de ajuste iniciado.")
    check = 0
    identificacao_ajuste = int(input("Insira o número da sua matrícula: "))
    for i in matriculados:
        if i.id == identificacao_ajuste:
            if i.etapa < 3 and tipo == 1:
                print("\nVocê ainda não pode fazer reajuste")
                return
            elif i.etapa >= 2 and tipo == 0:
                print("\nVocê não pode mais fazer ajustes!")
                return
            elif i.etapa == 4 and tipo == 1:
                print("\nVocê ainda não mais fazer reajuste")
            aluno = i
            check = 1
            print(f"\nBem-vindo(a), {aluno.nome}.")
            break
    if check == 0:
        print("Número de matrícula inválido.")
        return

    while True:
        print("Qual operação você quer realizar?")
        y = input("\n(1): Inserção de matéria."
                  "\n(2): Remoção de matéria."
                  "\n(3): Troca de matéria.\n"
                  "(4): Encerrar processo de requisições.\n"
                  "Selecione uma opção: ")
        if y == '1':
            insercao(aluno, tipo)
        elif y == '2':
            remocao(aluno, tipo)
        elif y == '3':
            troca(aluno, tipo)
        elif y == '4':
            if tipo == 0:
                aluno.etapa = 2
            else:
                aluno.etapa = 4
            return
            # voltar para tela inicial
        else:
            print("Opção inválida.")


def insercao(aluno: Aluno, tipo: int):
    confirm_requirement = True
    # checar se o cara já nao ta no maximo

    if len(aluno.materias_atuais) >= 10:
        print("Você já esta limite máximo de disciplinas cadastradas")
        return

    print("\nDisciplinas de Ciência da Computação:\n")
    for materia in grade_CC:
        if (materia in aluno.materias_pagas) or (materia in aluno.materias_atuais):
            continue
        print("\033[1m" + materia + "\033[0m" + ":", grade_CC[materia].nome, end=" || ")
    if tipo == 1:
        print("\nDisciplinas externas:\n")
        for materia in grade_externa:
            if materia in aluno.materias_atuais:
                continue
            print("\033[1m" + materia + "\033[0m" + ":", grade_externa[materia].nome, end=" || ")
    print("")

    while True:
        escolha = input("Digite o código da matéria (ou 'e' para sair): ").upper()
        print("")
        if escolha in grade_TCC:
            print("Essa matéria não pode ser inserida")
            continue
        if escolha == 'E':
            return
        if tipo == 1:
            if not escolha in mat_lista and not escolha in mat_lista_externa:
                print("Essa matéria não existe.")
                continue
        elif not escolha in mat_lista:
            print("Essa matéria não existe.")
            continue
        if escolha in aluno.materias_atuais:
            if escolha in grade_externa:
                print(f"Você já esta cadastrado em {grade_externa[escolha].nome}.")
                continue
            else:
                print(f"Você já esta cadastrado em {grade_CC[escolha].nome}.")
                continue
        else:
            # Ve se tem pré-requesito
            if tipo == 1 and escolha in grade_externa:
                lista_prereq = grade_externa[escolha].pre_requisitos
                quant_prereq = len(grade_externa[escolha].pre_requisitos)
            else:
                lista_prereq = grade_CC[escolha].pre_requisitos
                quant_prereq = len(grade_CC[escolha].pre_requisitos)

            confirm_requirement = False
            if quant_prereq > 0:
                for pagas in aluno.materias_pagas:
                    if tipo == 1 and escolha in grade_externa:
                        for pre_req in grade_externa[escolha].pre_requisitos:
                            if pre_req == pagas:
                                quant_prereq = quant_prereq - 1
                                lista_prereq.remove(pre_req)
                                if quant_prereq == 0:
                                    confirm_requirement = True
                                    break
                    else:
                        for pre_req in grade_CC[escolha].pre_requisitos:
                            if pre_req == pagas:
                                quant_prereq = quant_prereq - 1
                                lista_prereq.remove(pre_req)
                                if quant_prereq == 0:
                                    confirm_requirement = True
                                    break
                if confirm_requirement == False:
                    print(f"Você não tem o(s) pré-requisito(s) para pagar essa matéria. É necessário pagar: ")
                    print(*lista_prereq, sep=' ')
                    continue
            if escolha in aluno.materias_pagas:
                print("Você já pagou essa matéria.\n")
            else:
                # Ver se tem horario
                check = 0
                for materia in aluno.materias_atuais:  # pega a string materia
                    if materia in grade_TCC:
                        continue
                    elif tipo == 1 and escolha in grade_externa:
                        if materia in grade_externa:
                            for horarios_atuais_materias in grade_externa[
                                materia].horario:  # pega essa string materia e acessa seus horarios
                                for horarios_materias in grade_externa[
                                    escolha].horario:  # loopa os horario da materia escolhida com a materia que possui
                                    if horarios_atuais_materias == horarios_materias:
                                        check = 1
                                        print(
                                            f"Você não tem horário disponível para essa matéria, o horário da diciplina {grade_externa[materia].nome} é conflitante com a que voce quer aplicar ({grade_externa[escolha].nome}).")
                                        break
                                if check == 1:
                                    break
                        else:
                            for horarios_atuais_materias in grade_CC[
                                materia].horario:  # pega essa string materia e acessa seus horarios
                                for horarios_materias in grade_externa[
                                    escolha].horario:  # loopa os horario da materia escolhida com a materia que possui
                                    if horarios_atuais_materias == horarios_materias:
                                        check = 1
                                        print(
                                            f"Você não tem horário disponível para essa matéria, o horário da diciplina {grade_externa[materia].nome} é conflitante com a que voce quer aplicar ({grade_externa[escolha].nome}).")
                                        break
                                if check == 1:
                                    break
                    else:
                        for horarios_atuais_materias in grade_CC[
                            materia].horario:  # pega essa string materia e acessa seus horarios
                            for horarios_materias in grade_CC[
                                escolha].horario:  # loopa os horario da materia escolhida com a materia que possui
                                if horarios_atuais_materias == horarios_materias:
                                    check = 1
                                    print(
                                        f"Você não tem horário disponível para essa matéria, o horário da diciplina {grade_CC[materia].nome} é conflitante com a que voce quer aplicar ({grade_CC[escolha].nome}).")
                                    break
                            if check == 1:
                                break
                    if check == 1:
                        break
                if check == 1:
                    continue
                pedido = Pedido(aluno, escolha)
                if ajuste_lista != []:
                    check = 0
                    for i in ajuste_lista:
                        if i.aluno == pedido.aluno and i.insercao == pedido.insercao:
                            check = 1
                            print("Essa inseção já foi registrada!")
                            break
                    if check == 1:
                        continue
                ajuste_lista.append(pedido)
                print("Sua inserção foi registrada.")


def remocao(aluno: Aluno, tipo: int):
    if len(aluno.materias_atuais) - 1 < 3:
        print("Você deve ficar matriculado em no mínimo 3 matérias")
        return
    print("Materias atuais:")
    for materia in aluno.materias_atuais:
        print("\033[1m" + materia + "\033[0m")
    print("")

    while True:
        escolha = input("Qual matéria você quer ser removido?, digite o código: (digite 'e' para sair) ").upper()
        if escolha in grade_TCC:
            print("TCC não pode ser removida")
            continue
        if escolha == 'E':
            return
        if not escolha in aluno.materias_atuais:
            if tipo == 1:
                if not escolha in mat_lista or escolha not in mat_lista_externa:
                    print("matéria inexistente")
            elif not escolha in mat_lista:
                print("matéria inexistente")
            else:
                print(f"Você não esta matriculado na materia {escolha},e o por isso não pode ser removido dela.")
        else:
            pedido = Pedido(aluno, None, escolha)
            if ajuste_lista != []:
                check = 0
                for i in ajuste_lista:
                    if i.aluno == pedido.aluno and i.remocao == pedido.remocao:
                        check = 1
                        print("Essa remoção já foi registrada!")
                        break
                if check == 1:
                    continue
            ajuste_lista.append(pedido)
            print("Sua remoção foi registrada.")


def troca(aluno: Aluno, tipo: int):
    print("Materias atuais:")
    for materia in aluno.materias_atuais:
        print("\033[1m" + materia + "\033[0m")
    print("")
    while True:
        escolha_remover = input("Digite o código da matéria(remover): (digite 'e' para sair) ").upper()
        if escolha_remover in grade_TCC:
            print("TCC não pode ser removida")
            continue
        if escolha_remover == 'E':
            return
        if not escolha_remover in aluno.materias_atuais:
            if tipo == 1:
                if not escolha_remover in mat_lista or escolha_remover not in mat_lista_externa:
                    print("matéria inexistente")
            elif not escolha_remover in mat_lista:
                print("matéria inexistente")
            else:
                print(
                    f"Você não esta matriculado na materia {escolha_remover},e o por isso não pode ser removido dela.")
        else:
            break

    print("\nDisciplinas de Ciência:\n")
    for materia in grade_CC:
        if (materia in aluno.materias_pagas) or (materia in aluno.materias_atuais):
            continue
        print("\033[1m" + materia + "\033[0m" + ":", grade_CC[materia].nome, end=" || ")
    if tipo == 1:
        print("\n\nDisciplinas externas:\n")
        for materia in grade_externa:
            if (materia in aluno.materias_pagas) or (materia in aluno.materias_atuais):
                continue
            print("\033[1m" + materia + "\033[0m" + ":", grade_externa[materia].nome, end=" || ")
    print("")
    print("Agora informe ")

    while True:
        escolha_insercao = input("Digite o código da matéria(inserir): (digite 'e' para sair) ").upper()
        print("")
        if escolha_insercao in grade_TCC:
            print("Essa matéria não pode ser inserida")
            continue
        if escolha_insercao == 'E':
            return
        if tipo == 1:
            if not escolha_insercao in mat_lista and not escolha_insercao in mat_lista_externa:
                print("essa matéria não existe!")
                continue
        elif not escolha_insercao in mat_lista:
            print("essa matéria não existe!")
            continue
        if escolha_insercao in aluno.materias_atuais:
            if escolha_insercao in grade_externa:
                print(f"Você já esta cadastrado em {grade_externa[escolha_insercao].nome}")
            else:
                print(f"Você já esta cadastrado em {grade_CC[escolha_insercao].nome}")
            continue
        else:
            # Ve se tem pré-requesito
            if tipo == 1 and escolha_insercao in grade_externa:
                lista_prereq = grade_externa[escolha_insercao].pre_requisitos
                quant_prereq = len(grade_externa[escolha_insercao].pre_requisitos)
            else:
                lista_prereq = grade_CC[escolha_insercao].pre_requisitos
                quant_prereq = len(grade_CC[escolha_insercao].pre_requisitos)

            confirm_requirement = False
            if quant_prereq > 0:
                for pagas in aluno.materias_pagas:
                    if tipo == 1 and escolha_insercao in grade_externa:
                        for pre_req in grade_externa[escolha_insercao].pre_requisitos:
                            if pre_req == pagas:
                                quant_prereq = quant_prereq - 1
                                lista_prereq.remove(pre_req)
                                if quant_prereq == 0:
                                    confirm_requirement = True
                                    break
                    else:
                        for pre_req in grade_CC[escolha_insercao].pre_requisitos:
                            if pre_req == pagas:
                                quant_prereq = quant_prereq - 1
                                lista_prereq.remove(pre_req)
                                if quant_prereq == 0:
                                    confirm_requirement = True
                                    break
                if confirm_requirement == False:
                    print(f"Você NÃO tem o pre-requesito para pagar essa matéria, você precisa pagar:")
                    print(*lista_prereq, sep=' ')
                    continue
            if escolha_insercao in aluno.materias_pagas:
                print("Você já pagou essa matéria!\n")
            else:
                # Ver se tem horario
                check = 0
                for materia in aluno.materias_atuais:  # pega a string materia
                    if materia in grade_TCC:
                        continue
                    elif tipo == 1 and escolha_insercao in grade_externa:
                        if materia in grade_externa:
                            for horarios_atuais_materias in grade_externa[
                                materia].horario:  # pega essa string materia e acessa seus horarios
                                for horarios_materias in grade_externa[
                                    escolha_insercao].horario:  # loopa os horario da materia escolhida com a materia que possui
                                    if horarios_atuais_materias == horarios_materias:
                                        check = 1
                                        print(
                                            f"Você não tem horário disponível para essa matéria, o horário da diciplina {grade_externa[materia].nome} é conflitante com a que voce quer aplicar ({grade_externa[escolha_insercao].nome}).")
                                        break
                                if check == 1:
                                    break
                        else:
                            for horarios_atuais_materias in grade_CC[
                                materia].horario:  # pega essa string materia e acessa seus horarios
                                for horarios_materias in grade_externa[
                                    escolha_insercao].horario:  # loopa os horario da materia escolhida com a materia que possui
                                    if horarios_atuais_materias == horarios_materias:
                                        check = 1
                                        print(
                                            f"Você não tem horário disponível para essa matéria, o horário da diciplina {grade_externa[materia].nome} é conflitante com a que voce quer aplicar ({grade_externa[escolha_insercao].nome}).")
                                        break
                                if check == 1:
                                    break
                    else:
                        for horarios_atuais_materias in grade_CC[
                            materia].horario:  # pega essa string materia e acessa seus horarios
                            for horarios_materias in grade_CC[
                                escolha_insercao].horario:  # loopa os horario da materia escolhida com a materia que possui
                                if horarios_atuais_materias == horarios_materias:
                                    check = 1
                                    print(
                                        f"Você não tem horário disponível para essa matéria, o horário da diciplina {grade_CC[materia].nome} é conflitante com a que voce quer aplicar ({grade_CC[escolha_insercao].nome}).")
                                    break
                            if check == 1:
                                break
                    if check == 1:
                        break
                if check == 1:
                    continue
            pedido = Pedido(aluno, escolha_insercao, escolha_remover)
            print(pedido.insercao)
            if ajuste_lista != []:
                check = 0
                for i in ajuste_lista:
                    if i.aluno == pedido.aluno and i.insercao == pedido.insercao and i.remocao == pedido.remocao:
                        check = 1
                        print("Essa troca já foi registrada!")
                        break
                if check == 1:
                    continue
            ajuste_lista.append(pedido)
            print("troca registrada")
            break


def confirmar_Ajustes(ajuste_lista):
    if ajuste_lista == []:
        print("não há ajustes para realizar!")
        return ajuste_lista
    else:
        # for de ordenação
        for pedido in ajuste_lista:
            # trocas insert
            if pedido == '*':
                continue
            pedido.aluno.etapa = 3
            if pedido.insercao != None and pedido.remocao != None:
                if grade_CC[pedido.insercao].ocupado == grade_CC[pedido.insercao].limite:
                    print("matéria cheia! não vai ser possivel fazer a troca!")
                    print("Por favor tente denovo no reajuste: ", pedido.aluno.nome)
                    continue
                for j in range(len(ajuste_lista)):
                    if pedido == ajuste_lista[j] or ajuste_lista[j] == '*':
                        continue
                    elif (ajuste_lista[j].insercao == pedido.remocao) and ajuste_lista[j].remocao == None:
                        print("ajustando a troca: ", pedido.aluno.nome, " que atende inserção ",
                              ajuste_lista[j].aluno.nome, end="")
                        grade_CC[pedido.remocao].ocupado -= 1
                        pedido.aluno.materias_atuais.remove(pedido.remocao)
                        if pedido.remocao in grade_CC and grade_CC[pedido.remocao].tipo == 0:
                            print("Seu fluxo mudou para individual devido à remoção de uma matéria obrigatória.")
                            pedido.aluno.fluxo = 1
                        grade_CC[pedido.insercao].ocupado += 1
                        pedido.aluno.materias_atuais.append(pedido.insercao)
                        print("\najuste efetuado!")
                        ajuste_lista = ['*' if item == pedido else item for item in ajuste_lista]
            else:
                continue

        for pedido in ajuste_lista:
            # trocas remove
            if pedido == '*':
                continue
            pedido.aluno.etapa = 3
            if pedido.insercao != None and pedido.remocao != None:
                if grade_CC[pedido.insercao].ocupado == grade_CC[pedido.insercao].limite:
                    print("matéria cheia! não vai ser possivel fazer a troca!")
                    print("Por favor tente denovo no reajuste: ", pedido.aluno.nome)
                    continue
                for j in range(len(ajuste_lista)):
                    if pedido == ajuste_lista[j] or ajuste_lista[j] == '*':
                        continue
                    elif (ajuste_lista[j].remocao == pedido.insercao) and ajuste_lista[j].insercao == None:
                        print("ajustando a troca: ", pedido.aluno.nome, " que atende remoção ",
                              ajuste_lista[j].aluno.nome, end="")
                        grade_CC[pedido.remocao].ocupado -= 1
                        pedido.aluno.materias_atuais.remove(pedido.remocao)
                        if pedido.remocao in grade_CC and grade_CC[pedido.remocao].tipo == 0:
                            print("Seu fluxo mudou para individual devido à remoção de uma matéria obrigatória.")
                            pedido.aluno.fluxo = 1
                        grade_CC[pedido.insercao].ocupado += 1
                        pedido.aluno.materias_atuais.append(pedido.insercao)
                        print("\najuste efetuado!")
                        ajuste_lista = ['*' if item == pedido else item for item in ajuste_lista]
            else:
                continue

        for pedido in ajuste_lista:
            # trocas
            if pedido == '*':
                continue
            pedido.aluno.etapa = 3
            if pedido.insercao != None and pedido.remocao != None:
                if grade_CC[pedido.insercao].ocupado == grade_CC[pedido.insercao].limite:
                    print("matéria cheia! não vai ser possivel fazer a troca!")
                    print("Por favor tente denovo no reajuste: ", pedido.aluno.nome)
                    continue
                else:
                    print("ajustando a troca:", pedido.aluno.nome, end="")
                    grade_CC[pedido.remocao].ocupado -= 1
                    pedido.aluno.materias_atuais.remove(pedido.remocao)
                    if pedido.remocao in grade_CC and grade_CC[pedido.remocao].tipo == 0:
                        print("Seu fluxo mudou para individual devido à remoção de uma matéria obrigatória.")
                        pedido.aluno.fluxo = 1
                    grade_CC[pedido.insercao].ocupado += 1
                    pedido.aluno.materias_atuais.append(pedido.insercao)
                    print("\najuste efetuado!")
                    ajuste_lista = ['*' if item == pedido else item for item in ajuste_lista]
            else:
                continue

        for pedido in ajuste_lista:
            # remoções
            if pedido == '*':
                continue
            pedido.aluno.etapa = 3
            if pedido.insercao == None and pedido.remocao != None:
                if not pedido.remocao in pedido.aluno.materias_atuais:
                    print("você não está nessa matéria!!")
                    continue
                grade_CC[pedido.remocao].ocupado -= 1
                pedido.aluno.materias_atuais.remove(pedido.remocao)
                if pedido.remocao in grade_CC and grade_CC[pedido.remocao].tipo == 0:
                    print("Seu fluxo mudou para individual devido à remoção de uma matéria obrigatória.")
                    pedido.aluno.fluxo = 1
                print("ajustando remoção %s" % pedido.aluno.nome)
                print("removendo:", grade_CC[pedido.remocao].nome)
                ajuste_lista = ['*' if item == pedido else item for item in ajuste_lista]

        for pedido in ajuste_lista:
            if pedido == '*':
                continue
            pedido.aluno.etapa = 3
            if pedido.insercao != None and pedido.remocao == None:
                if grade_CC[pedido.insercao].ocupado == grade_CC[pedido.insercao].limite:
                    print("matéria cheia! não vai ser possivel fazer a inserção!")
                    print("Por favor tente denovo no reajuste: ", pedido.aluno.nome)
                    continue
                grade_CC[pedido.insercao].ocupado += 1
                pedido.aluno.materias_atuais.append(pedido.insercao)
                print("ajustando inserção %s" % pedido.aluno.nome)
                ajuste_lista = ['*' if item == pedido else item for item in ajuste_lista]
        result = filter(lambda val: val != '*', ajuste_lista)
        print("ajustes efetuados!!")
        return list(result)


def exibir_Alunos():
    for i in range(len(matriculados)):
        print("\n#", str(matriculados[i].id) + " || " + "\033[1m" + "Nome: " + "\033[0m" + matriculados[
            i].nome + " || " + "\033[1m" + "matérias atuais: " + "\033[0m" + str(
            matriculados[i].materias_atuais) + " || " + "\033[1m" + "coeficiente: " + "\033[0m" + str(
            matriculados[i].coeficiente) + " || " + "\033[1m" + "fluxo: " + "\033[0m" + str(
            matriculados[i].fluxo) + " || " + "\033[1m" + "matérias pagas:" + "\033[0m" + str(
            matriculados[i].materias_pagas) + " || " + "\033[1m" + "pendências: " + "\033[0m" + str(
            matriculados[i].pendencias))
    return


counter = 0
etapa_efetivar = False
while True:
    if counter == 4:
        print("Limite de entradas inválidas atingido. Programa encerrado.")
        exit()
    x = input(
        "\nBem-vindo ao sistema de matrícula, ajuste e reajuste.\n(1) - Matrícula;\n(2) - Ajuste;\n(3) - Efetivar Ajustes;\n(4) - Reajuste;\n(5) - Efetivar Reajustes;\n(6) - Listar Matriculados;\n(7) - Encerrar programa.\nSelecione uma opção: ")
    if x == '1':
        matricula()
        exibir_Alunos()
    elif x == '2':
        ajuste_reajuste(0)
    elif x == '3':
        etapa_efetivar = True
        ajuste_lista = list(confirmar_Ajustes(ajuste_lista))
        print(ajuste_lista)
    elif x == '4':
        if etapa_efetivar == False:
            print('Não é possivel fazer reajustes antes de efetivar os ajustes!')
        else:
            ajuste_reajuste(1)
    elif x == '5':
        if etapa_efetivar:
            ajuste_lista = list(confirmar_Reajustes(ajuste_lista))
            print(ajuste_lista)
        else:
            print("a Etapa de ajuste ainda não foi Efetivada!!")
    elif x == '6':
        exibir_Alunos()
    elif x == '7':
        print("Programa encerrado.")
        exit()
    else:
        print("Entrada inválida!")
        counter += 1