"""
Simple bioinformatics functions for sequence analysis
"""

def calculate_gc_content(sequence):
    """
    Calculate GC content percentage of a DNA sequence
    
    Args:
        sequence (str): DNA sequence string
    
    Returns:
        float: GC content as percentage
    """
    if not sequence:
        return 0.0
    
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100


def reverse_complement(sequence):
    """
    Return the reverse complement of a DNA sequence
    
    Args:
        sequence (str): DNA sequence string
    
    Returns:
        str: Reverse complement sequence
    """
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    sequence = sequence.upper()
    rev_comp = ''.join([complement.get(base, base) for base in sequence[::-1]])
    return rev_comp
