from materias import grade_curricular

class Aluno:
    def __init__(self, id: int, nome: str, fluxo: int, coeficiente: float, materias_atuais: list, materias_pagas: list, pendencias: list):
        self.id = id
        self.nome = nome  # Geralt of Rivia, James Howlett...
        self.fluxo = fluxo  # padrão (4), calouro (3), formando (2), individual (1)
        self.coeficiente = coeficiente  # 8.5
        self.materias_atuais = materias_atuais  # ["COMP359","COMP360","COMP361","COMP362","COMP363"]
        self.materias_pagas = materias_pagas  # ["COMP359","COMP360","COMP361","COMP362","COMP363"]
        self.pendencias = pendencias


def ajuste():
    global posicao_aluno_vetor
    posicao_aluno_vetor  = -1
    valido = False
    goback = input("(0) - Voltar\n"
                   "(1) - Continuar\n"
                   "Selecione uma opção: ")
    if goback == '0':
        return

    while valido == False:
        print("Processo de ajuste iniciado.")
        identificacao_ajuste = int(input("Insira seu ID: "))
        for ide in cadastrados:
            posicao_aluno_vetor = posicao_aluno_vetor + 1
            if ide.id == identificacao_ajuste:
                print(f"\nBem-vindo(a) {ide.nome}.")
                valido = True

        if valido == False:
            posicao_aluno_vetor = -1
            print("ID INVÁLIDO")

    game_off = True
    while (game_off):
        print("Qual operação vc quer realizar no ajuste?")
        y = int(input("\n(1): Inserção de matéria."
                      "\n(2): Remoção de matéria."
                      "\n(3): Troca de matéria.\n"
                      "(4): Encerrar.\n"
                      "Selecione uma opção: "))
        if y == 1:
            insercao()
            game_on = False
        elif y == 2:
            remocao()
            game_on = False
        elif y == 3:
            troca()
            game_on = False
        elif y  == 4:
            return
            #voltar para tela inicial
        else:
            print("Opção inválida")


def insercao():
    materias_inserir = []
    confirm_requirement = True
    global choice, escolha
    #checar se o cara já nao ta no maximo
    if len(cadastrados[posicao_aluno_vetor].materias_atuais) >= 10:
        print("Você já esta limite máximo de disciplinas cadastradas")
        return

    print("")
    while confirm_requirement: #checar se ele nao vai passar o máximo
        choice = int(input("Quantas matérias você quer ser inserido ?\n"))  # ASK AGAIN
        if choice + len(cadastrados[posicao_aluno_vetor].materias_atuais) > 10:
            print("Você só pode estar matriculado em no máximo 10 matérias")
            #voltar pergunta
        else:
            confirm_requirement = False

    for materias in grade_curricular:
        print(f"{materias}: {grade_curricular[materias].nome}")
    print("")
    for i in range(choice):
        escolha = input("Digite o código das matérias").upper()
        #checa se existe, se existe append
        materias_inserir.append(escolha)

    print("")
    #CHECAR SE EXISTE

    #Ve se tem pré-requesito
    lista_prereq = grade_curricular[escolha].pre_requisitos
    confirm_requirement = False
    quant_prereq = len(grade_curricular[escolha].pre_requisitos)
    if quant_prereq > 0:
        for pagas in cadastrados[posicao_aluno_vetor].materias_pagas:
            for pre_req in grade_curricular[escolha].pre_requisitos:
                if pre_req == pagas:
                    quant_prereq = quant_prereq - 1
                    lista_prereq.remove(pre_req)
                    if quant_prereq == 0:
                        confirm_requirement = True
                        print("Você tem o(s) pre-requesito(s) para pagar essa matéria.\n")
    else:
        confirm_requirement = True
        print("Essa matéria não tem pre-requesito.\n")

    if confirm_requirement == False:
        print(f"Você NÃO tem o pre-requesito para pagar essa matéria, você precisa pagar:")
        print(*lista_prereq, sep=' ')
        return


    #Ver se tem horario
    for mtm in cadastrados[posicao_aluno_vetor].materias_atuais: #pega a string materia
        for horarios_atuais_materias in grade_curricular[mtm].horario: #pega essa string materia e acessa seus horarios
            for horarios_materias in grade_curricular[escolha].horario: #loopa os horario da materia escolhida com a materia que possui
                if horarios_atuais_materias == horarios_materias:
                    print(f"Você não tem horário disponível para essa matéria, o horário da diciplina {grade_curricular[mtm].nome} é conflitante com a que voce quer aplicar ({grade_curricular[escolha].nome}).")
                    return


    choice = input("Você quer realizar outra inserção?" "s/n")
    if choice == 's':
        insercao()


