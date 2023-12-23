'Dupla: Eliabe De Jesus e Ana Paula Costa (e Daniel Christi)'

import modulo

def main():
    
    #declaração de variaveis
    dict_alunos = dict()
    dict_disciplina = dict()
    dict_matricula = dict()
    
    
    nome_arq = "ativ11.txt"#input("Nome do Arquivo das disciplinas: ") "ativ11.txt"
    dict_disciplina = modulo.f_disciplina(nome_arq)

    
    nome_arq_A = "ativ11parte2.txt" #input("Nome do Arquivo dos Alunos: ") "ativ11parte2.txt"
    dict_alunos = modulo.f_alunos(nome_arq_A)

    
    dict_matricula = modulo.f_matricular(dict_disciplina,dict_alunos)
    
    nome_arq_R = "relatorio.txt"#input("Nome do Arquivo do relatório: ")
    modulo.f_imprime(dict_matricula, dict_disciplina,dict_alunos,nome_arq_R)


    

if __name__ == "__main__":
    main()