def complement(template_strand):
    """
    Computes the complement strand of the given template strand.

    Parameters
    ----------
    template_strand : string
        The template strand we are evaluating.

    Returns
    -------
    complement_strand : string
        The resulting string after finding the complement for each nucleotide.
    """

    # Empty string to store the complement of the template strand
    complement_strand = ''

    complement_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    # For each nucleotide in the sequence, add its complement to a new string
    for char in template_strand:

        # Append the complement of the current nucleotide using our dictionary complement_dict
        complement_strand += complement_dict[char]

    return complement_strand


def transcribe(dna_sequence):
    """
    Computes the RNA strand produced from a given DNA sequence.

    Parameters
    ----------
    dna_sequence : string
        The DNA sequence we are evaluating.

    Returns
    -------
    rna_strand :
        The result of replacing all instances of 'A' with a 'U' in the given DNA sequence.
    """
    # Use the python function replace to replace instances of 'A' with 'U'
    rna_strand = dna_sequence.replace('A', 'U')

    return rna_strand


def translate(rna_sequence):
    """
    Compute the protein that will be produced by the given RNA sequence.

    Parameters
    ----------
    rna_sequence : string
        The RNA strand we are evaluating.

    Returns
    -------
    protein : string
        The resulting protein from evaluating the codons in the RNA strand.
    """

    rna_codon = { "UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
                  "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
                  "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
                  "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
                  "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
                  "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
                  "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
                  "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
                  "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
                  "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
                  "UAA" : "STOP", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
                  "UAG" : "STOP", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
                  "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
                  "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
                  "UGA" : "STOP", "CGA" : "R", "AGA" : "R", "GGA" : "G",
                  "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G"}

    # Contains the three stop codons that terminate the translation process
    stop_codon = ['UAA', 'UAG', 'UGA']

    # String that stores the protein being formed
    protein = ''

    # Iterate through the rna sequence in steps of 3 to analyze one codon at a time
    for i in range(0, len(rna_sequence), 3):
        # Look at the next 3 nucleotides from our starting point
        codon = rna_sequence[i:i + 3]

        # This condition terminates translation if the codon is one of the three termination codons
        if codon in stop_codon:
            break

        # Add the amino acid for the current codon to our protein string
        protein += rna_codon[codon]

    return protein
