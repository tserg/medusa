EXPECTED = [
    ("bare", {}),
    ("dead_store/call", {}),
    ("dead_store/annassign", {"Dead Store": 1}),
    ("dead_store/annassign_2", {"Dead Store": 1}),
]