def remocao():
    materias_remocao = []
    for materias in grade_curricular:
        print(f"{materias}: {grade_curricular[materias].nome}")
    print("")
    choice = int(input("Você quer sair de quantas matérias?\n")) #ASK AGAIN
    if len(cadastrados[posicao_aluno_vetor].materias_atuais) - choice < 3:
        print("Você deve permanecer em no mínimo três matérias.")
        #voltar pergunta

    print("")
    for i in range(choice):
        escolha = input("Qual matéria você quer ser removido?, digite o código: ").upper()

        #checar se é valida
        materias_remocao.append(escolha)

    remover_materias = []
    #checar se o usuário está matriculado na matéria
    for i in cadastrados[posicao_aluno_vetor].materias_atuais:
        for p in materias_remocao:
            if i == p:
                materias_remocao.remove(p)
                remover_materias.append(p)

    if len(materias_remocao) > 0 and len(remover_materias) > 0:
        for i in materias_remocao:
            print(f"Você não esta cadastrado na matéria {grade_curricular[i].nome} e por isso não pode ser removido "
                  f"dela.")

        print("Seu pedido de remoção das seguintes matérias foi realizado: ")
        print(*remover_materias, sep= ' ')

    elif len(materias_remocao) > 0:
        for i in materias_remocao:
            print(f"\nVocê não esta matriculado na matéria {grade_curricular[i].nome} e por isso não pode ser removido.")
    else:
        print("\nSeu pedido de remoção das seguintes matérias foi realizado: ")
        print(*remover_materias, sep= ' ')

    #ARMAZENAR REMOÇÃO



def troca():
    choice = input("Quantas trocas você quer efetuar?\n")
    for i in range(choice):
        pass

