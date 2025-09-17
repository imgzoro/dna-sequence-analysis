from src.dna_tools import count_nucleotides

def test_count_nucleotides():
    result = count_nucleotides("AAGT")
    assert result == {"A": 2, "T": 1, "G": 1, "C": 0}
