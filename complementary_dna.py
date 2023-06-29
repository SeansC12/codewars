def DNA_strand(dna):
    a_t = {"A": "T", "T": "A"}
    c_g = {"C": "G", "G": "C"}
    solution = list()

    for char in dna:
        if char in "AT":
            solution.append(a_t[char])
        else:
            solution.append(c_g[char])
    return "".join(solution)
print(DNA_strand("ATTGC"))