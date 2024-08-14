from operacoes import calcular_media, verificar_reprovacao, formatar_dados_reprovado

# Estrutura para armazenar dados dos alunos
alunos = [
    {"nome": "João", "matricula": "2023001", "notas": [7.5, 6.0, 8.0, 5.5]},
    {"nome": "Maria", "matricula": "2023002", "notas": [5.0, 4.5, 6.0, 7.0]},
    {"nome": "Pedro", "matricula": "2023003", "notas": [9.0, 8.5, 9.0, 8.0]},
]

# Lista para armazenar dados dos alunos reprovados
alunos_reprovados = []

for aluno in alunos:
    media = calcular_media(aluno["notas"])
    if verificar_reprovacao(media):
        aluno_reprovado_info = formatar_dados_reprovado(aluno["nome"], aluno["matricula"], media)
        alunos_reprovados.append(aluno_reprovado_info)

# Imprimir dados dos alunos reprovados
for info in alunos_reprovados:
    print(info)