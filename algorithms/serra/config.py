"""Config for the Structural Features algorithm."""

# Serra params
config = {
    "niter"             :   200,
    "alphaZ"            :   -0.01,
    "normalize_frames"  :   True,
    "viterbi_segmenter" :   True,
    "min_segment_length":   32
}

algo_id = "serra"
is_boundary_type = True
is_label_type = False