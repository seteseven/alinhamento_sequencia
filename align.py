# importando as bibliotecas necessárias
import csv
from Bio.Seq import Seq
from Bio.Align import PairwiseAligner
from Bio import SeqIO

seq1 = SeqIO.read('01.fasta','fasta')
seq2 = SeqIO.read('02.fasta','fasta')


# define o alinhador
alinhador = PairwiseAligner()

# configuração do alinhamento
alinhador.mode = 'global'
alinhador.match_score = 2
alinhador.mismatch_score = -1
alinhador.open_gap_score = -2
alinhador.extend_gap_score = -1

# realiza o alinhamento
alinhamentos = alinhador.align(seq1, seq2)

print(f'Foram detectados {len(alinhamentos)} alinhamentos possiveis.')

# imprime o resultado em arquivo TXT
for alinhamento in alinhamentos:
    print("Score:", alinhamento.score)
    f = open('alinhamento.txt', 'a')
    print('Score: ',alinhamento.score,"\n",'\n',alinhamento, file = f)
    print(alinhamento)

# salva o resultado em um arquivo CSV
with open('alinhamento.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Query', 'Target', 'Score'])
    for alinhamento in alinhamentos:
       
        writer.writerow([alinhamento[0], alinhamento[1], alinhamento.score])