# Baseline UDA
uda = dict(
    type='DACS_CDA',
    alpha=0.99,
    pseudo_threshold=0.968,
    pseudo_weight_ignore_top=0,
    pseudo_weight_ignore_bottom=0,
    imnet_feature_dist_lambda=0,
    imnet_feature_dist_classes=None,
    imnet_feature_dist_scale_min_ratio=None,
    mix='class',
    blur=True,
    color_jitter_strength=0.2,
    color_jitter_probability=0.2,
    debug_img_interval=1000,
    print_grad_magnitude=False,
    cda_level=None,
    cda_tgt_lambda=1,
    cheat_level={'attn': True, 'output': True},
    dacs_temp=-1,
    attn_sup_arch=None,
    attn_sup_patch_size=None,
    attn_sup_classes=None,
    valid_masking=False,
    attn_src_lambda="lambda x, y:0",
    attn_tgt_lambda="lambda x, y:0",
    attn_s2t_lambda="lambda x, y:0",
    attn_t2s_lambda="lambda x, y:0",
    attn_lambda=0,
    src_attn_tea=False,
)
use_ddp_wrapper = True