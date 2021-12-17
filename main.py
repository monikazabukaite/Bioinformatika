import math

from Bio import SeqIO
from Bio.Seq import Seq

classes = ["B1", "B2", "B3", "B4", "M1", "M2", "M3", "M4"]
codons = "ARNDCEQGHILKMFPSTWYV"


def findDistance(a, b):
    return math.pow((a - b), 2)


def findSequences(sequence):
    sequences = []
    for i in range(0, 3):
        sequences.append([sequence.seq[(j + i) * 3:(j + i) * 3 + 3]
                         for j in range(len(sequence.seq) // 3)])
    return sequences


def filterSequences(filename):
    sequences = []
    for seq in SeqIO.parse("data/" + filename, "fasta"):
        for j in range(0, 3):
            if len(seq.seq[j:]) % 3 != 0:
                sequence = Seq(seq.seq[j:-(len(seq.seq[j:]) % 3)])
                sequences.append(sequence)
                sequences.append(sequence.reverse_complement())
            else:
                sequence = Seq(seq.seq[j:])
                sequences.append(sequence)
                sequences.append(sequence.reverse_complement())
    codingSequences = []
    for sequence in sequences:
        stopIndex = 0
        for k in range(0, len(sequence), 3):
            if k < stopIndex:
                continue
            if sequence[k:k + 3] == 'ATG':
                for j in range(k, len(sequence), 3):
                    if sequence[j:j + 3] == 'TAA' or sequence[j:j + 3] == 'TAG' or sequence[j:j + 3] == 'TGA':
                        if j + 3 - k >= 100:
                            codingSequences.append(
                                sequence[k:j + 3].translate())
                        stopIndex = j + 3
                        break
    return codingSequences


def calculateCodonFrequences(sequences):
    codonFrequencies = []
    for codon in codons:
        length = 0
        counter = 0
        for sequence in sequences:
            length += len(sequence)
            for k in range(len(sequence)):
                if sequence[k] == codon:
                    counter += 1
        codonFrequencies.append(counter / length)
    return codonFrequencies


def calculateDicodonFrequences(sequences):
    dicodonFrequencies = []
    for firstCodon in codons:
        for secondCodon in codons:
            counter = 0
            length = 0
            for sequence in sequences:
                length += len(sequence)
                for k in range(len(sequence) - 1):
                    if sequence[k] == firstCodon and sequence[k + 1] == secondCodon:
                        counter += 1
            dicodonFrequencies.append(counter / length)
    return dicodonFrequencies


def createMatrix(frequencies):
    matrix = [[0.0 for _ in range(8)] for _ in range(8)]
    for i in range(0, len(frequencies) - 1):
        for j in range(i + 1, len(frequencies)):
            counter = 0.0
            for k in range(len(frequencies[i])):
                counter += findDistance(frequencies[i][k], frequencies[j][k])
            matrix[i][j] = math.sqrt(counter)
            matrix[j][i] = matrix[i][j]
    return matrix


if __name__ == '__main__':
    codonFrequencies = []
    dicodonFrequencies = []

    for i in range(1, 5):
        codingSequences = filterSequences(
            "bacterial" + str(i) + ".fasta")
        codonFrequencies.append(calculateCodonFrequences(codingSequences))
        dicodonFrequencies.append(
            calculateDicodonFrequences(codingSequences))
    for i in range(1, 5):
        codingSequences = filterSequences(
            "mamalian" + str(i) + ".fasta")
        codonFrequencies.append(calculateCodonFrequences(codingSequences))
        dicodonFrequencies.append(
            calculateDicodonFrequences(codingSequences))

    codonMatrix = createMatrix(codonFrequencies)
    dicodonMatrix = createMatrix(dicodonFrequencies)

    print(len(codonMatrix))
    for distanceList in codonMatrix:
        print(classes[codonMatrix.index(distanceList)], end=" ")
        for distance in distanceList:
            print(distance, end=" ")
        print()

    print(len(dicodonMatrix))
    for distanceList in dicodonMatrix:
        print(classes[dicodonMatrix.index(distanceList)], end=" ")
        for distance in distanceList:
            print(distance, end=" ")
        print()
