
'Dupla: Eliabe De Jesus e Ana Paula Costa (e Daniel Christi)'

from random import randint,uniform

#lê um arquivo e cria um dicionario das informações das diciplinas
def f_disciplina(Arq:str) -> dict:
    
    #declaração de variaveis
    codigo = int()
    disciplina = str()
    ementa = str()
    carga_horaria = str()
    lista_valor = list()
    dicionario = dict()
    dados = list()

    #abertura do arquivo
    ref_arq = open(Arq, mode="r", encoding="utf-8")
    
    #leitura do arquivo
    for linha in ref_arq:
        
        dados = linha.split(";")
        codigo = int(dados[0])
        disciplina = dados[1]
        ementa = dados[2]
        carga_horaria = int(dados[3])
        lista_valor = [disciplina,ementa,carga_horaria]
        dicionario[codigo] = lista_valor
    
    #fechamento do arquivo
    ref_arq.close()

    return dicionario

#lê um arquivo e cria um dicionario das informações dos alunos
def f_alunos(Arq:str) -> dict:

    #declaração de variaveis
    nome = str()
    dicionario = dict()
    nome = str()
    cpf = str()
    lista_valor = list()
    dados = list()
    
    #abertura do arquivo
    ref_arq = open(Arq, mode="r", encoding="utf-8")
    
    #leitura do arquivo
    for linha in ref_arq:
        dados = linha.split(";")
        matricula = dados[0]
        nome = dados[1]
        cpf = dados[2]
        
        lista_valor = [nome,cpf]
        dicionario[matricula] = lista_valor
    
    #fechamento do arquivo
    ref_arq.close()
    
    return dicionario

#matricula os alunos nas diciplinas
def f_matricular(disciplinas:dict, alunos:dict) -> dict:
    
    #declaração de variaveis
    dicionario = dict()
    notas = float()
    faltas = int()
    lista = list()
    dicionario = dict()
    carga_horaria = int()
    
    #for que percorre os dicionarios
    for i in disciplinas:
        for j in alunos:
            
            tupla = (i,j)
            carga_horaria = disciplinas[i][2]
            
            notas = uniform(0,100)
            faltas = randint(0,carga_horaria)
            lista = [notas,faltas]
            dicionario[tupla] = lista
            
    return dicionario
#imprime o relatório em um arquivo 
def f_imprime(dict_matricula:dict, dict_disciplina:dict, dict_alunos:dict, nome_arq_R:str):
    
    #declaração de variaveis
    codigo = list()
    nota = float()
    carga_horaria = int()
    faltas = int()
    
    ref_arq = open(nome_arq_R, mode="w", encoding="utf-8")
    
    #for que percorre disciplina
    
    for codigo in dict_disciplina:
        materia = dict_disciplina[codigo][0]
        ref_arq.write("Disciplina: ")
        ref_arq.write(materia)
        ref_arq.write("\n")
        print("Disciplina: ", materia)
        
        
        #for que percorre aluno
        for matricula in dict_alunos:
            
            nota = dict_matricula[codigo,matricula][0]
            faltas = dict_matricula[codigo,matricula][1]
            carga_horaria = dict_disciplina[codigo][2]
            
            estado = f_estado(nota,carga_horaria,faltas)
            
            ref_arq.write(matricula)
            ref_arq.write("  ")
            ref_arq.write(estado)
            ref_arq.write("\n")
            print(matricula, estado)
            
            
        

#Função que define o estado do aluno baseado em sua nota, faltas e a carga horária da matéria
def f_estado (nota:float,carga_horaria:int,faltas:int) -> str:
    
    #declaração de variaveis
    estado = str()
    max_faltas = (1/4) * carga_horaria
    
    #lógica para a definição
    if nota >= 60:
        if faltas <= max_faltas:
            estado = "A"
        else:
            estado = "RF"
    else:
        if faltas <= max_faltas:
            estado = "RN"
        else:
            estado = "RNF"

    return estado

