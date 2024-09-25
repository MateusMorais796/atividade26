# Crie um programa que receba as notas de 5 alunos e as armazene em uma lista. O programa deve exibir a maior nota, a menor nota e a média das notas.

# Exemplo de entrada:
# Nota do aluno 1: 8
# Nota do aluno 2: 6
# Nota do aluno 3: 9
# Nota do aluno 4: 7
# Nota do aluno 5: 5

# Exemplo de saída:
# Maior nota: 9
# Menor nota: 5
# Média das notas: 7.0

nota_dos_alunos = []
soma = 0
for n in range(0, 5):
    soma += 1
    nota_dos_alunos.append(float(input("Digite a nota ")))

s_nota = sum(nota_dos_alunos)

media = s_nota/soma

print(f'''a maior nota é {max(nota_dos_alunos)}
a menor nota é {min(nota_dos_alunos)}
a media das notas é {media}''')