EXPECTED = [
    ("bare", {}),
    ("dead_store/call", {}),
    ("dead_store/annassign", {"Dead Store": 1}),
    ("dead_store/annassign_2", {"Dead Store": 1}),
    ("unused_param/single", {"Unused Function Parameter": 1}),
    ("unused_param/double", {"Unused Function Parameter": 2}),
    ("unused_param/double_alt", {"Unused Function Parameter": 1}),
    ("unused_param/namespace_single", {"Unused Function Parameter": 1}),
    ("unused_param/nested_namespace_single", {"Unused Function Parameter": 1}),
]
