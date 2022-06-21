# A LISTAGEM AUTOMÁTICA DAS MATÉRIAS É APENAS NO CASO 'CALOURO'
# EM QUALQUER OUTRO PERÍODO O ALUNO DEVE SELECIONAR SUAS MATÉRIAS
# AS MATÉRIAS QUE APARECEREM PARA SELEÇÃO DEVEM SER FILTRADAS DE ACORDO COM OS PREREQUISITOS CUMPRIDOS PELO ALUNO

class Disciplina:
    def __init__(self, nome: str, pre_requisitos: list, horario: list):
        self.nome = nome
        self.pre_requisitos = pre_requisitos
        self.horario = horario
        self.limite = 10
        self.ocupado = 0  # quantos estão atualmente matriculados


grade_curricular = {
    # 1º periodo
    "COMP359": Disciplina("Programação 1", [], ['SX07300910', 'SX09201100']),
    "COMP360": Disciplina("Lógica para Computação", [], ['SG11101250', 'QA11101250']),
    "COMP361": Disciplina("Computação, Sociedade e Ética", [], ['SE09201100', 'QA09201100']),
    "COMP362": Disciplina("Matemática Discreta", [], ['SG07300910', 'QI07300910']),
    "COMP363": Disciplina("Cálculo Diferencial e Integral", [], ['TE07201110', 'QI07201110']),
    # 2º periodo
    "COMP364": Disciplina("Estrutura de Dados", ["COMP359"], ['SE13301510', 'QA13301510']),
    "COMP365": Disciplina("Banco de Dados", [], ['TE15201700', 'QI15201700']),
    "COMP366": Disciplina("Organização e Arquitetura de Computadores", [], ['SE17101850', 'QA17101850']),
    "COMP367": Disciplina("Geometria Analítica", [], ['SE15201700', 'QA15201700']),
    # 3º periodo
    "COMP368": Disciplina("Redes de Computadores", ["COMP359"], ['TE07201110', 'QI07201110']),
    "COMP369": Disciplina("Teoria dos Grafos", ["COMP364", "COMP362"], ['SE09201100', 'TE09201100']),
    "COMP370": Disciplina("Probabilidade e Estatística", ["COMP363"], ['SE07300910', 'QA07300910']),
    "COMP371": Disciplina("Álgebra Linear", ["COMP367"], ["SE11101250", "QA09201100"]),

    # 4º periodo
    "COMP372": Disciplina("Programação 2", ["COMP364", "COMP365", "COMP368"], ['QA13301510', 'QA15201700']),
    "COMP373": Disciplina("Programação 3", ["COMP364", "COMP365", "COMP368"], ['TE15201700', 'QI15201700']),
    "COMP374": Disciplina("Projeto e Análise de Algorítimos", ["COMP364", "COMP369"], ['SE13301510', 'QA17101850']),
    "COMP376": Disciplina("Teoria da Computação", [], ['TE13301510', 'QI13301510']),
    # 5º periodo
    "COMP378": Disciplina("Sistemas Operacionais", ["COMP366"], ['SE0730910', 'QA0730910']),
    "COMP379": Disciplina("Compiladores", ["COMP364", "COMP376"], ['SE11101250', 'QA11101250']),
    "COMP380": Disciplina("Inteligencia Artificial", ["COMP360", "COMP364"], ['SE09201100', 'QA09201100']),
    "COMP381": Disciplina("Computação Gráfica", [], ['TE07200910', 'QI07200910']),
    # 6º periodo
    "COMP382": Disciplina("Projeto e Desenvolvimento de Sistemas",
                          ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363", "COMP364", "COMP365", "COMP366",
                           "COMP367", "COMP369", "COMP370", "COMP371", "COMP372", "COMP373", "COMP374",
                           "COMP376", "COMP378", "COMP379", "COMP380", "COMP381"],
                          ['SE07201110', 'TE07201110', 'QA07201110', 'QI07201110']),
    # 7º periodo
    "COMP386": Disciplina("Metodologia de Pesquisa e Trabalho Individual", [], ['SX07300910', 'QA07300910']),
    "COMP387": Disciplina("Noções de Direito", [], ['SX09201100', 'SX11101250']),

    # ENFASES
    "COMP389": Disciplina("Conceitos de Linguagem de Programação", [], ['TE13301510', 'QI13301510']),
    "COMP390": Disciplina("Aprendizagem de Máquina", ["COMP404"], ['TE17101850', 'QI17101850']),
    "COMP391": Disciplina("Sistemas Digitais", ["COMP404"], ['TE15201700', 'SX15201700']),
    "COMP392": Disciplina("Sistemas Distribuidos", [], ['TE15201700', 'QI15201700']),
    "COMP393": Disciplina("Redes Neurais e Aprendizado Profundo", [], ["SE09201100", 'SE11101250']),
    "COMP394": Disciplina("FPGA", [], []),  ###
    "COMP395": Disciplina("Iteração Homem-Máquina", ["COMP373"], ['TE07200910', 'QI07200910']),
    "COMP396": Disciplina("Processamento Digital de Imagens", ["COMP381"], ['SE09201100', 'QA09201100']),
    "COMP397": Disciplina("Computação Evolucionária", [], ['SE09201100', 'QA09201100']),
    "COMP398": Disciplina("Sistemas Embarcados", [], []),  ###
    "COMP399": Disciplina("Gerencia de Projeto", ["COMP382"], ['TE17101850', 'QI17101850']),
    "COMP400": Disciplina("Visão Computacional", [], ['SE15201700', 'QA15201700']),
    "COMP401": Disciplina("Ciencia de Dados", ["COMP370"], ['SE15201700', 'QA15201700']),
    "COMP402": Disciplina("Microcontroladores e Aplicações", [], ['QA13301510', 'SX13301510']),
    "COMP403": Disciplina("Segurança de Sistemas Computacionais", ["COMP368"], ['QA09201100', 'SX09201100']),
    "COMP404": Disciplina("Calculo 3", ["COMP363"], ['TE13301510', 'QI13301510']),
    "COMP405": Disciplina("Tópicos em Ciência da Computação 1 ", [], []),
    "COMP406": Disciplina("Tópicos em Ciência da Computação 2", [], []),
    "COMP407": Disciplina("Tópicos em Ciência da Computação 3 ", [], []),
    "COMP409": Disciplina("Tópicos em Matemática para Computação 1 ", [], []),
    "COMP410": Disciplina("Tópicos em Matemática para Computação 2 ", [], []),
    "COMP411": Disciplina("Tópicos em Matemática para Computação 3 ", [], []),
    "COMP412": Disciplina("Tópicos em Física para Computação 1 ", [], []),
    "COMP413": Disciplina("Tópicos em Física para Computação 2 ", [], []),
    "COMP414": Disciplina("Tópicos em Física para Computação 3", [], []),

    # ELETIVAS
    "CC1941": Disciplina("Cálculo 4", [], []),
    "CC1942": Disciplina("Cálculo Numérico", [], []),
    "CC1943": Disciplina("Circuitos Digitais", [], []),
    "CC1944": Disciplina("Circuitos Impressos", [], []),
    "CC1945": Disciplina("Fundamentos de Libras", [], []),
    "CC1946": Disciplina("Geometria Computacional", [], []),
    "CC1947": Disciplina("Pesquisa Operacional", [], []),
    "CC1948": Disciplina("Programação para Sistemas Embarcados ", [], []),
    "CC1949": Disciplina("Projeto de Sistemas Embarcados", [], []),
    "CC1950": Disciplina("Tópicos em Arquitetura de Computadores ", [], []),
    "CC1951": Disciplina("Tópicos em Banco de Dados", [], []),
    "CC1952": Disciplina("Tópicos em Computação Científica ", [], []),
    "CC1953": Disciplina("Tópicos em Computação Paralela", [], []),
    "CC1954": Disciplina("Tópicos em Computação Visual", [], []),
    "CC1955": Disciplina("Tópicos em Comunicação de Dados ", [], []),
    "CC1956": Disciplina("Tópicos em Desenvolvimento de Sistemas ", [], []),
    "CC1957": Disciplina("Tópicos em Engenharia de Software", [], []),
    "CC1958": Disciplina("Tópicos em Humanidades ", [], []),
    "CC1959": Disciplina("Tópicos em Informática na Educação", [], []),
    "CC1960": Disciplina("Tópicos em Inteligência Artificial", [], []),
    "CC1961": Disciplina("Tópicos em Linguagens de Programação ", [], []),
    "CC1962": Disciplina("Tópicos em Programação ", [], []),
    "CC1963": Disciplina("Tópicos em Redes de Computadores ", [], []),
    "CC1964": Disciplina("Tópicos em Sistemas de Computação", [], []),
    "CC1965": Disciplina("Tópicos em Sistemas de Informação", [], []),
    "CC1966": Disciplina("Tópicos em Sistemas Distribuídos ", [], []),
    "CC1967": Disciplina("Tópicos em Sistemas Inteligentes", [], []),
    "CC1968": Disciplina("Tópicos em Software Básico ", [], []),
}

grade_externa = {

}