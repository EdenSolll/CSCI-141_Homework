import immutable_extra as extra
import node_types as node

def convert_to_nodes(dna: str) -> None | node.FrozenNode:
    return None if dna == "" else node.FrozenNode(dna[0], convert_to_nodes((dna[1:])))

def convert_to_string(dna_seq):
    return "" if dna_seq is None else "" + dna_seq.value, convert_to_string(dna_seq.next)

def length_rec(dna_seq):
    return 0 if dna_seq is None else 1 + length_rec(dna_seq.next)

def is_match(dna_seq1: node.FrozenNode, dna_seq2: node.FrozenNode) -> bool:
    return (lambda f:lambda a,b:f(f,a,b))(lambda f,a,b: ((b is None and a is None) if (a is None or b is None) else (a.value == b.value and f(f, a.next, b.next))))(dna_seq1,dna_seq2)

def is_pairing(dna_seq1: node.FrozenNode, dna_seq2: node.FrozenNode) -> bool:
    return (lambda f:lambda a,b:f(f,a,b))(lambda f,a,b: ((b is None and a is None) if (a is None or b is None) else (((a.value == "A" and b.value == "T") or (a.value == "T" and b.value == "A")) and f(f, a.next, b.next))))(dna_seq1,dna_seq2)