id = 0
cadastrados = [
    Aluno(111, 'José', 1, 6.0, [""], ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363", "COMP365", "COMP366", "COMP364", "COMP367"], []),
    Aluno(222, 'Maria', 3, 6.0, ["COMP373","COMP372", "CC1965"], ["COMP359", "COMP360","COMP361", "COMP362", "COMP363", "COMP365", "COMP366","COMP364", "COMP368"], [])
]

#possivel função de cadastro de alunos??

def matricula():
    print("Processo de matrícula iniciado.")

    w = 0
    while w < 10:
        if w == 4:
            print(
                "Limite de entradas inválidas atingido. Processo de matrícula encerrado.")
            return
        q = input("É calouro? (s = sim / n = não): ").lower()
        if q == 's':
            nome = input("Insira o nome: ").strip()
            nome = nome[0].upper() + nome[1:]
            if len(nome) == 0 or nome.isspace() or not all(i.isalpha() or i.isspace() for i in nome):
                print("Entrada inválida!")
                w += 1
            else:
                global id
                id += 1
                calouro = Aluno(id, nome, 3, 10.0, ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363"], [[]], [])
                for i in range(len(calouro.materias_atuais)):
                    if calouro.materias_atuais[i] in grade_curricular:
                        if (grade_curricular[calouro.materias_atuais[i]].ocupado == grade_curricular[calouro.materias_atuais[i]].limite):
                             print("materia cheia!!")
                             return
                        else:
                            grade_curricular[calouro.materias_atuais[i]].ocupado+=1
                matriculados.append(calouro)
                print("matricula efetuada!!")
                return
        elif q == 'n':
            num = int(input("Insira o número da sua matrícula: "))
            check=0
            for i in range(len(cadastrados)):
                if cadastrados[i].id == num:
                    aluno = cadastrados[i]
                    check=1
                    break
            if check == 0:
                if matriculados != []:
                    for j in range(len(matriculados)):
                        if matriculados[j].id == num:
                            print("\n\nvocê já está matriculado!")
                            if matriculados[j].fluxo == 3:
                                print("e você é calouro sim!!\n\n")
                            return
                print("\n\no aluno não consta no sistema!\n\n")
            else:
                for j in cadastrados:
                    if (aluno.fluxo < j.fluxo):
                        print("Desculpe, aguarde alunos de prioridade maior fazerem sua matrícula!!")
                        return
                while True:
                    if(len(aluno.materias_atuais) == 10):
                        matriculados.append(aluno)
                        cadastrados.remove(aluno)
                        print("limite de materias atingido")
                        print("matricula efetuada!!")
                        return

                    if(len(aluno.materias_atuais) <3):
                        sel = input("selecione uma materia para se matrícular: ").upper()
                    else:
                        while True:
                            sel = input("selecione uma materia para se matrícular (para encerrar digite 'e')):").upper() #DEPOIS TRATAR O CASO DO CARA ESCREVER ERRADO!!!!
                            if sel == 'E':
                                matriculados.append(aluno)
                                cadastrados.remove(aluno)
                                print("matricula efetuada!!")
                                return
                            else:
                                break
                    if sel in aluno.materias_pagas:  # JÁ PAGOU!?
                        print("você já pagou essa matéria")
                    elif sel in grade_curricular:
                        conflito=False
                        for i in range(len(aluno.materias_atuais)):
                            for j in range(len(grade_curricular[aluno.materias_atuais[i]].horario)):
                                for k in range(len( grade_curricular[sel].horario)):
                                    if grade_curricular[aluno.materias_atuais[i]].horario[j] == grade_curricular[sel].horario[k]:
                                        print("horarios conflitantes!!")
                                        return
                        print(grade_curricular[sel].nome)
                        if(grade_curricular[sel].ocupado == grade_curricular[sel].limite):
                            print("materia cheia!!!")
                            return
                        if(grade_curricular[sel].pre_requisitos != []):
                            for i in range(len(grade_curricular[sel].pre_requisitos)):
                                if not grade_curricular[sel].pre_requisitos[i] in aluno.materias_pagas:
                                    print("não cumpriu os pré-requisitos para ingressar na matéria!!")
                                    return
                        if sel in aluno.pendencias:
                            aluno.pendencias.remove(sel)
                        aluno.materias_atuais.append(sel)
                        grade_curricular[sel].ocupado+=1
                        print(len(aluno.materias_atuais))
                    else:
                        print("essa matéria não existe!!")
            return
        else:
            print("Entrada inválida!")
            w += 1

matriculados = []
counter = 0
while True:
    if counter == 4:
        print("Limite de entradas inválidas atingido. Programa encerrado.")
        exit()
    x = input("\nBem-vindo ao sistema de matrícula, ajuste e reajuste.\n(1) - Matrícula;\n(2) - Ajuste;\n(3) - Reajuste;\n(4) - Encerrar programa.\nSelecione uma opção: ")
    if x == '1':
        matricula()
        for i in range(len(matriculados)):
            print("\n# ", str(matriculados[i].id)+' - '+matriculados[i].nome+' atuais:'+str(matriculados[i].materias_atuais)+' coef:'+str(
                matriculados[i].coeficiente)+' fluxo:'+str(matriculados[i].fluxo)+' pagas'+str(matriculados[i].materias_pagas)+' pendencias'+str(matriculados[i].pendencias))
    elif x == '2':
        ajuste()
    elif x == '4':
        print("Programa encerrado.")
        exit()
    else:
        print("Entrada inválida!")
        counter += 1