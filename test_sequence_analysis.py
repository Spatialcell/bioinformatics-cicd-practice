"""
Tests for sequence analysis functions
"""

from sequence_analysis import calculate_gc_content, reverse_complement


def test_gc_content_basic():
    """Test basic GC content calculation"""
    assert calculate_gc_content("ATGC") == 50.0
    assert calculate_gc_content("AAAA") == 0.0
    assert calculate_gc_content("GGCC") == 100.0


def test_gc_content_case_insensitive():
    """Test that function handles lowercase"""
    assert calculate_gc_content("atgc") == 50.0
    assert calculate_gc_content("AtGc") == 50.0


def test_gc_content_empty():
    """Test empty sequence"""
    assert calculate_gc_content("") == 0.0


def test_reverse_complement_basic():
    """Test basic reverse complement"""
    assert reverse_complement("ATGC") == "GCAT"
    assert reverse_complement("AAAA") == "TTTT"
    assert reverse_complement("GCTA") == "TAGC"


def test_reverse_complement_case_insensitive():
    """Test reverse complement with lowercase"""
    assert reverse_complement("atgc") == "GCAT"
