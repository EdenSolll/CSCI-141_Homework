import node_types as node

def convert_to_nodes(dna: str) -> None | node.FrozenNode:
    """
    Recursively converts a string of DNA nucleotides into a linked list of nodes.

    Args:
        dna: A string of DNA nucleotides.

    Returns:
        None if the input string is empty, otherwise a FrozenNode object representing the first node in the linked list.
    """
    return None if not dna else node.FrozenNode(dna[0], convert_to_nodes(dna[1:]))

def convert_to_string(dna_seq: node.FrozenNode | None):
    """
    Converts a linked list of DNA sequence nodes to a string.

    Args:
        dna_seq: A linked list of DNA sequence nodes.

    Returns:
        A string representation of the DNA sequence.
    """
    return "" if not dna_seq else dna_seq.value + convert_to_string(dna_seq.next)

def length_rec(dna_seq: node.FrozenNode | None):
    """
    Recursively calculates the length of a DNA sequence represented as a linked list.

    Args:
        dna_seq: A linked list representing a DNA sequence.

    Returns:
        The length of the DNA sequence.
    """
    return 0 if not dna_seq else 1 + length_rec(dna_seq.next)

def is_match(dna_seq1: node.FrozenNode, dna_seq2: node.FrozenNode) -> bool:
    """
    Determines if two DNA sequences are a match by comparing their values.

    Args:
        dna_seq1 (node.FrozenNode): The first DNA sequence to compare.
        dna_seq2 (node.FrozenNode): The second DNA sequence to compare.

    Returns:
        bool: True if the sequences match, False otherwise.
    """
    return (lambda f:lambda a,b:f(f,a,b))(lambda f,a,b: ((b is None and a is None) if (a is None or b is None) else (a.value == b.value and f(f, a.next, b.next))))(dna_seq1,dna_seq2)

def is_pairing(dna_seq1: node.FrozenNode, dna_seq2: node.FrozenNode) -> bool:
    """
    Determines if two DNA sequences are complementary by checking if each nucleotide in one sequence pairs with its complementary nucleotide in the other sequence.

    Args:
    - dna_seq1: A FrozenNode representing the first DNA sequence.
    - dna_seq2: A FrozenNode representing the second DNA sequence.

    Returns:
    - A boolean value indicating whether the two DNA sequences are complementary.
    """
    return (lambda f:lambda a,b:f(f,a,b))(lambda f,a,b: ((b is None and a is None) if (a is None or b is None) else ((((a.value == "A" and b.value == "T") or (a.value == "T" and b.value == "A")) or ((a.value == "C" and b.value == "G") or (a.value == "G" and b.value == "C"))) and f(f, a.next, b.next))))(dna_seq1,dna_seq2)

def substitute(dna_seq1: node.FrozenNode | None, idx: int, base: str) -> node.FrozenNode | None:
    """
    Replaces the base at the given index with the given base in the given DNA sequence.

    Args:
    - dna_seq1: A FrozenNode representing the DNA sequence.
    - idx: An integer representing the index of the base to be replaced.
    - base: A string representing the base to replace the existing base at the given index.

    Returns:
    - A FrozenNode representing the new DNA sequence with the base replaced at the given index.
    """
    return [][0] if dna_seq1 is None or idx < 0 else node.FrozenNode(base, dna_seq1.next) if idx == 0 else node.FrozenNode(dna_seq1.value, substitute(dna_seq1.next, idx-1, base))

def insert_seq(dna_seq1: node.FrozenNode, dna_seq2: node.FrozenNode, idx: int) -> node.FrozenNode:
    """
    Inserts the second DNA sequence into the first DNA sequence at the specified index.

    Args:
        dna_seq1 (node.FrozenNode): The first DNA sequence.
        dna_seq2 (node.FrozenNode): The second DNA sequence to be inserted.
        idx (int): The index at which to insert the second DNA sequence.

    Returns:
        node.FrozenNode: The resulting DNA sequence after the insertion.
    """
    return [][0] if length_rec(dna_seq1) < idx else node.FrozenNode(dna_seq1.value, insert_seq(dna_seq1.next, dna_seq2, idx-1)) if idx != 0 else node.FrozenNode(dna_seq2.value, insert_seq(dna_seq1, dna_seq2.next, idx)) if dna_seq2 else dna_seq1

def delete_seq(dna_seq: node.FrozenNode, idx: int, segment_size: int) -> node.FrozenNode:
    """
    Deletes a segment of DNA sequence starting from the given index and of the given size.

    Args:
    dna_seq (node.FrozenNode): The DNA sequence to delete from.
    idx (int): The starting index of the segment to delete.
    segment_size (int): The size of the segment to delete.

    Returns:
    node.FrozenNode: The resulting DNA sequence after the deletion.
    """
    return dna_seq if segment_size == 0 else [][0] if length_rec(dna_seq) - idx < segment_size else delete_seq(dna_seq.next, idx, segment_size - 1) if idx == 0 else node.FrozenNode(dna_seq.value, delete_seq(dna_seq.next, idx-1, segment_size))

def duplicate_seq(dna_seq: node.FrozenNode, idx: int, segment_size: int) -> node.FrozenNode:
    """
    Returns a new DNA sequence with a segment of the original sequence duplicated and inserted at a specified index.

    Args:
    - dna_seq: a linked list representing a DNA sequence
    - idx: an integer representing the index where the duplicated segment should be inserted
    - segment_size: an integer representing the size of the segment to be duplicated

    Returns:
    - a new linked list representing the DNA sequence with the duplicated segment inserted at the specified index
    """
    return dna_seq if segment_size == 0 else [][0] if length_rec(dna_seq) - idx < segment_size else node.FrozenNode(dna_seq.value, duplicate_seq(dna_seq.next, idx-1, segment_size)) if idx != 0 else insert_seq(dna_seq, delete_seq(dna_seq, segment_size, length_rec(dna_seq) - segment_size), idx)
