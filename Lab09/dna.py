import node_types as node

def convert_to_nodes(dna: str) -> None | node.FrozenNode:
    return None if not dna else node.FrozenNode(dna[0], convert_to_nodes(dna[1:]))

def convert_to_string(dna_seq: node.FrozenNode | None):
    return "" if not dna_seq else dna_seq.value + convert_to_string(dna_seq.next)

def length_rec(dna_seq: node.FrozenNode | None):
    return 0 if not dna_seq else 1 + length_rec(dna_seq.next)

def is_match(dna_seq1: node.FrozenNode, dna_seq2: node.FrozenNode) -> bool:
    return (lambda f:lambda a,b:f(f,a,b))(lambda f,a,b: ((b is None and a is None) if (a is None or b is None) else (a.value == b.value and f(f, a.next, b.next))))(dna_seq1,dna_seq2)

def is_pairing(dna_seq1: node.FrozenNode, dna_seq2: node.FrozenNode) -> bool:
    return (lambda f:lambda a,b:f(f,a,b))(lambda f,a,b: ((b is None and a is None) if (a is None or b is None) else ((((a.value == "A" and b.value == "T") or (a.value == "T" and b.value == "A")) or ((a.value == "C" and b.value == "G") or (a.value == "G" and b.value == "C"))) and f(f, a.next, b.next))))(dna_seq1,dna_seq2)

def substitute(dna_seq1: node.FrozenNode | None, idx: int, base: str):
    return [][0] if dna_seq1 is None or idx < 0 else node.FrozenNode(base, dna_seq1.next) if idx == 0 else node.FrozenNode(dna_seq1.value, substitute(dna_seq1.next, idx-1, base))

def insert_seq(dna_seq1, dna_seq2, idx):
    return [][0] if length_rec(dna_seq1) < idx else node.FrozenNode(dna_seq1.value, insert_seq(dna_seq1.next, dna_seq2, idx-1)) if idx != 0 else node.FrozenNode(dna_seq2.value, insert_seq(dna_seq1, dna_seq2.next, idx)) if dna_seq2 else dna_seq1

def delete_seq(dna_seq, idx, segment_size):
    return dna_seq if segment_size == 0 else [][0] if length_rec(dna_seq) - idx < segment_size else delete_seq(dna_seq.next, idx, segment_size - 1) if idx == 0 else node.FrozenNode(dna_seq.value, delete_seq(dna_seq.next, idx-1, segment_size))

def duplicate_seq(dna_seq, idx, segment_size):
    return dna_seq if segment_size == 0 else [][0] if length_rec(dna_seq) - idx < segment_size else node.FrozenNode(dna_seq.value, duplicate_seq(dna_seq.next, idx-1, segment_size)) if idx != 0 else insert_seq(dna_seq, delete_seq(dna_seq, segment_size, length_rec(dna_seq) - segment_size), idx)
