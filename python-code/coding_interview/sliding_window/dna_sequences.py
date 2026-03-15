def findRepeatedDnaSequences(s):
    answer = set()
    n = len(s)

    dna_seen_map = set()
    for i in range(0, n - 10):
        dna = s[i:i+10]
        if dna in dna_seen_map:
            answer.add(dna)
        else:
            dna_seen_map.add(dna)

    # Return the encoded list of numbers
    return list(answer)


input1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
result1 = findRepeatedDnaSequences(input1)
print(result1)

input2 = "AAAAAAAAAAAAA"
result2 = findRepeatedDnaSequences(input2)
print(result2)