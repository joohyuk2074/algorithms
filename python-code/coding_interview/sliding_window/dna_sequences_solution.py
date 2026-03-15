def findRepeatedDnaSequences(s):
    to_int = {"A": 0, "C": 1, "G": 2, "T": 3}
    encoded_sequence = [to_int[c] for c in s]
    
    k, n = 10, len(s)
    
    if n <= k:
        return []
        
    a = 4
    h = 0  
    seen_hashes, output = set(), set()  
    a_k = 1 

    for i in range(k):
        h = h * a + encoded_sequence[i]
        a_k *= a  

    seen_hashes.add(h)  

    for start in range(1, n - k + 1):
        h = h * a - encoded_sequence[start - 1] * a_k + encoded_sequence[start + k - 1]

        if h in seen_hashes:
            output.add(s[start : start + k])
        else:
            seen_hashes.add(h)

    return list(output)  

# Driver code
def main():
    test_cases = [
        "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
        "AAAAAAAAAAAAA",
        "ACGTACGTACGTACGTACGTACGTACGTACGT",
        "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
        "GTACGTACGTACGCCCCCCCCGGGGG",
    ]
    
    for i, s in enumerate(test_cases):
        print(f'{i+1}.\tInput: "{s}"')
        print(f"\n\tOutput: {findRepeatedDnaSequences(s)}")
        print("-" * 100)

if __name__ == "__main__":
    main()