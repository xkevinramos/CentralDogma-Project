from my_module.functions import complement, transcribe, translate
import sys

test_template_strand = 'ATCTGACC'
test_dna_strand = 'TTCCATA'
test_rna_strand = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

def test_complement():
    print("Testing complement function...")
    assert isinstance(complement(test_template_strand), string)
    assert complement(test_template_strand) == 'TAGACTGG'


def test_transcribe():
    print("Testing transcribe function...")
    assert isinstance(transcribe(test_dna_strand), string)
    assert transcribe(test_dna_strand) == 'TTCCUTU'


def test_translate():
    print("Testing translate function...")
    assert isinstance(translate(test_rna_strand), string)
    assert translate(test_rna_strand) == 'MAMAPRTEINSTRING'


test_complement()
test_transcribe()
test_translation()

