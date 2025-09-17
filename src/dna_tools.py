def count_nucleotides(sequence: str) -> dict:
    """Count nucleotides in a DNA sequence."""
    sequence = sequence.upper()
    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C"),
    }

if __name__ == "__main__":
    with open("../data/sample_dna.txt", "r") as f:
        dna = f.read().strip()
    print("DNA Sequence:", dna)
    print("Counts:", count_nucleotides(dna))
