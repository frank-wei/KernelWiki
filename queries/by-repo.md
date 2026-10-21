# Query: By Repository

> Auto-generated. Do not edit manually.

<a id="dao-ailabflash-attention"></a>
## Dao-AILab/flash-attention
71 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#2960](../sources/prs/flash-attention/PR-2960.md) | [Cute, Sm100] bwd postprocess: load 2-CTA dQaccum directly into registers | 2026-10-04 |  | tmem |
| [#2962](../sources/prs/flash-attention/PR-2962.md) | [CuTe, SM100] Unify hd256 forward and recover the remaining stack | 2026-10-04 | pipeline-stages | mla, tma, tmem |
| [#2964](../sources/prs/flash-attention/PR-2964.md) | [CuTe, SM100] Unify hd256 backward (1/5): tests first, named 2CTA schedules and TMEM widths | 2026-10-04 | pipeline-stages | tmem |
| [#2965](../sources/prs/flash-attention/PR-2965.md) | [CuTe, SM100] Unify hd256 backward (2/5): 64-row KV tile per CTA (M=64 TMEM layout) with GQA, varlen and deterministic support | 2026-10-04 | pipeline-stages, swizzling | tcgen05, tma, tmem |
| [#2966](../sources/prs/flash-attention/PR-2966.md) | [CuTe, SM100] Unify hd256 backward (3/5): hdim 256 on FlashAttentionBackwardSm100 (opt-in) | 2026-10-04 | pipeline-stages, swizzling | reduction, tmem |
| [#2940](../sources/prs/flash-attention/PR-2940.md) | Fix lint failure | 2026-09-30 |  |  |
| [#2938](../sources/prs/flash-attention/PR-2938.md) | [Cute, Sm100] 1CTA MLA forward (dense + sparse top-k), MLA dispatch heuristic, sparse MLA backward at any head count | 2026-09-29 | pipeline-stages, swizzling, tile-scheduling | attention, clc, fp8 |
| [#2928](../sources/prs/flash-attention/PR-2928.md) | [CuTe, SM100] S/P ping-pong to overlap QK with softmax in decode | 2026-09-27 | pipeline-stages | attention, flash-attention, gemm |
| [#2917](../sources/prs/flash-attention/PR-2917.md) | [CuTe, SM100] hd256 fwd: derive lengths and KV ranges from BlockInfo/SeqlenInfoQK | 2026-09-25 | pipeline-stages | clc |
| [#2906](../sources/prs/flash-attention/PR-2906.md) | [CuTe, SM100] Write real zeros for block-sparse empty tiles | 2026-09-22 |  | attention, gemm, tcgen05 |
| [#2883](../sources/prs/flash-attention/PR-2883.md) | [CuTe, SM100] Support 1..128 Q heads in sparse MLA via in-kernel TMA padding | 2026-09-12 | pipeline-stages | attention, gemm, mla |
| [#2880](../sources/prs/flash-attention/PR-2880.md) | [CuTe, SM100] Preserve hd256 output alignment for vectorized stores | 2026-09-11 | pipeline-stages | attention |
| [#2867](../sources/prs/flash-attention/PR-2867.md) | One more deprecation; | 2026-09-08 |  |  |
| [#2816](../sources/prs/flash-attention/PR-2816.md) | [CuTe, SM100] Sparse MLA bwd: in-kernel recompute-P + token-chunked backward | 2026-08-24 | pipeline-stages, swizzling | gemm, mbarrier, mla |
| [#2807](../sources/prs/flash-attention/PR-2807.md) | [CuTe, SM100, HD256] optimize SM100 HD256 varlen scheduling and epilogues | 2026-08-18 | tile-scheduling | attention, flash-attention, tma |
| [#2804](../sources/prs/flash-attention/PR-2804.md) | [CuTe] Speed up SM100 hdim-64 bwd: dedicated P/dS TMEM slots + per-warp signaling | 2026-08-17 | pipeline-stages, tile-scheduling | mbarrier, reduction, tcgen05 |
| [#2775](../sources/prs/flash-attention/PR-2775.md) | [CuTe, Fwd] Fix PackGQA predication for padded head dimensions | 2026-08-09 |  | tma |
| [#2763](../sources/prs/flash-attention/PR-2763.md) | [CuTe, SM80/SM120] Guard invalid varlen forward tiles | 2026-08-07 |  |  |
| [#2768](../sources/prs/flash-attention/PR-2768.md) | Add an Attention Sink to Flash MLA for SM100 | 2026-08-07 |  | attention, fp8, mla |
| [#2755](../sources/prs/flash-attention/PR-2755.md) | [CuTe, SM100] Sparse MLA bwd: don't scatter dK/dV at -1 sentinel indices | 2026-08-04 |  | mla, reduction, topk |
| [#2745](../sources/prs/flash-attention/PR-2745.md) | [CuTe] Fix forward dynamic-shape correctness | 2026-07-29 | persistent-kernel | tma |
| [#2706](../sources/prs/flash-attention/PR-2706.md) | [Cute, bwd, sm90/100/110] Support learnable sink in backward | 2026-07-13 |  |  |
| [#2698](../sources/prs/flash-attention/PR-2698.md) | [CuTe,Bwd,Sm100] Support head_dim not a multiple of 32 in backward | 2026-07-09 |  | tcgen05, tma, tmem |
| [#2696](../sources/prs/flash-attention/PR-2696.md) | add tcgen.ld.red support to sm103a arch | 2026-07-06 |  | attention, flash-attention, fp4 |
| [#2692](../sources/prs/flash-attention/PR-2692.md) | add linearize scheduling to combine kernel for full cudagraph | 2026-07-01 | tile-scheduling | attention, flash-attention |
| [#2670](../sources/prs/flash-attention/PR-2670.md) | fix(hd256/sm100): forward reads actual input strides, drop .contiguous() patch | 2026-06-21 |  | attention |
| [#2671](../sources/prs/flash-attention/PR-2671.md) | Fix CuTe SM120 compile-time argument handling | 2026-06-21 |  |  |
| [#2669](../sources/prs/flash-attention/PR-2669.md) | Expand FLASHATTENTION_DISABLE_DROPOUT to not bring in unneeded headers | 2026-06-20 |  | attention, flash-attention |
| [#2661](../sources/prs/flash-attention/PR-2661.md) | Enable 2CTA for SM100 block-sparse backward | 2026-06-16 | pipeline-stages | attention, mbarrier, mla |
| [#2656](../sources/prs/flash-attention/PR-2656.md) | [NVIDIA][CuTe,Fwd,sm120] Implement Pack-GQA on SM120 (+ graceful SplitKV fallback) | 2026-06-15 |  |  |
| [#2627](../sources/prs/flash-attention/PR-2627.md) | [CuTe] Fix lint failure in flash_bwd_sm100.py | 2026-06-04 |  |  |
| [#2621](../sources/prs/flash-attention/PR-2621.md) | [Cute,Bwd,Sm100] add sparse MLA (Deepseek v4) backward kernels | 2026-06-03 | pipeline-stages, swizzling, tile-scheduling | attention, clc, gemm |
| [#2616](../sources/prs/flash-attention/PR-2616.md) | Add aux-scalars to interface to enable dynamic ints and floats in expressions | 2026-06-01 |  | attention |
| [#2602](../sources/prs/flash-attention/PR-2602.md) | NFC: replace deprecated APIs: cute.make_fragment and cute.core.ThrMma | 2026-05-29 |  |  |
| [#2558](../sources/prs/flash-attention/PR-2558.md) | [CuTe,Fwd,Sm100] refactor mla sm100 forward and add page table | 2026-05-13 |  | attention, flash-attention, mla |
| [#2559](../sources/prs/flash-attention/PR-2559.md) | [CuTe,Sm100] Varlen Dynamic Persistent scheduler and metadata | 2026-05-13 | persistent-kernel, pipeline-stages, swizzling | attention, clc, flash-attention |
| [#2557](../sources/prs/flash-attention/PR-2557.md) | [CuTe,Bwd,Sm100] allow 2cta with score mod and mask mod in bwd | 2026-05-12 |  |  |
| [#2497](../sources/prs/flash-attention/PR-2497.md) | [FA4][hd256] Backward TMA bulk-store epilogue + LSE/dpsum coalesce | 2026-04-27 |  | clc, tcgen05, tma |
| [#2488](../sources/prs/flash-attention/PR-2488.md) | [hd256] Improve forward kernel with exp2 FMA emulation (3% to 9% performance gain) | 2026-04-23 | pipeline-stages | attention, flash-attention, quantization |
| [#2489](../sources/prs/flash-attention/PR-2489.md) | [hd256] Add TMA paged KV support to SM100 2CTA forward kernel | 2026-04-23 |  | quantization, tma |
| [#2441](../sources/prs/flash-attention/PR-2441.md) | [Cute,Sm100,Fwd] add MLA 64/512 with topk sparsity for MQA 128 heads | 2026-04-06 | persistent-kernel, pipeline-stages | mla, tcgen05, topk |
| [#2412](../sources/prs/flash-attention/PR-2412.md) | Feat([FA4][CUTE DSL]) Add head_dim=256 support (forward + backward) | 2026-03-30 | persistent-kernel, pipeline-stages, swizzling | attention, clc, flash-attention |
| [#2360](../sources/prs/flash-attention/PR-2360.md) | [Fwd,Sm90] Add paged KV attention support (tma and cp.async) | 2026-03-17 | pipeline-stages | attention, mbarrier, tma |
| [#2333](../sources/prs/flash-attention/PR-2333.md) | Add SM120 varlen attention support | 2026-03-12 | tile-scheduling | attention |
| [#2261](../sources/prs/flash-attention/PR-2261.md) | [Cute,Flex,Sm100] vectorized mask_mod | 2026-02-17 |  |  |
| [#2218](../sources/prs/flash-attention/PR-2218.md) | [Ai-assisted] CLC work stealing | 2026-01-31 | pipeline-stages, swizzling, tile-scheduling | clc, mbarrier, tma |
| [#2186](../sources/prs/flash-attention/PR-2186.md) | [Cute,Fwd,Sm100] support irregular qhead / kvhead ratios | 2026-01-16 | pipeline-stages | attention, flash-attention, tma |
| [#2145](../sources/prs/flash-attention/PR-2145.md) | [CUTE][SM90]Enable pack-gqa with broadcasted maskmods | 2026-01-07 | pipeline-stages |  |
| [#2109](../sources/prs/flash-attention/PR-2109.md) | [Cute,Fwd,Sm100] fp8 e4m3 and e5m2 support | 2025-12-29 |  | attention, flash-attention, fp8 |
| [#2104](../sources/prs/flash-attention/PR-2104.md) | [Cute,Fwd,Sm100] distributed offset calculation for paged KV | 2025-12-28 |  | attention |
| [#2085](../sources/prs/flash-attention/PR-2085.md) | Add blocksparse support for bwd on blackwell | 2025-12-17 | pipeline-stages | attention, tma |
| [#2070](../sources/prs/flash-attention/PR-2070.md) | Add score-mod bwd support  | 2025-12-15 |  | tmem |
| [#2043](../sources/prs/flash-attention/PR-2043.md) | [Cute,Fwd] Extend score_mod to variable sequence length | 2025-12-03 |  |  |
| [#2033](../sources/prs/flash-attention/PR-2033.md) | [Cute,Bwd,Sm100] enable deterministic mode for sm100 bwd and fix race conditions | 2025-11-24 | tile-scheduling | tcgen05, tmem |
| [#2014](../sources/prs/flash-attention/PR-2014.md) | [Cute,Sm100,Fwd] use correction warps for epi when not using TMA | 2025-11-15 | tile-scheduling | tma |
| [#1999](../sources/prs/flash-attention/PR-1999.md) | [Cute,Fwd,Sm100] Support paged attention | 2025-11-11 | pipeline-stages | attention, flash-attention, tma |
| [#1985](../sources/prs/flash-attention/PR-1985.md) | [Cute] Block sparse support Sm100 | 2025-11-05 | pipeline-stages | attention, flash-attention, sparse-attention |
| [#1945](../sources/prs/flash-attention/PR-1945.md) | Blackwell FlashAttention-BWD (v1.0) | 2025-10-19 | pipeline-stages, swizzling, tile-scheduling | flash-attention, gemm, tcgen05 |
| [#1940](../sources/prs/flash-attention/PR-1940.md) | [Cute,Fwd,Sm100] Implement SplitKV | 2025-10-15 | persistent-kernel, tile-scheduling | attention, gemm, tcgen05 |
| [#1934](../sources/prs/flash-attention/PR-1934.md) | feat: Adding varlen support to cute-dsl sm80 bwd | 2025-10-13 | tile-scheduling | attention, flash-attention |
| [#1893](../sources/prs/flash-attention/PR-1893.md) | Improve causal backward determinism perf with SPT schedule | 2025-09-17 | swizzling, tile-scheduling |  |
| [#1823](../sources/prs/flash-attention/PR-1823.md) | Add sorting and head swizzle to varlen scheduler | 2025-08-19 | swizzling, tile-scheduling | sort |
| [#1604](../sources/prs/flash-attention/PR-1604.md) | Support hdimQK != hdimV backward | 2025-04-21 |  |  |
| [#1361](../sources/prs/flash-attention/PR-1361.md) | Fix FA3 Varlen Performance regression | 2024-11-29 | pipeline-stages | attention, flash-attention, tma |
| [#1331](../sources/prs/flash-attention/PR-1331.md) | FA3 paged attention: Readiness for Cutlass 3.6 / default value for block_table | 2024-11-12 |  | attention, flash-attention, gemm |
| [#1268](../sources/prs/flash-attention/PR-1268.md) | Paged Attention support for FA3 | 2024-10-10 |  | attention, flash-attention, fp8 |
| [#1236](../sources/prs/flash-attention/PR-1236.md) | FA3 kvcache + split kv + gqa parallelization | 2024-09-18 | tile-scheduling | fp8, gemm, tma |
| [#1233](../sources/prs/flash-attention/PR-1233.md) | Add local attention in Hopper FAv3 | 2024-09-16 |  | attention, fp8 |
| [#1173](../sources/prs/flash-attention/PR-1173.md) | FA3 FP8 qkv descales + restore max offset for h128 causal + added sync for producer WG | 2024-08-23 |  | fp8, gemm |
| [#1100](../sources/prs/flash-attention/PR-1100.md) | Fp8 kernel with "in-kernel" transpose of V in producer | 2024-07-26 | pipeline-stages, swizzling, tile-scheduling | attention, fp8, gemm |
| [#1072](../sources/prs/flash-attention/PR-1072.md) | Add var-seq-len to FA3 fp16 / bf16 fwd | 2024-07-19 |  | tma |

<a id="dao-ailabquack"></a>
## Dao-AILab/quack
6 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#181](../sources/prs/quack/PR-181.md) | Revert electone clean up in PR-#164 | 2026-07-23 |  |  |
| [#174](../sources/prs/quack/PR-174.md) | Bump CuTe-DSL to 4.6.1 | 2026-07-16 | tile-scheduling | attention, flash-attention |
| [#170](../sources/prs/quack/PR-170.md) | [GEMM] Full blockscaled MXFP4/6/8 QMMA and MXFP4/NVFP4 OMMA support for SM100 GEMM | 2026-07-10 |  | block-scale, fp4, fp6 |
| [#164](../sources/prs/quack/PR-164.md) | Avoid pre-electing bulk G2S copies | 2026-06-30 |  | attention, flash-attention, tma |
| [#158](../sources/prs/quack/PR-158.md) | [GEMM] Add SplitK Serial,Parallel,Separate modes to all GEMM classes and dtypes | 2026-06-16 | pipeline-stages, stream-k, tile-scheduling | block-scale, clc, fp8 |
| [#133](../sources/prs/quack/PR-133.md) | [Bug fix]: Fix the SwiGLU/dSwiGLU bug for the (2, 2) epilogue layout | 2026-05-07 |  | gemm, tmem |

<a id="hazyresearchthunderkittens"></a>
## HazyResearch/ThunderKittens
5 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#210](../sources/prs/ThunderKittens/PR-210.md) | Add FP8-output and FP4-output Vera Rubin GEMMs | 2026-09-12 | pipeline-stages, swizzling | block-scale, clc, fp4 |
| [#208](../sources/prs/ThunderKittens/PR-208.md) | Add SM107 support and Vera Rubin FP8/NVFP4 GEMMs | 2026-09-10 | swizzling | block-scale, clc, fp4 |
| [#209](../sources/prs/ThunderKittens/PR-209.md) | Fix compiler ordering around mbarrier waits | 2026-09-10 |  | mbarrier |
| [#201](../sources/prs/ThunderKittens/PR-201.md) | Add SM103 NVFP4 K96 tcgen05 support and B300 GEMM sample | 2026-06-05 | pipeline-stages, swizzling | block-scale, clc, fp4 |
| [#198](../sources/prs/ThunderKittens/PR-198.md) | Use XOR shuffles for register tile reductions | 2026-05-25 |  | reduction |

<a id="nvidiatensorrt-llm"></a>
## NVIDIA/TensorRT-LLM
365 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#20477](../sources/prs/TensorRT-LLM/PR-20477.md) | [https://nvbugs/6939562][fix] Bound module_out_sizes read in LoRA param-fill kernel | 2026-10-16 |  |  |
| [#20390](../sources/prs/TensorRT-LLM/PR-20390.md) | [None][perf] GLM-5.3-Flash C++ kernel speedups: vectorized FP8 1x128 quant and 288-expert router GEMM | 2026-10-15 | pipeline-stages | block-scale, fp8, gemm |
| [#20405](../sources/prs/TensorRT-LLM/PR-20405.md) | [TRTLLM-17109][perf] Reduce Gemma multimodal attention mask construction peak memory | 2026-10-15 |  | attention, flash-attention |
| [#20251](../sources/prs/TensorRT-LLM/PR-20251.md) | [None][perf] Score only visible pools on BF16 tensor cores in the GLM-5.3-Flash indexer | 2026-10-14 |  | attention, sort, sparse-attention |
| [#20271](../sources/prs/TensorRT-LLM/PR-20271.md) | [https://nvbugs/6905381][fix] Fix CUDA-core GEMM launch for wide FP8 outputs | 2026-10-14 |  | fp8, gemm |
| [#20290](../sources/prs/TensorRT-LLM/PR-20290.md) | [None][fix] Reduce deterministic GVR V2 top-K overflow overhead | 2026-10-14 |  | attention, topk |
| [#20181](../sources/prs/TensorRT-LLM/PR-20181.md) | [None][feat] CUTEDSL: switch the Rubin NVFP4 FC1 weight layout to gate16/up16 | 2026-10-13 | swizzling | block-scale, fp4, fp8 |
| [#20190](../sources/prs/TensorRT-LLM/PR-20190.md) | [TRTLLM-16460][fix] indexer K-cache gather/scatter: compute the contiguous-side offset in 64 bits | 2026-10-13 |  | fp8 |
| [#20205](../sources/prs/TensorRT-LLM/PR-20205.md) | [None][chore] Remove ArrayView and use `std::span` instead | 2026-10-13 |  | block-scale, moe, topk |
| [#20214](../sources/prs/TensorRT-LLM/PR-20214.md) | [TRTLLM-15864][chore] Consolidate the VisualGen attention domain under _torch/visual_gen/attention/ | 2026-10-13 | pipeline-stages | attention, flash-attention, sparse-attention |
| [#20223](../sources/prs/TensorRT-LLM/PR-20223.md) | [None][fix] Size the Blackwell spec-dec tree mask for the SwapsMmaAb kernel layout | 2026-10-13 | pipeline-stages | attention, flash-attention |
| [#20147](../sources/prs/TensorRT-LLM/PR-20147.md) | [TRTLLM-16780][feat] Honor per-request seeds in one-model speculative decoding's acceptance step | 2026-10-12 | kernel-fusion | scan, topk |
| [#20155](../sources/prs/TensorRT-LLM/PR-20155.md) | [None][chore] Refresh PrimTS vendor source onto FlashInfer main | 2026-10-12 | pipeline-stages, swizzling | attention, flash-attention, fp4 |
| [#20100](../sources/prs/TensorRT-LLM/PR-20100.md) | [None][feat] Deterministic mode for the self-sampling GVR V2 top-K decode (fp32) | 2026-10-11 |  | attention, sort, sparse-attention |
| [#20084](../sources/prs/TensorRT-LLM/PR-20084.md) | [None][perf] Avoid cuBLAS's fallback in the KDA prefill projection | 2026-10-10 |  | fp8, gemm, tma |
| [#19960](../sources/prs/TensorRT-LLM/PR-19960.md) | [None][feat] Kimi K3 optimizations on Rubin | 2026-10-08 | double-buffering, kernel-fusion | attention, fp4, fp8 |
| [#19873](../sources/prs/TensorRT-LLM/PR-19873.md) | [None][fix] Add a static tile scheduler override for context FMHA | 2026-10-06 | persistent-kernel, tile-scheduling | attention, flash-attention, mla |
| [#19860](../sources/prs/TensorRT-LLM/PR-19860.md) | [None][fix] Align GDN recurrent Q/K normalization with prefill | 2026-10-05 |  |  |
| [#19829](../sources/prs/TensorRT-LLM/PR-19829.md) | [None][fix] Kimi K3 attn_res kernels: order the ws_stats reads and fence the slot releases | 2026-10-02 | double-buffering, kernel-fusion, persistent-kernel | attention, mbarrier, tma |
| [#19830](../sources/prs/TensorRT-LLM/PR-19830.md) | [None][fix] kdaDecode legacy: __syncwarp before the lane-0 block-reduce stores | 2026-10-02 |  | reduction |
| [#19753](../sources/prs/TensorRT-LLM/PR-19753.md) | [TRTLLM-16404][fix] restore CUTLASS MoE compatibility and early feature checks | 2026-10-01 |  | fp4, gemm, moe |
| [#19772](../sources/prs/TensorRT-LLM/PR-19772.md) | [None][perf] Fuse MiniMax-H3 AdaLN RMSNorm with per-token modulation | 2026-10-01 | pipeline-stages | attention, fp4, fp8 |
| [#19719](../sources/prs/TensorRT-LLM/PR-19719.md) | [TRTLLM-16708][feat] Honor per-request seeds in batched TorchSampler sampling via the fused kernel | 2026-09-30 | kernel-fusion, pipeline-stages |  |
| [#19727](../sources/prs/TensorRT-LLM/PR-19727.md) | [TRTLLM-16621][feat] Support DeepSeek-V4.1-Flash | 2026-09-30 |  | attention, flash-attention, fp4 |
| [#19682](../sources/prs/TensorRT-LLM/PR-19682.md) | [None][perf] MoE routing: small-token single-block kernel for <= 8 tokens in the trtllm-gen custom routing | 2026-09-29 | kernel-fusion | fp4, gemm, grouped-gemm |
| [#19650](../sources/prs/TensorRT-LLM/PR-19650.md) | [None][perf] Fill the KVCM2 host tier progressively | 2026-09-28 |  |  |
| [#19581](../sources/prs/TensorRT-LLM/PR-19581.md) | [None][fix] wait for K1 readers before reusing KDA prefill stages | 2026-09-23 |  | tma |
| [#19539](../sources/prs/TensorRT-LLM/PR-19539.md) | [None][chore] CUTEDSL_FC12 phase-specific smem AB stages with FC2 epilogue overlay | 2026-09-22 | kernel-fusion, pipeline-stages | block-scale, fp4, moe |
| [#19477](../sources/prs/TensorRT-LLM/PR-19477.md) | [TRTLLMINF-391][infra] Upgrade public PyTorch to 2.14 and integrate Triton 3.8 | 2026-09-21 | persistent-kernel, swizzling | block-scale, fp4, fp8 |
| [#19488](../sources/prs/TensorRT-LLM/PR-19488.md) | [None][chore] enable cutedsl rubin fc1 swiglu clamp | 2026-09-21 |  | fp4, moe, nvfp4 |
| [#19502](../sources/prs/TensorRT-LLM/PR-19502.md) | [TRTLLM-16283][feat] Prepare DeepSeek V4 attention for sparse KV offload | 2026-09-21 |  | attention, flash-attention, fp8 |
| [#19446](../sources/prs/TensorRT-LLM/PR-19446.md) | [None][perf] PDL on the missing decode edges | 2026-09-20 |  | gemm, tma |
| [#19385](../sources/prs/TensorRT-LLM/PR-19385.md) | [TRTLLM-16498][fix] Avoid full KV pool casts in Triton prefill | 2026-09-18 |  | attention, fp8 |
| [#19391](../sources/prs/TensorRT-LLM/PR-19391.md) | [TRTLLM-16857][feat] Add RoPE precision options to NVFP4 cold-page compression | 2026-09-18 |  | attention, block-scale, fp4 |
| [#19422](../sources/prs/TensorRT-LLM/PR-19422.md) | [None][perf] Add MiniMax-M3 NVFP4 KV cache support | 2026-09-18 | swizzling | attention, block-scale, fp4 |
| [#19338](../sources/prs/TensorRT-LLM/PR-19338.md) | [None][feat] Upgrade Blackwell cuteDSL MLA kernel for packed q heads and compact input | 2026-09-17 |  | attention, fp8, mla |
| [#19361](../sources/prs/TensorRT-LLM/PR-19361.md) | [None][fix] Add SM107 (Rubin) to SM100-family support statements; gate W4A8 NVFP4 FP8 MoE to SM100/103 | 2026-09-17 |  | attention, flash-attention, fp4 |
| [#19249](../sources/prs/TensorRT-LLM/PR-19249.md) | [TRTLLMINF-440][infra] Upgrade C++ from 17 to 20 | 2026-09-16 | pipeline-stages |  |
| [#19251](../sources/prs/TensorRT-LLM/PR-19251.md) | [None][fix] size FP4 block-scale MoE permute buffers from local_num_experts | 2026-09-16 | pipeline-stages | block-scale, fp4, gemm |
| [#19273](../sources/prs/TensorRT-LLM/PR-19273.md) | [None][feat] Helix speculative verify groups: fp8 + fp4 MLA and DSpark | 2026-09-16 |  | attention, fp4, fp8 |
| [#19291](../sources/prs/TensorRT-LLM/PR-19291.md) | [None][perf] specialize NVFP4 MLA context gather for residual layout | 2026-09-16 |  | attention, fp4, fp8 |
| [#19182](../sources/prs/TensorRT-LLM/PR-19182.md) | [None][feat] Kimi K3 attention-residual RMSNorm fusion + KDA beta-cache alignment | 2026-09-15 | kernel-fusion, persistent-kernel, warp-specialization | attention, mbarrier, moe |
| [#19184](../sources/prs/TensorRT-LLM/PR-19184.md) | [None][feat] Rubin kernels & attention: DSV4/DSA, CuteDSL GEMM | 2026-09-15 | pipeline-stages, swizzling | attention, flash-attention, fp4 |
| [#19199](../sources/prs/TensorRT-LLM/PR-19199.md) | [https://nvbugs/6776338][fix] Enable DeepGEMM FP8 block scales on SM107 | 2026-09-15 |  | block-scale, fp4, fp8 |
| [#19217](../sources/prs/TensorRT-LLM/PR-19217.md) | [TRTLLM-16404][fix] support post-SiLU clamp in CUTLASS MoE | 2026-09-15 |  | fp8, moe |
| [#19220](../sources/prs/TensorRT-LLM/PR-19220.md) | [https://nvbugs/6672360][fix] Stabilize XQA attention sink normalization | 2026-09-15 |  | attention |
| [#19136](../sources/prs/TensorRT-LLM/PR-19136.md) | [None][feat] Add GLM-5.3-Flash (glm5_next) support | 2026-09-14 |  | attention, fp8, mla |
| [#19138](../sources/prs/TensorRT-LLM/PR-19138.md) | [None][feat] enable the GVR Top-K and MTP draft-loop index reuse for the QSA indexer | 2026-09-14 |  | attention, fp4, fp8 |
| [#19142](../sources/prs/TensorRT-LLM/PR-19142.md) | [None][fix] Reject unsupported SM100 sync-object factories | 2026-09-14 | pipeline-stages |  |
| [#19150](../sources/prs/TensorRT-LLM/PR-19150.md) | [None][fix] Pass alpha through SM107 scaled_mm compilation | 2026-09-14 |  | gemm, tcgen05 |
| [#19094](../sources/prs/TensorRT-LLM/PR-19094.md) | [TRTLLM-14329][perf] Enable fused DSA metadata by default | 2026-09-12 |  | attention, fp4, fp8 |
| [#19103](../sources/prs/TensorRT-LLM/PR-19103.md) | [None][fix] KVCM2: fix remaining Python/C++ parity issues and replace abort with a poison latch | 2026-09-12 | pipeline-stages |  |
| [#19040](../sources/prs/TensorRT-LLM/PR-19040.md) | [TRTLLM-16564][feat] MLA-backboned standalone DSpark drafter (Inferact/Kimi-K3-DSpark) | 2026-09-11 |  | attention, flash-attention, fp8 |
| [#19061](../sources/prs/TensorRT-LLM/PR-19061.md) | [TRTLLM-16184][refactor] Consolidate the C++ MoE kernels, thop ops and gtests under moe/ directories | 2026-09-11 | pipeline-stages | fp8, moe |
| [#19070](../sources/prs/TensorRT-LLM/PR-19070.md) | [None][feat] Add FP4 MLA attention backend | 2026-09-11 | pipeline-stages, swizzling | attention, flash-attention, fp4 |
| [#19076](../sources/prs/TensorRT-LLM/PR-19076.md) | [None][perf] GVR V2 top-K: 4K<n<=8K register rungs, unified QC gate, sampled small-envelope prefill plan, SM-count-aware dispatch with B300 tuning | 2026-09-11 |  | topk |
| [#19082](../sources/prs/TensorRT-LLM/PR-19082.md) | [None][perf] MLA context: fuse the Q FP8 quantization into the absorb bmm epilogue (CuTe-DSL BF16->FP8 bmm) + RoPE kOutputFp8Q | 2026-09-11 |  | attention, flash-attention, fp8 |
| [#18999](../sources/prs/TensorRT-LLM/PR-18999.md) | [None][perf] Triton top-k combine for Marlin NVFP4 MoE | 2026-09-10 |  | fp4, gemm, moe |
| [#19003](../sources/prs/TensorRT-LLM/PR-19003.md) | [None][feat] Kimi K3: unlock the CUTEDSL MoE backend for NVFP4 SiTU | 2026-09-10 |  | block-scale, fp4, moe |
| [#18925](../sources/prs/TensorRT-LLM/PR-18925.md) | [https://nvbugs/6641268][fix] Zero paged V-cache tails during context preprocessing | 2026-09-09 | tile-scheduling | attention, flash-attention |
| [#18938](../sources/prs/TensorRT-LLM/PR-18938.md) | [TRTLLM-15899][feat] Add new KDA decode non-mtp kernel and dispatch logic | 2026-09-09 |  | reduction |
| [#18869](../sources/prs/TensorRT-LLM/PR-18869.md) | [None][perf] Optimize HCA compressor decode | 2026-09-08 |  | reduction |
| [#18883](../sources/prs/TensorRT-LLM/PR-18883.md) | [None][perf] fuse decode kernel seams for Qwen3.8-Flash-Next and de-vendor the low-M GEMMs | 2026-09-08 |  | attention, fp4, gemm |
| [#18906](../sources/prs/TensorRT-LLM/PR-18906.md) | [None][perf] defer dynamic NVFP4 scale finalization for fused GELU MLPs | 2026-09-08 | pipeline-stages, swizzling | block-scale, fp4, fp8 |
| [#18783](../sources/prs/TensorRT-LLM/PR-18783.md) | [None][feat] Add DeepSeek-V4 support to NVFP4 cold-page KV Cache Compression | 2026-09-07 | pipeline-stages | attention, block-scale, fp4 |
| [#18799](../sources/prs/TensorRT-LLM/PR-18799.md) | [https://nvbugs/6667807][fix] Support more than 128 EP ranks in MoE two-sided prepare cumsum | 2026-09-07 |  | attention, moe, scan |
| [#18808](../sources/prs/TensorRT-LLM/PR-18808.md) | [None][chore] Update cutedsl to 4.8.0 dev | 2026-09-07 |  | block-scale, tcgen05 |
| [#18815](../sources/prs/TensorRT-LLM/PR-18815.md) | [None][feat] add generic PrimTS block-sparse FMHA and unify sparse attention runtime inputs | 2026-09-07 | pipeline-stages, tile-scheduling | attention, flash-attention, fp8 |
| [#18743](../sources/prs/TensorRT-LLM/PR-18743.md) | [TRTLLMINF-445][infra] Upgrade public torch to 2.13.0 and triton to 3.7.1 | 2026-09-05 | pipeline-stages | topk |
| [#18749](../sources/prs/TensorRT-LLM/PR-18749.md) | [None][feat] Add opt-in GPU keepalive to the benchmark fill gate | 2026-09-05 |  | gemm |
| [#18750](../sources/prs/TensorRT-LLM/PR-18750.md) | [TRTLLM-11484][fix] Address Quantization Regressions for VisualGen CuTeDSL FMHA | 2026-09-05 | kernel-fusion | attention, block-scale, flash-attention |
| [#18761](../sources/prs/TensorRT-LLM/PR-18761.md) | [None][feat] Add SM107 CuTe DSL BF16 dense GEMM/BMM custom ops and dispatch | 2026-09-05 | persistent-kernel, pipeline-stages | attention, fp4, gemm |
| [#18694](../sources/prs/TensorRT-LLM/PR-18694.md) | [https://nvbugs/6674826][fix] Drop overlap hint from KV cache page-index upload | 2026-09-04 |  |  |
| [#18702](../sources/prs/TensorRT-LLM/PR-18702.md) | [None][feat] Self-sampling GVR V2 prefill indexer top-K | 2026-09-04 | pipeline-stages | attention, flash-attention, fp4 |
| [#18714](../sources/prs/TensorRT-LLM/PR-18714.md) | [None][perf] speed up the block-scale MoE, GDN and sampler decode paths for Qwen3.8-flash-next | 2026-09-04 | pipeline-stages | block-scale, fp8, moe |
| [#18723](../sources/prs/TensorRT-LLM/PR-18723.md) | [None][feat] Enable NVFP4 KV for DSV4 | 2026-09-04 | pipeline-stages | attention, fp4, fp8 |
| [#18625](../sources/prs/TensorRT-LLM/PR-18625.md) | [None][fix] Self-sampling top-k drops +inf from the top-k (register family) | 2026-09-03 |  | attention, sort, sparse-attention |
| [#18683](../sources/prs/TensorRT-LLM/PR-18683.md) | [None][fix] Self-sampling top-k host: physical row-width envelope and exact-row warmup population | 2026-09-03 |  | topk |
| [#18585](../sources/prs/TensorRT-LLM/PR-18585.md) | [None][feat] add Qwen3.8-Flash-Next support | 2026-09-02 | kernel-fusion, pipeline-stages | attention, fp4, fp8 |
| [#18605](../sources/prs/TensorRT-LLM/PR-18605.md) | [None][feat] Support MiniMax-M3 in MegaMoE CuTeDSL | 2026-09-02 | pipeline-stages | fp4, moe, nvfp4 |
| [#18612](../sources/prs/TensorRT-LLM/PR-18612.md) | [TRTLLM-15316][fix] SM107 FP8 GEMM routing and runtime guards (follow-up to #17485) | 2026-09-02 |  | attention, block-scale, fp4 |
| [#18614](../sources/prs/TensorRT-LLM/PR-18614.md) | [None][perf] Fuse MiniMax-M3 MSA per-layer KV-cache writes into one kernel | 2026-09-02 | pipeline-stages | attention, flash-attention, fp4 |
| [#18476](../sources/prs/TensorRT-LLM/PR-18476.md) | [TRTLLM-14645][fix] VisualGen: allow sm_107a in CuTe DSL FMHA and guard unsupported SAGE SM | 2026-09-01 |  | attention, flash-attention, quantization |
| [#18478](../sources/prs/TensorRT-LLM/PR-18478.md) | [None][feat] Rubin fp4 mla refactor(P1) | 2026-09-01 | pipeline-stages, swizzling | attention, block-scale, flash-attention |
| [#18485](../sources/prs/TensorRT-LLM/PR-18485.md) | [TRTLLM-14620][feat] Add ragged sparse-attention row contracts | 2026-09-01 |  | attention, mla, sparse-attention |
| [#18496](../sources/prs/TensorRT-LLM/PR-18496.md) | [TRTLLM-16040][feat] Refresh SM90 SageAttention onto the per-thread-quantized kernel, Integrate to VisualGen | 2026-09-01 | swizzling, warp-specialization | attention, flash-attention, fp8 |
| [#18498](../sources/prs/TensorRT-LLM/PR-18498.md) | [None][feat] Add SM107 NVFP4 CuTe DSL fused MoE kernels and integration | 2026-09-01 |  | block-scale, fp4, mbarrier |
| [#18501](../sources/prs/TensorRT-LLM/PR-18501.md) | [None][fix] Enforce the count-crossing invariant in the self-sampling top-k register family | 2026-09-01 |  | sort, topk |
| [#18515](../sources/prs/TensorRT-LLM/PR-18515.md) | [TRTLLM-15137][feat] Add fused sampling and min-p support to AdvancedSamplingMode.FULL | 2026-09-01 | kernel-fusion | reduction, scan, sort |
| [#18533](../sources/prs/TensorRT-LLM/PR-18533.md) | [None][chore] Remove unused KV cache draft-token rewind helpers | 2026-09-01 |  |  |
| [#18541](../sources/prs/TensorRT-LLM/PR-18541.md) | [None][perf] Speed up burst KVCM2 resize for very long sequences | 2026-09-01 | pipeline-stages | sort, tcgen05 |
| [#18546](../sources/prs/TensorRT-LLM/PR-18546.md) | [None][feat] Add SM107 quantized dense and DSV4 CuTe DSL kernels | 2026-09-01 | pipeline-stages, swizzling, tile-scheduling | block-scale, clc, fp4 |
| [#18446](../sources/prs/TensorRT-LLM/PR-18446.md) | [None][feat] Two-level GVR decode top-K dispatch; remove the CUDA heuristic and temporal-only prior state | 2026-08-31 | pipeline-stages | attention, fp4, sort |
| [#18410](../sources/prs/TensorRT-LLM/PR-18410.md) | [None][feat] GVR V2 decode top-k goes hint-free by default: the bracket comes from the current row | 2026-08-30 |  | attention, quantization, sort |
| [#18329](../sources/prs/TensorRT-LLM/PR-18329.md) | [TRTLLM-15917][feat] Integrate Sol-Attn sparse attention into VisualGen | 2026-08-28 | pipeline-stages, swizzling | attention, flash-attention, gemm |
| [#18331](../sources/prs/TensorRT-LLM/PR-18331.md) | [TRTLLM-15316][feat] Fix fused mHC Phase-4 coherence and support uneven split-K | 2026-08-28 |  | tcgen05, tma |
| [#18339](../sources/prs/TensorRT-LLM/PR-18339.md) | [#18338][fix] Fix barrier-divergence races in the Blackwell CuTe DSL GVR top-k decode kernel | 2026-08-28 |  | quantization, topk |
| [#18357](../sources/prs/TensorRT-LLM/PR-18357.md) | [None][feat] add CuteDslFc12FusedMoE fused FC1+FC2 NVFP4 MoE backend (Rubin/SM107) | 2026-08-28 | kernel-fusion, persistent-kernel | block-scale, fp4, gemm |
| [#18369](../sources/prs/TensorRT-LLM/PR-18369.md) | [None][feat] Add Rubin SM107 CuTe DSL foundation and BF16 kernels | 2026-08-28 | pipeline-stages, swizzling, tile-scheduling | block-scale, fp4, fp8 |
| [#18391](../sources/prs/TensorRT-LLM/PR-18391.md) | [TRTLLM-14575][perf] Batch DSA cross-layer index remap into one kernel launch per indexer group | 2026-08-28 |  | attention, mla, reduction |
| [#18323](../sources/prs/TensorRT-LLM/PR-18323.md) | [https://nvbugs/6633931][fix] Size the SM90 fp8 block-scale MoE workspace for the buffers it actually uses | 2026-08-27 |  | block-scale, fp8, gemm |
| [#18233](../sources/prs/TensorRT-LLM/PR-18233.md) | [TRTLLM-15405][refactor] Remove the C++ decoder stack behind TRTLLMSampler | 2026-08-26 |  | mla, topk |
| [#18251](../sources/prs/TensorRT-LLM/PR-18251.md) | [TRTLLM-15498][perf] optimize Kimi KDA decode data flow | 2026-08-26 |  |  |
| [#18265](../sources/prs/TensorRT-LLM/PR-18265.md) | [TRTLLM-14575][perf] Enable fused-A GEMM for the GLM MLA A-projection | 2026-08-26 | kernel-fusion | gemm, mla, moe |
| [#18268](../sources/prs/TensorRT-LLM/PR-18268.md) | [TRTLLM-14575][perf] Fuse DSA decode metadata into a single Triton kernel | 2026-08-26 | kernel-fusion | attention, fp4, fp8 |
| [#18197](../sources/prs/TensorRT-LLM/PR-18197.md) | [TRTLLM-15316][feat] Rubin sm107 trtllm-gen gemms | 2026-08-25 | persistent-kernel | fp4, fp8, gemm |
| [#18205](../sources/prs/TensorRT-LLM/PR-18205.md) | [None][perf] Fuse MiniMax-M3 QKV and index projection | 2026-08-25 |  | attention, fp4, fp8 |
| [#18118](../sources/prs/TensorRT-LLM/PR-18118.md) | [None][perf] Enable configurable MLA skip correction for TRT-LLM Gen FMHA | 2026-08-24 |  | attention, flash-attention, fp8 |
| [#18126](../sources/prs/TensorRT-LLM/PR-18126.md) | [TRTLLMINF-397][infra] Update dependencies to NGC PyTorch 26.08 | 2026-08-24 |  |  |
| [#18131](../sources/prs/TensorRT-LLM/PR-18131.md) | [None][feat] Enable CuTe DSL MLA with Helix | 2026-08-24 |  | attention, fp8, mla |
| [#18141](../sources/prs/TensorRT-LLM/PR-18141.md) | [https://nvbugs/6530268][fix] Fix XQA race condition and attn sink numerical accuracy | 2026-08-24 |  | attention, gemm, quantization |
| [#18154](../sources/prs/TensorRT-LLM/PR-18154.md) | [None][perf] Histogram top-k for MiniMax-M3 block selector | 2026-08-24 |  | scan, sort, topk |
| [#18091](../sources/prs/TensorRT-LLM/PR-18091.md) | [None][feat] Add NVFP4 as a cold-page KV Cache Compression Method | 2026-08-22 |  | attention, block-scale, fp4 |
| [#18094](../sources/prs/TensorRT-LLM/PR-18094.md) | [None][fix] CuTe DSL GVR top-K decode: repair the non-converged threshold search | 2026-08-22 |  | attention, sort, sparse-attention |
| [#18061](../sources/prs/TensorRT-LLM/PR-18061.md) | [None][perf] optimize DSpark attention | 2026-08-21 | persistent-kernel, pipeline-stages, tile-scheduling | attention, mbarrier, tcgen05 |
| [#18079](../sources/prs/TensorRT-LLM/PR-18079.md) | [None][feat] add VisualGen VSA and SOL sparse attention on PrimTS block-sparse FMHA | 2026-08-21 | pipeline-stages | attention, flash-attention, quantization |
| [#18081](../sources/prs/TensorRT-LLM/PR-18081.md) | [None][perf] Convolve the Mamba2 prefill on a channel-last projection | 2026-08-21 |  |  |
| [#18082](../sources/prs/TensorRT-LLM/PR-18082.md) | [None][perf] Fuse relu2 into a single elementwise kernel | 2026-08-21 |  |  |
| [#18036](../sources/prs/TensorRT-LLM/PR-18036.md) | [TRTLLM-15740][perf] VisualGen Wan: deduplicate shared RoPE SMEM staging | 2026-08-20 |  |  |
| [#17956](../sources/prs/TensorRT-LLM/PR-17956.md) | [None][perf] update MegaMoE kernels for Blackwell and Rubin | 2026-08-19 | kernel-fusion, persistent-kernel, pipeline-stages | block-scale, fp4, fp8 |
| [#17968](../sources/prs/TensorRT-LLM/PR-17968.md) | [TRTLLM-14558][chore] Consolidate the Attention domain: modules, backends and unit tests | 2026-08-19 |  | attention, flash-attention, mla |
| [#17976](../sources/prs/TensorRT-LLM/PR-17976.md) | [None][perf] SM120 optimizations for Qwen3.6-35B-A3B-NVFP4 | 2026-08-19 |  | attention, flash-attention, fp4 |
| [#17987](../sources/prs/TensorRT-LLM/PR-17987.md) | [https://nvbugs/6535765][fix] bump Wan layernorm fusion math to FP32 | 2026-08-19 | pipeline-stages | fp4, nvfp4 |
| [#17862](../sources/prs/TensorRT-LLM/PR-17862.md) | [TRTLLM-15498][perf] fuse KDA beta preprocessing and isolate FLA fallbacks | 2026-08-18 | pipeline-stages | fp8, quantization |
| [#17865](../sources/prs/TensorRT-LLM/PR-17865.md) | [None][feat] bring up Kimi K3 NVFP4 with CUTLASS and cuteDSL MegaMoE SiTU | 2026-08-18 |  | fp4, fp8, moe |
| [#17870](../sources/prs/TensorRT-LLM/PR-17870.md) | [TRTLLM-15498][perf] optimize Kimi KDA prefill convolution data flow | 2026-08-18 |  | fp8 |
| [#17887](../sources/prs/TensorRT-LLM/PR-17887.md) | [TRTLLM-15498][perf] eliminate KDA recurrent-state and metadata copies | 2026-08-18 |  | attention |
| [#17889](../sources/prs/TensorRT-LLM/PR-17889.md) | [TRTLLM-15304][perf] add low-M BF16 GEMM dispatcher for SM10x decode | 2026-08-18 | pipeline-stages | gemm, mbarrier, reduction |
| [#17893](../sources/prs/TensorRT-LLM/PR-17893.md) | [None][perf] split routing kernels to reduce compile time | 2026-08-18 |  | block-scale, moe |
| [#17821](../sources/prs/TensorRT-LLM/PR-17821.md) | [TRTLLM-15293][perf] Add self-sampling (GVR V2) top-K decode kernels | 2026-08-17 |  | quantization, reduction, sort |
| [#17842](../sources/prs/TensorRT-LLM/PR-17842.md) | [None][feat] Add the ported MiniMax-M3 decode kernels ahead of their wiring | 2026-08-17 | pipeline-stages, swizzling | attention, flash-attention, fp8 |
| [#17781](../sources/prs/TensorRT-LLM/PR-17781.md) | [TRTLLM-15585][feat] Wire SkipSoftmax sparse attention into the CuTeDSL backend | 2026-08-16 |  | attention, block-scale, flash-attention |
| [#17681](../sources/prs/TensorRT-LLM/PR-17681.md) | [None][feat] Add NVFP4 KV cache support for DSA | 2026-08-14 |  | attention, block-scale, fp4 |
| [#17695](../sources/prs/TensorRT-LLM/PR-17695.md) | [TRTLLM-15400][perf] fuse per-token AdaLN for VisualGen Wan 2.2 5B | 2026-08-14 | pipeline-stages | block-scale, fp4, fp8 |
| [#17700](../sources/prs/TensorRT-LLM/PR-17700.md) | [None][perf] Qwen3.5/3.8 wave-2: MoE, attention-DP, GDN replay, weight loading | 2026-08-14 |  | attention, moe |
| [#17707](../sources/prs/TensorRT-LLM/PR-17707.md) | [TRTLLM-15316][feat] Rubin trtllmgen batchedGemm MoE | 2026-08-14 |  | attention, block-scale, flash-attention |
| [#17621](../sources/prs/TensorRT-LLM/PR-17621.md) | [None][fix] Fence MoE shared writes before async bulk copy | 2026-08-13 |  | moe |
| [#17635](../sources/prs/TensorRT-LLM/PR-17635.md) | [TRTLLM-15304][fix] MoE and MTP fixes for large hybrid-attention FP8 serving | 2026-08-13 |  | attention, block-scale, fp8 |
| [#17660](../sources/prs/TensorRT-LLM/PR-17660.md) | [https://nvbugs/6604925][fix] Swap the grid axes so N maps to the unbounded `grid.x` and M to `grid.y`… | 2026-08-13 |  | fp4, nvfp4, quantization |
| [#17539](../sources/prs/TensorRT-LLM/PR-17539.md) | [#17522][fix] Restore conv_state ordering barriers in the Triton conv kernels | 2026-08-12 |  |  |
| [#17550](../sources/prs/TensorRT-LLM/PR-17550.md) | [None][fix] GVR indexer top-K: repair the non-converged threshold search | 2026-08-12 |  | topk |
| [#17485](../sources/prs/TensorRT-LLM/PR-17485.md) | [TRTLLM-15316][feat] sm107 gemm + quant | 2026-08-11 |  | block-scale, fp4, fp8 |
| [#17512](../sources/prs/TensorRT-LLM/PR-17512.md) | [None][feat] Add cold-page codec support to KVCM2 | 2026-08-11 |  |  |
| [#17521](../sources/prs/TensorRT-LLM/PR-17521.md) | [TRTLLM-15314][feat] Add FP8 LoRA support for B200 | 2026-08-11 |  | fp8, gemm, grouped-gemm |
| [#17476](../sources/prs/TensorRT-LLM/PR-17476.md) | [None][feat] Load static FP8 Cosmos3 Nano/Super checkpoints without re-quantizing them | 2026-08-10 | kernel-fusion, pipeline-stages | attention, fp4, fp8 |
| [#17399](../sources/prs/TensorRT-LLM/PR-17399.md) | [None][feat] integrate PrimTS FMHA kernels | 2026-08-07 | persistent-kernel, pipeline-stages, swizzling | attention, clc, flash-attention |
| [#17425](../sources/prs/TensorRT-LLM/PR-17425.md) | [None][fix] Fix CuTeDSL packed QKV copy lowering | 2026-08-07 |  | attention, flash-attention |
| [#17269](../sources/prs/TensorRT-LLM/PR-17269.md) | [TRTLLM-14813][feat] Add Kimi K3 (KimiLinear) model | 2026-08-05 | pipeline-stages | attention, block-scale, flash-attention |
| [#17273](../sources/prs/TensorRT-LLM/PR-17273.md) | [TRTLLM-14597][perf] Fuse the DSv4 MLA prologue: kv_a_layernorm, q_nope FP8 quant and Q RoPE | 2026-08-05 |  | attention, flash-attention, fp8 |
| [#17274](../sources/prs/TensorRT-LLM/PR-17274.md) | [TRTLLM-13767][chore] upgrade CUTLASS DSL stack to 4.6.1 | 2026-08-05 |  | block-scale, flash-attention, fp4 |
| [#17307](../sources/prs/TensorRT-LLM/PR-17307.md) | [None][perf] fuse DSpark attention and RMSNorm RoPE | 2026-08-05 |  | attention, reduction, sparse-attention |
| [#17312](../sources/prs/TensorRT-LLM/PR-17312.md) | [None][refactor] Refactor Kimi K3 MLP | 2026-08-05 |  | attention, fp8, mla |
| [#17318](../sources/prs/TensorRT-LLM/PR-17318.md) | [None][perf] Use FP8 MiniMax-M3 MSA indexer QK | 2026-08-05 |  | attention, fp8 |
| [#17236](../sources/prs/TensorRT-LLM/PR-17236.md) | [None][perf] Optimize MiniMax-M3 MSA block selection | 2026-08-04 | warp-specialization | fp4, nvfp4, sort |
| [#17243](../sources/prs/TensorRT-LLM/PR-17243.md) | [https://nvbugs/6545424][perf] Enable Qwen3.5 fused ops under torch.c… | 2026-08-04 |  | attention, fp8 |
| [#17262](../sources/prs/TensorRT-LLM/PR-17262.md) | [TRTLLM-13767][feat] integrate FP4 Conv3d into parallel Wan VAE | 2026-08-04 | persistent-kernel, pipeline-stages, swizzling | block-scale, clc, fp4 |
| [#17190](../sources/prs/TensorRT-LLM/PR-17190.md) | [TRTLLM-14701][feat] Update trtllm-gen batchedGemm kernel drop for Kimi K3 MoE | 2026-08-03 | kernel-fusion | block-scale, gemm, moe |
| [#17225](../sources/prs/TensorRT-LLM/PR-17225.md) | [None][feat] Add Kimi K3 KDA prefill/MTP decode CuTe DSL kernels and fused attention-residual kernel | 2026-08-03 | warp-specialization | attention, mbarrier, tcgen05 |
| [#17093](../sources/prs/TensorRT-LLM/PR-17093.md) | [None][perf] Fold q/k/v quantization into qknorm_rope_fused kernel & remove contiguous | 2026-07-31 |  | attention, fp8, quantization |
| [#17120](../sources/prs/TensorRT-LLM/PR-17120.md) | [None][fix] Fix Qwen3.5 MoE fallback, GDN alignment, FP8 activation, and draft KV cache | 2026-07-31 |  | block-scale, fp8, moe |
| [#17054](../sources/prs/TensorRT-LLM/PR-17054.md) | [TRTLLM-14702][feat] Integrate Kimi K3 KDA decode kernel | 2026-07-30 |  | attention |
| [#17059](../sources/prs/TensorRT-LLM/PR-17059.md) | [None][perf] fuse Kimi K3 routing and MXFP8 quantization | 2026-07-30 |  | fp4, fp8, moe |
| [#17003](../sources/prs/TensorRT-LLM/PR-17003.md) | [TRTLLM-14798][perf] Fuse Wan DupUp3D output mapping | 2026-07-29 | kernel-fusion | fp4, reduction |
| [#16933](../sources/prs/TensorRT-LLM/PR-16933.md) | [https://nvbugs/6424956][fix] Support large FP8 quantization grids | 2026-07-28 |  | fp8, quantization |
| [#16953](../sources/prs/TensorRT-LLM/PR-16953.md) | [None][perf] Emission-assisted GVR top-K decode for the DeepSeek V4 indexer | 2026-07-28 | pipeline-stages | attention, fp4, gemm |
| [#16957](../sources/prs/TensorRT-LLM/PR-16957.md) | [None][feat] Add TriAttention KV-cache compression method | 2026-07-28 | double-buffering, pipeline-stages, swizzling | attention, gemm, reduction |
| [#16905](../sources/prs/TensorRT-LLM/PR-16905.md) | [None][perf] Fused SwiGLU-OAI | 2026-07-27 |  | attention, fp4, nvfp4 |
| [#16877](../sources/prs/TensorRT-LLM/PR-16877.md) | [TRTLLM-15293][perf] Add tiered GVR CuTe DSL top-k decode kernels (stacked on #16457) | 2026-07-26 | persistent-kernel | attention, quantization, scan |
| [#16836](../sources/prs/TensorRT-LLM/PR-16836.md) | [None][feat] Batched physical KV-cache compaction for KV cache compression | 2026-07-24 | double-buffering, pipeline-stages |  |
| [#16847](../sources/prs/TensorRT-LLM/PR-16847.md) | [TRTLLM-14616][feat] add VisualGen fp8 row-wise quant + autotuner | 2026-07-24 | pipeline-stages | attention, fp8, gemm |
| [#16849](../sources/prs/TensorRT-LLM/PR-16849.md) | [None][perf] fp8 block scale quant fusion in SM90 Cutlass MoE | 2026-07-24 | swizzling | block-scale, fp4, fp8 |
| [#16768](../sources/prs/TensorRT-LLM/PR-16768.md) | [TRTLLM-14345][feat] Improve the GDN Replay Kernel Under Low Latency | 2026-07-23 |  |  |
| [#16799](../sources/prs/TensorRT-LLM/PR-16799.md) | [None][perf] Optimize Blackwell fused MHC half-MMA kernel | 2026-07-23 | pipeline-stages | reduction, tcgen05, tma |
| [#16810](../sources/prs/TensorRT-LLM/PR-16810.md) | [None][feat] Support dense FP8 LoRA end to end | 2026-07-23 |  | attention, fp8, gemm |
| [#16716](../sources/prs/TensorRT-LLM/PR-16716.md) | [TRTLLM-14551][perf] avoid GDN state reset host synchronization | 2026-07-22 | pipeline-stages |  |
| [#16749](../sources/prs/TensorRT-LLM/PR-16749.md) | [None][feat] Enable Marlin NVFP4 on Ada Lovelace | 2026-07-22 |  | fp4, gemm, moe |
| [#16673](../sources/prs/TensorRT-LLM/PR-16673.md) | [None][chore] update DeepGEMM to 2.6.1 | 2026-07-21 | pipeline-stages, swizzling | fp4, fp8, gemm |
| [#16633](../sources/prs/TensorRT-LLM/PR-16633.md) | [None][perf] Optimize fusedQKNormRope Kernel | 2026-07-20 | pipeline-stages | fp4, fp8, nvfp4 |
| [#16569](../sources/prs/TensorRT-LLM/PR-16569.md) | [None][perf] Size the per-tensor FP8 dynamic-quant amax grid to the input | 2026-07-18 |  | fp8, quantization, reduction |
| [#16532](../sources/prs/TensorRT-LLM/PR-16532.md) | [None][perf] Fuse DeepSeek-V4 Indexer Q projection with CuTe DSL | 2026-07-17 | kernel-fusion, swizzling | attention, fp4, fp8 |
| [#16546](../sources/prs/TensorRT-LLM/PR-16546.md) | [None][feat] Raise the CuTE-DSL top-k decode limit to 16384 and support odd top_k | 2026-07-17 |  | topk |
| [#16558](../sources/prs/TensorRT-LLM/PR-16558.md) | [None][perf] Allocate DSA indexer k-cache only for layers that own an indexer | 2026-07-17 | pipeline-stages | attention, fp4, mla |
| [#16464](../sources/prs/TensorRT-LLM/PR-16464.md) | [TRTLLM-14345][feat] Support GDN MTP Replay | 2026-07-16 |  | fp4, gemm, nvfp4 |
| [#16469](../sources/prs/TensorRT-LLM/PR-16469.md) | [TRTLLM-14352][perf] Fuse Qwen3.5/3.6 attention preprocessing (QK-nor… | 2026-07-16 |  | attention, quantization |
| [#16511](../sources/prs/TensorRT-LLM/PR-16511.md) | [TRTLLM-12720][feat] Support nvfp4 w4a16 on sm120 | 2026-07-16 | pipeline-stages, swizzling | attention, block-scale, fp4 |
| [#16394](../sources/prs/TensorRT-LLM/PR-16394.md) | [TRTLLM-14268][feat] Cosmos3 Transfer (control-video conditioning) | 2026-07-15 | kernel-fusion, pipeline-stages | attention, quantization |
| [#16424](../sources/prs/TensorRT-LLM/PR-16424.md) | [None][perf] DSv4 GVR top-k (CuTe DSL): P4 histogram refinement + redundant-warp sync reduction | 2026-07-15 | double-buffering | attention, reduction, topk |
| [#16457](../sources/prs/TensorRT-LLM/PR-16457.md) | [None][perf] GVR top-K decode: enable R0 histogram-ladder admission by default | 2026-07-15 | pipeline-stages | attention, sort, topk |
| [#16365](../sources/prs/TensorRT-LLM/PR-16365.md) | [TRTLLM-13212][refactor] Unify sampler ops and clean up dead code in TorchSampler | 2026-07-14 | pipeline-stages | topk |
| [#16369](../sources/prs/TensorRT-LLM/PR-16369.md) | [TRTLLM-14026][feat] BREAKING: Remove C++ modules for legacy TRT backend | 2026-07-14 | pipeline-stages | block-scale, fp4, fp8 |
| [#16299](../sources/prs/TensorRT-LLM/PR-16299.md) | [None][perf] fuse gdn post-conv split, QK norm and gating and  RMSNorm with FP8 quantization | 2026-07-13 |  | fp4, fp8, nvfp4 |
| [#16303](../sources/prs/TensorRT-LLM/PR-16303.md) | [https://nvbugs/6445494][infra] Upgrade Triton to 3.7.0 for Torch 2.12.0 compatibility | 2026-07-13 | persistent-kernel, swizzling, warp-specialization | fp4, fp8, moe |
| [#16314](../sources/prs/TensorRT-LLM/PR-16314.md) | [TRTLLM-14054][perf] Load Qwen3-Next GDN in_proj in dense layout and add a multi-row gated RMSNorm | 2026-07-13 |  | fp4, fp8, moe |
| [#16221](../sources/prs/TensorRT-LLM/PR-16221.md) | [None][fix] Fix fused mHC output reuse and extend compressor next_n | 2026-07-10 |  | reduction |
| [#16224](../sources/prs/TensorRT-LLM/PR-16224.md) | [None][feat] Enable DeepSeek-V4 and DSA (DeepSeek-V3.2/GLM) serving on SM120 via FlashInfer sparse-MLA | 2026-07-10 | epilogue-fusion, pipeline-stages | attention, flash-attention, fp8 |
| [#16190](../sources/prs/TensorRT-LLM/PR-16190.md) | [None][feat] Update CuTeDSL MegaMoE kernels | 2026-07-09 | kernel-fusion, pipeline-stages | block-scale, fp4, fp8 |
| [#16028](../sources/prs/TensorRT-LLM/PR-16028.md) | [None][perf] Port remaining DeepSeek V4 optimizations to main | 2026-07-07 |  | attention, sparse-attention |
| [#16074](../sources/prs/TensorRT-LLM/PR-16074.md) | [TRTLLM-14138][perf] Add fused kernels for Gemma4 serving | 2026-07-07 | kernel-fusion, swizzling | attention, block-scale, fp4 |
| [#15909](../sources/prs/TensorRT-LLM/PR-15909.md) | [TRTLLM-14024][feat] Prune CuTe DSL NVFP4 GEMM autotuner tactics with nvMatmulHeuristics | 2026-07-03 | swizzling, tile-scheduling | fp4, gemm, nvfp4 |
| [#15887](../sources/prs/TensorRT-LLM/PR-15887.md) | [https://nvbugs/5805494][fix] Use int64 indexing in trtllm-gen block-scale MoE kernels | 2026-07-02 |  | attention, block-scale, fp8 |
| [#15831](../sources/prs/TensorRT-LLM/PR-15831.md) | [None][feat] VisualGen: Add CuTe DSL JIT kernels for FMHA | 2026-07-01 | persistent-kernel, swizzling, tile-scheduling | attention, block-scale, flash-attention |
| [#15835](../sources/prs/TensorRT-LLM/PR-15835.md) | [None][perf] Cute DSL GVR Top-K: short-row remove cluster sync in run_one_row | 2026-07-01 | pipeline-stages | attention, topk |
| [#15754](../sources/prs/TensorRT-LLM/PR-15754.md) | [None][perf] overlap LTX-2 v2a cross-attn comm with compute via async-Ulysses | 2026-06-30 | kernel-fusion, pipeline-stages | attention, fp4, gemm |
| [#15756](../sources/prs/TensorRT-LLM/PR-15756.md) | [None][feat] Improve cute dsl radix top-k | 2026-06-30 |  | scan, sort, topk |
| [#15762](../sources/prs/TensorRT-LLM/PR-15762.md) | [TRTLLM-11780][feat] Wan 2.2 layernorm + shiftscale + quant fusion | 2026-06-30 | kernel-fusion, pipeline-stages, swizzling | fp4, fp8, gemm |
| [#15780](../sources/prs/TensorRT-LLM/PR-15780.md) | [TRTLLM-15344][feat] cache transceiver nixl bounce buffer | 2026-06-30 | pipeline-stages |  |
| [#15714](../sources/prs/TensorRT-LLM/PR-15714.md) | [TRTLLM-13581][test] Add moe fp4 gpu dequant and unpack optimization | 2026-06-29 |  | fp4, moe, quantization |
| [#15717](../sources/prs/TensorRT-LLM/PR-15717.md) | [None][perf] DSv4 follow-up: sparse attention and model defaults | 2026-06-29 | double-buffering, kernel-fusion, pipeline-stages | attention, flash-attention, fp4 |
| [#15739](../sources/prs/TensorRT-LLM/PR-15739.md) | [https://nvbugs/6250439][fix] Correct speculative XQA attention sinks | 2026-06-29 |  | attention |
| [#15656](../sources/prs/TensorRT-LLM/PR-15656.md) | [None][feat] Optimize trtllmgen moe routing | 2026-06-26 |  | block-scale, moe, topk |
| [#15660](../sources/prs/TensorRT-LLM/PR-15660.md) | [None][fix] Fix marlin_nvfp4_template.h compilation error | 2026-06-26 | pipeline-stages | quantization, reduction |
| [#15618](../sources/prs/TensorRT-LLM/PR-15618.md) | [TRTLLM-13614][feat] Disaggregated KV-cache bounce transfer | 2026-06-25 |  | mla |
| [#15621](../sources/prs/TensorRT-LLM/PR-15621.md) | [https://nvbugs/6242591][fix] Fix bugs in Beam Search kernels | 2026-06-25 |  | sort |
| [#15632](../sources/prs/TensorRT-LLM/PR-15632.md) | [TRTLLM-12950][perf] DSv4 follow-up: DeepGEMM and MegaMoE | 2026-06-25 |  | attention, fp4, gemm |
| [#15575](../sources/prs/TensorRT-LLM/PR-15575.md) | [None][chore] Remove nv-internal-release guardword comments in mega_moe_nvfp4 | 2026-06-24 |  | moe |
| [#15390](../sources/prs/TensorRT-LLM/PR-15390.md) | [None][perf] DSv4 prep: attention fusion custom ops | 2026-06-16 |  | attention, block-scale, fp8 |
| [#15402](../sources/prs/TensorRT-LLM/PR-15402.md) | [None][feat] DSv4 prep: MoE routing and backend support | 2026-06-16 |  | attention, block-scale, fp4 |
| [#15409](../sources/prs/TensorRT-LLM/PR-15409.md) | [None][feat] DSv4: sparse MLA attention backend | 2026-06-16 |  | attention, flash-attention, mla |
| [#15379](../sources/prs/TensorRT-LLM/PR-15379.md) | [None][feat] DSv4 prep: compressor and mHC primitives | 2026-06-15 | kernel-fusion, pipeline-stages, swizzling | attention, fp4, fp8 |
| [#15381](../sources/prs/TensorRT-LLM/PR-15381.md) | [None][feat] DSv4 prep: IndexerTopK and TopK primitives | 2026-06-15 |  | attention, mla, moe |
| [#15338](../sources/prs/TensorRT-LLM/PR-15338.md) | [None][fix] fix tinygemm barrier bug | 2026-06-13 | pipeline-stages | gemm, tma |
| [#15292](../sources/prs/TensorRT-LLM/PR-15292.md) | [None][feat] BREAKING: Add MiniMax-M3 PyTorch backend bring-up with API changes | 2026-06-12 |  | attention, reduction, sparse-attention |
| [#15297](../sources/prs/TensorRT-LLM/PR-15297.md) | [None][feat] Share Expert Fusion with cherry-pick #11143 | 2026-06-12 | pipeline-stages | block-scale, fp8, moe |
| [#15299](../sources/prs/TensorRT-LLM/PR-15299.md) | [TRTLLM-13370][perf] LTX2 + WAN: Fuse MLP up-GEMM + bias + GELU(tanh) + NVFP4-quant into CuteDSL epilogue | 2026-06-12 | kernel-fusion | attention, block-scale, fp4 |
| [#15304](../sources/prs/TensorRT-LLM/PR-15304.md) | [TRTLLM-35882][feat] cute dsl gvr-topk load-balance optimization | 2026-06-12 | pipeline-stages | attention, mbarrier, sort |
| [#15330](../sources/prs/TensorRT-LLM/PR-15330.md) | [None][chore] Simplify MoE lora | 2026-06-12 |  | gemm, grouped-gemm, moe |
| [#15258](../sources/prs/TensorRT-LLM/PR-15258.md) | [None][perf] Cutedsl NVF4 MOE: grouped/swiglu GEMM: Fix acc pipeline release arrive threads + FC2 meta stage code clean | 2026-06-11 | pipeline-stages | block-scale, gemm, grouped-gemm |
| [#15271](../sources/prs/TensorRT-LLM/PR-15271.md) | [None][chore] Integration tests for MoE lora & bugfixes | 2026-06-11 |  | gemm, grouped-gemm, moe |
| [#15198](../sources/prs/TensorRT-LLM/PR-15198.md) | [TRTLLM-35882][feat] cute dsl gvr-top multi-cta optimization | 2026-06-10 | pipeline-stages | attention, topk |
| [#15138](../sources/prs/TensorRT-LLM/PR-15138.md) | [None][feat] add CuteDSL FP8/FP16 MLA decode attention fmha lib | 2026-06-09 | persistent-kernel, tile-scheduling | attention, flash-attention, fp8 |
| [#15163](../sources/prs/TensorRT-LLM/PR-15163.md) | [None][feat] skip-softmax on SM120: TMA-load + sync-MMA warp-specialized context FMHA for sm_120/sm_121 | 2026-06-09 | swizzling, warp-specialization | attention, flash-attention, mbarrier |
| [#15092](../sources/prs/TensorRT-LLM/PR-15092.md) | [None][feat] Enhance CuteDSL NVF4 MOE | 2026-06-08 | pipeline-stages | block-scale, fp4, gemm |
| [#15098](../sources/prs/TensorRT-LLM/PR-15098.md) | [TRTLLM-13319][fix] fix output distribution correctness for Eagle3 dynamic-tree rejection sampling | 2026-06-08 |  | fp8 |
| [#15102](../sources/prs/TensorRT-LLM/PR-15102.md) | [TRTLLM-13265][feat] Fuse LTX-2 Gate + Residual + Norm + AdaLN modulation(ShiftScale) + Quant kernels | 2026-06-08 | kernel-fusion, pipeline-stages, swizzling | attention, block-scale, fp4 |
| [#15110](../sources/prs/TensorRT-LLM/PR-15110.md) | [None][feat] Support partial RoPE fusion for Hopper kernels in XQA for Laguna | 2026-06-08 | swizzling | attention |
| [#15125](../sources/prs/TensorRT-LLM/PR-15125.md) | [None][fix] Fix beam search log_probs non-determinism with batch_size > 1 | 2026-06-08 |  |  |
| [#15053](../sources/prs/TensorRT-LLM/PR-15053.md) | [TRTLLM-13264][feat] Add native bias epilogue to NVFP4 GEMM | 2026-06-07 | epilogue-fusion | fp4, gemm, nvfp4 |
| [#14923](../sources/prs/TensorRT-LLM/PR-14923.md) | [TRTLLM-12507][feat] Cudagraph support for routed-expert MoE LoRA with Cutlass backend - Part 1 | 2026-06-04 |  | attention, gemm, grouped-gemm |
| [#14962](../sources/prs/TensorRT-LLM/PR-14962.md) | [None][feat] add MXFP8 weight format + CUTLASS W8A8 Linear and MoE | 2026-06-04 |  | block-scale, fp4, fp8 |
| [#14881](../sources/prs/TensorRT-LLM/PR-14881.md) | [TRTLLM-12507][feat] Cudagraph support for per-expert lora in Cutlass backend - Part 2 | 2026-06-03 |  | gemm, grouped-gemm, moe |
| [#14898](../sources/prs/TensorRT-LLM/PR-14898.md) | [None][perf] Support Gemma RMSNorm + interleaved mRoPE in fused_qk_no… | 2026-06-03 |  | attention |
| [#14841](../sources/prs/TensorRT-LLM/PR-14841.md) | [None][fix] Stabilize Mamba replay state update | 2026-06-02 |  |  |
| [#14848](../sources/prs/TensorRT-LLM/PR-14848.md) | [TRTLLM-12373][feat] RMSNorm nvfp4 quant fusion for DS V3.2 / Kimi-K2.5 | 2026-06-02 |  | attention, fp4, mla |
| [#14869](../sources/prs/TensorRT-LLM/PR-14869.md) | [None][perf] Use a Triton kernel for Cpp mamba hybrid state update | 2026-06-02 |  |  |
| [#14775](../sources/prs/TensorRT-LLM/PR-14775.md) | [TRTLLM-12288][feat] Support Nemotron-H nvfp4 ckpt on Hopper | 2026-05-30 | pipeline-stages, swizzling | block-scale, fp4, fp8 |
| [#14668](../sources/prs/TensorRT-LLM/PR-14668.md) | [https://nvbugs/5970614][fix] Sync CTA before PDL trigger in quantize_with_block_size | 2026-05-28 | kernel-fusion | block-scale, fp4, fp8 |
| [#14602](../sources/prs/TensorRT-LLM/PR-14602.md) | [TRTLLM-35882][feat] Add cute dsl gvr top-k decode kernel | 2026-05-27 | pipeline-stages | attention, reduction, scan |
| [#14608](../sources/prs/TensorRT-LLM/PR-14608.md) | [TRTLLM-12950][feat] Add MegaMoECuteDsl NVFP4 MoE backend | 2026-05-27 | kernel-fusion, persistent-kernel, pipeline-stages | block-scale, clc, fp4 |
| [#14652](../sources/prs/TensorRT-LLM/PR-14652.md) | [https://nvbugs/6194552][fix] stabilize Triton Mamba softplus | 2026-05-27 |  |  |
| [#14548](../sources/prs/TensorRT-LLM/PR-14548.md) | [None][perf] Fuse FlashInfer GDN prefill state I/O into Triton kernels | 2026-05-26 |  |  |
| [#14590](../sources/prs/TensorRT-LLM/PR-14590.md) | [TRTLLM-12214][perf] customMoeRoutingKernel: lower BLOCK_SIZE to 128, raise maxNumBlocks | 2026-05-26 |  | fp8, moe, topk |
| [#14591](../sources/prs/TensorRT-LLM/PR-14591.md) | [TRTLLM-12214][perf] DeepGemmFusedMoE: skip redundant data expand via fused expand+quant Triton kernel | 2026-05-26 | kernel-fusion, pipeline-stages | fp8, gemm, moe |
| [#14592](../sources/prs/TensorRT-LLM/PR-14592.md) | [TRTLLM-12214][perf] DeepGemmFusedMoE: fuse masked gather + finalize-scale into one Triton kernel | 2026-05-26 | kernel-fusion, pipeline-stages | fp8, gemm, moe |
| [#14509](../sources/prs/TensorRT-LLM/PR-14509.md) | [None][fix] Stabilize Mamba replay state update | 2026-05-25 | double-buffering |  |
| [#14529](../sources/prs/TensorRT-LLM/PR-14529.md) | [TRTLLM-12949][refactor] visual_gen: unify fused QK-norm+rope dispatch | 2026-05-25 |  | attention |
| [#14537](../sources/prs/TensorRT-LLM/PR-14537.md) | [https://nvbugs/6168859][fix] move tinygemm PDL release after reduction | 2026-05-25 |  | reduction |
| [#14459](../sources/prs/TensorRT-LLM/PR-14459.md) | [https://nvbugs/6117811][fix] Fix XQA IMA for invalid pages with sliding window | 2026-05-22 |  |  |
| [#14396](../sources/prs/TensorRT-LLM/PR-14396.md) | [None][perf] Cascade attention impl faster than MMHA 4.6x | 2026-05-21 | double-buffering, pipeline-stages | attention, fp8, gemm |
| [#14354](../sources/prs/TensorRT-LLM/PR-14354.md) | [None][chore] Use CUDA 13 CUTLASS DSL package | 2026-05-20 |  | block-scale |
| [#14279](../sources/prs/TensorRT-LLM/PR-14279.md) | [None][refactor] Add derived properties for the thop.attention call site | 2026-05-19 |  | attention, fp8, mla |
| [#14280](../sources/prs/TensorRT-LLM/PR-14280.md) | [TRTLLM-12347][feat] enable VSA in VisualGen | 2026-05-19 | pipeline-stages, swizzling, tile-scheduling | attention, flash-attention, gemm |
| [#14291](../sources/prs/TensorRT-LLM/PR-14291.md) | [None][feat] Update the logic of FMHA JIT path | 2026-05-19 | pipeline-stages, swizzling, tile-scheduling | attention, clc, flash-attention |
| [#14268](../sources/prs/TensorRT-LLM/PR-14268.md) | [None][feat] Indexer TopK: single-block / multi-pass radix | 2026-05-18 |  | scan, sort, topk |
| [#14219](../sources/prs/TensorRT-LLM/PR-14219.md) | [None][feat] DSv4: enable GVR Heuristic Top-K for compress_ratio=4 | 2026-05-17 |  | attention, mla, reduction |
| [#14194](../sources/prs/TensorRT-LLM/PR-14194.md) | [#12702][feat] Autodeploy deprecate the legacy triton attention | 2026-05-15 | pipeline-stages | attention, fp8, reduction |
| [#14197](../sources/prs/TensorRT-LLM/PR-14197.md) | [TRTLLM-12706][perf] Optimize beam search candidate reconstruction by skipping prompt-prefix copies | 2026-05-15 |  |  |
| [#14133](../sources/prs/TensorRT-LLM/PR-14133.md) | [TRTLLM-35237][feat] Tune cute dsl paged MQA logits decode kernel | 2026-05-14 |  | attention, fp4, fp8 |
| [#14134](../sources/prs/TensorRT-LLM/PR-14134.md) | [None][feat] Add chunked prefill support for Gemma4 (text + vision multimodal) | 2026-05-14 |  | attention, moe |
| [#14060](../sources/prs/TensorRT-LLM/PR-14060.md) | [TRTLLM-12027][feat] Disagg serving support with block reuse ON for hybrid models | 2026-05-13 |  | attention |
| [#14047](../sources/prs/TensorRT-LLM/PR-14047.md) | [None][feat] KVCacheManagerV2 C++ translation | 2026-05-12 | pipeline-stages | sort |
| [#13975](../sources/prs/TensorRT-LLM/PR-13975.md) | [None][perf] Add CUDA q_b norm for DeepSeek V4 | 2026-05-11 |  |  |
| [#13978](../sources/prs/TensorRT-LLM/PR-13978.md) | [TRTLLM-11457][feat] Async Ulysses pipeline (Enabled for LTX-2 + WAN) | 2026-05-11 | pipeline-stages, swizzling | attention, fp4, gemm |
| [#13985](../sources/prs/TensorRT-LLM/PR-13985.md) | [TRTLLM-12580][perf] ltx2: fused RMSNorm+RoPE across all attention paths + PE pre-shard | 2026-05-11 | kernel-fusion, pipeline-stages | attention, fp4, gemm |
| [#13929](../sources/prs/TensorRT-LLM/PR-13929.md) | [TRTLLM-35237][feat] Add cute dsl FP4 paged MQA logits decode kernel | 2026-05-09 |  | attention, fp4, fp8 |
| [#13938](../sources/prs/TensorRT-LLM/PR-13938.md) | [None][feat] Keep DSv4 o_a_proj as FP8, and port vLLM's fused_inv_rope_fp8_quant | 2026-05-09 | kernel-fusion | attention, block-scale, fp8 |
| [#13892](../sources/prs/TensorRT-LLM/PR-13892.md) | [None][perf] mHC fused_hc kernel optimizations + DS-V4 entry-boundary RMSNorm fold-in | 2026-05-08 | pipeline-stages, swizzling | attention, mbarrier, moe |
| [#13833](../sources/prs/TensorRT-LLM/PR-13833.md) | [None][perf] FC2 DenseGEMM autotune: split-K, swap_ab, fine-grained tuning buckets | 2026-05-07 | pipeline-stages, swizzling | fp4, gemm, moe |
| [#13811](../sources/prs/TensorRT-LLM/PR-13811.md) | [None][feat] Indexer topk opt | 2026-05-06 |  | sort, topk |
| [#13761](../sources/prs/TensorRT-LLM/PR-13761.md) | [None][perf] Optimize DeepSeek-V4 compressor BF16 input | 2026-05-05 |  |  |
| [#13767](../sources/prs/TensorRT-LLM/PR-13767.md) | [None][fix] Plumb swiglu_limit through DeepGEMM and TRTLLMGen FP8 fused MoE | 2026-05-05 |  | block-scale, fp8, moe |
| [#13771](../sources/prs/TensorRT-LLM/PR-13771.md) | [None][fix] Fix fused MHC for DeepSeek-V4-Pro hidden size | 2026-05-05 |  | tcgen05 |
| [#13721](../sources/prs/TensorRT-LLM/PR-13721.md) | [TRTLLM-12436][feat] visual_gen: add CuTe DSL attention via exported binaries | 2026-05-04 |  | attention, flash-attention, fp8 |
| [#13740](../sources/prs/TensorRT-LLM/PR-13740.md) | [https://nvbugs/6108841][fix] add hidden_dim=6144 router GEMM instantiation for GLM-5 | 2026-05-04 |  | fp8, gemm, moe |
| [#13628](../sources/prs/TensorRT-LLM/PR-13628.md) | [None][feat] Fuse FP8 1x128 quantize + UE8M0 scale pack on SM100 | 2026-04-30 | kernel-fusion | attention, block-scale, fp8 |
| [#13630](../sources/prs/TensorRT-LLM/PR-13630.md) | [#13580][fix] AutoDeploy: Support Gemma3n/4 E2B variants | 2026-04-30 |  | attention, fp8 |
| [#13645](../sources/prs/TensorRT-LLM/PR-13645.md) | [None][feat] Enable flashifner gdn decoding kernel for qwen3.5 | 2026-04-30 |  | fp4, nvfp4, quantization |
| [#13652](../sources/prs/TensorRT-LLM/PR-13652.md) | [None][feat] Add DeepSeekV4 attention kernels | 2026-04-30 |  | attention, flash-attention, mla |
| [#13559](../sources/prs/TensorRT-LLM/PR-13559.md) | [None][feat] Add Laguna model support (Poolside Laguna-XS.2) | 2026-04-28 |  | attention, block-scale, fp4 |
| [#13476](../sources/prs/TensorRT-LLM/PR-13476.md) | [TRTLLM-12242][feat] Add Marlin NVFP4 backend for MoE and Linear on Hopper | 2026-04-26 | double-buffering, pipeline-stages, swizzling | attention, block-scale, fp4 |
| [#13477](../sources/prs/TensorRT-LLM/PR-13477.md) | [None][perf] Scheme X L2-aware dispatcher and PDL launchers for sparse-attention GVR Top-K | 2026-04-26 | pipeline-stages | attention, reduction, sort |
| [#13426](../sources/prs/TensorRT-LLM/PR-13426.md) | [None][perf] EAGLE3 dynamic tree kernel optimizations | 2026-04-24 |  |  |
| [#13433](../sources/prs/TensorRT-LLM/PR-13433.md) | [None][perf] Extend customMoeRouting kernel to support Qwen3.5 | 2026-04-24 |  | fp4, moe, nvfp4 |
| [#13340](../sources/prs/TensorRT-LLM/PR-13340.md) | [None][feat] Integrate FP4 indexer for DSA on Blackwell | 2026-04-22 | kernel-fusion | attention, fp4, fp8 |
| [#13219](../sources/prs/TensorRT-LLM/PR-13219.md) | [TRTLLM-34871][feat] Add cute dsl FP8 paged MQA logits decode kernel | 2026-04-20 | persistent-kernel, pipeline-stages, swizzling | attention, fp8, gemm |
| [#13103](../sources/prs/TensorRT-LLM/PR-13103.md) | [None][feat] Optimize causal_conv1d prefill and decode kernels | 2026-04-16 |  |  |
| [#13117](../sources/prs/TensorRT-LLM/PR-13117.md) | [None][feat] Add FP4 residual quantization kernel without channel reo… | 2026-04-16 | swizzling | fp4, fp8, gemm |
| [#13033](../sources/prs/TensorRT-LLM/PR-13033.md) | [None][feat] Update rms_norm + fp4_qaunt kernel supporting more dim | 2026-04-14 | swizzling | fp4, moe, nvfp4 |
| [#13052](../sources/prs/TensorRT-LLM/PR-13052.md) | [#12716][feat] Fused cross-head QK Norm + RoPE kernel for WAN | 2026-04-14 | kernel-fusion | attention, reduction |
| [#12958](../sources/prs/TensorRT-LLM/PR-12958.md) | [TRTLLM-11538][feat] Blackwell custom mask fmha support | 2026-04-12 |  | attention, flash-attention, fp8 |
| [#12946](../sources/prs/TensorRT-LLM/PR-12946.md) | [#12784][feat] AutoDeploy: Optimize DeepSeek-R1 model performance | 2026-04-11 |  | attention, mla, moe |
| [#12937](../sources/prs/TensorRT-LLM/PR-12937.md) | [TRTLLM-11485][feat] Feature rework: Add SageAttention refreshed kernels (attentionOp only) | 2026-04-10 |  | attention, fp8, quantization |
| [#12884](../sources/prs/TensorRT-LLM/PR-12884.md) | [TRTLLM-11585][feat] Add CUTEDSL moe backend for nemotron-h | 2026-04-09 |  | block-scale, gemm, grouped-gemm |
| [#12731](../sources/prs/TensorRT-LLM/PR-12731.md) | [None][feat] Optimize mamba SSD prefill and extend flashinfer dispatch | 2026-04-03 |  | moe, topk |
| [#12733](../sources/prs/TensorRT-LLM/PR-12733.md) | [None][refactor] Unify sparse attention framework with clean backend interfaces | 2026-04-03 |  | attention, flash-attention, fp8 |
| [#12642](../sources/prs/TensorRT-LLM/PR-12642.md) | [None][feat] Add triton paged attention for AutoDeploy | 2026-04-01 | pipeline-stages | attention, reduction |
| [#12612](../sources/prs/TensorRT-LLM/PR-12612.md) | [None][feat] Trtllm-gen FMHA JIT support | 2026-03-31 |  | attention, flash-attention, mla |
| [#12581](../sources/prs/TensorRT-LLM/PR-12581.md) | [https://nvbugs/5983390][perf] Multiple host perf optimizations for DSA part | 2026-03-30 |  | attention, fp8, sparse-attention |
| [#12537](../sources/prs/TensorRT-LLM/PR-12537.md) | [None][feat] Add Mamba2 MTP SSM cache CUDA kernel for tree-based speculative decoding | 2026-03-25 |  |  |
| [#12470](../sources/prs/TensorRT-LLM/PR-12470.md) | [None][feat] Support sparse mqa/gqa attention | 2026-03-24 |  | attention, flash-attention, mla |
| [#12506](../sources/prs/TensorRT-LLM/PR-12506.md) | [None][feat] Add PDL support to CuTE DSL top-k kernels | 2026-03-24 |  | gemm, topk |
| [#12456](../sources/prs/TensorRT-LLM/PR-12456.md) | [None][perf] add Dynamic SMEM block routing in MOE | 2026-03-23 |  | block-scale, moe, scan |
| [#12385](../sources/prs/TensorRT-LLM/PR-12385.md) | [None][feat] Temporally-Correlated Heuristic-guided Indexer TopK for Sparse Attention | 2026-03-20 |  | attention, fp4, nvfp4 |
| [#12354](../sources/prs/TensorRT-LLM/PR-12354.md) | [TRTLLM-10407][perf] Add cute dsl single pass multi cta cluster topk | 2026-03-19 |  | quantization, sort, topk |
| [#12320](../sources/prs/TensorRT-LLM/PR-12320.md) | [None][feat] Support update weight for nvfp4 | 2026-03-18 |  | attention, block-scale, fp4 |
| [#12322](../sources/prs/TensorRT-LLM/PR-12322.md) | [https://nvbugs/5983390][perf] Kernel fusions in _gather_k_cache_for_chunk of Indexer in DSA | 2026-03-18 | kernel-fusion | attention, fp4, fp8 |
| [#12236](../sources/prs/TensorRT-LLM/PR-12236.md) | [TRTLLM-10407][perf] Enable CuteDSL indexer_top_k in model | 2026-03-16 |  | reduction, sort, topk |
| [#12136](../sources/prs/TensorRT-LLM/PR-12136.md) | [None][feat] Add DWDP (Distributed Weight Data Parallelism) support for MoE inference | 2026-03-12 | double-buffering | block-scale, fp4, gemm |
| [#12062](../sources/prs/TensorRT-LLM/PR-12062.md) | [TRTLLM-11540][feat] Add EAGLE3 dynamic tree speculative decoding support | 2026-03-10 |  | attention, flash-attention, topk |
| [#12074](../sources/prs/TensorRT-LLM/PR-12074.md) | [TRTLLM-11289][feat] Integrate CuteDSL's bf16 dense GEMMs | 2026-03-10 | pipeline-stages, swizzling, tile-scheduling | attention, fp4, gemm |
| [#12079](../sources/prs/TensorRT-LLM/PR-12079.md) | [None][feat] CuteDSL MOE: Add raster along M/N support for blockscaled contiguous backbone kernel | 2026-03-10 | persistent-kernel, swizzling, tile-scheduling | block-scale, gemm, moe |
| [#11943](../sources/prs/TensorRT-LLM/PR-11943.md) | [TRTLLM-12427][perf] Qwen2.5/3/3.5-VL Performance Optimization | 2026-03-05 |  | attention, fp8, reduction |
| [#11897](../sources/prs/TensorRT-LLM/PR-11897.md) | [TRTLLM-10990][feat] Fuse SwiGLU and quant into shared expert | 2026-03-04 | kernel-fusion | fp4, fp8, gemm |
| [#11899](../sources/prs/TensorRT-LLM/PR-11899.md) | [TRTLLM-10421][perf] Add fused cat+fp8_quantize CUDA kernel for DSA indexer | 2026-03-04 | kernel-fusion | fp8, quantization, reduction |
| [#11900](../sources/prs/TensorRT-LLM/PR-11900.md) | [TRTLLM-10407][feat] Integrate CuTE DSL top-k kernel for Blackwell | 2026-03-04 |  | scan, sort, topk |
| [#11869](../sources/prs/TensorRT-LLM/PR-11869.md) | [None][feat] Add fused DiT QK Norm + RoPE CUDA kernel for FLUX | 2026-03-03 | kernel-fusion | attention, fp4, fp8 |
| [#11733](../sources/prs/TensorRT-LLM/PR-11733.md) | [https://nvbugs/5799917][fix] Recover from CUTLASS MoE doActivation perf regression for MXFP4/NVFP4 dtype | 2026-02-26 | pipeline-stages | fp4, moe, nvfp4 |
| [#11697](../sources/prs/TensorRT-LLM/PR-11697.md) | [TRTLLM-11092][feat] add support for visual gen FA4 attention backend | 2026-02-25 | double-buffering, pipeline-stages, swizzling | attention, flash-attention, fp4 |
| [#11718](../sources/prs/TensorRT-LLM/PR-11718.md) | [TRTLLM-11119][feat] Blackwell SageAttention, Integrate into AttentionOp API | 2026-02-25 | pipeline-stages | attention, flash-attention, fp8 |
| [#11501](../sources/prs/TensorRT-LLM/PR-11501.md) | [None][feat] TRT-LLM Gen MoE finalize kernel optimization | 2026-02-13 | pipeline-stages | block-scale, moe |
| [#11510](../sources/prs/TensorRT-LLM/PR-11510.md) | [None][feat] Add support for expert_number<=2048 and K<=32 | 2026-02-13 | pipeline-stages | block-scale, moe, reduction |
| [#11473](../sources/prs/TensorRT-LLM/PR-11473.md) | [None][feat] Optimize by fuse nvfp4_quant to layernorm_gated for mamba2_mixer | 2026-02-12 | pipeline-stages, swizzling | fp4, nvfp4, quantization |
| [#11273](../sources/prs/TensorRT-LLM/PR-11273.md) | [None][feat] Optimize super-v3 nvfp4 for better perf | 2026-02-04 | kernel-fusion, pipeline-stages, swizzling | attention, flash-attention, fp4 |
| [#11181](../sources/prs/TensorRT-LLM/PR-11181.md) | [https://nvbugs/5854860][fix] Fix cutedsl argmax on sm120 | 2026-02-02 | pipeline-stages |  |
| [#11165](../sources/prs/TensorRT-LLM/PR-11165.md) | [https://nvbugs/5799917][fix] Recover from CUTLASS MoE doActivation perf regression for MXFP4/NVFP4 dtype | 2026-01-31 | pipeline-stages | fp4, fp8, moe |
| [#11143](../sources/prs/TensorRT-LLM/PR-11143.md) | [None][feat] fuse shared to sparse experts in TRT-LLM Gen MoE | 2026-01-30 | pipeline-stages | block-scale, moe, topk |
| [#10987](../sources/prs/TensorRT-LLM/PR-10987.md) | [TRTLLM-9831][perf] Use TMA.RED to improve effective memory bandwidth | 2026-01-26 | pipeline-stages, swizzling | block-scale, gemm, reduction |
| [#10742](../sources/prs/TensorRT-LLM/PR-10742.md) | [https://nvbugs/5669671][fix] Support GuidedDecoder with sharded logits (pick #10698) | 2026-01-16 | pipeline-stages |  |
| [#10476](../sources/prs/TensorRT-LLM/PR-10476.md) | [TRTLLM-10276][feat] Integrate cutedsl argmax kernel | 2026-01-07 |  | mbarrier, reduction |
| [#10479](../sources/prs/TensorRT-LLM/PR-10479.md) | [None] [feat] Add densegemm backend for MoE | 2026-01-07 | pipeline-stages, swizzling, tile-scheduling | block-scale, fp4, gemm |
| [#10429](../sources/prs/TensorRT-LLM/PR-10429.md) | [None] [feat] Add test script and raster M for gather fc1 kernel | 2026-01-06 | persistent-kernel, pipeline-stages, swizzling | block-scale |
| [#10327](../sources/prs/TensorRT-LLM/PR-10327.md) | [None][fix] impl fused triton kernel for e8m0 resmooth to reduce memory footprint | 2025-12-29 | pipeline-stages | fp8, quantization |
| [#10264](../sources/prs/TensorRT-LLM/PR-10264.md) | [TRTLLM-10022][feat] Add hopper xqa decode support for skip softmax attention | 2025-12-24 | pipeline-stages | attention |
| [#10190](../sources/prs/TensorRT-LLM/PR-10190.md) | [None][feat] sm100 weight-only kernel | 2025-12-22 | pipeline-stages, swizzling, warp-specialization | clc, fp8, gemm |
| [#10201](../sources/prs/TensorRT-LLM/PR-10201.md) | [TRTLLM-9831][perf] Enable 2CTA with autotune for CuteDSL MoE and Grouped GEMM optimizations | 2025-12-22 | double-buffering, pipeline-stages | block-scale, gemm, grouped-gemm |
| [#10130](../sources/prs/TensorRT-LLM/PR-10130.md) | [TRTLLM-9457][feat] Add cute dsl fp8 gemm for Blackwell | 2025-12-18 | pipeline-stages | fp4, fp8, gemm |
| [#10088](../sources/prs/TensorRT-LLM/PR-10088.md) | [None][feat] CuteDSL MOE FC1 Enhancement | 2025-12-17 | double-buffering, pipeline-stages, tile-scheduling | block-scale, gemm, moe |
| [#10042](../sources/prs/TensorRT-LLM/PR-10042.md) | [None][perf] Add more optimization options for MOE CuteDSL finalized kernel | 2025-12-16 | double-buffering, persistent-kernel, pipeline-stages | block-scale, grouped-gemm, moe |
| [#10043](../sources/prs/TensorRT-LLM/PR-10043.md) | [TRTLLM-9992][perf] Enable PDL for CuteDSL kernels and overlap MoeOutputMemset | 2025-12-16 | persistent-kernel, pipeline-stages | block-scale, moe |
| [#9905](../sources/prs/TensorRT-LLM/PR-9905.md) | [None][feat] Adding torch ext API for FusedAddRMSNormQuant kernel | 2025-12-11 | kernel-fusion, pipeline-stages | fp4, quantization |
| [#9924](../sources/prs/TensorRT-LLM/PR-9924.md) | [TRTLLM-9493][feat] Add helixPostProcessNative kernel for cp_dim=2 | 2025-12-11 | pipeline-stages |  |
| [#9838](../sources/prs/TensorRT-LLM/PR-9838.md) | [https://nvbugs/5726962][feat] Apply fusion for W4AFP8_AWQ MoE | 2025-12-09 | epilogue-fusion, pipeline-stages | block-scale, fp4, fp8 |
| [#9852](../sources/prs/TensorRT-LLM/PR-9852.md) | [None][feat] Fused kernels (qknormrope + moe routing) and two-model MTP support for glm4moe | 2025-12-09 | kernel-fusion, pipeline-stages | attention, fp4, moe |
| [#9854](../sources/prs/TensorRT-LLM/PR-9854.md) | [None][feat] Port fp4 quantization kernel optimization from FlashInfer | 2025-12-09 | pipeline-stages, swizzling | block-scale, fp4, quantization |
| [#9618](../sources/prs/TensorRT-LLM/PR-9618.md) | [TRTLLM-9685] [feat] Add gather fc1 kernel by cuteDSL | 2025-12-02 | pipeline-stages | block-scale, fp4, gemm |
| [#9175](../sources/prs/TensorRT-LLM/PR-9175.md) | [None][feat] TRT-LLM Gen MoE optimize DeepSeek Fp8 activation kernel | 2025-11-14 | pipeline-stages | block-scale, fp8, moe |
| [#9087](../sources/prs/TensorRT-LLM/PR-9087.md) | [None][fix] support topk autotuner input for expert slot per group larger than 32 | 2025-11-12 | pipeline-stages | block-scale, fp4, moe |
| [#8620](../sources/prs/TensorRT-LLM/PR-8620.md) | [None][feat] Enable nvfp4 cuda core for sm120 | 2025-10-23 | pipeline-stages | fp4, gemm, nvfp4 |
| [#8501](../sources/prs/TensorRT-LLM/PR-8501.md) | [None][fix] Fix the performance issue of FP8 blockwise grouped GEMM when using attention DP | 2025-10-20 | pipeline-stages | attention, block-scale, fp8 |
| [#8405](../sources/prs/TensorRT-LLM/PR-8405.md) | [TRTLLM-8535][feat] Support DeepSeek V3.2 with FP8 + BF16 KV cache/NVFP4 + BF16 KV cache | 2025-10-16 | pipeline-stages | attention, fp4, fp8 |
| [#7937](../sources/prs/TensorRT-LLM/PR-7937.md) | [None][feat] GPT-OSS Sm120/Sm121 Support | 2025-09-23 | pipeline-stages | attention, flash-attention, fp4 |
| [#7755](../sources/prs/TensorRT-LLM/PR-7755.md) | [None][fix] Fix and add test for TRTLLM MoE backend | 2025-09-16 | pipeline-stages | block-scale, fp8, moe |
| [#7761](../sources/prs/TensorRT-LLM/PR-7761.md) | [TRTLLM-8637][feat] Optimize the routing kernel for DeepseekV3 (MoE CUTLASS backend); Add support for 384 experts (MoE TRTLLM backend) | 2025-09-16 | pipeline-stages | block-scale, moe, reduction |
| [#7524](../sources/prs/TensorRT-LLM/PR-7524.md) | [None][chore] Fix kernel launch param and add TRTLLM MoE backend test | 2025-09-04 | pipeline-stages | block-scale, fp4, fp8 |
| [#6809](../sources/prs/TensorRT-LLM/PR-6809.md) | [OMNIML-2336][feat] Add NVFP4 x FP8 | 2025-08-12 | pipeline-stages, swizzling | fp4, fp8, gemm |
| [#4867](../sources/prs/TensorRT-LLM/PR-4867.md) | feat: Add w4a8_mxfp4_fp8 quantization recipe. | 2025-06-03 | persistent-kernel, pipeline-stages, tile-scheduling | fp4, gemm, quantization |

<a id="nvidiacccl"></a>
## NVIDIA/cccl
625 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#12094](../sources/prs/cccl/PR-12094.md) | [Version] Update main to v3.7.0 | 2026-10-20 |  |  |
| [#12070](../sources/prs/cccl/PR-12070.md) | [cudax] Rename `make_cg_equivalent_group` to `make_group` | 2026-10-19 |  |  |
| [#12076](../sources/prs/cccl/PR-12076.md) | [CUB][Refactor] Moves shared top-k radix-pass helpers into `cub/detail/topk_helpers.cuh` | 2026-10-19 |  | sort, topk |
| [#12084](../sources/prs/cccl/PR-12084.md) | Remove CUDA runtime headers | 2026-10-19 |  |  |
| [#12085](../sources/prs/cccl/PR-12085.md) | [CUB] Fix two CUB header inclusion cycles | 2026-10-19 |  |  |
| [#12060](../sources/prs/cccl/PR-12060.md) | Recoups performance for `+/-0.0` float normalization in `DeviceBatchedTopK` | 2026-10-18 |  | sort, topk |
| [#12063](../sources/prs/cccl/PR-12063.md) | Reject unsupported `tie_break` requests in `cub::DeviceTopK` | 2026-10-18 |  |  |
| [#12011](../sources/prs/cccl/PR-12011.md) | [QA Agent] BlockHistogram findings | 2026-10-15 |  |  |
| [#12013](../sources/prs/cccl/PR-12013.md) | [CUB] Refactor `cub::DeviceHistogram` to always take an environment  | 2026-10-15 |  |  |
| [#12015](../sources/prs/cccl/PR-12015.md) | [cudax] Rework optional participation in groups | 2026-10-15 |  |  |
| [#12001](../sources/prs/cccl/PR-12001.md) | cccl-modernize-type-trait | 2026-10-14 |  |  |
| [#12004](../sources/prs/cccl/PR-12004.md) | Reenable HW warp redux min/max f32 | 2026-10-14 |  |  |
| [#12009](../sources/prs/cccl/PR-12009.md) | Apply clang-tidy `misc-include-cleaner` to `iterator`, `memory`, `exception`, `execution` | 2026-10-14 |  |  |
| [#11994](../sources/prs/cccl/PR-11994.md) | [STF] Locality-domain tests: single-domain devices have nothing to split | 2026-10-13 |  |  |
| [#11995](../sources/prs/cccl/PR-11995.md) | [Cub] Modularize util_type | 2026-10-13 | double-buffering | scan, sort |
| [#11983](../sources/prs/cccl/PR-11983.md) | [cudax] Remove `invalid()` member functions from synchronizer instances | 2026-10-12 |  |  |
| [#11963](../sources/prs/cccl/PR-11963.md) | [libc++] Define _CCCL_PTX_ARCH for NVHPC | 2026-10-09 |  |  |
| [#11964](../sources/prs/cccl/PR-11964.md) | Selectively merge Thrust's reduce_by_key default tuning into CUB | 2026-10-09 |  |  |
| [#11973](../sources/prs/cccl/PR-11973.md) | Change cub device radix sort to always take an env | 2026-10-09 |  | sort |
| [#11974](../sources/prs/cccl/PR-11974.md) | Optimize `WarpReduce` for floating-point types (Min/Max) | 2026-10-09 |  | reduction |
| [#11975](../sources/prs/cccl/PR-11975.md) | [cudax][cuco] Stop unnecessary probing in for_each | 2026-10-09 |  |  |
| [#11943](../sources/prs/cccl/PR-11943.md) | Consolidate and remove various overlaping type-trait implementations | 2026-10-08 |  |  |
| [#11951](../sources/prs/cccl/PR-11951.md) | `warp_redux` uses `is_integer` instead of `is_integral` | 2026-10-08 |  |  |
| [#11956](../sources/prs/cccl/PR-11956.md) | [fp] Promote the FP component from cuda::experimental:: to cuda:: | 2026-10-08 |  |  |
| [#11911](../sources/prs/cccl/PR-11911.md) | [stf] Fix nvcc 12.0 + gcc 12 + C++17 crashes | 2026-10-07 |  |  |
| [#11914](../sources/prs/cccl/PR-11914.md) | [CUB] Rename phaseInOutW to phaseInOutL in warpspeed scan | 2026-10-07 |  |  |
| [#11923](../sources/prs/cccl/PR-11923.md) | [cub] Fix scan reduction for `AccumT` without identity element | 2026-10-07 |  | reduction |
| [#11933](../sources/prs/cccl/PR-11933.md) | [libcu++]Refactor no-throw driver APIs to be actually no-throw | 2026-10-07 |  |  |
| [#11934](../sources/prs/cccl/PR-11934.md) | Apply clang-tidy `misc-include-cleaner` to cuda/std math functionalities | 2026-10-07 |  |  |
| [#11891](../sources/prs/cccl/PR-11891.md) | Add cub::detail::DeviceSetOps pairs APIs | 2026-10-06 |  |  |
| [#11903](../sources/prs/cccl/PR-11903.md) | [cudax] Fix minimum thread scope for cluster level | 2026-10-06 |  |  |
| [#11906](../sources/prs/cccl/PR-11906.md) | Add sm107 tunings for DeviceFind::FindIf | 2026-10-06 |  |  |
| [#11853](../sources/prs/cccl/PR-11853.md) | [libcu++] Expose `cuda::std::constant_wrapper` | 2026-10-05 |  |  |
| [#11860](../sources/prs/cccl/PR-11860.md) | Include device_segmented_scan.cuh in cub/cub.cuh | 2026-10-05 |  |  |
| [#11862](../sources/prs/cccl/PR-11862.md) | [libcu++] Cleanup threading support | 2026-10-05 |  |  |
| [#11872](../sources/prs/cccl/PR-11872.md) | Read back CUB test/example results on the producing stream | 2026-10-05 |  |  |
| [#11873](../sources/prs/cccl/PR-11873.md) | [cudax][cuco] Use 1D hierarchy queries for bulk kernels | 2026-10-05 |  |  |
| [#11876](../sources/prs/cccl/PR-11876.md) | Remove deprecated rle_non_trivial_runs_policy alias | 2026-10-05 |  |  |
| [#11878](../sources/prs/cccl/PR-11878.md) | Use vote instructions in `WarpReduce` | 2026-10-05 |  | reduction |
| [#11879](../sources/prs/cccl/PR-11879.md) | [cudax][cuco] Skip redundant erased-key checks during insertion | 2026-10-05 |  |  |
| [#11835](../sources/prs/cccl/PR-11835.md) | Treat -0.0 and +0.0 as equal in DeviceBatchedTopK ranking | 2026-10-03 |  | topk |
| [#11843](../sources/prs/cccl/PR-11843.md) | [cudax] Fix simple groups example | 2026-10-03 |  |  |
| [#11844](../sources/prs/cccl/PR-11844.md) | Add cub::detail::DeviceSetOps::SetIntersection (keys) | 2026-10-03 |  |  |
| [#11845](../sources/prs/cccl/PR-11845.md) | Add cub::detail::DeviceSetOps::SetSymmetricDifference (keys) | 2026-10-03 |  |  |
| [#11808](../sources/prs/cccl/PR-11808.md) | Retune sm107 lookahead scan tuning for i128 inputs | 2026-10-02 |  |  |
| [#11822](../sources/prs/cccl/PR-11822.md) | Add cub::detail::DeviceSetOps::SetUnion (keys) | 2026-10-02 |  |  |
| [#11826](../sources/prs/cccl/PR-11826.md) | Tune the sm100 lookahead scan for int64 | 2026-10-02 |  |  |
| [#11827](../sources/prs/cccl/PR-11827.md) | Optimize WarpReduce for large integers (Min/Max) | 2026-10-02 |  | reduction |
| [#11779](../sources/prs/cccl/PR-11779.md) | [cudax] Simplify `cudax::coop::make_this_group` | 2026-10-01 |  |  |
| [#11780](../sources/prs/cccl/PR-11780.md) | [cudax] Fix `is_part_of` query exec space | 2026-10-01 |  |  |
| [#11781](../sources/prs/cccl/PR-11781.md) | [cudax] Fix missing includes in groups | 2026-10-01 |  |  |
| [#11783](../sources/prs/cccl/PR-11783.md) | [cudax] Tighten requirements on mapping result | 2026-10-01 |  |  |
| [#11790](../sources/prs/cccl/PR-11790.md) | [cudax] Make `static_count` query work | 2026-10-01 |  |  |
| [#11792](../sources/prs/cccl/PR-11792.md) | [cudax] Add missing `invalid()` method to barrier synchronizer instance | 2026-10-01 |  |  |
| [#11798](../sources/prs/cccl/PR-11798.md) | Update ci matrix to 13.4 | 2026-10-01 |  |  |
| [#11804](../sources/prs/cccl/PR-11804.md) | Move the bulk store of the warpspeed scan into a dedicated store squad | 2026-10-01 |  | scan, tma |
| [#11768](../sources/prs/cccl/PR-11768.md) | [cudax] Add simple groups example | 2026-09-30 |  | reduction |
| [#11770](../sources/prs/cccl/PR-11770.md) | [EASY] [STF] stream_task: releases inside guards report a failure instead of aborting | 2026-09-30 |  |  |
| [#11772](../sources/prs/cccl/PR-11772.md) | [EASY] [STF] graph_ctx: releases in fail guards and shared_ptr deleters report a failure instead of aborting | 2026-09-30 |  |  |
| [#11773](../sources/prs/cccl/PR-11773.md) | [EASY][STF] host_launch_scope, parallel_for_scope: timing events are released under a policy, not an abort | 2026-09-30 |  |  |
| [#11774](../sources/prs/cccl/PR-11774.md) | [STF] Long tail of cuda_safe_call in guards, deleters and destructors: release under notify, restore under abort | 2026-09-30 |  |  |
| [#11698](../sources/prs/cccl/PR-11698.md) | Warn on including `<cub/cub.cuh>` and replace it with targeted headers | 2026-09-29 |  |  |
| [#11717](../sources/prs/cccl/PR-11717.md) | [cudax] Rename group rank/count-related parameters | 2026-09-29 |  |  |
| [#11736](../sources/prs/cccl/PR-11736.md) | Add cub::detail::DeviceSetOps::SetDifference | 2026-09-29 |  | scan |
| [#11738](../sources/prs/cccl/PR-11738.md) | FP component housekeeping ahead of the `cuda::` promotion | 2026-09-29 |  |  |
| [#11741](../sources/prs/cccl/PR-11741.md) | Allow `baseline_topk_policy` to hold a variable number of worker policies | 2026-09-29 |  | sort |
| [#11742](../sources/prs/cccl/PR-11742.md) | [EASY] [STF] exception_policy: spell library-level throws with the CCCL exception macros | 2026-09-29 |  |  |
| [#11749](../sources/prs/cccl/PR-11749.md) | Fix [QA Agent] mdspan copy | 2026-09-29 |  |  |
| [#11750](../sources/prs/cccl/PR-11750.md) | Add sm107 tuning for DeviceTransform ublkcp | 2026-09-29 |  |  |
| [#11753](../sources/prs/cccl/PR-11753.md) | CUB should reuse libcu++ `operator_properties.h` instead of rolling its own | 2026-09-29 |  |  |
| [#11670](../sources/prs/cccl/PR-11670.md) | Fix cub::Uninitialized storage alignment for overaligned types | 2026-09-28 |  |  |
| [#11673](../sources/prs/cccl/PR-11673.md) | [CUB] Simplify `::TempStorage` to `using` aliases | 2026-09-28 |  |  |
| [#11679](../sources/prs/cccl/PR-11679.md) | Fix STF clang-tidy errors | 2026-09-28 |  |  |
| [#11682](../sources/prs/cccl/PR-11682.md) | Combine load and sched squad in warpspeed scan | 2026-09-28 |  |  |
| [#11661](../sources/prs/cccl/PR-11661.md) | Port Thrust set operation algorithms to CUB | 2026-09-27 |  |  |
| [#11662](../sources/prs/cccl/PR-11662.md) | Modernize device vector initialization in three Thrust examples | 2026-09-27 |  |  |
| [#11645](../sources/prs/cccl/PR-11645.md) | Fix [QA Agent] Cooperative reduction - Warp | 2026-09-24 |  | reduction |
| [#11646](../sources/prs/cccl/PR-11646.md) | Fix [QA Agent] Cooperative reduction - Block | 2026-09-24 |  | reduction |
| [#11651](../sources/prs/cccl/PR-11651.md) | [places] Drop the default index on the locality-domain deactivate() override | 2026-09-24 |  |  |
| [#11654](../sources/prs/cccl/PR-11654.md) | [CUB] Handle empty input in DeviceFind::FindIf | 2026-09-24 |  |  |
| [#11656](../sources/prs/cccl/PR-11656.md) | [STF] cuda_try in the remaining straight-line sites; pops complete their transition and then report | 2026-09-24 |  |  |
| [#11610](../sources/prs/cccl/PR-11610.md) | [cudax] Change how `group_by` is deduced and instantiated | 2026-09-23 |  |  |
| [#11611](../sources/prs/cccl/PR-11611.md) | [cudax] Fix missing specializations for `__is_group_mapping_v` trait | 2026-09-23 |  |  |
| [#11612](../sources/prs/cccl/PR-11612.md) | [cudax] Separate implicit hierarchy from groups | 2026-09-23 |  |  |
| [#11615](../sources/prs/cccl/PR-11615.md) | [cudax] Change how `take` is deduced and instantiated | 2026-09-23 |  |  |
| [#11622](../sources/prs/cccl/PR-11622.md) | Enable clang-tidy cppcoreguidelines-* | 2026-09-23 |  |  |
| [#11623](../sources/prs/cccl/PR-11623.md) | Optimize `WarpReduce` for large integers (Sum) | 2026-09-23 |  | reduction |
| [#11625](../sources/prs/cccl/PR-11625.md) | [cudax][cuco] Migrate insert_or_assign APIs for fixed_capacity_map | 2026-09-23 |  |  |
| [#11626](../sources/prs/cccl/PR-11626.md) | Run clang-tidy over the cudax Places subproject | 2026-09-23 |  |  |
| [#11627](../sources/prs/cccl/PR-11627.md) | `cppcoreguidelines-rvalue-reference-param-not-moved` | 2026-09-23 |  |  |
| [#11629](../sources/prs/cccl/PR-11629.md) | `cppcoreguidelines-pro-type-member-init` | 2026-09-23 |  | reduction, scan |
| [#11630](../sources/prs/cccl/PR-11630.md) | `cppcoreguidelines-pro-type-union-access` | 2026-09-23 |  |  |
| [#11631](../sources/prs/cccl/PR-11631.md) | `cppcoreguidelines-pro-type-const-cast` | 2026-09-23 |  |  |
| [#11632](../sources/prs/cccl/PR-11632.md) | `cppcoreguidelines-use-enum-class` | 2026-09-23 |  |  |
| [#11633](../sources/prs/cccl/PR-11633.md) | `cppcoreguidelines-non-private-member-variables-in-classes` | 2026-09-23 |  |  |
| [#11634](../sources/prs/cccl/PR-11634.md) | `cppcoreguidelines-pro-type-cstyle-cast` | 2026-09-23 |  |  |
| [#11635](../sources/prs/cccl/PR-11635.md) | `cppcoreguidelines-prefer-member-initializer` | 2026-09-23 |  |  |
| [#11636](../sources/prs/cccl/PR-11636.md) | `cppcoreguidelines-slicing` | 2026-09-23 |  |  |
| [#11639](../sources/prs/cccl/PR-11639.md) | `cppcoreguidelines-missing-std-forward` | 2026-09-23 |  |  |
| [#11642](../sources/prs/cccl/PR-11642.md) | [STF] Run clang-tidy over CUDA STF (measurement + backlog cleanup) | 2026-09-23 |  |  |
| [#11643](../sources/prs/cccl/PR-11643.md) | [STF] cuda_try for the straight-line CUDA calls in graph_ctx and stream_ctx | 2026-09-23 |  |  |
| [#11580](../sources/prs/cccl/PR-11580.md) | [cudax] Reorganize coop groups & algorithms | 2026-09-22 |  |  |
| [#11581](../sources/prs/cccl/PR-11581.md) | [CUB]: Move more logic into `cub::detail::log_dispatch` | 2026-09-22 |  |  |
| [#11584](../sources/prs/cccl/PR-11584.md) | [CUB] Add `_CUB_LOG_KERNEL_LAUNCH` macro and migrate kernel-launch logging | 2026-09-22 |  | scan |
| [#11585](../sources/prs/cccl/PR-11585.md) | [cub] Always dispatch with min arch tuning when compiling with `nvc++` | 2026-09-22 |  |  |
| [#11587](../sources/prs/cccl/PR-11587.md) | [CUB] Refactor `cub::DeviceMergeSort` to always take an environment | 2026-09-22 |  | sort |
| [#11589](../sources/prs/cccl/PR-11589.md) | [CUB] Refactor `cub::DeviceMerge` to always take an environment | 2026-09-22 |  |  |
| [#11590](../sources/prs/cccl/PR-11590.md) | [CUB] Refactor `cub::DeviceMemcpy` to always take an environment | 2026-09-22 |  |  |
| [#11593](../sources/prs/cccl/PR-11593.md) | [CUB] Log chosen items-per-thread and achieved bytes-in-flight in DeviceTransform async dispatch | 2026-09-22 |  |  |
| [#11598](../sources/prs/cccl/PR-11598.md) | Rename remaining non-snake_case Thrust function names and enforce via clang-tidy | 2026-09-22 |  |  |
| [#11601](../sources/prs/cccl/PR-11601.md) | Rename remaining non-snake_case Thrust data members and enforce via clang-tidy | 2026-09-22 |  |  |
| [#11549](../sources/prs/cccl/PR-11549.md) | [cudax] Add exec_place::all_locality_domains([split]) over every domain of every device | 2026-09-21 |  |  |
| [#11555](../sources/prs/cccl/PR-11555.md) | Re-enable RTX 5090 fill tuning for 8-byte stores | 2026-09-21 |  |  |
| [#11558](../sources/prs/cccl/PR-11558.md) | Rename ALL_CAPS/snake_case/camelCase CUB template parameters to PascalCase | 2026-09-21 |  | scan, sort |
| [#11559](../sources/prs/cccl/PR-11559.md) | Rename `_ALLCAPS` template parameters to `PascalCase` | 2026-09-21 |  |  |
| [#11565](../sources/prs/cccl/PR-11565.md) | Rename remaining leading/mid-underscore template parameters to PascalCase | 2026-09-21 |  | scan, topk |
| [#11523](../sources/prs/cccl/PR-11523.md) | [C Parallel v2] Fix freestanding HostJIT verification on Windows | 2026-09-20 |  |  |
| [#11479](../sources/prs/cccl/PR-11479.md) | [CUB] Compare input values in ArgMin and ArgMax | 2026-09-18 |  |  |
| [#11485](../sources/prs/cccl/PR-11485.md) | Allocate virtual shared memory in the streaming reduce-by-key dispatch | 2026-09-18 |  |  |
| [#11487](../sources/prs/cccl/PR-11487.md) | [[libcu++] Replace std::vector with a simpler alternative | 2026-09-18 |  |  |
| [#11498](../sources/prs/cccl/PR-11498.md) | Replace CUB `fast_mod_div` with `cuda::fast_mod_div` | 2026-09-18 |  |  |
| [#11506](../sources/prs/cccl/PR-11506.md) | [CUB] Thread-level Pairwise Sorting Networks | 2026-09-18 |  | sort, topk |
| [#11451](../sources/prs/cccl/PR-11451.md) | [cudax] Tighten rules for optional participation in a group | 2026-09-17 |  |  |
| [#11453](../sources/prs/cccl/PR-11453.md) | [cudax] Improve groups interop with CG | 2026-09-17 |  |  |
| [#11456](../sources/prs/cccl/PR-11456.md) | Improve diagnostics for PTX/SASS compute-capability mismatches | 2026-09-17 |  |  |
| [#11467](../sources/prs/cccl/PR-11467.md) | Enable clang-tidy readability-identifier-naming for macros and namespaces | 2026-09-17 |  |  |
| [#11468](../sources/prs/cccl/PR-11468.md) | [CUB] `DeviceCopy::Copy(mdspan)` forwards through `cuda::copy` | 2026-09-17 |  |  |
| [#11437](../sources/prs/cccl/PR-11437.md) | Remove binary version of `cub::detail::ptx_compute_cap` | 2026-09-16 |  |  |
| [#11449](../sources/prs/cccl/PR-11449.md) | [cudax][cuco] Migrate index generation and wraparound fixes | 2026-09-16 |  |  |
| [#11402](../sources/prs/cccl/PR-11402.md) | Speed up and simplify c2h RNG | 2026-09-15 |  |  |
| [#11406](../sources/prs/cccl/PR-11406.md) | [cudax] Rename missed `group` type to `generic_group` | 2026-09-15 |  |  |
| [#11419](../sources/prs/cccl/PR-11419.md) | [c2h] Fix CTK 13.0 unknown pragma warnings | 2026-09-15 |  |  |
| [#11420](../sources/prs/cccl/PR-11420.md) | Enable clang-tidy google-* | 2026-09-15 |  |  |
| [#11387](../sources/prs/cccl/PR-11387.md) | [cudax] Expose group exhaustivity/contiguity properties | 2026-09-14 |  |  |
| [#11391](../sources/prs/cccl/PR-11391.md) | [cudax][cuco] Use cuda::launch and fix noexcept specifications | 2026-09-14 |  |  |
| [#11393](../sources/prs/cccl/PR-11393.md) | [cudax] Groups renames | 2026-09-14 |  |  |
| [#11399](../sources/prs/cccl/PR-11399.md) | [cudax][cuco] Cover HyperLogLog host merge APIs | 2026-09-14 |  |  |
| [#11352](../sources/prs/cccl/PR-11352.md) | Add BlockScan::Sum benchmark covering extended floating-point types | 2026-09-11 |  | scan |
| [#11354](../sources/prs/cccl/PR-11354.md) | [cudax] Simplify invalid mapping result | 2026-09-11 |  |  |
| [#11356](../sources/prs/cccl/PR-11356.md) | [cudax] Implement `cudax::coalesced_group` | 2026-09-11 |  |  |
| [#11357](../sources/prs/cccl/PR-11357.md) | [cudax] Use `bit_fns` instead of `__fns` | 2026-09-11 |  |  |
| [#11324](../sources/prs/cccl/PR-11324.md) | [cudax] Don't require mapping's and synchronizer's special funcs to be `const` | 2026-09-10 |  |  |
| [#11330](../sources/prs/cccl/PR-11330.md) | [cudax] Fix `.map(...)` for empty `composite_mapping` | 2026-09-10 |  |  |
| [#11332](../sources/prs/cccl/PR-11332.md) | Add IKET annotations to lookback scan | 2026-09-10 |  |  |
| [#11338](../sources/prs/cccl/PR-11338.md) | Refactor C2H headers by responsibility | 2026-09-10 |  |  |
| [#11340](../sources/prs/cccl/PR-11340.md) | [cudax][cuco] Migrate host and device insert_and_find APIs for fixed_capacity_map | 2026-09-10 |  |  |
| [#11344](../sources/prs/cccl/PR-11344.md) | C2H cuda::buffer support | 2026-09-10 |  |  |
| [#11345](../sources/prs/cccl/PR-11345.md) | [cudax][cuco] Explicitly mark the open addressing destructor as host-only | 2026-09-10 |  |  |
| [#11283](../sources/prs/cccl/PR-11283.md) | Disambiguate arg-extremum reductions in the reduce tuning policy selector | 2026-09-09 |  | reduction |
| [#11284](../sources/prs/cccl/PR-11284.md) | Add key type classification to the TopK policy selector | 2026-09-09 |  | topk |
| [#11285](../sources/prs/cccl/PR-11285.md) | Add sm107 tunings for ArgMinMax | 2026-09-09 |  |  |
| [#11286](../sources/prs/cccl/PR-11286.md) | Add sm107 tunings for Device::Topk::*Keys | 2026-09-09 |  | topk |
| [#11297](../sources/prs/cccl/PR-11297.md) | Fix `DeviceBatchedTopK` launch failure (`cudaErrorInvalidDeviceFunction`) on CUDA 12.4 to 12.6 | 2026-09-09 |  |  |
| [#11321](../sources/prs/cccl/PR-11321.md) | Move `cudax::copy(mdspan)` to libcu++ | 2026-09-09 |  |  |
| [#11255](../sources/prs/cccl/PR-11255.md) | Unwrap zip_iterators in `DeviceTransform` | 2026-09-08 |  |  |
| [#11256](../sources/prs/cccl/PR-11256.md) | [cudax] places: let make_partition / make_partition_descriptor take a shape with get_data_dims() | 2026-09-08 |  |  |
| [#11257](../sources/prs/cccl/PR-11257.md) | Add IKET annotations to warpspeed scan | 2026-09-08 |  |  |
| [#11258](../sources/prs/cccl/PR-11258.md) | [cudax] Add exec_place::locality_domains(dev_id[, split]) | 2026-09-08 |  |  |
| [#11263](../sources/prs/cccl/PR-11263.md) | [CUB] `misc-const-correctness` | 2026-09-08 |  |  |
| [#11264](../sources/prs/cccl/PR-11264.md) | [CUB tests] `misc-const-correctness` | 2026-09-08 |  |  |
| [#11266](../sources/prs/cccl/PR-11266.md) | [Thrust tests] `misc-const-correctness` | 2026-09-08 |  | reduction, sort |
| [#11267](../sources/prs/cccl/PR-11267.md) | [cudax] `misc-const-correctness` | 2026-09-08 |  |  |
| [#11268](../sources/prs/cccl/PR-11268.md) | [c2h][nvbench_helper][C parallel] `misc-const-correctness` | 2026-09-08 |  |  |
| [#11273](../sources/prs/cccl/PR-11273.md) | examples: add the FP component examples under examples/cudax/fp | 2026-09-08 |  |  |
| [#11275](../sources/prs/cccl/PR-11275.md) | [CUB] Plumb value/offset types into the TopK policy selector | 2026-09-08 |  | topk |
| [#11278](../sources/prs/cccl/PR-11278.md) | Enable misc-const-correctness | 2026-09-08 |  |  |
| [#11279](../sources/prs/cccl/PR-11279.md) | Optimize `WarpReduce` for bitwise operators | 2026-09-08 |  | reduction |
| [#11235](../sources/prs/cccl/PR-11235.md) | [STF] Make the task-teardown path nothrow, from the leaves up | 2026-09-07 |  | sort |
| [#11236](../sources/prs/cccl/PR-11236.md) | [STF] Fix the cudaGraph_t shared_ptr deleter: leak and UB on failure | 2026-09-07 |  |  |
| [#11237](../sources/prs/cccl/PR-11237.md) | [STF] finalize() completes even when the synchronize fails | 2026-09-07 |  |  |
| [#11238](../sources/prs/cccl/PR-11238.md) | Simplify radix sort agent a bit | 2026-09-07 |  | sort |
| [#11229](../sources/prs/cccl/PR-11229.md) | [STF] Unify and harden the ctx callback-args resources | 2026-09-06 |  |  |
| [#11230](../sources/prs/cccl/PR-11230.md) | [STF] Batch 3: notify, not abort, for non-essential cleanup | 2026-09-06 |  |  |
| [#11224](../sources/prs/cccl/PR-11224.md) | [STF] Scope-guard batch 2: leak windows, wrong flavors, host-register UB | 2026-09-05 |  |  |
| [#11226](../sources/prs/cccl/PR-11226.md) | [STF] SCOPE(exit, name), and SCOPE(exit) throw policy | 2026-09-05 |  |  |
| [#11228](../sources/prs/cccl/PR-11228.md) | Make _CCCL_PP_THIRD variadic; use it to drop SCOPE's C++20 gate | 2026-09-05 |  |  |
| [#11197](../sources/prs/cccl/PR-11197.md) | Add sm107 tunings for DevicePartition::Flagged | 2026-09-04 |  |  |
| [#11198](../sources/prs/cccl/PR-11198.md) | Add sm107 tuning for DeviceRunLengthEncode::Encode | 2026-09-04 |  |  |
| [#11199](../sources/prs/cccl/PR-11199.md) | Topk tuning/b300 keys cluster | 2026-09-04 |  | topk |
| [#11202](../sources/prs/cccl/PR-11202.md) | [STF] use driver's memory pool for locality domains | 2026-09-04 |  |  |
| [#11206](../sources/prs/cccl/PR-11206.md) | [cudax] Enable group stacking | 2026-09-04 |  |  |
| [#11211](../sources/prs/cccl/PR-11211.md) | [cudax] Implement `cudax::interwarp_synchronizer` | 2026-09-04 |  |  |
| [#11215](../sources/prs/cccl/PR-11215.md) | [STF] cuda_safe_call<fun>(args...): introspected call forms shared with cuda_try | 2026-09-04 |  |  |
| [#11216](../sources/prs/cccl/PR-11216.md) | [cudax] Delete group's copy/move cons + assign op | 2026-09-04 |  |  |
| [#11166](../sources/prs/cccl/PR-11166.md) | Restrict sm107 select tunings to primitive and 128-bit integer inputs | 2026-09-03 |  |  |
| [#11168](../sources/prs/cccl/PR-11168.md) | Add sm107 tuning for Select::UniqueByKey | 2026-09-03 |  |  |
| [#11169](../sources/prs/cccl/PR-11169.md) | Add sm107 tunings for DeviceSelect::Flagged | 2026-09-03 |  |  |
| [#11170](../sources/prs/cccl/PR-11170.md) | Add sm107 tunings for DeviceRunLengthEncode::NonTrivialRuns | 2026-09-03 |  |  |
| [#11171](../sources/prs/cccl/PR-11171.md) | Add sm107 tuning for DeviceAdjacentDifference::SubtractLeftCopy | 2026-09-03 |  |  |
| [#11173](../sources/prs/cccl/PR-11173.md) | Add sm107 tuning for Histogram::MultiEven | 2026-09-03 |  |  |
| [#11174](../sources/prs/cccl/PR-11174.md) | Add sm107 tuning for Reduce::ByKey | 2026-09-03 |  |  |
| [#11175](../sources/prs/cccl/PR-11175.md) | Add sm107 tunings for DeviceHistogram::HistogramRange | 2026-09-03 |  |  |
| [#11177](../sources/prs/cccl/PR-11177.md) | [libcu++] Separate macros for Driver/Runtime API calls | 2026-09-03 |  |  |
| [#11179](../sources/prs/cccl/PR-11179.md) | Merge `cub::UpperBound` overloads | 2026-09-03 |  |  |
| [#11187](../sources/prs/cccl/PR-11187.md) | [STF] Harden scope guards: report-and-abort on guard-body failure, capture-guard fixes | 2026-09-03 |  |  |
| [#11104](../sources/prs/cccl/PR-11104.md) | Further optimize `cudax::copy(mdspan)` | 2026-09-02 | swizzling |  |
| [#11155](../sources/prs/cccl/PR-11155.md) | `misc-anonymous-namespace-in-header` | 2026-09-02 |  |  |
| [#11158](../sources/prs/cccl/PR-11158.md) | `misc-predictable-rand` | 2026-09-02 |  |  |
| [#11164](../sources/prs/cccl/PR-11164.md) | [CUB] A more efficient `WarpReduce` dispatch | 2026-09-02 |  | reduction |
| [#11079](../sources/prs/cccl/PR-11079.md) | Segmented Topk tuning on B200 `keys.cluster` | 2026-09-01 |  | topk |
| [#11080](../sources/prs/cccl/PR-11080.md) | Segmented TopK tuning on B300 `indexed.cluster` | 2026-09-01 |  | topk |
| [#11081](../sources/prs/cccl/PR-11081.md) | Add sm107 tunings for DeviceReduce::Min/Max | 2026-09-01 |  |  |
| [#11082](../sources/prs/cccl/PR-11082.md) | Add sm107 tunings for DeviceReduce::ArgMin/ArgMax | 2026-09-01 |  |  |
| [#11084](../sources/prs/cccl/PR-11084.md) | Add sm107 tunings for DeviceRadixSort::SortKeys | 2026-09-01 |  |  |
| [#11085](../sources/prs/cccl/PR-11085.md) | Add sm107 tunings for DeviceHistogram::Even | 2026-09-01 |  |  |
| [#11086](../sources/prs/cccl/PR-11086.md) | [libcu++] Remove cudart dependency from `cuda_error` | 2026-09-01 |  |  |
| [#11092](../sources/prs/cccl/PR-11092.md) | Add sm107 tunings for DeviceRadixSort::Pairs | 2026-09-01 |  |  |
| [#11093](../sources/prs/cccl/PR-11093.md) | Add sm107 tunings for DevicePartition::If three-way | 2026-09-01 |  |  |
| [#11095](../sources/prs/cccl/PR-11095.md) | [cudax][cuco] Migrate key-range for_each APIs for fixed_capacity_map | 2026-09-01 |  |  |
| [#11098](../sources/prs/cccl/PR-11098.md) | Clarify to some compilers that `[[noreturn]]` means `[[noreturn]]` | 2026-09-01 |  |  |
| [#11100](../sources/prs/cccl/PR-11100.md) | Add Warp `redux` min/max for Rubin | 2026-09-01 |  | reduction |
| [#11101](../sources/prs/cccl/PR-11101.md) | Αdd sm107 tunings for DevicePartition::If | 2026-09-01 |  |  |
| [#11102](../sources/prs/cccl/PR-11102.md) | Add sm107 tunings for `DeviceSelect::If/Unique` | 2026-09-01 |  |  |
| [#11064](../sources/prs/cccl/PR-11064.md) | Avoid use of `__input`/`__output` | 2026-08-31 |  |  |
| [#11068](../sources/prs/cccl/PR-11068.md) | Fix more `_CCCL_DEVICE static` -> `_CCCL_DEVICE_API` | 2026-08-31 |  |  |
| [#11070](../sources/prs/cccl/PR-11070.md) | [STF] Do not misattribute stale CUDA errors in `pin_memory`/`unpin_memory` and executable-graph updates | 2026-08-31 |  |  |
| [#11060](../sources/prs/cccl/PR-11060.md) | Reduces the latency of air-based block-level top-k | 2026-08-30 | double-buffering | sort, topk |
| [#11055](../sources/prs/cccl/PR-11055.md) | [libcu++] Try to use the _CCCL_NODEBUG attribute more often | 2026-08-28 |  |  |
| [#11056](../sources/prs/cccl/PR-11056.md) | [STF] Fix/update cond token deps | 2026-08-28 |  |  |
| [#11057](../sources/prs/cccl/PR-11057.md) | Support no_init for DeviceSegmentedReduce | 2026-08-28 |  | reduction |
| [#11042](../sources/prs/cccl/PR-11042.md) | Deprecate `[CUB|THRUST]_DEBUG_SYNC`, `CUB_DEBUG_ALL` and drop it from tests | 2026-08-27 |  |  |
| [#11043](../sources/prs/cccl/PR-11043.md) | Lookahead RunLengthEncode should write the last key of the run to be consistent with ReduceByKey | 2026-08-27 | swizzling |  |
| [#11013](../sources/prs/cccl/PR-11013.md) | [CUB] Refactor `cub::DeviceFor` to always take an environment | 2026-08-26 |  |  |
| [#11029](../sources/prs/cccl/PR-11029.md) | Add `mbarrier` wait instructions `reportValue` | 2026-08-26 |  | mbarrier |
| [#10992](../sources/prs/cccl/PR-10992.md) | Add sm107 tunings for lookahead scan | 2026-08-25 |  |  |
| [#10993](../sources/prs/cccl/PR-10993.md) | [CUB] Fix silent sample loss in DeviceHistogram for signed bytes and wide histograms | 2026-08-25 |  |  |
| [#10996](../sources/prs/cccl/PR-10996.md) | [CUB] Fix HistogramEven bin arithmetic for level ranges wider than the common type | 2026-08-25 |  |  |
| [#11004](../sources/prs/cccl/PR-11004.md) | [CUB] Fix unqualified calls to libcu++ entities | 2026-08-25 |  |  |
| [#11010](../sources/prs/cccl/PR-11010.md) | [STF] Fix box construction from arrays of integral bounds | 2026-08-25 |  |  |
| [#10964](../sources/prs/cccl/PR-10964.md) | Make every compute warp wait for the pos ring slot in RLE lookahead | 2026-08-24 |  | mbarrier |
| [#10974](../sources/prs/cccl/PR-10974.md) | Remove `_Is[Not]Same` | 2026-08-24 |  |  |
| [#10985](../sources/prs/cccl/PR-10985.md) | [cudax] Isolate and synchronize reduce scratch | 2026-08-24 |  | reduction |
| [#10955](../sources/prs/cccl/PR-10955.md) | [STF] store(target): storing the exception as a composable policy | 2026-08-22 |  |  |
| [#10923](../sources/prs/cccl/PR-10923.md) | Increase DeviceTransform min bytes in flight to 128 KiB on sm_107 | 2026-08-21 |  |  |
| [#10926](../sources/prs/cccl/PR-10926.md) | [cudax] Use `uint32_t` instead of `unsigned` in groups | 2026-08-21 |  |  |
| [#10928](../sources/prs/cccl/PR-10928.md) | [CUB] Align reduce vector buffer | 2026-08-21 |  | reduction |
| [#10929](../sources/prs/cccl/PR-10929.md) | [STF] Make empty boxes iterate as empty | 2026-08-21 |  |  |
| [#10930](../sources/prs/cccl/PR-10930.md) | [STF] Validate dim4 index extents | 2026-08-21 |  |  |
| [#10943](../sources/prs/cccl/PR-10943.md) | Constrain Rubin bytes-in-flight to not reach sm120 | 2026-08-21 |  |  |
| [#10954](../sources/prs/cccl/PR-10954.md) | [CUB]: Fix histogram bfloat16 bug and add regression test | 2026-08-21 |  |  |
| [#10909](../sources/prs/cccl/PR-10909.md) | [libcu++] Update cuda::ptx:: in main for CUDA 13.4 | 2026-08-20 |  | block-scale, mbarrier, tcgen05 |
| [#10910](../sources/prs/cccl/PR-10910.md) | [cudax] Don't store synchronizer in `group` | 2026-08-20 |  |  |
| [#10911](../sources/prs/cccl/PR-10911.md) | [cudax] Expose `implict_hierarchy[_1d]` | 2026-08-20 |  |  |
| [#10912](../sources/prs/cccl/PR-10912.md) | [Tile] Fix window CI scripts | 2026-08-20 |  |  |
| [#10914](../sources/prs/cccl/PR-10914.md) | Add cuda::__call_once now that the paradigm is used quite often | 2026-08-20 |  |  |
| [#10890](../sources/prs/cccl/PR-10890.md) | fix(cub): align temporary vector buffer to VectorT in AgentFind | 2026-08-19 |  |  |
| [#10865](../sources/prs/cccl/PR-10865.md) | [CUB] Revert "[CUB] Avoid compiler error on nonintegral __nv_atomic argument (#10623)" | 2026-08-18 |  |  |
| [#10868](../sources/prs/cccl/PR-10868.md) | [cudax] Implement `cudax::virtual_group` | 2026-08-18 |  | reduction |
| [#10870](../sources/prs/cccl/PR-10870.md) | Replace CachingDeviceAllocator in CUB examples | 2026-08-18 |  | sort, topk |
| [#10878](../sources/prs/cccl/PR-10878.md) | Deprecate CachingDeviceAllocator | 2026-08-18 |  |  |
| [#10881](../sources/prs/cccl/PR-10881.md) | [cudax] Use _CCCL_NO_UNIQUE_ADDRESS instead of [[no_unique_address]] | 2026-08-18 |  |  |
| [#10885](../sources/prs/cccl/PR-10885.md) | Remove some unused Thrust includes | 2026-08-18 |  |  |
| [#10888](../sources/prs/cccl/PR-10888.md) | [cudax][cuco] Remove noexcept from fixed_capacity_map async APIs that can throw | 2026-08-18 |  |  |
| [#10850](../sources/prs/cccl/PR-10850.md) | [cudax] Restrict generic group queries | 2026-08-17 |  |  |
| [#10812](../sources/prs/cccl/PR-10812.md) | Implement sorted outputs for segmented TopK | 2026-08-14 | kernel-fusion | sort, topk |
| [#10816](../sources/prs/cccl/PR-10816.md) | [cudax] Make `this_meow` queries a bit more flexible | 2026-08-14 |  |  |
| [#10820](../sources/prs/cccl/PR-10820.md) | [cudax] Require synchronizers to provide a view | 2026-08-14 |  |  |
| [#10824](../sources/prs/cccl/PR-10824.md) | [STF] Formalize that parallel_for on the host requires nvcc or nvc++ | 2026-08-14 |  |  |
| [#10826](../sources/prs/cccl/PR-10826.md) | [STF] Throw through _CCCL_THROW in STF and places headers | 2026-08-14 |  |  |
| [#10830](../sources/prs/cccl/PR-10830.md) | [libcudacxx][fp] add fptool: fp_custom and fpmp2_stat + unit tests | 2026-08-14 |  | reduction |
| [#10786](../sources/prs/cccl/PR-10786.md) | [STF] Add locality_domain scope to place_partition | 2026-08-13 |  |  |
| [#10787](../sources/prs/cccl/PR-10787.md) | [cudax] Implement `cudax::group_view` | 2026-08-13 |  |  |
| [#10793](../sources/prs/cccl/PR-10793.md) | Make eight STF tests and examples portable to clang-cuda | 2026-08-13 |  |  |
| [#10796](../sources/prs/cccl/PR-10796.md) | Unpack launch()'s kernel arguments with cuda::std::apply | 2026-08-13 |  |  |
| [#10801](../sources/prs/cccl/PR-10801.md) | Prepend to tuples without a deduction guide, so device code can too | 2026-08-13 |  |  |
| [#10807](../sources/prs/cccl/PR-10807.md) | [STF] Composable exception-handling policies: the on_throw algebra | 2026-08-13 |  |  |
| [#10769](../sources/prs/cccl/PR-10769.md) | [STF] Structured partitions: cute_partition across C++, C API, and Python (stack 1/4) | 2026-08-12 |  |  |
| [#10770](../sources/prs/cccl/PR-10770.md) | [STF] Placement evaluation: score a mapping before committing memory (stack 2/4) | 2026-08-12 |  | quantization |
| [#10751](../sources/prs/cccl/PR-10751.md) | Add sm107 tunings for DeviceScan::*ByKey | 2026-08-11 |  |  |
| [#10752](../sources/prs/cccl/PR-10752.md) | Add sm107 tunings for DeviceReduce::Sum | 2026-08-11 |  |  |
| [#10757](../sources/prs/cccl/PR-10757.md) | [cudax][cuco] Migrate contains_if APIs for fixed_capacity_map | 2026-08-11 |  |  |
| [#10759](../sources/prs/cccl/PR-10759.md) | [cudax][cuco] Migrate insert_if APIs for fixed_capacity_map | 2026-08-11 |  |  |
| [#10763](../sources/prs/cccl/PR-10763.md) | Minor maintenance on memory resource | 2026-08-11 |  |  |
| [#10764](../sources/prs/cccl/PR-10764.md) | [STF] SM split methods for locality-domain execution places | 2026-08-11 |  |  |
| [#10732](../sources/prs/cccl/PR-10732.md) | Add missing `_CCCL_DEDUCTION_GUIDE_ATTRIBUTES` to deduction guides | 2026-08-10 |  |  |
| [#10733](../sources/prs/cccl/PR-10733.md) | Fixes various issues in partial tile merge sort | 2026-08-10 |  | sort |
| [#10729](../sources/prs/cccl/PR-10729.md) | [pre-commit.ci] pre-commit autoupdate | 2026-08-09 |  | scan, sort |
| [#10730](../sources/prs/cccl/PR-10730.md) | Use `mbarrier_arrive_expect_tx` with `sem_relaxed_t` in DeviceTransform when available | 2026-08-09 |  |  |
| [#10731](../sources/prs/cccl/PR-10731.md) | Add `cub::DeviceReduce::ArgMin[Last]Max` | 2026-08-09 |  | reduction |
| [#10725](../sources/prs/cccl/PR-10725.md) | Adds support for logical sub-warps to `WarpBitonicSort` | 2026-08-08 |  | sort |
| [#10702](../sources/prs/cccl/PR-10702.md) | [Cub] Limit lookahead atomic size | 2026-08-07 |  |  |
| [#10681](../sources/prs/cccl/PR-10681.md) | [STF] Restore the current device in green_ctx data place allocate/deallocate | 2026-08-06 |  |  |
| [#10688](../sources/prs/cccl/PR-10688.md) | [cudax][cuco] Migrate device initialize and make_copy APIs for fixed_capacity_map_ref | 2026-08-06 |  |  |
| [#10691](../sources/prs/cccl/PR-10691.md) | Fall back to memcpy when possible for CUB DeviceCopy | 2026-08-06 |  |  |
| [#10693](../sources/prs/cccl/PR-10693.md) | [cudax][cuco] Migrate host rehash APIs for fixed_capacity_map | 2026-08-06 |  |  |
| [#10694](../sources/prs/cccl/PR-10694.md) | [cudax][cuco] Migrate host size API for fixed_capacity_map | 2026-08-06 |  | reduction |
| [#10695](../sources/prs/cccl/PR-10695.md) | [cudax][cuco] Migrate rebind APIs for fixed_capacity_map_ref | 2026-08-06 |  |  |
| [#10658](../sources/prs/cccl/PR-10658.md) | [STF] locality domain places | 2026-08-05 |  | reduction |
| [#10660](../sources/prs/cccl/PR-10660.md) | [cudax] Make mapping purely group's constructor parameter | 2026-08-05 |  |  |
| [#10674](../sources/prs/cccl/PR-10674.md) | Use iters + num_items on inner most level of MGMN algorithms | 2026-08-05 |  |  |
| [#10677](../sources/prs/cccl/PR-10677.md) | Work around gcc 8 ICE in `constexpr cub::MergePolicy::operator==` | 2026-08-05 |  |  |
| [#10621](../sources/prs/cccl/PR-10621.md) | [libcu++] Promote cuco hashers to cuda::hash | 2026-08-04 |  |  |
| [#10623](../sources/prs/cccl/PR-10623.md) | [CUB] Avoid compiler error on nonintegral `__nv_atomic` argument | 2026-08-04 |  |  |
| [#10625](../sources/prs/cccl/PR-10625.md) | [STF] data_place::replicated — one copy per grid member, read-only | 2026-08-04 |  | sort |
| [#10627](../sources/prs/cccl/PR-10627.md) | Fixes a race condition in `DeviceTopK` | 2026-08-04 |  |  |
| [#10628](../sources/prs/cccl/PR-10628.md) | Enable precompiled headers for `cuda.compute` HostJIT builds | 2026-08-04 |  |  |
| [#10609](../sources/prs/cccl/PR-10609.md) | [STF] Keep composite localized allocations alive across stackable pops | 2026-08-03 |  |  |
| [#10611](../sources/prs/cccl/PR-10611.md) | [Tile] Ensure CUB builds fine with `--enable-tile` | 2026-08-03 |  |  |
| [#10612](../sources/prs/cccl/PR-10612.md) | Fix exception escapes and a clang-cuda parse failure in cudax | 2026-08-03 |  |  |
| [#10581](../sources/prs/cccl/PR-10581.md) | cudax: add configurable on_throw exception handling | 2026-08-02 |  | reduction |
| [#10583](../sources/prs/cccl/PR-10583.md) | [STF] Analytic block placement for structured composite allocations | 2026-08-02 |  | quantization |
| [#10565](../sources/prs/cccl/PR-10565.md) | cudax: complete Library Fundamentals TS v3 scope guards | 2026-07-31 |  |  |
| [#10570](../sources/prs/cccl/PR-10570.md) | [cub] Always set smem limit to max for lookahead scan | 2026-07-31 |  | scan |
| [#10573](../sources/prs/cccl/PR-10573.md) | [Version] Update main to v3.6.0 | 2026-07-31 |  |  |
| [#10537](../sources/prs/cccl/PR-10537.md) | Restore _CCCL_GRID_CONSTANT on streaming_context in DeviceSelect | 2026-07-30 |  |  |
| [#10539](../sources/prs/cccl/PR-10539.md) | [Tile] Mark formatters of tuning policies as host_device | 2026-07-30 |  | scan |
| [#10558](../sources/prs/cccl/PR-10558.md) | [cudax][cuco] Migrate async readbacks to `cuda::copy_bytes` | 2026-07-30 |  |  |
| [#10559](../sources/prs/cccl/PR-10559.md) | cudax/stf: add defer_exception and void checks for SCOPE | 2026-07-30 |  |  |
| [#10523](../sources/prs/cccl/PR-10523.md) | cudax/stf: cuda_try migration — graph_task (PR10) | 2026-07-29 |  |  |
| [#10507](../sources/prs/cccl/PR-10507.md) | Replace deprecated `std::aligned_storage_t` in STF `small_vector` | 2026-07-28 |  |  |
| [#10517](../sources/prs/cccl/PR-10517.md) | [libcudacxx][fp] add fpmp2 multi-precision arithmetic + unit tests | 2026-07-28 | pipeline-stages |  |
| [#10519](../sources/prs/cccl/PR-10519.md) | Add tunable prefetching to DeviceSelect::Flagged | 2026-07-28 |  | scan |
| [#10521](../sources/prs/cccl/PR-10521.md) | [cudax][cuco] Migrate retrieve_all API for fixed_capacity_map | 2026-07-28 |  |  |
| [#10504](../sources/prs/cccl/PR-10504.md) | Prevent OOB write for RBK and RLE in streaming context | 2026-07-27 | double-buffering |  |
| [#10227](../sources/prs/cccl/PR-10227.md) | [CUB] Test and document in-place BlockExchange overloads | 2026-07-24 |  |  |
| [#10105](../sources/prs/cccl/PR-10105.md) | Take CUB environments by `const&` | 2026-07-23 | double-buffering | scan |
| [#10210](../sources/prs/cccl/PR-10210.md) | [cudax] Infrastructure for passing scratch to cooperative algorihms | 2026-07-23 |  |  |
| [#10217](../sources/prs/cccl/PR-10217.md) | [cudax][cuco] Fix const mismatch in cooperative HyperLogLog merge | 2026-07-23 |  |  |
| [#10218](../sources/prs/cccl/PR-10218.md) | [cudax][cuco] Return double from HyperLogLog estimate | 2026-07-23 |  |  |
| [#10220](../sources/prs/cccl/PR-10220.md) | [cudax][cuco] Reject undersized hyperloglog_ref storage | 2026-07-23 |  |  |
| [#10076](../sources/prs/cccl/PR-10076.md) | Prepare select and partition tuning policies for lookahead | 2026-07-22 |  | scan |
| [#10077](../sources/prs/cccl/PR-10077.md) | Prepare three-way partition tuning policies for lookahead | 2026-07-22 |  | scan |
| [#10078](../sources/prs/cccl/PR-10078.md) | Prepare reduce-by-key tuning policy for lookahead | 2026-07-22 |  | scan |
| [#10079](../sources/prs/cccl/PR-10079.md) | Prepare scan-by-key tuning policy for lookahead | 2026-07-22 |  | scan |
| [#10080](../sources/prs/cccl/PR-10080.md) | Prepare non-trivial-runs tuning policy for lookahead | 2026-07-22 |  | scan |
| [#10081](../sources/prs/cccl/PR-10081.md) | Prepare batched-copy tuning policy for lookahead | 2026-07-22 |  |  |
| [#10084](../sources/prs/cccl/PR-10084.md) | Use block-scoped atomics in BlockHistogramAtomic on SM 60+ | 2026-07-22 |  |  |
| [#10038](../sources/prs/cccl/PR-10038.md) | [STF] Expose geometry-aware allocation and native partition functions in the C API | 2026-07-21 |  |  |
| [#10009](../sources/prs/cccl/PR-10009.md) | Deprecate `thrust::*trivially_relocatable* traits` | 2026-07-20 |  |  |
| [#10025](../sources/prs/cccl/PR-10025.md) | [cuco] Adds support for 1 and 2 byte key and value types in `fixed_capacity_map` | 2026-07-20 |  |  |
| [#10028](../sources/prs/cccl/PR-10028.md) | Restructure the RLE encode tuning policy | 2026-07-20 |  | scan |
| [#10006](../sources/prs/cccl/PR-10006.md) | [STF] Support compound while-loop conditions in the C API | 2026-07-19 |  |  |
| [#10003](../sources/prs/cccl/PR-10003.md) | cudax/stf: cuda_try migration — stream_task (PR9) | 2026-07-18 |  |  |
| [#10000](../sources/prs/cccl/PR-10000.md) | Fix `cuda::ptx` `shr` and `bfind` `long`, `long long` handling | 2026-07-17 |  |  |
| [#9894](../sources/prs/cccl/PR-9894.md) | Use `thrust::is_contiguous_iterator_v` over `cuda::std::contiguous_iterator` | 2026-07-16 |  |  |
| [#9898](../sources/prs/cccl/PR-9898.md) | [places] Add checked execution grid reshaping | 2026-07-16 |  |  |
| [#9871](../sources/prs/cccl/PR-9871.md) | [cudax] Implement `cudax::level_synchronizer` | 2026-07-15 |  |  |
| [#9876](../sources/prs/cccl/PR-9876.md) | Replace `bool_constant` by `if constexpr` in agent_sub_warp_merge_sort | 2026-07-15 |  | sort |
| [#9879](../sources/prs/cccl/PR-9879.md) | Add `cstdio` and `cstdarg` hostlib headers | 2026-07-15 |  |  |
| [#9853](../sources/prs/cccl/PR-9853.md) | Fix clang-tidy errors reported on several PRs | 2026-07-14 |  |  |
| [#9855](../sources/prs/cccl/PR-9855.md) | [clang-tidy] Suppress new warnings emitted by clang-tidy-22 | 2026-07-14 |  |  |
| [#9858](../sources/prs/cccl/PR-9858.md) | Remove most `CCCL_GRID_CONSTANT` annotations | 2026-07-14 |  |  |
| [#9861](../sources/prs/cccl/PR-9861.md) | [CUB] Fix DeviceAdjacentDifference for cuda::device_buffer iterators | 2026-07-14 |  |  |
| [#9862](../sources/prs/cccl/PR-9862.md) | Add `cudax::distributed` and `cudax::returned_to` specifiers for cooperative algorithms | 2026-07-14 |  | scan, sort |
| [#9865](../sources/prs/cccl/PR-9865.md) | Add deferred argument to 2-phase InclusiveScan | 2026-07-14 |  | scan |
| [#9868](../sources/prs/cccl/PR-9868.md) | [cudax][cuco] Migrate host and device find APIs for fixed_capacity_map | 2026-07-14 |  |  |
| [#9808](../sources/prs/cccl/PR-9808.md) | [STF] Drive parallel_for and data placement from structured partitions | 2026-07-13 |  | sort |
| [#9810](../sources/prs/cccl/PR-9810.md) | [cub] Fix `bugprone-branch-clone` error | 2026-07-13 |  |  |
| [#9813](../sources/prs/cccl/PR-9813.md) | Use plus tunings for lookahead scan more widely | 2026-07-13 |  |  |
| [#9818](../sources/prs/cccl/PR-9818.md) | [cudax] Implement `cudax::take` mapping | 2026-07-13 |  |  |
| [#9826](../sources/prs/cccl/PR-9826.md) | DeviceScan::InclusiveScan() accepts a `cuda::args::deferred` | 2026-07-13 |  | scan |
| [#9829](../sources/prs/cccl/PR-9829.md) | Remove _CCCL_GRID_CONSTANT from merge sort kernel parameters | 2026-07-13 |  | sort |
| [#9801](../sources/prs/cccl/PR-9801.md) | Segmented Topk tuning on B200 `indexed.cluster` | 2026-07-11 |  | topk |
| [#9803](../sources/prs/cccl/PR-9803.md) | [STF] Implement cyclic_partition::get_executor | 2026-07-11 |  |  |
| [#9804](../sources/prs/cccl/PR-9804.md) | [STF] Add structured tensor partitions and placement evaluation to the places layer | 2026-07-11 |  | quantization, sort |
| [#9779](../sources/prs/cccl/PR-9779.md) | [STF] Add exec places from externally-owned CUDA contexts | 2026-07-10 |  |  |
| [#9795](../sources/prs/cccl/PR-9795.md) | Remove `_CCCL_GRID_CONSTANT` from `DeviceSelectSweepKernel` parameters | 2026-07-10 |  |  |
| [#9758](../sources/prs/cccl/PR-9758.md) | [STF] Export blocked_partition_custom into cuda::experimental::stf | 2026-07-09 |  |  |
| [#9762](../sources/prs/cccl/PR-9762.md) | Do not vectorize large type reductions | 2026-07-09 |  |  |
| [#9772](../sources/prs/cccl/PR-9772.md) | Fully classify the `cub::detail::InputValue` template to avoid implicit conversions | 2026-07-09 |  |  |
| [#9776](../sources/prs/cccl/PR-9776.md) | Handle a type of size exactly 3 in cuda::buffer | 2026-07-09 |  |  |
| [#9777](../sources/prs/cccl/PR-9777.md) | [libcudacxx][fp] add fpemu (double-precision emulation) + unit tests | 2026-07-09 | pipeline-stages |  |
| [#9743](../sources/prs/cccl/PR-9743.md) | Deprecate CUB device count functions | 2026-07-08 |  |  |
| [#9744](../sources/prs/cccl/PR-9744.md) | Deprecate `cub::ChainedPolicy` | 2026-07-08 |  |  |
| [#9745](../sources/prs/cccl/PR-9745.md) | Add tuning policies to CUB API docs | 2026-07-08 |  |  |
| [#9748](../sources/prs/cccl/PR-9748.md) | [cudax][cuco] Port fixed_capacity_map benchmarks from cuCollections | 2026-07-08 |  |  |
| [#9751](../sources/prs/cccl/PR-9751.md) | [CUB] warpspeed kernel: make scan_resources_t copy | 2026-07-08 |  |  |
| [#9752](../sources/prs/cccl/PR-9752.md) | Refactor enum to string functions | 2026-07-08 |  | scan |
| [#9722](../sources/prs/cccl/PR-9722.md) | [CUB] `DeviceReduce` with device resident problem size | 2026-07-07 |  | reduction |
| [#9723](../sources/prs/cccl/PR-9723.md) | Implement prefetching | 2026-07-07 |  | tma |
| [#9728](../sources/prs/cccl/PR-9728.md) | [libcu++] Fix `cuda::std::aligned_alloc` argument order | 2026-07-07 |  |  |
| [#9735](../sources/prs/cccl/PR-9735.md) | Rename cuco `.hpp` headers to `.cuh` | 2026-07-07 |  |  |
| [#9738](../sources/prs/cccl/PR-9738.md) | [cudax] Change cuco test target names | 2026-07-07 |  |  |
| [#9740](../sources/prs/cccl/PR-9740.md) | [CUB] GPU-to-GPU `DeviceReduce` with device resident problem size | 2026-07-07 |  | reduction |
| [#9709](../sources/prs/cccl/PR-9709.md) | Improve NV_IF_ELSE_TARGET formatting in segmented reduce dispatch | 2026-07-06 |  |  |
| [#9711](../sources/prs/cccl/PR-9711.md) | Rename `AgentTopKPolicy` to `agent_topk_policy` | 2026-07-06 |  | scan, topk |
| [#9712](../sources/prs/cccl/PR-9712.md) | Tuning policy cleanup 2/2 | 2026-07-06 |  | scan |
| [#9714](../sources/prs/cccl/PR-9714.md) | Separate from and deprecate `DispatchScanByKey` | 2026-07-06 |  | scan |
| [#9716](../sources/prs/cccl/PR-9716.md) | Swap `small_segment` and `medium_segment` in `SegmentedSortPolicy` | 2026-07-06 |  |  |
| [#9717](../sources/prs/cccl/PR-9717.md) | Remove `num_` from tuning policy members | 2026-07-06 |  | scan |
| [#9719](../sources/prs/cccl/PR-9719.md) | Make stream and memory resource explicit in fixed_capacity_map APIs | 2026-07-06 |  |  |
| [#9720](../sources/prs/cccl/PR-9720.md) | Make stream and memory resource explicit in hyperloglog APIs | 2026-07-06 |  |  |
| [#9708](../sources/prs/cccl/PR-9708.md) | Cover __half and __nv_bfloat16 in CUB Reduce/Scan/RadixSort benchmarks | 2026-07-05 |  | reduction, sort |
| [#9706](../sources/prs/cccl/PR-9706.md) | [STF] Name green context data places by handle and support VMM mem_create | 2026-07-04 |  |  |
| [#9699](../sources/prs/cccl/PR-9699.md) | Warpspeed Implementation of `cub::DeviceRunLengthEncode::Encode` | 2026-07-03 | pipeline-stages, swizzling, warp-specialization | clc, mbarrier, scan |
| [#9704](../sources/prs/cccl/PR-9704.md) | Fix use of `reduce_policy` | 2026-07-03 |  |  |
| [#9684](../sources/prs/cccl/PR-9684.md) | Use `cuda::std::is_sufficiently_aligned` in CCCL | 2026-07-02 |  |  |
| [#9685](../sources/prs/cccl/PR-9685.md) | Allow public tuning of `cub::DeviceSegmentedRadixSort` | 2026-07-02 |  | sort |
| [#9686](../sources/prs/cccl/PR-9686.md) | Allow public tuning of `cub::DeviceSegmentedReduce` | 2026-07-02 |  |  |
| [#9688](../sources/prs/cccl/PR-9688.md) | Allow public tuning of `cub::DeviceFind::*BoundSortedValues` | 2026-07-02 |  |  |
| [#9689](../sources/prs/cccl/PR-9689.md) | Rename `FindPolicy` to `FindIfPolicy` | 2026-07-02 |  |  |
| [#9658](../sources/prs/cccl/PR-9658.md) | Allow public tuning of `cub::DeviceCopy` | 2026-07-01 |  |  |
| [#9659](../sources/prs/cccl/PR-9659.md) | Small refactorings for batched memcpy | 2026-07-01 |  |  |
| [#9660](../sources/prs/cccl/PR-9660.md) | [CUB] Refactor `dispatch_streaming_arg_reduce` to take a tuning environment | 2026-07-01 |  |  |
| [#9665](../sources/prs/cccl/PR-9665.md) | [cudax] Implement `cudax::coop::any_of` algorithm for <= warp groups | 2026-07-01 |  |  |
| [#9675](../sources/prs/cccl/PR-9675.md) | [cudax][cuco] Use the detail config header and proper visibility macros in cuco headers | 2026-07-01 |  |  |
| [#9676](../sources/prs/cccl/PR-9676.md) | Fix CUB DeviceReduce env overloads to accept no_init_t | 2026-07-01 |  |  |
| [#9681](../sources/prs/cccl/PR-9681.md) | Productize `DeviceSegmentedSort` tuning API | 2026-07-01 |  | scan, sort |
| [#9637](../sources/prs/cccl/PR-9637.md) | Allow public tuning of `cub::DeviceMerge` | 2026-06-30 |  |  |
| [#9639](../sources/prs/cccl/PR-9639.md) | Unify reduce and rfa policy | 2026-06-30 |  | reduction |
| [#9640](../sources/prs/cccl/PR-9640.md) | Move `bits_per_pass` last in `topk_policy` | 2026-06-30 |  | scan |
| [#9641](../sources/prs/cccl/PR-9641.md) | [cub] Specialize `std::formatter` for enums | 2026-06-30 |  | scan |
| [#9649](../sources/prs/cccl/PR-9649.md) | [cuda.compute]: fix v2 issue with some well known ops not being supported | 2026-06-30 |  |  |
| [#9625](../sources/prs/cccl/PR-9625.md) | [cudax] Add `unit_` prefix to unit-related data in mapping result | 2026-06-29 |  |  |
| [#9603](../sources/prs/cccl/PR-9603.md) | [CUB] Cleanup some dispatch arguments | 2026-06-26 |  |  |
| [#9604](../sources/prs/cccl/PR-9604.md) | [STF] Fix multi-context parallel for for grid places | 2026-06-26 |  |  |
| [#9552](../sources/prs/cccl/PR-9552.md) | [CUB] Refactor `DeviceHistogram::MultiHistogramEven` to always take an environment | 2026-06-23 |  |  |
| [#9553](../sources/prs/cccl/PR-9553.md) | [CUB] Refactor `DeviceHistogram::HistogramEven` to always take an environment | 2026-06-23 |  |  |
| [#9554](../sources/prs/cccl/PR-9554.md) | [CUB] Refactor `DeviceHistogram::MultiHistogramRange` to always take an environment | 2026-06-23 |  |  |
| [#9555](../sources/prs/cccl/PR-9555.md) | [CUB] Refactor `DeviceHistogram::HistogramRange` to always take an environment | 2026-06-23 |  |  |
| [#9565](../sources/prs/cccl/PR-9565.md) | warpspeed run_to_run deterministic scan for SM90 using atomic global counter | 2026-06-23 |  | reduction |
| [#9570](../sources/prs/cccl/PR-9570.md) | [CUB][Bug] Fix DeviceHistogram out-of-bounds write | 2026-06-23 |  |  |
| [#9540](../sources/prs/cccl/PR-9540.md) | [STF] Fix data race on stackable_logical_data across host threads | 2026-06-22 |  |  |
| [#9541](../sources/prs/cccl/PR-9541.md) | [STF] Make exec_place/data_place singletons thread-safe | 2026-06-22 |  |  |
| [#9497](../sources/prs/cccl/PR-9497.md) | CRITICAL: Add PDL guard back missed in #9247 | 2026-06-17 |  |  |
| [#9501](../sources/prs/cccl/PR-9501.md) | [STF] Support ctx.wait() on a token | 2026-06-17 |  |  |
| [#9505](../sources/prs/cccl/PR-9505.md) | bugprone-narrowing-conversions | 2026-06-17 |  | sort |
| [#9506](../sources/prs/cccl/PR-9506.md) | bugprone-misplaced-widening-cast | 2026-06-17 |  | scan |
| [#9510](../sources/prs/cccl/PR-9510.md) | bugprone-exception-escape | 2026-06-17 |  |  |
| [#9513](../sources/prs/cccl/PR-9513.md) | bugprone-branch-clone | 2026-06-17 |  |  |
| [#9517](../sources/prs/cccl/PR-9517.md) | bugprone-sizeof-expression | 2026-06-17 |  |  |
| [#9519](../sources/prs/cccl/PR-9519.md) | bugprone-assignment-in-if-condition | 2026-06-17 |  |  |
| [#9521](../sources/prs/cccl/PR-9521.md) | bugprone-unintended-char-ostream-output | 2026-06-17 |  |  |
| [#9525](../sources/prs/cccl/PR-9525.md) | bugprone-suspicious-stringview-data-usage | 2026-06-17 |  |  |
| [#9530](../sources/prs/cccl/PR-9530.md) | Duplicate radix sort dispatch to deprecate `DispatchRadixSort` | 2026-06-17 | double-buffering | scan, sort |
| [#9481](../sources/prs/cccl/PR-9481.md) | Vectorize output store in ublkcp DeviceTransform kernel | 2026-06-16 |  |  |
| [#9485](../sources/prs/cccl/PR-9485.md) | Rename `warp_threads` in tuning policies | 2026-06-16 |  |  |
| [#9489](../sources/prs/cccl/PR-9489.md) | Radix sort policy name improvements | 2026-06-16 |  | scan, sort |
| [#9490](../sources/prs/cccl/PR-9490.md) | Ensure warpspeed scan uses <= 256 threads for NVHPC | 2026-06-16 |  |  |
| [#9491](../sources/prs/cccl/PR-9491.md) | Allow public tuning of `cub::DeviceRadixSort` | 2026-06-16 |  | scan, sort |
| [#9495](../sources/prs/cccl/PR-9495.md) | static assert fail when -G and rdc are enabled to avoid lookahead compilation error | 2026-06-16 |  |  |
| [#9454](../sources/prs/cccl/PR-9454.md) | Refactor `device_adjacent_difference::dispatch` to take a tuning | 2026-06-15 |  |  |
| [#9455](../sources/prs/cccl/PR-9455.md) | [CUB] Refactor `DeviceSelect::Flagged` to always take an environment | 2026-06-15 |  |  |
| [#9456](../sources/prs/cccl/PR-9456.md) | [CUB] Refactor `cub::DeviceSelect::If` to always take an environment | 2026-06-15 |  |  |
| [#9457](../sources/prs/cccl/PR-9457.md) | [CUB] Refactor `DeviceSelect::FlaggedIf` to always take an environment | 2026-06-15 |  |  |
| [#9458](../sources/prs/cccl/PR-9458.md) | [CUB] Refactor `DeviceSelect::Unique` to always take an environment | 2026-06-15 |  |  |
| [#9459](../sources/prs/cccl/PR-9459.md) | [CUB] Refactor `DeviceSelect::UniqueByKey` to always take an environment | 2026-06-15 |  |  |
| [#9463](../sources/prs/cccl/PR-9463.md) | [CUB] Refactor `DevicePartition::Flagged` to always take an environment | 2026-06-15 |  |  |
| [#9464](../sources/prs/cccl/PR-9464.md) | [CUB] Refactor `DevicePartition::If` to always take an environment | 2026-06-15 |  |  |
| [#9470](../sources/prs/cccl/PR-9470.md) | Fix `BlockTopK` +/-0.0 handling | 2026-06-15 |  | sort, topk |
| [#9471](../sources/prs/cccl/PR-9471.md) | use `__ballot_sync` in warpspeed lookahead  | 2026-06-15 |  | scan |
| [#9445](../sources/prs/cccl/PR-9445.md) | Remove __syncthreads() duplicate from agent_radix_histogram | 2026-06-13 |  |  |
| [#9416](../sources/prs/cccl/PR-9416.md) | [CUB] Refactor `DeviceCopy` to always take an environment | 2026-06-12 |  |  |
| [#9418](../sources/prs/cccl/PR-9418.md) | [CUB] Refactor `DeviceAdjacentDifference::SubtractLeft` to always take an environment | 2026-06-12 |  |  |
| [#9419](../sources/prs/cccl/PR-9419.md) | [CUB] Refactor `DeviceAdjacentDifference::SubtractRight` to always take an environment | 2026-06-12 |  |  |
| [#9429](../sources/prs/cccl/PR-9429.md) | Refactor `DeviceFind` | 2026-06-12 |  |  |
| [#9430](../sources/prs/cccl/PR-9430.md) | Productize tuning API for `DeviceSegmentedScan` | 2026-06-12 |  | scan |
| [#9436](../sources/prs/cccl/PR-9436.md) | Reorganize cuco implementation headers under detail/ | 2026-06-12 |  |  |
| [#9439](../sources/prs/cccl/PR-9439.md) | Enforce MergePolicy tuning values | 2026-06-12 |  |  |
| [#9441](../sources/prs/cccl/PR-9441.md) | [CUB] Fully support warp `redux`  | 2026-06-12 |  | reduction |
| [#9390](../sources/prs/cccl/PR-9390.md) | [cudax] Implement `cudax::coop::shuffle_up` for threads within a warp | 2026-06-11 |  |  |
| [#9392](../sources/prs/cccl/PR-9392.md) | [cudax] Use `coop::shuffle_down` in `coop::reduce` | 2026-06-11 |  |  |
| [#9394](../sources/prs/cccl/PR-9394.md) | [cudax][STF] Auto-free graph allocations on launch | 2026-06-11 |  |  |
| [#9403](../sources/prs/cccl/PR-9403.md) | [CUB] Refactor `DeviceReduce::Arg{Min, Max}` to always take an environment | 2026-06-11 |  |  |
| [#9359](../sources/prs/cccl/PR-9359.md) | Allow public tuning of `cub::DeviceMemcpy` | 2026-06-10 |  |  |
| [#9360](../sources/prs/cccl/PR-9360.md) | [cudax] Implement broadcasted variants of `cudax::coop::reduce` | 2026-06-10 |  |  |
| [#9361](../sources/prs/cccl/PR-9361.md) | Histogram tuning policy cleanup | 2026-06-10 |  |  |
| [#9362](../sources/prs/cccl/PR-9362.md) | Allow public tuning of `cub::DeviceHistogram` | 2026-06-10 |  |  |
| [#9370](../sources/prs/cccl/PR-9370.md) | Allow public tuning for `cub::DeviceSelect:::UniqueByKey` | 2026-06-10 |  | scan |
| [#9371](../sources/prs/cccl/PR-9371.md) | [cudax] Implement `cudax::coop::shuffle_down` for threads within a warp | 2026-06-10 |  |  |
| [#9306](../sources/prs/cccl/PR-9306.md) | cudax/stf: cuda_try migration — stream_ctx (PR8) | 2026-06-09 |  |  |
| [#9311](../sources/prs/cccl/PR-9311.md) | Adds tests for segment-specific-k-values | 2026-06-09 |  |  |
| [#9316](../sources/prs/cccl/PR-9316.md) | Allow public tuning of `cub::DeviceSelect` (without `UniqueByKey`) and `cub::DevicePartition` (without three-way) | 2026-06-09 |  | scan |
| [#9318](../sources/prs/cccl/PR-9318.md) | [PSTL] Use env based overload for `DeviceFindIf` | 2026-06-09 |  |  |
| [#9324](../sources/prs/cccl/PR-9324.md) | Allow public tuning of three-way `cub::DevicePartition::If` | 2026-06-09 | double-buffering | scan, sort |
| [#9325](../sources/prs/cccl/PR-9325.md) | [cudax] Implement `cudax::coop::shuffle` for threads within a warp | 2026-06-09 |  |  |
| [#9327](../sources/prs/cccl/PR-9327.md) | Rename non-library uses of "warpspeed" to "lookahead" | 2026-06-09 |  | scan |
| [#9329](../sources/prs/cccl/PR-9329.md) | Allow public tuning of the `cub::DeviceReduce::ReduceByKey` and `cub::DeviceRunLengthEncode::Encode` | 2026-06-09 |  | scan |
| [#9331](../sources/prs/cccl/PR-9331.md) | Exposes `DeviceBatchedTopK::{Min,Max}{Keys,Pairs}` for non-deterministic, unordered, and small segments-only | 2026-06-09 |  | topk |
| [#9336](../sources/prs/cccl/PR-9336.md) | Take environments by `const&` in `DeviceTransform` | 2026-06-09 |  |  |
| [#9347](../sources/prs/cccl/PR-9347.md) | Allow public tuning of the `cub::DeviceRunLengthEncode::NonTrivialRuns` | 2026-06-09 |  | scan |
| [#9349](../sources/prs/cccl/PR-9349.md) | Unify atomic and two-phase reduction | 2026-06-09 |  | reduction |
| [#9294](../sources/prs/cccl/PR-9294.md) | Better asserts for warp primitives without temp storage | 2026-06-08 |  | scan |
| [#9295](../sources/prs/cccl/PR-9295.md) | Implement minimal host-side logging for CUB | 2026-06-08 |  | scan |
| [#9297](../sources/prs/cccl/PR-9297.md) | Allow public tuning of `cub::DeviceFor` | 2026-06-08 |  |  |
| [#9300](../sources/prs/cccl/PR-9300.md) | [cudax] Implement `cuda::coop::reduce` for threads within a warp  | 2026-06-08 |  |  |
| [#9301](../sources/prs/cccl/PR-9301.md) | cudax/stf: cuda_try migration — graph misc (PR6) | 2026-06-08 |  |  |
| [#9303](../sources/prs/cccl/PR-9303.md) | cudax/stf: cuda_try migration — stream event_types (PR7) | 2026-06-08 |  |  |
| [#9286](../sources/prs/cccl/PR-9286.md) | [CUB] Makes the batched top-k selection direction compile-time only | 2026-06-07 |  | topk |
| [#9289](../sources/prs/cccl/PR-9289.md) | Support `cub::DeviceReduce` without initial value | 2026-06-07 |  |  |
| [#9267](../sources/prs/cccl/PR-9267.md) | Use uniform type names for init values throughout CUB | 2026-06-05 |  |  |
| [#9268](../sources/prs/cccl/PR-9268.md) | cudax/stf: migrate stream/interfaces/ from cuda_safe_call to cuda_try | 2026-06-05 |  | reduction |
| [#9247](../sources/prs/cccl/PR-9247.md) | Add PDL to `cub::DeviceRadixSort` | 2026-06-04 |  |  |
| [#9248](../sources/prs/cccl/PR-9248.md) | cudax/stf: migrate internal/ context + resources from cuda_safe_call to cuda_try | 2026-06-04 |  |  |
| [#9249](../sources/prs/cccl/PR-9249.md) | cudax/stf: migrate internal/ launch + host_launch_scope from cuda_safe_call to cuda_try | 2026-06-04 |  |  |
| [#9251](../sources/prs/cccl/PR-9251.md) | [libcu++] Make argument namespace and wrappers construction public | 2026-06-04 |  | topk |
| [#9258](../sources/prs/cccl/PR-9258.md) | [cudax] Implement `cudax::coop::reduce` for warp groups within a block | 2026-06-04 |  |  |
| [#9263](../sources/prs/cccl/PR-9263.md) | run to run scan warpspeed impl sm100+ | 2026-06-04 |  | reduction |
| [#9264](../sources/prs/cccl/PR-9264.md) | [cudax] Update lane mask inside mappings only when unit is thread | 2026-06-04 |  |  |
| [#9265](../sources/prs/cccl/PR-9265.md) | cudax/stf: migrate internal/ parallel_for + cuda_kernel scopes from cuda_safe_call to cuda_try | 2026-06-04 |  |  |
| [#9224](../sources/prs/cccl/PR-9224.md) | Implement Segmented TopK using Thread-Block-Clusters | 2026-06-03 | pipeline-stages | mbarrier, reduction, scan |
| [#9230](../sources/prs/cccl/PR-9230.md) | [cudax] Implement `cudax::invoke_one` | 2026-06-03 |  |  |
| [#9232](../sources/prs/cccl/PR-9232.md) | [STF] Add C bindings for the places layer | 2026-06-03 |  |  |
| [#9233](../sources/prs/cccl/PR-9233.md) | [STF] Add C bindings for stackable contexts | 2026-06-03 |  |  |
| [#9234](../sources/prs/cccl/PR-9234.md) | Deprecate `DispatchScan` and `AgentScanPolicy` | 2026-06-03 |  | scan |
| [#9235](../sources/prs/cccl/PR-9235.md) | Deprecate `AgentMergeSortPolicy` and `AgentAdjacentDifferencePolicy` | 2026-06-03 |  |  |
| [#9236](../sources/prs/cccl/PR-9236.md) | Allow public tuning of `DeviceFind` | 2026-06-03 |  |  |
| [#9240](../sources/prs/cccl/PR-9240.md) | Use the new tuning API internally for detail::find::dispatch | 2026-06-03 |  |  |
| [#9241](../sources/prs/cccl/PR-9241.md) | cudax/stf: migrate internal/ misc files from cuda_safe_call to cuda_try | 2026-06-03 |  |  |
| [#9244](../sources/prs/cccl/PR-9244.md) | Rename `block_scan_algorithm` to `scan_algorithm` | 2026-06-03 |  | scan |
| [#9246](../sources/prs/cccl/PR-9246.md) | [libcu++] Rename max to highest in arguments framework | 2026-06-03 |  |  |
| [#9215](../sources/prs/cccl/PR-9215.md) | Allow public tuning of `cub::DeviceScan::*ByKey` | 2026-06-02 |  | scan |
| [#9218](../sources/prs/cccl/PR-9218.md) | Allow public tuning of `cub::DeviceAdjacentDifference` | 2026-06-02 |  |  |
| [#9202](../sources/prs/cccl/PR-9202.md) | Avoid passing OOB data to scan operator in warpspeed scan | 2026-06-01 |  |  |
| [#9203](../sources/prs/cccl/PR-9203.md) | [cudax] Implement `cudax::coop::reduce` for `cudax::this_grid` | 2026-06-01 |  |  |
| [#9210](../sources/prs/cccl/PR-9210.md) | [Tile] tile DeviceTransform port | 2026-06-01 |  |  |
| [#9193](../sources/prs/cccl/PR-9193.md) | `cudax::fill_bytes(mdspan)` | 2026-05-30 |  |  |
| [#9194](../sources/prs/cccl/PR-9194.md) | Use the new tuning API internally for `detail::segmented_scan::dispatch` | 2026-05-30 |  |  |
| [#9171](../sources/prs/cccl/PR-9171.md) | Fix NVRTC 13.3 warning bug in CCCL and CCCL.C | 2026-05-29 |  |  |
| [#9178](../sources/prs/cccl/PR-9178.md) | [STF] Add re-launchable popped graphs to stackable_ctx | 2026-05-29 |  |  |
| [#9181](../sources/prs/cccl/PR-9181.md) | Control unrolling in `cub::DeviceMerge[Sort]` via tuning  | 2026-05-29 |  | sort |
| [#9186](../sources/prs/cccl/PR-9186.md) | [STF] Fix host-thread data races in concurrent task submission | 2026-05-29 |  |  |
| [#9150](../sources/prs/cccl/PR-9150.md) | [STF] Migrate __stf/utility/ from cuda_safe_call to cuda_try | 2026-05-28 |  |  |
| [#9153](../sources/prs/cccl/PR-9153.md) | [cub] Fix warp reduce of fixed size random access range | 2026-05-28 |  |  |
| [#9154](../sources/prs/cccl/PR-9154.md) | [cudax] Initial `cudax::coop::reduce` prototype | 2026-05-28 |  |  |
| [#9163](../sources/prs/cccl/PR-9163.md) | Only enabled PDL for PTX/SASS supporting it | 2026-05-28 |  |  |
| [#9165](../sources/prs/cccl/PR-9165.md) | cudax/stf: migrate stackable/ from cuda_safe_call to cuda_try | 2026-05-28 |  |  |
| [#9167](../sources/prs/cccl/PR-9167.md) | [cudax] Implement `cudax::coop::reduce` for `cudax::this_cluster` | 2026-05-28 |  |  |
| [#9168](../sources/prs/cccl/PR-9168.md) | Refactor warpspeed scan 1/2 | 2026-05-28 | pipeline-stages, warp-specialization | scan, tma |
| [#9169](../sources/prs/cccl/PR-9169.md) | Refactor warpspeed scan 2/2  | 2026-05-28 |  | scan |
| [#9137](../sources/prs/cccl/PR-9137.md) | `cudax::copy(mdspan)` Optimize shared memory cases | 2026-05-27 | swizzling | sort |
| [#9138](../sources/prs/cccl/PR-9138.md) | [STF] [TRIVIAL] Rename decorated_stream to augmented_stream | 2026-05-27 |  |  |
| [#9140](../sources/prs/cccl/PR-9140.md) | [cudax] Make `lane_mask` part of the mapping result | 2026-05-27 |  |  |
| [#9143](../sources/prs/cccl/PR-9143.md) | Update all the things to CTK 13.3. | 2026-05-27 |  |  |
| [#9147](../sources/prs/cccl/PR-9147.md) | [STF] Migrate __stf/allocators/ from cuda_safe_call to cuda_try | 2026-05-27 |  |  |
| [#9148](../sources/prs/cccl/PR-9148.md) | [places] Align cyclic_shape::size with iteration cardinality | 2026-05-27 |  |  |
| [#9127](../sources/prs/cccl/PR-9127.md) | Hardcode `DeviceTransform` `OffsetT` to `int64` | 2026-05-26 |  |  |
| [#9128](../sources/prs/cccl/PR-9128.md) | Make more warpspeed scan stage counts tunable | 2026-05-26 |  |  |
| [#9129](../sources/prs/cccl/PR-9129.md) | [libcu++] Implement tuple protocol for `integer_sequence` | 2026-05-26 |  |  |
| [#9136](../sources/prs/cccl/PR-9136.md) | [STF] Deduplicate cudaStreamIsCapturing helper | 2026-05-26 |  |  |
| [#9123](../sources/prs/cccl/PR-9123.md) | Distribute `std::tuple_(size|element)` specializations to implementation files | 2026-05-25 |  |  |
| [#9124](../sources/prs/cccl/PR-9124.md) | use `std::scoped_lock` | 2026-05-25 |  |  |
| [#9120](../sources/prs/cccl/PR-9120.md) | [FEA] Unify is_even functor | 2026-05-23 |  |  |
| [#9106](../sources/prs/cccl/PR-9106.md) | Use the new tuning API internally for `detail::histogram::dispatch` | 2026-05-22 |  |  |
| [#9112](../sources/prs/cccl/PR-9112.md) | [CUB] Fix invalid condition to exclude 128 bit integers | 2026-05-22 |  |  |
| [#9117](../sources/prs/cccl/PR-9117.md) | [STF] Use out parameter for partition mappers | 2026-05-22 |  |  |
| [#9088](../sources/prs/cccl/PR-9088.md) | Refactor DeviceReduce dispatch logic | 2026-05-21 |  | reduction |
| [#9093](../sources/prs/cccl/PR-9093.md) | Use the new tuning API internally for `detail::batch_memcpy::dispatch` | 2026-05-21 |  |  |
| [#9095](../sources/prs/cccl/PR-9095.md) | Use the new tuning API internally for `detail::batched_topk::dispatch` | 2026-05-21 |  | topk |
| [#9098](../sources/prs/cccl/PR-9098.md) | run_to_run deterministic device scan | 2026-05-21 | swizzling | reduction, scan |
| [#9101](../sources/prs/cccl/PR-9101.md) | Implement parallel final reduction in BlockReduceWarp | 2026-05-21 |  | reduction |
| [#9074](../sources/prs/cccl/PR-9074.md) | [cub] Replace cub parameter framework with cuda::argument | 2026-05-20 |  | topk |
| [#9056](../sources/prs/cccl/PR-9056.md) | Vectorize contiguous iterators in `cub::BlockLoad`/`Store` | 2026-05-18 |  |  |
| [#9046](../sources/prs/cccl/PR-9046.md) | [libcu++] Implement `std::constant_wrapper` | 2026-05-17 |  |  |
| [#9019](../sources/prs/cccl/PR-9019.md) | [libcu++] Always suppress C++ extensions warnings in prologue | 2026-05-15 |  |  |
| [#8981](../sources/prs/cccl/PR-8981.md) | Final env-passthrough 3/4 | 2026-05-14 |  | sort |
| [#8985](../sources/prs/cccl/PR-8985.md) | CCCL C v2 | 2026-05-14 |  |  |
| [#8905](../sources/prs/cccl/PR-8905.md) | [STF] Add per-handle exec_place stream resources | 2026-05-12 |  | reduction |
| [#8914](../sources/prs/cccl/PR-8914.md) | [STF] Fix graph capture integration | 2026-05-12 |  |  |
| [#8915](../sources/prs/cccl/PR-8915.md) | [STF] Make graph_task and stream_task move-only | 2026-05-12 |  |  |
| [#8919](../sources/prs/cccl/PR-8919.md) | [STF] Properly destroy CUDA streams and do not try to initialize CUDA while capturing | 2026-05-12 |  |  |
| [#8925](../sources/prs/cccl/PR-8925.md) | Use the new tuning API internally for `detail::select|three_way_partition::dispatch` and `DevicePartition` | 2026-05-12 |  |  |
| [#8927](../sources/prs/cccl/PR-8927.md) | Use the new tuning API internally for `detail::segmented_radix_sort::dispatch` | 2026-05-12 |  |  |
| [#8894](../sources/prs/cccl/PR-8894.md) | [cudax] Implement `binary_partition` mapping for threads within warp | 2026-05-11 |  |  |
| [#8891](../sources/prs/cccl/PR-8891.md) | STF: extend cuda_try output-parameter inference (first/last + ambiguity rejection) | 2026-05-10 |  |  |
| [#8888](../sources/prs/cccl/PR-8888.md) | [infra] Add `clang-22` CUDA build job to nightly/weekly CI | 2026-05-09 |  |  |
| [#8880](../sources/prs/cccl/PR-8880.md) | Use the new tuning API internally for `detail::select::dispatch` and `DeviceSelect` | 2026-05-08 |  |  |
| [#8861](../sources/prs/cccl/PR-8861.md) | [cub] Simplify arch dispatch | 2026-05-07 |  |  |
| [#8863](../sources/prs/cccl/PR-8863.md) | Allow public tuning of non-ByKey `cub::DeviceReduce` | 2026-05-07 |  | reduction |
| [#8839](../sources/prs/cccl/PR-8839.md) | Fix Warpspeed scan shifted output store | 2026-05-06 |  | scan |
| [#8853](../sources/prs/cccl/PR-8853.md) | Allow public tuning of non-ByKey `cub::DeviceScan` | 2026-05-06 | pipeline-stages | reduction, scan |
| [#8826](../sources/prs/cccl/PR-8826.md) | Use the new tuning API internally for `detail::reduce[_nd]::dispatch[_nd]` | 2026-05-05 |  |  |
| [#8780](../sources/prs/cccl/PR-8780.md) | [CUB] Add DeviceFind lower/upper bound for sorted values via merge-path | 2026-05-01 |  |  |
| [#8756](../sources/prs/cccl/PR-8756.md) | Use the new tuning API internally for `detail::reduce_by_key::dispatch` | 2026-04-30 |  |  |
| [#8761](../sources/prs/cccl/PR-8761.md) | Use the new tuning API internally for `detail::scan_by_key::dispatch` | 2026-04-30 |  |  |
| [#8742](../sources/prs/cccl/PR-8742.md) | Use the new tuning API internally for `detail::topk::dispatch` | 2026-04-29 |  | topk |
| [#8745](../sources/prs/cccl/PR-8745.md) | Allow public tuning of `cub::DeviceTransform` | 2026-04-29 |  | tma |
| [#8695](../sources/prs/cccl/PR-8695.md) | Replace `detail::segmented_reduce::dispatch` by the public API | 2026-04-27 |  |  |
| [#8541](../sources/prs/cccl/PR-8541.md) | [libcu++] Add image processing CCCL Runtime / CUB example | 2026-04-21 | double-buffering, pipeline-stages | reduction |
| [#8565](../sources/prs/cccl/PR-8565.md) | Replace `detail::for_each::dispatch` by CUB's public API | 2026-04-21 |  |  |
| [#8600](../sources/prs/cccl/PR-8600.md) | Allow public tuning of `cub::DeviceMergeSort`  | 2026-04-21 |  |  |
| [#8538](../sources/prs/cccl/PR-8538.md) | Implement the new tuning API for `detail::batched_topk::dispatch_batched_topk` | 2026-04-20 |  |  |
| [#8495](../sources/prs/cccl/PR-8495.md) | Replace `detail::scan::dispatch` by CUB's public API | 2026-04-16 |  | scan |
| [#8473](../sources/prs/cccl/PR-8473.md) | Replace `detail::merge_sort::dispatch` by CUB's public API | 2026-04-15 |  | sort |
| [#8423](../sources/prs/cccl/PR-8423.md) | Vectorize mbarrier initialization in warpspeed scan | 2026-04-14 |  | mbarrier |
| [#8391](../sources/prs/cccl/PR-8391.md) | Add WarpBitonicSort | 2026-04-13 |  | sort, topk |
| [#8395](../sources/prs/cccl/PR-8395.md) | [CUB] Replace `Shuffle(Up|Down|Index)` with cuda::device::warp_shuffle - RadixSort only | 2026-04-13 |  |  |
| [#8355](../sources/prs/cccl/PR-8355.md) | [cub]: implement utilities for policy selection | 2026-04-10 |  | scan |
| [#8381](../sources/prs/cccl/PR-8381.md) | Replace `detail::merge::dispatch` by CUB's public API | 2026-04-10 |  |  |
| [#8352](../sources/prs/cccl/PR-8352.md) | Apply some random warpspeed tunings | 2026-04-09 |  |  |
| [#8332](../sources/prs/cccl/PR-8332.md) | simplify dispatch segmented reduce to use latest dispatch and new tunings API | 2026-04-08 |  | reduction |
| [#8311](../sources/prs/cccl/PR-8311.md) | Implement the new tuning API for `DispatchSelectIf` | 2026-04-07 |  | scan |
| [#8291](../sources/prs/cccl/PR-8291.md) | Port `thrust::min|max_element` to CUB | 2026-04-04 |  |  |
| [#8183](../sources/prs/cccl/PR-8183.md) | Refactor `WarpExchangeShfl` | 2026-03-26 |  |  |
| [#8184](../sources/prs/cccl/PR-8184.md) | Avoid passing uninitialized values to scan_op | 2026-03-26 |  | reduction, scan, tma |
| [#8190](../sources/prs/cccl/PR-8190.md) | [STF] Move unstable_unique from STF to generic cudax utility | 2026-03-26 |  |  |
| [#8125](../sources/prs/cccl/PR-8125.md) | Optimized Device-to-Device Tensor Copy (cudax) - Transpose Case | 2026-03-20 |  | sort |
| [#8040](../sources/prs/cccl/PR-8040.md) | Adds support for non-fundamental types via decomposer to `DeviceTopK`  | 2026-03-16 |  | sort, topk |
| [#7928](../sources/prs/cccl/PR-7928.md) | Implement the new tuning API for `DispatchTopK` | 2026-03-09 | double-buffering | scan, topk |
| [#7940](../sources/prs/cccl/PR-7940.md) | [cuda.compute]: Fix faulty pointer arithmetic calculation in CUB dispatch | 2026-03-09 |  |  |
| [#7949](../sources/prs/cccl/PR-7949.md) | Use the new tuning API for `detail::radix_sort::dispatch` | 2026-03-09 | double-buffering | sort |
| [#7874](../sources/prs/cccl/PR-7874.md) | Implement the new tuning API for `DispatchSegmentedSort` | 2026-03-03 | double-buffering | scan, sort |
| [#7844](../sources/prs/cccl/PR-7844.md) | Implement the new tuning API for `DispatchSegmentedRadixSort` | 2026-03-02 | double-buffering | scan, sort |
| [#7823](../sources/prs/cccl/PR-7823.md) | Optimized Device-to-Device Tensor Copy (`cudax`) | 2026-02-27 |  | sort, tma |
| [#7805](../sources/prs/cccl/PR-7805.md) | Forward policy hub from `dispatch_streaming_arg_reduce_t` to `reduce::dispatch` | 2026-02-26 |  |  |
| [#7807](../sources/prs/cccl/PR-7807.md) | Implement the new tuning API for `detail::reduce::dispatch_streaming_arg_reduce_t` | 2026-02-26 | double-buffering | reduction |
| [#7810](../sources/prs/cccl/PR-7810.md) | Use the new tuning API internally for `detail::transform::dispatch` | 2026-02-26 |  |  |
| [#7814](../sources/prs/cccl/PR-7814.md) | [Backport branch/3.3.x] Forward policy hub from `dispatch_streaming_arg_reduce_t` to `reduce::dispatch` | 2026-02-26 |  |  |
| [#7795](../sources/prs/cccl/PR-7795.md) | Add env SegmentedReduce (non fixed-size overloads) | 2026-02-25 |  | reduction |
| [#7718](../sources/prs/cccl/PR-7718.md) | Optimize non fixed size segmented reduce for small segments using max_segment_size | 2026-02-19 |  |  |
| [#7705](../sources/prs/cccl/PR-7705.md) | Add fixed_capacity_map to cudax | 2026-02-18 |  | reduction |
| [#7669](../sources/prs/cccl/PR-7669.md) | Implement the new tuning API for `DeviceRleDispatch` | 2026-02-13 |  | scan |
| [#7449](../sources/prs/cccl/PR-7449.md) | Support `cp_async_bulk_ignore_oob` in DeviceTransform | 2026-02-02 |  |  |
| [#7384](../sources/prs/cccl/PR-7384.md) | Radix-selection based `BlockTopK` specialization | 2026-01-27 |  | scan, sort, topk |
| [#7346](../sources/prs/cccl/PR-7346.md) | Implement the new tuning API for deterministic (rfa) reduce dispatch | 2026-01-25 |  | reduction |
| [#7114](../sources/prs/cccl/PR-7114.md) | Two-phase reduction for fixed size segmented reduction for very large segment sizes | 2026-01-08 |  | reduction |
| [#7093](../sources/prs/cccl/PR-7093.md) | Implement new tuning API arch dispatching | 2026-01-06 |  |  |
| [#7079](../sources/prs/cccl/PR-7079.md) | Add NVRTC compatibility errors to CUB headers | 2026-01-05 |  |  |
| [#6819](../sources/prs/cccl/PR-6819.md) | Use integer promotion for `warp_reduce` | 2025-12-01 |  | reduction |
| [#6811](../sources/prs/cccl/PR-6811.md) | Integrate decoupled lookahead warpspeed scan | 2025-11-28 | warp-specialization | mbarrier, scan, tma |
| [#6597](../sources/prs/cccl/PR-6597.md) | Split fixed-size segmented reduce dispatch header | 2025-11-12 |  | reduction |
| [#6152](../sources/prs/cccl/PR-6152.md) | Fix debug section around line 390 of dispatch_topk | 2025-10-08 |  |  |
| [#6069](../sources/prs/cccl/PR-6069.md) | Add dynamic CUB dispatch for segmented_sort | 2025-09-30 |  | scan |
| [#6077](../sources/prs/cccl/PR-6077.md) | [CUB] Use `BlockLoadToShared` in `DeviceMerge` | 2025-09-30 |  | tma |
| [#5408](../sources/prs/cccl/PR-5408.md) | Combine `block_reduce_warp_reduction_nondeterministic.cuh` specialization with original deterministic one  | 2025-08-01 |  | reduction |
| [#5314](../sources/prs/cccl/PR-5314.md) | CUB - Add internal integer utils and tests (Split `WarpReduce` PR) | 2025-07-18 |  |  |
| [#5315](../sources/prs/cccl/PR-5315.md) | [STF] Add python bindings | 2025-07-18 |  |  |
| [#4996](../sources/prs/cccl/PR-4996.md) | Implement `cudax::demangle` | 2025-06-16 |  |  |
| [#4961](../sources/prs/cccl/PR-4961.md) | Add nondeterministic reduce that uses atomics | 2025-06-11 |  | reduction |
| [#4716](../sources/prs/cccl/PR-4716.md) | Split Optimize Warp Reduce PR - CUB part | 2025-05-15 |  |  |
| [#3691](../sources/prs/cccl/PR-3691.md) | Fix SM100 histogram tunings | 2025-02-05 |  |  |
| [#3559](../sources/prs/cccl/PR-3559.md) | Add b200 tunings for scan.exclusive.sum | 2025-01-28 |  |  |
| [#3517](../sources/prs/cccl/PR-3517.md) | Fix the vectorized loading of BlockLoad | 2025-01-24 |  | topk |
| [#3236](../sources/prs/cccl/PR-3236.md) | Fix scan / sm90 perf regression  | 2025-01-02 |  |  |
| [#2944](../sources/prs/cccl/PR-2944.md) | fix thread-reduce performance regression | 2024-11-22 |  | reduction |

<a id="nvidiacutlass"></a>
## NVIDIA/cutlass
96 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#3747](../sources/prs/cutlass/PR-3747.md) | v4.8.1 update. | 2026-10-16 |  |  |
| [#3725](../sources/prs/cutlass/PR-3725.md) | [CuTeDSL] fix: accept bare int as local_partition's index argument | 2026-10-09 |  |  |
| [#3720](../sources/prs/cutlass/PR-3720.md) | [CuTeDSL] docs: fix local_tile example output shapes | 2026-10-08 |  |  |
| [#3702](../sources/prs/cutlass/PR-3702.md) | [CuTeDSL] Add MLIR_RAW and keep source locations in the clean IR | 2026-09-30 |  | gemm |
| [#3666](../sources/prs/cutlass/PR-3666.md) | [CuTeDSL] docs: fix cutlass.range unroll=0 and unroll_full descriptions | 2026-09-24 |  |  |
| [#3663](../sources/prs/cutlass/PR-3663.md) | Update 4.8 tag | 2026-09-23 | pipeline-stages, swizzling, tile-scheduling | clc, gemm |
| [#3645](../sources/prs/cutlass/PR-3645.md) | v4.8 update | 2026-09-20 | pipeline-stages, swizzling, tile-scheduling | block-scale, fp4, fp6 |
| [#3639](../sources/prs/cutlass/PR-3639.md) | [CuTeDSL] Use vectorized codegen for CUDA 12.9 2CTA grouped GEMM | 2026-09-15 |  | fp8, gemm, grouped-gemm |
| [#3636](../sources/prs/cutlass/PR-3636.md) | [CuTeDSL] Fix CLC epilogue TMA-store stage rotation | 2026-09-14 | swizzling | clc, tma |
| [#3637](../sources/prs/cutlass/PR-3637.md) | Fix: enable CUDA_CTA_RECONFIG_ACTIVATED for SM110a (Jetson AGX Thor) | 2026-09-14 |  |  |
| [#3610](../sources/prs/cutlass/PR-3610.md) | [GitHub CI] Add CUTLASS test infrastructure and CuTeDSL/C++ coverage | 2026-09-11 |  |  |
| [#3611](../sources/prs/cutlass/PR-3611.md) | Restore TMEM allocator class constants for backward compatibility | 2026-09-11 |  | tmem |
| [#3563](../sources/prs/cutlass/PR-3563.md) | [CuTeDSL] Fix blockwise GEMM opt-level version gate | 2026-08-28 |  | gemm |
| [#3565](../sources/prs/cutlass/PR-3565.md) | [CuTeDSL] Preserve deterministic link library ordering | 2026-08-28 |  |  |
| [#3556](../sources/prs/cutlass/PR-3556.md) | Update Blackwell CuTeDSL helpers for Rubin compatibility | 2026-08-27 | double-buffering, persistent-kernel, pipeline-stages | block-scale, fp8, gemm |
| [#3551](../sources/prs/cutlass/PR-3551.md) | v4.8 dev update. | 2026-08-26 | swizzling | fp4, fp8, gemm |
| [#3464](../sources/prs/cutlass/PR-3464.md) | fix(tvm-ffi): env stream detection for tuple parameters | 2026-08-15 |  |  |
| [#3448](../sources/prs/cutlass/PR-3448.md) | [CuTeDSL] Fix export_to_c shape slot width for 64-bit dynamic dims | 2026-08-12 |  |  |
| [#3446](../sources/prs/cutlass/PR-3446.md) | [CuTeDSL] Skip the numpy round-trip for in-range integer scalars | 2026-08-11 |  |  |
| [#3432](../sources/prs/cutlass/PR-3432.md) | v4.7 update. | 2026-08-04 |  | attention, flash-attention, fp8 |
| [#3426](../sources/prs/cutlass/PR-3426.md) | Cutlass compiler: Introducing CuTe IR MLIR dialect | 2026-07-31 | pipeline-stages, swizzling |  |
| [#3427](../sources/prs/cutlass/PR-3427.md) | Fix ScaledBasis equality for mismatched bases, add SM120 sparse metadata K assert | 2026-07-31 |  | block-scale, gemm, tma |
| [#3424](../sources/prs/cutlass/PR-3424.md) | [CuTe DSL] Fix REPL crash: clear diagnostic and keep the interpreter alive (issue #3413) | 2026-07-30 |  |  |
| [#3407](../sources/prs/cutlass/PR-3407.md) | [CuTeDSL] Publish IKET GEMM tutorial and update JSON schema | 2026-07-24 | pipeline-stages, swizzling, tile-scheduling | clc, gemm, quantization |
| [#3400](../sources/prs/cutlass/PR-3400.md) | fix fmha regression | 2026-07-21 |  | attention, flash-attention |
| [#3397](../sources/prs/cutlass/PR-3397.md) | SM100f distributed fix | 2026-07-20 |  | block-scale, gemm |
| [#3387](../sources/prs/cutlass/PR-3387.md) | quick fix for fmha regression | 2026-07-14 |  | attention, flash-attention |
| [#3381](../sources/prs/cutlass/PR-3381.md) | SM100 GEMM AR, GEMM RS Update | 2026-07-13 | pipeline-stages, swizzling, tile-scheduling | block-scale, gemm, tcgen05 |
| [#3383](../sources/prs/cutlass/PR-3383.md) | v4.6.1 update. | 2026-07-13 |  |  |
| [#3384](../sources/prs/cutlass/PR-3384.md) | [CuTeDSL] Allow `reassoc` fastmath flag on vector reduction ops | 2026-07-13 |  | reduction |
| [#3378](../sources/prs/cutlass/PR-3378.md) | [Hopper CuTeDSL] Add FP8 GEMM with GELU epilogues | 2026-07-09 | persistent-kernel, pipeline-stages, swizzling | fp8, gemm, tma |
| [#3376](../sources/prs/cutlass/PR-3376.md) | fix arguments for tensorop_gemm | 2026-07-08 |  |  |
| [#3369](../sources/prs/cutlass/PR-3369.md) | Fix grouped GEMM issue | 2026-07-07 |  | gemm, grouped-gemm, tma |
| [#3370](../sources/prs/cutlass/PR-3370.md) | [CuTeDSL] Gate Blackwell example tuning by CUDA backend | 2026-07-07 |  | attention, fp8, gemm |
| [#3362](../sources/prs/cutlass/PR-3362.md) | v4.6 tag release. | 2026-07-02 |  | fp8, gemm, quantization |
| [#3344](../sources/prs/cutlass/PR-3344.md) | [CLI] Recover ssd and blockwise group gemm perf | 2026-06-23 |  | attention, gemm |
| [#3328](../sources/prs/cutlass/PR-3328.md) | Fix license. | 2026-06-18 |  | attention, gemm, mla |
| [#3322](../sources/prs/cutlass/PR-3322.md) | Update tensorop_gemm.py | 2026-06-16 |  |  |
| [#3315](../sources/prs/cutlass/PR-3315.md) | v4.6 dev update. | 2026-06-12 | swizzling, tile-scheduling | block-scale, fp8, gemm |
| [#3309](../sources/prs/cutlass/PR-3309.md) | quick fix for fmha_bwd regressions | 2026-06-09 |  | attention, flash-attention |
| [#3303](../sources/prs/cutlass/PR-3303.md) | Fix dense_gemm_fp8_2xacc validation codes | 2026-06-05 |  | fp8 |
| [#3293](../sources/prs/cutlass/PR-3293.md) | Fix example with upcoming release | 2026-06-03 |  | grouped-gemm |
| [#3294](../sources/prs/cutlass/PR-3294.md) | Fix CUDA Device import for distributed CuTeDSL examples | 2026-06-03 |  |  |
| [#3295](../sources/prs/cutlass/PR-3295.md) | [CLI] quick fix for fmha compile options | 2026-06-03 |  | attention, flash-attention |
| [#3291](../sources/prs/cutlass/PR-3291.md) | [CLI] Recover fmha perf | 2026-06-02 |  | attention, flash-attention |
| [#3292](../sources/prs/cutlass/PR-3292.md) | add tileN = 8,16 for SM120 blockscale GEMM. | 2026-06-02 |  | block-scale, gemm |
| [#3285](../sources/prs/cutlass/PR-3285.md) | NFC: Replace deprecated cute.make_fragment with cute.make_rmem_tensor | 2026-05-29 |  |  |
| [#3283](../sources/prs/cutlass/PR-3283.md) | Enable tcgen05 blockscaled ops on Thor SM110 | 2026-05-28 |  | block-scale, fp4, moe |
| [#3280](../sources/prs/cutlass/PR-3280.md) | [SM120] Add ptr-array TMA collective for tensor/token-scaled FP8 grouped GEMM | 2026-05-27 | pipeline-stages | block-scale, fp8, gemm |
| [#3274](../sources/prs/cutlass/PR-3274.md) | [CLI] add mixed precision blockscaled gemm example | 2026-05-26 | swizzling | block-scale, fp4, fp6 |
| [#3270](../sources/prs/cutlass/PR-3270.md) | [CuTeDSL] Make @cute.struct instances flattenable across scf.if / scf.while | 2026-05-25 | warp-specialization |  |
| [#3272](../sources/prs/cutlass/PR-3272.md) | Add Blackwell GeForce blockscaled GEMM examples | 2026-05-25 | persistent-kernel, pipeline-stages, swizzling | block-scale, fp4, fp6 |
| [#3264](../sources/prs/cutlass/PR-3264.md) | v4.5.2 update. | 2026-05-24 |  | gemm, reduction, tma |
| [#3262](../sources/prs/cutlass/PR-3262.md) | Fix hopper grouped gemm example `elect_sync` api use | 2026-05-22 |  | gemm, grouped-gemm |
| [#3251](../sources/prs/cutlass/PR-3251.md) | [CLI] Update FMHA & improve perf | 2026-05-20 | pipeline-stages | attention, flash-attention, fp8 |
| [#3244](../sources/prs/cutlass/PR-3244.md) | [CuTe] Add missing include for smem_ptr_flag_bits in print_tensor.hpp | 2026-05-18 |  |  |
| [#3176](../sources/prs/cutlass/PR-3176.md) | Small Tile N BlockScaled GEMM + Grouped GEMM on SM12x | 2026-04-19 | pipeline-stages | block-scale, gemm, grouped-gemm |
| [#3135](../sources/prs/cutlass/PR-3135.md) | [CuTeDSL] Add a render function hook to allow render layout natively | 2026-03-30 |  |  |
| [#3130](../sources/prs/cutlass/PR-3130.md) | Update blackwell tutorial to be compatible with 4.5-dev version | 2026-03-25 |  | gemm |
| [#3124](../sources/prs/cutlass/PR-3124.md) | [CuTeDSL] Add SM103 grouped block-scaled GEMM kernel and tests | 2026-03-23 | persistent-kernel, pipeline-stages | block-scale, fp4, gemm |
| [#3106](../sources/prs/cutlass/PR-3106.md) | [CLI] add cutedsl fp16 gemm tutorial from 2 to 6 | 2026-03-13 | pipeline-stages, swizzling, tile-scheduling | clc, gemm, quantization |
| [#3092](../sources/prs/cutlass/PR-3092.md) | Support for Group GEMM in CUTLASS Profiler for GeForce and Spark | 2026-03-07 | pipeline-stages | gemm |
| [#3091](../sources/prs/cutlass/PR-3091.md) | [Hopper CuTeDSL] Add grouped GEMM kernel example | 2026-03-06 | pipeline-stages, swizzling, tile-scheduling | fp8, gemm, grouped-gemm |
| [#3055](../sources/prs/cutlass/PR-3055.md) | Replace std::min with cute::min in sm120 blockwise scaling device functions | 2026-02-23 |  | gemm |
| [#3043](../sources/prs/cutlass/PR-3043.md) | add fp4_x2 example | 2026-02-19 |  |  |
| [#3021](../sources/prs/cutlass/PR-3021.md) | [Cute-DSL] Add option for issue_clc_query without multicast | 2026-02-11 | swizzling | clc |
| [#2995](../sources/prs/cutlass/PR-2995.md) | [CuTeDSL] Fix: SM100 block-scale gemm overlapping accumulator | 2026-02-03 | pipeline-stages | block-scale, gemm, tmem |
| [#2965](../sources/prs/cutlass/PR-2965.md) | [Bug Fix]Set NumSplitsM to 1 when TileShapeM < 128 in sm90 fp8 blockwise scaling CollectiveMma | 2026-01-19 |  | fp8, gemm |
| [#2921](../sources/prs/cutlass/PR-2921.md) | Fix incorrect tensor layout strides in Blackwell MMA tutorial comments | 2026-01-03 |  |  |
| [#2881](../sources/prs/cutlass/PR-2881.md) | new example with TMA prefetch feature targeting for DRAM latency boun… | 2025-12-16 | pipeline-stages, swizzling, tile-scheduling | fp8, gemm, quantization |
| [#2875](../sources/prs/cutlass/PR-2875.md) | [cute] Add constexpr specifier to make_tiled_copy | 2025-12-12 |  |  |
| [#2865](../sources/prs/cutlass/PR-2865.md) | [Bug Fix]Bypass launch grids for SM120 Kernel with SM90 Mainloop & SM100 TileScheduler | 2025-12-09 | tile-scheduling | block-scale, gemm |
| [#2851](../sources/prs/cutlass/PR-2851.md) | add `SM75_16x8x8_F16F16F16F16_TN` | 2025-12-06 |  |  |
| [#2790](../sources/prs/cutlass/PR-2790.md) | Blockscaled Ragged Contiguous Grouped Gemm for MoEs | 2025-11-21 | tile-scheduling, warp-specialization | block-scale, fp4, gemm |
| [#2750](../sources/prs/cutlass/PR-2750.md) | Add tutorial fp16_gemm_1 | 2025-11-05 | pipeline-stages, swizzling | gemm, tcgen05, tma |
| [#2746](../sources/prs/cutlass/PR-2746.md) | Support for GEMM-K=0 for Blackwell Grouped GEMMs | 2025-11-04 |  | gemm |
| [#2719](../sources/prs/cutlass/PR-2719.md) | Support PDL for SM90 Array TMA GEMM | 2025-10-24 |  | gemm, grouped-gemm, tma |
| [#2713](../sources/prs/cutlass/PR-2713.md) | DistGEMM bug fixes | 2025-10-22 |  | gemm |
| [#2599](../sources/prs/cutlass/PR-2599.md) | fix gqa issue for blackwell fmha.py | 2025-08-28 |  | attention, flash-attention |
| [#2492](../sources/prs/cutlass/PR-2492.md) | fix: examples/cute/tutorial/blackwell/04_mma_tma_2sm_sm100.cu GridDim miscalculated | 2025-07-23 |  |  |
| [#2472](../sources/prs/cutlass/PR-2472.md) | Add Blackwell MLA forward (shape: d=192, dv=128) implementation | 2025-07-16 | persistent-kernel, tile-scheduling | attention, flash-attention, fp8 |
| [#2466](../sources/prs/cutlass/PR-2466.md) | Example 77 add blackwell fmha bwd for MLA shape | 2025-07-14 |  | attention, flash-attention, fp8 |
| [#2378](../sources/prs/cutlass/PR-2378.md) | support fp16 accmulator for sm89 fp8 mma | 2025-06-07 |  | fp8 |
| [#2366](../sources/prs/cutlass/PR-2366.md) | [ex77] fix mla split; add fwd lse; add bwd varlen | 2025-06-04 | persistent-kernel, tile-scheduling | attention, flash-attention, mla |
| [#2333](../sources/prs/cutlass/PR-2333.md) | Fix epilogue::thread::Convert cannot be used with DefaultEpilogue | 2025-05-26 |  | gemm |
| [#2270](../sources/prs/cutlass/PR-2270.md) | hopper-blockwise-generalization-optimization | 2025-04-29 | pipeline-stages, tile-scheduling, warp-specialization | block-scale, fp8, gemm |
| [#2220](../sources/prs/cutlass/PR-2220.md) | Set EpiTile correctly when TileN is not divisible by 32 | 2025-04-04 |  |  |
| [#2161](../sources/prs/cutlass/PR-2161.md) | Blockwise Improvement and Programmatic Dependent Launch | 2025-03-10 |  | gemm |
| [#2134](../sources/prs/cutlass/PR-2134.md) | Flash MLA Support - Step 2 | 2025-02-26 |  | mla |
| [#2139](../sources/prs/cutlass/PR-2139.md) | Blockwise and Groupwise GEMM for Blackwell and Improvements for Hopper | 2025-02-26 | swizzling, tile-scheduling, warp-specialization | block-scale, clc, fp8 |
| [#2130](../sources/prs/cutlass/PR-2130.md) | Flash MLA support | 2025-02-24 | double-buffering, swizzling, tile-scheduling | flash-attention, fp8, gemm |
| [#2123](../sources/prs/cutlass/PR-2123.md) | Hopper Grouped GEMM support for FP8 Accum | 2025-02-20 | pipeline-stages, warp-specialization | fp8, gemm, grouped-gemm |
| [#2095](../sources/prs/cutlass/PR-2095.md) | Improvements for: Groupwise scaling along M for FP8 gemm | 2025-02-10 |  | block-scale, fp8, gemm |
| [#2037](../sources/prs/cutlass/PR-2037.md) | Groupwise scaling along M for FP8 gemm | 2025-01-13 | swizzling, tile-scheduling, warp-specialization | block-scale, fp8, gemm |
| [#2033](../sources/prs/cutlass/PR-2033.md) | [EVT] Add support for Row/Col broadcast PtrArray | 2025-01-08 |  | fp8, gemm, grouped-gemm |
| [#1883](../sources/prs/cutlass/PR-1883.md) | Improve sm90 mixed dtype kernel | 2024-10-18 | warp-specialization | block-scale, fp8, gemm |

<a id="deepseek-aideepgemm"></a>
## deepseek-ai/DeepGEMM
17 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#478](../sources/prs/DeepGEMM/PR-478.md) | Fix mega_mhc split barriers under CUDA graph replay | 2026-10-19 |  |  |
| [#471](../sources/prs/DeepGEMM/PR-471.md) | Public release 10/14 | 2026-10-14 | pipeline-stages | fp8, gemm, moe |
| [#462](../sources/prs/DeepGEMM/PR-462.md) | Public release 26/09/30 | 2026-09-30 | persistent-kernel, pipeline-stages | fp4, fp8, gemm |
| [#441](../sources/prs/DeepGEMM/PR-441.md) | Fix Mega MoE task info slot release ordering | 2026-09-14 |  | moe |
| [#432](../sources/prs/DeepGEMM/PR-432.md) | Public Release 26/09 | 2026-09-10 | epilogue-fusion, pipeline-stages, swizzling | block-scale, fp4, fp8 |
| [#377](../sources/prs/DeepGEMM/PR-377.md) | Public release 26/07 | 2026-07-14 | pipeline-stages, swizzling | block-scale, fp4, fp8 |
| [#364](../sources/prs/DeepGEMM/PR-364.md) | Multiple updates and refactorings | 2026-06-23 | pipeline-stages, swizzling | block-scale, fp4, fp8 |
| [#347](../sources/prs/DeepGEMM/PR-347.md) | Multiple updates and refactorings | 2026-06-01 | swizzling | attention, fp4, fp8 |
| [#343](../sources/prs/DeepGEMM/PR-343.md) | Fix a race condition in contiguous k-grouped GEMM where in-flight tensormaps are updated in-place | 2026-05-29 |  | gemm, grouped-gemm, mbarrier |
| [#328](../sources/prs/DeepGEMM/PR-328.md) | Sync nv_dev with upstream #316 (Mega MoE optimizations & benchmarks) | 2026-05-07 |  | attention, moe, tcgen05 |
| [#304](../sources/prs/DeepGEMM/PR-304.md) | [Public release 26/04] Introducing Mega MoE, FP4 Indexer and other features/fixes | 2026-04-16 | pipeline-stages, swizzling | block-scale, fp4, fp8 |
| [#193](../sources/prs/DeepGEMM/PR-193.md) | Fix multicast bug and optimize masked GEMM | 2025-09-12 |  | gemm |
| [#168](../sources/prs/DeepGEMM/PR-168.md) | Fix performance issue of m-grouped contiguous GEMMs. | 2025-08-20 |  | gemm |
| [#88](../sources/prs/DeepGEMM/PR-88.md) | Support TMA multicast on B with m_grouped_gemm_contiguous. | 2025-04-18 |  | gemm, tma |
| [#86](../sources/prs/DeepGEMM/PR-86.md) | Use swizzling instead of padding | 2025-04-14 | swizzling | tma, wgmma |
| [#83](../sources/prs/DeepGEMM/PR-83.md) | Use 1D TMA store instead of 3D | 2025-04-11 |  | tma, wgmma |
| [#78](../sources/prs/DeepGEMM/PR-78.md) |  Solving bank conflict via padding and TMA 3D store | 2025-04-03 |  | tma, wgmma |

<a id="deepseek-aitilekernels"></a>
## deepseek-ai/TileKernels
2 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#38](../sources/prs/TileKernels/PR-38.md) | Release tile-kernels v2.1.0 | 2026-10-14 | pipeline-stages | fp8, quantization, reduction |
| [#34](../sources/prs/TileKernels/PR-34.md) | Release tile-kernels v2.0.0 | 2026-09-30 | double-buffering, pipeline-stages | fp4, fp8, gemm |

<a id="flashinfer-aiflashinfer"></a>
## flashinfer-ai/flashinfer
1266 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#6813](../sources/prs/flashinfer/PR-6813.md) | deslop(cake_nvfp4_per_token): fold kernel and binding twins, slim the registry, ship csrc in wheels | 2026-10-20 | stream-k, swizzling | fp4, gemm, mbarrier |
| [#6816](../sources/prs/flashinfer/PR-6816.md) | perf(cake_causal_conv1d): per-warp staged with grad with eight channels per thread on sm_100a, sm_103a and sm_107a | 2026-10-20 | pipeline-stages | mbarrier, reduction |
| [#6819](../sources/prs/flashinfer/PR-6819.md) | fix(cake_deepgemm_mixed_gemm): wait for the peer CTA's last stage releases before the load warp exits | 2026-10-20 | pipeline-stages | fp4, fp8, gemm |
| [#6820](../sources/prs/flashinfer/PR-6820.md) | fix(cake_minimax_h3): wait for the peer CTA's last stage releases before the pre-attention QKV GEMM load warp exits | 2026-10-20 | pipeline-stages | attention, fp4, gemm |
| [#6821](../sources/prs/flashinfer/PR-6821.md) | fix(cake_kimi_k3_latent_moe): wait for the peer CTA's last stage releases before the tail GEMM load warp exits | 2026-10-20 | pipeline-stages | gemm, mbarrier, moe |
| [#6822](../sources/prs/flashinfer/PR-6822.md) | fix(cake_minimax_h3): wait for the peer CTA's last stage releases before the FC1 / MLP / out-proj GEMM load warps exit | 2026-10-20 |  | fp4, gemm, mbarrier |
| [#6825](../sources/prs/flashinfer/PR-6825.md) | feat(moe): Trtllm gen workspace size | 2026-10-20 |  | gemm, moe, quantization |
| [#6827](../sources/prs/flashinfer/PR-6827.md) | deslop(cake_sage_block_sparse_attention): one SM120 kernel source, drop degenerate modules and dead device code | 2026-10-20 |  | attention, fp8, mbarrier |
| [#6828](../sources/prs/flashinfer/PR-6828.md) | fix(cake_mla): address each warp's own TMEM lane quarter in the FP8 page-32 Blackwell MLA decode | 2026-10-20 | pipeline-stages | attention, fp8, mla |
| [#6830](../sources/prs/flashinfer/PR-6830.md) | deslop(cake_kimi_k3_vision_tower): one launcher for the 76 host bindings, fold SM100 attention copies, compact registry | 2026-10-20 |  | attention, gemm, tcgen05 |
| [#6831](../sources/prs/flashinfer/PR-6831.md) | perf(cake_comm): QkvNormRopeExchangeOverlap SM107 four-rank plans use the bulk-row-store build | 2026-10-20 | pipeline-stages | mbarrier, tcgen05, tma |
| [#6836](../sources/prs/flashinfer/PR-6836.md) | feat(cake_dsa): native NoPE sparse MLA kernels (GLM-5.3-Flash) for the 64-head DSA backend on SM100 / SM103 / SM107 with grad (#6489) | 2026-10-20 | pipeline-stages | attention, mbarrier, mla |
| [#6841](../sources/prs/flashinfer/PR-6841.md) | perf(cake_all_gather_matmul): SM103a peer-outer tile order, TP4 gate/up | 2026-10-20 | pipeline-stages | gemm, mbarrier, tcgen05 |
| [#6842](../sources/prs/flashinfer/PR-6842.md) | perf(cake_rmsnorm): faster H1536 / H4096 grad (SM100 / SM103 / SM107) | 2026-10-20 | pipeline-stages | mbarrier, reduction |
| [#6844](../sources/prs/flashinfer/PR-6844.md) | perf(cake_causal_conv1d): 2-D TMA stage loads in the sm_100a/sm_103a with grad | 2026-10-20 | pipeline-stages | mbarrier, tma |
| [#6847](../sources/prs/flashinfer/PR-6847.md) | fix(cake_minimax_h3): order the SM120 dense attention epilogue before the next Q TMA refill and close the ping-pong barrier | 2026-10-20 |  | attention, fp4, fp8 |
| [#6857](../sources/prs/flashinfer/PR-6857.md) | perf(cake_w8a8_megamoe_ep16): evict-first L2 hint on the FC2 weight loads | 2026-10-20 |  | gemm, mbarrier, moe |
| [#6862](../sources/prs/flashinfer/PR-6862.md) | deslop(cake_fp8_gemm): table-driven batch routing, shared headers, mxfp8 and grouped source folds, dead host text | 2026-10-20 | pipeline-stages, swizzling | fp8, gemm, grouped-gemm |
| [#6867](../sources/prs/flashinfer/PR-6867.md) | refactor(cake_fused_qk_rope_fp8_append): regenerate the kernel and route the host through the in-tree program loader | 2026-10-20 |  | fp8, quantization |
| [#6868](../sources/prs/flashinfer/PR-6868.md) | refactor(cake_grouped_mxfp8_quantize): regenerate the kernels and route the host through the in-tree program loader | 2026-10-20 |  | quantization |
| [#6869](../sources/prs/flashinfer/PR-6869.md) | refactor(cake_minimax_h3_qkv_quantize_pack): regenerate the kernels and route the host through the in-tree program loader | 2026-10-20 |  | block-scale, fp4, nvfp4 |
| [#6871](../sources/prs/flashinfer/PR-6871.md) | deslop(cake_stepfun_moe): derived launchers, compact registry, routing-twin fold, 47 shared bindings, preamble hoist | 2026-10-20 |  | fp4, fp8, moe |
| [#6872](../sources/prs/flashinfer/PR-6872.md) | perf(cake_sage): faster SM100/SM103 Sage-FP8 block-sparse attention and quantizers | 2026-10-20 |  | attention, fp8, quantization |
| [#6874](../sources/prs/flashinfer/PR-6874.md) | perf(cake_causal_conv1d): a shape-selected big-channel backward program (C >= 512 on sm_100a/sm_103a, C >= 1024 on sm_107a) | 2026-10-20 | pipeline-stages | mbarrier |
| [#6876](../sources/prs/flashinfer/PR-6876.md) | deslop(cake_kda_tf32): dead host code, one device-helper header, 24 kernel clones folded onto 9 bodies | 2026-10-20 | pipeline-stages | mbarrier, tcgen05, tma |
| [#6878](../sources/prs/flashinfer/PR-6878.md) | perf(cake_nvfp4_svdquant): converge the Cake NVFP4 SVDQuant GEMM backend and ship it as a vendorable package | 2026-10-20 | pipeline-stages | block-scale, fp4, gemm |
| [#6879](../sources/prs/flashinfer/PR-6879.md) | deslop(cake_kimi_k3_situ): dead selectors, one device-helper header, the FC1 pair folded, nine host bindings shared | 2026-10-20 | pipeline-stages | block-scale, fp4, mbarrier |
| [#6758](../sources/prs/flashinfer/PR-6758.md) | deslop(cake_kda_bf16): render the host bindings, fold the fused-M128 clones, route kernel-less requests, trim dead host code | 2026-10-19 | persistent-kernel | tcgen05, tma |
| [#6759](../sources/prs/flashinfer/PR-6759.md) | feat(cake_w8a8_megamoe_ep16): experimental W8A8 MXFP8 MegaMoE EP16 backend for SM103 | 2026-10-19 | pipeline-stages, swizzling | block-scale, fp8, gemm |
| [#6761](../sources/prs/flashinfer/PR-6761.md) | perf(cake_all_gather_matmul): SM103a 16-CTA push launch, 1024-row TP8 | 2026-10-19 |  | gemm |
| [#6763](../sources/prs/flashinfer/PR-6763.md) | fix(cake_dense_projection_gemm): every CTA-pair program drains the multicast stage releases before it exits | 2026-10-19 | pipeline-stages | gemm, tcgen05 |
| [#6765](../sources/prs/flashinfer/PR-6765.md) | feat(cake_rmsnorm): re-export the BF16 RMSNorm grad for sm_100a, sm_103a and sm_107a | 2026-10-19 |  |  |
| [#6766](../sources/prs/flashinfer/PR-6766.md) | deslop(cake_blackwell_msa): fold uniform-FP8 arch pair, share NVFP4 helpers, name arg plans once | 2026-10-19 | pipeline-stages | fp4, fp8, mbarrier |
| [#6767](../sources/prs/flashinfer/PR-6767.md) | fix(cake_alpha_moe): one TMEM address per warp for the NVFP4 epilogue tcgen05.ld | 2026-10-19 |  | fp4, moe, nvfp4 |
| [#6769](../sources/prs/flashinfer/PR-6769.md) | perf(cake_quant_lora_gemm): W-resident strip raster for the SM90 FP8 LoRA GEMM hint program | 2026-10-19 | tile-scheduling | fp4, fp8, gemm |
| [#6775](../sources/prs/flashinfer/PR-6775.md) | perf(cake_ssd_combined): SM107 varlen exact-scan geometry through the aux stage and full-grid tail-pair routing | 2026-10-19 |  |  |
| [#6778](../sources/prs/flashinfer/PR-6778.md) | fix(cake_dsa_train): each warp's tcgen05.ld addresses its own TMEM lane quarter | 2026-10-19 |  | attention, sparse-attention, tcgen05 |
| [#6780](../sources/prs/flashinfer/PR-6780.md) | deslop(cake_kimi_k3_fp8_projection): share kernel/launcher sources, slim MODULES, drop dead host code | 2026-10-19 | stream-k | attention, fp8, gemm |
| [#6782](../sources/prs/flashinfer/PR-6782.md) | feat(cake_causal_conv1d): packed causal conv + SiLU kernels for sm_100a, sm_103a and sm_107a with grad | 2026-10-19 | pipeline-stages | attention, mbarrier, reduction |
| [#6787](../sources/prs/flashinfer/PR-6787.md) | feat(cake_kda): packed KDA chunked training kernels for GLM-5.3-Flash with grad | 2026-10-19 | pipeline-stages | attention, mbarrier, tcgen05 |
| [#6788](../sources/prs/flashinfer/PR-6788.md) | perf(moe): advertise FP4 tile 192 on Rubin and widen the trtllm-gen MoE tuner window by one tile below | 2026-10-19 |  | block-scale, fp4, moe |
| [#6792](../sources/prs/flashinfer/PR-6792.md) | feat(cake_rmsnorm): add H1536 / H4096 routes with grad (SM100 / SM103 / SM107) | 2026-10-19 |  | reduction |
| [#6796](../sources/prs/flashinfer/PR-6796.md) | feat(cake_w8a8_megamoe_ep16): regenerate the six device kernels from their Cake sources | 2026-10-19 |  | quantization, tcgen05 |
| [#6801](../sources/prs/flashinfer/PR-6801.md) | feat(cake_stepfun): StepFun SwiGLU fused MoE Cake backend in the cake-build form (SM100a, SM103a) | 2026-10-19 | pipeline-stages | block-scale, fp4, fp8 |
| [#6802](../sources/prs/flashinfer/PR-6802.md) | deslop(cake_dsa_indexer): fold kernel twins, share launcher bindings, drop dead registry glue | 2026-10-19 |  | scan, tma, topk |
| [#6806](../sources/prs/flashinfer/PR-6806.md) | fix(cake_selective_state_update): sync each consumer warp before its elected stage release | 2026-10-19 |  |  |
| [#6808](../sources/prs/flashinfer/PR-6808.md) | fix(cake_ssd_combined): regenerate the device sources with tcgen05 thread-sync fences on every thread synchronization | 2026-10-19 |  | tcgen05 |
| [#6715](../sources/prs/flashinfer/PR-6715.md) | perf(cake_ssd_combined): capability-routed one-launch and tail-wave exact-scan programs for Blackwell | 2026-10-18 |  | mbarrier, tcgen05, tma |
| [#6718](../sources/prs/flashinfer/PR-6718.md) | fix(cake_mla): skip empty KV splits in the FP8 page-64 MLA decode producer | 2026-10-18 | pipeline-stages | attention, fp8, mbarrier |
| [#6719](../sources/prs/flashinfer/PR-6719.md) | deslop(cake_vsa): fold duplicated sources and remove the SM90 CuTe DSL build | 2026-10-18 |  | attention, sparse-attention, tcgen05 |
| [#6720](../sources/prs/flashinfer/PR-6720.md) | perf(cake_diffusion): MiniMax-H3 FC1+SwiGLU 256x448 MXFP8 tile, PDL and packed epilogue rounding; prologue scale arithmetic (SM100/SM103) | 2026-10-18 | pipeline-stages | fp4, fp8, gemm |
| [#6723](../sources/prs/flashinfer/PR-6723.md) | deslop(cake_warp_decode): remove dead JSON, FFI exports and host code; move checks to tests | 2026-10-18 |  | fp4, gemm, moe |
| [#6725](../sources/prs/flashinfer/PR-6725.md) | perf(cake_msa): persistent heavy-first union prefill, streaming Top-K merge/scan (rounds 11-15 re-export) | 2026-10-18 |  | attention, fp8, sort |
| [#6728](../sources/prs/flashinfer/PR-6728.md) | perf(cake_quant_lora_gemm): faster SM90 FP8 LoRA GEMM mainloop | 2026-10-18 |  | fp4, fp8, gemm |
| [#6731](../sources/prs/flashinfer/PR-6731.md) | deslop(cake_dsv4): share arch-identical SM100/SM103 kernels, fold NVFP4 launchers, drop dead host paths | 2026-10-18 |  | attention, fp4, fp8 |
| [#6733](../sources/prs/flashinfer/PR-6733.md) | deslop(cake_deepgemm_mqa): fold SM120 and dense paged clones, share the host helper, drop unread catalog data | 2026-10-18 |  | fp4, fp8, tcgen05 |
| [#6737](../sources/prs/flashinfer/PR-6737.md) | deslop(cake_minimax_h3): merge SM100/SM103 sources, share the FP8 FC1 GEMMs, fold nodelta clones | 2026-10-18 | swizzling | attention, fp4, fp8 |
| [#6739](../sources/prs/flashinfer/PR-6739.md) | deslop(cake_mamba): drop unreachable SSD sources, share the exactpre launcher, fold the STP mb4 clone | 2026-10-18 |  |  |
| [#6740](../sources/prs/flashinfer/PR-6740.md) | fix(cake_kimi_k3_attn_res): drain tcgen05.ld with tcgen05.wait::ld before the TMEM dealloc (persistent programs) | 2026-10-18 |  | attention, tcgen05, tmem |
| [#6742](../sources/prs/flashinfer/PR-6742.md) | perf(cake_all_gather_matmul): SM103a K-slice readiness, 512-row TP8 push | 2026-10-18 | pipeline-stages | gemm, mbarrier, tcgen05 |
| [#6744](../sources/prs/flashinfer/PR-6744.md) | fix(cake_kimi_k3_attn_res): drain tcgen05.ld with tcgen05.wait::ld before the TMEM dealloc (native programs) | 2026-10-18 |  | attention, tcgen05, tmem |
| [#6745](../sources/prs/flashinfer/PR-6745.md) | deslop(cake_bgmv_moe): drop 30 never-launched kernels, fold hidden/rank/FMA clones, gate per target | 2026-10-18 | pipeline-stages | moe |
| [#6746](../sources/prs/flashinfer/PR-6746.md) | feat(cake_ssd_combined): Rubin sm_107a programs for the Mamba2 SSD combined prefill | 2026-10-18 | pipeline-stages | mbarrier, tcgen05, tmem |
| [#6747](../sources/prs/flashinfer/PR-6747.md) | perf(cake): sm_107a (Rubin) kernels for DeepSeek fused routing, BGMV MoE and concat-MLA-K | 2026-10-18 |  | mla, moe, topk |
| [#6748](../sources/prs/flashinfer/PR-6748.md) | deslop(cake_msa_icp_indexer): fold the scorer clones via -DBLOCK_Q, share one binding per role, drop dead host code | 2026-10-18 |  | fp8, tma |
| [#6750](../sources/prs/flashinfer/PR-6750.md) | perf(cake_deepgemm_kgroup_gemm): host-built LPT tile order for seven three-group keys (M = 5120 / N = 2304 and M = 4608 / N = 5120 across bf16 / fp32 / fp32-accumulate output modes) on the N256 and BM240 schedules on SM100a and SM103a | 2026-10-18 | pipeline-stages, swizzling | fp4, gemm, grouped-gemm |
| [#6751](../sources/prs/flashinfer/PR-6751.md) | deslop(cake_fused_qk_rope_append): one kernel and binding per family, slim manifests, policy-gap fix | 2026-10-18 |  | fp8, mla, quantization |
| [#6752](../sources/prs/flashinfer/PR-6752.md) | perf(cake_gdn): refresh Blackwell GDN prefill bodies for 84 records (guard fold, tcgen05 thread-sync fences) | 2026-10-18 |  | fp8, tcgen05 |
| [#6753](../sources/prs/flashinfer/PR-6753.md) | perf(cake_quant_lora_gemm): hoisted stage wait in the SM90 FP8 LoRA GEMM | 2026-10-18 |  | fp4, fp8, gemm |
| [#6754](../sources/prs/flashinfer/PR-6754.md) | perf(cake_rubin): sm_107a (Rubin) kernels for GDN prefill, GDN decode and packed KDA T=1 | 2026-10-18 | pipeline-stages | fp8, mbarrier |
| [#6756](../sources/prs/flashinfer/PR-6756.md) | deslop(cake_kimi_k3_attn_res): shared sources, three launch bindings, tabular registry, dead planner code | 2026-10-18 |  | attention |
| [#6613](../sources/prs/flashinfer/PR-6613.md) | feat(cake_comm): QkvNormRopeExchangeOverlap per-world-size producer variants and plan defaults on sm_100a / sm_103a / sm_90a | 2026-10-17 | pipeline-stages | mbarrier, tcgen05, tma |
| [#6614](../sources/prs/flashinfer/PR-6614.md) | feat(cake_bf16_fp4_gemm): faster SM100/SM103 BF16 x FP4 GEMM kernels for the blackwell-native and blackwell-tiled backends | 2026-10-17 | pipeline-stages | block-scale, fp4, gemm |
| [#6616](../sources/prs/flashinfer/PR-6616.md) | feat(mla): read DeepSeek-V4.1 inline-scale KV records natively on SM120 | 2026-10-17 | pipeline-stages | attention, fp4, fp8 |
| [#6620](../sources/prs/flashinfer/PR-6620.md) | feat(cake_comm): QkvNormRopeExchangeOverlap adds the SM107 (Rubin) producer programs | 2026-10-17 | pipeline-stages | mbarrier, tcgen05, tma |
| [#6622](../sources/prs/flashinfer/PR-6622.md) | perf(cake_fused_moe): Kimi-K3 NVFP4 SiTU experts SM100 8192-token row: fused quantization + reset and 512-pair routing CTAs | 2026-10-17 | pipeline-stages | fp4, moe, nvfp4 |
| [#6624](../sources/prs/flashinfer/PR-6624.md) | perf(cake_all_gather_matmul): SM103a spill-split pair twins for gate/up | 2026-10-17 | pipeline-stages | mbarrier, tcgen05, tma |
| [#6627](../sources/prs/flashinfer/PR-6627.md) | fix(cake_mega_moe): route a topk_idx of -1 to no expert in mega_moe_v3 | 2026-10-17 | pipeline-stages | fp4, fp8, mbarrier |
| [#6628](../sources/prs/flashinfer/PR-6628.md) | perf(cake_fused_moe): Kimi-K3 NVFP4 SiTU experts SM100 8- and 16-token rows with evict-first weight-stream loads | 2026-10-17 | pipeline-stages | block-scale, fp4, mbarrier |
| [#6685](../sources/prs/flashinfer/PR-6685.md) | deslop(cake_sampling): delete the 42 stage-1 kernel builds the host dispatch never selects | 2026-10-17 |  |  |
| [#6690](../sources/prs/flashinfer/PR-6690.md) | deslop(cake_mok_bf16): share the fused bindings and BF16 kernels across targets, one launcher per shape, compact sources.json, drop the uncalled helper | 2026-10-17 | kernel-fusion | moe, tma, topk |
| [#6696](../sources/prs/flashinfer/PR-6696.md) | deslop(cake_mxfp4_situ_moe): fix pack_g1_geom, delete the 16 unreachable stages, share the dense GEMM sources between the PDL and _nopdl modules | 2026-10-17 |  | fp4, gemm, moe |
| [#6704](../sources/prs/flashinfer/PR-6704.md) | deslop(cake_fmha): caller-LSE fix, fold the kernel clones and per-arch copies into one source per family, dedupe host code, add the fp8 decode GPU test | 2026-10-17 | pipeline-stages | attention, block-scale, clc |
| [#6706](../sources/prs/flashinfer/PR-6706.md) | perf(cake_gdn): faster Blackwell GDN prefill programs for 84 records (sm_100a, sm_103a) | 2026-10-17 |  | tcgen05, tmem |
| [#6707](../sources/prs/flashinfer/PR-6707.md) | deslop(cake_gdn): remove dead text, merge clone bodies, render host shims | 2026-10-17 |  | mbarrier, tma |
| [#6710](../sources/prs/flashinfer/PR-6710.md) | perf(cute_dsl_mla): let small CuTe-DSL MLA decode launches use more KV splits | 2026-10-17 |  | attention, fp8, mla |
| [#6712](../sources/prs/flashinfer/PR-6712.md) | deslop(cake_kda): render bindings, fold clone bodies, drop dead PTX host code | 2026-10-17 | persistent-kernel | tcgen05 |
| [#6572](../sources/prs/flashinfer/PR-6572.md) | fix(cake_moe_grouped_gemm): rotate wgrad tensor-map slots so a group switch never edits a map an in-flight TMA load still reads (#6570) | 2026-10-16 | pipeline-stages | gemm, grouped-gemm, moe |
| [#6577](../sources/prs/flashinfer/PR-6577.md) | perf(cake_fused_moe): swap-AB cluster split-K GEMM1 forms, grouped dense raster and the CuTe DSL cluster rendezvous fix for the Kimi-K3 MXFP4 SiTU MoE export (cake, cake_cute) | 2026-10-16 | pipeline-stages, tile-scheduling | attention, flash-attention, fp4 |
| [#6578](../sources/prs/flashinfer/PR-6578.md) | perf(cake_dsv4): launch the NVFP4 sparse-MLA decode split-KV merge with programmatic dependent launch (SM100/SM103) | 2026-10-16 |  | attention, fp4, mla |
| [#6579](../sources/prs/flashinfer/PR-6579.md) | perf(cake_deepgemm_dense_mqa): v11 re-export on the folded catalog, withdrawn paged points | 2026-10-16 | pipeline-stages | block-scale, fp4, fp8 |
| [#6580](../sources/prs/flashinfer/PR-6580.md) | feat(cake_msa_icp_indexer): add world-2 exchange-merge geometries (8,8), (4,8), (2,8), (2,6), (1,6) for sm_100a and sm_103a | 2026-10-16 |  | fp4, moe, nvfp4 |
| [#6581](../sources/prs/flashinfer/PR-6581.md) | feat(cake_quant_lora_gemm): prepared NVFP4 LoRA adapter (SVDQuant-equivalent fold) and re-export of the fused quantized-base GEMM + runtime BF16 LoRA kernels | 2026-10-16 | pipeline-stages | fp4, fp8, gemm |
| [#6582](../sources/prs/flashinfer/PR-6582.md) | perf(cake_ssd_combined): fused exact-scan programs, host routing, look-back chunk-parallel, exactpre family (SM100 / SM103) | 2026-10-16 | pipeline-stages | mbarrier, scan, tcgen05 |
| [#6584](../sources/prs/flashinfer/PR-6584.md) | refactor(cake): build.json manifests, shared cake_build loader, header-free bindings; MoK sm_107a BF16/MXFP8 kernels (#6553 steps 2-4) | 2026-10-16 | pipeline-stages | mbarrier, moe, tcgen05 |
| [#6586](../sources/prs/flashinfer/PR-6586.md) | perf(cake_all_gather_matmul): SM100a CTA-pair main kernel for nine measured shapes | 2026-10-16 |  | tcgen05, tma |
| [#6590](../sources/prs/flashinfer/PR-6590.md) | fix(cake_mla): read layout-B scores from the warp's TMEM lane quarter | 2026-10-16 |  | attention, clc, fp8 |
| [#6606](../sources/prs/flashinfer/PR-6606.md) | perf(cake_all_gather_matmul): SM103a 16-CTA push and ws2 CTA-pair points | 2026-10-16 | pipeline-stages | mbarrier, tcgen05, tma |
| [#6507](../sources/prs/flashinfer/PR-6507.md) | perf(gdn): Rubin (SM107) chunked-prefill kernel subclass and SM107 fp32 decode launch config | 2026-10-15 | pipeline-stages | tmem |
| [#6508](../sources/prs/flashinfer/PR-6508.md) | feat(gemm): SM107 CuTe-DSL blockwise FP8 GEMM backend for gemm_fp8_nt_groupwise | 2026-10-15 | pipeline-stages, swizzling, tile-scheduling | block-scale, fp8, gemm |
| [#6511](../sources/prs/flashinfer/PR-6511.md) | perf(cake_alpha_moe): faster NVFP4 routed-MoE routes on sm_100a/sm_103a (self-routing up kernels, K-256 W2 panels, per-CC dispatch) | 2026-10-15 | pipeline-stages | attention, block-scale, flash-attention |
| [#6512](../sources/prs/flashinfer/PR-6512.md) | perf(cake_alpha_moe): dispatch the W8A8 fused MoE kernel by (M, K) across three pipeline variants | 2026-10-15 | kernel-fusion, pipeline-stages | attention, block-scale, flash-attention |
| [#6516](../sources/prs/flashinfer/PR-6516.md) | perf(cake_comm): fold the readiness barrier into the QKV norm+RoPE exchange producer (2 launches per call, default on SM90/SM100/SM103) | 2026-10-15 | kernel-fusion, pipeline-stages | mbarrier, reduction, tcgen05 |
| [#6518](../sources/prs/flashinfer/PR-6518.md) | perf(cake_msa): faster Blackwell MSA uniform-FP8 decode and Top-K programs — epilogue overlap and QK ahead of PV (D-U1, D-U2, D-U2b), streaming Top-K merge network (S2), tradix v2 radix layout, per-architecture topk_select (CAKE-1183 round 10) | 2026-10-15 | pipeline-stages, swizzling | attention, fp4, fp8 |
| [#6519](../sources/prs/flashinfer/PR-6519.md) | feat(cake_gdn): host-free non-CP prefill launch -- optional cu_seqlens_cpu, no device-to-host sync, launch ABI v2 | 2026-10-15 | pipeline-stages, tile-scheduling | mbarrier, tcgen05 |
| [#6524](../sources/prs/flashinfer/PR-6524.md) | perf(cake_deepgemm_fp4_gemm): cooperative mbarrier initialisation on six routes, early load start on the BN224 / BN256 routes, and a cross-pass epilogue pipeline on the normal BN160 program (SM100a, SM103a; outputs bitwise unchanged) | 2026-10-15 | pipeline-stages | block-scale, fp4, fp8 |
| [#6525](../sources/prs/flashinfer/PR-6525.md) | perf(cake_deepgemm_mixed_gemm): cooperative mbarrier initialisation, early load start, and a split-K route for the 148-SM M = 16 / N = 4608 / K = 5120 swap-AB configuration (SM100a, SM103a; shipped programs bitwise unchanged, split-K output deterministic) | 2026-10-15 | pipeline-stages | block-scale, fp4, fp8 |
| [#6526](../sources/prs/flashinfer/PR-6526.md) | perf(cake_deepgemm_batched_gemm): evict-first B-operand loads on the swap-AB batched FP8 GEMM programs (SM100a, SM103a; outputs bitwise unchanged) | 2026-10-15 |  | block-scale, fp4, fp8 |
| [#6529](../sources/prs/flashinfer/PR-6529.md) | feat(prims-ts): cache attention kernels and enable FP8-to-BF16 decode | 2026-10-15 |  | attention, fp4, fp8 |
| [#6530](../sources/prs/flashinfer/PR-6530.md) | perf(cake_deepgemm): SM120 paged MQA-logits indexer: batch-aware Q-atom programs, DeepGEMM block-table cache, num_heads metadata kwarg | 2026-10-15 | pipeline-stages | fp8, mbarrier, tma |
| [#6543](../sources/prs/flashinfer/PR-6543.md) | perf(cake_mok): optimizations, B200 MXFP8 imbalance split, opt-in GB300 EP8 split (SM100a, SM103a; stacked on #6439) | 2026-10-15 | double-buffering, pipeline-stages | block-scale, gemm, quantization |
| [#6544](../sources/prs/flashinfer/PR-6544.md) | [Feat] Support Muse-Spark-Open with fused normalization and TP/EP MoE optimizations | 2026-10-15 | kernel-fusion, pipeline-stages | fp4, gemm, mbarrier |
| [#6546](../sources/prs/flashinfer/PR-6546.md) | perf(moe): split the topK reduction in small-batch trtllm-gen MoE finalize | 2026-10-15 |  | block-scale, fp4, fp8 |
| [#6550](../sources/prs/flashinfer/PR-6550.md) | perf(cake_sparse_mla): FP8 prologue levers: h64 source-exact prologue overlap, low-head prefill index staging, h8/h16 setup order (SM100/SM103) | 2026-10-15 | pipeline-stages | clc, fp4, fp8 |
| [#6552](../sources/prs/flashinfer/PR-6552.md) | perf(cake_kimi_k3_fp8_projection): round 11 — static / grid-stride GEMM schedules, PDL-after-weights loader, 19 table adoptions (SM100a, SM103a) | 2026-10-15 | pipeline-stages, stream-k, tile-scheduling | block-scale, clc, fp8 |
| [#6555](../sources/prs/flashinfer/PR-6555.md) | perf(moe): retune the routingCustom split-topK dispatch rule | 2026-10-15 | kernel-fusion, pipeline-stages | moe, topk |
| [#6565](../sources/prs/flashinfer/PR-6565.md) | add-new-decoding-pipeline-for-blackwell-megamoe | 2026-10-15 | persistent-kernel, pipeline-stages, swizzling | block-scale, clc, fp4 |
| [#6566](../sources/prs/flashinfer/PR-6566.md) | perf(cake_all_gather_matmul): SM103a CTA-pair main kernel for two measured gate/up shapes (region table with column ranges) | 2026-10-15 | pipeline-stages | mbarrier, tcgen05, tma |
| [#6446](../sources/prs/flashinfer/PR-6446.md) | fix(cake_dsa_indexer): racecheck-clean verdict hand-off (single-lane verdict reads), regenerated scan programs (SM100a, SM103a) | 2026-10-14 | pipeline-stages | attention, mbarrier, scan |
| [#6447](../sources/prs/flashinfer/PR-6447.md) | perf(moe): optimize sparse SM107 MegaMoE decode | 2026-10-14 |  | block-scale, fp4, moe |
| [#6450](../sources/prs/flashinfer/PR-6450.md) | feat(cake_msa_icp_indexer): Cake MiniMax-M3 ICP indexer chain programs (fused Top-16 scorer + cross-rank exchange merge, TP2/TP4) for sm_100a and sm_103a | 2026-10-14 |  | fp4, fp8, nvfp4 |
| [#6452](../sources/prs/flashinfer/PR-6452.md) | fix(cake_fused_moe): ship every route layout and the odd weight-tile dense GEMM2 arm in the Kimi-K3 MXFP4 SiTU MoE export (cake, cake_cute) | 2026-10-14 |  | fp4, gemm, moe |
| [#6459](../sources/prs/flashinfer/PR-6459.md) | perf(cake_msa): Blackwell MSA Top-K streaming select 1.39-1.41x faster (bank-conflict-free candidate dump, one barrier per argmax round); small-grid stage-only plan rule (bit-identical selections) | 2026-10-14 | double-buffering | attention, fp4, fp8 |
| [#6463](../sources/prs/flashinfer/PR-6463.md) | perf(cake_msa): faster Blackwell MSA prefill programs — union-route selection census, Q-resident long-route order, two-stage folded-GQA rings, shared-TMEM QK/PV issue order, tile interleave, host-side cu_seqlens_k removal (rounds 4–9 levers) | 2026-10-14 | pipeline-stages | attention, fp4, fp8 |
| [#6471](../sources/prs/flashinfer/PR-6471.md) | perf(attention): Enable multi-token NVFP4 KV token/head grouping | 2026-10-14 |  | attention, flash-attention, fp4 |
| [#6474](../sources/prs/flashinfer/PR-6474.md) | perf(cake_diffusion): bitwise norm/AdaLN prologue rewrite for MiniMax-H3 FC1+SwiGLU and fused MLP (SM100/SM103) | 2026-10-14 |  | fp4, gemm, nvfp4 |
| [#6475](../sources/prs/flashinfer/PR-6475.md) | perf(cake_diffusion): MiniMax-H3 SM120 FC1+SwiGLU — FP8 mxf8f6f4 unit-scale form on GeForce, raster group 64, NVFP4 producer-warpgroup form | 2026-10-14 |  | fp4, fp8, gemm |
| [#6478](../sources/prs/flashinfer/PR-6478.md) | feat(cake_gdn): FP32-state initial prefill records for the Qwen3-Next / Qwen3.5 TP2/TP4/TP8 geometries and the re-delivered Cake CP-prefill programs (sm_100a, sm_103a) | 2026-10-14 | pipeline-stages | mbarrier, tcgen05, tma |
| [#6488](../sources/prs/flashinfer/PR-6488.md) | fix(moe): adapt localized execution to the updated PyTorch stream API | 2026-10-14 |  | block-scale, gemm, grouped-gemm |
| [#6501](../sources/prs/flashinfer/PR-6501.md) | perf(cake_all_gather_matmul): SM103a SM push route band and cta_group::2 pair main kernel for measured regions | 2026-10-14 | pipeline-stages | gemm, mbarrier, tcgen05 |
| [#6503](../sources/prs/flashinfer/PR-6503.md) | refactor-moe-engine-to-avoid-hardcoded-registry-table | 2026-10-14 | pipeline-stages | block-scale, fp4, moe |
| [#6504](../sources/prs/flashinfer/PR-6504.md) | Add SM120 Frost Moe Grouped Gemm Support for Swap-AB, MXFP8, NVFP4 and MXFP8×MXFP4 | 2026-10-14 | persistent-kernel, swizzling, tile-scheduling | block-scale, fp4, fp8 |
| [#6397](../sources/prs/flashinfer/PR-6397.md) | perf(cake_msa): faster Blackwell MSA decode programs (FP16 flat ring, per-arch uniform-FP8 stages, FP8-KV q1 prefetch) | 2026-10-13 | pipeline-stages, swizzling | attention, fp4, fp8 |
| [#6398](../sources/prs/flashinfer/PR-6398.md) | perf(moe_ep): fuse Rubin MegaMoE forward preparation | 2026-10-13 |  | fp4, nvfp4, quantization |
| [#6400](../sources/prs/flashinfer/PR-6400.md) | fix(topk): order the cached-count reset after the previous round's read in topk_clusters_exact | 2026-10-13 |  | topk |
| [#6410](../sources/prs/flashinfer/PR-6410.md) | perf(cake_msa): faster Blackwell MSA Top-K select programs (keq fold, 32-query instance, plan refit; bit-identical indices) | 2026-10-13 |  | attention, fp4, fp8 |
| [#6411](../sources/prs/flashinfer/PR-6411.md) | perf(cake_fused_moe): device-side GEMM2 path gate for the Kimi-K3 W4A8 MXFP4 SiTU mixed192 long-prefill chain (cake, cake_cute) | 2026-10-13 | pipeline-stages | attention, block-scale, flash-attention |
| [#6413](../sources/prs/flashinfer/PR-6413.md) | perf(cake_deepgemm): fused 32-head FP8 routes, next_n-4 paged text, static windows (SM100a, SM103a) | 2026-10-13 | pipeline-stages | fp4, fp8, gemm |
| [#6427](../sources/prs/flashinfer/PR-6427.md) | perf(cake_deepgemm_mega_gate): deterministic small-M route on a cta_group::2 split-1 template -- one exported template for M <= 16 deterministic calls (SM100a, SM103a) | 2026-10-13 | pipeline-stages | gemm, mbarrier, moe |
| [#6428](../sources/prs/flashinfer/PR-6428.md) | perf(cake_deepgemm_kgroup_gemm): n256 schedule tier for the FP32-accumulate l2 geometry on 152-SM devices, and a rotated tile order for its M = 5120 / N = 2304 / 3-group FP32-accumulate key on both devices (SM100a, SM103a) | 2026-10-13 | pipeline-stages, swizzling | block-scale, fp4, fp8 |
| [#6429](../sources/prs/flashinfer/PR-6429.md) | perf(cake_deepgemm_sparse_mqa): K-gated evict_first KV gather for the paged logits programs, a single-writer metadata fix, and programmatic dependent launch of the logits stage by default on the paged layouts (SM100a, SM103a) | 2026-10-13 | swizzling | block-scale, fp4, fp8 |
| [#6433](../sources/prs/flashinfer/PR-6433.md) | perf(cake_kimi_k3_fp8_projection): round 10 — cluster split-K pair GEMM, prefetched stream-K, 128×384 pair-tile GEMM, interleaved confirm protocol and dispatch-table re-tune (SM100a, SM103a) | 2026-10-13 | pipeline-stages, stream-k | block-scale, clc, fp8 |
| [#6439](../sources/prs/flashinfer/PR-6439.md) | perf(cake_mok): imbalance-aware comm split, earlier backward replay dispatch and an atomics-free load count (SM100a, SM103a, SM107a) | 2026-10-13 |  | moe, quantization, reduction |
| [#6440](../sources/prs/flashinfer/PR-6440.md) | perf(cake_all_gather_matmul): 128-wide main tile for small decode shards and a wide SM push for 8 MiB peer payloads (SM100a, SM103a) | 2026-10-13 | pipeline-stages | mbarrier, tcgen05, tma |
| [#6442](../sources/prs/flashinfer/PR-6442.md) | perf(cake_fused_moe): Kimi-K3 NVFP4 SiTU experts SM100 16384-token row with per-CTA privatized routing | 2026-10-13 |  | block-scale, fp4, moe |
| [#6443](../sources/prs/flashinfer/PR-6443.md) | fix(cake_msa): Blackwell MSA FP8 decode programs no longer hang (two-phase mbarrier lead); M16 decode programs drop four dependency-free sync sites (bitwise-identical outputs) | 2026-10-13 | pipeline-stages | attention, fp4, fp8 |
| [#6444](../sources/prs/flashinfer/PR-6444.md) | perf(cake_concat_mla_kv_quant_fp8): re-export the four Cake programs with bit-placement BF16 widening | 2026-10-13 |  | fp8, quantization |
| [#6336](../sources/prs/flashinfer/PR-6336.md) | perf: [PrimsTS] add BF16 N192 MoE kernel; batchM shuffled weight; fix TMA routing perf regression | 2026-10-12 |  | fp4, fp8, moe |
| [#6340](../sources/prs/flashinfer/PR-6340.md) | perf(cake_fused_moe): Kimi-K3 NVFP4 SiTU experts SM100 single-token row with the fused quantization + routing FC1 | 2026-10-12 | pipeline-stages | fp4, mbarrier, moe |
| [#6341](../sources/prs/flashinfer/PR-6341.md) | perf(cake_fused_moe): Kimi-K3 NVFP4 SiTU experts SM100 large rows with the 8-bit per-tile FC2 partial | 2026-10-12 |  | fp4, moe, nvfp4 |
| [#6343](../sources/prs/flashinfer/PR-6343.md) | [SM90] Add W4A8 MegaMoE support | 2026-10-12 | kernel-fusion, persistent-kernel, pipeline-stages | fp4, fp8, gemm |
| [#6346](../sources/prs/flashinfer/PR-6346.md) | feat(cake_mega_moe): [SM120] MXFP4 x MXFP8 MegaMoE through MoEEpLayer (sm120_mxfp4_mxfp8_bf16_cake) | 2026-10-12 | persistent-kernel, swizzling | fp4, fp8, gemm |
| [#6357](../sources/prs/flashinfer/PR-6357.md) | perf(cake_dsv4): overlap the next tile's V transform with PV in the NVFP4 sparse-MLA decode persistent member (SM100/SM103) | 2026-10-12 | double-buffering | attention, fp4, mbarrier |
| [#6374](../sources/prs/flashinfer/PR-6374.md) | feat(moe): support swiglu_limit in the SM107 CuTe DSL NVFP4 MoE | 2026-10-12 |  | block-scale, fp4, gemm |
| [#6375](../sources/prs/flashinfer/PR-6375.md) | perf(cake_minimax_h3_varlen_attention): round-13 per-plan program dispatch -- dynamic ticket scheduling for long multi-wave plans (SM100a, SM103a) and a publish-tail cut for the SM100a static plans | 2026-10-12 |  | attention, fp4, mbarrier |
| [#6387](../sources/prs/flashinfer/PR-6387.md) | feat(cake_msa): Cake NVFP4 MSA decode use_cache_hit union programs for sm_100a and sm_103a | 2026-10-12 | pipeline-stages | fp4, mbarrier, nvfp4 |
| [#6390](../sources/prs/flashinfer/PR-6390.md) | perf(cake_deepgemm): FP4 dense MQA single-launch scan routes run the in-kernel ScheduleMeta scan before the barrier/TMEM setup (re-export of the two fused-scan programs) | 2026-10-12 | pipeline-stages | fp4, fp8, mbarrier |
| [#6315](../sources/prs/flashinfer/PR-6315.md) | perf(cake_msa): regenerate the Blackwell MSA family after the CAKE-1183 re-baseline (SM100/SM103) | 2026-10-11 | pipeline-stages | attention, block-scale, fp4 |
| [#6318](../sources/prs/flashinfer/PR-6318.md) | perf(cake_deepgemm): per-architecture 64-head FP8 dense texts, static-preferred windows and two new paged geometries (SM100a, SM103a) | 2026-10-11 | pipeline-stages | fp4, fp8, gemm |
| [#6320](../sources/prs/flashinfer/PR-6320.md) | chore(cake_fused_moe): re-render the Kimi-K3 MXFP4 SiTU MoE export (cake, cake_cute) from the merged Cake main revision | 2026-10-11 |  | attention, flash-attention, fp4 |
| [#6323](../sources/prs/flashinfer/PR-6323.md) | perf(cake_gdn): SM107a FP64-free q-scale, fp32 T=1 tilev32 band, chunked-parallel prefill route and native packed-KDA tile64 variant | 2026-10-11 |  | moe |
| [#6324](../sources/prs/flashinfer/PR-6324.md) | feat(cake_quant_lora_gemm): fused NVFP4 / FP8 GEMM with a runtime BF16 LoRA correction (mm_nvfp4_lora, mm_fp8_lora) | 2026-10-11 | pipeline-stages, swizzling, tile-scheduling | block-scale, clc, fp4 |
| [#6325](../sources/prs/flashinfer/PR-6325.md) | perf(cake_deepgemm): single-launch 32-head FP8 / FP4 dense MQA logits routes, per-architecture 64-head programs and new paged next_n = 2 geometries; catalog schema v9 re-export | 2026-10-11 | pipeline-stages | fp4, fp8, mbarrier |
| [#6327](../sources/prs/flashinfer/PR-6327.md) | perf(cake_dsa_indexer): SM103a dispatch set for the wide, paired and split scan programs of the DSA indexer top-k (SM100a programs unchanged) | 2026-10-11 |  | mbarrier, tma, topk |
| [#6330](../sources/prs/flashinfer/PR-6330.md) | perf(cake_ssd_combined): exact-scan epilogue ring + calibrated schedule-variant rule (SM100 / SM103) | 2026-10-11 | double-buffering | mbarrier, scan, tcgen05 |
| [#6332](../sources/prs/flashinfer/PR-6332.md) | feat(cake_qkv_norm_rope_exchange_overlap): fused QKV projection + QK RMSNorm + RoPE overlapped with the Ulysses head exchange (SM90 / SM100 / SM103) | 2026-10-11 | pipeline-stages | attention, fp8, gemm |
| [#6335](../sources/prs/flashinfer/PR-6335.md) | perf(cake_kimi_k3_fp8_projection): round 9 — cluster split-K re-association cells, K=128 / 192-wide GEMM cells, fused-shape re-tune, quant_done barrier (SM100a, SM103a) | 2026-10-11 | pipeline-stages, stream-k | block-scale, fp8, gemm |
| [#6307](../sources/prs/flashinfer/PR-6307.md) | fix(moe): wait for Rubin finalize reductions before shared-buffer reuse | 2026-10-10 |  | block-scale, moe, reduction |
| [#6309](../sources/prs/flashinfer/PR-6309.md) | reduce-frost-host-overhead | 2026-10-10 | swizzling | fp4, gemm, moe |
| [#6314](../sources/prs/flashinfer/PR-6314.md) | perf(cake_diffusion): MiniMax-H3 full MLP FC2 BF16 epilogue with 4 warps, bit-identical re-export (SM100 / SM103) | 2026-10-10 |  | fp4, gemm, mbarrier |
| [#6274](../sources/prs/flashinfer/PR-6274.md) | Gdn/umma replayssm ucache flush | 2026-10-09 | swizzling | mbarrier, tcgen05, tma |
| [#6277](../sources/prs/flashinfer/PR-6277.md) | Add small-shape W4A16 MegaMoE tactics and model benchmarks | 2026-10-09 |  | attention, fp4, moe |
| [#6279](../sources/prs/flashinfer/PR-6279.md) | feat(moe): extend moe_utils to all supported arches and add more activation types for cuDNN grouped-GEMM MoE backends | 2026-10-09 |  | fp8, gemm, grouped-gemm |
| [#6286](../sources/prs/flashinfer/PR-6286.md) | feat(prims-ts): allow TMEM overlap for NVFP4 qkv overlap | 2026-10-09 |  | fp4, gemm, nvfp4 |
| [#6291](../sources/prs/flashinfer/PR-6291.md) | perf(cake_ssd_combined): round-4 exact-scan schedule, chunk-parallel host model and graph-capturable prepared submission (SM100 / SM103) | 2026-10-09 | pipeline-stages | mbarrier, scan, tcgen05 |
| [#6292](../sources/prs/flashinfer/PR-6292.md) | [BugFix #5139] Accept the TC-decode ultra FC2 tile in the SM12x W4A16 `force_tile_config` re-pin | 2026-10-09 |  | fp4, moe, nvfp4 |
| [#6217](../sources/prs/flashinfer/PR-6217.md) | perf(cake_kimi_k3_fp8_projection): round 8 — bit-exact dispatch-cell convergence, K=128 GEMM operand hand-off, cached launch receipts, short-row TMA-store fix (SM100a, SM103a) | 2026-10-08 | pipeline-stages, stream-k | block-scale, fp4, fp8 |
| [#6219](../sources/prs/flashinfer/PR-6219.md) | feat(cake_deepgemm): SM120 paged MQA-logits indexer: next_n 3, 5 and 6 programs for 32 and 64 heads | 2026-10-08 | pipeline-stages | attention, fp8, mbarrier |
| [#6220](../sources/prs/flashinfer/PR-6220.md) | perf(cake_sparse_mla): BF16 lever batch: online-softmax chunking, prologue rendezvous, split-KV reducer lane weights (SM100/SM103) | 2026-10-08 | pipeline-stages | fp4, mbarrier, mla |
| [#6226](../sources/prs/flashinfer/PR-6226.md) | feat(moe): add TRTLLM Gen SwiGLU StepFun support | 2026-10-08 | swizzling | fp4, fp8, gemm |
| [#6230](../sources/prs/flashinfer/PR-6230.md) | feat(cake_dsa_indexer): round 3 generated programs -- SM100 wide-kind register split (232 math / 40 I/O per lane, host-dispatched), bitwise identical to round 2 on SM100 / SM103 / SM107; lean export (shared headers, lever table in tests, cached device queries), SASS unchanged | 2026-10-08 | pipeline-stages | mbarrier, tcgen05, tma |
| [#6238](../sources/prs/flashinfer/PR-6238.md) | feat(cake_kernel_rubin): Cake backends on Rubin (sm_107a / CC 10.7) — routing, BGMV MoE, concat-MLA-K, GDN decode/prefill, packed KDA T=1 | 2026-10-08 | pipeline-stages | mla, moe, reduction |
| [#6242](../sources/prs/flashinfer/PR-6242.md) | feat(cake_mla): experimental Cake dense NVFP4 MLA decode for the NVFP4 paged latent cache (SM100a/SM103a, CUDA 13.4) | 2026-10-08 | pipeline-stages | attention, block-scale, fp4 |
| [#6243](../sources/prs/flashinfer/PR-6243.md) | feat(mega_moe): SM90 pull-style BF16 CuTeDSL mega kernel  | 2026-10-08 | kernel-fusion, persistent-kernel, pipeline-stages | block-scale, clc, fp4 |
| [#6248](../sources/prs/flashinfer/PR-6248.md) | perf(cake_fused_moe): Kimi-K3 NVFP4 SiTU experts SM103 large rows with an 8-bit per-tile FC2 partial | 2026-10-08 |  | fp4, moe, nvfp4 |
| [#6253](../sources/prs/flashinfer/PR-6253.md) | feat(cute): Cute mega moe un-finalized output support | 2026-10-08 |  | moe, reduction, topk |
| [#6254](../sources/prs/flashinfer/PR-6254.md) | fix(cake_all_gather_matmul): proxy fence after the readiness acquire | 2026-10-08 |  | tma |
| [#6258](../sources/prs/flashinfer/PR-6258.md) | perf(cake_minimax_h3_varlen_attention): round-6 SM100a single P barrier and tail-round Q-split planner (SM100a, SM103a) | 2026-10-08 | pipeline-stages | attention, block-scale, mbarrier |
| [#6262](../sources/prs/flashinfer/PR-6262.md) | perf(cake_dsv4): add the H64 tile member to the NVFP4 sparse-MLA decode family (SM100/SM103) | 2026-10-08 |  | attention, block-scale, fp4 |
| [#6267](../sources/prs/flashinfer/PR-6267.md) | perf(trtllm-gen decode): keep CGA reduction for small-batch long-KV decode; fuse v_scale in the decode wrapper | 2026-10-08 |  | attention, flash-attention, fp4 |
| [#6153](../sources/prs/flashinfer/PR-6153.md) | perf(cake_all_gather_matmul): overlap the gather with the GEMM — persistent arrival-ordered schedule, SM push for small shards, PDL chaining (SM100a, SM103a) | 2026-10-07 | persistent-kernel, pipeline-stages | attention, flash-attention, fp4 |
| [#6154](../sources/prs/flashinfer/PR-6154.md) | feat(cake_fused_moe): add the Kimi-K3 W4A8 MXFP4 SiTU TP8 long-prefill mixed192 chain (T >= 8192) to the Cake-exported backends (cake, cake_cute) | 2026-10-07 | pipeline-stages, swizzling | attention, block-scale, flash-attention |
| [#6163](../sources/prs/flashinfer/PR-6163.md) | feat(cake_concat_mla_kv_quant_fp8): generated Cake kernels for the fused MLA K/V pack + fp8 cast | 2026-10-07 | kernel-fusion | attention, flash-attention, fp4 |
| [#6167](../sources/prs/flashinfer/PR-6167.md) | [feat] Add warp level split k mxfp8 gemm | 2026-10-07 | pipeline-stages, swizzling, tile-scheduling | block-scale, fp8, gemm |
| [#6169](../sources/prs/flashinfer/PR-6169.md) | feat(cake_diffusion): MiniMax-H3 SM120 fused quantized full MLP, FC1 + SwiGLU + FC2 + gated residual (RTX 5090 / RTX PRO 6000) | 2026-10-07 | pipeline-stages | attention, block-scale, flash-attention |
| [#6176](../sources/prs/flashinfer/PR-6176.md) | feat(cake_diffusion): MiniMax-H3 full MLP block operator (BF16 / MXFP8 / NVFP4, SM100 / SM103) | 2026-10-07 | tile-scheduling | attention, block-scale, clc |
| [#6180](../sources/prs/flashinfer/PR-6180.md) | feat(cake_deepgemm): SM120 paged FP8 MQA lightning-indexer logits for RTX PRO 6000 / RTX 5090 (experimental generated-program export) | 2026-10-07 | pipeline-stages, swizzling | attention, flash-attention, fp4 |
| [#6190](../sources/prs/flashinfer/PR-6190.md) | refactor(cake_dsv4): fold the NVFP4 decode knob clones into kernel templates and share the binding host code (SM100/SM103) | 2026-10-07 | pipeline-stages | attention, block-scale, flash-attention |
| [#6193](../sources/prs/flashinfer/PR-6193.md) | perf(cake_sparse_mla): FP8 H128 prologue rendezvous + BF16 SWA128 two-chunk online softmax (SM100/SM103) | 2026-10-07 | pipeline-stages | attention, flash-attention, fp4 |
| [#6194](../sources/prs/flashinfer/PR-6194.md) | perf(cake_fused_moe): Kimi-K3 NVFP4 SiTU experts SM103 single-token fused quant+route FC1 | 2026-10-07 | kernel-fusion, pipeline-stages | attention, block-scale, flash-attention |
| [#6195](../sources/prs/flashinfer/PR-6195.md) | perf(cake_dsa_indexer): one lowering of the weighted ReLU sum in the DSA indexer top-k programs (SM100a, SM103a, SM107a) | 2026-10-07 |  | fp4, fp8, reduction |
| [#6196](../sources/prs/flashinfer/PR-6196.md) | perf(cake_diffusion): MiniMax-H3 SM120 quantized MLP, FP8 FC1 raster group 64 and NVFP4 FC1 producer warpgroup + staged y emission (RTX 5090 / RTX PRO 6000) | 2026-10-07 |  | attention, flash-attention, fp4 |
| [#6199](../sources/prs/flashinfer/PR-6199.md) | feat(cake_deepgemm): SM120 paged MQA-logits indexer: one Q atom per request for next_n 4, strided per-layer cache views | 2026-10-07 | pipeline-stages | attention, flash-attention, fp4 |
| [#6202](../sources/prs/flashinfer/PR-6202.md) | perf(cake_deepgemm_mega_mhc): two-lane Sinkhorn normalization chain on the 40- and 27-split mHC programs (SM100a, SM103a) | 2026-10-07 | persistent-kernel, pipeline-stages | fp8, gemv, mbarrier |
| [#6206](../sources/prs/flashinfer/PR-6206.md) | perf(cake_ssd_combined): preprocess, exact-scan and chunk-parallel prefill improvements (SM100 / SM103) | 2026-10-07 | double-buffering, persistent-kernel, pipeline-stages | attention, flash-attention, fp4 |
| [#6215](../sources/prs/flashinfer/PR-6215.md) | perf(cake_dsv4): dequantize the NVFP4 decode cache with the hardware QMUL4 via PTX ISA 9.4; require CUDA 13.4 (SM100/SM103) | 2026-10-07 | swizzling | attention, fp4, mla |
| [#6093](../sources/prs/flashinfer/PR-6093.md) | fix(msa): keep earlier blocks when the NVFP4 prefill replay rebases deeply | 2026-10-06 |  | attention, fp4, nvfp4 |
| [#6096](../sources/prs/flashinfer/PR-6096.md) | feat(cake_kimi_k3_fp8_projection): mid-M dispatch buckets, per-weight cached launcher, SM103 152-SM plan (round 7) | 2026-10-06 | pipeline-stages, stream-k | attention, block-scale, flash-attention |
| [#6097](../sources/prs/flashinfer/PR-6097.md) | perf(cake_deepgemm): folded weighted-sum epilogue for the 64-head FP8 MQA logits program; tiered sm_100a paged admission (SM100a, SM103a) | 2026-10-06 |  | attention, flash-attention, fp4 |
| [#6099](../sources/prs/flashinfer/PR-6099.md) | perf(cake_all_gather_matmul): one native host sequence per route (SM100a, SM103a) | 2026-10-06 |  | attention, flash-attention, fp4 |
| [#6100](../sources/prs/flashinfer/PR-6100.md) | feat(cake_ssd_combined): <128-token calls, seq_idx guard, grouped epilogue loads, any chunk_size via cu_seqlens (SM100 / SM103) | 2026-10-06 |  | attention, flash-attention, fp4 |
| [#6103](../sources/prs/flashinfer/PR-6103.md) | feat(cake_dsv4): NVFP4 DeepSeek-V4 sparse-MLA decode on SM100/SM103 (backend="cake") | 2026-10-06 |  | attention, block-scale, flash-attention |
| [#6105](../sources/prs/flashinfer/PR-6105.md) | perf(cake_sampling): round 10 -- CTA-local select twins, integer-tested whole-CTA tail, R200 one-wave re-pick (SM90, SM100a, SM103a, SM107a) | 2026-10-06 |  | attention, flash-attention, fp4 |
| [#6106](../sources/prs/flashinfer/PR-6106.md) | feat(mla): unify backend execution and add wrapper autotuning | 2026-10-06 |  | attention, fp8, mla |
| [#6107](../sources/prs/flashinfer/PR-6107.md) | perf(cake_nvfp4_mla_decode): faster than the FP8 CuTe-DSL MLA decode on every shipped shape (SM100a, SM103a) | 2026-10-06 | pipeline-stages | attention, flash-attention, fp4 |
| [#6108](../sources/prs/flashinfer/PR-6108.md) | perf(cake_kimi_k3_attn_res): qualify the native ports on 148- and 152-SM parts (SM100a, SM103a) | 2026-10-06 | pipeline-stages | attention, flash-attention, fp4 |
| [#6109](../sources/prs/flashinfer/PR-6109.md) | perf(cake_kimi_k3_latent_moe): plan from the device SM count; qualify 148- and 152-SM parts (SM100a, SM103a) | 2026-10-06 | stream-k | attention, flash-attention, fp4 |
| [#6111](../sources/prs/flashinfer/PR-6111.md) | perf(cake_fmha): uniform-gated per-item L2 stream hints for the balanced q1 decode kernels (SM100a, SM103a) | 2026-10-06 |  | attention, mbarrier |
| [#6118](../sources/prs/flashinfer/PR-6118.md) | perf(cake_deepgemm): dynamic chunk scheduler for the paged FP8 MQA logits; 64-head dense programs: early Q-stage release, short-KV one-split routes and a prologue prefetch; refreshed admission tables (SM100a, SM103a) | 2026-10-06 | pipeline-stages | attention, block-scale, flash-attention |
| [#6119](../sources/prs/flashinfer/PR-6119.md) | perf(cake_fmha): plan-free static one-wave program for the E4M3 head_dim-128 balanced DCP decode family (SM100a, SM103a) | 2026-10-06 |  | attention, fp8 |
| [#6126](../sources/prs/flashinfer/PR-6126.md) | fix(cake_kimi_k3_mla): bound the lazy E4M3 reference drop on the row-tile kernels (Inf/NaN rows with attention-sink keys); regenerate SM100 / SM103 | 2026-10-06 |  | attention, flash-attention, fp4 |
| [#6127](../sources/prs/flashinfer/PR-6127.md) | perf(cake_nvfp4_mla_decode): pin the decode kernel's launch bounds so its register budgets apply (SM100a 1.6-2 % faster) | 2026-10-06 |  | attention, flash-attention, fp4 |
| [#6129](../sources/prs/flashinfer/PR-6129.md) | perf(cake_deepgemm_mega_gate): 16-way split-K cluster reduction with a compensated token-parallel combine on the small-M routing-gate routes (SM100a, SM103a) | 2026-10-06 | pipeline-stages | attention, flash-attention, fp4 |
| [#6131](../sources/prs/flashinfer/PR-6131.md) | perf(cake_gdn): Qwen3.5 BF16-state T=1 decode bands and five prefill head splits (SM100a, SM103a) | 2026-10-06 | pipeline-stages | attention, flash-attention, fp4 |
| [#6133](../sources/prs/flashinfer/PR-6133.md) | perf(norm): SM107 launch config for add_rmsnorm_fp4quant | 2026-10-06 | swizzling | fp4, nvfp4, quantization |
| [#6135](../sources/prs/flashinfer/PR-6135.md) | refactor(cake_kimi_k3_situ): regenerate the SiTU MoE backend from its producer, drop dead bindings and sequences, fold per-arch copies | 2026-10-06 | pipeline-stages | attention, flash-attention, fp4 |
| [#6136](../sources/prs/flashinfer/PR-6136.md) | fix(gemm): use the SM107 CuTe-DSL kernel for mm_mxfp8(backend="cute-dsl") on Rubin | 2026-10-06 |  | block-scale, fp4, fp8 |
| [#6137](../sources/prs/flashinfer/PR-6137.md) | fix(prims-ts): compile batched GEMM under CuTe DSL 4.8 | 2026-10-06 |  | attention, fp4, gemm |
| [#6138](../sources/prs/flashinfer/PR-6138.md) | fix(msa): fence generic SMEM stores before tcgen05.mma in the pinned NVFP4 decode | 2026-10-06 |  | fp4, gemm, nvfp4 |
| [#6143](../sources/prs/flashinfer/PR-6143.md) | perf(cake_sampling): round 11 -- exact early termination of the leader radix passes, per-capability dispatch, hard floors (SM90, SM100a, SM103a, SM107a) | 2026-10-06 | pipeline-stages | attention, flash-attention, fp4 |
| [#6144](../sources/prs/flashinfer/PR-6144.md) | feat: uniform_q_len planner hint + specialized SM90 fp8-KV kernel for speculative-decoding target verify | 2026-10-06 | pipeline-stages, swizzling | attention, fp8, reduction |
| [#6146](../sources/prs/flashinfer/PR-6146.md) | perf(cake_fp8_projection): Kimi-K3 KDA/MLA projection GEMM round 7 (FP8 token ring on the M=256 cluster split-K cell, parallel-issue DSM partial exchange), shared-source export (SM100a, SM103a) | 2026-10-06 | pipeline-stages | attention, block-scale, flash-attention |
| [#6051](../sources/prs/flashinfer/PR-6051.md) | feat(cake_ssd_combined): one exact-scan family with FP16 delta, FP32 state, token-major out, any seqlen and varlen without initial states (SM100 / SM103) | 2026-10-05 | pipeline-stages, swizzling | attention, flash-attention, fp4 |
| [#6053](../sources/prs/flashinfer/PR-6053.md) | feat(cake_moe): BF16 and MXFP8 MoE training with recompute, clamped SwiGLU and variable sequence lengths on Blackwell and Rubin | 2026-10-05 | pipeline-stages | block-scale, gemm, mbarrier |
| [#6054](../sources/prs/flashinfer/PR-6054.md) | feat(cake_all_gather_matmul): accept the engine's [N,K] weight view, any local M and any N % 256 == 0 | 2026-10-05 | pipeline-stages | attention, flash-attention, fp4 |
| [#6055](../sources/prs/flashinfer/PR-6055.md) | feat(cake_minimax_h3): two-launch BF16 pre-attention stage consuming the engine-resident QKV weight (SM100a / SM103a) | 2026-10-05 |  | attention, flash-attention, fp4 |
| [#6056](../sources/prs/flashinfer/PR-6056.md) | feat(cake_dsa_indexer): round 2 generated programs -- host-dispatched scan pipeline levers and the staged / two-level prefix-popcount rank finalize with pools sized by max_seqlen_k, bulk-copy row I/O, a 16-slot thread form for top_k > 2048 and an SM107 persistent two-row form for top_k <= 2048, bitwise identical (SM100 / SM103 / SM107) | 2026-10-05 | pipeline-stages | attention, flash-attention, fp4 |
| [#6058](../sources/prs/flashinfer/PR-6058.md) | feat(cake_mega_moe): pre-reduced BF16 combine wire and fixed-cost levers for the SM90 MegaMoE backend | 2026-10-05 |  | attention, flash-attention, fp4 |
| [#6059](../sources/prs/flashinfer/PR-6059.md) | feat(cake_deepgemm): DeepSeek-V3.2 DSA indexer logits with the DeepGEMM signatures -- 64-head dense fp8_mqa_logits routes for any Q/K and paged FP8 fp8_paged_mqa_logits + metadata over the block table, admitted per arch (SM100a, SM103a) | 2026-10-05 | pipeline-stages | attention, flash-attention, fp4 |
| [#6060](../sources/prs/flashinfer/PR-6060.md) | perf(cake_nvfp4_attn): warp-specialised attention form for the MiniMax-H3 SM120 NVFP4 varlen attention, selected per call on RTX PRO 6000 | 2026-10-05 | warp-specialization | attention, flash-attention, fp4 |
| [#6061](../sources/prs/flashinfer/PR-6061.md) | fix(cake_fmha): cake fmha smallm hang and graph launch | 2026-10-05 |  | attention, flash-attention, mbarrier |
| [#6062](../sources/prs/flashinfer/PR-6062.md) | perf(cake_minimax_h3_varlen_attention): round-2/3 BF16 varlen attention schedule and segment plan cache (SM100a, SM103a) | 2026-10-05 | pipeline-stages | attention, block-scale, flash-attention |
| [#6065](../sources/prs/flashinfer/PR-6065.md) | perf(cake_sampling): round 9 -- leader-push exchange twins of the multi-CTA streams, graph-replay host fix | 2026-10-05 | pipeline-stages | attention, flash-attention, fp4 |
| [#6066](../sources/prs/flashinfer/PR-6066.md) | fix(cake_sparse_mla): trtllm-gen sparse-validity semantics, workspace contract and FP8 probability scale for the SM100/SM103 DSv4 sparse-MLA Cake programs | 2026-10-05 | pipeline-stages | attention, flash-attention, fp4 |
| [#6067](../sources/prs/flashinfer/PR-6067.md) | feat(cake_warp_decode): cover the sharded Qwen3.5-397B TP2/TP4 and MiniMax-M2 TP2/TP4 slices (SM100 / SM103) | 2026-10-05 | pipeline-stages | attention, flash-attention, fp4 |
| [#6068](../sources/prs/flashinfer/PR-6068.md) | perf(cake_nvfp4_attn): block-relative P codes and a selector upper bound for the MiniMax-H3 SM120 NVFP4 varlen attention | 2026-10-05 | warp-specialization | attention, block-scale, flash-attention |
| [#6070](../sources/prs/flashinfer/PR-6070.md) | feat(cake_kimi_k3_attn_res): serving-shape routing (M 1..16384) + snapshot-write variant for SM100 / SM103 | 2026-10-05 | pipeline-stages | attention, flash-attention, fp4 |
| [#6071](../sources/prs/flashinfer/PR-6071.md) | feat(cake_dsv4_sparse_mla): variant-indexed generated family for the SM120 DSv4.1 mixed-cache sparse-MLA decode | 2026-10-05 | swizzling | attention, flash-attention, fp4 |
| [#6029](../sources/prs/flashinfer/PR-6029.md) | feat(cake_mega_moe): add the FP4 1024- and 4096-token model routes (SM100 / SM103) | 2026-10-04 | pipeline-stages | attention, flash-attention, fp4 |
| [#6030](../sources/prs/flashinfer/PR-6030.md) | fix(cake_selective_state_update): threshold the softplus of dt in the MTP-short and checkpoint programs, register the family in the AOT build (SM100 / SM103) | 2026-10-04 |  | attention, flash-attention, fp4 |
| [#6033](../sources/prs/flashinfer/PR-6033.md) | feat(cake_dsv4): SM120 DeepSeek-V4 NVFP4 fused GPT-J RoPE + quantize + paged-insert writers | 2026-10-04 |  | attention, flash-attention, fp4 |
| [#6034](../sources/prs/flashinfer/PR-6034.md) | refactor(cake_mega_moe): fold mega_moe_v3 into one architecture-neutral program per schedule (SM100 / SM103) | 2026-10-04 | pipeline-stages | attention, flash-attention, fp4 |
| [#6035](../sources/prs/flashinfer/PR-6035.md) | Yanqinz/move frost out from experiment | 2026-10-04 | pipeline-stages, swizzling | fp4, nvfp4, quantization |
| [#6036](../sources/prs/flashinfer/PR-6036.md) | feat(cake_kimi_k3_attn_res): mid-M routing of the small-M Kimi-K3 AttnRes programs for SM100 / SM103 | 2026-10-04 |  | attention, flash-attention, fp4 |
| [#6039](../sources/prs/flashinfer/PR-6039.md) | feat(cake_minimax_h3): MiniMax-H3 stage operators take the diffusion engine's native operands (strided AdaLN tables, int64 indices, RoPE cache + positions, strided q/k/v views) on SM100/SM103 | 2026-10-04 |  | attention, flash-attention, fp4 |
| [#6040](../sources/prs/flashinfer/PR-6040.md) | feat(cake_selective_state_update): promote the headdim-64 / dstate-128 single-token decode row (Nemotron-H, granite-4.0-h) | 2026-10-04 | pipeline-stages | attention, flash-attention, fp4 |
| [#6043](../sources/prs/flashinfer/PR-6043.md) | refactor(cake_dcp): one program per split-KV variant, batch size as a kernel argument | 2026-10-04 | pipeline-stages | attention, flash-attention, fp4 |
| [#6044](../sources/prs/flashinfer/PR-6044.md) | feat(cake_gemm): masked grouped FP8 batch DeepGEMM MoE GEMM backend for SM100 / SM103 (backend="cake") | 2026-10-04 | pipeline-stages | attention, block-scale, flash-attention |
| [#6045](../sources/prs/flashinfer/PR-6045.md) | perf(cake_sparse_mla): rounds 7-17 DSv4 sparse-MLA Cake programs for SM100/SM103 on the #5920 layout (cumulative) | 2026-10-04 | pipeline-stages | attention, clc, flash-attention |
| [#6046](../sources/prs/flashinfer/PR-6046.md) | feat(cake_stepfun): Cake backend for the StepFun SwiGLU fused MoE, full path (SM100a, SM103a) | 2026-10-04 | persistent-kernel, pipeline-stages, swizzling | block-scale, clc, fp4 |
| [#6048](../sources/prs/flashinfer/PR-6048.md) | feat(cake_grouped_fp8_gemm): block-scaled UE8M0 family with native -1 padding and per-call operand rebinding (SM100a/SM103a) | 2026-10-04 | pipeline-stages | attention, block-scale, flash-attention |
| [#5993](../sources/prs/flashinfer/PR-5993.md) | refactor(cake_grouped_fp8_gemm): regenerate grouped FP8 GEMM and fused SiLU-quant kernels for SM100/SM103 | 2026-10-03 | pipeline-stages | attention, flash-attention, fp4 |
| [#5994](../sources/prs/flashinfer/PR-5994.md) | feat(cake_kimi_k3_attn_res): small-M Kimi-K3 AttnRes programs for SM100 / SM103 | 2026-10-03 |  | attention, flash-attention, fp4 |
| [#6000](../sources/prs/flashinfer/PR-6000.md) | perf(cake_dsv4_sparse_mla): split-count-guarded batched merge for 8-split SM120 decode calls and GB10 head-tile refinements | 2026-10-03 | tile-scheduling | attention, flash-attention, fp4 |
| [#6003](../sources/prs/flashinfer/PR-6003.md) | refactor(cake_selective_state_update): regenerate the checkpoint, MTP and FP32 STP programs as architecture-neutral sources, keep the shipped BF16 STP kernels (SM100 / SM103) | 2026-10-03 | pipeline-stages | attention, flash-attention, fp4 |
| [#6004](../sources/prs/flashinfer/PR-6004.md) | perf(cake_dsv4_sparse_mla): speed up the SM120 DeepSeek-V4 NVFP4 sparse-MLA prefill kernels with exact-equivalent schedule changes | 2026-10-03 | pipeline-stages | attention, flash-attention, fp4 |
| [#6007](../sources/prs/flashinfer/PR-6007.md) | perf(cake_dsa): per-target key-range-pass rule for the 64-head DSA sparse-attention training backward (SM100 / SM103 / SM107) and regenerated programs | 2026-10-03 | pipeline-stages | attention, flash-attention, fp4 |
| [#6008](../sources/prs/flashinfer/PR-6008.md) | perf(cake_fused_qk_rope_append): per-architecture / per-shape program selection for the fused BF16 QK RMSNorm + NeoX RoPE + paged KV append (SM90 / SM100 / SM103) | 2026-10-03 | kernel-fusion | attention, flash-attention, fp4 |
| [#6014](../sources/prs/flashinfer/PR-6014.md) | perf(prims-ts): tune the block-sparse/sage kernel for SM103 | 2026-10-03 | pipeline-stages | attention, fp8, quantization |
| [#6015](../sources/prs/flashinfer/PR-6015.md) | perf(cake_fused_moe): Kimi-K3 NVFP4 SiTU experts SM100 + SM103 claim8 FC2 2 CTAs/SM | 2026-10-03 | pipeline-stages | attention, block-scale, flash-attention |
| [#6016](../sources/prs/flashinfer/PR-6016.md) | perf(cake_bgmv_moe): round-5 BGMV MoE kernels: pair-grouped exact pipeline, programmatic dependent launch, per-arch selectors | 2026-10-03 | double-buffering, pipeline-stages | attention, flash-attention, fp4 |
| [#6017](../sources/prs/flashinfer/PR-6017.md) | refactor(cake_moe_grouped_gemm): re-export with deduplicated sources and thin launchers | 2026-10-03 |  | attention, flash-attention, fp4 |
| [#6019](../sources/prs/flashinfer/PR-6019.md) | perf(cake_dsa): direct accumulation into the caller's packed fp32 rows, key-range pass cap, in-kernel row lengths and fused index preparation for the native 64-head DSA sparse-attention kernels (#5657) | 2026-10-03 | pipeline-stages | attention, clc, flash-attention |
| [#6025](../sources/prs/flashinfer/PR-6025.md) | refactor(cake_gdn): regenerate SM100/SM103 context-parallel prefill kernels as architecture-neutral programs | 2026-10-03 | pipeline-stages | attention, flash-attention, fp4 |
| [#6026](../sources/prs/flashinfer/PR-6026.md) | refactor(cake_kda): regenerate fused KDA decode kernels as generic stride-taking programs | 2026-10-03 |  | attention, flash-attention, fp4 |
| [#6027](../sources/prs/flashinfer/PR-6027.md) | fix(cake_dsv4_sparse_mla): regenerate the SM120 decode kernels with the 32-bit E2M1 unpack for CUDA 12.9 ptxas | 2026-10-03 | pipeline-stages | attention, flash-attention, fp4 |
| [#5897](../sources/prs/flashinfer/PR-5897.md) | feat(cake_lm_head_loss): fuse the last chunk's dW scale + cast into its GEMM epilogue; per-geometry GEMM programs (#5680) | 2026-10-02 | pipeline-stages, tile-scheduling | attention, flash-attention, fp4 |
| [#5900](../sources/prs/flashinfer/PR-5900.md) | perf(prims-ts): qk-bf16/pv-fp8 and all-fp8 dense fmha context perf bringup | 2026-10-02 | swizzling | attention, flash-attention, fp8 |
| [#5901](../sources/prs/flashinfer/PR-5901.md) | refactor(cake kda decode): drop the seven never-selected instances and serve each family from one binding header | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5902](../sources/prs/flashinfer/PR-5902.md) | perf(kda): one-wave dispatch and single-pass RMSNorm for multi-token KDA decode on SM10x | 2026-10-02 |  | quantization, reduction |
| [#5905](../sources/prs/flashinfer/PR-5905.md) | refactor(cake_minimax_h3): MiniMax-H3 SM120 FP8/NVFP4 GEMMs, norm/quant kernels and FP8 packed-varlen attention: share the host helpers and norm/quant kernels, bound the caches | 2026-10-02 | swizzling | attention, flash-attention, fp4 |
| [#5906](../sources/prs/flashinfer/PR-5906.md) | refactor(cake_deepseek_fused_routing): DeepSeek-V3 fused MoE expert routing (scores + bias top-k) on SM100/SM103: fold 36 routing kernels into two templates and check contiguity | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5907](../sources/prs/flashinfer/PR-5907.md) | refactor(cake_sage): block-sparse Sage attention (FP8 on SM100/SM103, SM120 variants): share the SM120 launcher, merge the SM100/SM103 sources, drop the manifests | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5908](../sources/prs/flashinfer/PR-5908.md) | refactor(cake_warp_decode): fused-MoE warp-decode expert GEMM on SM100/SM103: compile from a per-target source list, share the identical SM100/SM103 kernels, add a GPU parity test | 2026-10-02 | pipeline-stages | attention, flash-attention, fp4 |
| [#5909](../sources/prs/flashinfer/PR-5909.md) | refactor(cake_kda): one TF32 prefill kernel source per schedule with a shared host shim and compact registry | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5910](../sources/prs/flashinfer/PR-5910.md) | refactor(cake tinygemm2_sm100): fold the six STAGES x PDL sections into one templated kernel | 2026-10-02 | pipeline-stages | attention, flash-attention, fp4 |
| [#5911](../sources/prs/flashinfer/PR-5911.md) | refactor(cake_megamoe_topk_reduce): MegaMoE top-k expert-output reduce (BF16, hidden 4096, top_k 6) on SM100/SM103: one generated source, only the helpers the kernel calls | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5912](../sources/prs/flashinfer/PR-5912.md) | refactor(cake_deepgemm_fp8_gemm): regenerate the FP8 1D1D GEMM as CUDA source with runtime shapes | 2026-10-02 | pipeline-stages | attention, block-scale, flash-attention |
| [#5913](../sources/prs/flashinfer/PR-5913.md) | perf(cake_fmha): round-5 E4M3 head_dim 128 balanced DCP programs and the hd64 / hd256 uniform-batch fast path on SM100/SM103 | 2026-10-02 | double-buffering, pipeline-stages | attention, flash-attention, fp4 |
| [#5914](../sources/prs/flashinfer/PR-5914.md) | feat(cake_dsv4): SM120 DeepSeek-V4 NVFP4 sparse-MLA decode backend for RTX PRO 6000 / RTX 5090 (#5690) | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5915](../sources/prs/flashinfer/PR-5915.md) | refactor(cake_router_gemm): DeepSeek-V3 MoE router GEMM (M 1..16, K 6144/7168) on SM100/SM103: standard JIT path, one binding, dense-view validation | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5916](../sources/prs/flashinfer/PR-5916.md) | feat(cake_kimi_k3_attn_res): regenerate the Kimi-K3 AttnRes programs after the schedule-selection round (SM100 / SM103) | 2026-10-02 | persistent-kernel, pipeline-stages | attention, flash-attention, fp4 |
| [#5917](../sources/prs/flashinfer/PR-5917.md) | refactor(cake_kda): drop import manifests and tools from the unbounded-softplus prefill kernels | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5918](../sources/prs/flashinfer/PR-5918.md) | refactor(cake_minimax_h3): MiniMax-H3 MXFP8 pre-attention (norm + quantize stages before attention) on SM100/SM103: one generated source per stage, one loader, thin launcher | 2026-10-02 |  | attention, block-scale, flash-attention |
| [#5919](../sources/prs/flashinfer/PR-5919.md) | refactor(cake kda): render the generated prefill selectors from Python and compact the module table | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5920](../sources/prs/flashinfer/PR-5920.md) | refactor(cake_dsv4_sparse_mla): DeepSeek-V4 sparse-MLA decode on SM100/SM103: one launcher-helper header, shared split-merge reducers, data-only loader, route rejections up front | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5922](../sources/prs/flashinfer/PR-5922.md) | refactor(cake_mxfp8_megamoe_ep16): one fused source behind a return-protocol flag, admit SM100 (SM100 / SM103) | 2026-10-02 | pipeline-stages | attention, flash-attention, fp4 |
| [#5923](../sources/prs/flashinfer/PR-5923.md) | refactor(cake_vsa_sm90): drop the planner-dead split stages, regenerate the Hopper VSA kernels with shared headers and thin launchers (SM90) | 2026-10-02 | persistent-kernel, pipeline-stages | attention, flash-attention, fp4 |
| [#5925](../sources/prs/flashinfer/PR-5925.md) | refactor(cake_deepgemm_kgroup_gemm): accept any group layout with one program per schedule and output mode | 2026-10-02 | swizzling, tile-scheduling | attention, flash-attention, fp4 |
| [#5929](../sources/prs/flashinfer/PR-5929.md) | refactor(cake_gqa_decode): sm110, one registry, thin launcher bindings, no per-call host sync | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5930](../sources/prs/flashinfer/PR-5930.md) | refactor(cake_alphamoe_nvfp4): drop dead kernels and exports, share the device helper library, set the smem opt-in once | 2026-10-02 |  | attention, block-scale, flash-attention |
| [#5931](../sources/prs/flashinfer/PR-5931.md) | refactor(cake_deepgemm_batched_gemm): one source per schedule, dispatch by schedule rule (SM100 / SM103) | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5933](../sources/prs/flashinfer/PR-5933.md) | refactor(cake_fmha): drop unreachable members and merge one-line per-arch copies | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5934](../sources/prs/flashinfer/PR-5934.md) | refactor(cake_fmha): remove unreachable request-ordered decode modules and benchmark-row routing | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5935](../sources/prs/flashinfer/PR-5935.md) | refactor(cake_deepgemm_fp4_gemm): one runtime-shape program per schedule, no per-arch copies or per-shape catalog (SM100 / SM103) | 2026-10-02 | pipeline-stages, swizzling | attention, block-scale, flash-attention |
| [#5938](../sources/prs/flashinfer/PR-5938.md) | refactor(cake_minimax_h3): MiniMax-H3 NVFP4 pre-attention and QKV quantize-and-pack kernels on SM100/SM103: one generated source per program | 2026-10-02 |  | attention, block-scale, flash-attention |
| [#5939](../sources/prs/flashinfer/PR-5939.md) | refactor(cake_gdn): collapse constant-clone kernels; merge SM100/SM103 copies | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5940](../sources/prs/flashinfer/PR-5940.md) | refactor(cake_kimi_k3_tp12_tail): one source per program, K23 keyed by capacity, runtime rank for the one-shot K1 | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5941](../sources/prs/flashinfer/PR-5941.md) | refactor(cake_deepgemm_mixed_gemm): one runtime-shape kernel family instead of per-shape programs | 2026-10-02 | pipeline-stages | attention, block-scale, flash-attention |
| [#5942](../sources/prs/flashinfer/PR-5942.md) | perf(cake_fused_moe): pre-shuffled scale-factor route with a register-only writer kernel for the 8192- and 16384-token Kimi-K3 NVFP4 SiTU rows (SM100/SM103) | 2026-10-02 |  | attention, block-scale, flash-attention |
| [#5944](../sources/prs/flashinfer/PR-5944.md) | perf(cake_mm_fp4): stream-K stripe tail for the partial last wave of the per-token NVFP4 2-CTA GEMM (SM100) | 2026-10-02 | stream-k | attention, block-scale, flash-attention |
| [#5947](../sources/prs/flashinfer/PR-5947.md) | refactor(cake_deepgemm_sparse_mqa): one metadata program per layout with arch-neutral logits and a registry loader | 2026-10-02 | pipeline-stages, swizzling | attention, block-scale, flash-attention |
| [#5950](../sources/prs/flashinfer/PR-5950.md) | perf(cake_sampling): round 8 -- slab-tail twins of the sample builds, pushed-coarse-sums twin of the cluster-8 default build, Hopper whole-CTA tail policy | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5951](../sources/prs/flashinfer/PR-5951.md) | refactor(cake_grouped_mxfp8_quantize): use one dtype-templated kernel; cache target resolution | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5952](../sources/prs/flashinfer/PR-5952.md) | feat(cake_fused_qk_rope_append): fused BF16 QK RMSNorm + NeoX RoPE + paged KV append for SM90 / SM100 / SM103 | 2026-10-02 | kernel-fusion | attention, flash-attention, fp4 |
| [#5953](../sources/prs/flashinfer/PR-5953.md) | refactor(cake_ulysses): arch-neutral generated kernels, drop the 36 unused bindings and the examples-hosted test fixture | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5954](../sources/prs/flashinfer/PR-5954.md) | refactor(cake_balanced_gqa_decode): regenerate the export as arch-neutral programs | 2026-10-02 | pipeline-stages | attention, flash-attention, fp4 |
| [#5955](../sources/prs/flashinfer/PR-5955.md) | refactor(cake_deepgemm_mega_mhc): one generated source per program across SM100 and SM103 with a lean loader | 2026-10-02 | pipeline-stages | attention, flash-attention, fp4 |
| [#5956](../sources/prs/flashinfer/PR-5956.md) | feat(cake_fused_qk_rope_append): Cake backend for the fused QK RMSNorm, RoPE, FP8 quantize and paged KV append entry (SM90, SM100) | 2026-10-02 | pipeline-stages | attention, flash-attention, fp4 |
| [#5957](../sources/prs/flashinfer/PR-5957.md) | refactor(cake_dsa): GLM-5.2 64-head DSA sparse-attention training kernels (forward and backward) on SM100/SM103/SM107: six architecture-neutral programs with by-value TMA descriptors and a thin launcher host | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5958](../sources/prs/flashinfer/PR-5958.md) | feat(cake_mega_moe): SM90 native BF16 MegaMoE expert compute through MoEEpLayer (sm90_bf16_bf16_bf16_push_cake) | 2026-10-02 | pipeline-stages | attention, flash-attention, fp4 |
| [#5959](../sources/prs/flashinfer/PR-5959.md) | feat(cake_dsv4_sparse_mla): add SM120 DeepSeek-V4 NVFP4 sparse-MLA prefill backend for RTX PRO 6000 / RTX 5090 | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5960](../sources/prs/flashinfer/PR-5960.md) | refactor(cake_nvfp4_svdquant): one source set, shape-rule routing, by-value tensor maps (SM100 / SM103) | 2026-10-02 | persistent-kernel, pipeline-stages | attention, flash-attention, fp4 |
| [#5961](../sources/prs/flashinfer/PR-5961.md) | refactor(cake_deepgemm_mega_gate): take the token count at runtime with one program per schedule template | 2026-10-02 | pipeline-stages | attention, flash-attention, fp4 |
| [#5962](../sources/prs/flashinfer/PR-5962.md) | refactor(cake_kimi_k3_fused_router): regenerate as arch-neutral programs with shared headers | 2026-10-02 | persistent-kernel | attention, flash-attention, fp4 |
| [#5968](../sources/prs/flashinfer/PR-5968.md) | refactor(cake_mla): regenerate the Blackwell MLA decode programs as runtime-shape families | 2026-10-02 |  | attention, clc, flash-attention |
| [#5969](../sources/prs/flashinfer/PR-5969.md) | refactor(cake_minimax_h3): MiniMax-H3 packed-varlen BF16/NVFP4 self-attention (prefill and split-KV) on SM100/SM103: one Cake-generated source per program | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5970](../sources/prs/flashinfer/PR-5970.md) | feat(cake_backend): generated backend="cake" for nvfp4_sparse_mla_decode on SM100 / SM103 | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5971](../sources/prs/flashinfer/PR-5971.md) | refactor(cake_mm_fp4): regenerate the per-token NVFP4 programs as architecture-neutral sources (SM100 / SM103) | 2026-10-02 | pipeline-stages, stream-k, swizzling | attention, block-scale, flash-attention |
| [#5972](../sources/prs/flashinfer/PR-5972.md) | feat(cake_dsa_indexer): fused DSA indexer scoring + deterministic exact top-k for training (SM100/SM103/SM107) | 2026-10-02 | pipeline-stages | attention, flash-attention, fp4 |
| [#5974](../sources/prs/flashinfer/PR-5974.md) | refactor(kimi_k3_latent_moe): regenerate as arch-neutral programs with compile-line TP constants and a flat registry | 2026-10-02 | pipeline-stages, stream-k | attention, flash-attention, fp4 |
| [#5977](../sources/prs/flashinfer/PR-5977.md) | fix(moe): skip unrouted (-1) expert ids in the SM12x fp8/mxfp8_mxfp4 grouped MoE route | 2026-10-02 |  | fp8, moe, quantization |
| [#5983](../sources/prs/flashinfer/PR-5983.md) | feat(cake_dsv4_sparse_mla): SM120/SM121 DeepSeek-V4.1 mixed-cache sparse-MLA decode (528 B FP8 SWA + 288 B FP4 compressed, BF16 Q) | 2026-10-02 | pipeline-stages | attention, flash-attention, fp4 |
| [#5985](../sources/prs/flashinfer/PR-5985.md) | refactor(cake_sampling): top-k/top-p radix sampling from probabilities on SM90/SM100/SM103/SM12x: drop the dead whole-CTA-tail blocks and the undispatched stage-2/3 forms, lean loader and host dispatch | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5988](../sources/prs/flashinfer/PR-5988.md) | refactor(cake_deepgemm_dense_mqa): one program set with runtime shapes and KV-range routes (SM100 / SM103) | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5989](../sources/prs/flashinfer/PR-5989.md) | refactor(cake_bgmv_moe): BGMV (batched gather matrix-vector) MoE expand/shrink kernels on SM90/SM100/SM103: host and binding cleanup | 2026-10-02 |  | attention, flash-attention, fp4 |
| [#5990](../sources/prs/flashinfer/PR-5990.md) | refactor(cake_bf16_fp4_gemm): regenerate SM100/SM103 BF16 x FP4 GEMM kernels from one generator | 2026-10-02 | pipeline-stages | attention, flash-attention, fp4 |
| [#5783](../sources/prs/flashinfer/PR-5783.md) | feat(cake_fused_moe): add the Kimi-K3 W4A8 MXFP4 SiTU routed MoE as Cake-exported backends (cake, cake_cute) | 2026-10-01 | pipeline-stages | attention, block-scale, flash-attention |
| [#5809](../sources/prs/flashinfer/PR-5809.md) | feat(cake_bgmv_moe): fall back to the portable BGMV MoE path for unsupported inputs and launch the portable kernels on the current stream | 2026-10-01 | pipeline-stages | attention, flash-attention, fp4 |
| [#5846](../sources/prs/flashinfer/PR-5846.md) | perf(cake_kda): read packed-row strided q/k/v in place in every prefill body | 2026-10-01 |  | attention, flash-attention, fp4 |
| [#5847](../sources/prs/flashinfer/PR-5847.md) | perf(cake_sampling): round 7 -- speculative-sample stage-1 twin, whole-CTA tail for cluster-8 streams, capability-keyed host policy | 2026-10-01 | pipeline-stages | attention, flash-attention, fp4 |
| [#5850](../sources/prs/flashinfer/PR-5850.md) | feat(cake_bgmv_moe): generic-shape Cake BGMV MoE bundles (hidden % 8 == 0, rank 8/16/32/64) and a token->pair route index for arbitrary pair order | 2026-10-01 |  | attention, flash-attention, fp4 |
| [#5851](../sources/prs/flashinfer/PR-5851.md) | perf(cake_kimi_k3_latent_moe): round 11 -- programs regenerated by the current generator (no kernel change; unused device helpers dropped), SM100a/SM103a | 2026-10-01 | stream-k | attention, flash-attention, fp4 |
| [#5853](../sources/prs/flashinfer/PR-5853.md) | feat(cake_kimi_k3_attn_res): add Kimi-K3 AttnRes backend for SM100/SM103 | 2026-10-01 | persistent-kernel, pipeline-stages | attention, flash-attention, fp4 |
| [#5855](../sources/prs/flashinfer/PR-5855.md) | perf(cake_fmha): round-4 balanced DCP E4M3 bodies and deterministic packed-MTP fold on SM100/SM103 | 2026-10-01 |  | attention, flash-attention, fp4 |
| [#5863](../sources/prs/flashinfer/PR-5863.md) | Canonical-layout NVFP4 W4A4 MoE in CuTe DSL on SM12x | 2026-10-01 | pipeline-stages, swizzling | block-scale, fp4, gemm |
| [#5865](../sources/prs/flashinfer/PR-5865.md) | perf(cake_dsa): single-pass key ranges for packed multi-segment rows, GB200-trace bench rows and fused varlen index glue for the native 64-head DSA sparse-attention kernels (#5657) | 2026-10-01 | pipeline-stages | attention, flash-attention, fp4 |
| [#5866](../sources/prs/flashinfer/PR-5866.md) | refactor(cake_nvfp4_attention): regenerate without dead code and accept strided inputs | 2026-10-01 |  | attention, block-scale, flash-attention |
| [#5867](../sources/prs/flashinfer/PR-5867.md) | refactor(cake_nvfp4_mla_decode): share kernel sources across SM100 and SM103 | 2026-10-01 |  | attention, flash-attention, fp4 |
| [#5868](../sources/prs/flashinfer/PR-5868.md) | refactor(cake_mla_varq_dcp_decode): regenerate as one source per schedule | 2026-10-01 | pipeline-stages | attention, flash-attention, fp4 |
| [#5869](../sources/prs/flashinfer/PR-5869.md) | perf(cake_mm_fp4): half-M pair tile for the narrow-N 2-CTA rows of the per-token NVFP4 route (sm_100a, sm_103a) | 2026-10-01 |  | attention, block-scale, clc |
| [#5871](../sources/prs/flashinfer/PR-5871.md) | refactor(cake_mla): for kimi_k3, share kernel sources across SM100 and SM103 | 2026-10-01 |  | attention, flash-attention, fp4 |
| [#5872](../sources/prs/flashinfer/PR-5872.md) | refactor(cake_xqa): regenerate Thor (sm110) XQA as one templated source per program | 2026-10-01 | pipeline-stages | attention, flash-attention, fp4 |
| [#5874](../sources/prs/flashinfer/PR-5874.md) | refactor(cake_fused_norm_combine): regenerate as one source per variant | 2026-10-01 | persistent-kernel, pipeline-stages | attention, flash-attention, fp4 |
| [#5875](../sources/prs/flashinfer/PR-5875.md) | refactor(cake_msa_nvfp4_decode): regenerate as one source per program | 2026-10-01 | persistent-kernel, pipeline-stages | attention, flash-attention, fp4 |
| [#5881](../sources/prs/flashinfer/PR-5881.md) | refactor(cake_all_gather_matmul): share kernel sources across SM100 and SM103 | 2026-10-01 | pipeline-stages | attention, flash-attention, fp4 |
| [#5884](../sources/prs/flashinfer/PR-5884.md) | refactor(cake_kimi_k3_vision_tower): regenerate as one source per program | 2026-10-01 | pipeline-stages, stream-k | attention, flash-attention, fp4 |
| [#5887](../sources/prs/flashinfer/PR-5887.md) | perf(cake_fmha): round-5 balanced DCP speculative-decode bodies (BF16, E4M3 head_dim 256) on SM100/SM103 | 2026-10-01 |  | attention, flash-attention, fp4 |
| [#5888](../sources/prs/flashinfer/PR-5888.md) | refactor(cake_fp8_projection): for kimi_k3, share kernel sources across SM100 and SM103 | 2026-10-01 | pipeline-stages | attention, block-scale, flash-attention |
| [#5891](../sources/prs/flashinfer/PR-5891.md) | update-frost-kernel-and-name | 2026-10-01 |  | fp4, moe, nvfp4 |
| [#5893](../sources/prs/flashinfer/PR-5893.md) | refactor(cake_msa): regenerate the Blackwell MSA family as one source per program | 2026-10-01 | pipeline-stages, swizzling | attention, flash-attention, fp4 |
| [#5895](../sources/prs/flashinfer/PR-5895.md) | perf(cake_fused_moe): thread-block-cluster routing kernel for the 512- and 1024-token Kimi-K3 NVFP4 SiTU rows (SM100/SM103) | 2026-10-01 |  | attention, flash-attention, fp4 |
| [#5714](../sources/prs/flashinfer/PR-5714.md) | perf(cake_gemm): two-fragment TMEM drain and routing-aware route selection for the fused grouped FP8 gate_up + SwiGLU + quant program | 2026-09-30 | stream-k | attention, flash-attention, fp4 |
| [#5721](../sources/prs/flashinfer/PR-5721.md) | perf(cake_kimi_k3_latent_moe): round 9 -- release-scoped stream-K publication in both prefill GEMMs, symmetric two-way fix-up for the front's trailing-wave K halves (SM100a/SM103a) | 2026-09-30 | stream-k | attention, flash-attention, fp4 |
| [#5727](../sources/prs/flashinfer/PR-5727.md) | feat(cake_bgmv_moe): SM90/SM100/SM103 support and cake_bgmv_moe naming for the deterministic multi-LoRA BGMV MoE backend | 2026-09-30 | pipeline-stages | attention, flash-attention, fp4 |
| [#5731](../sources/prs/flashinfer/PR-5731.md) | feat(cake_sampling): round-6 radix sampling bundle: coarse-sample stage-1 twins, row-span filter arm and small-k dispatch re-fit | 2026-09-30 |  | attention, flash-attention, fp4 |
| [#5734](../sources/prs/flashinfer/PR-5734.md) | perf(cake_kimi_k3_latent_moe): round 10 -- final-item staged TMA store for the 256-wide prefill tail GEMM instances (SM100a/SM103a) | 2026-09-30 | stream-k | attention, flash-attention, fp4 |
| [#5735](../sources/prs/flashinfer/PR-5735.md) | Canonical-layout NVFP4 W4A16 MoE in CuTe DSL on SM12x | 2026-09-30 | kernel-fusion, persistent-kernel, swizzling | block-scale, fp4, gemm |
| [#5736](../sources/prs/flashinfer/PR-5736.md) | perf(cake_fused_moe): fused quant+router and epilogue-triggered FC1 programs for the Kimi-K3 NVFP4 SiTU small rows (SM100/SM103) | 2026-09-30 | pipeline-stages | attention, block-scale, flash-attention |
| [#5737](../sources/prs/flashinfer/PR-5737.md) | feat(cake_dsa): SM107 (Rubin) generated programs and strided / packed GLM-5.2 trainer layouts for the native 64-head DSA sparse-attention training kernels (#5675) | 2026-09-30 |  | attention, flash-attention, fp4 |
| [#5739](../sources/prs/flashinfer/PR-5739.md) | perf(cake_deepgemm): faster two-CTA prologue, early TMA load start and descriptor prefetch on the mixed FP8xFP4 and native FP4 GEMM routes (SM100a, SM103a) | 2026-09-30 | pipeline-stages | attention, flash-attention, fp4 |
| [#5741](../sources/prs/flashinfer/PR-5741.md) | feat(cake_rmsnorm_train): add fused BF16 RMSNorm training forward/backward (FP32 rstd, deterministic dw) for SM100/SM103/SM107 | 2026-09-30 | pipeline-stages | attention, flash-attention, fp4 |
| [#5744](../sources/prs/flashinfer/PR-5744.md) | perf(cake_mm_fp4): tactic rules and regenerated programs for the per-token NVFP4 route | 2026-09-30 | pipeline-stages | attention, block-scale, flash-attention |
| [#5745](../sources/prs/flashinfer/PR-5745.md) | fix(sampling): honor per-row seed and offset tensors | 2026-09-30 |  | topk |
| [#5746](../sources/prs/flashinfer/PR-5746.md) | perf(cake_vision_backend): round 6 — split-KV attention with exact fixed-order merge, wide unit table + prefetch, per-row cluster trim, half-N GEMM tail twins (sm_100a/sm_103a) | 2026-09-30 | pipeline-stages | attention, flash-attention, fp4 |
| [#5750](../sources/prs/flashinfer/PR-5750.md) | perf(cake_gqa): serve BF16/page-16 and E4M3/page-64 (head_dim 128/256) DCP speculative decode on SM100/SM103 with the on-device load-balanced programs | 2026-09-30 | pipeline-stages | attention, flash-attention, fp4 |
| [#5752](../sources/prs/flashinfer/PR-5752.md) | feat(cake_lm_head_loss): add chunked LM-head + fused loss training kernels for SM100/SM103 (#5680) | 2026-09-30 | pipeline-stages | attention, flash-attention, fp4 |
| [#5753](../sources/prs/flashinfer/PR-5753.md) | feat(cake_dense_projection_gemm): GLM-5.2 dense projection GEMMs (grad, batched MLA, FP32 router) for SM100/SM107 | 2026-09-30 | pipeline-stages | gemm, mbarrier, mla |
| [#5754](../sources/prs/flashinfer/PR-5754.md) | perf(cake_deepgemm): one bulk TMA store per 16-row slab on the FP32 K-grouped FP4 GEMM swapped route (SM100a, SM103a) | 2026-09-30 | swizzling | attention, flash-attention, fp4 |
| [#5755](../sources/prs/flashinfer/PR-5755.md) | perf(cake_fused_moe): pre-shuffled scale-factor copy for the 16384-token FC1 of the Kimi-K3 NVFP4 SiTU experts (SM100/SM103) | 2026-09-30 |  | attention, flash-attention, fp4 |
| [#5762](../sources/prs/flashinfer/PR-5762.md) | Sm120 cudnn frost moe bf16 | 2026-09-30 | persistent-kernel, pipeline-stages, swizzling | block-scale, clc, gemm |
| [#5766](../sources/prs/flashinfer/PR-5766.md) | perf(cake_deepgemm): per-group leader pre-ranking on the M = 1 routing-gate cluster split-K route (SM100a, SM103a) | 2026-09-30 |  | attention, flash-attention, fp4 |
| [#5767](../sources/prs/flashinfer/PR-5767.md) | feat(experimental): migrate b12x to experimental submodule | 2026-09-30 | double-buffering, pipeline-stages, swizzling | attention, block-scale, flash-attention |
| [#5665](../sources/prs/flashinfer/PR-5665.md) | feat(kda): kda-for-kda CAKE PTX impl | 2026-09-29 |  | attention, tma |
| [#5667](../sources/prs/flashinfer/PR-5667.md) | feat(concat_mla_kv_quant_fp8): specialized kernel as a second backend, auto routing by head count | 2026-09-29 | kernel-fusion | fp8, mla |
| [#5668](../sources/prs/flashinfer/PR-5668.md) | perf(cake_latent_moe): Kimi-K3 TP12 fused LatentMoE tail round 6: fused K23 up to eight tokens (capacity ladder), fp64-gated numerics | 2026-09-29 | kernel-fusion | attention, flash-attention, fp4 |
| [#5671](../sources/prs/flashinfer/PR-5671.md) | perf(cake_kimi_k3_latent_moe): round 8 -- single-wave aligned K halves for the front prefill trailing wave, evict_first front instance for T <= 512, coalesced stream-K partial slots (SM100a/SM103a) | 2026-09-29 | pipeline-stages, stream-k | attention, flash-attention, fp4 |
| [#5672](../sources/prs/flashinfer/PR-5672.md) | perf(cake_fp8_projection): Kimi-K3 KDA/MLA projection GEMM round 6 (L2 prefetch, weight multicast, TMA-store epilogue, cluster split-K, 192-wide / stream-K GEMM, PDL), shared-source export (SM100a, SM103a) | 2026-09-29 | pipeline-stages, stream-k | attention, flash-attention, fp4 |
| [#5674](../sources/prs/flashinfer/PR-5674.md) | perf(cake_xqa): per-GQA-ratio tmem kernels and the cta_group::2 pair routes for experimental SM110 XQA | 2026-09-29 |  | attention, flash-attention, fp4 |
| [#5681](../sources/prs/flashinfer/PR-5681.md) | revert(cake_fused_moe): remove the Kimi-K3 W4A8 MXFP4 SiTU changes to the CuTe DSL MoE path (#5430) | 2026-09-29 |  | attention, block-scale, flash-attention |
| [#5682](../sources/prs/flashinfer/PR-5682.md) | fix(cute_dsl): wait on grid dependencies before the finalize-fusion kernel reads routing outputs | 2026-09-29 | tile-scheduling | attention, block-scale, flash-attention |
| [#5684](../sources/prs/flashinfer/PR-5684.md) | perf(cake_sampling): round-5 kernels (software-pipelined sampled pass, ballot-gated filter, two-level cluster select, two-warp fused tail, ept-32 streams, per-architecture stage-2/3 forms) and chain-aware dispatch | 2026-09-29 | pipeline-stages | attention, flash-attention, fp4 |
| [#5686](../sources/prs/flashinfer/PR-5686.md) | perf(cake_sparse_mla): round-5 DSv4 sparse-MLA Cake programs for SM100/SM103 (exact numerics; stacked on #5644) | 2026-09-29 | pipeline-stages | attention, flash-attention, fp4 |
| [#5687](../sources/prs/flashinfer/PR-5687.md) | perf(cake_vsa_sm90): queue-scheduled persistent stage for long uniform plans | 2026-09-29 |  | attention, flash-attention, fp4 |
| [#5691](../sources/prs/flashinfer/PR-5691.md) | perf(cake_vision_backend): round 5 — PDL prologue overlap (PDL_EARLY) census windows, m_e8 / m_e8_cs tiles, fc1 stream-K twins (sm_100a/sm_103a) | 2026-09-29 | pipeline-stages, stream-k | attention, flash-attention, fp4 |
| [#5692](../sources/prs/flashinfer/PR-5692.md) | perf(cake_gemm): evict_first weight stream and descriptor prefetch for the fused grouped FP8 gate_up + SwiGLU + quant program | 2026-09-29 | stream-k | attention, flash-attention, fp4 |
| [#5696](../sources/prs/flashinfer/PR-5696.md) | feat(moe): fuse tanh-clamped squared relu in CUTLASS epilogues | 2026-09-29 | epilogue-fusion | block-scale, fp8, gemm |
| [#5697](../sources/prs/flashinfer/PR-5697.md) | feat(cake_mm_fp4): add per-token NVFP4 quantize + mm_fp4 per-token alpha backend for SM100 and SM103 | 2026-09-29 | pipeline-stages, tile-scheduling | attention, block-scale, clc |
| [#5700](../sources/prs/flashinfer/PR-5700.md) | perf(cake_sparse_mla): round-6 DSv4 sparse-MLA Cake programs for SM100/SM103 (exact numerics; stacked on #5686) | 2026-09-29 | pipeline-stages | attention, flash-attention, fp4 |
| [#5703](../sources/prs/flashinfer/PR-5703.md) | perf(mla): deepen FP8 and FP16/BF16 decode load pipelines on SM107 | 2026-09-29 | pipeline-stages | attention, fp8, mla |
| [#5704](../sources/prs/flashinfer/PR-5704.md) | feat(cake_dsa): add native 64-query-head DSA sparse-attention kernels for SM100/SM103 (#5657) | 2026-09-29 |  | attention, flash-attention, fp4 |
| [#5709](../sources/prs/flashinfer/PR-5709.md) | perf(mla): prefetch split partials in the CuTe DSL MLA decode reducer | 2026-09-29 | pipeline-stages | attention, fp8, mla |
| [#5623](../sources/prs/flashinfer/PR-5623.md) | perf(cake_vision_backend): round 3 — attention score ring, GEMM tile boundaries, TMA-out epilogue, pointer TMA ABI (sm_100a/sm_103a) | 2026-09-28 | pipeline-stages | attention, flash-attention, fp4 |
| [#5624](../sources/prs/flashinfer/PR-5624.md) | perf(cake_latent_moe): Kimi-K3 TP12 fused LatentMoE tail round 4: persistent K3 pipeline from 256 tokens, weight-streaming K2 for M <= 4 (GB200 / GB300 NVL72) | 2026-09-28 | pipeline-stages | attention, flash-attention, fp4 |
| [#5627](../sources/prs/flashinfer/PR-5627.md) | perf(cake_mla): kimi_k3, regenerate both architectures for the r54 kernel (redundant p_full barrier removed) | 2026-09-28 | pipeline-stages | attention, flash-attention, fp4 |
| [#5628](../sources/prs/flashinfer/PR-5628.md) | optimize-cudnn-frost-moe-decoding | 2026-09-28 | swizzling | fp4, moe, nvfp4 |
| [#5630](../sources/prs/flashinfer/PR-5630.md) | perf(cake_sparse_mla): round-3 DSv4 sparse-MLA programs for SM100/SM103 (persistent-item epilogue, index ring, retained-KV decode body, SwapsAb V alias, routing) | 2026-09-28 | pipeline-stages | attention, flash-attention, fp4 |
| [#5636](../sources/prs/flashinfer/PR-5636.md) | perf(cake_sampling): round-4 kernels (streaming candidate-list stage 1, fused small-k tail, host-decided PDL trigger) and k-aware dispatch | 2026-09-28 | pipeline-stages | attention, flash-attention, fp4 |
| [#5638](../sources/prs/flashinfer/PR-5638.md) | perf(cake_vsa_sm90): round-8 planner load model, odd-tile store guard and acquire-release split merge on the CuTe route | 2026-09-28 |  | attention, flash-attention, fp4 |
| [#5641](../sources/prs/flashinfer/PR-5641.md) | perf(cake_kda): round 5 — grouped TMEM loads with the state decay off the ready chain, strided q/k/v read in place, ping-pong prefix chain | 2026-09-28 | pipeline-stages | attention, flash-attention, fp4 |
| [#5642](../sources/prs/flashinfer/PR-5642.md) | perf(cake_fp8_projection): Kimi-K3 KDA/MLA projection GEMM (per-token FP8 activations x per-block FP8 weights, SM100/SM103) round 5: cluster split-K decode routes and staged register GEMM epilogue | 2026-09-28 | pipeline-stages, swizzling | attention, block-scale, flash-attention |
| [#5643](../sources/prs/flashinfer/PR-5643.md) | perf(cake_vision_backend): round 4 — stream-K tail for the N=1024 projector GEMMs, per-arch attention split cost model (sm_100a/sm_103a) | 2026-09-28 | pipeline-stages, stream-k | attention, flash-attention, fp4 |
| [#5644](../sources/prs/flashinfer/PR-5644.md) | perf(cake_sparse_mla): round-4 DSv4 sparse-MLA Cake programs for SM100/SM103 (stacked on #5630) | 2026-09-28 | pipeline-stages | attention, flash-attention, fp4 |
| [#5645](../sources/prs/flashinfer/PR-5645.md) | feat(cake_gemm): paired BF16 conversions and a mixed-schedule route for the fused grouped FP8 gate_up + SwiGLU + quant program (SM100a) | 2026-09-28 | stream-k | attention, flash-attention, fp4 |
| [#5646](../sources/prs/flashinfer/PR-5646.md) | perf(cake_latent_moe): Kimi-K3 TP12 fused LatentMoE tail round 5: early shared scatter K1, fused K2+K3 for M <= 4, bulk reduce-scatter K3 pipeline above 256 tokens (GB200 / GB300 NVL72) | 2026-09-28 | double-buffering, pipeline-stages | attention, flash-attention, fp4 |
| [#5647](../sources/prs/flashinfer/PR-5647.md) | perf(cake_kimi_k3_latent_moe): packed global-y norm, landing-zone alias, deferred cluster wait and a 128-wide TP8 tail tile (SM100a/SM103a), regenerated programs | 2026-09-28 | pipeline-stages | attention, flash-attention, fp4 |
| [#5648](../sources/prs/flashinfer/PR-5648.md) | Add native W4A16 prefetch and grouped-tile tactics on SM121 | 2026-09-28 |  | fp4, gemm, moe |
| [#5658](../sources/prs/flashinfer/PR-5658.md) | perf(cake_xqa): add the tcgen05/TMEM cluster-multicast D512 tree routes to experimental SM110 XQA | 2026-09-28 |  | attention, flash-attention, fp4 |
| [#5659](../sources/prs/flashinfer/PR-5659.md) | fix(cake_kda): repack the BF16 inverse fragment before block composition in the native prefill facade bodies | 2026-09-28 |  | attention, flash-attention, fp4 |
| [#5660](../sources/prs/flashinfer/PR-5660.md) | feat(cake_nvfp4_attn): opt-in uncompensated (nodelta) NVFP4 varlen attention variant for MiniMax-H3 SM120 | 2026-09-28 |  | attention, flash-attention, fp4 |
| [#5582](../sources/prs/flashinfer/PR-5582.md) | perf(cake_vsa_sm90): cluster-merge small route for uniform sliced selections | 2026-09-27 | persistent-kernel | attention, flash-attention, fp4 |
| [#5583](../sources/prs/flashinfer/PR-5583.md) | perf(cake_nvfp4_attn): MiniMax-H3 SM120 ragged NVFP4 attention (SageAttention3 recipe): block-max-first softmax, 4 partial row sums | 2026-09-27 |  | attention, flash-attention, fp4 |
| [#5584](../sources/prs/flashinfer/PR-5584.md) | perf(cake_kimi_k3_latent_moe): fused-norm single-launch prefill tail for single-wave rows + 6-deep ring instance for the TP1 tail at T <= 256 (SM100a/SM103a), regenerated programs | 2026-09-27 | pipeline-stages, stream-k | attention, clc, flash-attention |
| [#5586](../sources/prs/flashinfer/PR-5586.md) | perf(cake_vsa_sm90): two-warpgroup small kernels, deferred cluster rendezvous, persistent first-tile header | 2026-09-27 | persistent-kernel | attention, flash-attention, fp4 |
| [#5590](../sources/prs/flashinfer/PR-5590.md) | perf(cake_fp8_projection): Kimi-K3 KDA/MLA projection GEMM (per-token FP8 activations x per-block FP8 weights, SM100/SM103) round 2: TMA-store epilogue and fused-quant decode route for large-M single-N-tile layers | 2026-09-27 | pipeline-stages, swizzling | attention, block-scale, flash-attention |
| [#5591](../sources/prs/flashinfer/PR-5591.md) | fix(cake_sparse_mla): harden the DSv4 sparse-MLA Cake backend for #4671 (padded Q, separate SWA/compressed tables, caller-owned workspace, length offsets) and regenerate the SM100/SM103 programs | 2026-09-27 | pipeline-stages | attention, flash-attention, fp4 |
| [#5592](../sources/prs/flashinfer/PR-5592.md) | feat(cake_gemm): odd-tail kernel, routing-aware route rule and wide activation kernel for the fused grouped FP8 gate_up + SwiGLU + quant program (SM100a) | 2026-09-27 | kernel-fusion, swizzling | attention, flash-attention, fp4 |
| [#5593](../sources/prs/flashinfer/PR-5593.md) | perf(cake_warp_decode): evict-first weight streams for the sm_103a Qwen3-30B-A3B fused route-pack rows (num_tokens 8-32) | 2026-09-27 | pipeline-stages | attention, flash-attention, fp4 |
| [#5594](../sources/prs/flashinfer/PR-5594.md) | feat(cake_msa): nvfp4_decode, compute capability 10.7 programs under a three-architecture export lock | 2026-09-27 | pipeline-stages | attention, flash-attention, fp4 |
| [#5595](../sources/prs/flashinfer/PR-5595.md) | perf(cake_nvfp4_attn): MiniMax-H3 SM120 NVFP4 varlen attention: fused statistics + quantization pre-processing for mid-size plans | 2026-09-27 | kernel-fusion | attention, block-scale, flash-attention |
| [#5596](../sources/prs/flashinfer/PR-5596.md) | feat(cake_vsa_sm90): CuTe DSL build of the Hopper VSA kernels (backend="cake_cute") | 2026-09-27 | persistent-kernel, pipeline-stages | attention, flash-attention, fp4 |
| [#5597](../sources/prs/flashinfer/PR-5597.md) | perf(cake_xqa): add the split-KV register-MMA FP16 page128 route to experimental SM110 XQA | 2026-09-27 |  | attention, flash-attention, fp4 |
| [#5598](../sources/prs/flashinfer/PR-5598.md) | perf(cake_kda): shorter unbounded prepare chain for the BF16 prefill programs (sm_100a, sm_103a), correction buffer only on the chain route | 2026-09-27 | pipeline-stages, swizzling | attention, flash-attention, fp4 |
| [#5602](../sources/prs/flashinfer/PR-5602.md) | perf(cake_mla): kimi_k3 shape, regenerate both architectures for the r52 kernel (deferred O rescale, wider long-request threshold) | 2026-09-27 |  | attention, flash-attention, fp4 |
| [#5603](../sources/prs/flashinfer/PR-5603.md) | feat(cake_latent_moe): Kimi-K3 TP12 fused LatentMoE tail for GB200 / GB300 NVL72, kimi_k3_tp12_tail) | 2026-09-27 |  | attention, flash-attention, fp4 |
| [#5604](../sources/prs/flashinfer/PR-5604.md) | perf(cake_fp8_projection): Kimi-K3 KDA/MLA projection GEMM (per-token FP8 activations x per-block FP8 weights, SM100/SM103) round 3: narrow quantization units and a decoupled BF16 token ring in the fused-quant decode kernel | 2026-09-27 | pipeline-stages | attention, block-scale, flash-attention |
| [#5607](../sources/prs/flashinfer/PR-5607.md) | perf(cake_sampling): round-3 kernels (candidate-list stage 1, composite bitonic stage 2/3) and re-fitted dispatch | 2026-09-27 | pipeline-stages | attention, flash-attention, fp4 |
| [#5609](../sources/prs/flashinfer/PR-5609.md) | perf(cake_mm_fp4): faster NVFP4 per-token path (register-resident per-token quantize, per-tile alpha epilogue, low-M split-K, L2 eviction policies) | 2026-09-27 | persistent-kernel, pipeline-stages | attention, block-scale, flash-attention |
| [#5610](../sources/prs/flashinfer/PR-5610.md) | perf(cake_sparse_mla): warp-uniform FP8/H128 TMA gathers and 32-byte epilogue stores in the DSv4 sparse-MLA Cake programs (SM100/SM103) | 2026-09-27 | pipeline-stages | attention, flash-attention, fp4 |
| [#5612](../sources/prs/flashinfer/PR-5612.md) | feat(kda): kda for kda cutedsl impl | 2026-09-27 | pipeline-stages | attention, sort, tma |
| [#5621](../sources/prs/flashinfer/PR-5621.md) | perf(cake_kimi_k3_fused_router): Kimi-K3 router register-prefetch L arm on the 32-128-token shapes it wins, per-architecture route tables, regenerated programs | 2026-09-27 |  | attention, flash-attention, fp4 |
| [#5622](../sources/prs/flashinfer/PR-5622.md) | perf(cake_kda): scan-owned state epilogue on the apply route, apply-route descriptor re-encode after a plan-cache rebind (round 4, sm_100a, sm_103a) | 2026-09-27 |  | attention, flash-attention, fp4 |
| [#5562](../sources/prs/flashinfer/PR-5562.md) | perf(cake_diffusion): MiniMax-H3 out-proj NVFP4 quantization pass 14x2 loads in flight, raster group 8, 64-column TMEM drain (SM100/SM103) | 2026-09-26 | pipeline-stages | attention, flash-attention, fp4 |
| [#5563](../sources/prs/flashinfer/PR-5563.md) | perf(cake_kernel): unified 16-warp epilogue role for the epilogue-fused NVFP4 QKV GEMM on SM103a (MiniMax-H3 pre-attention) | 2026-09-26 |  | attention, flash-attention, fp4 |
| [#5564](../sources/prs/flashinfer/PR-5564.md) | perf(cake_backend): warp-per-row selection arm for the largest Kimi-K3 fused router batches (SM100/SM103) | 2026-09-26 |  | attention, flash-attention, fp4 |
| [#5565](../sources/prs/flashinfer/PR-5565.md) | perf(cake_kda): faster fused M128 BF16 prefill body (checkpoint rows off the chain, packed gate scan), page64 phase fix | 2026-09-26 | pipeline-stages | attention, flash-attention, fp4 |
| [#5566](../sources/prs/flashinfer/PR-5566.md) | chore(cake_kernel): regenerate the epilogue-fused NVFP4 QKV GEMM export for MiniMax-H3 pre-attention (SM100a/SM103a) | 2026-09-26 |  | attention, flash-attention, fp4 |
| [#5567](../sources/prs/flashinfer/PR-5567.md) | feat(cake_gemm): fused grouped FP8 gate_up GEMM + SwiGLU + FP8 quantization for SM100a | 2026-09-26 | kernel-fusion | attention, flash-attention, fp4 |
| [#5568](../sources/prs/flashinfer/PR-5568.md) | perf(cake_backend): split cooperative joins and a warp-level round-0 shortcut for the mid and large Kimi-K3 fused router batches (SM100/SM103) | 2026-09-26 |  | attention, flash-attention, fp4 |
| [#5569](../sources/prs/flashinfer/PR-5569.md) | feat(cake_vsa_sm90): SM90 BF16 variable block-sparse attention backend for VariableBlockSparseAttentionWrapper | 2026-09-26 | persistent-kernel, pipeline-stages | attention, flash-attention, fp4 |
| [#5570](../sources/prs/flashinfer/PR-5570.md) | perf(cake_vision_backend): Kimi-K3 vision tower Cake backend round 2 (SM100a/SM103a): packed epilogues, f16x2 RoPE table, PDL | 2026-09-26 | pipeline-stages | attention, flash-attention, fp4 |
| [#5571](../sources/prs/flashinfer/PR-5571.md) | perf(cake_minimax_h3): fp8-PV split-program schedule fix and sm_103a split-cost recalibration (SM100/SM103) | 2026-09-26 |  | attention, flash-attention, fp4 |
| [#5572](../sources/prs/flashinfer/PR-5572.md) | feat(cake_backend): Kimi-K3 FP8_PB_WO KDA/MLA projection GEMMs (SM100/SM103) | 2026-09-26 | pipeline-stages, swizzling | attention, block-scale, flash-attention |
| [#5573](../sources/prs/flashinfer/PR-5573.md) | perf(cake_kda): fused apply route for the unbounded affine BF16 prefill composite (operator export, pair-map prefix, fused apply kernel), H12 beta export fix | 2026-09-26 | pipeline-stages | attention, flash-attention, fp4 |
| [#5574](../sources/prs/flashinfer/PR-5574.md) | perf(cake_warp_decode): route the SM103 Qwen3-30B-A3B num_tokens=8 warp-decode row onto the fused route-pack K256 path | 2026-09-26 | pipeline-stages | attention, flash-attention, fp4 |
| [#5575](../sources/prs/flashinfer/PR-5575.md) | feat(cake_backend): Kimi-K3 Stable LatentMoE front/tail projections (SM100a/SM103a) with generated programs | 2026-09-26 | pipeline-stages, stream-k | attention, flash-attention, fp4 |
| [#5577](../sources/prs/flashinfer/PR-5577.md) | feat(cake_mla_varq_dcp_decode): Cake MLA variable-query decode with DCP for SM100 / SM103 | 2026-09-26 |  | attention, flash-attention, fp4 |
| [#5581](../sources/prs/flashinfer/PR-5581.md) | perf(cake_vsa_sm90): split-KV small-selection route for sub-occupancy grids | 2026-09-26 | persistent-kernel, pipeline-stages | attention, flash-attention, fp4 |
| [#5539](../sources/prs/flashinfer/PR-5539.md) | feat(cake_minimax_h3): SM120 FP8 packed-varlen attention for MiniMax-H3 (RTX 5090 / RTX PRO 6000) | 2026-09-25 |  | attention, flash-attention, fp4 |
| [#5540](../sources/prs/flashinfer/PR-5540.md) | feat(cake_fused_norm_combine): add SM103 (B300) eight-peer fused norm-combine beside SM100 and a pipelined persistent owner reduce for 1024+ tokens | 2026-09-25 | kernel-fusion, pipeline-stages | attention, flash-attention, fp4 |
| [#5543](../sources/prs/flashinfer/PR-5543.md) | feat(cake_kda): dense-beta unbounded coverage, measured affine break-even, sm_103a constants | 2026-09-25 | swizzling | attention, flash-attention, fp4 |
| [#5545](../sources/prs/flashinfer/PR-5545.md) | feat(cake_nvfp4_attn): MiniMax-H3 SM120 ragged NVFP4 attention with the SageAttention3 FP4 recipe (experimental, #4532 candidate 5090-K2) | 2026-09-25 |  | attention, block-scale, flash-attention |
| [#5547](../sources/prs/flashinfer/PR-5547.md) | perf(cake_mla): split the FP8 page-64 producer o_done handshake per V stage (SM100 + SM103) | 2026-09-25 | pipeline-stages | attention, clc, flash-attention |
| [#5548](../sources/prs/flashinfer/PR-5548.md) | perf(cake_backend): drop the redundant device fence before the grid join in the Kimi-K3 fused router (SM100/SM103) | 2026-09-25 |  | attention, flash-attention, fp4 |
| [#5551](../sources/prs/flashinfer/PR-5551.md) | feat(cake_kda): Kimi K3 TP12 H=8 fused KDA decode in the Cake backend on SM100/SM103 | 2026-09-25 | pipeline-stages | attention, flash-attention, fp4 |
| [#5552](../sources/prs/flashinfer/PR-5552.md) | feat(cake_kimi_k3_mla): Cake-generated Kimi-K3 MLA FP8 paged attention backend for SM100/SM103 (backend="cake") | 2026-09-25 | pipeline-stages, swizzling | attention, flash-attention, fp4 |
| [#5554](../sources/prs/flashinfer/PR-5554.md) | feat(cake_vision_backend): Kimi-K3 vision tower Cake backend (SM100a/SM103a) with generated programs | 2026-09-25 | pipeline-stages | attention, flash-attention, fp4 |
| [#5558](../sources/prs/flashinfer/PR-5558.md) | feat(cake_warp_decode): add clamped DeepSeek-V4-Flash routed NVFP4 decode for SM100 | 2026-09-25 | pipeline-stages | attention, block-scale, flash-attention |
| [#5509](../sources/prs/flashinfer/PR-5509.md) | feat(cake_megamoe_topk_reduce): publish the SM103a reducer export and enable the native reducer on B300 | 2026-09-24 |  | attention, flash-attention, fp4 |
| [#5513](../sources/prs/flashinfer/PR-5513.md) | perf(cake_diffusion): 256x448 GEMM tile for the MiniMax-H3 FC1+SwiGLU NVFP4 operator (SM100a/SM103a) | 2026-09-24 | pipeline-stages | attention, flash-attention, fp4 |
| [#5521](../sources/prs/flashinfer/PR-5521.md) | feat(cake_diffusion): MiniMax-H3 SM120 fused quantized FC1 + SwiGLU (RTX 5090 / RTX PRO 6000) | 2026-09-24 |  | attention, block-scale, flash-attention |
| [#5523](../sources/prs/flashinfer/PR-5523.md) | feat(cake_deepgemm): add generated DeepGEMM-family kernels for SM100a/SM103a (sparse MQA indexer, routing gate, mHC, MoE, FP8/FP4 GEMM) | 2026-09-24 | pipeline-stages, swizzling | attention, block-scale, flash-attention |
| [#5524](../sources/prs/flashinfer/PR-5524.md) | feat(cake_minimax_h3): SM120 FP8/NVFP4 fused MiniMax-H3 attention output projection with indexed gate + residual (RTX 5090 / RTX PRO 6000) | 2026-09-24 |  | attention, flash-attention, fp4 |
| [#5525](../sources/prs/flashinfer/PR-5525.md) | feat(cake_diffusion): add MiniMax-H3 direct-layout out-proj + gated residual for SM100 and SM103 | 2026-09-24 | double-buffering, kernel-fusion, swizzling | attention, block-scale, clc |
| [#5527](../sources/prs/flashinfer/PR-5527.md) | feat(cake_backend): MiniMax-H3 one-pass QKV quantize-and-pack helpers (NVFP4 + MXFP8, SM100a/SM103a) | 2026-09-24 | swizzling | attention, block-scale, flash-attention |
| [#5528](../sources/prs/flashinfer/PR-5528.md) | feat(cake_fused_norm_combine): SM100 eight-peer fused residual-add + RMSNorm + BF16 combine | 2026-09-24 |  | attention, flash-attention, fp4 |
| [#5529](../sources/prs/flashinfer/PR-5529.md) | feat(cake_kernel): epilogue-fused NVFP4 QKV GEMM for MiniMax-H3 pre-attention (SM100a/SM103a) | 2026-09-24 | pipeline-stages, swizzling | attention, block-scale, flash-attention |
| [#5530](../sources/prs/flashinfer/PR-5530.md) | perf(cake_minimax_h3): K/V-split the partial-wave units of the packed-varlen attention (SM100/SM103) | 2026-09-24 |  | attention, flash-attention, fp4 |
| [#5531](../sources/prs/flashinfer/PR-5531.md) | feat(cake_backend): Kimi-K3 fused MoE router (896 experts, top-16) generated programs for SM100/SM103 | 2026-09-24 |  | attention, flash-attention, fp4 |
| [#5478](../sources/prs/flashinfer/PR-5478.md) | fix(prims-ts): support CuTe DSL 4.7 and 4.8 | 2026-09-23 |  | attention, flash-attention, mla |
| [#5482](../sources/prs/flashinfer/PR-5482.md) | perf(cake_sampling): qualify the radix sampling pipeline on SM90 (H100) and SM107 (Rubin R200); select JIT targets through CompilationContext | 2026-09-23 | pipeline-stages | attention, flash-attention, fp4 |
| [#5490](../sources/prs/flashinfer/PR-5490.md) | perf(cake_backend): packed-row MTP fast path for the experimental balanced_gqa_decode (q_len_per_req 3..8) on SM100/SM103 | 2026-09-23 |  | attention, flash-attention, fp4 |
| [#5491](../sources/prs/flashinfer/PR-5491.md) | feat(cake_diffusion): add MiniMax-H3 fused RMSNorm + AdaLN + FC1 + SwiGLU for SM100 and SM103 | 2026-09-23 | kernel-fusion, swizzling | attention, block-scale, clc |
| [#5493](../sources/prs/flashinfer/PR-5493.md) | feat(cake_minimax_h3): SM120 FP8/NVFP4 fused MiniMax-H3 pre-attention (RTX 5090 / RTX PRO 6000) | 2026-09-23 |  | attention, flash-attention, fp4 |
| [#5494](../sources/prs/flashinfer/PR-5494.md) | docs: fix live documentation audit findings | 2026-09-23 |  | attention, gemm, grouped-gemm |
| [#5496](../sources/prs/flashinfer/PR-5496.md) | feat(cake_backend): add MiniMax-H3 NVFP4 (W4A4) pre-attention for SM100a/SM103a | 2026-09-23 | swizzling | attention, block-scale, flash-attention |
| [#5497](../sources/prs/flashinfer/PR-5497.md) | fix(moe): forward enable_pdl to CuTeDSL MoE routing | 2026-09-23 |  | moe |
| [#5499](../sources/prs/flashinfer/PR-5499.md) | feat(cake_minimax_h3): experimental MiniMax-H3 packed-varlen BF16 + NVFP4 attention (SM100/SM103) | 2026-09-23 | pipeline-stages | attention, flash-attention, fp4 |
| [#5500](../sources/prs/flashinfer/PR-5500.md) | feat(cake_gemm): prepared contiguous grouped FP8 GEMM program family for SM100a | 2026-09-23 | pipeline-stages, stream-k, warp-specialization | attention, block-scale, flash-attention |
| [#5503](../sources/prs/flashinfer/PR-5503.md) | feat(kda): support bf16 state in packed fused KDA decode for T>1 | 2026-09-23 |  |  |
| [#5504](../sources/prs/flashinfer/PR-5504.md) | Per-token alpha for NVFP4 mm_fp4 (CuTe-DSL SM100/SM103) and out_scale fold in per-token quantize | 2026-09-23 | pipeline-stages | fp4, gemm, moe |
| [#5506](../sources/prs/flashinfer/PR-5506.md) | perf(cake_diffusion): 256-column quantized GEMM tiles for the MiniMax-H3 fused FC1 + SwiGLU on SM100 and SM103 | 2026-09-23 | pipeline-stages, swizzling | attention, block-scale, flash-attention |
| [#5396](../sources/prs/flashinfer/PR-5396.md) | feat(kda,mamba): enable CuTe packed KDA decode, cvt.rs stochastic rounding and Mamba2 SSD on SM107 (Rubin) | 2026-09-22 |  | attention, gemm, tcgen05 |
| [#5397](../sources/prs/flashinfer/PR-5397.md) | feat(attention): enable CuTe DSL VSA/BSA and Sage-quant tests on SM107 (Rubin) | 2026-09-22 |  | attention, flash-attention, fp8 |
| [#5402](../sources/prs/flashinfer/PR-5402.md) | feat(cake_msa): NVFP4 paged-KV MSA decode program for SM100/SM103 + layout contract | 2026-09-22 | persistent-kernel, swizzling | attention, block-scale, flash-attention |
| [#5430](../sources/prs/flashinfer/PR-5430.md) | feat(cake_fused_moe): add Kimi-K3 W4A8 MXFP4 SiTU routed MoE for SM100/SM103 | 2026-09-22 | double-buffering, kernel-fusion, persistent-kernel | attention, block-scale, flash-attention |
| [#5431](../sources/prs/flashinfer/PR-5431.md) | perf(cake_megamoe_topk_reduce): regenerate the SM100a reducer from the current Cake exporter | 2026-09-22 |  | attention, flash-attention, fp4 |
| [#5433](../sources/prs/flashinfer/PR-5433.md) | feat(cake_mega_moe): add CuTe DSL backend for experimental MXFP8 MegaMoE EP16 | 2026-09-22 |  | block-scale, reduction, topk |
| [#5434](../sources/prs/flashinfer/PR-5434.md) | feat(prims-ts): add native two-source sparse MLA | 2026-09-22 | persistent-kernel, pipeline-stages, swizzling | attention, block-scale, clc |
| [#5439](../sources/prs/flashinfer/PR-5439.md) | feat(cake_sampling): fused radix top-k / top-p sampling pipeline for SM100/SM103 (single source; SM90/SM107/SM110 compile targets) | 2026-09-22 | pipeline-stages | attention, flash-attention, fp4 |
| [#5440](../sources/prs/flashinfer/PR-5440.md) | fix(cake_kda): regenerate the BF16 KDA prefill modules with tile-anchored unbounded-gate decay (SM100/SM103) | 2026-09-22 |  | attention, flash-attention, fp4 |
| [#5442](../sources/prs/flashinfer/PR-5442.md) | feat(cake_sage): add SM100 and SM103 Sage-FP8 block-sparse attention with fused quantizer | 2026-09-22 |  | attention, flash-attention, fp4 |
| [#5443](../sources/prs/flashinfer/PR-5443.md) | feat(cake_nvfp4_mla_decode): add experimental NVFP4 DeepSeek-V4 decode attention on SM100/SM103 | 2026-09-22 | pipeline-stages | attention, block-scale, flash-attention |
| [#5444](../sources/prs/flashinfer/PR-5444.md) | fix(moe): initialize TRTLLM routing padding for TMA gathers | 2026-09-22 |  | fp4, gemm, moe |
| [#5451](../sources/prs/flashinfer/PR-5451.md) | fix(moe): skip unrouted (-1) expert ids in the SM12x b12x fused MoE | 2026-09-22 | pipeline-stages | fp4, moe, nvfp4 |
| [#5452](../sources/prs/flashinfer/PR-5452.md) | feat(cake_kda): prepared BF16 KDA prefill plan cache, FP32 intermediate states and cached affine split for unbounded FP32-state prefill (SM100/SM103) | 2026-09-22 |  | attention, flash-attention, fp4 |
| [#5455](../sources/prs/flashinfer/PR-5455.md) | feat(moe_ep): Support Kimi K3 SiTU in NVFP4 MegaMoE | 2026-09-22 |  | fp4, nvfp4 |
| [#5462](../sources/prs/flashinfer/PR-5462.md) | feat(moe): refresh the SM107 CuTe DSL gather+activation MoE kernel from TensorRT-LLM (SiTU, Relu2) | 2026-09-22 |  | block-scale, gemm, grouped-gemm |
| [#5463](../sources/prs/flashinfer/PR-5463.md) | feat(mla): MLA SM100 auto mode | 2026-09-22 | tile-scheduling | attention, flash-attention, fp8 |
| [#5472](../sources/prs/flashinfer/PR-5472.md) | feat(cake_fmha): MiniMax-H3 dense BF16 self-attention for SM120 (Cake kernel route + benchmark) | 2026-09-22 | double-buffering, kernel-fusion, swizzling | attention, flash-attention, fp4 |
| [#5474](../sources/prs/flashinfer/PR-5474.md) | feat(cake_gqa): experimental on-device load-balanced BF16 paged GQA decode (balanced_gqa_decode) on SM100/SM103 | 2026-09-22 |  | attention, flash-attention, fp4 |
| [#5475](../sources/prs/flashinfer/PR-5475.md) | perf(prims-ts): bf16 dense fmha context perf bringup | 2026-09-22 | pipeline-stages | attention, flash-attention, fp8 |
| [#5363](../sources/prs/flashinfer/PR-5363.md) | perf(cake_kda): route one-wave BF16 grids to the M64 value split | 2026-09-21 |  | attention, flash-attention, fp4 |
| [#5369](../sources/prs/flashinfer/PR-5369.md) | feat(cake_fmha): add BF16 head-dim-256 small-M speculative decode route | 2026-09-21 | double-buffering, pipeline-stages | attention, block-scale, flash-attention |
| [#5370](../sources/prs/flashinfer/PR-5370.md) | perf(cake_kda): regenerate the BF16 KDA modules from the current Cake revision | 2026-09-21 |  | attention, flash-attention, fp4 |
| [#5372](../sources/prs/flashinfer/PR-5372.md) | feat(moe): relax the alignment constraints of the SM90 CuTe-DSL MoE | 2026-09-21 |  | gemm, moe, tma |
| [#5378](../sources/prs/flashinfer/PR-5378.md) | feat(cake_gdn): add Qwen3.5 TP2 seven-token decode rows for SM100 and SM103 | 2026-09-21 |  | attention, flash-attention, fp4 |
| [#5384](../sources/prs/flashinfer/PR-5384.md) | feat(moe_ep): add SM107 block-scaled MegaMoE backends | 2026-09-21 | persistent-kernel, pipeline-stages, swizzling | block-scale, clc, fp4 |
| [#5351](../sources/prs/flashinfer/PR-5351.md) | perf(prims-ts): optimize QToken-KvBlock-Sparse-Attention | 2026-09-20 | pipeline-stages | attention, flash-attention, fp4 |
| [#5338](../sources/prs/flashinfer/PR-5338.md) | perf(mega_moe): SM90 fp8 megamoe optimization | 2026-09-19 | kernel-fusion | fp8, gemm, quantization |
| [#5340](../sources/prs/flashinfer/PR-5340.md) | fix(sampling): index per-request top_k / min_p by probs row when indices is set | 2026-09-19 |  | topk |
| [#5312](../sources/prs/flashinfer/PR-5312.md) | feat(topk_varlen): gvr_2 decode: fused page-table output (page_table), decode latency floor, K=2048 clustered admission, two-CTA slab for unsplit rows | 2026-09-18 | kernel-fusion | attention, sort, topk |
| [#5314](../sources/prs/flashinfer/PR-5314.md) | feat: Add SM100 cuteDSL ReplaySSM GDN MTP decode kernels | 2026-09-18 | pipeline-stages, swizzling, warp-specialization | gemm, tcgen05, tma |
| [#5319](../sources/prs/flashinfer/PR-5319.md) | perf: optimize CuTe DSL W4A4 and W4A16 unfused finalize | 2026-09-18 | pipeline-stages | block-scale, fp4, gemm |
| [#5320](../sources/prs/flashinfer/PR-5320.md) | feat(cake_gdn): add opt-in SM100/SM103 context-parallel prefill backend | 2026-09-18 | pipeline-stages | attention, flash-attention, fp4 |
| [#5329](../sources/prs/flashinfer/PR-5329.md) | perf: specialize persistent BatchAttention for equal KV strides | 2026-09-18 | persistent-kernel | attention, fp4, nvfp4 |
| [#5281](../sources/prs/flashinfer/PR-5281.md) | Enable PDL for intermediate quantization | 2026-09-17 |  | fp4, moe, nvfp4 |
| [#5283](../sources/prs/flashinfer/PR-5283.md) | feat(cake_nvfp4_attn): add experimental NVFP4 attention on SM103 | 2026-09-17 |  | attention, block-scale, flash-attention |
| [#5293](../sources/prs/flashinfer/PR-5293.md) | feat(cake_xqa): add experimental SM110 XQA attention (tcgen05 and register-MMA) | 2026-09-17 | pipeline-stages, swizzling | attention, flash-attention, fp4 |
| [#5295](../sources/prs/flashinfer/PR-5295.md) | feat(moe): add more activation types to the SM90 CuTe-DSL MoE backend | 2026-09-17 | warp-specialization | gemm, grouped-gemm, moe |
| [#5300](../sources/prs/flashinfer/PR-5300.md) | perf(quantization): SM107 dispatch tuning and 128x4 tile kernels for nvfp4/mxfp4/mxfp8 | 2026-09-17 | pipeline-stages, swizzling | fp4, fp8, nvfp4 |
| [#5302](../sources/prs/flashinfer/PR-5302.md) | feat(cake_gqa): add experimental prepared SM110 GQA decode | 2026-09-17 | pipeline-stages | attention, flash-attention, fp4 |
| [#5255](../sources/prs/flashinfer/PR-5255.md) | fix(gdn): honor Q/K normalization in GDN prefill | 2026-09-16 |  | attention, reduction |
| [#5272](../sources/prs/flashinfer/PR-5272.md) | feat(attention): FA2 per-(token, head) FP8 KV scale | 2026-09-16 |  | attention, block-scale, fp4 |
| [#5276](../sources/prs/flashinfer/PR-5276.md) | feat(moe): add Rubin locality-domain execution | 2026-09-16 | persistent-kernel, swizzling | block-scale, fp4, gemm |
| [#5278](../sources/prs/flashinfer/PR-5278.md) | feat(cake_kda): add TF32 and BF16 prefill kernels for SM100a and SM103a | 2026-09-16 | pipeline-stages | attention, flash-attention, fp4 |
| [#5229](../sources/prs/flashinfer/PR-5229.md) | feat(prims-ts): extend QToken-KvBlock-Sparse-Attention shapes and patterns | 2026-09-15 | persistent-kernel | attention, clc, flash-attention |
| [#5231](../sources/prs/flashinfer/PR-5231.md) | BF16 CuTeDSL Dense GEMM: use runtime M and revert kernel disk caching | 2026-09-15 |  | gemm |
| [#5239](../sources/prs/flashinfer/PR-5239.md) | Remove the SM100+ gate on the NVFP4 KV tile repack | 2026-09-15 | persistent-kernel, swizzling | attention, fp4, fp8 |
| [#5242](../sources/prs/flashinfer/PR-5242.md) | Native-layout NVFP4 W4A16 in CuTe DSL on SM12x | 2026-09-15 | swizzling | fp4, gemm, nvfp4 |
| [#5243](../sources/prs/flashinfer/PR-5243.md) | perf(cake_gdn): optimize prefill kernels for SM100 and SM103 | 2026-09-15 | pipeline-stages | attention, flash-attention, fp4 |
| [#5249](../sources/prs/flashinfer/PR-5249.md) | add-cudnn-frost-as-moe-backend | 2026-09-15 | swizzling | block-scale, fp4, gemm |
| [#5251](../sources/prs/flashinfer/PR-5251.md) | fix(topk): add missing __syncthreads before AdvanceRadixGroupBarrier | 2026-09-15 |  | topk |
| [#5207](../sources/prs/flashinfer/PR-5207.md) | fix: perf regression from missing trtllm moe tactics | 2026-09-14 |  | fp4, moe, nvfp4 |
| [#5223](../sources/prs/flashinfer/PR-5223.md) | chore: clean up stale comments and vendoring notes | 2026-09-14 |  | attention, moe |
| [#5177](../sources/prs/flashinfer/PR-5177.md) | fix(attention): size prefill partial outputs by query rows, not packed indices | 2026-09-13 |  | attention |
| [#5183](../sources/prs/flashinfer/PR-5183.md) | feat(cake_fused_moe): add Kimi-K3 NVFP4 SiTU experts for SM100/SM103 | 2026-09-13 | pipeline-stages | attention, block-scale, flash-attention |
| [#5186](../sources/prs/flashinfer/PR-5186.md) | perf: reduce split W4A16 routing and output overhead | 2026-09-13 |  | clc, fp4, moe |
| [#5187](../sources/prs/flashinfer/PR-5187.md) | fix(topk): handle padded short rows in CUB transforms | 2026-09-13 |  | attention, topk |
| [#5197](../sources/prs/flashinfer/PR-5197.md) | refactor(sparse-mla): unify SM120 execution, calibration and DSv4.1 support | 2026-09-13 | pipeline-stages, warp-specialization | attention, block-scale, fp4 |
| [#5168](../sources/prs/flashinfer/PR-5168.md) | perf(sm12x): optimize fused MoE kernels | 2026-09-12 | pipeline-stages | block-scale, fp4, moe |
| [#5169](../sources/prs/flashinfer/PR-5169.md) | perf(cake_comm): reduce PCIe CE ring publication overhead on SM120 | 2026-09-12 | pipeline-stages | attention, flash-attention, fp4 |
| [#5176](../sources/prs/flashinfer/PR-5176.md) | fix(attention): materialize block_valid_mask for padded CUDA-graph prefill launches | 2026-09-12 |  | attention, fp4, nvfp4 |
| [#5112](../sources/prs/flashinfer/PR-5112.md) | feat(quantization): support fp32 input in the CuTe-DSL mxfp8_quantize kernel | 2026-09-11 |  | fp8, quantization |
| [#5116](../sources/prs/flashinfer/PR-5116.md) | feat(cake_comm): support SM100 and SM103 TP8 packed-QKV all-gather matmul | 2026-09-11 | double-buffering, pipeline-stages | attention, flash-attention, fp4 |
| [#5119](../sources/prs/flashinfer/PR-5119.md) | feat: add low-latency Frost DSv4.1 sparse MLA decode | 2026-09-11 | persistent-kernel, pipeline-stages, swizzling | attention, fp4, fp8 |
| [#5123](../sources/prs/flashinfer/PR-5123.md) | feat(prims-ts): 8-bit Q/K/V sage attention for the PrimTS block sparse decode kernels | 2026-09-11 | persistent-kernel, pipeline-stages, tile-scheduling | attention, clc, flash-attention |
| [#5125](../sources/prs/flashinfer/PR-5125.md) | fix(cute-dsl): use has_side_effects to prevent wrong llvm optimisation | 2026-09-11 | pipeline-stages | fp4, nvfp4, quantization |
| [#5127](../sources/prs/flashinfer/PR-5127.md) | fix(cake_sage_attn): cover Sage combinations and pass tensor maps by value | 2026-09-11 | pipeline-stages | attention, flash-attention, fp4 |
| [#5134](../sources/prs/flashinfer/PR-5134.md) | fix(cake_warp_decode): extend NVFP4 warp-decode coverage and synchronization | 2026-09-11 | pipeline-stages | attention, block-scale, flash-attention |
| [#5137](../sources/prs/flashinfer/PR-5137.md) | feat(cake_diffusion): add SM100a support to MiniMax-H3 BF16 pre-attention | 2026-09-11 | pipeline-stages | attention, flash-attention, fp4 |
| [#5138](../sources/prs/flashinfer/PR-5138.md) | feat(cake_bf16_fp4_gemm): add SM100/SM103 BF16 x FP4 GEMM kernels | 2026-09-11 |  | attention, flash-attention, fp4 |
| [#5144](../sources/prs/flashinfer/PR-5144.md) | refactor(attention): use fixed page tables for paged block-sparse attention | 2026-09-11 |  | attention, sparse-attention |
| [#5148](../sources/prs/flashinfer/PR-5148.md) | perf(cake_mega_moe): optimize BF16 x MXFP8 MegaMoE EP16 backend | 2026-09-11 |  | reduction, tma, topk |
| [#5149](../sources/prs/flashinfer/PR-5149.md) | feat(moe): wire dynamic FP8 FC2 quantization for per-channel MoE | 2026-09-11 |  | fp8, gemm, moe |
| [#5152](../sources/prs/flashinfer/PR-5152.md) | feat(quantization): expose NVFP4 4over6 recipe through the public API | 2026-09-11 |  | block-scale, fp4, fp8 |
| [#5073](../sources/prs/flashinfer/PR-5073.md) | feat(gdn): prefix-cache state materialization kernel | 2026-09-10 | persistent-kernel, swizzling | gemm, mbarrier, tma |
| [#5075](../sources/prs/flashinfer/PR-5075.md) | feat(sm120): runtime KV row stride + canonical 528B GLM53_NOPE rows + NaN-safe masked gathers in sparse MLA | 2026-09-10 |  | attention, block-scale, fp4 |
| [#5076](../sources/prs/flashinfer/PR-5076.md) | feat(cake_nvfp4_svdquant): add NVFP4 SVDQuant GEMM SM100 and SM103 backend | 2026-09-10 | pipeline-stages | attention, block-scale, flash-attention |
| [#5083](../sources/prs/flashinfer/PR-5083.md) | fix(cake_sage_attention): support non-contiguous Sage attention with partial KV tiles | 2026-09-10 |  | attention, flash-attention, fp4 |
| [#5088](../sources/prs/flashinfer/PR-5088.md) | fix(sampling): preserve softmax normalization at low temperatures | 2026-09-10 |  |  |
| [#5100](../sources/prs/flashinfer/PR-5100.md) | Add SM12x NVFP4 support to the CuTe DSL GEMM backend | 2026-09-10 | double-buffering, pipeline-stages, swizzling | block-scale, fp4, gemm |
| [#5106](../sources/prs/flashinfer/PR-5106.md) | fix[mla]: add Q8 floor for tile selection in trtllm-gen sparse mla kernels | 2026-09-10 | tile-scheduling | attention, flash-attention, mla |
| [#5108](../sources/prs/flashinfer/PR-5108.md) | fix: guard K-tail loads in Blackwell gather GEMM | 2026-09-10 | swizzling | block-scale, fp4, gemm |
| [#5048](../sources/prs/flashinfer/PR-5048.md) | fix(mla): prevent intermittent hang in SM120 sparse-MLA swapAB prefill on DGX Spark | 2026-09-09 | pipeline-stages | attention, mbarrier, mla |
| [#5052](../sources/prs/flashinfer/PR-5052.md) | feat(cake_gqa): Add an experimental SM110 GQA decode kernel | 2026-09-09 | pipeline-stages | attention, flash-attention, fp4 |
| [#5059](../sources/prs/flashinfer/PR-5059.md) | feat(prims-ts): add non-absorbed MLA prefill | 2026-09-09 | pipeline-stages | attention, fp8, mla |
| [#5060](../sources/prs/flashinfer/PR-5060.md) | feat(cake_kernel): add MiniMax-H3 MXFP8 pre-attention for SM100a/SM103a | 2026-09-09 |  | attention, block-scale, flash-attention |
| [#5072](../sources/prs/flashinfer/PR-5072.md) | fix(moe): bound routing_replay_out dim0 from below in both validators | 2026-09-09 |  | fp4, fp8, moe |
| [#5019](../sources/prs/flashinfer/PR-5019.md) | feat(moe): add CuTe DSL NVFP4 W4A16 MegaMoE | 2026-09-08 | kernel-fusion, persistent-kernel, pipeline-stages | block-scale, fp4, gemm |
| [#5021](../sources/prs/flashinfer/PR-5021.md) | feat(kda): support graph-safe CuTe DSL prefix checkpoints | 2026-09-08 |  | tcgen05 |
| [#5023](../sources/prs/flashinfer/PR-5023.md) | feat(comm): add PCIe IPC all-gather and reduce-scatter | 2026-09-08 | double-buffering | fp8, reduction |
| [#5024](../sources/prs/flashinfer/PR-5024.md) | fix(moe): avoid FP8 scale overflow in the Humming MXFP4 path | 2026-09-08 |  | fp4, fp8, moe |
| [#5027](../sources/prs/flashinfer/PR-5027.md) | feat(comm): add allocation-stable head-chunk Ulysses primitives | 2026-09-08 | pipeline-stages | attention, fp8 |
| [#5031](../sources/prs/flashinfer/PR-5031.md) | fix(moe): Fix per-token quantization `fast-math` INF scale when activation contains all-zero row | 2026-09-08 |  | fp4, moe, nvfp4 |
| [#5036](../sources/prs/flashinfer/PR-5036.md) | feat(cake_warp_decode): Add SM100 NVFP4 warp decode and standalone SiLU | 2026-09-08 | pipeline-stages | attention, block-scale, flash-attention |
| [#5038](../sources/prs/flashinfer/PR-5038.md) | fix(decode): reserve max(K+V, st.o) smem for FA2 FP8+GQA decode | 2026-09-08 |  | attention, fp8 |
| [#4996](../sources/prs/flashinfer/PR-4996.md) | feat(prims-ts): add QToken-KvBlock-Sparse-Attention | 2026-09-07 | pipeline-stages | attention, flash-attention, fp8 |
| [#4997](../sources/prs/flashinfer/PR-4997.md) | perf(attention): Refresh DSL_FMHA cubins | 2026-09-07 |  | attention, block-scale, flash-attention |
| [#5002](../sources/prs/flashinfer/PR-5002.md) | perf(prims-ts): Optimize&refine PrimsTS block sparse attention | 2026-09-07 | persistent-kernel, pipeline-stages | attention, clc, flash-attention |
| [#5004](../sources/prs/flashinfer/PR-5004.md) | refactor(moe): update and refactor the SM90 CuTe-DSL MoE tactics | 2026-09-07 | pipeline-stages, swizzling | gemm, grouped-gemm, moe |
| [#5005](../sources/prs/flashinfer/PR-5005.md) | perf(moe): improve SM90 mixed-input CUTLASS MoE backend performance | 2026-09-07 | swizzling | fp4, fp8, gemm |
| [#5013](../sources/prs/flashinfer/PR-5013.md) | fix(activation): pick a vector width that divides hidden_size in act_and_mul (fixes d=3420) | 2026-09-07 |  |  |
| [#4951](../sources/prs/flashinfer/PR-4951.md) | feat(cake_sage): add SM120 block-sparse attention backend | 2026-09-04 |  | attention, flash-attention, fp4 |
| [#4955](../sources/prs/flashinfer/PR-4955.md) | feat(sm120): add NVFP4 sparse MLA support for DeepSeek V4 Flash | 2026-09-04 | double-buffering, pipeline-stages | attention, block-scale, flash-attention |
| [#4967](../sources/prs/flashinfer/PR-4967.md) | feat(cake_kda): add fused decode backend for B200 and B300 | 2026-09-04 |  | attention, flash-attention, fp4 |
| [#4970](../sources/prs/flashinfer/PR-4970.md) | feat(cake_mega_moe): add optimized MXFP8 MegaMoE EP16 backend | 2026-09-04 | kernel-fusion, pipeline-stages | block-scale, mbarrier, quantization |
| [#4980](../sources/prs/flashinfer/PR-4980.md) | feat(cake_fmha): add sm100/103 paged-attention | 2026-09-04 |  | attention, block-scale, flash-attention |
| [#4981](../sources/prs/flashinfer/PR-4981.md) | bench: sm107 whitelist and updates | 2026-09-04 | swizzling | attention, fp4, fp8 |
| [#4982](../sources/prs/flashinfer/PR-4982.md) | feat(MSA): Add NVFP4 paged-KV MSA sparse decode and prefill for SM100/SM103 | 2026-09-04 | swizzling, warp-specialization | attention, block-scale, fp4 |
| [#4908](../sources/prs/flashinfer/PR-4908.md) | [feat] Add warp level split k bf16 gemm | 2026-09-03 | pipeline-stages | gemm, mbarrier |
| [#4912](../sources/prs/flashinfer/PR-4912.md) | feat(gdn): adopt the CuTe-DSL disk cache for TVM-FFI GDN kernels | 2026-09-03 |  | fp8 |
| [#4917](../sources/prs/flashinfer/PR-4917.md) | perf(gdn): optimize SM100 CP kernels | 2026-09-03 |  | attention |
| [#4918](../sources/prs/flashinfer/PR-4918.md) | feat(mla): expose DSv4 TRTLLM-GEN RopeQuant | 2026-09-03 | tile-scheduling | attention, block-scale, flash-attention |
| [#4927](../sources/prs/flashinfer/PR-4927.md) | docs: resolve documentation check failures | 2026-09-03 |  | attention, fp8, moe |
| [#4929](../sources/prs/flashinfer/PR-4929.md) | feat(comm): add fused decode CP A2A + LSE reduce | 2026-09-03 | kernel-fusion | attention, flash-attention, mla |
| [#4894](../sources/prs/flashinfer/PR-4894.md) | fix(moe): write fused-shared routing replay as routed-only [T, K] | 2026-09-02 |  | fp4, fp8, moe |
| [#4859](../sources/prs/flashinfer/PR-4859.md) | feat(attention): add skip-softmax to SM120 PRIMS | 2026-09-01 | pipeline-stages | attention, flash-attention, fp8 |
| [#4860](../sources/prs/flashinfer/PR-4860.md) | feat(cake_concat_mla): add SM100/SM103 concat MLA K backend | 2026-09-01 |  | fp8, mla |
| [#4872](../sources/prs/flashinfer/PR-4872.md) | feat(prims-ts): support proxy-compensated block-sparse attention | 2026-09-01 | pipeline-stages | attention, flash-attention, sparse-attention |
| [#4878](../sources/prs/flashinfer/PR-4878.md) | feat(moe): add CuTe DSL SM90 BF16 MoE backend | 2026-09-01 | pipeline-stages, swizzling, warp-specialization | gemm, grouped-gemm, mbarrier |
| [#4829](../sources/prs/flashinfer/PR-4829.md) | refactor(attention): unify PrimTS plan/run and page-table contracts | 2026-08-31 | swizzling | attention, mla, tcgen05 |
| [#4830](../sources/prs/flashinfer/PR-4830.md) | feat(prims_ts): support no-padding MLA query rows | 2026-08-31 |  | attention, flash-attention, mla |
| [#4831](../sources/prs/flashinfer/PR-4831.md) | feat: add is_deterministic mode to top_k_renorm_probs | 2026-08-31 |  | quantization, reduction, sort |
| [#4838](../sources/prs/flashinfer/PR-4838.md) | Refactor SM120 grouped GEMM as SM12x GEMM | 2026-08-31 |  | block-scale, fp8, gemm |
| [#4839](../sources/prs/flashinfer/PR-4839.md) | feat(attention): opt-in LDTM.STAT for PrimTS context row_max | 2026-08-31 |  | attention, flash-attention, fp8 |
| [#4843](../sources/prs/flashinfer/PR-4843.md) | feat(moe_ep): add fused Hopper MXFP4 MegaMoE with autotuning | 2026-08-31 | pipeline-stages, swizzling | fp4, fp8, gemm |
| [#4845](../sources/prs/flashinfer/PR-4845.md) | feat(cake_kda): add fp32 state & long context kda prefill kernels | 2026-08-31 | pipeline-stages, swizzling, tile-scheduling | attention, flash-attention, fp4 |
| [#4849](../sources/prs/flashinfer/PR-4849.md) | feat(cake_tinygemm2): enable tinygemm2_sm100 on SM107 (Rubin) | 2026-08-31 |  | gemm |
| [#4851](../sources/prs/flashinfer/PR-4851.md) | feat(moe): enable tile_size=256 for Rubin MoE autotuning | 2026-08-31 |  | moe, quantization |
| [#4853](../sources/prs/flashinfer/PR-4853.md) | fix(gemm,moe): restore bmm_fp8 auto fallback and drop an over-strict SM107 tactic guard | 2026-08-31 |  | block-scale, fp8, gemm |
| [#4855](../sources/prs/flashinfer/PR-4855.md) | feat(cake_warp_decode): add SM103 NVFP4 warp-decode backend | 2026-08-31 |  | attention, flash-attention, fp4 |
| [#4856](../sources/prs/flashinfer/PR-4856.md) | fix(fp4_gemm autotune) SM107 kernel family excluded from autotune candidates and heuristics update | 2026-08-31 | persistent-kernel, swizzling | fp4, gemm |
| [#4822](../sources/prs/flashinfer/PR-4822.md) | feat(cake_comm): extend Blackwell all-gather matmul to TP8 | 2026-08-30 | pipeline-stages | attention, flash-attention, fp4 |
| [#4825](../sources/prs/flashinfer/PR-4825.md) | perf(cute-dsl): skip inactive pages in windowed decode | 2026-08-30 |  | attention, reduction |
| [#4815](../sources/prs/flashinfer/PR-4815.md) | Replayssm prefix materialize | 2026-08-29 | persistent-kernel | fp8 |
| [#4819](../sources/prs/flashinfer/PR-4819.md) | feat(cake_mega_moe): add reusable MegaMoE workspaces and an SM100a reducer | 2026-08-29 |  | attention, flash-attention, fp4 |
| [#4820](../sources/prs/flashinfer/PR-4820.md) | feat(cake_backend): add grouped MXFP8 quantization | 2026-08-29 |  | attention, flash-attention, fp4 |
| [#4821](../sources/prs/flashinfer/PR-4821.md) | feat(cake_bgmv): add deterministic prepared Blackwell MoE backend | 2026-08-29 | pipeline-stages | attention, flash-attention, fp4 |
| [#4793](../sources/prs/flashinfer/PR-4793.md) | Unify MoE CuTe DSL dispatch to be dtype agnostic | 2026-08-28 | pipeline-stages | block-scale, fp4, gemm |
| [#4802](../sources/prs/flashinfer/PR-4802.md) | Refactor Sparse MLA SM120 | 2026-08-28 | double-buffering, pipeline-stages, warp-specialization | attention, block-scale, fp8 |
| [#4804](../sources/prs/flashinfer/PR-4804.md) | perf(cake_vsa): refresh Blackwell block-sparse WS kernel | 2026-08-28 | pipeline-stages | attention, flash-attention, fp4 |
| [#4809](../sources/prs/flashinfer/PR-4809.md) | feat(kda): add fused speculative decode kernel | 2026-08-28 | kernel-fusion | quantization, reduction |
| [#4810](../sources/prs/flashinfer/PR-4810.md) | feat(cake_mega_moe): add SM100 BF16 rank-major MegaMoE backend | 2026-08-28 |  | attention, flash-attention, fp4 |
| [#4811](../sources/prs/flashinfer/PR-4811.md) | feat(topk): self-sampling GVR V2 backend (SM100/103/107), oracle-tracking auto, and the V1 threshold repair | 2026-08-28 |  | block-scale, sort, tcgen05 |
| [#4767](../sources/prs/flashinfer/PR-4767.md) | fix(attention): count NVFP4 scale-factor staging in the batch smem budget | 2026-08-27 |  | attention, fp4, nvfp4 |
| [#4769](../sources/prs/flashinfer/PR-4769.md) | perf(attention): repack NVFP4 KV tiles to 16-bit on targets without a native E2M1 convert | 2026-08-27 | swizzling | attention, flash-attention, fp4 |
| [#4772](../sources/prs/flashinfer/PR-4772.md) | Add bias support to cublast gemm backend and as fallback backend for cutedsl gemm backend | 2026-08-27 |  | gemm |
| [#4787](../sources/prs/flashinfer/PR-4787.md) | Rubin open issue fixes | 2026-08-27 |  | attention, fp4, fp8 |
| [#4736](../sources/prs/flashinfer/PR-4736.md) | perf(attention): specialize paged FA2 equal-stride KV | 2026-08-26 |  | attention, fp4, nvfp4 |
| [#4737](../sources/prs/flashinfer/PR-4737.md) | Paged-MQA logits: Rubin (SM107) enablement, FP4 next_n=4, and DKG epilogue/scheduler optimizations | 2026-08-26 | persistent-kernel, pipeline-stages | attention, block-scale, fp4 |
| [#4741](../sources/prs/flashinfer/PR-4741.md) | Fix TRTLLM MOE per-token NVFP4 TileN 192 and update cubins | 2026-08-26 |  | fp4, moe, nvfp4 |
| [#4746](../sources/prs/flashinfer/PR-4746.md) | perf(attention): cut NVFP4 KV dequant instructions on targets without native FP4/FP8 conversion | 2026-08-26 |  | attention, block-scale, fp4 |
| [#4752](../sources/prs/flashinfer/PR-4752.md) | perf(sparse mla): Update sparse MLA half-Q-tile heuristic to apply to short queries only | 2026-08-26 |  | attention, flash-attention, fp4 |
| [#4753](../sources/prs/flashinfer/PR-4753.md) | fix(cute_dsl): make the optional-dependency guard independent of cutlass | 2026-08-26 |  | attention, block-scale, gemm |
| [#4718](../sources/prs/flashinfer/PR-4718.md) | perf(sm12x): optimize and unify static MoE | 2026-08-25 | pipeline-stages | attention, fp4, moe |
| [#4719](../sources/prs/flashinfer/PR-4719.md) | feat(mla): support variable-Q decode with DCP in CuTeDSL | 2026-08-25 |  | attention, fp8, mla |
| [#4720](../sources/prs/flashinfer/PR-4720.md) | feat(moe): add SM12x (SM120/SM121) fp8 + mxfp8_mxfp4 grouped-MoE kernels | 2026-08-25 | swizzling, tile-scheduling, warp-specialization | block-scale, fp4, fp8 |
| [#4722](../sources/prs/flashinfer/PR-4722.md) | feat(cake_comm): Add a Cake Blackwell all-gather matmul backend | 2026-08-25 | pipeline-stages | attention, flash-attention, fp4 |
| [#4726](../sources/prs/flashinfer/PR-4726.md) | feat(cake_kda): add recurrent training template dispatch | 2026-08-25 | pipeline-stages, swizzling | attention, flash-attention, fp4 |
| [#4728](../sources/prs/flashinfer/PR-4728.md) | perf(cake_kda): add recurrence-piece persistent M128 prefill | 2026-08-25 |  | attention, flash-attention, fp4 |
| [#4732](../sources/prs/flashinfer/PR-4732.md) | [bug fix] Issue 3700 sparse mla sm121 hang | 2026-08-25 |  | attention, mla, topk |
| [#4733](../sources/prs/flashinfer/PR-4733.md) | perf(activation): cap act_and_mul_kernel block size for ~17-19% speedup at large hidden dims | 2026-08-25 |  |  |
| [#4735](../sources/prs/flashinfer/PR-4735.md) | Fix MoE Tile Mapping Zeroing | 2026-08-25 |  | block-scale, moe |
| [#4697](../sources/prs/flashinfer/PR-4697.md) | refactor(mla): isolate planned FA2, FA3, and CUTLASS backends | 2026-08-24 |  | attention, fp8, mla |
| [#4699](../sources/prs/flashinfer/PR-4699.md) | perf(gdn): reduce non-CP CuTeDSL launch overhead | 2026-08-24 |  |  |
| [#4702](../sources/prs/flashinfer/PR-4702.md) | fix(fmha): select CGA reduction for MLA H512 decode | 2026-08-24 |  | attention, flash-attention, fp8 |
| [#4708](../sources/prs/flashinfer/PR-4708.md) | (perf) add fused_GDN_step support for Qwen 3.6 35B A3B on sm120 | 2026-08-24 | persistent-kernel | gemv, reduction |
| [#4710](../sources/prs/flashinfer/PR-4710.md) | fix(kda): accept SM107 (Rubin) in the FlashKDA family guards | 2026-08-24 |  | gemm, moe |
| [#4714](../sources/prs/flashinfer/PR-4714.md) | feat: Add cute-dsl-prims backend for SM120 FP8 GQA prefill | 2026-08-24 |  | attention, flash-attention, fp8 |
| [#4688](../sources/prs/flashinfer/PR-4688.md) | Sm90 megamoe optimization | 2026-08-23 | kernel-fusion, pipeline-stages | fp4, fp8, gemm |
| [#4690](../sources/prs/flashinfer/PR-4690.md) | feat(cake_diffusion): add SM103a BF16 pre-attention | 2026-08-23 | kernel-fusion, pipeline-stages | attention, flash-attention, fp4 |
| [#4691](../sources/prs/flashinfer/PR-4691.md) | feat(sparse): add SM120 Sage (QK-INT8/PV-FP8 and ALL FP8) block-sparse attention (b… | 2026-08-23 | pipeline-stages, swizzling | attention, fp8, gemm |
| [#4675](../sources/prs/flashinfer/PR-4675.md) | perf(cake_kda): further optimize recurrent-KDA prefill on Blackwell | 2026-08-22 | pipeline-stages | attention, flash-attention, fp4 |
| [#4676](../sources/prs/flashinfer/PR-4676.md) | feat: add NVFP4 quantize-append path for the MLA paged KV cache | 2026-08-22 |  | attention, fp4, fp8 |
| [#4685](../sources/prs/flashinfer/PR-4685.md) | Add CuteDSL Low Latency GEMM tactic to mm_fp4, mm_fp8, mm_mxfp8, tgv_gemm_sm100 backends (SM100/SM103) | 2026-08-22 | pipeline-stages, swizzling, warp-specialization | block-scale, fp4, fp8 |
| [#4650](../sources/prs/flashinfer/PR-4650.md) | feat(mla): uniform LSE base semantics via return_lse_base_on_e | 2026-08-21 |  | attention, flash-attention, fp8 |
| [#4654](../sources/prs/flashinfer/PR-4654.md) | fix: SageAttention support block size doesn't divide sequence; support K-smoothing  | 2026-08-21 |  | attention, flash-attention, quantization |
| [#4660](../sources/prs/flashinfer/PR-4660.md) | fix(sm120): align MXFP8 plain tactic and FP8 moe stage policy | 2026-08-21 |  | fp8, moe |
| [#4664](../sources/prs/flashinfer/PR-4664.md) | fix(attention): make PrimTS paged block-sparse metadata live | 2026-08-21 |  | attention, flash-attention, sparse-attention |
| [#4667](../sources/prs/flashinfer/PR-4667.md) | fix(kda): fall back to Cake when CuTe DSL predates cutlass.experimental | 2026-08-21 |  | attention, mla, tcgen05 |
| [#4632](../sources/prs/flashinfer/PR-4632.md) | [SM120] Add W4A8 CuTeDSL MegaMoE backend | 2026-08-20 | kernel-fusion, persistent-kernel, pipeline-stages | block-scale, clc, fp4 |
| [#4633](../sources/prs/flashinfer/PR-4633.md) | feat(kda): add SM120a CuTe DSL prefill backend | 2026-08-20 | swizzling | reduction, tma |
| [#4635](../sources/prs/flashinfer/PR-4635.md) | [perf] split TRT-LLM Gen routing kernels to reduce compile time | 2026-08-20 |  |  |
| [#4636](../sources/prs/flashinfer/PR-4636.md) | feat(cake_kda): add paired recurrent training for SM100a and SM103a | 2026-08-20 |  | attention, flash-attention, fp4 |
| [#4638](../sources/prs/flashinfer/PR-4638.md) | feat(cake_activation): add fused Blackwell SwiGLU MXFP8 quantization | 2026-08-20 |  | attention, flash-attention, fp4 |
| [#4649](../sources/prs/flashinfer/PR-4649.md) | fix(cute_dsl): consult the arch gate in the GEMM and GDN dispatchers | 2026-08-20 |  | gemm |
| [#4599](../sources/prs/flashinfer/PR-4599.md) | Adding var-window FMHA context support for PrimsTS. | 2026-08-19 |  | attention, flash-attention, fp8 |
| [#4602](../sources/prs/flashinfer/PR-4602.md) | fix(moe): restore SM12x MoE kernels broken by self-resolved helper in borrowed dense methods | 2026-08-19 |  | fp4, gemm, moe |
| [#4603](../sources/prs/flashinfer/PR-4603.md) | feat(moe): allow B12xMoEWrapper to share pre-allocated workspaces | 2026-08-19 |  | fp4, moe, nvfp4 |
| [#4604](../sources/prs/flashinfer/PR-4604.md) | feat(moe_ep): MXFP8 x BF16 integration | 2026-08-19 | pipeline-stages, swizzling | fp4, fp8, gemm |
| [#4612](../sources/prs/flashinfer/PR-4612.md) | feat(cute_dsl): replace SM100 blk64 BSA C++/CUTLASS kernel with CuTe-DSL | 2026-08-19 | pipeline-stages, swizzling, tile-scheduling | attention, block-scale, clc |
| [#4616](../sources/prs/flashinfer/PR-4616.md) | feat(cake_mamba): add Blackwell selective state update backend | 2026-08-19 | pipeline-stages | attention, flash-attention, fp4 |
| [#4621](../sources/prs/flashinfer/PR-4621.md) | Enable top_k_varlen on Rubin (SM107) and add the DKG filtered-radix backend (`radix_filter`) | 2026-08-19 | double-buffering | scan, sort, tma |
| [#4573](../sources/prs/flashinfer/PR-4573.md) | feat(cake_sparse_mla): support SM100 and SM103 | 2026-08-18 | pipeline-stages | attention, flash-attention, fp4 |
| [#4576](../sources/prs/flashinfer/PR-4576.md) | feat(cake_mamba): add Blackwell Mamba SSDCombined | 2026-08-18 | pipeline-stages | attention, flash-attention, fp4 |
| [#4581](../sources/prs/flashinfer/PR-4581.md) | feat(cake_gdn): add gdn prefill decode mtp Cake backend for SM100 and SM103 | 2026-08-18 | pipeline-stages | attention, flash-attention, fp4 |
| [#4587](../sources/prs/flashinfer/PR-4587.md) | feat(cake_backend): accelerate DeepSeek fused routing | 2026-08-18 |  | attention, flash-attention, fp4 |
| [#4590](../sources/prs/flashinfer/PR-4590.md) | add backward-compatible aliases for bsa_attn_fwd and bsa_attn_blk64_fwd | 2026-08-18 |  | attention, sparse-attention |
| [#4593](../sources/prs/flashinfer/PR-4593.md) | feat(cake_vsa): add optimized SM100/SM103 block-sparse attention (VSA) | 2026-08-18 | pipeline-stages | attention, flash-attention, fp4 |
| [#4594](../sources/prs/flashinfer/PR-4594.md) | feat(cake_backend): add Blackwell Router GEMM | 2026-08-18 |  | attention, flash-attention, fp4 |
| [#4595](../sources/prs/flashinfer/PR-4595.md) | fix(sampling): reject unsafe multi-CTA top-k launches on low-SM GPUs | 2026-08-18 |  | sort, topk |
| [#4596](../sources/prs/flashinfer/PR-4596.md) | feat: trtllm-gen FMHA features for sm107 (spcompress, fp16softmax) | 2026-08-18 | tile-scheduling | attention, flash-attention, mla |
| [#4557](../sources/prs/flashinfer/PR-4557.md) | feat(cake_mla): add generated Blackwell TRT-LLM MLA decode backend for SM100 and SM103 | 2026-08-17 | pipeline-stages | attention, clc, flash-attention |
| [#4558](../sources/prs/flashinfer/PR-4558.md) | fix(moe): release W4A16 CuTe DSL scratch workspaces | 2026-08-17 |  | fp4, fp8, moe |
| [#4562](../sources/prs/flashinfer/PR-4562.md) | feat(cake_kda): add optimized H12 packed decode across SM100 family | 2026-08-17 |  | attention, flash-attention, fp4 |
| [#4563](../sources/prs/flashinfer/PR-4563.md) | [fix] disable tileN=192 for trtllmgen per-token NVFP4 MoE | 2026-08-17 |  | fp4, moe, nvfp4 |
| [#4570](../sources/prs/flashinfer/PR-4570.md) | feat(xqa): support non-MLA head_dim 512 (Gemma-style GQA decode) on SM12x | 2026-08-17 | swizzling | attention, fp8, mla |
| [#4571](../sources/prs/flashinfer/PR-4571.md) | feat(cake_kda): optimize small-BH recurrent-KDA prefill | 2026-08-17 |  | attention, flash-attention, fp4 |
| [#4540](../sources/prs/flashinfer/PR-4540.md) | perf(moe): fold W4A16 SiTU reciprocals | 2026-08-16 |  | fp4, gemm, moe |
| [#4545](../sources/prs/flashinfer/PR-4545.md) | Add ReplaySSM autotuning | 2026-08-16 | pipeline-stages |  |
| [#4528](../sources/prs/flashinfer/PR-4528.md) | fix(gdn): support WY ucache kernels on SM121 | 2026-08-15 |  |  |
| [#4535](../sources/prs/flashinfer/PR-4535.md) | feat(cake_kda): add native unbounded-softplus Kimi-Linear kernels | 2026-08-15 | pipeline-stages, swizzling | attention, flash-attention, fp4 |
| [#4518](../sources/prs/flashinfer/PR-4518.md) | feat(cake_fmha): add native Blackwell DCP speculative decode | 2026-08-14 | pipeline-stages | attention, flash-attention, fp4 |
| [#4525](../sources/prs/flashinfer/PR-4525.md) | fix(xqa): out-of-bounds read of attention sinks in SM90 kernel epilogue | 2026-08-14 |  | attention, fp8 |
| [#4526](../sources/prs/flashinfer/PR-4526.md) | feat: CuTe DSL kernels for Rubin (SM107) and batched FP8 GEMM for Blackwell | 2026-08-14 | persistent-kernel, pipeline-stages, swizzling | attention, block-scale, flash-attention |
| [#4494](../sources/prs/flashinfer/PR-4494.md) | fix(norm): limit add RMSNorm FP4 launch config heuristics to SM100 and SM103 | 2026-08-13 |  | fp4, nvfp4, quantization |
| [#4501](../sources/prs/flashinfer/PR-4501.md) | docs: include top_k in topk API docs | 2026-08-13 |  | attention, fp4, fp8 |
| [#4502](../sources/prs/flashinfer/PR-4502.md) | perf(sm120): optimize NVFP4 attention with N64 score-slot reuse | 2026-08-13 | persistent-kernel, pipeline-stages | attention, fp4, gemm |
| [#4506](../sources/prs/flashinfer/PR-4506.md) | perf(moe): fold the SiTU beta reciprocal in the CuTe DSL MoE epilogue | 2026-08-13 |  | block-scale, fp4, moe |
| [#4507](../sources/prs/flashinfer/PR-4507.md) | fix(gdn): compile and tune CuTe-DSL decode kernels for the operand device | 2026-08-13 |  |  |
| [#4474](../sources/prs/flashinfer/PR-4474.md) | feat(attention): add PrimTS Q64/KV256 and paged GQA block-sparse attention | 2026-08-12 | persistent-kernel, pipeline-stages, swizzling | attention, clc, flash-attention |
| [#4478](../sources/prs/flashinfer/PR-4478.md) | feat: unpacked FP8 per-tensor scaling support for TRTLLM fused MoE | 2026-08-12 |  | fp8, gemm, moe |
| [#4479](../sources/prs/flashinfer/PR-4479.md) | feat(b12x): support MXFP4 dense GEMM on SM120 | 2026-08-12 |  | fp4, gemm, moe |
| [#4480](../sources/prs/flashinfer/PR-4480.md) | feat(norm): fused Add+RMSNorm+1x128 fp8 block-quant producer | 2026-08-12 | kernel-fusion | block-scale, fp8, moe |
| [#4481](../sources/prs/flashinfer/PR-4481.md) | Add Qwen fused GDN decode step for sm120 | 2026-08-12 | persistent-kernel | fp4, gemv, nvfp4 |
| [#4457](../sources/prs/flashinfer/PR-4457.md) | Update Docker CI tags to 20260811-e673f7f | 2026-08-11 |  | fp8, quantization |
| [#4460](../sources/prs/flashinfer/PR-4460.md) | feat(moe): add SiTU-GLU activation to the CUTLASS fused-MoE backend | 2026-08-11 |  | fp8, moe |
| [#4466](../sources/prs/flashinfer/PR-4466.md) | feat: sm100 cute_dsl w4a16 gemm | 2026-08-11 | swizzling | fp4, fp8, gemm |
| [#4431](../sources/prs/flashinfer/PR-4431.md) | fix(moe): use per-expert Humming residual scales in SM90 CUTLASS MXFP4xFP8 MoE backend | 2026-08-10 | swizzling | fp4, fp8, gemm |
| [#4436](../sources/prs/flashinfer/PR-4436.md) | feat(gdn): add pooled state and state checkpointing and dtype support for feature parity | 2026-08-10 |  | tcgen05, tmem |
| [#4440](../sources/prs/flashinfer/PR-4440.md) | feat(moe): MXFP8 x MXFP4 CuTe-DSL fused MoE for SM100, plus large-batch routing locality | 2026-08-10 | pipeline-stages | fp4, gemm, grouped-gemm |
| [#4442](../sources/prs/flashinfer/PR-4442.md) | feat: CUB `DeviceBatchedTopK` top-k backend with variable-length support | 2026-08-10 | pipeline-stages | sort, topk |
| [#4444](../sources/prs/flashinfer/PR-4444.md) | perf(gdn): reuse pretranspose kernels across pool capacity and stride | 2026-08-10 |  |  |
| [#4445](../sources/prs/flashinfer/PR-4445.md) | feat(cake_kda): add strided prefill state checkpoints and packed decode | 2026-08-10 | swizzling | attention, flash-attention, fp4 |
| [#4449](../sources/prs/flashinfer/PR-4449.md) | refactor(moe_ep): taxonomy/provenance restructure; incorporate SM90 push-style FP8 backend; sync CuTe-DSL 4.7 quant-staging fix | 2026-08-10 | swizzling | block-scale, fp4, fp8 |
| [#4416](../sources/prs/flashinfer/PR-4416.md) | perf(norm): speed up fused add RMSNorm FP4 quantization | 2026-08-08 | swizzling | fp4, nvfp4, quantization |
| [#4420](../sources/prs/flashinfer/PR-4420.md) | feat: SM120 NVFP4 SVDQuant Gemm in CuteDSL | 2026-08-08 | pipeline-stages, swizzling | block-scale, fp4, fp8 |
| [#4423](../sources/prs/flashinfer/PR-4423.md) | perf(cake_tinygemm2): add a STAGES=16 kernel tier for single-wave large-K shapes | 2026-08-08 | swizzling | fp8, gemm, mbarrier |
| [#4386](../sources/prs/flashinfer/PR-4386.md) | feat(moe_ep): SM100 BF16 CuTeDSL MegaMoE kernel | 2026-08-07 | double-buffering, kernel-fusion, pipeline-stages | block-scale, clc, fp4 |
| [#4387](../sources/prs/flashinfer/PR-4387.md) | feat(moe_ep): SM120 MXFP8 swap-AB CuTeDSL MegaMoE kernel | 2026-08-07 | double-buffering, kernel-fusion, persistent-kernel | block-scale, clc, fp4 |
| [#4389](../sources/prs/flashinfer/PR-4389.md) | fix(fmha): propagate LSE reduction launch errors | 2026-08-07 |  | attention, flash-attention, reduction |
| [#4394](../sources/prs/flashinfer/PR-4394.md) | feat(moe): support GeGLU and SiTU in W4A16 | 2026-08-07 |  | fp4, moe, nvfp4 |
| [#4401](../sources/prs/flashinfer/PR-4401.md) | fix(attention): handle extreme negative logits in masked softmax | 2026-08-07 |  | attention, mla, reduction |
| [#4404](../sources/prs/flashinfer/PR-4404.md) | feat(moe): add TopKSigmoid routing method (TopK -> Sigmoid) | 2026-08-07 |  | moe, topk |
| [#4405](../sources/prs/flashinfer/PR-4405.md) | Feat/deepseek fused moe fp8 blockwise swigluoai | 2026-08-07 |  | attention, block-scale, fp4 |
| [#4413](../sources/prs/flashinfer/PR-4413.md) | [prims-ts] Refactor FMHA decode padding-task scheduling | 2026-08-07 |  | attention, flash-attention |
| [#4414](../sources/prs/flashinfer/PR-4414.md) | [prims-ts] Mixed precision Fmha decode | 2026-08-07 | pipeline-stages, swizzling | attention, flash-attention, fp4 |
| [#4365](../sources/prs/flashinfer/PR-4365.md) | Add paged MQA logits (attn_scores) kernels for Blackwell SM100 | 2026-08-06 | persistent-kernel, pipeline-stages, swizzling | attention, fp4, fp8 |
| [#4368](../sources/prs/flashinfer/PR-4368.md) | Fix HCA Gather4 support for public CuTe DSL | 2026-08-06 | pipeline-stages | attention, tcgen05, tma |
| [#4370](../sources/prs/flashinfer/PR-4370.md) | feat(cake_bf16_bmm): add optimized SM100a and SM103a backend | 2026-08-06 |  | attention, flash-attention, fp4 |
| [#4373](../sources/prs/flashinfer/PR-4373.md) | feat: support FP8 KV NoPE MLA on SM90 | 2026-08-06 | swizzling | attention, fp8, mla |
| [#4374](../sources/prs/flashinfer/PR-4374.md) | perf(gdn): optimize cp host launch overhead for sm90 and sm120 | 2026-08-06 | pipeline-stages |  |
| [#4377](../sources/prs/flashinfer/PR-4377.md) | fix: guard oversized shared memory driver enums with CUDA >= 13.4 | 2026-08-06 |  | attention, flash-attention |
| [#4380](../sources/prs/flashinfer/PR-4380.md) | feat(sm120): consolidate DSV4 sparse MLA top-k 192/256 support | 2026-08-06 |  | attention, fp4, mla |
| [#4382](../sources/prs/flashinfer/PR-4382.md) | fix: correct trtllm-gen reduction indexing for FMHA decode at long q_len | 2026-08-06 |  | attention, flash-attention, reduction |
| [#4355](../sources/prs/flashinfer/PR-4355.md) | feat(cake_msa): add Blackwell minimax sparse attention source kernels | 2026-08-05 | pipeline-stages, swizzling | attention, flash-attention, fp4 |
| [#4357](../sources/prs/flashinfer/PR-4357.md) | Add task-scheduled Blackwell attention kernels | 2026-08-05 | double-buffering, persistent-kernel, pipeline-stages | attention, clc, flash-attention |
| [#4361](../sources/prs/flashinfer/PR-4361.md) | Add CUTLASS Primitives and Task Scheduling Blackwell MoE kernels | 2026-08-05 | persistent-kernel | block-scale, clc, fp4 |
| [#4362](../sources/prs/flashinfer/PR-4362.md) | fix: honor sparse MLA KV page strides | 2026-08-05 |  | attention, mla, tma |
| [#4329](../sources/prs/flashinfer/PR-4329.md) | feat: optimize gated SM12x dynamic NVFP4 MoE | 2026-08-04 |  | attention, fp4, moe |
| [#4331](../sources/prs/flashinfer/PR-4331.md) | perf(moe): persist b12x MoE CuTe-DSL kernels to the disk cache | 2026-08-04 | pipeline-stages | block-scale, fp4, gemm |
| [#4335](../sources/prs/flashinfer/PR-4335.md) | feat: add CuTe-DSL backend for layernorm_quant | 2026-08-04 |  | fp8, mbarrier, quantization |
| [#4339](../sources/prs/flashinfer/PR-4339.md) | perf(cake_alpha_moe): accelerate AlphaMoE fused router on Blackwell | 2026-08-04 |  | attention, flash-attention, fp4 |
| [#4340](../sources/prs/flashinfer/PR-4340.md) | feat(cake_alpha_moe): add Blackwell AlphaMoE NVFP4 expert up/down compute | 2026-08-04 | pipeline-stages | attention, block-scale, flash-attention |
| [#4345](../sources/prs/flashinfer/PR-4345.md) | feat(msa): fp8 index-k and index-q support in the SM12x proxy-score kernels | 2026-08-04 | pipeline-stages, swizzling | fp8, gemm, mbarrier |
| [#4351](../sources/prs/flashinfer/PR-4351.md) | fix(cake_kda): support non-aligned recurrent prefill head counts | 2026-08-04 |  | attention, flash-attention, fp4 |
| [#4318](../sources/prs/flashinfer/PR-4318.md) | perf(sm120): wave+residue tile-selection for plain groupwise MoE GEMM | 2026-08-03 |  | block-scale, fp8, gemm |
| [#4324](../sources/prs/flashinfer/PR-4324.md) | MSA decode path improvements | 2026-08-03 |  | fp4, nvfp4, sort |
| [#4314](../sources/prs/flashinfer/PR-4314.md) | feat(cake_kda): share recurrent decode kernels across SM100 family | 2026-08-02 |  | attention, flash-attention, fp4 |
| [#4315](../sources/prs/flashinfer/PR-4315.md) | feat(topk): support compact page table transforms | 2026-08-02 |  | sort, topk |
| [#4313](../sources/prs/flashinfer/PR-4313.md) | feat(cake_kda): share recurrent prefill kernels across SM100 family | 2026-08-01 |  | attention, flash-attention, fp4 |
| [#4285](../sources/prs/flashinfer/PR-4285.md) | perf(moe): sync SM12x NVFP4 fused-MoE kernels to b12x HEAD | 2026-07-31 | double-buffering, kernel-fusion, pipeline-stages | block-scale, fp4, moe |
| [#4287](../sources/prs/flashinfer/PR-4287.md) | feat(cake_alpha_moe): add optimized Blackwell W8A8 expert up/down compute | 2026-07-31 | pipeline-stages, swizzling | attention, block-scale, fp4 |
| [#4290](../sources/prs/flashinfer/PR-4290.md) | feat(sm120): add native MXFP4 W4A4 fused MoE | 2026-07-31 |  | block-scale, fp4, gemm |
| [#4291](../sources/prs/flashinfer/PR-4291.md) | Upgrade CuTe DSL FMHA cubins | 2026-07-31 | swizzling | attention, block-scale, flash-attention |
| [#4293](../sources/prs/flashinfer/PR-4293.md) | chore: drop unused <nvrtc.h> includes from three launchers | 2026-07-31 |  | attention, flash-attention, fp8 |
| [#4295](../sources/prs/flashinfer/PR-4295.md) | perf(topk): skip output index sort for tie-break selection | 2026-07-31 |  | sort, topk |
| [#4302](../sources/prs/flashinfer/PR-4302.md) | feat(moe): expert parallelism for the SM12x W4A16 fused MoE | 2026-07-31 |  | fp4, moe, nvfp4 |
| [#4305](../sources/prs/flashinfer/PR-4305.md) | feat(gemm): port SM12x MXFP8 dense GEMM from b12x | 2026-07-31 | pipeline-stages | block-scale, fp4, gemm |
| [#4308](../sources/prs/flashinfer/PR-4308.md) | fix(moe): prepare MXFP8 MXFP4 profiler inputs | 2026-07-31 |  | block-scale, fp4, fp8 |
| [#4255](../sources/prs/flashinfer/PR-4255.md) | feat(moe): sync SM12x W4A16 fused MoE family to b12x HEAD | 2026-07-30 | kernel-fusion, swizzling | block-scale, fp4, fp8 |
| [#4259](../sources/prs/flashinfer/PR-4259.md) |  integrate SM120 VSA (Video Sparse Attention) block-sparse backend | 2026-07-30 | pipeline-stages, swizzling, tile-scheduling | attention, gemm, sparse-attention |
| [#4262](../sources/prs/flashinfer/PR-4262.md) | feat(cake_kda): add optimized B200 recurrent prefill backend | 2026-07-30 | swizzling | attention, flash-attention, fp4 |
| [#4263](../sources/prs/flashinfer/PR-4263.md) | fix(quantization): use 64-bit row addressing in per-token NVFP4 quantizer | 2026-07-30 | swizzling | fp4, moe, nvfp4 |
| [#4266](../sources/prs/flashinfer/PR-4266.md) | [feat] Add Blackwell cutedsl BF16 splitk dense gemm | 2026-07-30 | pipeline-stages | gemm, mbarrier, reduction |
| [#4274](../sources/prs/flashinfer/PR-4274.md) | feat(cake_tinygemm2): add CAKE-generated SM100/SM103 tinygemm2 variants with bit-identical outputs | 2026-07-30 | pipeline-stages, swizzling | gemm, mbarrier, reduction |
| [#4279](../sources/prs/flashinfer/PR-4279.md) | feat(cake_kda): add optimized B200 recurrent decode backend | 2026-07-30 |  | attention, flash-attention, fp4 |
| [#4280](../sources/prs/flashinfer/PR-4280.md) | SM 107 Reland + Merge Back from v0.6.16 Release Branch | 2026-07-30 |  | attention, flash-attention, fp4 |
| [#4282](../sources/prs/flashinfer/PR-4282.md) | feat(cake_softmax): add optimized Blackwell softmax | 2026-07-30 | pipeline-stages | attention, flash-attention, fp4 |
| [#4243](../sources/prs/flashinfer/PR-4243.md) | feat(kda): add fused Kimi K3 decode kernel | 2026-07-29 |  |  |
| [#4253](../sources/prs/flashinfer/PR-4253.md) | feat(gemm): sync mm_fp4 SM120 NVFP4 dense GEMM kernel to b12x HEAD | 2026-07-29 | pipeline-stages | block-scale, fp4, gemm |
| [#4192](../sources/prs/flashinfer/PR-4192.md) | fix(moe): serialize CuTe DSL autotune replay | 2026-07-28 |  | fp4, mla, moe |
| [#4199](../sources/prs/flashinfer/PR-4199.md) | fix(xqa): fix PDL load ordering and SM90 fp8 draft-mask dispatch | 2026-07-28 |  | attention, fp8 |
| [#4202](../sources/prs/flashinfer/PR-4202.md) | fix: support fp8 e5m2 output in rmsnorm_quant and fused_add_rmsnorm_quant | 2026-07-28 |  | fp8, quantization |
| [#4212](../sources/prs/flashinfer/PR-4212.md) | feat: paged KV cache support for the modular CuTe-DSL Blackwell prefill | 2026-07-28 | double-buffering, pipeline-stages, swizzling | attention, fp8, mbarrier |
| [#4161](../sources/prs/flashinfer/PR-4161.md) | [fix]fix xqa flaky test on spark | 2026-07-27 |  | mbarrier |
| [#4167](../sources/prs/flashinfer/PR-4167.md) | fix(norm): convert float2 to e4m3 directly in packed cast | 2026-07-27 | pipeline-stages | fp8, quantization |
| [#4169](../sources/prs/flashinfer/PR-4169.md) | feat(topk): support separate page table row starts | 2026-07-27 |  | sort, topk |
| [#4171](../sources/prs/flashinfer/PR-4171.md) | Revert PR 4122 | 2026-07-27 |  | attention, flash-attention, fp4 |
| [#4178](../sources/prs/flashinfer/PR-4178.md) | feat(mla): support packed low-head and variable-Q decode | 2026-07-27 |  | attention, flash-attention, fp8 |
| [#4186](../sources/prs/flashinfer/PR-4186.md) | fix(moe): handle CuTe DSL finalize output tails | 2026-07-27 | persistent-kernel | block-scale, fp4, moe |
| [#4152](../sources/prs/flashinfer/PR-4152.md) | [perf]  Optimize TRT-LLM routing for high-expert, high-top-k workloads | 2026-07-26 | pipeline-stages, warp-specialization | sort, topk |
| [#4122](../sources/prs/flashinfer/PR-4122.md) | Adds SM107 support | 2026-07-24 |  | attention, flash-attention, fp4 |
| [#4130](../sources/prs/flashinfer/PR-4130.md) | feat(sm120): fused MoE (SwiGLU) via moe_gemm is_gated for cute SM120 groupwise GEMM | 2026-07-24 | pipeline-stages, tile-scheduling | block-scale, fp8, gemm |
| [#4137](../sources/prs/flashinfer/PR-4137.md) | feat(xqa): ragged Q and per-row sliding-window masking for speculative decode | 2026-07-24 |  | attention, fp8 |
| [#4106](../sources/prs/flashinfer/PR-4106.md) | Add distribution-aware autotuning for TRT-LLM MoE | 2026-07-23 | kernel-fusion | fp4, fp8, moe |
| [#4113](../sources/prs/flashinfer/PR-4113.md) | feat(moe_ep): SM90 (Hopper) pull-style FP8 mega-MoE backend | 2026-07-23 | kernel-fusion, persistent-kernel, pipeline-stages | block-scale, clc, fp4 |
| [#4117](../sources/prs/flashinfer/PR-4117.md) | fix(gdn): support WY decode on SM121 | 2026-07-23 |  | mbarrier, tma |
| [#4095](../sources/prs/flashinfer/PR-4095.md) | fix(trtllm-gen): select dynamic-page decode kernels for MHA (numHeadsQPerKv == 1) | 2026-07-22 |  | attention, flash-attention, sparse-attention |
| [#4101](../sources/prs/flashinfer/PR-4101.md) | perf(moe_ep): CuTe-DSL 4.5.2 mainloop WAR — drop the 4.6.1 runtime floor | 2026-07-22 |  | fp4, moe, nvfp4 |
| [#4078](../sources/prs/flashinfer/PR-4078.md) | feat: add sm100 cp delta rule prefill | 2026-07-21 | pipeline-stages, swizzling | gemm, tcgen05, tma |
| [#4079](../sources/prs/flashinfer/PR-4079.md) | feat(moe_ep): MegaMoE framework integration ready: CUDA graph support, fused quant+stage launch, persistent knob cache, and prequantized weight packs | 2026-07-21 | kernel-fusion | fp4, moe, nvfp4 |
| [#4080](../sources/prs/flashinfer/PR-4080.md) | fix: Add missing nvfp4 sizing branch in getProfilerWorkspaces | 2026-07-21 |  | fp4, fp8, gemm |
| [#4063](../sources/prs/flashinfer/PR-4063.md) | perf(sm103): optimize NVFP4 epilogue stores and scaling | 2026-07-20 | epilogue-fusion | fp4, gemm, nvfp4 |
| [#4069](../sources/prs/flashinfer/PR-4069.md) | feat(moe_ep): add SM90 push FP8 mega-MoE backend for Hopper | 2026-07-20 | pipeline-stages | block-scale, fp4, fp8 |
| [#4072](../sources/prs/flashinfer/PR-4072.md) | feat: add optional normed-output (y_out) to add_rmsnorm_fp4quant | 2026-07-20 |  | attention, block-scale, fp4 |
| [#4046](../sources/prs/flashinfer/PR-4046.md) | fix(gemm): prevent out-of-bounds read in MaskedScheduler | 2026-07-18 |  | gemm, grouped-gemm |
| [#4048](../sources/prs/flashinfer/PR-4048.md) | feat(moe): support BF16 activations in CuTe DSL NVFP4 MoE | 2026-07-18 | persistent-kernel, pipeline-stages, warp-specialization | clc, fp4, gemm |
| [#4010](../sources/prs/flashinfer/PR-4010.md) | fix(moe): unify the NVFP4 profiler workspace predicate and fix gated fc1 SF sizing | 2026-07-17 |  | fp4, fp8, gemm |
| [#4027](../sources/prs/flashinfer/PR-4027.md) | MoE monokernel Bug fix, barrrier remove and kernel rewrite. | 2026-07-17 | double-buffering, pipeline-stages, swizzling | block-scale, fp8, mbarrier |
| [#4029](../sources/prs/flashinfer/PR-4029.md) | perf(gemm): Improve mm_fp4 cute-dsl autotune time via disk-cache and parallel compilation | 2026-07-17 |  | block-scale, fp4, gemm |
| [#4030](../sources/prs/flashinfer/PR-4030.md) | perf(msa): chunked top-k and in-kernel causal offsets for the SM12x indexer | 2026-07-17 |  | attention, fp4, nvfp4 |
| [#4038](../sources/prs/flashinfer/PR-4038.md) | perf(gemm): split-K, occupancy, and m=1 stream-GEMV decode tactics for mm_bf16_fp4 | 2026-07-17 | pipeline-stages | fp4, gemm, gemv |
| [#4039](../sources/prs/flashinfer/PR-4039.md) | feat(msa): accept K/V views split from a packed paged KV cache | 2026-07-17 |  | attention, fp4, fp8 |
| [#4040](../sources/prs/flashinfer/PR-4040.md) | feat: CuTe-DSL Fused SwiGLU NVFP4 Quantization | 2026-07-17 | swizzling | fp4, nvfp4, quantization |
| [#4009](../sources/prs/flashinfer/PR-4009.md) | feat(moe): add CuTe-DSL GeGLU-tanh and SiTU activations | 2026-07-16 |  | block-scale, fp4, gemm |
| [#3980](../sources/prs/flashinfer/PR-3980.md) | feat(moe_ep): restructure MegaMoE kernel sources into kernel_src + latest CuTeDSL MegaMoE kernels with improved performance | 2026-07-15 | kernel-fusion, persistent-kernel, pipeline-stages | block-scale, fp4, fp8 |
| [#3982](../sources/prs/flashinfer/PR-3982.md) | [feat] Add TRTLLM/SageAttention quantization routine | 2026-07-15 |  | attention, fp8, quantization |
| [#3984](../sources/prs/flashinfer/PR-3984.md) | perf: normalize autotuner nearest-profile cache keys | 2026-07-15 |  | fp4, fp8, mla |
| [#3952](../sources/prs/flashinfer/PR-3952.md) | CuTe-DSL modular prefill: sliding-window support + band-mask performance | 2026-07-14 | persistent-kernel, pipeline-stages | attention, flash-attention, fp8 |
| [#3955](../sources/prs/flashinfer/PR-3955.md) | feat: expose trtllm-gen block-sparse attention for decode | 2026-07-14 |  | attention, fp8, mla |
| [#3960](../sources/prs/flashinfer/PR-3960.md) | fix(gdn): compile SM12x CuteDSL kernels as sm_121a on DGX Spark | 2026-07-14 |  | moe, tma |
| [#3962](../sources/prs/flashinfer/PR-3962.md) | feat: fused FP8 quantization output for LayerNorm | 2026-07-14 | kernel-fusion | fp8, quantization |
| [#3975](../sources/prs/flashinfer/PR-3975.md) |  mamba checkpointing SSU: two-kernel split + ring-buffer cache for checkpointing SSU | 2026-07-14 | double-buffering, pipeline-stages, swizzling | block-scale, fp8, gemm |
| [#3976](../sources/prs/flashinfer/PR-3976.md) | feat(moe): add deterministic CuTe DSL NVFP4 finalize mode | 2026-07-14 | pipeline-stages | fp4, moe, nvfp4 |
| [#3943](../sources/prs/flashinfer/PR-3943.md) | Add CuTe DSL HCA backend for DeepSeek V4 sparse MLA | 2026-07-13 | persistent-kernel, tile-scheduling | attention, fp8, mla |
| [#3946](../sources/prs/flashinfer/PR-3946.md) | Fix the routing inconsistency for num_groups > 1 | 2026-07-13 |  |  |
| [#3932](../sources/prs/flashinfer/PR-3932.md) | fix(b12x): correct fp4 quantization numerics and add input_global_scale to decouple weight and activation scales | 2026-07-12 |  | block-scale, fp4, fp8 |
| [#3922](../sources/prs/flashinfer/PR-3922.md) | fix(cute_dsl): migrate off APIs removed in nvidia-cutlass-dsl 4.6 (keeps 4.5.x compat) | 2026-07-10 |  | attention, block-scale, fp8 |
| [#3888](../sources/prs/flashinfer/PR-3888.md) | fix(mla): enable cute-dsl/auto on SM103 + cluster-aware cutlass split_kv | 2026-07-09 |  | attention, mla, reduction |
| [#3889](../sources/prs/flashinfer/PR-3889.md) | Revert GDN prefill regression | 2026-07-09 |  | gemm, tcgen05, tmem |
| [#3890](../sources/prs/flashinfer/PR-3890.md) | fix: skip LogitsTransform on lanes beyond the split-KV chunk boundary in FA2 kernels | 2026-07-09 | persistent-kernel | attention |
| [#3891](../sources/prs/flashinfer/PR-3891.md) | Add FP8 groupwise MoE GEMM entry (cute SM120 backend) | 2026-07-09 | persistent-kernel, swizzling | block-scale, fp8, gemm |
| [#3901](../sources/prs/flashinfer/PR-3901.md) | feat(topk): Add top_k_varlen with GVR and radix backends for sparse-attention KV selection | 2026-07-09 |  | attention, sort, sparse-attention |
| [#3857](../sources/prs/flashinfer/PR-3857.md) | [feat] New CuTe DSL JIT kernels for FMHA: Dense & MXFP8 & NVFP4 formats | 2026-07-07 | persistent-kernel, swizzling, tile-scheduling | attention, block-scale, flash-attention |
| [#3858](../sources/prs/flashinfer/PR-3858.md) | feat: SM100 CUTLASS NVFP4 SVDQuant fused GEMM (mm_nvfp4_svdquant) | 2026-07-07 | pipeline-stages, swizzling | block-scale, fp4, fp8 |
| [#3861](../sources/prs/flashinfer/PR-3861.md) | feat(autotuner): Autotuner v2 (autotune_v2) — managed persistence, deployment-matched measurement, runner contract | 2026-07-07 |  | moe |
| [#3863](../sources/prs/flashinfer/PR-3863.md) | fix(attention): clamp CTA_TILE_Q for fp8 h512 ragged prefill on 99KB-smem GPUs | 2026-07-07 |  | attention, fp4, fp8 |
| [#3866](../sources/prs/flashinfer/PR-3866.md) | perf(gdn): optimize delta rule cp prefill for ultra low parallelism case | 2026-07-07 |  |  |
| [#3871](../sources/prs/flashinfer/PR-3871.md) | Fix: graph-safe uniform multi-token decode on FA2 tensor-core path | 2026-07-07 |  | attention |
| [#3874](../sources/prs/flashinfer/PR-3874.md) | feat(jit): JitSpec ABC + disk cache for JIT-compiled CuTe-DSL kernels | 2026-07-07 | swizzling | quantization, tma |
| [#3875](../sources/prs/flashinfer/PR-3875.md) | fix: preserve DeepSeek no-group sigmoid routing weights | 2026-07-07 |  | moe, topk |
| [#3847](../sources/prs/flashinfer/PR-3847.md) | [feat] Add cutedsl split K for MXFP8 dense gemm | 2026-07-06 | pipeline-stages, swizzling, tile-scheduling | block-scale, fp4, fp8 |
| [#3849](../sources/prs/flashinfer/PR-3849.md) | feat: Grouped-token MLA support for the TRTLLM-Gen FMHA backend. | 2026-07-06 | epilogue-fusion, tile-scheduling | attention, block-scale, flash-attention |
| [#3852](../sources/prs/flashinfer/PR-3852.md) | feat: MegaMoE Kernel integration in moe_ep | 2026-07-06 | kernel-fusion, persistent-kernel, pipeline-stages | block-scale, clc, fp4 |
| [#3840](../sources/prs/flashinfer/PR-3840.md) | fix(moe): fail loudly instead of IMA when no routing tier covers (numExperts, topK) | 2026-07-05 | pipeline-stages | fp4, gemm, moe |
| [#3838](../sources/prs/flashinfer/PR-3838.md) | fix(attention): correct SM120 NVFP4 qk_correction layout, row-sum reduction, and lse | 2026-07-04 |  | attention, flash-attention, fp4 |
| [#3822](../sources/prs/flashinfer/PR-3822.md) | Optimize FP4 V-scale dequant for h512 FA2 prefill | 2026-07-03 |  | attention, fp4, fp8 |
| [#3788](../sources/prs/flashinfer/PR-3788.md) | perf: optimize sm90 cp delta rule | 2026-07-01 |  |  |
| [#3794](../sources/prs/flashinfer/PR-3794.md) | feat(cute-dsl): sliding window and attention sinks for GQA decode (non-paged + paged) | 2026-07-01 |  | attention, flash-attention, reduction |
| [#3749](../sources/prs/flashinfer/PR-3749.md) | docs: add missing arg docs for output_scalar_scale and activation | 2026-06-29 |  | moe |
| [#3751](../sources/prs/flashinfer/PR-3751.md) | [feat] Optimize TRTLLMGEN MoE routing | 2026-06-29 |  | moe, topk |
| [#3756](../sources/prs/flashinfer/PR-3756.md) |   [CuTe DSL][MoE] Optimize PDL startup and balance GEMM2 partial-tile stores | 2026-06-29 | pipeline-stages, tile-scheduling | block-scale, gemm, grouped-gemm |
| [#3761](../sources/prs/flashinfer/PR-3761.md) | perf(moe): optimize CUTLASS fused MoE mem-bound kernels | 2026-06-29 |  | fp4, fp8, gemm |
| [#3766](../sources/prs/flashinfer/PR-3766.md) | perf(kda): optimize recurrent decode kernels | 2026-06-29 | double-buffering, pipeline-stages |  |
| [#3748](../sources/prs/flashinfer/PR-3748.md) | Add paged NVFP4 KV dequantization helper | 2026-06-28 |  | attention, fp4, fp8 |
| [#3737](../sources/prs/flashinfer/PR-3737.md) | Feat/cutedsl moe swiglu oai and use activation type to pass in | 2026-06-26 |  | block-scale, moe, tcgen05 |
| [#3738](../sources/prs/flashinfer/PR-3738.md) | perf: optimize MXFP4xBF16 & INT4xFP8 and add MXFP4xFP8 CUTLASS MoE backend for SM90 | 2026-06-26 | swizzling | block-scale, fp4, fp8 |
| [#3739](../sources/prs/flashinfer/PR-3739.md) | Enable Ampere FA2 large-head attention | 2026-06-26 |  | attention, fp4, nvfp4 |
| [#3740](../sources/prs/flashinfer/PR-3740.md) | Add NVFP4 slot-mapping paged KV append | 2026-06-26 |  | attention, fp4, nvfp4 |
| [#3741](../sources/prs/flashinfer/PR-3741.md) | Add caller-owned workspace sizing helper | 2026-06-26 |  | attention |
| [#3742](../sources/prs/flashinfer/PR-3742.md) | Improve GDN prefill perf by ~20-25% (mainloop efficiency) | 2026-06-26 | pipeline-stages | gemm, tcgen05, tmem |
| [#3744](../sources/prs/flashinfer/PR-3744.md) | feat(moe): add gelu_tanh and swiglu_oai activations to b12x NVFP4 MoE for SM12x | 2026-06-26 | pipeline-stages, swizzling | fp4, moe, nvfp4 |
| [#3746](../sources/prs/flashinfer/PR-3746.md) | feat: E2E MoE LoRA integration with bgmv backend | 2026-06-26 |  | moe |
| [#3717](../sources/prs/flashinfer/PR-3717.md) | Fix CuteDSL paged decode non-causal boundary mask | 2026-06-24 |  | attention |
| [#3694](../sources/prs/flashinfer/PR-3694.md) | feat(attention): FP8 KV cache support for Hopper SM90 MLA | 2026-06-23 | swizzling | attention, fp8, mla |
| [#3709](../sources/prs/flashinfer/PR-3709.md) | fix(moe): Fix unbounded weight-cache growth in b12x MoE | 2026-06-23 |  | moe |
| [#3684](../sources/prs/flashinfer/PR-3684.md) | feat(attention): asymmetric VO-split NVFP4 paged prefill (qk=512/vo=256) for Gemma-4 on SM120/121 | 2026-06-22 | swizzling | attention, block-scale, fp4 |
| [#3682](../sources/prs/flashinfer/PR-3682.md) | fix(attention): add LEFT_SLIDING_WINDOW drain loop to FP8 Hopper prefill (#3578) | 2026-06-20 | pipeline-stages, warp-specialization | attention, fp8, gemm |
| [#3659](../sources/prs/flashinfer/PR-3659.md) | feat: add sm120 cp delta rule | 2026-06-17 |  |  |
| [#3649](../sources/prs/flashinfer/PR-3649.md) | perf(gdn): make GDN kernels compilation batch-size agnostic (support dynamic batch shapes for vLLM integration) | 2026-06-16 |  |  |
| [#3655](../sources/prs/flashinfer/PR-3655.md) | feat(attn): Enable MiniMax Sparse Attention (MSA) for Consumer Blackwell GPUs (SM120/121) | 2026-06-16 | double-buffering, pipeline-stages, swizzling | attention, block-scale, fp4 |
| [#3640](../sources/prs/flashinfer/PR-3640.md) | Add SM120 NVFP4 attention JIT path | 2026-06-15 | pipeline-stages, warp-specialization | attention, fp4, gemm |
| [#3642](../sources/prs/flashinfer/PR-3642.md) | Add Relu2 + ungated MoE to CuteDSL MoE | 2026-06-15 |  | block-scale, gemm, grouped-gemm |
| [#3645](../sources/prs/flashinfer/PR-3645.md) | Add per-token NVFP4 quantization to CuTe DSL MoE | 2026-06-15 | kernel-fusion, pipeline-stages | block-scale, fp4, moe |
| [#3630](../sources/prs/flashinfer/PR-3630.md) | fix: fix tinygemm barrier bug | 2026-06-13 |  |  |
| [#3599](../sources/prs/flashinfer/PR-3599.md) | Accept uint8 workspaces in CUTE DSL MLA decode | 2026-06-12 |  | attention, mla |
| [#3608](../sources/prs/flashinfer/PR-3608.md) | fix: pass XQA NVFP4 scale-factor strides | 2026-06-12 |  | fp4, nvfp4 |
| [#3614](../sources/prs/flashinfer/PR-3614.md) | fix: make the cutlass MoE gemm profiler MXFP8-aware (autotune crash on MXFP8xMXFP8) | 2026-06-12 | warp-specialization | block-scale, fp8, gemm |
| [#3615](../sources/prs/flashinfer/PR-3615.md) | fix(topk): eliminate multi-CTA radix top-k stream hangs on SM120/SM121 | 2026-06-12 |  | sort, topk |
| [#3623](../sources/prs/flashinfer/PR-3623.md) | fix(sampling): terminate top-p search at adjacent float bounds | 2026-06-12 |  |  |
| [#3624](../sources/prs/flashinfer/PR-3624.md) | fix(sampling): fix shared-memory race and out-of-range token id in SamplingFromLogitsKernel | 2026-06-12 |  | reduction |
| [#3576](../sources/prs/flashinfer/PR-3576.md) | feat(attention): head_dim=512 support for attention prefill & decode for Gemma 4 on SM120/121 | 2026-06-11 |  | attention, fp8 |
| [#3597](../sources/prs/flashinfer/PR-3597.md) | feat: Add BF16_FP4 GEMM with cuDNN and CuTe-DSL backends for SM120/121 for W4A16 workloads | 2026-06-11 | persistent-kernel, pipeline-stages, swizzling | block-scale, fp4, fp8 |
| [#3560](../sources/prs/flashinfer/PR-3560.md) | perf(gemm): update mm_fp4 b12x SM120 NVFP4 dense GEMM kernel | 2026-06-10 |  | fp4, gemm, nvfp4 |
| [#3561](../sources/prs/flashinfer/PR-3561.md) |  feat(moe): add DSv4 hash-based MoE routing (MOE-01-HASH) | 2026-06-10 |  | moe, reduction, topk |
| [#3562](../sources/prs/flashinfer/PR-3562.md) | Add MXFP8 MoE GEMM entry (cute SM120 backend) | 2026-06-10 | swizzling | block-scale, fp8, gemm |
| [#3564](../sources/prs/flashinfer/PR-3564.md) | perf(moe): Enhance CuteDSL NVF4 MOE Perf | 2026-06-10 | pipeline-stages | block-scale, gemm, grouped-gemm |
| [#3544](../sources/prs/flashinfer/PR-3544.md) | feat: add BF16Q FP8KV transform-mode selection | 2026-06-09 | pipeline-stages | attention, flash-attention, fp8 |
| [#3546](../sources/prs/flashinfer/PR-3546.md) | docs: close v0.6.13 doc-check gaps + fix(moe) misleading topk_indices ICHECK message | 2026-06-09 |  | moe, quantization |
| [#3535](../sources/prs/flashinfer/PR-3535.md) | feat(moe_bgmv): direct decode fast-path for shrink (1.3-3.8x vs sliced kernel) | 2026-06-08 | kernel-fusion, pipeline-stages | moe, reduction |
| [#3542](../sources/prs/flashinfer/PR-3542.md) | perf(moe_bgmv): coalesced 128-bit loads for expand kernel (1.8–3× at batch≥256) | 2026-06-08 |  | moe, reduction |
| [#3529](../sources/prs/flashinfer/PR-3529.md) | Fix smem race in `FilteredTopK` overflow refinement | 2026-06-07 |  | sort, topk |
| [#3523](../sources/prs/flashinfer/PR-3523.md) | perf: remove dead cudaGetDeviceProperties in sm120 groupwise GEMM | 2026-06-06 |  | fp8, gemm |
| [#3524](../sources/prs/flashinfer/PR-3524.md) | perf: vectorize AppendPagedKVMlaCache to 128-bit access | 2026-06-06 |  | fp8, mla |
| [#3526](../sources/prs/flashinfer/PR-3526.md) | fix: keep HEAD_DIM 256 prefill within 64 KiB smem on SM75/SM70 | 2026-06-06 | swizzling | attention, fp4, fp8 |
| [#3518](../sources/prs/flashinfer/PR-3518.md) | FMHAv2 on SM120 for head_dim 256/512 + sliding-window masks | 2026-06-05 | warp-specialization | attention, flash-attention, fp8 |
| [#3502](../sources/prs/flashinfer/PR-3502.md) | feat(gdn): BF16 state recovery/decode kernel with per-request K and f… | 2026-06-04 |  |  |
| [#3501](../sources/prs/flashinfer/PR-3501.md) | [feat] Add gated tanh-GELU (GeluTanh) activation to CUTLASS fused MoE (GEMMA 4) | 2026-06-03 |  | gemm, moe |
| [#3490](../sources/prs/flashinfer/PR-3490.md) | Ameyn/fix fp32 mtp pool out indices | 2026-06-02 |  |  |
| [#3492](../sources/prs/flashinfer/PR-3492.md) | feat(moe): add SWIGLUSTEP activation to CUTLASS fused MoE | 2026-06-02 |  | fp4, fp8, moe |
| [#3473](../sources/prs/flashinfer/PR-3473.md) | NFC: replace deprecated API: cute.make_fragment | 2026-06-01 |  | block-scale, gemm |
| [#3476](../sources/prs/flashinfer/PR-3476.md) | Optimize MoE routing top-k reduction and non-power-of-two sorting | 2026-06-01 |  | moe, reduction, sort |
| [#3477](../sources/prs/flashinfer/PR-3477.md) | feat: add sm90 delta rule dsl prefill | 2026-06-01 | pipeline-stages, swizzling, warp-specialization | gemm, reduction, tma |
| [#3479](../sources/prs/flashinfer/PR-3479.md) | feat: add sm120 delta rule dsl prefill | 2026-06-01 | pipeline-stages, swizzling, warp-specialization | gemm, mbarrier, tma |
| [#3481](../sources/prs/flashinfer/PR-3481.md) | feat: add sm90 cp delta rule dsl | 2026-06-01 |  |  |
| [#3483](../sources/prs/flashinfer/PR-3483.md) | Use an environment variable to control the number of reserved SMs for overlapping in TRT-LLM fused MoE | 2026-06-01 |  | moe |
| [#3485](../sources/prs/flashinfer/PR-3485.md) | perf(attention): Speed up FP8 KV-cache prefill (FA2 BatchPrefill) by repacking K/V to BF16 in shared memory | 2026-06-01 | swizzling | attention, fp4, fp8 |
| [#3441](../sources/prs/flashinfer/PR-3441.md) | docs(attention): backfill missing/stale Attention/POD/cuDNN/CuteDSL APIs; restore single_prefill_with_kv_cache_return_lse | 2026-05-29 |  | attention, fp8, gemm |
| [#3443](../sources/prs/flashinfer/PR-3443.md) | docs(moe): close fused_moe / trtllm_*_moe / CuteDSL MoE doc gaps | 2026-05-29 |  | fp4, moe, nvfp4 |
| [#3448](../sources/prs/flashinfer/PR-3448.md) | Add CuTe DSL NVFP4 quantization with 4over6 FP16 scoring | 2026-05-29 | swizzling | fp4, moe, nvfp4 |
| [#3456](../sources/prs/flashinfer/PR-3456.md) | [docs] Backfill missing docstrings and decorators across kernels | 2026-05-29 |  | attention, gemm, quantization |
| [#3458](../sources/prs/flashinfer/PR-3458.md) | fix: use explicit .ptr on scalar struct fields in monolithic MLA decode to get cleaner logs | 2026-05-29 |  | attention, fp8, mla |
| [#3430](../sources/prs/flashinfer/PR-3430.md) | replace deprecated APIs: cute.make_fragment and cute.core.ThrMma | 2026-05-28 |  | attention, gemm |
| [#3439](../sources/prs/flashinfer/PR-3439.md) | Fix cross-warp race in checkpointing SSU kernel (mamba) | 2026-05-28 |  | fp8, quantization |
| [#3417](../sources/prs/flashinfer/PR-3417.md) | Add support for non-multiple VEC_COLS in fused_rmsnorm_silu for bf16/fp8 | 2026-05-27 |  | block-scale, fp4, fp8 |
| [#3424](../sources/prs/flashinfer/PR-3424.md) | Fused FP8 blockwise MoE megakernel For BS <= 8 | 2026-05-27 | double-buffering, pipeline-stages, swizzling | block-scale, fp8, mbarrier |
| [#3404](../sources/prs/flashinfer/PR-3404.md) | Remove excessive CuteDslMoEWrapper memory allocation | 2026-05-26 |  |  |
| [#3395](../sources/prs/flashinfer/PR-3395.md) | feat(attention): add SM120 sparse MLA kernels | 2026-05-23 | double-buffering, pipeline-stages, warp-specialization | attention, block-scale, fp8 |
| [#3392](../sources/prs/flashinfer/PR-3392.md) | fix(norm): widen address arithmetic to int64 for large contiguous inputs > 2**31 elements | 2026-05-22 |  | fp8, quantization |
| [#3393](../sources/prs/flashinfer/PR-3393.md) | fix: headDim=512 GQA decode (#3343) | 2026-05-22 |  | attention, flash-attention, reduction |
| [#3382](../sources/prs/flashinfer/PR-3382.md) | feat(moe): write routing_replay_out from custom routing kernels | 2026-05-21 |  | moe, topk |
| [#3384](../sources/prs/flashinfer/PR-3384.md) | feat(cute_dsl/moe): re-enable use_cold_l2_cache in CuteDslMoEWrapper TuningConfig | 2026-05-21 |  | moe |
| [#3387](../sources/prs/flashinfer/PR-3387.md) | Make cute dsl mxfp8/nvfp4 quantizer bitwise exact | 2026-05-21 |  | block-scale, fp4, fp8 |
| [#3360](../sources/prs/flashinfer/PR-3360.md) | feat: integrate cute-dsl Blackwell GQA decode into BatchDecodeWithPagedKVCacheWrapper | 2026-05-19 | pipeline-stages, warp-specialization | attention, flash-attention, fp8 |
| [#3340](../sources/prs/flashinfer/PR-3340.md) | fix(cute_dsl): avoid MoE wrapper runner reference cycle | 2026-05-16 |  | moe |
| [#3333](../sources/prs/flashinfer/PR-3333.md) | fix deprecation warnings from cute-dsl | 2026-05-15 |  | attention, block-scale, fp4 |
| [#3336](../sources/prs/flashinfer/PR-3336.md) | Replace SM120 W4A16 MoE kernels | 2026-05-15 | kernel-fusion, pipeline-stages, swizzling | block-scale, fp4, gemm |
| [#3324](../sources/prs/flashinfer/PR-3324.md) | checkpointing_ssu kernel: fused replay + conditional state-write for Mamba2 | 2026-05-14 | double-buffering, pipeline-stages, swizzling | attention, block-scale, fp8 |
| [#3328](../sources/prs/flashinfer/PR-3328.md) | feat(cute_dsl/moe): add `moe_output_memset_inplace` dense memset wrapper | 2026-05-14 |  | gemm, moe |
| [#3309](../sources/prs/flashinfer/PR-3309.md) | [Feat] Add num_heads < 128 support for mla decode kernel | 2026-05-13 | pipeline-stages | attention, fp8, mla |
| [#3296](../sources/prs/flashinfer/PR-3296.md) | Restore monolithic CuTe-DSL MLA decode alongside modular, gated by cute_dsl_impl= | 2026-05-12 | persistent-kernel, tile-scheduling | attention, fp8, mla |
| [#3302](../sources/prs/flashinfer/PR-3302.md) | Reject EP configurations in b12x MoE with a clear error | 2026-05-12 |  | moe |
| [#3285](../sources/prs/flashinfer/PR-3285.md) | Add mHC post mapping and pre big-fuse kernels | 2026-05-11 | kernel-fusion | reduction |
| [#3286](../sources/prs/flashinfer/PR-3286.md) | feat(cute_dsl/moe): deterministic balanced autotune profile inputs | 2026-05-11 |  | fp4, fp8, moe |
| [#3289](../sources/prs/flashinfer/PR-3289.md) | Optimize mxfp8 quantization on sm100 | 2026-05-11 |  | block-scale, fp4, fp8 |
| [#3281](../sources/prs/flashinfer/PR-3281.md) | feat(gemm): CuTeDSL "cute_ext" TGV backend as default for mm_bf16 / bmm_bf16 | 2026-05-10 | warp-specialization | gemm, tcgen05, tma |
| [#3276](../sources/prs/flashinfer/PR-3276.md) | fix(fmha_v2): fix FP8 V-scratch pipeline and varlen scheduler on SM90 | 2026-05-09 | persistent-kernel, pipeline-stages, warp-specialization | attention, flash-attention, fp8 |
| [#3268](../sources/prs/flashinfer/PR-3268.md) | Ameyn/gdn bf16 dispatcher and 4d pool | 2026-05-08 |  |  |
| [#3269](../sources/prs/flashinfer/PR-3269.md) | Add DeepSeek V4 sparse MLA TRTLLM-GEN kernels | 2026-05-08 |  | attention, flash-attention, fp8 |
| [#3271](../sources/prs/flashinfer/PR-3271.md) | feat(moe): add SM120 W4A16 b12x kernels | 2026-05-08 | pipeline-stages, swizzling | block-scale, fp4, fp8 |
| [#3259](../sources/prs/flashinfer/PR-3259.md) | Add dynamic tokens-per-page TRTLLM-GEN GQA kernels | 2026-05-07 |  | attention, flash-attention, mla |
| [#3249](../sources/prs/flashinfer/PR-3249.md) | Add BGMV MoE CUDA kernels for multi-LoRA | 2026-05-06 | pipeline-stages | fp8, gemm, grouped-gemm |
| [#3250](../sources/prs/flashinfer/PR-3250.md) |  integrate VSA (Video Sparse Attention) into block-sparse API | 2026-05-06 | pipeline-stages, swizzling, tile-scheduling | attention, clc, flash-attention |
| [#3252](../sources/prs/flashinfer/PR-3252.md) | fix(cute_dsl/moe): unbias autotuner profiling for tile_size enumeration | 2026-05-06 |  | moe |
| [#3235](../sources/prs/flashinfer/PR-3235.md) | Support Kimi K2.5 H64 CuTe DSL MLA decode | 2026-05-05 |  | attention, mla, reduction |
| [#3237](../sources/prs/flashinfer/PR-3237.md) | perf: optimize per-token nvfp4 quantization kernel. | 2026-05-05 | swizzling | fp4, nvfp4, quantization |
| [#3216](../sources/prs/flashinfer/PR-3216.md) | fix(cute_dsl/moe): make autotuner bucket configuration adapt to runtime input | 2026-05-01 |  | gemm, moe |
| [#3191](../sources/prs/flashinfer/PR-3191.md) | fix(sm12x): fix micro-kernel workspace sizing when routed_rows > num_local_experts | 2026-04-27 |  | moe, topk |
| [#3181](../sources/prs/flashinfer/PR-3181.md) | cute-dsl fmha prefill (cubin integration): remove front-padding, add attention_sink, and pdl support | 2026-04-26 |  | attention, flash-attention, fp8 |
| [#3185](../sources/prs/flashinfer/PR-3185.md) | feat: enable glm5 router gemm | 2026-04-26 |  | gemm, moe |
| [#3151](../sources/prs/flashinfer/PR-3151.md) | perf: Add no-bias path for tinygemm_bf16 | 2026-04-23 |  | gemm |
| [#3152](../sources/prs/flashinfer/PR-3152.md) | Integrate CUTLASS Small Tile N Blockscaled GEMMs/Grouped GEMMs for SM120 and SM121 | 2026-04-23 | swizzling | block-scale, fp4, gemm |
| [#3153](../sources/prs/flashinfer/PR-3153.md) | feat: Add support for LoRa delta in MOE mxint4 x bf16, MXFP8 & BF16 to trtllm backend | 2026-04-23 |  | block-scale, gemm, moe |
| [#3157](../sources/prs/flashinfer/PR-3157.md) | feat: DiT layer norm fusions for WAN: flashinfer.diffusion_ops | 2026-04-23 | swizzling | attention, block-scale, fp4 |
| [#3148](../sources/prs/flashinfer/PR-3148.md) | feat: RMSNorm + RoPE fusion for WAN: flashinfer.diffusion_ops.fused_qk_rmsnorm_rope | 2026-04-22 | kernel-fusion | attention, fp8, quantization |
| [#3129](../sources/prs/flashinfer/PR-3129.md) | feat: Enable FP8 (E4M3/E5M2) in concat_mla_k for optimize long-context prefill performance and refactor type dispatch for BF16/FP16 | 2026-04-21 |  | attention, flash-attention, fp4 |
| [#3097](../sources/prs/flashinfer/PR-3097.md) | Support NVFP4 KV for prefill and batch attention kernels | 2026-04-17 | swizzling | attention, block-scale, fp4 |
| [#3066](../sources/prs/flashinfer/PR-3066.md) | feat: Add b12x CuTe DSL fused MoE for SM120 | 2026-04-14 | kernel-fusion, persistent-kernel, pipeline-stages | block-scale, fp4, fp8 |
| [#3051](../sources/prs/flashinfer/PR-3051.md) | feat: Add backend="b12x" for mm_fp4 on SM120 | 2026-04-13 | pipeline-stages, swizzling, tile-scheduling | block-scale, fp4, gemm |
| [#3024](../sources/prs/flashinfer/PR-3024.md) | [feat] Add routing_replay_out support to MoE kernels and Python API | 2026-04-09 | kernel-fusion, pipeline-stages | block-scale, fp8, moe |
| [#3025](../sources/prs/flashinfer/PR-3025.md) | Prevent MoE autotuner buffer overflow on large token buckets | 2026-04-09 |  | fp4, fp8, gemm |
| [#3026](../sources/prs/flashinfer/PR-3026.md) | perf: Port TRT-LLM SM120/SM121 FP4 CUTLASS GEMM optimizations. Add PDL | 2026-04-09 | epilogue-fusion, persistent-kernel, pipeline-stages | block-scale, fp4, gemm |
| [#3027](../sources/prs/flashinfer/PR-3027.md) | [feat] Trtllm-gen Per-token Nvfp4 MoE | 2026-04-09 | swizzling | block-scale, fp4, fp8 |
| [#3014](../sources/prs/flashinfer/PR-3014.md) | perf: Optimize CUTLASS MoE helper kernels for small-batch decode workloads | 2026-04-08 |  | fp4, fp8, gemm |
| [#3001](../sources/prs/flashinfer/PR-3001.md) | [feat] Add blackwell GDN prefill kernel | 2026-04-07 | tile-scheduling | attention |
| [#3007](../sources/prs/flashinfer/PR-3007.md) | fix: use sym_int64 for strides in rmsnorm CuTe DSL kernels to prevent int32 overflow | 2026-04-07 |  | quantization |
| [#3008](../sources/prs/flashinfer/PR-3008.md) | feat: add PDL support to rmsnorm_fp4quant and add_rmsnorm_fp4quant CuTe DSL kernels | 2026-04-07 |  | fp4, quantization |
| [#2988](../sources/prs/flashinfer/PR-2988.md) | [Fmha] support nvfp4 output keepsMmaAb generation kernels | 2026-04-06 |  | attention, flash-attention, fp4 |
| [#2996](../sources/prs/flashinfer/PR-2996.md) | fix: tinygemm2 hang issue due to barrier sync | 2026-04-06 |  | mbarrier, reduction, tma |
| [#2962](../sources/prs/flashinfer/PR-2962.md) | Improved `simple` mamba SSU kernel  | 2026-04-02 | double-buffering, pipeline-stages | quantization, tma |
| [#2965](../sources/prs/flashinfer/PR-2965.md) | Add flashinfer.fused_rmsnorm_silu() with native kernel backend | 2026-04-02 |  | block-scale, fp4, fp8 |
| [#2944](../sources/prs/flashinfer/PR-2944.md) | feat: Add CuTe DSL grouped-gemm + combine fusion support | 2026-04-01 | persistent-kernel, pipeline-stages | block-scale, gemm, grouped-gemm |
| [#2945](../sources/prs/flashinfer/PR-2945.md) | fix: use float instead of double in sampling binary search to avoid FP64 bottleneck on SM103 | 2026-04-01 |  | topk |
| [#2914](../sources/prs/flashinfer/PR-2914.md) | feat: Add cuBLASLt backend for `mm_bf16` and enable multi-tactic autotuning for FP8/MXFP8 runners | 2026-03-30 |  | fp4, fp8, gemm |
| [#2913](../sources/prs/flashinfer/PR-2913.md) | [NVIDIA] fix(jit): enable GDC for CUTLASS fused MoE PDL — prevent random crashes on SM12x | 2026-03-29 |  | block-scale, fp4, fp8 |
| [#2908](../sources/prs/flashinfer/PR-2908.md) | feat(gdn): state checkpointing in chunk_gated_delta_rule | 2026-03-28 |  |  |
| [#2901](../sources/prs/flashinfer/PR-2901.md) | feat: add pdl support for cute dsl mla decode kernel support | 2026-03-27 |  | mla |
| [#2902](../sources/prs/flashinfer/PR-2902.md) | feat: add MXFP8 GEMM support for SM120 | 2026-03-27 | persistent-kernel, swizzling | block-scale, fp4, gemm |
| [#2904](../sources/prs/flashinfer/PR-2904.md) | perf: Optimize CuTe-DSL fp4 and fp8 quantization kernels | 2026-03-27 | pipeline-stages, swizzling | fp4, fp8, nvfp4 |
| [#2865](../sources/prs/flashinfer/PR-2865.md) | Mamba SSU: horizontal MTP kernel (+ DSTATE=96 support) | 2026-03-23 | double-buffering, pipeline-stages, swizzling | block-scale, mbarrier, tma |
| [#2836](../sources/prs/flashinfer/PR-2836.md) | [Fmha] Sparse MLA decode kernel selection heuristics | 2026-03-20 |  | attention, flash-attention, fp8 |
| [#2838](../sources/prs/flashinfer/PR-2838.md) | feat: Add CuTe-DSL backend for NVFP4 quantization | 2026-03-20 | pipeline-stages, swizzling, warp-specialization | fp4, fp8, gemm |
| [#2811](../sources/prs/flashinfer/PR-2811.md) | CuteDSL MoE fix redundant output buffer zeroing | 2026-03-18 | pipeline-stages | block-scale, fp4, moe |
| [#2805](../sources/prs/flashinfer/PR-2805.md) | [CuTe DSL] Add modular FMHA prefill and MLA decode attention kernels | 2026-03-17 | double-buffering, persistent-kernel, pipeline-stages | attention, flash-attention, fp8 |
| [#2809](../sources/prs/flashinfer/PR-2809.md) | feat(MoE): FP8 MoE per-channel quant support  | 2026-03-17 |  | fp8, gemm, moe |
| [#2792](../sources/prs/flashinfer/PR-2792.md) | feat: Support padding tokens with seqlen=0 for rope+quant+kv cache update fusion kernel | 2026-03-16 |  | attention, mla, quantization |
| [#2777](../sources/prs/flashinfer/PR-2777.md) | perf: Performance tune cute dsl RMSNorm variants | 2026-03-13 |  | fp8, mbarrier, quantization |
| [#2779](../sources/prs/flashinfer/PR-2779.md) | feat: FP8 output support for CUTLASS MLA paged attention | 2026-03-13 |  | attention, fp8, gemm |
| [#2752](../sources/prs/flashinfer/PR-2752.md) | [feat] Add air top-p algorithm | 2026-03-11 |  | sort, topk |
| [#2757](../sources/prs/flashinfer/PR-2757.md) | feat: Add FP4 KV cache quant/dequant kernels  | 2026-03-11 | swizzling | block-scale, fp4, fp8 |
| [#2738](../sources/prs/flashinfer/PR-2738.md) | Support for MXFP4 and NVFP4 group GEMMs on GeForce and Spark | 2026-03-10 | swizzling | block-scale, fp4, fp8 |
| [#2743](../sources/prs/flashinfer/PR-2743.md) | Add cute dsl mla decode op | 2026-03-10 | persistent-kernel, tile-scheduling | attention, fp8, mla |
| [#2744](../sources/prs/flashinfer/PR-2744.md) | [feat] Add 2048 experts and 32 Top K  | 2026-03-10 |  | moe, reduction, scan |
| [#2727](../sources/prs/flashinfer/PR-2727.md) | [gdn] support non-contiguous state for decoding | 2026-03-09 |  |  |
| [#2702](../sources/prs/flashinfer/PR-2702.md) | Add NVFP4 KV cache quantization support for SM100 | 2026-03-06 |  | attention, flash-attention, fp4 |
| [#2709](../sources/prs/flashinfer/PR-2709.md) | Mamba2 SSD Combined Forward Pass (Blackwell CuTe DSL Kernel) | 2026-03-06 | kernel-fusion, persistent-kernel, tile-scheduling | attention, scan, tma |
| [#2711](../sources/prs/flashinfer/PR-2711.md) | feat: Add DiT-oriented kernels where Qk (Bmm1) type can be reinterpreted into Int8 or BFloat16 | 2026-03-06 |  | attention, flash-attention |
| [#2700](../sources/prs/flashinfer/PR-2700.md) | Add varlen and speculative decoding support to selective state update | 2026-03-05 |  | quantization |
| [#2670](../sources/prs/flashinfer/PR-2670.md) | fix: reduce smem allocation for tinygemm2 kernel in SM120 | 2026-03-03 | pipeline-stages |  |
| [#2661](../sources/prs/flashinfer/PR-2661.md) | feat: implement deterministic topk | 2026-03-01 |  | scan, sort, topk |
| [#2653](../sources/prs/flashinfer/PR-2653.md) | [feat] trtllm-gen mxfp8 gemm | 2026-02-28 | swizzling | fp4, fp8, gemm |
| [#2660](../sources/prs/flashinfer/PR-2660.md) | feat: support mxfp4 & mxfp8 entrypoint for blackwell cutedsl dense gemm | 2026-02-28 | pipeline-stages, swizzling | block-scale, fp4, fp8 |
| [#2642](../sources/prs/flashinfer/PR-2642.md) | [fp8_blockwise]Fix int32 overflow in TRTLLM fused MoE activation kernel | 2026-02-26 | pipeline-stages | moe, topk |
| [#2645](../sources/prs/flashinfer/PR-2645.md) | int16 Block-Scaled State and Stochastic Rounding for SSU (mamba) | 2026-02-26 |  | block-scale, quantization, reduction |
| [#2629](../sources/prs/flashinfer/PR-2629.md) | fix: cute dsl nvfp4 moe routing index error | 2026-02-24 |  | fp4, moe, nvfp4 |
| [#2631](../sources/prs/flashinfer/PR-2631.md) | fix: add SM121 support to SM120 version guards | 2026-02-24 |  | gemm |
| [#2625](../sources/prs/flashinfer/PR-2625.md) | feat: Fuse shared experts into trtllm_gen moe (fp8) | 2026-02-23 | pipeline-stages | block-scale, fp8, moe |
| [#2618](../sources/prs/flashinfer/PR-2618.md) | perf(gdn): optimize MTP kernel with ILP rows and SMEM v caching | 2026-02-22 | pipeline-stages | reduction, tma |
| [#2610](../sources/prs/flashinfer/PR-2610.md) | Ameyn/gdn bf16 tolerance parallel reduction | 2026-02-21 |  | reduction |
| [#2605](../sources/prs/flashinfer/PR-2605.md) | [bugfix] Fix FilteredTopK overflow correctness | 2026-02-20 |  | sort, topk |
| [#2587](../sources/prs/flashinfer/PR-2587.md) | feat: trtllm tinygemm2 in flashinfer as bf16 routergemm | 2026-02-19 |  | gemm, mbarrier |
| [#2591](../sources/prs/flashinfer/PR-2591.md) | Mamba SSU: better automatic kernel selection + algorithm selection optionally exposed to the user. | 2026-02-19 |  | tma |
| [#2581](../sources/prs/flashinfer/PR-2581.md) | Implement `cutlass_fused_moe` mxfp8 | 2026-02-18 | swizzling | block-scale, fp4, fp8 |
| [#2572](../sources/prs/flashinfer/PR-2572.md) | feat(kda): add recurrent KDA decode kernel with per-K gating | 2026-02-17 | kernel-fusion | attention |
| [#2573](../sources/prs/flashinfer/PR-2573.md) | [Bug] Fix spark unit test failures for test_add_rmsnorm_fp4_quant_cute_dsl | 2026-02-17 |  |  |
| [#2564](../sources/prs/flashinfer/PR-2564.md) | fix: W4A8 autotune crash in cutlass_fused_moe profiler workspace | 2026-02-14 |  | fp4, fp8, moe |
| [#2540](../sources/prs/flashinfer/PR-2540.md) | feat: cute dsl mmfp4 for blackwell | 2026-02-11 | pipeline-stages, swizzling, tile-scheduling | block-scale, fp4, gemm |
| [#2520](../sources/prs/flashinfer/PR-2520.md) | Support NVFP4 KV cache decode on SM120 | 2026-02-08 | swizzling | fp4, nvfp4, quantization |
| [#2521](../sources/prs/flashinfer/PR-2521.md) | Feat/gdn decode pooled | 2026-02-08 |  | attention, reduction |
| [#2509](../sources/prs/flashinfer/PR-2509.md) | perf: cache cudaGetDeviceProperties in gdn_prefill to avoid per-call overhead | 2026-02-06 |  |  |
| [#2498](../sources/prs/flashinfer/PR-2498.md) | Ameyn/gdn decode cutedsl kernel | 2026-02-05 |  | attention, reduction |
| [#2503](../sources/prs/flashinfer/PR-2503.md) | refactor: Port upstream CUTLASS fixes and refactor grouped_gemm_nt_masked GEMM module location | 2026-02-05 |  | block-scale, gemm |
| [#2477](../sources/prs/flashinfer/PR-2477.md) | feat: Add TRTLLM-Gen Skip-Softmax kernels for prefill and decode | 2026-02-03 |  | attention, flash-attention |
| [#2482](../sources/prs/flashinfer/PR-2482.md) | feat: Add valid_hidden_size and valid_intermediate_size params t… | 2026-02-03 |  | fp4, gemm, moe |
| [#2460](../sources/prs/flashinfer/PR-2460.md) | perf: add fp4 GEMM tile configs and streamK scheduler for SM120 | 2026-02-02 | stream-k, tile-scheduling | fp4, gemm |
| [#2462](../sources/prs/flashinfer/PR-2462.md) | feat: Support Fused MoE non gated Relu2 NVFP4 & FP8 and support Nemotron, fixed | 2026-02-02 |  | fp4, fp8, moe |
| [#2464](../sources/prs/flashinfer/PR-2464.md) | feat: Add MXFP8 GEMM mm_mxfp8 (cutlass) | 2026-02-02 | persistent-kernel, swizzling | block-scale, fp4, fp8 |
| [#2456](../sources/prs/flashinfer/PR-2456.md) | fix: fix illegal memory access for NaN input in sampling kernels | 2026-01-31 |  |  |
| [#2443](../sources/prs/flashinfer/PR-2443.md) | Add cute-dsl backends to mxfp[8,4]_quantization for future refactor | 2026-01-30 | swizzling | fp4, fp8, nvfp4 |
| [#2444](../sources/prs/flashinfer/PR-2444.md) | MTP for mamba  | 2026-01-30 | pipeline-stages, swizzling | gemm, tma |
| [#2446](../sources/prs/flashinfer/PR-2446.md) | feat: Add TRTLLM fmha_v2 library for SM90 attention with Skip-Softmax  | 2026-01-30 | kernel-fusion, swizzling | attention, flash-attention, fp8 |
| [#2432](../sources/prs/flashinfer/PR-2432.md) | fix: Sampling: CUDA Graph fix | 2026-01-29 |  |  |
| [#2441](../sources/prs/flashinfer/PR-2441.md) | fix: Fix NaN output in mxfp8_quantize for very small input values | 2026-01-29 |  | quantization |
| [#2428](../sources/prs/flashinfer/PR-2428.md) | refactor: refactoring cuda code to cute-dsl (part 1) | 2026-01-28 |  | fp8, quantization |
| [#2421](../sources/prs/flashinfer/PR-2421.md) | refactor: simplify fp4 rmsnorm | 2026-01-27 |  | fp4, fp8, mbarrier |
| [#2422](../sources/prs/flashinfer/PR-2422.md) | refactor: reduce hopper's gdn prefill compilation time and fix docstring. | 2026-01-27 |  |  |
| [#2415](../sources/prs/flashinfer/PR-2415.md) | Remove cudaMalloc/Free in GDN prefill kernel | 2026-01-25 |  | tma |
| [#2405](../sources/prs/flashinfer/PR-2405.md) | perf: improve gdn decode cute-dsl kernels | 2026-01-23 | pipeline-stages | reduction |
| [#2398](../sources/prs/flashinfer/PR-2398.md) | feat: cuteDSL fp4 moe for better DSR1 performance. | 2026-01-22 |  | fp4, fp8, moe |
| [#2395](../sources/prs/flashinfer/PR-2395.md) | feat: Add output_both_sf_layouts option to add_rmsnorm_fp4quant API | 2026-01-21 | swizzling | block-scale, fp4, nvfp4 |
| [#2378](../sources/prs/flashinfer/PR-2378.md) | bugfix: hotfix of PR 2366 (mamba kernel) | 2026-01-20 |  |  |
| [#2380](../sources/prs/flashinfer/PR-2380.md) | fix: ensure each CTA processes full numHeadsQPerKv for trtllm decode kernel | 2026-01-20 |  | attention, flash-attention |
| [#2385](../sources/prs/flashinfer/PR-2385.md) | fix: In-place Residual Update for add_rmsnorm_fp4quant | 2026-01-20 |  | fp4, quantization |
| [#2387](../sources/prs/flashinfer/PR-2387.md) | A Blackwell-optimized version of selective_state_update (mamba) | 2026-01-20 | pipeline-stages | reduction, tma |
| [#2370](../sources/prs/flashinfer/PR-2370.md) | feat: [Qwen3-Next] Add Cute DSL GDN decode kernel and  tests | 2026-01-18 | pipeline-stages, swizzling | attention, reduction, tma |
| [#2366](../sources/prs/flashinfer/PR-2366.md) | Enable fp16/bf16/f32 support for selective_state_update (mamba) | 2026-01-16 |  | tma |
| [#2343](../sources/prs/flashinfer/PR-2343.md) | Optimize quantization function in large problem size | 2026-01-13 | swizzling, warp-specialization | block-scale, fp4, fp8 |
| [#2327](../sources/prs/flashinfer/PR-2327.md) | [perf] Improve gemm_fp8_nt_groupwise (cutlass backend) by 10-40% for batch sizes <= 32 | 2026-01-11 |  | fp8, gemm, tcgen05 |
| [#2328](../sources/prs/flashinfer/PR-2328.md) | fix: guard batchWarpReduceSum with ENABLE_FP8 to fix compilation without FP8 | 2026-01-11 |  | fp8 |
| [#2325](../sources/prs/flashinfer/PR-2325.md) | bugfix: fix multi-cta top-k implementation when k value is different for different row | 2026-01-10 |  | sort, topk |
| [#2323](../sources/prs/flashinfer/PR-2323.md) | [ML3] Optimized Router Gemm | 2026-01-09 |  | gemm, moe |
| [#2308](../sources/prs/flashinfer/PR-2308.md) | Fix: FilteredTopKUnifiedKernel read value out of length | 2026-01-08 |  | topk |
| [#2303](../sources/prs/flashinfer/PR-2303.md) | [Perf][Feature] Add SM103-specific schedulers for NVFP4 CUTLASS kernels | 2026-01-07 | persistent-kernel | fp4, gemm, nvfp4 |
| [#2304](../sources/prs/flashinfer/PR-2304.md) | feat: Support Fused MoE non gated Relu2 NVFP4 & FP8 and support Nemotron | 2026-01-07 |  | fp4, fp8, gemm |
| [#2301](../sources/prs/flashinfer/PR-2301.md) | Selective State Update kernel (mamba) | 2026-01-06 |  | tma |
| [#2279](../sources/prs/flashinfer/PR-2279.md) | [WIP] Refactor: simplify torch -> cute-dsl boilerplate and enable tvm-ffi for cute-dsl kernels | 2026-01-01 | swizzling | fp4 |
| [#2276](../sources/prs/flashinfer/PR-2276.md) | feat: add GDN Attention | 2025-12-31 |  | attention, gemm |
| [#2265](../sources/prs/flashinfer/PR-2265.md) | [TRTLLM-Gen Fmha] add optimized trtllm-gen decode kernels for high throughput + speculative decoding | 2025-12-24 |  | attention, flash-attention, mla |
| [#2260](../sources/prs/flashinfer/PR-2260.md) | fix: Add global scale support and optional output allocation for RMSNorm+FP4Quant fusion kernels | 2025-12-23 | swizzling | block-scale, fp4, nvfp4 |
| [#2255](../sources/prs/flashinfer/PR-2255.md) | fix: support int64 IdType for RoPE part argument in `rope_quantize_fp8_append_paged_kv_cache` | 2025-12-22 |  |  |
| [#2243](../sources/prs/flashinfer/PR-2243.md) | feat: RMSNorm/Fused RMSNorm + FP8 Quantization kernels | 2025-12-19 |  | fp8, quantization |
| [#2244](../sources/prs/flashinfer/PR-2244.md) | Remove cudaStreamSynchronize from gemm_groupwise_sm120.cuh for CUDA graph compatibility | 2025-12-19 |  | gemm |
| [#2237](../sources/prs/flashinfer/PR-2237.md) | [feat] Integrate SGLang concat_mla_k kernel into flashinfer | 2025-12-18 |  | attention, mla |
| [#2233](../sources/prs/flashinfer/PR-2233.md) | feat: Fused RMSNorm + FP4 Quantization Kernels in CuTe-DSL | 2025-12-17 | kernel-fusion, swizzling | block-scale, fp4, fp8 |
| [#2215](../sources/prs/flashinfer/PR-2215.md) | feat: further optimize top-k and add fused top-k page construction kernels for DSA | 2025-12-13 |  | sort, topk |
| [#2159](../sources/prs/flashinfer/PR-2159.md) | feat: MxInt4 x Bf16 TRT-LLM Gen MoE support | 2025-12-02 |  | block-scale, gemm, moe |
| [#2149](../sources/prs/flashinfer/PR-2149.md) | enable sm103 moe dsl backend | 2025-11-28 |  | block-scale, moe |
| [#2142](../sources/prs/flashinfer/PR-2142.md) | feat: TRTLLM FMHAv2 backend for ctx attention | 2025-11-25 |  | attention, flash-attention, fp8 |
| [#2138](../sources/prs/flashinfer/PR-2138.md) | feat: add trtllm-gen per-tensor sparseMla kernels. | 2025-11-24 |  | attention, flash-attention, mla |
| [#2131](../sources/prs/flashinfer/PR-2131.md) | make DeepGEMM swapAB available for linear gemm SM90 | 2025-11-22 |  | block-scale, fp8, gemm |
| [#2126](../sources/prs/flashinfer/PR-2126.md) | fix flaky xqa test | 2025-11-21 |  | attention |
| [#2119](../sources/prs/flashinfer/PR-2119.md) | perf: bunch of features and optimizations for top-k (sampling + sparse attention) | 2025-11-20 | double-buffering | attention, reduction, sort |
| [#2109](../sources/prs/flashinfer/PR-2109.md) | feat: support more head dim in RoPE kernel | 2025-11-19 |  |  |
| [#2110](../sources/prs/flashinfer/PR-2110.md) | add tensor scale input for xqa | 2025-11-19 |  | attention, fp8, quantization |
| [#2111](../sources/prs/flashinfer/PR-2111.md) | refactor: update fa3 codebase and fix hopper unittest [part 1] | 2025-11-19 | double-buffering | attention, fp8, quantization |
| [#2114](../sources/prs/flashinfer/PR-2114.md) | feature: make the LSE returned by MLA support base 2 or e  #2113 | 2025-11-19 |  | attention, mla |
| [#2105](../sources/prs/flashinfer/PR-2105.md) | enable xqa speculative decoding | 2025-11-18 |  | attention |
| [#2090](../sources/prs/flashinfer/PR-2090.md) | refactor: pass hopper deepgemm include directory through python | 2025-11-14 |  | moe |
| [#2092](../sources/prs/flashinfer/PR-2092.md) | perf: TRT-LLM Gen finalize kernel optimization | 2025-11-14 |  | moe, topk |
| [#2079](../sources/prs/flashinfer/PR-2079.md) | [Feature] Support batch prefill for POD Attention | 2025-11-12 |  | attention |
| [#2081](../sources/prs/flashinfer/PR-2081.md) | enable xqa fp8 output | 2025-11-12 |  | fp8 |
| [#2070](../sources/prs/flashinfer/PR-2070.md) | feat: BF16 GEMM using CUTLASS backend for SM100 | 2025-11-10 |  | gemm |
| [#2058](../sources/prs/flashinfer/PR-2058.md) | perf: Optimize helper max/minmax function in sampling.cuh | 2025-11-07 |  | reduction |
| [#2062](../sources/prs/flashinfer/PR-2062.md) | Fix: several bugs/issues with trtllm-gen attention kernels.  | 2025-11-07 |  | attention, flash-attention, mla |
| [#2063](../sources/prs/flashinfer/PR-2063.md) | perf: TRT-LLM MoE Block-FP8 activation optimization | 2025-11-07 |  | block-scale, fp8, moe |
| [#2051](../sources/prs/flashinfer/PR-2051.md) | Add support for topkPacked input in block-level renormalize | 2025-11-06 |  |  |
| [#2053](../sources/prs/flashinfer/PR-2053.md) | feat: add xqa mla backend | 2025-11-06 |  | fp8, mla |
| [#2044](../sources/prs/flashinfer/PR-2044.md) | perf: improve sampling/mask/softmax performance (part 1/2) | 2025-11-05 |  | reduction, sort, topk |
| [#2047](../sources/prs/flashinfer/PR-2047.md) | Rebase FP8 SM100 Cutlass FMHA Attention to main (original PR#1238) | 2025-11-05 |  | attention, flash-attention, fp8 |
| [#2049](../sources/prs/flashinfer/PR-2049.md) | [BUG] Fix trtllm-gen fp4 moe renormalize routing | 2025-11-05 |  | fp4, moe, quantization |
| [#2033](../sources/prs/flashinfer/PR-2033.md) | use scalar for kv_scale in xqa | 2025-11-04 |  | fp8 |
| [#2037](../sources/prs/flashinfer/PR-2037.md) | feat: Add flashinfer.rope.rope_quantize_fp8_append_paged_kv_cache (fused RoPE + Q + KV cache, supports MLA/GQA/MHA)  | 2025-11-04 |  | attention, fp8, mla |
| [#2025](../sources/prs/flashinfer/PR-2025.md) | perf: Speed up fp4 quantization for small batch with swizzling for cutlass MoE | 2025-11-03 | swizzling | block-scale, fp4, moe |
| [#2028](../sources/prs/flashinfer/PR-2028.md) | [NVIDIA] Thor & Spark Support | 2025-11-03 |  |  |
| [#2019](../sources/prs/flashinfer/PR-2019.md) | [DSV3] Optimized Router Gemm | 2025-10-31 |  | gemm, reduction |
| [#2020](../sources/prs/flashinfer/PR-2020.md) | update trtllm cutlass moe  | 2025-10-31 | epilogue-fusion, swizzling | block-scale, fp4, fp8 |
| [#2014](../sources/prs/flashinfer/PR-2014.md) | [feat] Refactor trtllmgen MOE and add Bf16 trtllmgen moe | 2025-10-30 |  | fp4, fp8, moe |
| [#2001](../sources/prs/flashinfer/PR-2001.md) | feat: add xqa backend and completes NHD/HND coverage for trtllm-gen/xqa backend | 2025-10-29 |  | attention, fp8 |
| [#1994](../sources/prs/flashinfer/PR-1994.md) | minor fix for xqa | 2025-10-28 |  | mla |
| [#1982](../sources/prs/flashinfer/PR-1982.md) | fix: correct PDL parameter handling in RopeQuantize kernel | 2025-10-26 |  | quantization |
| [#1969](../sources/prs/flashinfer/PR-1969.md) | feat: enable deepgemm jit for fp8 block-scale on SM90 | 2025-10-23 |  | block-scale, fp8 |
| [#1973](../sources/prs/flashinfer/PR-1973.md) | Feature: Add support for L40 FusedMoE in cutlass path | 2025-10-23 |  | fp4, fp8, gemm |
| [#1954](../sources/prs/flashinfer/PR-1954.md) | Feature: Support Relu2 activation in fused MoE | 2025-10-20 |  | fp8, gemm, moe |
| [#1955](../sources/prs/flashinfer/PR-1955.md) | Update trtllm-gen fused moe routing kernel and add more kernels | 2025-10-20 |  | block-scale, fp4, fp8 |
| [#1926](../sources/prs/flashinfer/PR-1926.md) | Add layernorm op for inputs of mixed dtype | 2025-10-14 |  | fp8, quantization, topk |
| [#1927](../sources/prs/flashinfer/PR-1927.md) | silu_and_mul nvfp4 quanization fusion rework | 2025-10-14 | swizzling | block-scale, fp4, gemm |
| [#1924](../sources/prs/flashinfer/PR-1924.md) | MLA RoPE + quantization fused kernel: shape generalization for MHA / GQA | 2025-10-13 | kernel-fusion | attention, fp8, mla |
| [#1882](../sources/prs/flashinfer/PR-1882.md) | feat: Add FP4 TRTLLM-Gen throughput MOE batched gemms | 2025-10-07 |  | fp4, gemm, moe |
| [#1878](../sources/prs/flashinfer/PR-1878.md) | Tune kernel compilation parameters for https://github.com/flashinfer-ai/flashinfer/pull/1850  | 2025-10-06 | pipeline-stages | attention |
| [#1865](../sources/prs/flashinfer/PR-1865.md) | Bugfix: fix o_strides in persistent kernel  | 2025-10-04 | persistent-kernel | attention |
| [#1850](../sources/prs/flashinfer/PR-1850.md) | Add head_dim=64 for blackwell cutlass fmha implementation | 2025-10-03 |  | attention, flash-attention |
| [#1826](../sources/prs/flashinfer/PR-1826.md) | Bugfix: Fix data hazard in persistent reduce | 2025-10-01 |  | attention |
| [#1829](../sources/prs/flashinfer/PR-1829.md) | feat: trtrllm-gen global scaled FP8 GEMMs | 2025-10-01 |  | fp8, gemm |
| [#1831](../sources/prs/flashinfer/PR-1831.md) | Update the routing for TRTLLMGEN to support kimi k2 and qwen | 2025-10-01 |  | moe, reduction, scan |
| [#1835](../sources/prs/flashinfer/PR-1835.md) | [Quantization] Add per-expert global scaling factor for fp4 batched quantize | 2025-10-01 |  | fp4, quantization |
| [#1819](../sources/prs/flashinfer/PR-1819.md) | feat:enable fp8 blockscale moe for fused cultass for sm90 | 2025-09-30 | pipeline-stages, swizzling | block-scale, fp8, gemm |
| [#1769](../sources/prs/flashinfer/PR-1769.md) | feat: add xqa fp8 mha and fp8 kv cache | 2025-09-25 | swizzling | attention, fp8, gemm |
| [#1774](../sources/prs/flashinfer/PR-1774.md) | Masked batch nvfp4 quantization | 2025-09-25 |  | block-scale, fp4, nvfp4 |
| [#1723](../sources/prs/flashinfer/PR-1723.md) | Fix DeepSeek quality for TRTLLM fused MoE routing | 2025-09-19 |  | moe |
| [#1724](../sources/prs/flashinfer/PR-1724.md) | bugfix: partially fix tests/test_trtllm_gen_fused_moe.py unit test failure | 2025-09-19 |  | topk |
| [#1725](../sources/prs/flashinfer/PR-1725.md) | TVM: support TVM binding for GroupedGemm | 2025-09-19 |  | fp8, gemm, grouped-gemm |
| [#1727](../sources/prs/flashinfer/PR-1727.md) | fix: put sampling kernel launch into macro | 2025-09-19 |  |  |
| [#1685](../sources/prs/flashinfer/PR-1685.md) | perf: Port the separate reduce kernel mode from trtllm. | 2025-09-16 |  | attention, flash-attention, fp8 |
| [#1696](../sources/prs/flashinfer/PR-1696.md) | Support Kimi-K2 for TRT: templatize number of experts | 2025-09-16 |  | gemm, grouped-gemm, sort |
| [#1682](../sources/prs/flashinfer/PR-1682.md) | Update TGV GEMM default kernel and TGV code cleanup. | 2025-09-15 |  | gemm |
| [#1677](../sources/prs/flashinfer/PR-1677.md) | Support output signals for overlapping for cutedsl gemm | 2025-09-14 |  | block-scale, gemm |
| [#1670](../sources/prs/flashinfer/PR-1670.md) | feat: Add `variant.OutputTransform()` to decode kernels | 2025-09-11 | epilogue-fusion | attention, fp8 |
| [#1675](../sources/prs/flashinfer/PR-1675.md) | feat: Batch-size invariant FA2 Prefill & Decode | 2025-09-11 |  | attention |
| [#1668](../sources/prs/flashinfer/PR-1668.md) | TGV GEMM as a BF16 backend alternative to cuBLAS | 2025-09-10 | swizzling, tile-scheduling | attention, fp8, gemm |
| [#1661](../sources/prs/flashinfer/PR-1661.md) | perf&bugfix: skip kv-tile computation out of sliding window in FA2; fix __syncthreads in mergestate | 2025-09-09 |  | attention |
| [#1631](../sources/prs/flashinfer/PR-1631.md) | bugfix: trtllm-gen fmha sm101 and sm100 compatibility | 2025-09-03 |  | attention, flash-attention |
| [#1622](../sources/prs/flashinfer/PR-1622.md) | bugfix: collect all modules to aot | 2025-09-02 |  |  |
| [#1614](../sources/prs/flashinfer/PR-1614.md) | bugfix: fix merge_attention_state in BatchAttention w/ gqa-group-size in Qwen family | 2025-09-01 |  | attention |
| [#1608](../sources/prs/flashinfer/PR-1608.md) | feat: initial support for SM103, SM110, SM120, SM121 | 2025-08-30 |  | attention, flash-attention |
| [#1609](../sources/prs/flashinfer/PR-1609.md) | feat: cutlass fp4 gemm bringup for SM120 & SM121 | 2025-08-30 | persistent-kernel | block-scale, fp4, gemm |
| [#1610](../sources/prs/flashinfer/PR-1610.md) | feat: cutlass fp8 gemm bringup for SM120 & SM121 | 2025-08-30 |  | fp8, gemm, grouped-gemm |
| [#1611](../sources/prs/flashinfer/PR-1611.md) | bugfix: fix fp4 quantization with 8x4 scale factor layout | 2025-08-30 | swizzling | fp4, quantization |
| [#1596](../sources/prs/flashinfer/PR-1596.md) | bugfix: fix fused-temperature softmax IMA issue | 2025-08-28 |  |  |
| [#1597](../sources/prs/flashinfer/PR-1597.md) | bugfix: fix the register overflow issue for topk renorm kernels on blackwell | 2025-08-28 |  | topk |
| [#1582](../sources/prs/flashinfer/PR-1582.md) | bugfix: Fix arg passing to TORCH_CHECK and TORCH_WARN macros | 2025-08-26 |  | topk |
| [#1567](../sources/prs/flashinfer/PR-1567.md) | Backend: downgrade trtllm-gen kernel to cuda-12 | 2025-08-25 |  | attention, flash-attention |
| [#1571](../sources/prs/flashinfer/PR-1571.md) | bugfix: fix cuda version guard macros | 2025-08-25 |  |  |
| [#1573](../sources/prs/flashinfer/PR-1573.md) | update trtllm-gen fp4 autotuner and routing | 2025-08-25 |  | fp4 |
| [#1559](../sources/prs/flashinfer/PR-1559.md) | bugfix: fix persistent attention kernel correctness on blackwell | 2025-08-24 |  | attention |
| [#1565](../sources/prs/flashinfer/PR-1565.md) | fix: separate out fp4 lib into sm90 and sm100 versions, add oob checking in fused moe | 2025-08-24 |  | fp4, moe, quantization |
| [#1547](../sources/prs/flashinfer/PR-1547.md) | perf: replace cudaGetDeviceProperties with cudaDeviceGetAttribute | 2025-08-22 |  |  |
| [#1530](../sources/prs/flashinfer/PR-1530.md) | bugfix: Fix compile error for undefined swizzle enum. | 2025-08-21 | swizzling | quantization |
| [#1533](../sources/prs/flashinfer/PR-1533.md) | bugfix: Fix Persistent kernel precision for masked output  | 2025-08-21 | persistent-kernel | attention |
| [#1537](../sources/prs/flashinfer/PR-1537.md) | feat: Integrate TRTLLM varlen kernel for deepseek R1 prefill  | 2025-08-21 |  | attention, flash-attention |
| [#1518](../sources/prs/flashinfer/PR-1518.md) | backend: Refactor trtllm-gen fmha metainfo loading | 2025-08-20 |  | attention, flash-attention |
| [#1521](../sources/prs/flashinfer/PR-1521.md) | refactor fp4 masked gemm cute-dsl implementation and add manual cache | 2025-08-20 |  | block-scale, fp4, fp8 |
| [#1525](../sources/prs/flashinfer/PR-1525.md) | Add GeGLU support to trtllm-gen NVFP4 Fused MoE Kernel | 2025-08-20 |  | fp4, moe, nvfp4 |
| [#1503](../sources/prs/flashinfer/PR-1503.md) | feat: integrate xqa attention backend | 2025-08-18 | swizzling | attention, fp8, gemm |
| [#1509](../sources/prs/flashinfer/PR-1509.md) | bugfix: Fix stream handling in cutedsl gemm | 2025-08-18 |  | block-scale, gemm |
| [#1500](../sources/prs/flashinfer/PR-1500.md) | fix: Replace cub Max/Min with cuda::maximum/minimum for cuda 13 compatibility | 2025-08-16 |  | reduction |
| [#1498](../sources/prs/flashinfer/PR-1498.md) | feat: scaling at fp4 gemm epilogue | 2025-08-15 |  | block-scale, fp4, gemm |
| [#1483](../sources/prs/flashinfer/PR-1483.md) | perf: add fast path to TopPRenormProbKernel for top_p >= 1.0, significantly boosting SGLang workloads | 2025-08-14 |  |  |
| [#1488](../sources/prs/flashinfer/PR-1488.md) | fix: update cutedsl masked moe gemm | 2025-08-14 |  | block-scale, fp4, fp8 |
| [#1490](../sources/prs/flashinfer/PR-1490.md) | feat: Support fp8 qkv, fp16/bf16 out MHA for trtllm-gen. | 2025-08-14 |  | attention, flash-attention, fp8 |
| [#1481](../sources/prs/flashinfer/PR-1481.md) | Add python API for masked grouped gemm | 2025-08-13 |  | block-scale, gemm, grouped-gemm |
| [#1475](../sources/prs/flashinfer/PR-1475.md) | tuner: Trtllm-gen Fp4 MoE Autotunner | 2025-08-12 |  | fp4, fp8, moe |
| [#1445](../sources/prs/flashinfer/PR-1445.md) | Add alignment in MxFP8Quantization | 2025-08-10 | swizzling | block-scale, fp4, quantization |
| [#1446](../sources/prs/flashinfer/PR-1446.md) | Remove getEnvEnablePDL in favor of enable_pdl parameter | 2025-08-10 |  | attention, block-scale, flash-attention |
| [#1396](../sources/prs/flashinfer/PR-1396.md) | gpt-oss: Add MXFP8 x MXFP4 CUTLASS MOE for SM100 and BF16 x MXFP4 CUTLASS for SM90 + SwigluBias Activation | 2025-08-06 | swizzling | block-scale, fp4, fp8 |
| [#1397](../sources/prs/flashinfer/PR-1397.md) | feature: add cutlass as bmm_fp8 backend. | 2025-08-06 |  | fp8, gemm |
| [#1402](../sources/prs/flashinfer/PR-1402.md) | fix shared memory alignment conflict in sampling.cuh | 2025-08-06 |  |  |
| [#1389](../sources/prs/flashinfer/PR-1389.md) | GPT-OSS Support: Add Blackwell MoE mxfp4 implementation from TRTLLM and Attention Sink | 2025-08-05 | swizzling | attention, block-scale, fp4 |
| [#1376](../sources/prs/flashinfer/PR-1376.md) | bugfix: Add guard for fp4/fp8 related include headers | 2025-08-04 |  | fp4, fp8 |
| [#1371](../sources/prs/flashinfer/PR-1371.md) | bugfix: fixed cutlass fused moe usage of FP4QuantizationSFLayout::SWIZZLED | 2025-08-03 | swizzling | moe |
| [#1360](../sources/prs/flashinfer/PR-1360.md) | support trtllm-gen prefill fp4 output | 2025-07-31 |  | attention, flash-attention, fp4 |
| [#1355](../sources/prs/flashinfer/PR-1355.md) | feature: add fp4 mm using trtllm backend | 2025-07-30 | swizzling | fp4, quantization |
| [#1339](../sources/prs/flashinfer/PR-1339.md) | feat: Fused rope fp8 quantize kernel for MLA | 2025-07-28 |  | fp8, mla, quantization |
| [#1324](../sources/prs/flashinfer/PR-1324.md) | feat: Support logits_soft_cap for Persistent attn; fix kv split limit | 2025-07-25 |  | attention |
| [#1331](../sources/prs/flashinfer/PR-1331.md) | feat: masked layout fp4 gemm using cute-dsl | 2025-07-25 | tile-scheduling | block-scale, fp4, gemm |
| [#1320](../sources/prs/flashinfer/PR-1320.md) | Add blockwise-scaled FP8 GEMM via TRTLLM-Gen. | 2025-07-24 | swizzling | block-scale, fp4, fp8 |
| [#1322](../sources/prs/flashinfer/PR-1322.md) | feat: Add k_scale and v_scale to persistent attention  | 2025-07-24 |  | attention |
| [#1307](../sources/prs/flashinfer/PR-1307.md) | Fix the bug of the kernel-selection heuristic in trtllm-gen | 2025-07-23 |  | attention, flash-attention, mla |
| [#1305](../sources/prs/flashinfer/PR-1305.md) | [Feature] SM level profiler  | 2025-07-22 |  |  |
| [#1294](../sources/prs/flashinfer/PR-1294.md) | Update cutlass fp4 moe kernels | 2025-07-21 | swizzling | fp4, fp8, gemm |
| [#1296](../sources/prs/flashinfer/PR-1296.md) | add cutlass backend for mm_fp4 | 2025-07-21 | persistent-kernel, warp-specialization | fp4, gemm, grouped-gemm |
| [#1290](../sources/prs/flashinfer/PR-1290.md) | [fix] fix integer overflow in FA2 customized_mask & add buffer overflow warning. | 2025-07-19 |  | attention, quantization |
| [#1292](../sources/prs/flashinfer/PR-1292.md) | refactor: Improved metainfo for trtllm-gen fmha | 2025-07-19 |  | attention, flash-attention |
| [#1287](../sources/prs/flashinfer/PR-1287.md) | Bug fix: guard fp8 e8m0 and e2m1 compile  | 2025-07-18 |  | fp8, quantization |
| [#1289](../sources/prs/flashinfer/PR-1289.md) | refactor: refactor trtllm-gen attention kernel integration code | 2025-07-18 |  | attention, flash-attention, mla |
| [#1267](../sources/prs/flashinfer/PR-1267.md) | Bug fix: fix duplicate launch in POD | 2025-07-16 |  | attention |
| [#1251](../sources/prs/flashinfer/PR-1251.md) | Reduce the JIT compilation time of gen_gemm_sm100_module | 2025-07-14 |  | gemm |
| [#1240](../sources/prs/flashinfer/PR-1240.md) | Patch fp8 cubin availability | 2025-07-11 |  | fp8 |
| [#1241](../sources/prs/flashinfer/PR-1241.md) | feat: Support MXFP8 x MXFP4 CUTLASS grouped GEMM | 2025-07-11 | swizzling | fp4, gemm, grouped-gemm |
| [#1242](../sources/prs/flashinfer/PR-1242.md) | Add trtllm-gen attention mha kernel with FP8 Q/K/V and FP8 output | 2025-07-11 |  | attention, flash-attention, fp4 |
| [#1230](../sources/prs/flashinfer/PR-1230.md) | feat: Add non-causal cudnn prefill kernels | 2025-07-08 |  |  |
| [#1234](../sources/prs/flashinfer/PR-1234.md) | bugfix: support uint8_t for vec_t class template | 2025-07-08 |  | fp8 |
| [#1221](../sources/prs/flashinfer/PR-1221.md) | Enable cudnn decode and add tests for the cudnn decode kernel | 2025-07-07 |  | tma |
| [#1222](../sources/prs/flashinfer/PR-1222.md) | feat: add trtllm-gen mla cubin | 2025-07-07 |  | attention, flash-attention, mla |
| [#1227](../sources/prs/flashinfer/PR-1227.md) | Fix missing hash in the cudnn cubin path | 2025-07-07 |  | attention, flash-attention |
| [#1214](../sources/prs/flashinfer/PR-1214.md) | Feature/sm100 low latency nvfp4 kernels | 2025-07-04 | swizzling | block-scale, fp4, fp8 |
| [#1212](../sources/prs/flashinfer/PR-1212.md) | feat: trtllm-gen fp8 moe kernels | 2025-07-03 |  | block-scale, fp8, moe |
| [#1208](../sources/prs/flashinfer/PR-1208.md) | Fix the issue with auxillary kernel launch and grid dim calculation | 2025-07-02 |  |  |
| [#1206](../sources/prs/flashinfer/PR-1206.md) | [fix] fix BatchAttention CTA_TILE_KV mask issue | 2025-07-01 |  | attention |
| [#1198](../sources/prs/flashinfer/PR-1198.md) | bugfix: fix blackwell fmha hanging issue for empty kv_len | 2025-06-30 |  | attention, flash-attention |
| [#1200](../sources/prs/flashinfer/PR-1200.md) | [feat] optimize persistent batch attention perf. | 2025-06-30 |  | attention, reduction |
| [#1189](../sources/prs/flashinfer/PR-1189.md) | update trtllm-gen decode attention kernel launcher | 2025-06-28 |  | attention, flash-attention, mla |
| [#1178](../sources/prs/flashinfer/PR-1178.md) | bugfix: softmax NaN results caused by large -inf masks | 2025-06-25 |  | topk |
| [#1158](../sources/prs/flashinfer/PR-1158.md) | Add more logging to TRTLLM-GEN debug trace (NFC) | 2025-06-19 | tile-scheduling | attention, flash-attention |
| [#1153](../sources/prs/flashinfer/PR-1153.md) | feat: Fused temperature online softmax kernel | 2025-06-18 |  | reduction |
| [#1140](../sources/prs/flashinfer/PR-1140.md) | Fix FA2 and FA3 multi-item scoring and cuda illegal memory access error | 2025-06-12 |  | attention |
| [#1137](../sources/prs/flashinfer/PR-1137.md) | [feat] add unified batch attention w/ correctness tests. | 2025-06-11 | persistent-kernel, pipeline-stages, swizzling | attention, reduction |
| [#1116](../sources/prs/flashinfer/PR-1116.md) | hotfix: fix the blackwell fmha stream | 2025-06-06 |  | attention, flash-attention |
| [#1117](../sources/prs/flashinfer/PR-1117.md) | [Feature] Support PDL for batch Prefill and Decode | 2025-06-06 |  | attention, mla, quantization |
| [#1114](../sources/prs/flashinfer/PR-1114.md) | bugfix: Fix test and output shape of fp4 quantize | 2025-06-05 |  | fp4, gemm, quantization |
| [#1113](../sources/prs/flashinfer/PR-1113.md) | Add CUTLASS fused moe kernels from TensorRT-LLM. | 2025-06-04 | epilogue-fusion, pipeline-stages, swizzling | fp4, fp8, gemm |
| [#1106](../sources/prs/flashinfer/PR-1106.md) | bugfix: host-precomuted plan function for blackwell fmha | 2025-05-31 |  | attention, flash-attention, scan |
| [#1086](../sources/prs/flashinfer/PR-1086.md) | perf: accelerate blackwell grouped gemm | 2025-05-23 |  | gemm, grouped-gemm, moe |
| [#1087](../sources/prs/flashinfer/PR-1087.md) | bugfix: fix fp8 attention kernels aot compilation issue | 2025-05-23 |  | attention, fp8, quantization |
| [#1071](../sources/prs/flashinfer/PR-1071.md) | bugfix: adding lse output to blackwell fmha kernels | 2025-05-20 |  | attention, flash-attention |
| [#1072](../sources/prs/flashinfer/PR-1072.md) | bugfix: follow user-specified sm_scale for blackwell cutlass fmha | 2025-05-20 |  | attention, flash-attention |
| [#1059](../sources/prs/flashinfer/PR-1059.md) | Parameterize prefix mask call (needed by POD-Attention) | 2025-05-14 |  | attention |
| [#1054](../sources/prs/flashinfer/PR-1054.md) | Fix KV chunking for POD.  | 2025-05-13 |  | attention |
| [#1055](../sources/prs/flashinfer/PR-1055.md) | bugfix: temporally disable split-kv in blackwell mla | 2025-05-13 |  | attention, mla |
| [#1050](../sources/prs/flashinfer/PR-1050.md) | fix: top_k_mask_logits hangs on -inf inputs | 2025-05-09 |  |  |
| [#1051](../sources/prs/flashinfer/PR-1051.md) | [nvidia] Add Blackwell FMHA decode kernel from TRT-LLM | 2025-05-09 | persistent-kernel, tile-scheduling | attention, flash-attention, mla |
| [#1039](../sources/prs/flashinfer/PR-1039.md) | [nvidia] initial support for blackwell kernels | 2025-04-24 |  | attention, flash-attention, tma |
| [#1033](../sources/prs/flashinfer/PR-1033.md) | feat: add functional per-head FP8 quantization for FA3 | 2025-04-23 | pipeline-stages, tile-scheduling | attention, fp8, gemm |
| [#1035](../sources/prs/flashinfer/PR-1035.md) | feat: Softmax free sampling | 2025-04-23 |  | scan |
| [#1029](../sources/prs/flashinfer/PR-1029.md) | fix: add zero init for KV tiled copy | 2025-04-21 |  | attention |
| [#1025](../sources/prs/flashinfer/PR-1025.md) | feat: ragged tensor padding kernel for blackwell kernel alignment | 2025-04-20 |  | scan |
| [#1015](../sources/prs/flashinfer/PR-1015.md) | add multi-item scoring | 2025-04-11 | tile-scheduling | attention, quantization |
| [#1014](../sources/prs/flashinfer/PR-1014.md) | misc: fix instrument code for mla profiler | 2025-04-10 |  | attention, mla |
| [#1007](../sources/prs/flashinfer/PR-1007.md) | feat: update decode attention APIs | 2025-04-07 |  | attention |
| [#997](../sources/prs/flashinfer/PR-997.md) | 3rdparty: upgrade cutlass to 3.9 | 2025-04-03 |  | attention |
| [#991](../sources/prs/flashinfer/PR-991.md) | perf: prefetch page indices for mla kernel | 2025-03-31 |  | attention, mla |
| [#982](../sources/prs/flashinfer/PR-982.md) | SM-constraint-GEMM by triton persistent kernel | 2025-03-29 | persistent-kernel | gemm |
| [#983](../sources/prs/flashinfer/PR-983.md) | Triton `rms_norm` kernels | 2025-03-29 |  |  |
| [#974](../sources/prs/flashinfer/PR-974.md) | perf: dual pivot top-p/top-k renorm | 2025-03-26 |  | topk |
| [#969](../sources/prs/flashinfer/PR-969.md) | perf: Fix python API overhead when CUDAGraph is not enabled | 2025-03-23 |  |  |
| [#952](../sources/prs/flashinfer/PR-952.md) | perf: Use 2WG pipeline design for MLA implementation on Hopper | 2025-03-17 | pipeline-stages, swizzling | attention, mla, wgmma |
| [#945](../sources/prs/flashinfer/PR-945.md) | bugfix: fix potential issues of FA3 template loading nans for PageAttention | 2025-03-14 |  | attention |
| [#930](../sources/prs/flashinfer/PR-930.md) | feat: experimenta support of PDL | 2025-03-11 |  |  |
| [#913](../sources/prs/flashinfer/PR-913.md) | feat: flashinfer intra-kernel profiler | 2025-03-05 |  | attention, mla |
| [#901](../sources/prs/flashinfer/PR-901.md) | perf: tweak the pipeline design of mla kernel | 2025-02-27 | pipeline-stages | attention, mla |
| [#898](../sources/prs/flashinfer/PR-898.md) | perf: fix MLA split-k performance bug | 2025-02-25 |  | attention, mla |
| [#887](../sources/prs/flashinfer/PR-887.md) | perf: FlashAttention-3 style MLA PageAttention | 2025-02-23 | pipeline-stages, swizzling, warp-specialization | attention, flash-attention, mla |
| [#888](../sources/prs/flashinfer/PR-888.md) | feat - support mla kvcache store | 2025-02-23 |  | mla |
| [#869](../sources/prs/flashinfer/PR-869.md) | Naive Support for Hopper FP8 Prefill Kernel with Per-Head Quantization | 2025-02-18 | pipeline-stages, tile-scheduling | attention, flash-attention, fp8 |
| [#858](../sources/prs/flashinfer/PR-858.md) | Add POD-Attention to FlashInfer | 2025-02-17 | swizzling | attention |
| [#863](../sources/prs/flashinfer/PR-863.md) | perf: dynamic split-k for MLA | 2025-02-17 | swizzling | attention, mla |
| [#868](../sources/prs/flashinfer/PR-868.md) | bugfix: fix the behavior of MLA kernel when kv-length is 0 | 2025-02-17 |  | attention, mla |
| [#844](../sources/prs/flashinfer/PR-844.md) | perf: MLA decode kernel implemented by CuTe targeted to SM80 | 2025-02-14 | pipeline-stages, swizzling | attention, gemm, mla |
| [#821](../sources/prs/flashinfer/PR-821.md) | bugfix: bugfix on sm89 MLA | 2025-02-13 |  | attention, mla |
| [#810](../sources/prs/flashinfer/PR-810.md) | bugfix: mla page-attention kernel for different page sizes | 2025-02-12 |  | attention, mla |
| [#812](../sources/prs/flashinfer/PR-812.md) | feat: unlocking MLA for A100 | 2025-02-12 | swizzling | attention, mla |
| [#814](../sources/prs/flashinfer/PR-814.md) | feat: unlock MLA attention for sm89 (L40/L40s/4090) | 2025-02-12 | swizzling | attention, mla |
| [#804](../sources/prs/flashinfer/PR-804.md) | perf: memory efficient deepseek mla fused page-attention kernel | 2025-02-10 | pipeline-stages, swizzling | attention, mla |
| [#801](../sources/prs/flashinfer/PR-801.md) | feat: apply sm_scale at logits instead of q in FA2 template | 2025-02-09 |  | attention |
| [#799](../sources/prs/flashinfer/PR-799.md) | feat: support f32 attention output in FA2 template | 2025-02-08 |  | attention |
| [#793](../sources/prs/flashinfer/PR-793.md) | fix rope logic in mla decoding | 2025-02-07 |  | attention, mla |
| [#787](../sources/prs/flashinfer/PR-787.md) | bugfix: MLA decode should multiply sm_scale by math::log2e | 2025-02-05 |  | attention, mla |
| [#785](../sources/prs/flashinfer/PR-785.md) | bugfix: drop CTA_TILE_Q=32 | 2025-02-04 |  |  |
| [#776](../sources/prs/flashinfer/PR-776.md) | perf: refactor fa2 prefill template | 2025-02-03 |  | attention |
| [#774](../sources/prs/flashinfer/PR-774.md) | bugfix: Ensure Loop Termination by Enforcing IEEE-754 Compliance in Sampling Kernels | 2025-02-01 |  |  |
| [#765](../sources/prs/flashinfer/PR-765.md) | feat: support deepseek prefill attention shape | 2025-01-30 |  | attention, gemm, mla |
| [#754](../sources/prs/flashinfer/PR-754.md) | Change `apply_rope_with_cos_sin_cache` to accept `cos_sin_cache` | 2025-01-27 |  |  |
| [#728](../sources/prs/flashinfer/PR-728.md) | Align KV chunk size binary search with actual KV chunk splitting. | 2025-01-09 |  | attention |
| [#718](../sources/prs/flashinfer/PR-718.md) | bugfix: FusedAddRMSNorm kernels might require more than 48KB shared memory when d is large. | 2025-01-06 |  |  |
| [#714](../sources/prs/flashinfer/PR-714.md) | perf: fix the iteration bound of SWA in FA2 prefill template | 2025-01-03 |  | attention |

<a id="pytorchpytorch"></a>
## pytorch/pytorch
317 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#201127](../sources/prs/pytorch/PR-201127.md) | flex_gemm: compose output transforms with captures, aux outputs, and varlen-M reductions | 2026-10-16 |  | gemm, grouped-gemm, moe |
| [#201085](../sources/prs/pytorch/PR-201085.md) | cutedsl: lower division by a constant to a reciprocal multiply | 2026-10-15 |  | gemm, moe |
| [#201087](../sources/prs/pytorch/PR-201087.md) | flex_gemm: read and write interleaved two-lane epilogue tensors | 2026-10-15 |  | gemm, reduction, tma |
| [#200710](../sources/prs/pytorch/PR-200710.md) | [quack] Stop relying on the process-wide mixed_constexpr_if AST patch | 2026-10-13 |  | gemm |
| [#200591](../sources/prs/pytorch/PR-200591.md) | reland [inductor-perf] allow fusion into template epilogue inputs. (#198809) (#200591) | 2026-10-12 | epilogue-fusion |  |
| [#200593](../sources/prs/pytorch/PR-200593.md) | Launch only the warps a narrow row needs in vectorized layer/RMS norm forward | 2026-10-12 |  | reduction |
| [#200499](../sources/prs/pytorch/PR-200499.md) | [module-level kernels] inductor: define user-defined Triton kernels at module level too | 2026-10-10 |  | attention, tma |
| [#200328](../sources/prs/pytorch/PR-200328.md) | [ROCm] Speed up radixSelect with a register-resident path | 2026-10-08 | double-buffering | reduction, sort, topk |
| [#199986](../sources/prs/pytorch/PR-199986.md) | Vectorize inner-contiguous strided CUDA copies with 16-byte chunks | 2026-10-07 |  | attention |
| [#200046](../sources/prs/pytorch/PR-200046.md) | Avoid redundant zeroing in CUDA max_pool2d backward | 2026-10-07 |  |  |
| [#200164](../sources/prs/pytorch/PR-200164.md) | [CUDA][avgpool2d] Scope sm10x launch-bounds fix to architecture, not dtype | 2026-10-07 |  | reduction |
| [#200179](../sources/prs/pytorch/PR-200179.md) | [FSDP2] Fold _reduce_scatter_copy_in_ into chunk_cat_mixed_dtype | 2026-10-07 | kernel-fusion |  |
| [#200202](../sources/prs/pytorch/PR-200202.md) | [ROCm] Enable triton rocshmem device reduction | 2026-10-07 |  | reduction |
| [#199947](../sources/prs/pytorch/PR-199947.md) | Make CUDA median(dim) deterministic among tied values | 2026-10-06 |  | reduction |
| [#199969](../sources/prs/pytorch/PR-199969.md) | Make _CudaDeviceProperties clock rates query their own device | 2026-10-06 |  |  |
| [#199972](../sources/prs/pytorch/PR-199972.md) | [symm_mem]: Let the NCCL tensor-only ops take a group, and expose a handle's group | 2026-10-06 |  |  |
| [#199732](../sources/prs/pytorch/PR-199732.md) | Fix CUDA split_with_sizes_copy crash on empty inputs | 2026-10-05 |  |  |
| [#199775](../sources/prs/pytorch/PR-199775.md) | Fix missing cp.async drain in memory-efficient attention backward kernel | 2026-10-05 |  | attention, gemm |
| [#199848](../sources/prs/pytorch/PR-199848.md) | [ROCm] Batch the single-block topk gather and shorten its warp scan | 2026-10-05 | double-buffering | scan, sort, topk |
| [#199710](../sources/prs/pytorch/PR-199710.md) | Extend tiled CUDA transpose copy to batched and N-dim permutes | 2026-10-04 |  |  |
| [#199425](../sources/prs/pytorch/PR-199425.md) | [ROCm] Make single-block topk gather deterministic | 2026-10-02 | double-buffering | scan, topk |
| [#199427](../sources/prs/pytorch/PR-199427.md) | [triton][3.8] Lazily load TLX registry options (#199427) | 2026-10-02 |  |  |
| [#199438](../sources/prs/pytorch/PR-199438.md) | [ROCm] Fix layer_norm vectorized chunk offset overflow | 2026-10-02 |  |  |
| [#199444](../sources/prs/pytorch/PR-199444.md) | [ROCm] Stop hipify from rewriting std::max/std::min to ::max/::min | 2026-10-02 |  | quantization, sort, topk |
| [#199472](../sources/prs/pytorch/PR-199472.md) | Use mutable_data_ptr in nested tensor kernels | 2026-10-02 |  |  |
| [#199479](../sources/prs/pytorch/PR-199479.md) | Remove unused dummy_mean_/dummy_var_ in Normalization.cuh | 2026-10-02 |  |  |
| [#199484](../sources/prs/pytorch/PR-199484.md) | [ROCm] Fix feature tile offset in coalesceValuesKernel | 2026-10-02 |  |  |
| [#199569](../sources/prs/pytorch/PR-199569.md) | Fix shared-memory race in embedding_backward_feature_kernel | 2026-10-02 |  |  |
| [#199594](../sources/prs/pytorch/PR-199594.md) | Fix CUDA SDPA grid overflow for large batches and heads | 2026-10-02 |  | attention, flash-attention |
| [#199598](../sources/prs/pytorch/PR-199598.md) | Fix CUDA short-row scan launch configuration | 2026-10-02 |  |  |
| [#199154](../sources/prs/pytorch/PR-199154.md) | [precompile] hydrate Triton's JIT cache from a verified bundle | 2026-09-30 |  |  |
| [#199172](../sources/prs/pytorch/PR-199172.md) | Use slow path to support barebones unsigned types in CUDA _foreach_copy_ | 2026-09-30 | kernel-fusion |  |
| [#199040](../sources/prs/pytorch/PR-199040.md) | flex_gemm: consider small swapped tiles for skinny dense mm | 2026-09-29 |  | block-scale, gemm, tmem |
| [#199049](../sources/prs/pytorch/PR-199049.md) | [CUDA] Remove outdated grouped GEMM alignment constraints | 2026-09-29 |  | gemm, grouped-gemm |
| [#198922](../sources/prs/pytorch/PR-198922.md) | Fix missing cp.async drain in memory-efficient attention forward kernel | 2026-09-28 |  | attention, gemm |
| [#198789](../sources/prs/pytorch/PR-198789.md) | [precompile] carry Triton's JIT runtime cache through precompile.capture / load | 2026-09-27 |  |  |
| [#198809](../sources/prs/pytorch/PR-198809.md) | [inductor-perf] allow fusion into template epilogue inputs.  | 2026-09-27 | epilogue-fusion |  |
| [#198723](../sources/prs/pytorch/PR-198723.md) | [ATen] Specialize int32/bool -> int64 and bool -> float64 copies on CUDA | 2026-09-26 |  |  |
| [#198648](../sources/prs/pytorch/PR-198648.md) | [Profiler] Upstreaming Kineto into Pytorch | 2026-09-25 |  |  |
| [#198452](../sources/prs/pytorch/PR-198452.md) | Fix int32 overflow in cdist CUDA backward kernel | 2026-09-24 |  |  |
| [#198565](../sources/prs/pytorch/PR-198565.md) | [ATen][ROCm] zero_: keep the memset fast path outside graph capture on ROCm 7.0.x | 2026-09-24 |  |  |
| [#198415](../sources/prs/pytorch/PR-198415.md) | [BE] Compute linspace/logspace step in the opmath type for half and bfloat16 | 2026-09-23 |  |  |
| [#198196](../sources/prs/pytorch/PR-198196.md) | [ROCm] Clamp nearest2d backward launch grid | 2026-09-22 |  |  |
| [#198231](../sources/prs/pytorch/PR-198231.md) | [RAWTHROW][13] widen include_patterns: 20 conversions, 11 that must not be | 2026-09-22 |  |  |
| [#198022](../sources/prs/pytorch/PR-198022.md) | [ROCm] Return early from memory-efficient attention on empty inputs and unskip its tests | 2026-09-21 |  | attention |
| [#198050](../sources/prs/pytorch/PR-198050.md) | [Inductor] Refactor user_defined triton kerenls transitive closure to exclude imports (#198050) | 2026-09-21 | epilogue-fusion |  |
| [#197713](../sources/prs/pytorch/PR-197713.md) | [CUDA] Fix arange overflow for N >= 2**32 | 2026-09-19 |  |  |
| [#197747](../sources/prs/pytorch/PR-197747.md) | [ROCm] Bump AOTriton to 0.14.2b | 2026-09-19 |  | attention |
| [#197485](../sources/prs/pytorch/PR-197485.md) | [inductor][NVGEMM] Chain dependent NVFP4 launches into Triton consumers | 2026-09-18 |  | attention, block-scale, fp4 |
| [#197564](../sources/prs/pytorch/PR-197564.md) | Fix sparse CSR add aliasing indices between out and inputs | 2026-09-18 |  | gemm |
| [#197377](../sources/prs/pytorch/PR-197377.md) | [ATen] Keep the fill_ kernel for zero_ on ROCm 7.0.x (hipMemsetAsync corrupts under graph capture) (#197377) | 2026-09-17 |  |  |
| [#197444](../sources/prs/pytorch/PR-197444.md) | [pytorch][aten] make isinf/isfinite work for fp8 dtypes that cannot encode infinity (#197444) | 2026-09-17 |  | fp8 |
| [#197470](../sources/prs/pytorch/PR-197470.md) | Fix sort and topk for dimensions longer than INT_MAX | 2026-09-17 |  | sort, topk |
| [#197199](../sources/prs/pytorch/PR-197199.md) | [CUDA] Support float8 scalar scatter | 2026-09-16 |  | fp8 |
| [#197204](../sources/prs/pytorch/PR-197204.md) | [FSDP2] Add native collective copy ops | 2026-09-16 |  | sort |
| [#196984](../sources/prs/pytorch/PR-196984.md) | [inductor][NVGEMM] Support nvidia-cutlass-operators==0.2.0: a follow-up | 2026-09-14 |  |  |
| [#197008](../sources/prs/pytorch/PR-197008.md) | [native] Share RMSNorm forward and backward kernel launchers | 2026-09-14 |  | reduction |
| [#197011](../sources/prs/pytorch/PR-197011.md) | [native] Optimize RMSNorm backward reduction and dispatch | 2026-09-14 |  | reduction |
| [#197017](../sources/prs/pytorch/PR-197017.md) | [ATen] Keep the fill_ kernel for zero_ on ROCm 7.0.0-7.1.0 (hipMemsetAsync corrupts under graph capture) (#197017) | 2026-09-14 |  |  |
| [#196718](../sources/prs/pytorch/PR-196718.md) | [torchTLX] Reland tri-state tlx_mode knob, with a type-safe JK read | 2026-09-11 |  |  |
| [#196538](../sources/prs/pytorch/PR-196538.md) | [ROCm] Enforce signed short for __builtin_amdgcn_flat_atomic_fadd_v2bf16 | 2026-09-10 |  |  |
| [#196578](../sources/prs/pytorch/PR-196578.md) | Fix #187340: [torch.compile][Inductor][CUDA] torch.nextafter is incorrectly compiled as no-op | 2026-09-10 |  |  |
| [#196598](../sources/prs/pytorch/PR-196598.md) | [Native DSL] Make topk kernels N-dynamic | 2026-09-10 |  | sort, topk |
| [#196599](../sources/prs/pytorch/PR-196599.md) | [Native DSL] Share topk policy across JIT and AOT | 2026-09-10 |  | sort, topk |
| [#196431](../sources/prs/pytorch/PR-196431.md) | [native] Compute bmm outer-product kernel offsets in int64 (OOB writes for (batch-1)*M*N > INT32_MAX) | 2026-09-09 |  | gemm |
| [#196457](../sources/prs/pytorch/PR-196457.md) | [BE] Unify reflection/replication padding shape checks | 2026-09-09 |  |  |
| [#196507](../sources/prs/pytorch/PR-196507.md) | [native_aot] tools: Triton toolchain (raw-cubin + generated driver-API launcher) | 2026-09-09 | warp-specialization |  |
| [#196318](../sources/prs/pytorch/PR-196318.md) | flex_gemm: support F.grouped_mm through QuACK varlen-M | 2026-09-08 |  | gemm, moe |
| [#196371](../sources/prs/pytorch/PR-196371.md) | [inductor] Scalar accumulators for all reductions in large inner loops | 2026-09-08 | persistent-kernel | reduction |
| [#196230](../sources/prs/pytorch/PR-196230.md) | [BE] Unify Pooling shape checks across backends / families | 2026-09-07 |  |  |
| [#196155](../sources/prs/pytorch/PR-196155.md) | Let fastAtomicAdd derive its bound from a packed accessor | 2026-09-06 |  |  |
| [#196156](../sources/prs/pytorch/PR-196156.md) | Use fastAtomicAdd for the max-pool backward scatters | 2026-09-06 |  |  |
| [#196174](../sources/prs/pytorch/PR-196174.md) | flex_gemm: Inductor-owned QUACK autotuning | 2026-09-06 |  |  |
| [#196088](../sources/prs/pytorch/PR-196088.md) | Reject non-contiguous noise on CUDA instead of silently dropping its writes | 2026-09-05 |  |  |
| [#196100](../sources/prs/pytorch/PR-196100.md) | Fix histc(out=) dtype validation mismatch between CPU and CUDA | 2026-09-05 |  |  |
| [#196125](../sources/prs/pytorch/PR-196125.md) | Widen Float2 constructor to accscalar_t in batch norm reduction | 2026-09-05 |  | reduction |
| [#195829](../sources/prs/pytorch/PR-195829.md) | torch/_native: one CuTeDSL kernel for the chunked linear_cross_entropy backward | 2026-09-03 |  | gemm, reduction |
| [#195947](../sources/prs/pytorch/PR-195947.md) | [symm_mem]: Add per-PG stream serialization for ops | 2026-09-03 |  |  |
| [#195650](../sources/prs/pytorch/PR-195650.md) | [cuDNN][varlen] Support causal GQA paged KV serving | 2026-09-02 |  | attention, flash-attention |
| [#195676](../sources/prs/pytorch/PR-195676.md) | Delete the never-instantiated apply1 machinery in CUDAApplyUtils | 2026-09-02 |  |  |
| [#195697](../sources/prs/pytorch/PR-195697.md) | Make the int4mm sm_80 requirement an actual runtime check | 2026-09-02 |  |  |
| [#195786](../sources/prs/pytorch/PR-195786.md) | [ROCm][FlexAttention] Enable TLX backward template choices | 2026-09-02 |  |  |
| [#195537](../sources/prs/pytorch/PR-195537.md) | [CUDA] Optimize 2d scatter_reduce/index_reduce min/max | 2026-09-01 | double-buffering | reduction, tma |
| [#195538](../sources/prs/pytorch/PR-195538.md) | [inductor][NVGEMM] Support swap_ab reduction epilogues | 2026-09-01 |  | block-scale, gemm, reduction |
| [#195542](../sources/prs/pytorch/PR-195542.md) | [ATen] Vectorize bf16/fp16 -> fp32 copies on CUDA | 2026-09-01 |  |  |
| [#195396](../sources/prs/pytorch/PR-195396.md) | Name RowwiseScaledMM's EVT arguments, drop dead warning suppression | 2026-08-31 |  | gemm |
| [#195307](../sources/prs/pytorch/PR-195307.md) | Pop the diagnostic pushes that were never popped | 2026-08-30 |  |  |
| [#195303](../sources/prs/pytorch/PR-195303.md) | [ATen] Zero CUDA tensors with cudaMemsetAsync instead of a fill kernel (#195303) | 2026-08-29 |  |  |
| [#195119](../sources/prs/pytorch/PR-195119.md) | [CUDA] Hoist uniform divisor in avg_pool3d backward | 2026-08-28 |  |  |
| [#195041](../sources/prs/pytorch/PR-195041.md) | [inductor] Fix frexp returning mantissa 0 for float32 subnormals on CUDA | 2026-08-27 |  |  |
| [#195050](../sources/prs/pytorch/PR-195050.md) | [_native][2/8] Add shared CuTeDSL and reduction machinery | 2026-08-27 |  | reduction |
| [#195051](../sources/prs/pytorch/PR-195051.md) | [_native][5/8] Add general, column, and cross-CTA reductions | 2026-08-27 |  | reduction, sort, tma |
| [#195052](../sources/prs/pytorch/PR-195052.md) | [_native][3/8] Add shared tile reduction and the row driver | 2026-08-27 |  | reduction |
| [#195056](../sources/prs/pytorch/PR-195056.md) | [_native][4/8] Serve narrow rows on the tile body, TMA-staged where that wins | 2026-08-27 | pipeline-stages, swizzling | gemm, reduction, tma |
| [#195059](../sources/prs/pytorch/PR-195059.md) | [_native][6/8] Add the inner-tree fold order, with the static-fragment datapath it needs | 2026-08-27 |  | reduction |
| [#195061](../sources/prs/pytorch/PR-195061.md) | [_native][7/8] Stage the inner-tree order's mid-band through smem, in tiles | 2026-08-27 |  | reduction, tma |
| [#195062](../sources/prs/pytorch/PR-195062.md) | [_native][8/8] Serve the ordered sum/prod overrides with the shared kernel's inner-tree order | 2026-08-27 |  |  |
| [#194873](../sources/prs/pytorch/PR-194873.md) | [inductor][NVGEMM] Define scheduler Loop IR epilogue lowering | 2026-08-26 |  | gemm, reduction |
| [#194890](../sources/prs/pytorch/PR-194890.md) | [ATen]: complex type support for arange method | 2026-08-26 |  |  |
| [#194927](../sources/prs/pytorch/PR-194927.md) | [cuDNN] Add guards for cuDNN SDPA decode | 2026-08-26 |  | attention |
| [#194934](../sources/prs/pytorch/PR-194934.md) | [CUDA][ROCm] Support pruned lookups in quantized embedding_bag_byte_rowwise_offsets | 2026-08-26 |  | quantization |
| [#194727](../sources/prs/pytorch/PR-194727.md) | make sure `stream` is `torch.cuda.ExternalStream` or `torch.cuda.Stream` | 2026-08-25 |  | gemm |
| [#194787](../sources/prs/pytorch/PR-194787.md) | grid_sample: support mode='bicubic' with 5-D input, including its double backward | 2026-08-25 |  |  |
| [#194792](../sources/prs/pytorch/PR-194792.md) | [inductor][NVGEMM] Generalize block-scaled GEMM epilogues | 2026-08-25 |  | block-scale, gemm, reduction |
| [#194793](../sources/prs/pytorch/PR-194793.md) | [inductor][NVGEMM] Generalize dense GEMM epilogues | 2026-08-25 |  | block-scale, gemm, reduction |
| [#194818](../sources/prs/pytorch/PR-194818.md) | [varlen] Fix cuDNN backend bugs found by fuzz testing | 2026-08-25 |  | attention |
| [#194651](../sources/prs/pytorch/PR-194651.md) | [inductor][NVGEMM] Fuse NVFP4 output scaling | 2026-08-24 | epilogue-fusion, pipeline-stages | block-scale, fp4, fp8 |
| [#194652](../sources/prs/pytorch/PR-194652.md) | [inductor][NVGEMM] Improve NVFP4 autotuning | 2026-08-24 | epilogue-fusion | fp4, fp8, gemm |
| [#194434](../sources/prs/pytorch/PR-194434.md) | [FSDP2] Separate sharded and unsharded gradient dtypes | 2026-08-22 |  |  |
| [#194310](../sources/prs/pytorch/PR-194310.md) | Add tiled CUDA kernel for dense 2D transpose copies | 2026-08-21 |  |  |
| [#194364](../sources/prs/pytorch/PR-194364.md) | [NVGEMM] Migrate to CUTLASS Operators and Re-enable NVGEMM in B200 CI | 2026-08-21 |  | reduction |
| [#194391](../sources/prs/pytorch/PR-194391.md) | [CUDA] Remove unused multinomial probability copy | 2026-08-21 |  |  |
| [#194160](../sources/prs/pytorch/PR-194160.md) | Name the foreach norm block reduction once | 2026-08-20 |  | reduction |
| [#194169](../sources/prs/pytorch/PR-194169.md) | Build tensor_lists without copying each inner list | 2026-08-20 | kernel-fusion |  |
| [#194177](../sources/prs/pytorch/PR-194177.md) | [inductor] Vendor and adapt QuACK symmetric GEMM | 2026-08-20 | pipeline-stages, tile-scheduling | gemm, tma |
| [#194184](../sources/prs/pytorch/PR-194184.md) | Stop instantiating unreachable cat kernels | 2026-08-20 |  |  |
| [#194189](../sources/prs/pytorch/PR-194189.md) | Drop the unused BiasType parameter from the grouped FP8 GEMM | 2026-08-20 |  | fp8, gemm |
| [#194246](../sources/prs/pytorch/PR-194246.md) | [ROCm] Restore preview_unsafeAtomicAdd for ROCm < 6.4 in headeronly | 2026-08-20 |  |  |
| [#194263](../sources/prs/pytorch/PR-194263.md) | [ROCm] Avoid OpenMP capture of structured bindings in SparseCsrTensorMath (#194263) | 2026-08-20 |  |  |
| [#194100](../sources/prs/pytorch/PR-194100.md) | [ROCm] Check AOTriton attention errors at the originating callsite | 2026-08-19 |  | attention |
| [#194131](../sources/prs/pytorch/PR-194131.md) | [ROCm] Guard native BMM outer-product launches against the HIP work-item limit | 2026-08-19 |  |  |
| [#193873](../sources/prs/pytorch/PR-193873.md) | [torchTLX] tri-state knob with a build-supplied default and a JustKnob override (#193873) | 2026-08-18 |  |  |
| [#193927](../sources/prs/pytorch/PR-193927.md) | [ROCm][BE] Remove outdated version conditions | 2026-08-18 |  |  |
| [#193940](../sources/prs/pytorch/PR-193940.md) | Support `nvidia-cutlass-operators==0.2.0` | 2026-08-18 |  |  |
| [#193857](../sources/prs/pytorch/PR-193857.md) | [Inductor][Host-side TMA] Add host-side TMA support for Triton B200 GEMM templates | 2026-08-17 |  | gemm, tma |
| [#193729](../sources/prs/pytorch/PR-193729.md) | [BE][Ez]: Update c10::complex kernels to use sincos | 2026-08-16 |  |  |
| [#193583](../sources/prs/pytorch/PR-193583.md) | [BE] Share matrix multiplication shape checks | 2026-08-14 |  |  |
| [#193604](../sources/prs/pytorch/PR-193604.md) | [pytorch][PR] Migrate fastAtomicAdd to headeronly (#193176) (#193604) | 2026-08-14 |  |  |
| [#193632](../sources/prs/pytorch/PR-193632.md) | [sdpa] Fix bottom-right efficient attention when Q exceeds K | 2026-08-14 |  | attention |
| [#193291](../sources/prs/pytorch/PR-193291.md) | [ROCm] Fix incorrect results in cross-CTA reductions (argmax/max) | 2026-08-13 |  | reduction |
| [#193404](../sources/prs/pytorch/PR-193404.md) | [CUDA][LinAlg] nopiv LU - improve performance for batched moderate size (<= 1024) inputs | 2026-08-13 |  |  |
| [#193408](../sources/prs/pytorch/PR-193408.md) | Fix CUDA illegal memory access in embedding_bag per_sample_weights backward | 2026-08-13 |  |  |
| [#193434](../sources/prs/pytorch/PR-193434.md) | Extend inline asm hop for multiple-return | 2026-08-13 |  |  |
| [#193459](../sources/prs/pytorch/PR-193459.md) | Support inline_asm_elementwise in flex_attention score/mask mods | 2026-08-13 |  |  |
| [#192883](../sources/prs/pytorch/PR-192883.md) | [inductor] Extend strict_numerics INNER_TREE ordering to prod | 2026-08-11 |  | tma |
| [#192894](../sources/prs/pytorch/PR-192894.md) | flex_gemm: compose paired fragment reductions | 2026-08-11 |  | fp4, fp8, gemm |
| [#193016](../sources/prs/pytorch/PR-193016.md) | [CUDA] Fix out-of-bounds/invalid-gradient in layer_norm's huge-M gamma/beta backward | 2026-08-11 |  |  |
| [#192844](../sources/prs/pytorch/PR-192844.md) | Migrate fastAtomicAdd to headeronly | 2026-08-10 |  |  |
| [#192661](../sources/prs/pytorch/PR-192661.md) | flex_gemm: support contiguous transposed reduction outputs | 2026-08-09 |  | reduction |
| [#192662](../sources/prs/pytorch/PR-192662.md) | flex_gemm: route QUACK through modern EpiMod | 2026-08-09 | double-buffering, persistent-kernel, pipeline-stages | block-scale, clc, fp4 |
| [#192571](../sources/prs/pytorch/PR-192571.md) | [ROCm] Fix bfe() bit-field extraction in the quantized CUDA EmbeddingBag kernel (#192571) | 2026-08-08 |  | quantization |
| [#192573](../sources/prs/pytorch/PR-192573.md) | [CUDA][ROCm] Support pruned lookups in quantized embedding_bag_byte_rowwise_offsets (#192573) | 2026-08-08 |  | quantization |
| [#192546](../sources/prs/pytorch/PR-192546.md) | [BE] Move Aten files to be CLANG-FORMATTED and do it | 2026-08-07 |  |  |
| [#192547](../sources/prs/pytorch/PR-192547.md) | [BE] Delete old ROCm branches that apply to ROCM < 6.4 | 2026-08-07 |  |  |
| [#192548](../sources/prs/pytorch/PR-192548.md) | Fix (unused) return type for AtomicFPOp for BF16 | 2026-08-07 |  |  |
| [#192271](../sources/prs/pytorch/PR-192271.md) | [SDPA] Enable fused CUDA backends for rank-3 inputs | 2026-08-06 |  | attention, flash-attention |
| [#192298](../sources/prs/pytorch/PR-192298.md) | [inductor][NVGEMM] Cover epilogue providers and share reduction metadata | 2026-08-06 |  | block-scale, reduction |
| [#192348](../sources/prs/pytorch/PR-192348.md) | BE: Raise NotImplementedError for unsupported bool ops | 2026-08-06 |  |  |
| [#192410](../sources/prs/pytorch/PR-192410.md) | [triton][inductor] Eliminate full-tile loads when the value repeats across the reduction (#192410) | 2026-08-06 |  | reduction, tma |
| [#192247](../sources/prs/pytorch/PR-192247.md) | [Inductor][CuTeDSL] CSE repeated captured loads | 2026-08-05 | pipeline-stages |  |
| [#192138](../sources/prs/pytorch/PR-192138.md) | [CUDA][SDPA] Fix remap extents, causal key bound, and 32-bit dropout offsets in mem-efficient attention | 2026-08-04 |  | attention |
| [#191915](../sources/prs/pytorch/PR-191915.md) | fix(grid_sampler): Validate grad_output shape in 2D/3D backward | 2026-08-03 |  |  |
| [#191945](../sources/prs/pytorch/PR-191945.md) | [CUDA] Add NHWC GroupNorm Implementation | 2026-08-03 |  |  |
| [#191775](../sources/prs/pytorch/PR-191775.md) | [WIP] [inductor] Fuse staged MXFP6 packing epilogues | 2026-07-31 | kernel-fusion, persistent-kernel, swizzling | fp4, fp8, nvfp4 |
| [#191576](../sources/prs/pytorch/PR-191576.md) | [cuDNN][varlen] Support paged KV cache (block_table) and seqused_k in cuDNN varlen attention | 2026-07-30 |  | attention, flash-attention, reduction |
| [#191600](../sources/prs/pytorch/PR-191600.md) | [inductor][FlexGEMM] Share CuTeDSL epilogue codegen | 2026-07-30 |  | gemm, reduction |
| [#191628](../sources/prs/pytorch/PR-191628.md) | [inductor][ROCm] Skip GEMM configs where BLOCK_K underfills the packed MFMA | 2026-07-30 |  | attention, fp8, gemm |
| [#191491](../sources/prs/pytorch/PR-191491.md) | [BE][CUDA] Centralize cuda::std compatibility alias | 2026-07-29 |  |  |
| [#191514](../sources/prs/pytorch/PR-191514.md) | [inductor][NVGEMM] Adapt dense EFC to direct CuTeDSL epilogues | 2026-07-29 |  | reduction |
| [#191515](../sources/prs/pytorch/PR-191515.md) | [inductor][NVGEMM] Use direct CuTeDSL lowering for dense epilogues | 2026-07-29 |  | block-scale, reduction |
| [#191536](../sources/prs/pytorch/PR-191536.md) | [CUDA] Simplify alpha_ptr setup in scaled_gemm | 2026-07-29 |  | fp4, nvfp4 |
| [#191301](../sources/prs/pytorch/PR-191301.md) | Add half and bfloat16 support to angle on CUDA | 2026-07-28 |  |  |
| [#191358](../sources/prs/pytorch/PR-191358.md) | [BE][Ez]: Optimize some TensorIter calls to use const_inputs | 2026-07-28 |  |  |
| [#191381](../sources/prs/pytorch/PR-191381.md) | inductor: reduce autotune logging noise | 2026-07-28 |  | gemm |
| [#191166](../sources/prs/pytorch/PR-191166.md) | [ROCm][inductor] gfx1250 TDM support for dense mm/addmm | 2026-07-27 |  | attention, fp4, fp8 |
| [#191271](../sources/prs/pytorch/PR-191271.md) | flex_gemm: support bool main outputs | 2026-07-27 |  | reduction |
| [#191085](../sources/prs/pytorch/PR-191085.md) | [SDPA] Add memory-efficient GQA and vmap backward support | 2026-07-25 |  | attention, flash-attention, reduction |
| [#191086](../sources/prs/pytorch/PR-191086.md) | [CUDA] Add non-overlapping fast path for avg_pool2d backward | 2026-07-25 |  |  |
| [#191107](../sources/prs/pytorch/PR-191107.md) | [BE][Ez]: Add missing moves to std::get from std::tuple | 2026-07-25 |  |  |
| [#190953](../sources/prs/pytorch/PR-190953.md) | Remove redundant zero-init of fully-overwritten buffers in CUDA kernels | 2026-07-24 |  | gemm, reduction |
| [#191007](../sources/prs/pytorch/PR-191007.md) | [Inductor] Gate deprecated Triton block-pointer codegen (`tl.make_block_ptr`) | 2026-07-24 |  | tma |
| [#191026](../sources/prs/pytorch/PR-191026.md) | flex_gemm: support blocked local-reduce output layouts | 2026-07-24 | swizzling | fp4, gemm, nvfp4 |
| [#191062](../sources/prs/pytorch/PR-191062.md) | [ROCm] Use flattened literal OCKL path for ROCm device kernel asserts | 2026-07-24 |  |  |
| [#190895](../sources/prs/pytorch/PR-190895.md) | [native_aot] tools: declaration contract, CuTeDSL toolchain, AOT export driver | 2026-07-23 |  |  |
| [#190896](../sources/prs/pytorch/PR-190896.md) | [native_aot][1/7] tools: shared sm-string parsing + the toolchain link/ABI contract | 2026-07-23 |  |  |
| [#190899](../sources/prs/pytorch/PR-190899.md) | [native_aot] topk: first AOT declaration (fp32/bf16 radix kernels) + e2e tests | 2026-07-23 |  | sort, topk |
| [#190752](../sources/prs/pytorch/PR-190752.md) | flex_gemm: accept explicit QUACK configs | 2026-07-22 |  | gemm, reduction |
| [#190769](../sources/prs/pytorch/PR-190769.md) | [Inductor][autoWS] Enable 2-CTA for Blackwell max-autotune GEMM | 2026-07-22 | swizzling | gemm, tma |
| [#190774](../sources/prs/pytorch/PR-190774.md) | [BC breaking] Deduplicate ADAM_MODE enum and collapse fused Adam CUDA impls   | 2026-07-22 |  |  |
| [#190808](../sources/prs/pytorch/PR-190808.md) | [inductor][NVGEMM] Fuse pointwise epilogues into scaled GEMM | 2026-07-22 | epilogue-fusion | block-scale, fp4, gemm |
| [#190810](../sources/prs/pytorch/PR-190810.md) | [inductor][NVGEMM] Fuse grouped reduction epilogues | 2026-07-22 |  | block-scale, gemm, reduction |
| [#190813](../sources/prs/pytorch/PR-190813.md) | [inductor][NVGEMM] Compose grouped reductions with scaled outputs | 2026-07-22 |  | reduction |
| [#190817](../sources/prs/pytorch/PR-190817.md) | [inductor][NVGEMM] Support physical grouped reductions and centering | 2026-07-22 |  | reduction |
| [#190819](../sources/prs/pytorch/PR-190819.md) | [inductor][NVGEMM] Vendor the SM100 dense EFC kernel | 2026-07-22 | epilogue-fusion, persistent-kernel | gemm |
| [#190820](../sources/prs/pytorch/PR-190820.md) | [inductor][NVGEMM] Extend block-scaled kernel reduction mechanics | 2026-07-22 | pipeline-stages | block-scale, fp4, gemm |
| [#190821](../sources/prs/pytorch/PR-190821.md) | [inductor][NVGEMM] Register vendored epilogue providers | 2026-07-22 |  | block-scale |
| [#190689](../sources/prs/pytorch/PR-190689.md) | [inductor] Emit combo sub-kernel bodies as noinline device functions | 2026-07-21 |  |  |
| [#190692](../sources/prs/pytorch/PR-190692.md) | [inductor] Add scalar accumulators for online softmax | 2026-07-21 |  | reduction |
| [#190710](../sources/prs/pytorch/PR-190710.md) | flex_gemm: add fast math kernel option | 2026-07-21 |  |  |
| [#190546](../sources/prs/pytorch/PR-190546.md) | [ATen] [Native] [CUDA] Increase elements per thread for Rubin vectorized_elementwise_kernel | 2026-07-20 |  |  |
| [#190549](../sources/prs/pytorch/PR-190549.md) | [cuda] Compact ragged partials for foreach norm/max reductions | 2026-07-20 |  | reduction |
| [#190568](../sources/prs/pytorch/PR-190568.md) | Remove obsolete CUTLASS compatibility versioning | 2026-07-20 |  | gemm, grouped-gemm |
| [#190594](../sources/prs/pytorch/PR-190594.md) | [inductor] Fuse interleaved sub-parent reduction epilogues | 2026-07-20 |  | fp4, fp8, nvfp4 |
| [#190410](../sources/prs/pytorch/PR-190410.md) | Fix 32-bit shift in Bitfield<uint64_t> non-PTX path | 2026-07-18 |  |  |
| [#190329](../sources/prs/pytorch/PR-190329.md) | [CUDA][LinAlg] Batched LU with partial pivoting: a MAGMA-like kernel | 2026-07-17 | kernel-fusion | gemm, reduction |
| [#190372](../sources/prs/pytorch/PR-190372.md) | Bump cublasLt grouped GEMM version requirement to 13.3 | 2026-07-17 |  | gemm, grouped-gemm |
| [#190404](../sources/prs/pytorch/PR-190404.md) | [inductor] Use native NaN-propagating Triton minmax | 2026-07-17 |  | attention, flash-attention, reduction |
| [#190144](../sources/prs/pytorch/PR-190144.md) | [CUDA] Use 64-bit sample offsets in NLLLoss2d backward | 2026-07-16 |  | reduction |
| [#190158](../sources/prs/pytorch/PR-190158.md) | flex_gemm: support contracted main outputs | 2026-07-16 |  | gemm, tma |
| [#190245](../sources/prs/pytorch/PR-190245.md) | native_group_norm_backward: Fix precision errors | 2026-07-16 | pipeline-stages |  |
| [#190246](../sources/prs/pytorch/PR-190246.md) | [native_group_norm] Do some basic code cleanups | 2026-07-16 |  |  |
| [#190253](../sources/prs/pytorch/PR-190253.md) | Introduce stateless RNG APIs for randint / raw bits | 2026-07-16 |  |  |
| [#190269](../sources/prs/pytorch/PR-190269.md) | Add 32-bit indexed kernel for CUDA FFT conjugate-symmetry fill | 2026-07-16 |  |  |
| [#190036](../sources/prs/pytorch/PR-190036.md) | Simplify stateless RNG split() / fold_in() kernels with no grid-stride loop | 2026-07-15 |  |  |
| [#190039](../sources/prs/pytorch/PR-190039.md) | Fix typos in comments, docstrings, and strings across inductor and fx passes | 2026-07-15 |  |  |
| [#190092](../sources/prs/pytorch/PR-190092.md) | Add c10::safe_conv (strict, integer-only) and c10::unsafe_wrapping_convert (#190092) | 2026-07-15 |  |  |
| [#189805](../sources/prs/pytorch/PR-189805.md) | [inductor][NVGEMM] Perf: NVFP4 alpha fusion, oracle configs, TMA prefetch, zero-copy swap_ab | 2026-07-14 | pipeline-stages | block-scale, fp4, fp8 |
| [#189915](../sources/prs/pytorch/PR-189915.md) | MTA now writes the same len of data as prescribed for complex | 2026-07-14 |  |  |
| [#189953](../sources/prs/pytorch/PR-189953.md) |  Add Barebones Unsigned Integer Support to the Clamp Family | 2026-07-14 |  |  |
| [#189685](../sources/prs/pytorch/PR-189685.md) | Fix int32 overflow in CUDA bincount/histogram bin index | 2026-07-13 |  |  |
| [#189767](../sources/prs/pytorch/PR-189767.md) | Add support for full uint64 range + tensor data to fold_in() | 2026-07-13 |  |  |
| [#189772](../sources/prs/pytorch/PR-189772.md) | [inductor][NVGEMM] Migrate to cutlass.operators | 2026-07-13 | swizzling | block-scale, fp4, nvfp4 |
| [#189506](../sources/prs/pytorch/PR-189506.md) | [Reland] Port D104346887/PR 182675 for index_add fast path (#184824) | 2026-07-10 | pipeline-stages | tma |
| [#189332](../sources/prs/pytorch/PR-189332.md) | [submodule] bump cutlass to 4.5.3 | 2026-07-09 |  | gemm |
| [#189338](../sources/prs/pytorch/PR-189338.md) | Cleanup/cuda indexing stale remnants | 2026-07-09 |  |  |
| [#189405](../sources/prs/pytorch/PR-189405.md) | [ROCm] Optimize AMD normalization backward kernel by using tiled and two pass implementations where they are most efficient. | 2026-07-09 |  | reduction |
| [#189463](../sources/prs/pytorch/PR-189463.md) | Fix segfault in replication_pad{1d,2d}_backward on channel mismatch | 2026-07-09 |  |  |
| [#189162](../sources/prs/pytorch/PR-189162.md) | [inductor] Use non-NaN-propagating fmax in softmax persistent reduction | 2026-07-07 | persistent-kernel | reduction |
| [#189188](../sources/prs/pytorch/PR-189188.md) | flex_gemm: support scalar captured epilogue args | 2026-07-07 |  | gemm |
| [#189082](../sources/prs/pytorch/PR-189082.md) | Fix #188957 | 2026-07-06 |  |  |
| [#189094](../sources/prs/pytorch/PR-189094.md) | [torchTLX] move codebase to triton-beta / fbtriton (#189094) | 2026-07-06 |  |  |
| [#188971](../sources/prs/pytorch/PR-188971.md) | Fix OOB write in repeat_interleave with output_size and negative repeats (#188938) | 2026-07-05 |  |  |
| [#188865](../sources/prs/pytorch/PR-188865.md) | [inductor][NVGEMM] Use string literals for CuTeDSL fence_proxy API | 2026-07-03 |  |  |
| [#188869](../sources/prs/pytorch/PR-188869.md) | Fix from 20260702-pytorch-adhoc-6f35e0 | 2026-07-03 |  | attention, reduction |
| [#188876](../sources/prs/pytorch/PR-188876.md) | [FlexAttention] Fix int64/int32 index dtype mismatches in CuTeDSL score_mod codegen | 2026-07-03 |  | attention |
| [#188820](../sources/prs/pytorch/PR-188820.md) | [native] Move scatter-add N-dim to dynamic | 2026-07-02 |  | tma |
| [#188661](../sources/prs/pytorch/PR-188661.md) | Fix `int32` overflow in `embedding_bag(mode="max")` backward pass | 2026-07-01 |  |  |
| [#188739](../sources/prs/pytorch/PR-188739.md) | flex_gemm: add quant lowerings | 2026-07-01 | swizzling | fp4, nvfp4, quantization |
| [#188556](../sources/prs/pytorch/PR-188556.md) | [inductor] Preserve eager semantics for infinite Bessel inputs | 2026-06-30 |  |  |
| [#188597](../sources/prs/pytorch/PR-188597.md) | [ROCm] Add initial support for gfx1250 | 2026-06-30 |  | attention, flash-attention, fp4 |
| [#188469](../sources/prs/pytorch/PR-188469.md) | flex_gemm: support compressed local reduce aux outputs | 2026-06-29 | swizzling | fp4, gemm, nvfp4 |
| [#188470](../sources/prs/pytorch/PR-188470.md) | flex_gemm: extend local reduce aux groups | 2026-06-29 |  | gemm |
| [#188494](../sources/prs/pytorch/PR-188494.md) | [CUDA] Fix AvgPool2d backward handling of zero-padding  | 2026-06-29 |  |  |
| [#188345](../sources/prs/pytorch/PR-188345.md) | Fix avg_pool2d CUDA backward for channels_last inputs with padding | 2026-06-27 |  |  |
| [#188229](../sources/prs/pytorch/PR-188229.md) | Fix 64-bit indexing in avg_pool3d backward atomic kernel | 2026-06-26 |  |  |
| [#188247](../sources/prs/pytorch/PR-188247.md) | Align softmax path for half_to_float | 2026-06-26 | persistent-kernel | reduction |
| [#188186](../sources/prs/pytorch/PR-188186.md) | [native] Add TLParse-based compile/cache instrumentation for native DSL ops | 2026-06-25 |  | topk |
| [#188006](../sources/prs/pytorch/PR-188006.md) | Fix pdist and cdist launch failure past 2^24 outputs on ROCm | 2026-06-24 |  |  |
| [#188031](../sources/prs/pytorch/PR-188031.md) | Fix 64-bit indexing in spatial softmax backward | 2026-06-24 |  |  |
| [#188067](../sources/prs/pytorch/PR-188067.md) | [ROCm] fix wait instructions | 2026-06-24 |  |  |
| [#188072](../sources/prs/pytorch/PR-188072.md) | [ROCm] derive the hipcub compatible cccl version from 'HIPCUB_CCCL_VERSION' | 2026-06-24 |  |  |
| [#188112](../sources/prs/pytorch/PR-188112.md) | flex_gemm: feed local reductions into epilogues | 2026-06-24 |  | gemm, reduction |
| [#187961](../sources/prs/pytorch/PR-187961.md) | [inductor] Add compile-time per-subkernel autotuning for combo kernels | 2026-06-23 |  |  |
| [#187971](../sources/prs/pytorch/PR-187971.md) | [inductor] Add strict_numerics config to emit INNER_TREE reduction ordering for sum | 2026-06-23 | kernel-fusion | reduction, sort, tma |
| [#187767](../sources/prs/pytorch/PR-187767.md) | Fix uninitialized return in Chebyshev polynomial helpers for NaN inputs | 2026-06-20 |  |  |
| [#187700](../sources/prs/pytorch/PR-187700.md) | Fix for 187407 | 2026-06-18 |  |  |
| [#187569](../sources/prs/pytorch/PR-187569.md) |  Support fp32 output for row-wise scaled fp8 matmul on the CUTLASS path | 2026-06-17 |  | fp8 |
| [#187354](../sources/prs/pytorch/PR-187354.md) | Match Inductor i0/i1 infinities to eager CUDA | 2026-06-15 |  |  |
| [#187278](../sources/prs/pytorch/PR-187278.md) | Add in Aux-return support for just 1 aux | 2026-06-14 |  | gemm |
| [#187254](../sources/prs/pytorch/PR-187254.md) | Add captured tensor FlexGEMM epilogue args | 2026-06-13 |  | gemm |
| [#187165](../sources/prs/pytorch/PR-187165.md) | [ROCm] Enable FMA inductor lowering on ROCm | 2026-06-12 |  |  |
| [#187108](../sources/prs/pytorch/PR-187108.md) | Add dense FlexGEMM QuACK tuning | 2026-06-11 |  |  |
| [#186928](../sources/prs/pytorch/PR-186928.md) | `bcomplex32` dtype, attempt 2 | 2026-06-10 |  |  |
| [#186933](../sources/prs/pytorch/PR-186933.md) | [inductor] Use tl.minimum to handle signed zeros in torch.minimum | 2026-06-10 |  |  |
| [#186944](../sources/prs/pytorch/PR-186944.md) | Fix QuACK vendoring source and patch split | 2026-06-10 |  |  |
| [#186956](../sources/prs/pytorch/PR-186956.md) | [ROCm] Fix layer_norm fallback launch limit | 2026-06-10 |  |  |
| [#186621](../sources/prs/pytorch/PR-186621.md) | Repro for Inductor tl.broadcast_to(False) Triton compile crash (#186621) | 2026-06-08 |  |  |
| [#186480](../sources/prs/pytorch/PR-186480.md) | [BE][Ez]: More semi-automated edits to move return values | 2026-06-06 |  |  |
| [#186483](../sources/prs/pytorch/PR-186483.md) | Add PyTorch QuACK GEMM epilogue adapter e.g FlexGemm | 2026-06-06 |  | gemm, reduction |
| [#186310](../sources/prs/pytorch/PR-186310.md) | Add PyTorch QuACK GEMM epilogue adapter | 2026-06-05 |  | gemm, sort |
| [#186346](../sources/prs/pytorch/PR-186346.md) | Handle invalid CUDA JITerator cache entries | 2026-06-05 | persistent-kernel |  |
| [#186390](../sources/prs/pytorch/PR-186390.md) | remove plain assertions in torch/_inductor/codegen | 2026-06-05 | epilogue-fusion |  |
| [#186414](../sources/prs/pytorch/PR-186414.md) | native_group_norm: Handle non-contiguous tensors, rather than throwing | 2026-06-05 | pipeline-stages |  |
| [#186262](../sources/prs/pytorch/PR-186262.md) | [inductor] Make template / extern kernel registration idempotent | 2026-06-04 |  |  |
| [#186284](../sources/prs/pytorch/PR-186284.md) | Bring in gemm kernels form quack and CI testing for patch set | 2026-06-04 | persistent-kernel, pipeline-stages, swizzling | block-scale, clc, fp4 |
| [#186019](../sources/prs/pytorch/PR-186019.md) | Add aux-scalars binding to flex flash | 2026-06-03 |  | attention |
| [#185889](../sources/prs/pytorch/PR-185889.md) | Support bfloat16 in _embedding_bag_per_sample_weights_backward on CUDA | 2026-06-02 |  |  |
| [#185988](../sources/prs/pytorch/PR-185988.md) | Fix FlexAttention scalar captured grad backward | 2026-06-02 |  |  |
| [#186006](../sources/prs/pytorch/PR-186006.md) | [Inductor] No-bench per-subkernel combo-kernel config selection | 2026-06-02 |  | reduction |
| [#185788](../sources/prs/pytorch/PR-185788.md) | Support 64-bit indexing in channels_last bilinear upsampling | 2026-06-01 |  |  |
| [#185812](../sources/prs/pytorch/PR-185812.md) | Fix arange int64 fractional truncation | 2026-06-01 |  |  |
| [#185853](../sources/prs/pytorch/PR-185853.md) | Separate value index expressions from indexing | 2026-06-01 |  |  |
| [#185854](../sources/prs/pytorch/PR-185854.md) | [MPS] Add `_dirichlet_grad` Metal implementation | 2026-06-01 |  |  |
| [#185490](../sources/prs/pytorch/PR-185490.md) | [cpp] use std::clamp | 2026-05-28 |  |  |
| [#185552](../sources/prs/pytorch/PR-185552.md) | [contd][cpp] use std::clamp | 2026-05-28 |  |  |
| [#185354](../sources/prs/pytorch/PR-185354.md) | [fix][cuda][easy] signed zero in relu and clamp | 2026-05-27 |  |  |
| [#185241](../sources/prs/pytorch/PR-185241.md) | Fix typos in comments and documentation | 2026-05-26 |  | gemm |
| [#185254](../sources/prs/pytorch/PR-185254.md) | [BE][Ez]: Add missing std::move in std::make_tuple calls | 2026-05-26 |  | quantization |
| [#185040](../sources/prs/pytorch/PR-185040.md) | Clean up unused variables, redundant casts and namespaces in CUDA kernels | 2026-05-24 |  | quantization |
| [#185019](../sources/prs/pytorch/PR-185019.md) | Add lane analysis helpers for CuteDSL vector loads | 2026-05-23 |  |  |
| [#185020](../sources/prs/pytorch/PR-185020.md) | Generalize flex flash vectorization config for mask mods | 2026-05-23 |  | attention, flash-attention |
| [#185024](../sources/prs/pytorch/PR-185024.md) | Fix reflection_pad1d backward CUDA launch for large batches | 2026-05-23 |  |  |
| [#184865](../sources/prs/pytorch/PR-184865.md) | [cuteDSL] Remove cuda dependency in forked precompile subprocesses | 2026-05-22 |  | gemm |
| [#184926](../sources/prs/pytorch/PR-184926.md) | [Native DSL] Add CuTeDSL radix-select topk override | 2026-05-22 |  | reduction, scan, sort |
| [#184927](../sources/prs/pytorch/PR-184927.md) | [Native DSL] Register-resident topk for small K, small N | 2026-05-22 |  | sort, topk |
| [#184676](../sources/prs/pytorch/PR-184676.md) | Use at::aminmax | 2026-05-21 |  |  |
| [#184706](../sources/prs/pytorch/PR-184706.md) | Validate MaxUnpool output sizes | 2026-05-21 |  |  |
| [#184824](../sources/prs/pytorch/PR-184824.md) | [Reland] Port D104346887/PR 182675 for index_add fast path (#184824) | 2026-05-21 | pipeline-stages | tma |
| [#184474](../sources/prs/pytorch/PR-184474.md) | Replace deprecated std::aligned_storage in group/layer norm CUDA kernels | 2026-05-20 |  |  |
| [#184538](../sources/prs/pytorch/PR-184538.md) | [Inductor] add broader CuteDSL op overrides | 2026-05-20 |  |  |
| [#184301](../sources/prs/pytorch/PR-184301.md) | Hoist invariant gather prologue loads in mm templates | 2026-05-19 |  |  |
| [#184377](../sources/prs/pytorch/PR-184377.md) | Use rand4x for Inductor Triton random | 2026-05-19 |  |  |
| [#184393](../sources/prs/pytorch/PR-184393.md) | Modernize some CUDA kernels | 2026-05-19 |  |  |
| [#184152](../sources/prs/pytorch/PR-184152.md) | [c10] Make basic_string_view inherit from std::basic_string_view | 2026-05-18 |  |  |
| [#184166](../sources/prs/pytorch/PR-184166.md) | Stabilize efficient attention checkpoint metadata | 2026-05-18 |  | attention |
| [#184176](../sources/prs/pytorch/PR-184176.md) | Fix Inductor CUDA frexp exponent for non-finite inputs | 2026-05-18 |  |  |
| [#184288](../sources/prs/pytorch/PR-184288.md) | [ROCm] Bump AOTriton to 0.12b | 2026-05-18 |  | attention |
| [#184093](../sources/prs/pytorch/PR-184093.md) | [inductor] Rewrite Triton self-subtraction locally | 2026-05-17 |  |  |
| [#183982](../sources/prs/pytorch/PR-183982.md) | Remove CUDA <=11 version guards | 2026-05-16 |  |  |
| [#183984](../sources/prs/pytorch/PR-183984.md) | Fix CUDA atan numerics in Inductor | 2026-05-16 |  | reduction |
| [#184008](../sources/prs/pytorch/PR-184008.md) | Handle fp8e4m3fn dequantization on pre-sm89 CUDA | 2026-05-16 |  |  |
| [#183864](../sources/prs/pytorch/PR-183864.md) | [ROCm] Fix LayerNorm backward kernel for AMD Strix Halo GPUs | 2026-05-15 |  | reduction |
| [#183938](../sources/prs/pytorch/PR-183938.md) | Expand dtype/shape coverage | 2026-05-15 |  |  |
| [#183946](../sources/prs/pytorch/PR-183946.md) | [cuda][eager] Preserve internal precision for native_group_norm | 2026-05-15 |  |  |
| [#182986](../sources/prs/pytorch/PR-182986.md) | [Eager] [Bitwise-Equivalence] Implement an INNER_TREE sum reduction (#182986) | 2026-05-08 |  | reduction |
| [#182809](../sources/prs/pytorch/PR-182809.md) | [2/N] Replace data_ptr with mutable_data_ptr | 2026-05-07 |  | quantization |
| [#182329](../sources/prs/pytorch/PR-182329.md) | Plumb precompile metadata through async_compile to subprocess workers | 2026-05-04 |  |  |
| [#180885](../sources/prs/pytorch/PR-180885.md) | CUDA: unrolled kernels for upsample_linear1d forward/backward when grid is small | 2026-04-20 |  |  |
| [#180310](../sources/prs/pytorch/PR-180310.md) | [ROCm] Workaround for UpSamplingNearest2D Fwd due to HIP UINT32_MAX limit | 2026-04-14 | pipeline-stages |  |
| [#177037](../sources/prs/pytorch/PR-177037.md) | Add cublasLt as a backend for grouped GEMM (bf16/fp16 support) | 2026-03-10 |  | fp8, gemm, grouped-gemm |
| [#173895](../sources/prs/pytorch/PR-173895.md) | Remove named tensor | 2026-01-30 |  |  |
| [#172108](../sources/prs/pytorch/PR-172108.md) | [cuDNN][varlen] Fixes for cuDNN varlen SDPA | 2026-01-09 |  | attention |
| [#171588](../sources/prs/pytorch/PR-171588.md) | Remove CUB branches for CUDA <12 | 2026-01-01 |  |  |
| [#152967](../sources/prs/pytorch/PR-152967.md) | [ATen][CUDA] Optimize 128 bit vectorization | 2025-05-06 |  |  |
| [#150676](../sources/prs/pytorch/PR-150676.md) | [CUDA][avgpool2d] Fix backward launch bounds again for `sm100`, `sm120` | 2025-04-04 |  |  |
| [#150705](../sources/prs/pytorch/PR-150705.md) | [CUDA] Only use vec128 if CUDA version is newer than 12.8 | 2025-04-04 |  |  |
| [#150640](../sources/prs/pytorch/PR-150640.md) | [CUDA][avgpool2d] Fix backward launch bounds again for `sm100`, `sm120` | 2025-04-03 |  |  |

<a id="sgl-projectsglang"></a>
## sgl-project/sglang
794 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#45112](../sources/prs/sglang/PR-45112.md) | [Refactor] kernels: Regroup operators by computation and dissolve ops/muse_spark | 2026-10-19 | persistent-kernel, swizzling | attention, block-scale, fp4 |
| [#45118](../sources/prs/sglang/PR-45118.md) | [Fix] diffusion: Prevent int32 overflow in Qwen-Image-2.1-Turbo VAE RMSNorm | 2026-10-19 |  |  |
| [#44969](../sources/prs/sglang/PR-44969.md) | [Refactor] attention: Separate decode metadata from pool ownership | 2026-10-18 | kernel-fusion | attention, flash-attention, mla |
| [#44970](../sources/prs/sglang/PR-44970.md) | [Perf] unified-memory: Reduce allocation and SWA retirement overhead | 2026-10-18 |  |  |
| [#44972](../sources/prs/sglang/PR-44972.md) | [Perf] speculative: Fuse draft write-window gathering and KV translation | 2026-10-18 |  |  |
| [#44973](../sources/prs/sglang/PR-44973.md) | [Perf] attention: Capture translated FA4 verify metadata for DSPARK | 2026-10-18 |  | attention, fp4, nvfp4 |
| [#45037](../sources/prs/sglang/PR-45037.md) | [Fix] deepseek-v4.1: Start the PD decode draft SWA window at the prefill draft valid-from | 2026-10-18 |  |  |
| [#44904](../sources/prs/sglang/PR-44904.md) | [Fix] moe: Renormalize per-rank shared-slot routing over routed experts only | 2026-10-17 | kernel-fusion | moe, topk |
| [#44906](../sources/prs/sglang/PR-44906.md) | [Perf] mhc: Parallelize small-batch post across hidden tiles | 2026-10-17 | pipeline-stages | fp8 |
| [#44927](../sources/prs/sglang/PR-44927.md) | [Perf] [AMD] deepseek-v4: Skip top-k refinement for proven positive-zero ties | 2026-10-17 |  | fp4, topk |
| [#44618](../sources/prs/sglang/PR-44618.md) | [Perf] deepseek_v4: size the masked silu-mul-quant grid to the GPU, not the padded capacity | 2026-10-16 | swizzling | fp4, fp8, moe |
| [#44665](../sources/prs/sglang/PR-44665.md) | [Feat] kernels: Add muse spark operators and collective GEMM (2/5) | 2026-10-16 | persistent-kernel | attention, block-scale, fp4 |
| [#44666](../sources/prs/sglang/PR-44666.md) | [Feat] srt: Add muse spark runtime, multimodal support and tests (3/5) | 2026-10-16 |  | attention, fp4, gemm |
| [#44690](../sources/prs/sglang/PR-44690.md) | [Refactor] kernels/diffusion/tests: Prune dead code and fix tests that never ran | 2026-10-16 |  | attention, fp4, fp8 |
| [#44783](../sources/prs/sglang/PR-44783.md) | [Perf] DSv4.1: Skip discarded KV rows during window commit | 2026-10-16 |  | attention |
| [#44403](../sources/prs/sglang/PR-44403.md) | [Perf] DSv4.1: Enable decoder bounded replay by default | 2026-10-15 |  | attention, sort |
| [#44405](../sources/prs/sglang/PR-44405.md) | [Perf] [AMD] dspark: No per-step host sync in decode (1/4) | 2026-10-15 |  | attention |
| [#44418](../sources/prs/sglang/PR-44418.md) | [Feat] diffusion: support FLUX 3 Image Klein | 2026-10-15 |  | attention, flash-attention, fp4 |
| [#44518](../sources/prs/sglang/PR-44518.md) | [Feat] nemotron: Port Nemotron 3.5 Super serving changes | 2026-10-15 |  | block-scale, fp4, fp8 |
| [#44555](../sources/prs/sglang/PR-44555.md) | [DSv4.1] Fuse request-window KV copies | 2026-10-15 |  | attention |
| [#44580](../sources/prs/sglang/PR-44580.md) | [Fix] attention: Opt FlashMLA scheduler into dynamic shared memory | 2026-10-15 |  | attention |
| [#44592](../sources/prs/sglang/PR-44592.md) | [Perf] unified-memory: Prewarm the compaction move at startup and copy whole page envelopes by page id | 2026-10-15 |  | attention, mla, reduction |
| [#44180](../sources/prs/sglang/PR-44180.md) | [Perf] MiniMax-H3: fused indexed modulation for FP32 AdaLN tables | 2026-10-14 |  |  |
| [#44325](../sources/prs/sglang/PR-44325.md) | [Feat] diffusion: Add support for the MOSS-Image family | 2026-10-14 | pipeline-stages | attention, quantization, reduction |
| [#43991](../sources/prs/sglang/PR-43991.md) | [Fix] [AMD] kda: Match the fused verify Q/K norm to its reference kernel | 2026-10-13 | kernel-fusion | attention |
| [#44004](../sources/prs/sglang/PR-44004.md) | [Perf] [AMD] moe: small-batch sort with histogram + bitonic sort for 32 < P <= 256 (3/8) | 2026-10-13 |  | moe, sort, topk |
| [#44006](../sources/prs/sglang/PR-44006.md) | [Perf] [AMD] dsv4: FP4 indexer on aiter's row-group kernel for decode and target-verify (5/8) | 2026-10-13 |  | fp4 |
| [#44007](../sources/prs/sglang/PR-44007.md) | [Perf] [AMD] dsv4: optional e8m0 mxscale GEMM for dense 128x128 fp8 linears (6/8) | 2026-10-13 |  | attention, fp8, gemm |
| [#44016](../sources/prs/sglang/PR-44016.md) | [Perf] [AMD] dsv4: fp8 unified_kv decode/verify on FlyDSL v4 nm decode with a latency-model split plan (1/8) | 2026-10-13 |  | attention, fp8 |
| [#44051](../sources/prs/sglang/PR-44051.md) | [DeepSeek-V4.1] DeepSelect cluster top-k for long rows and bf16 index logits | 2026-10-13 |  | fp4, mbarrier, sort |
| [#44137](../sources/prs/sglang/PR-44137.md) | Mark FP32 redux asm volatile | 2026-10-13 |  |  |
| [#43735](../sources/prs/sglang/PR-43735.md) | [DCP] Decode context parallelism for DSA (GLM-5.2 / GLM-5.3) with MTP | 2026-10-12 |  | attention, fp8, mla |
| [#43775](../sources/prs/sglang/PR-43775.md) | [Perf] dsa: Route the k-pool indexer top-k through the top-k v2 kernel | 2026-10-12 | kernel-fusion | fp8, topk |
| [#43803](../sources/prs/sglang/PR-43803.md) | [AMD] Add flydsl mxfp8 dense gemm kernel for dpsk v4.1 prefill | 2026-10-12 | pipeline-stages, swizzling | fp8, gemm, quantization |
| [#43823](../sources/prs/sglang/PR-43823.md) | [Feat] VSA-H3: support sm80 (A100) with a raw-pointer Triton load path | 2026-10-12 | pipeline-stages | attention, sparse-attention, tcgen05 |
| [#43838](../sources/prs/sglang/PR-43838.md) | [Perf] DeepSeek-V4.1: Run the small-batch decode fusions at TP2 | 2026-10-12 | swizzling | attention, quantization |
| [#43849](../sources/prs/sglang/PR-43849.md) | [NPU][Bugfix] use CANN libdevice for DSpark Markov sampling | 2026-10-12 |  |  |
| [#43667](../sources/prs/sglang/PR-43667.md) | [Diffusion] Speed up LTX-2 guidance and video output | 2026-10-11 |  | attention, reduction |
| [#43463](../sources/prs/sglang/PR-43463.md) | [QSA] Bound the decode indexer's work by the context length | 2026-10-10 |  | attention, gemm, topk |
| [#43508](../sources/prs/sglang/PR-43508.md) | [diffusion] Run head_dim-128 QK-norm + RoPE two rows per warp for every RoPE layout | 2026-10-10 |  |  |
| [#43621](../sources/prs/sglang/PR-43621.md) | [DSpark] Add `MarkovSampleStep`, one op for a markov draft step's add and token pick | 2026-10-10 |  |  |
| [#43267](../sources/prs/sglang/PR-43267.md) | [diffusion] perf: tile MiniMax-H3's indexed modulation kernels by 2048 columns | 2026-10-09 |  |  |
| [#43326](../sources/prs/sglang/PR-43326.md) | [Feat] unified-memory: Fuse drafts with sliding-window and recurrent-state layers | 2026-10-09 |  | attention, sort, topk |
| [#43327](../sources/prs/sglang/PR-43327.md) | [diffusion] perf: fuse MiniMax-H3's RMSNorm and indexed AdaLN under quality lossless | 2026-10-09 | kernel-fusion, pipeline-stages | attention |
| [#43332](../sources/prs/sglang/PR-43332.md) | [GDN] Fix CuTe DSL decode to read the [N, HV, V, K] state layout | 2026-10-09 |  | attention |
| [#43337](../sources/prs/sglang/PR-43337.md) | [diffusion] perf: run MiniMax-H3's QK-norm + RoPE two rows per warp, bit-identical | 2026-10-09 | pipeline-stages | attention |
| [#43390](../sources/prs/sglang/PR-43390.md) | [Perf] [NVIDIA] fp8_fa_sm120: Use the block-scaled MMA encoding | 2026-10-09 |  | attention, block-scale, fp8 |
| [#43438](../sources/prs/sglang/PR-43438.md) | [Fix] attn_residual: int64 program ids in the score/combine kernels (int32 overflow at 37,451 tokens) | 2026-10-09 |  | attention, tma |
| [#43444](../sources/prs/sglang/PR-43444.md) | [Scheduler] Fix the deterministic-inference hang when a prefill chunk is shorter than its alignment | 2026-10-09 |  | attention |
| [#43106](../sources/prs/sglang/PR-43106.md) | Fuse MiMo verification RoPE and KV cache writes | 2026-10-08 |  | attention |
| [#43140](../sources/prs/sglang/PR-43140.md) | [Diffusion] Fix int32 offset overflow in the Ulysses packed-QKV pack kernel | 2026-10-08 |  | attention |
| [#43227](../sources/prs/sglang/PR-43227.md) | [Perf] Avoid gate copies in gated RMSNorm | 2026-10-08 |  | attention |
| [#43237](../sources/prs/sglang/PR-43237.md) | [Perf] Fuse BF16 writes to native HND KV cache storage | 2026-10-08 |  | fp8 |
| [#42837](../sources/prs/sglang/PR-42837.md) | [Fix] moe_sum_reduce: gate the bf16 vectorized path on hidden % 16 | 2026-10-07 |  | moe, topk |
| [#42911](../sources/prs/sglang/PR-42911.md) | [AMD] Fuse prefill index-Q RoPE fake-quant and fp4 quantize kernels in DSV4.1 | 2026-10-07 |  | attention, fp4, quantization |
| [#42982](../sources/prs/sglang/PR-42982.md) | [AMD][Fix] Saturate FP8 KV commits instead of reproducing e4m3fnuz NaN overflow | 2026-10-07 |  | attention, fp8 |
| [#43013](../sources/prs/sglang/PR-43013.md) | [Perf] Fuse short-convolution checkpoint tracking metadata | 2026-10-07 |  | attention |
| [#42743](../sources/prs/sglang/PR-42743.md) | [diffusion] model: support Kandinsky 6 | 2026-10-06 | pipeline-stages | attention |
| [#42753](../sources/prs/sglang/PR-42753.md) | [Refactor] Translate each KV loc once per iteration | 2026-10-06 |  | attention, fp8, mla |
| [#42782](../sources/prs/sglang/PR-42782.md) | [Model] Add support for EmbeddingGemma 2 | 2026-10-06 |  | attention |
| [#42810](../sources/prs/sglang/PR-42810.md) | [kernel] SwiGLU-OAI MXFP8 producer; move swizzled MXFP8 producers to ops/quantization | 2026-10-06 | swizzling | quantization |
| [#42557](../sources/prs/sglang/PR-42557.md) | [Feat] paged-experts: Serve MoE models whose weights do not fit VRAM | 2026-10-05 | stream-k | attention, fp4, fp8 |
| [#42604](../sources/prs/sglang/PR-42604.md) | [SM90] Use native block32 DeepGEMM for DeepSeek-V4.1 | 2026-10-05 |  | attention, fp8, gemm |
| [#42609](../sources/prs/sglang/PR-42609.md) | [Diffusion] Fuse Anima FP32 split-half Q/K RoPE | 2026-10-05 |  | attention, flash-attention, reduction |
| [#42611](../sources/prs/sglang/PR-42611.md) | [Fix] Make the fused KDA beta sigmoid bit-identical to torch.sigmoid | 2026-10-05 |  | attention, fp4, gemm |
| [#42614](../sources/prs/sglang/PR-42614.md) | [AMD] MiniMax-M3 indexer CP: packed scoring for EAGLE verify rows | 2026-10-05 |  | attention, fp4, fp8 |
| [#42624](../sources/prs/sglang/PR-42624.md) | [DSpark] Mask uncommitted slots before commit-inject cache lookups | 2026-10-05 |  |  |
| [#42659](../sources/prs/sglang/PR-42659.md) | perf(mla): use native SATFINITE FP8 conversion in MLA KV/Q preparation | 2026-10-05 |  | fp8, mla, tma |
| [#42683](../sources/prs/sglang/PR-42683.md) | perf(kda): rebalance MTP verify precompute and state synchronization | 2026-10-05 |  | attention |
| [#42486](../sources/prs/sglang/PR-42486.md) | [Kernel] Use explicit reciprocal scaling for recurrent Q/K normalization | 2026-10-04 |  | attention, reduction |
| [#42489](../sources/prs/sglang/PR-42489.md) | [Perf] Improve GLM-5.3-Flash DFlash decoding on B300 | 2026-10-04 |  | attention, fp8, moe |
| [#42494](../sources/prs/sglang/PR-42494.md) | [AMD] Fix RoPE cache dtype and diffusion CI failures | 2026-10-04 |  | quantization |
| [#42297](../sources/prs/sglang/PR-42297.md) | [Speculative] Add opt-in block verification | 2026-10-03 |  | attention, reduction, topk |
| [#42391](../sources/prs/sglang/PR-42391.md) | [diffusion] move kernel validation into launchers and simplify dispatch | 2026-10-03 |  | attention, fp8, quantization |
| [#42175](../sources/prs/sglang/PR-42175.md) | [Performance] Optimize Qwen3.8-Flash-Next BF16 decode on Blackwell | 2026-10-02 |  | attention, moe, reduction |
| [#42178](../sources/prs/sglang/PR-42178.md) | [DSA] k-pool: 256-token logical page so index page id = logical page id | 2026-10-02 |  | attention, sort |
| [#42212](../sources/prs/sglang/PR-42212.md) | [MoE] Skip block-padding rows in the TMA down activation and quant | 2026-10-02 |  | fp8, gemm, moe |
| [#42239](../sources/prs/sglang/PR-42239.md) | [Perf] Accelerate DiffusionGemma with FA4 and CUDA graphs on Blackwell | 2026-10-02 |  | attention, gemm, mla |
| [#42251](../sources/prs/sglang/PR-42251.md) | [KDA] Add an opt-in decode-parity mode to the Triton multi-token recurrence | 2026-10-02 |  | attention, reduction |
| [#42252](../sources/prs/sglang/PR-42252.md) | [unified-memory] Copy page envelopes in place during compaction | 2026-10-02 |  | mla |
| [#42273](../sources/prs/sglang/PR-42273.md) | [Dsv4.1] Bounded replay with sparse mla path | 2026-10-02 |  | attention, mla |
| [#41965](../sources/prs/sglang/PR-41965.md) | [Diffusion][MiniMax-H3] Fix int32 offset overflow in SubBlock router kernels | 2026-10-01 |  | attention, topk |
| [#41971](../sources/prs/sglang/PR-41971.md) | [AMD][V4.1][*/N] Pick the gfx950 wo_a batched gemm tile by row count | 2026-10-01 |  | fp8, gemm |
| [#41981](../sources/prs/sglang/PR-41981.md) | [AMD][V4.1][*/N] Greedy dspark draft/accept under SGLANG_SIMULATE_ACC_LEN | 2026-10-01 |  | topk |
| [#42011](../sources/prs/sglang/PR-42011.md) | [AMD][V4.1][*/N] Fix shared-expert fusion accuracy and speed up MoE routing on ROCm | 2026-10-01 |  | fp4, fp8, moe |
| [#42017](../sources/prs/sglang/PR-42017.md) | [AMD][V4.1][*/N] OPUS sparse prefill on gfx950 through layout conversion | 2026-10-01 |  | attention, fp8, sort |
| [#42019](../sources/prs/sglang/PR-42019.md) | [Gemma4][Attention] Enable Gemma4 FA4 on SM90 with head-dim 512 support | 2026-10-01 | pipeline-stages | attention, flash-attention, fp8 |
| [#42055](../sources/prs/sglang/PR-42055.md) | [AMD][V4.1][*/N] Fuse MXFP8 activation quant into producer kernels on gfx950 | 2026-10-01 |  | fp8, gemm, quantization |
| [#42101](../sources/prs/sglang/PR-42101.md) | [Perf] Optimize MiMo local audio attention on Hopper | 2026-10-01 | pipeline-stages | attention |
| [#42159](../sources/prs/sglang/PR-42159.md) | [DSV4.1] Reduce eager Engram extend preparation | 2026-10-01 |  |  |
| [#41790](../sources/prs/sglang/PR-41790.md) | [DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.3-Flash with BF16 KV Cache | 2026-09-30 |  | attention, fp8, mla |
| [#41830](../sources/prs/sglang/PR-41830.md) | [diffusion] kernels: take the Wan VAE decoder's remaining first-decode work off the request path | 2026-09-30 |  |  |
| [#41887](../sources/prs/sglang/PR-41887.md) | Add blackwell dual gemm fusion support for MLP | 2026-09-30 | kernel-fusion, pipeline-stages, warp-specialization | fp8, gemm, quantization |
| [#41906](../sources/prs/sglang/PR-41906.md) |  [Diffusion] MiniMax-H3 fuse the video VAE decoder's RMSNorm and QK RoPE | 2026-09-30 |  | attention |
| [#41933](../sources/prs/sglang/PR-41933.md) | [qwen 3.8 next] Fuse QSA prefill KV gathering and dtype conversion | 2026-09-30 |  | attention, fp4, fp8 |
| [#41951](../sources/prs/sglang/PR-41951.md) | [perf] [multi-lora] remove empty CTAs from fused LoRA expand and add split-K to shrink | 2026-09-30 |  | reduction |
| [#41603](../sources/prs/sglang/PR-41603.md) | [DSV4.1] Add opt-in TRT-LLM sparse attention support | 2026-09-29 |  | attention, fp8, mla |
| [#41657](../sources/prs/sglang/PR-41657.md) | [DSv4.1] Fold q_rope_store into fused_q_norm_rope | 2026-09-29 |  |  |
| [#41658](../sources/prs/sglang/PR-41658.md) | [DSv4.1] Faster fp4 index-K gather and combine_topk_swa_indices | 2026-09-29 |  | attention, fp4, quantization |
| [#41660](../sources/prs/sglang/PR-41660.md) | [DSv4.1] Fused c1/c2 compress for eager extend, faster c2 decode | 2026-09-29 |  |  |
| [#41671](../sources/prs/sglang/PR-41671.md) | [diffusion] Fuse Flux3 rowwise FP8 quantization with Triton | 2026-09-29 |  | attention, fp8, quantization |
| [#41687](../sources/prs/sglang/PR-41687.md) | [ROCm] Select DSA indexer top-k wave size by arch (wave32 on gfx1250) | 2026-09-29 |  | fp4, mla, topk |
| [#41704](../sources/prs/sglang/PR-41704.md) | [DSv4.1] Trim prefill model-entry overhead | 2026-09-29 |  |  |
| [#41710](../sources/prs/sglang/PR-41710.md) | [diffusion] kernels: stop specializing on per-request sequence lengths | 2026-09-29 |  |  |
| [#41725](../sources/prs/sglang/PR-41725.md) | [ROCm] GLM-5.2 decode path: decode-shaped MoE/MLA tiles, split speculative softmax, and bf16 GEMM routing | 2026-09-29 |  | fp4, fp8, gemm |
| [#41737](../sources/prs/sglang/PR-41737.md) | [DFlash2] Keep the greedy selector walk in range for all-NaN score rows | 2026-09-29 |  |  |
| [#41759](../sources/prs/sglang/PR-41759.md) | [MoE] Keep the moe_align_block_size pad fill inside sorted_token_ids | 2026-09-29 |  | moe |
| [#41572](../sources/prs/sglang/PR-41572.md) | [KDA] Fix ptx_kda prefill NaN without a gate lower bound and workspace growth | 2026-09-28 |  | attention, sort |
| [#41590](../sources/prs/sglang/PR-41590.md) | [Model] Add IQuest Q1 support and MTP draft | 2026-09-28 |  | attention, fp8, moe |
| [#41459](../sources/prs/sglang/PR-41459.md) | [KDA+Kimi K3] Speed up LTX-2.3 QK norm and split RoPE on H200 | 2026-09-27 | kernel-fusion | reduction |
| [#41486](../sources/prs/sglang/PR-41486.md) | [Perf] Tune SM90 GDN recurrent verify launch for small batches | 2026-09-27 |  | attention, reduction, topk |
| [#41488](../sources/prs/sglang/PR-41488.md) | [AMD] Add opt-in MiniMax-M3 TP4 indexer context partitioning | 2026-09-27 |  | attention, fp8, sort |
| [#41305](../sources/prs/sglang/PR-41305.md) | [KDA+Kimi K3] Speed up SANA-Video residual gate add on H200 | 2026-09-26 |  |  |
| [#41339](../sources/prs/sglang/PR-41339.md) | [diffusion] Qwen-Image 2.1: fuse Q/K RMSNorm + RoPE + KV packing into one CUDA kernel and project Q/K/V with one packed GEMM | 2026-09-26 | kernel-fusion | attention, gemm, quantization |
| [#41340](../sources/prs/sglang/PR-41340.md) | [diffusion] Qwen-Image 2.1 VAE decoder fast paths: bit-exact norm/bias fusions by default, channels_last decode under quality=extra-high | 2026-09-26 |  | attention, reduction |
| [#41344](../sources/prs/sglang/PR-41344.md) | [VLM] Introduce FA4 into ViT for SM100/SM103 | 2026-09-26 |  | attention, fp8, reduction |
| [#41356](../sources/prs/sglang/PR-41356.md) | [AMD] Fix jit broken on rocm env | 2026-09-26 |  |  |
| [#41364](../sources/prs/sglang/PR-41364.md) | [DeepSelect] Add page-table transform to top-k and tighten the layout contract | 2026-09-26 |  | attention, topk |
| [#41229](../sources/prs/sglang/PR-41229.md) | [Perf] [AMD] attention: Spread uneven Triton decode batches across XCDs | 2026-09-25 |  | attention, mla |
| [#41243](../sources/prs/sglang/PR-41243.md) | [Refactor] Restore logical kernel groups and test organization | 2026-09-25 |  | attention, fp4, fp8 |
| [#41251](../sources/prs/sglang/PR-41251.md) | [Perf] Optimize DeepSeek V4.1 Flash Hopper paths and Blackwell prefill selection | 2026-09-25 |  | fp4, fp8, gemm |
| [#41018](../sources/prs/sglang/PR-41018.md) | dsv4.1-amd: gfx950 MXFP8 matmul kernels and fp8-grid producers | 2026-09-24 |  | block-scale, fp8, gemm |
| [#41019](../sources/prs/sglang/PR-41019.md) | dsv4.1-amd: KV cache layouts, FP4 indexer, compressor and router kernels | 2026-09-24 |  | attention, fp4, fp8 |
| [#41020](../sources/prs/sglang/PR-41020.md) | dsv4.1-amd: gfx950 sparse decode attention and sorted top-k | 2026-09-24 |  | attention, fp4, fp8 |
| [#41105](../sources/prs/sglang/PR-41105.md) | [GLM-5.3-Flash] Capture the KDA extend in breakable prefill CUDA graphs | 2026-09-24 |  | attention, fp8, moe |
| [#41120](../sources/prs/sglang/PR-41120.md) | [AMD] Add .co for deepseek v4 fp8 decode kernel and add group decode opt | 2026-09-24 |  | attention, fp8 |
| [#41134](../sources/prs/sglang/PR-41134.md) | [AMD] Small-M W8A8 FP8 projection GEMM for Qwen3.5 AttnFP8 on gfx950 | 2026-09-24 |  | attention, fp4, fp8 |
| [#41147](../sources/prs/sglang/PR-41147.md) | [JIT] Clean up kernel headers: move runtime helpers, add once.h | 2026-09-24 |  | gemm |
| [#41159](../sources/prs/sglang/PR-41159.md) | [AMD] Fix int32 offset overflow in Triton DSv4 KV store kernels | 2026-09-24 |  |  |
| [#41166](../sources/prs/sglang/PR-41166.md) | [qwen 3.8 next] Fuse small CUDA graph input buffer copies | 2026-09-24 |  | fp4, nvfp4, topk |
| [#41173](../sources/prs/sglang/PR-41173.md) | [qwen 3.8 next] Fuse QSA graph replay metadata across draft steps | 2026-09-24 |  | attention, fp4, nvfp4 |
| [#41175](../sources/prs/sglang/PR-41175.md) | [qwen 3.8 next] Fuse NEXTN verify and draft graph input preparation | 2026-09-24 |  | fp4, nvfp4, topk |
| [#40972](../sources/prs/sglang/PR-40972.md) | [qwen next] Fuse QSA KV preparation and sparse block expansion | 2026-09-23 |  | attention, topk |
| [#40767](../sources/prs/sglang/PR-40767.md) | [JIT] Add an occupancy-preserving L1 carveout preference | 2026-09-22 |  | gemm |
| [#40785](../sources/prs/sglang/PR-40785.md) | [JIT] Fuse FP8 KV-cache quantization into the prefix-valid commit kernel | 2026-09-22 | kernel-fusion | attention, fp8, quantization |
| [#40556](../sources/prs/sglang/PR-40556.md) | [DeepSeek V4.1] Add DeepSelect JIT kernel. | 2026-09-21 | swizzling | attention, clc, mbarrier |
| [#40405](../sources/prs/sglang/PR-40405.md) | [Diffusion] Fuse lossless Wan VAE post-ops for LongLive 2 I2V | 2026-09-20 | kernel-fusion | reduction |
| [#40425](../sources/prs/sglang/PR-40425.md) | [Diffusion] Fuse lossless LingBot World FP32 normalization | 2026-09-20 |  | attention, fp8, quantization |
| [#40431](../sources/prs/sglang/PR-40431.md) | [dsv4.1]Optimize FP4 indexer by skipping invisible tiles | 2026-09-20 |  | attention, block-scale, fp4 |
| [#40490](../sources/prs/sglang/PR-40490.md) | [diffusion] Fuse lossless Klein packed QK RMSNorm and RoPE on Hopper | 2026-09-20 | kernel-fusion | attention, moe, quantization |
| [#40494](../sources/prs/sglang/PR-40494.md) | [Diffusion] Fuse Joy Image Edit QKV concatenation and avoid QK copies | 2026-09-20 |  | attention, gemm, moe |
| [#40500](../sources/prs/sglang/PR-40500.md) | [PD] Pack draft KV head slices for DCP transfers | 2026-09-20 |  |  |
| [#40278](../sources/prs/sglang/PR-40278.md) | [HiCache] TMA-staged host<->device KV transfer kernel (sm_90+) | 2026-09-19 | pipeline-stages | mbarrier, mla, tma |
| [#40325](../sources/prs/sglang/PR-40325.md) | [Fix] Repair CI fixtures and ROCm speculative tree device checks | 2026-09-19 |  |  |
| [#40326](../sources/prs/sglang/PR-40326.md) | [unified-memory] Derive KV row addresses from strides, not shapes (1/7) | 2026-09-19 |  | attention, fp8, mla |
| [#40329](../sources/prs/sglang/PR-40329.md) | [unified-memory] Remove the kernel-page multiplier plumbing (5/7) | 2026-09-19 |  | attention, block-scale, mla |
| [#40330](../sources/prs/sglang/PR-40330.md) | [unified-memory] Stride the KV translate kernel and route every translate through it (6/7) | 2026-09-19 | kernel-fusion | attention |
| [#40371](../sources/prs/sglang/PR-40371.md) | [NPU][BugFix] Avoid M-RoPE recompilation for variable sequence lengths | 2026-09-19 |  | attention |
| [#40384](../sources/prs/sglang/PR-40384.md) | [Diffusion] Fuse LongCat GELU+cat and support Edit-Turbo BCG | 2026-09-19 | kernel-fusion | attention, gemm, quantization |
| [#40163](../sources/prs/sglang/PR-40163.md) | Fix TopK v2 fallback when 16-block cluster capacity is zero | 2026-09-18 |  | topk |
| [#40175](../sources/prs/sglang/PR-40175.md) | [diffusion] attention: add fp8_fa_sm120 FP8 backend for SM120 GPUs | 2026-09-18 | swizzling | attention, flash-attention, fp8 |
| [#40197](../sources/prs/sglang/PR-40197.md) | [Refactor] Deduplicate kernel helpers and remove unused code | 2026-09-18 | pipeline-stages, swizzling | attention, mla, moe |
| [#40208](../sources/prs/sglang/PR-40208.md) | [Kernel] Fuse hc_combine_norm for mid-size verify batches (9-96 rows) | 2026-09-18 |  |  |
| [#39875](../sources/prs/sglang/PR-39875.md) | [AMD][bugfix] Fix dsv4 server launch | 2026-09-17 |  | quantization |
| [#39921](../sources/prs/sglang/PR-39921.md) | [DSV4] Generalize attention metadata, sparse prefill, and KV pool over compress ratios | 2026-09-17 |  | attention, topk |
| [#39931](../sources/prs/sglang/PR-39931.md) | [ROCm] topk v2: split one long row across blocks, the CDNA cluster-path equivalent | 2026-09-17 |  | fp4, topk |
| [#39957](../sources/prs/sglang/PR-39957.md) | [DSV4.1] Big fused wo_a quant | 2026-09-17 | pipeline-stages, swizzling | attention, fp8, gemm |
| [#39983](../sources/prs/sglang/PR-39983.md) | [diffusion] model: support qwen-image-2.1 | 2026-09-17 |  | flash-attention, fp4, nvfp4 |
| [#39987](../sources/prs/sglang/PR-39987.md) | [AMD] Tune Qwen3.5 TP4 GDN recurrent launch on gfx950 | 2026-09-17 |  | attention, fp4, fp8 |
| [#40001](../sources/prs/sglang/PR-40001.md) | [Spec][PP] Fix hybrid recurrent-state commit and micro-batch pairing under PP x speculative decoding | 2026-09-17 | pipeline-stages | attention, topk |
| [#40033](../sources/prs/sglang/PR-40033.md) | [Kernel] Move CUDA and ROCm speculative kernels to JIT | 2026-09-17 |  | scan, topk |
| [#40041](../sources/prs/sglang/PR-40041.md) | [qwen 3.8 next] Fuse Qwen PLE gate and convolution preparation for target verify | 2026-09-17 |  | reduction |
| [#39688](../sources/prs/sglang/PR-39688.md) | Fuse GLM-5.3-Flash KDA projections and prefill metadata | 2026-09-16 |  | attention, quantization |
| [#39704](../sources/prs/sglang/PR-39704.md) | [DSV4.1] Reduce mHC, metadata and small-batch router overhead | 2026-09-16 |  | attention, fp4, gemm |
| [#39726](../sources/prs/sglang/PR-39726.md) | [HiCache] Add the page-unified KV load-back JIT kernel  | 2026-09-16 |  | mla |
| [#39769](../sources/prs/sglang/PR-39769.md) | Skip fully-masked KV tiles in sliding-window extend attention | 2026-09-16 |  | attention, moe, reduction |
| [#39837](../sources/prs/sglang/PR-39837.md) | [2/N] [Kernel] Fuse padding-preserving HiSparse slot translation | 2026-09-16 | kernel-fusion | attention, fp4, fp8 |
| [#39500](../sources/prs/sglang/PR-39500.md) | [PD] Add optional KV transfer checksums | 2026-09-15 |  | reduction |
| [#39606](../sources/prs/sglang/PR-39606.md) | [HiCache] Add staged write-back for the page-unified KV cache layout | 2026-09-15 |  | mla |
| [#39614](../sources/prs/sglang/PR-39614.md) | [Qwen4-Exp] Optional fp8 (e4m3) storage for the compressed QSA indexer cache | 2026-09-15 |  | attention, fp8, gemm |
| [#39618](../sources/prs/sglang/PR-39618.md) | [XPU] Add dynamic_expert_bias and track_state support | 2026-09-15 |  | topk |
| [#39646](../sources/prs/sglang/PR-39646.md) | dsv4.1: standalone kernels and Python wrappers | 2026-09-15 | tile-scheduling | fp8, gemm, quantization |
| [#39648](../sources/prs/sglang/PR-39648.md) | dsv4.1: Top-k kernels and candidate selection | 2026-09-15 |  | attention, scan, sort |
| [#39652](../sources/prs/sglang/PR-39652.md) | dsv4.1: compression, KV I/O, and metadata kernels | 2026-09-15 |  | attention, block-scale, fp4 |
| [#39656](../sources/prs/sglang/PR-39656.md) | dsv4.1: RoPE and FP4 packing kernels | 2026-09-15 |  | block-scale, fp4, fp8 |
| [#39657](../sources/prs/sglang/PR-39657.md) | dsv4.1: Hopper FP8 matmul kernels and tuning | 2026-09-15 |  | fp8, quantization |
| [#39664](../sources/prs/sglang/PR-39664.md) | dsv4.1: mHC computation and compensated projections | 2026-09-15 |  | attention, reduction |
| [#39339](../sources/prs/sglang/PR-39339.md) | [AMD] [GLM-5.3-Flash Day 0] Build the fused DSA k-pool top-k JIT kernel on HIP | 2026-09-14 |  | attention, fp4, fp8 |
| [#39340](../sources/prs/sglang/PR-39340.md) | [AMD] [GLM-5.3-Flash Day 0] Support non-2048 top-k widths in the DSA page-table transform | 2026-09-14 |  | attention, fp4, fp8 |
| [#39341](../sources/prs/sglang/PR-39341.md) | [AMD] [GLM-5.3-Flash Day 0] Enable the k-pool DSA indexer on gfx950 | 2026-09-14 |  | attention, fp4, fp8 |
| [#39405](../sources/prs/sglang/PR-39405.md) | [misc] Revert #38346, #33426, #39061 and #39219 | 2026-09-14 |  | attention, reduction |
| [#39475](../sources/prs/sglang/PR-39475.md) | [Feat] diffusion/model: support Cosmos Dreams and Cosmos Multiview (#39475) | 2026-09-14 | pipeline-stages | attention, flash-attention, sparse-attention |
| [#39273](../sources/prs/sglang/PR-39273.md) | [AMD] [GLM-5.3-Flash] Enable FP8 and MXFP4 serving on gfx950 | 2026-09-13 | kernel-fusion | attention, fp4, fp8 |
| [#39313](../sources/prs/sglang/PR-39313.md) | fuse shared experts with routed experts in MegaMoE's DeepGEMM | 2026-09-13 |  | fp4, fp8, gemm |
| [#39172](../sources/prs/sglang/PR-39172.md) | [AMD] gfx950 assembly attention: length-aware split-KV for dynamic workload | 2026-09-12 |  | attention, fp4, fp8 |
| [#38960](../sources/prs/sglang/PR-38960.md) | [Qwen 3.8 Next] Remove unused tokenwise QSA implementation and tests | 2026-09-11 |  |  |
| [#39034](../sources/prs/sglang/PR-39034.md) | [Diffusion] Recover IPC JIT initialization after interrupted builds | 2026-09-11 |  |  |
| [#39059](../sources/prs/sglang/PR-39059.md) | [AMD] Tune Triton sparse MLA on gfx950 and make split-K workspaces graph-safe | 2026-09-11 |  | attention, fp8, mla |
| [#39124](../sources/prs/sglang/PR-39124.md) | fix(kda_prefill): fence shared writes before async proxy reads | 2026-09-11 |  | attention, tcgen05 |
| [#39126](../sources/prs/sglang/PR-39126.md) | [Qwen3.8] Enable NVIDIA NVFP4 on DGX Spark with file-backed PLE and PDL router fix | 2026-09-11 |  | fp4, fp8, gemm |
| [#39130](../sources/prs/sglang/PR-39130.md) | Add triton autotune on the Mamba2 SSD kernels | 2026-09-11 |  | attention, fp4, nvfp4 |
| [#38798](../sources/prs/sglang/PR-38798.md) | dsv4.1: remaining model and runtime integration | 2026-09-10 |  | attention, block-scale, fp4 |
| [#38830](../sources/prs/sglang/PR-38830.md) | [JIT] Port the expert-pack MXFP4 kernels to load_jit and fix their launch limits | 2026-09-10 |  | fp4, moe, topk |
| [#38841](../sources/prs/sglang/PR-38841.md) | [MiniMax-M3] Decode: paged K/V tile loads and a tiny GEMM for the router projection | 2026-09-10 |  | attention, fp4, gemm |
| [#38845](../sources/prs/sglang/PR-38845.md) | [GLM-5.3 Flash] Restore and enable KPool metadata fusion | 2026-09-10 |  | attention, moe, sort |
| [#38851](../sources/prs/sglang/PR-38851.md) | fix(qsa): make the paged sparse-decode gather memory-safe (zero-fill scratch, int64 offsets, dequant FP8 on gather) | 2026-09-10 |  | attention, fp4, fp8 |
| [#38876](../sources/prs/sglang/PR-38876.md) | [AMD] Add a Triton packed sparse decode path for QSA on ROCm | 2026-09-10 |  | attention, sparse-attention, topk |
| [#38948](../sources/prs/sglang/PR-38948.md) | [Perf] Fuse SWA page lookup and mapping clear | 2026-09-10 | kernel-fusion |  |
| [#38583](../sources/prs/sglang/PR-38583.md) | [ROCm] GLM-5.2: gfx950 four-kernel fused DSA indexer decode path | 2026-09-09 |  | fp4, fp8, gemv |
| [#38584](../sources/prs/sglang/PR-38584.md) | [Diffusion] Optimize Qwen-Image-Edit attention on Hopper | 2026-09-09 |  | attention, flash-attention, reduction |
| [#38612](../sources/prs/sglang/PR-38612.md) | [Kimi-K3] Accept fp32 routing weights in the fused MoE finalize | 2026-09-09 |  | moe |
| [#38615](../sources/prs/sglang/PR-38615.md) | [MiniMax-M3] Instantiate the decode block top-k in register buckets | 2026-09-09 |  | fp4, nvfp4, sort |
| [#38641](../sources/prs/sglang/PR-38641.md) | [Deps] Upgrade the CUDA PyTorch stack to 2.14 | 2026-09-09 |  | attention |
| [#38650](../sources/prs/sglang/PR-38650.md) | [Diffusion] Fuse the Wan VAE conv bias epilogue and tile the RMSNorm+SiLU kernel | 2026-09-09 | kernel-fusion, pipeline-stages | reduction |
| [#38409](../sources/prs/sglang/PR-38409.md) | [Fix] Wait for PDL before reading DeepSeek V4 K cache locations | 2026-09-08 |  | attention |
| [#38526](../sources/prs/sglang/PR-38526.md) | Add Ling-3.0-flash-VL model support | 2026-09-08 |  | attention, fp4, fp8 |
| [#38529](../sources/prs/sglang/PR-38529.md) | [Diffusion] Optimize SANA-WM convolution post-processing and streaming GDN | 2026-09-08 | pipeline-stages | reduction |
| [#38533](../sources/prs/sglang/PR-38533.md) | [Diffusion] Preserve BF16 rounding in Hopper LTX QKNorm and RoPE fusion | 2026-09-08 | kernel-fusion, pipeline-stages | attention, reduction |
| [#38547](../sources/prs/sglang/PR-38547.md) | [AMD] [GLM-5.3-Flash Day 0] Enable zero-RoPE TileLang DSA on gfx950 | 2026-09-08 |  | attention, fp8, gemm |
| [#38163](../sources/prs/sglang/PR-38163.md) | Revert "[AMD][DSV4] Fix unified-KV pool sizing and SWA ring accounting" | 2026-09-06 |  |  |
| [#38182](../sources/prs/sglang/PR-38182.md) | [Diffusion] Keep the Wan VAE decoder channels_last and add a Triton NHWC nearest upsample | 2026-09-06 | kernel-fusion, pipeline-stages | attention, reduction |
| [#38192](../sources/prs/sglang/PR-38192.md) | [AMD][DSV4] Reland unified-KV pool sizing and SWA ring accounting, fully gated | 2026-09-06 |  | fp8 |
| [#38220](../sources/prs/sglang/PR-38220.md) | [perf] Optimize w4a8 MoE for glm5.2 on H200 | 2026-09-06 |  | gemm, grouped-gemm, moe |
| [#38082](../sources/prs/sglang/PR-38082.md) | [Kernel] Add KDA FP8 skinny GEMM for SM120 | 2026-09-05 | pipeline-stages, swizzling, warp-specialization | block-scale, fp8, gemm |
| [#37889](../sources/prs/sglang/PR-37889.md) | [AMD] Enable GLM DSA prefill top-k to the v2 kernel | 2026-09-04 |  | attention, fp4, sort |
| [#37903](../sources/prs/sglang/PR-37903.md) | [diffusion] model: support VDN-H3 (hybrid window softmax + Video Delta linear attention MiniMax-H3, 8-NFE distill) with a hybrid_window_attn_h3 backend | 2026-09-04 | pipeline-stages, swizzling | attention, block-scale, flash-attention |
| [#37910](../sources/prs/sglang/PR-37910.md) | [Diffusion] Fuse LingBot per-token gated residual and RMSNorm modulate | 2026-09-04 |  | gemm, moe, reduction |
| [#37926](../sources/prs/sglang/PR-37926.md) | [Perf] Unified memory: close the DCP decode gap on Blackwell | 2026-09-04 | kernel-fusion | attention, mla |
| [#37941](../sources/prs/sglang/PR-37941.md) | [Fix] dsa: Make the fused top-k exact on an overflowing threshold bin | 2026-09-04 |  | sort, topk |
| [#37982](../sources/prs/sglang/PR-37982.md) | [Diffusion][MiniMax-H3] Add SM90 Sage compute for SubBlock sparse attention | 2026-09-04 |  | attention, fp8, quantization |
| [#38039](../sources/prs/sglang/PR-38039.md) | fix(mamba): unify causal_conv1d col* dtype to x (MiniCPM-V-4.6 GDN prefill bf16/fp16 mismatch) | 2026-09-04 |  |  |
| [#38040](../sources/prs/sglang/PR-38040.md) | [diffusion] quantization: ConvRot INT8 online W8A8 for DiTs (sgl-kernel + `convrot_int8_customkernel`) | 2026-09-04 | persistent-kernel, tile-scheduling, warp-specialization | fp4, fp8, gemm |
| [#38044](../sources/prs/sglang/PR-38044.md) | [diffusion] fuse LingBot MoE group-limited top-k index selection | 2026-09-04 | kernel-fusion | moe, reduction, topk |
| [#37693](../sources/prs/sglang/PR-37693.md) | [Feature] Unified memory: support decode context parallelism for the trtllm_mla family | 2026-09-03 |  | attention, fp8, mla |
| [#37764](../sources/prs/sglang/PR-37764.md) | [AMD][DSv4] Fuse the DSv4 FP4 indexer prefill-schedule preamble into one kernel | 2026-09-03 |  | attention, fp4, reduction |
| [#37500](../sources/prs/sglang/PR-37500.md) | support qwen 3.8 flash next | 2026-09-02 |  | attention, reduction, sort |
| [#37511](../sources/prs/sglang/PR-37511.md) | Size the unified read-table grid from bs, and fuse the allocator's tombstone scatters | 2026-09-02 |  | attention, mla, moe |
| [#37512](../sources/prs/sglang/PR-37512.md) | Build the unified read stream directly, without the page-table rectangle | 2026-09-02 | kernel-fusion | attention, flash-attention, mla |
| [#37577](../sources/prs/sglang/PR-37577.md) | [Feature] Add Aaronson-Gumbel text watermarking | 2026-09-02 | pipeline-stages | sort, topk |
| [#37580](../sources/prs/sglang/PR-37580.md) | [AMD] Skip unused TOPK v2 plan kernel on ROCm | 2026-09-02 |  | topk |
| [#37591](../sources/prs/sglang/PR-37591.md) | [ROCm] Make DSA indexer top-k exact with cooperative selection | 2026-09-02 |  | fp4, mbarrier, scan |
| [#37622](../sources/prs/sglang/PR-37622.md) | perf(lfm2): fuse gating and short convolution on SM90 | 2026-09-02 |  | moe |
| [#37625](../sources/prs/sglang/PR-37625.md) | Fix overflow in legacy and v1 DSA top-k selectors | 2026-09-02 |  | sort, topk |
| [#37627](../sources/prs/sglang/PR-37627.md) | [unified-memory] Speculative decoding on the unified memory pool: translate every read and write path | 2026-09-02 |  | mla |
| [#37628](../sources/prs/sglang/PR-37628.md) | [unified-memory] Fuse the draft model's KV into the target's page envelope (mechanism) | 2026-09-02 |  | attention, topk |
| [#37654](../sources/prs/sglang/PR-37654.md) | [Model] Add native IFM K2 Horizon serving support | 2026-09-02 |  | attention, gemm, moe |
| [#37659](../sources/prs/sglang/PR-37659.md) | [AMD] Parallelize aiter spec-decode KV index building over token blocks | 2026-09-02 |  | attention, fp4, topk |
| [#37662](../sources/prs/sglang/PR-37662.md) | [diffusion] perf: FastH3 8-Step V2 native support, native Blackwell VSA, batched H3 VAE decode | 2026-09-02 | pipeline-stages, swizzling, warp-specialization | attention, clc, flash-attention |
| [#37667](../sources/prs/sglang/PR-37667.md) | [Speculative Decoding] Add native UNO serving support | 2026-09-02 | kernel-fusion | attention, flash-attention, topk |
| [#37317](../sources/prs/sglang/PR-37317.md) | [Kernel] Raise shape limits in shared FLA and MoE kernels (ported from #36507) | 2026-09-01 |  | moe |
| [#37331](../sources/prs/sglang/PR-37331.md) | Fix GPU kernel ordering and MXFP8 quantization dispatch | 2026-09-01 |  | quantization |
| [#37376](../sources/prs/sglang/PR-37376.md) | [kernel] add fused silu mul quant fp8 | 2026-09-01 | kernel-fusion | fp8, gemm, moe |
| [#37413](../sources/prs/sglang/PR-37413.md) | [AMD][DSV4] feat: enable fp8 two-pool unified_kv on gfx950 | 2026-09-01 |  | attention, fp8, sort |
| [#37423](../sources/prs/sglang/PR-37423.md) | [AMD][DSv4] Switch output projection gemm (oproj_a) to fp8 | 2026-09-01 |  | attention, block-scale, fp4 |
| [#37462](../sources/prs/sglang/PR-37462.md) | [Spec] Add LiLiCorr: a candidate-lattice reranker for DFlash drafts | 2026-09-01 |  | attention, sort, topk |
| [#37477](../sources/prs/sglang/PR-37477.md) | [Kernel] GLM 5.3 Flash related kernels (ported from #36507) | 2026-09-01 |  | sort, topk |
| [#37480](../sources/prs/sglang/PR-37480.md) | [diffusion] model: support FastH3 (4-step VSA-distilled MiniMax-H3) with a VSA-H3 attention backend | 2026-09-01 |  | attention, fp8, quantization |
| [#37210](../sources/prs/sglang/PR-37210.md) | [CI][RFC] Replace black-jupyter with ruff-format | 2026-08-31 |  | attention, moe, quantization |
| [#37075](../sources/prs/sglang/PR-37075.md) | [Diffusion][Kernel] Fuse Wan2.2 NVFP4 bias + GELU on Blackwell | 2026-08-30 | kernel-fusion | attention, fp4, gemm |
| [#37093](../sources/prs/sglang/PR-37093.md) | [BugFix][DSA] Bound prefill Triton specializations for page-table stride | 2026-08-30 |  | attention, topk |
| [#37112](../sources/prs/sglang/PR-37112.md) | [Diffusion] Fuse FLUX.2 gated residual normalization on Blackwell | 2026-08-30 |  | attention, fp4, nvfp4 |
| [#37116](../sources/prs/sglang/PR-37116.md) | [diffusion] perf: absorb Qwen-Image output projection biases | 2026-08-30 |  | attention, fp4, fp8 |
| [#37123](../sources/prs/sglang/PR-37123.md) | [Diffusion] Fuse Qwen-Image FP8 QKV projection and Blackwell epilogue | 2026-08-30 | pipeline-stages | attention, fp4, fp8 |
| [#37129](../sources/prs/sglang/PR-37129.md) | [Diffusion] Fuse Qwen-Image residual norm and NVFP4 quantization | 2026-08-30 | swizzling | fp4, nvfp4, quantization |
| [#37134](../sources/prs/sglang/PR-37134.md) | [ROCm] Fix EAGLE spec-decode verify silently sampling greedy on HIP | 2026-08-30 |  | sort, topk |
| [#37140](../sources/prs/sglang/PR-37140.md) | [AMD] fix: use the hardware fp8 e4m3 convert on gfx950 | 2026-08-30 |  | fp8, quantization |
| [#37141](../sources/prs/sglang/PR-37141.md) | [Diffusion] Fuse FLUX.2 token concatenation and NVFP4 quantization | 2026-08-30 | swizzling | attention, fp4, gemm |
| [#37152](../sources/prs/sglang/PR-37152.md) | [ROCm] Widen the HiCache JIT copy rounds and enable the K-only host pool | 2026-08-30 |  | fp8, mla |
| [#37156](../sources/prs/sglang/PR-37156.md) | [Diffusion] Fuse Qwen-Image FP8 norm and activation quantization | 2026-08-30 | kernel-fusion | attention, fp8, quantization |
| [#37162](../sources/prs/sglang/PR-37162.md) | [Diffusion] Fuse FLUX.2 ModelOpt FP8 producers and QKV packing | 2026-08-30 |  | attention, fp4, fp8 |
| [#36805](../sources/prs/sglang/PR-36805.md) | Support Hy4-preview | 2026-08-28 |  | attention, mla, moe |
| [#36811](../sources/prs/sglang/PR-36811.md) | [Kernel] Avoid zero-bias allocation in fused softmax routing | 2026-08-28 |  | fp4, moe, nvfp4 |
| [#36821](../sources/prs/sglang/PR-36821.md) | [KDA] Support ReplaySSM ring-write in the fused chain-verify kernel | 2026-08-28 | kernel-fusion | attention, reduction |
| [#36825](../sources/prs/sglang/PR-36825.md) | [diffusion] Fix the XPU capability gates that broke the Wan2.2 A14B DiT path | 2026-08-28 |  |  |
| [#36871](../sources/prs/sglang/PR-36871.md) | [AMD] support gfx1250 on ROCM 10 | 2026-08-28 |  | attention, fp4, fp8 |
| [#36890](../sources/prs/sglang/PR-36890.md) | [Feature] Unified memory: support decode context parallelism for Kimi-Linear | 2026-08-28 |  | attention, mla |
| [#36680](../sources/prs/sglang/PR-36680.md) | [Diffusion] Optimize Qwen-Image TP collectives and attention | 2026-08-27 | persistent-kernel | attention, fp4, fp8 |
| [#36684](../sources/prs/sglang/PR-36684.md) | [AMD] Enable deepseek-v4 topk_transform v2 kernel | 2026-08-27 |  | attention, sort, topk |
| [#36502](../sources/prs/sglang/PR-36502.md) | [diffusion] fuse Helios paired transposed RoPE | 2026-08-26 |  | attention |
| [#36504](../sources/prs/sglang/PR-36504.md) | [diffusion][kernel] support transposed residual-gate add | 2026-08-26 |  |  |
| [#36507](../sources/prs/sglang/PR-36507.md) | GLM-5.3-Flash support | 2026-08-26 |  | attention, fp8, gemm |
| [#36521](../sources/prs/sglang/PR-36521.md) | [diffusion][kernel] avoid 4D scale-shift autotuning | 2026-08-26 | pipeline-stages |  |
| [#36527](../sources/prs/sglang/PR-36527.md) | MiniMax-M3: share the sparse index top-k across layers and reuse the decode top-k buffer | 2026-08-26 |  | attention, moe, quantization |
| [#36546](../sources/prs/sglang/PR-36546.md) | MiniMax-M3: run the sparse prefill main attention through AITER Gluon paged attention | 2026-08-26 |  | attention, fp8, gemm |
| [#36549](../sources/prs/sglang/PR-36549.md) | MiniMax-M3: allocate the lightning-indexer K cache in fp8 on gfx95 | 2026-08-26 |  | attention, fp8, gemm |
| [#36557](../sources/prs/sglang/PR-36557.md) | MiniMax-M3: Triton split-K router GEMV with in-kernel fixup | 2026-08-26 |  | attention, fp8, gemm |
| [#36559](../sources/prs/sglang/PR-36559.md) | MoE: small-batch sorting path with fused mxfp8 quantisation | 2026-08-26 | swizzling | attention, fp8, gemm |
| [#36560](../sources/prs/sglang/PR-36560.md) | MiniMax-M3: wave64 histogram-select decode top-k, and raise kMaxNumBlocks for CUDA graphs | 2026-08-26 |  | attention, fp8, gemm |
| [#36237](../sources/prs/sglang/PR-36237.md) | [MegaMoE] Respect padded MXFP8 scale row strides in pre-dispatch | 2026-08-25 |  | gemm, moe, tma |
| [#36267](../sources/prs/sglang/PR-36267.md) | [Performance] Optimize Qwen3.5 GDN prefill projection layouts | 2026-08-25 |  | attention, fp4, moe |
| [#36330](../sources/prs/sglang/PR-36330.md) | [AMD] Optimize Qwen3.5 MTP unified attention on gfx950 | 2026-08-25 |  | attention, fp4, fp8 |
| [#36340](../sources/prs/sglang/PR-36340.md) | feat(kv-cache): support SM100 NVFP4 GenMHA and speculative decoding | 2026-08-25 | swizzling | attention, block-scale, fp4 |
| [#36379](../sources/prs/sglang/PR-36379.md) | fix(lora): build the MoE LoRA align JIT kernel on ROCm | 2026-08-25 |  | attention, moe |
| [#36176](../sources/prs/sglang/PR-36176.md) | [kernel] Share the warp vectorized copy and enforce its alignment | 2026-08-24 |  | moe, reduction, scan |
| [#35981](../sources/prs/sglang/PR-35981.md) | [diffusion] Flatten Wan VAE RMSNorm row addressing | 2026-08-22 |  | reduction |
| [#35995](../sources/prs/sglang/PR-35995.md) | [diffusion] Fuse LongCat-Image QKNorm and interleaved RoPE | 2026-08-22 | kernel-fusion | attention, reduction |
| [#36003](../sources/prs/sglang/PR-36003.md) | [Kernel] Skip reserved writes in MLA KV cache | 2026-08-22 |  | attention, fp8, mla |
| [#36004](../sources/prs/sglang/PR-36004.md) | [AMD][DSV4] perf: use full 1024-thread block for indexer top-k on ROCm | 2026-08-22 |  | attention, topk |
| [#36009](../sources/prs/sglang/PR-36009.md) | [diffusion] Fix Hunyuan QKV pack indexing at production video shapes | 2026-08-22 |  |  |
| [#35770](../sources/prs/sglang/PR-35770.md) | [AMD] Optimize Kimi-K3 Triton MLA prefill on gfx950 | 2026-08-21 | pipeline-stages | attention, fp4, fp8 |
| [#35798](../sources/prs/sglang/PR-35798.md) | [Spec] Fix CDF boundary handling in `TreeSpeculativeSamplingTargetOnly` | 2026-08-21 |  |  |
| [#35634](../sources/prs/sglang/PR-35634.md) | [Feature] Add DeepEPv2 (ElasticBuffer) MoE A2A backend  | 2026-08-20 |  | attention, fp8, gemm |
| [#35695](../sources/prs/sglang/PR-35695.md) | [diffusion] Fuse SANA-Video interleaved RoPE | 2026-08-20 |  |  |
| [#35698](../sources/prs/sglang/PR-35698.md) | [diffusion] Fuse LTX-2.5 decoder 3D RoPE | 2026-08-20 |  |  |
| [#35757](../sources/prs/sglang/PR-35757.md) | fix: FA4 paged-KV zero-size page-table registers on SM90 | 2026-08-20 |  | attention, flash-attention, fp8 |
| [#35758](../sources/prs/sglang/PR-35758.md) | qwen 3.8 rebase | 2026-08-20 |  |  |
| [#35762](../sources/prs/sglang/PR-35762.md) | [PD] Pack DCP1→DCP-N PD KV transfers into dest-contiguous RDMA blocks | 2026-08-20 |  | mla |
| [#35499](../sources/prs/sglang/PR-35499.md) | [AMD] Improve K3 dspark draft attn kernel perf | 2026-08-19 |  | attention, mla, sort |
| [#35544](../sources/prs/sglang/PR-35544.md) | [GDN] Amortize ReplaySSM checkpoint materialization | 2026-08-19 |  | attention, fp4, nvfp4 |
| [#35571](../sources/prs/sglang/PR-35571.md) | [sampling] Fix int32 offset overflow in top-k renorm Triton kernels | 2026-08-19 |  | topk |
| [#35233](../sources/prs/sglang/PR-35233.md) | [AMD] Fix registered HiCache host pointer aliases | 2026-08-18 |  | mla |
| [#35245](../sources/prs/sglang/PR-35245.md) | refactor(unified-memory): translate the KV write location once, at ForwardBatch construction | 2026-08-18 |  | attention, sort |
| [#35314](../sources/prs/sglang/PR-35314.md) | Support deepseek v4 and kimi k3 on ssd | 2026-08-18 |  | fp4, fp8, moe |
| [#35337](../sources/prs/sglang/PR-35337.md) | [XPU][CI] key persistent JIT kernel cache by image content ID | 2026-08-18 |  |  |
| [#35371](../sources/prs/sglang/PR-35371.md) | [Spec] DFlash2: local convolution + candidate selector | 2026-08-18 |  | flash-attention, quantization, topk |
| [#35372](../sources/prs/sglang/PR-35372.md) | [Kernel] Support wider rows in mega_moe_pre_dispatch | 2026-08-18 |  | fp8, quantization, reduction |
| [#35114](../sources/prs/sglang/PR-35114.md) | [kernels] Reorganize ops/diffusion by operator domain behind a lazy facade | 2026-08-17 |  | attention, quantization |
| [#35118](../sources/prs/sglang/PR-35118.md) | [DSV4] hc-prenorm: fuse the combine step into a Triton kernel | 2026-08-17 | kernel-fusion | reduction |
| [#35128](../sources/prs/sglang/PR-35128.md) | [AMD] Guard ROCm 7.0 build from using hipMemcpyBatchAsync | 2026-08-17 |  |  |
| [#35154](../sources/prs/sglang/PR-35154.md) | fix(unified-memory): four boot/correctness fixes on the hybrid model paths | 2026-08-17 | pipeline-stages | attention, mla, sort |
| [#35175](../sources/prs/sglang/PR-35175.md) | [DSA] Route the ragged prefill top-k to the v2 kernel | 2026-08-17 |  | attention, sort, topk |
| [#35188](../sources/prs/sglang/PR-35188.md) | [Bugfix] Fix int32 destination offset overflow in CUTLASS MoE pre-reorder | 2026-08-17 |  | fp8, moe |
| [#35031](../sources/prs/sglang/PR-35031.md) | [JIT Kernel] Migrate causal_conv1d_fwd and causal_conv1d_update from AOT to JIT | 2026-08-16 |  | moe |
| [#35041](../sources/prs/sglang/PR-35041.md) | [DSA] Trim top-k v2 output modes and tighten its PDL waits | 2026-08-16 |  | attention, topk |
| [#35062](../sources/prs/sglang/PR-35062.md) | [Misc] Clean up python/sglang package structure | 2026-08-16 |  |  |
| [#34915](../sources/prs/sglang/PR-34915.md) | [MoE] Gather the cutlass MoE activation and its scales in one launch | 2026-08-15 | kernel-fusion | fp8, gemm, grouped-gemm |
| [#34928](../sources/prs/sglang/PR-34928.md) | [diffusion][kernel] Accelerate Sana BCG with bit-exact conv post-processing | 2026-08-15 |  | attention |
| [#34820](../sources/prs/sglang/PR-34820.md) | Store mamba prefix-cache checkpoints at the configured SSM state dtype | 2026-08-14 |  | attention, sort |
| [#34837](../sources/prs/sglang/PR-34837.md) | [AMD] Add concat_and_cast_mha_k_pad_kernel to support 12-head and enable K3 aiter prefill kernel | 2026-08-14 |  | attention, fp8, mla |
| [#34859](../sources/prs/sglang/PR-34859.md) | Qwen3.8-27B Model Support | 2026-08-14 | stream-k | fp8, gemm, gemv |
| [#34642](../sources/prs/sglang/PR-34642.md) | Revert "[Kimi K3] Fuse MLA gate projection into QKV-A GEMM" | 2026-08-13 |  | gemm, mla |
| [#34651](../sources/prs/sglang/PR-34651.md) | [DCP] Share one pack kernel between both a2a backends | 2026-08-13 |  | attention, mla, reduction |
| [#34693](../sources/prs/sglang/PR-34693.md) | [Kernel] Replace dsv3_router_gemm with the unified tiny GEMM | 2026-08-13 |  | gemm, reduction |
| [#34695](../sources/prs/sglang/PR-34695.md) | [AMD] Speed up Wan2.2 DiT FP8 attention per-tensor quantization | 2026-08-13 | persistent-kernel, pipeline-stages | attention, flash-attention, fp8 |
| [#34741](../sources/prs/sglang/PR-34741.md) | [AMD] Fix Triton 3.7 gfx950 extend-attention spills | 2026-08-13 |  | attention, sort |
| [#34490](../sources/prs/sglang/PR-34490.md) | [AMD] Add Radix-4 MoE top-k router kernel for Kimi-K3 routing | 2026-08-12 |  | moe, reduction, sort |
| [#34503](../sources/prs/sglang/PR-34503.md) | [Diffusion] Tune QK head LayerNorm for SM103 | 2026-08-12 |  |  |
| [#34505](../sources/prs/sglang/PR-34505.md) | [Diffusion][MiniMax H3] Extend exact QKNorm+RoPE rounding to SM103 | 2026-08-12 |  |  |
| [#34507](../sources/prs/sglang/PR-34507.md) | [Diffusion][Z-Image] Tune native QK RMSNorm launch for SM103 | 2026-08-12 |  |  |
| [#34509](../sources/prs/sglang/PR-34509.md) | [JIT Kernel] Migrate moe_topk_softmax from AOT to JIT | 2026-08-12 |  | moe, topk |
| [#34517](../sources/prs/sglang/PR-34517.md) | [AMD][Spec] Accelerate Qwen3.5 verification with grouped-head shared KV | 2026-08-12 |  | attention, fp4, fp8 |
| [#34537](../sources/prs/sglang/PR-34537.md) | [AMD][DCP 3/N] add aiter asm for kimi k3 target verify | 2026-08-12 |  | attention, fp8, mla |
| [#34580](../sources/prs/sglang/PR-34580.md) | [AMD] Optimize KIMI-K3 with Triton MLA decode kernel by tuning the stage-1 geometry for gfx950 | 2026-08-12 |  | attention, fp8, mla |
| [#34584](../sources/prs/sglang/PR-34584.md) | [diffusion] Wan2.2-TI2V: fuse per-token adaLN table add into contiguous slices + hoist rope cache (denoise -13.1% H100 / -12.6% H200, bit-exact; eager beats compile) | 2026-08-12 |  | attention, gemm |
| [#34613](../sources/prs/sglang/PR-34613.md) | feat(unified-memory): read unified pool from attention backends fa3/flashinfer/trtllm_mha/flashmla | 2026-08-12 |  | attention, flash-attention, mla |
| [#34614](../sources/prs/sglang/PR-34614.md) | [DCP] Fuse the a2a pack/unpack copies in the MLA LSE reduce | 2026-08-12 |  | attention, fp8, mla |
| [#34616](../sources/prs/sglang/PR-34616.md) | [Diffusion][FLUX.2] Fuse eager AdaLN and packed SwiGLU | 2026-08-12 |  |  |
| [#34617](../sources/prs/sglang/PR-34617.md) | [Diffusion][HunyuanVideo] Fuse eager QKV packing and high-quality QKNorm | 2026-08-12 |  | attention |
| [#34620](../sources/prs/sglang/PR-34620.md) | [Diffusion][ERNIE] Fuse QKNorm with full-width RoPE | 2026-08-12 |  |  |
| [#34329](../sources/prs/sglang/PR-34329.md) | HiSparse: shared-index (IndexShare) plan-then-IO swap-in prefetch | 2026-08-11 | kernel-fusion | mla |
| [#34331](../sources/prs/sglang/PR-34331.md) | [quantization] Add tuned Triton tile configs for channelwise FP8 GEMM… | 2026-08-11 |  | fp8, gemm, quantization |
| [#34347](../sources/prs/sglang/PR-34347.md) | [Diffusion][MiniMax H3] Fix SM120 QKNorm+RoPE rounding | 2026-08-11 |  |  |
| [#34349](../sources/prs/sglang/PR-34349.md) | [Diffusion] Tune QK head LayerNorm for SM120 | 2026-08-11 | kernel-fusion |  |
| [#34421](../sources/prs/sglang/PR-34421.md) | [AMD][Perf] Fuse GatedDeltaNet QKVZBA split/reshape/cat into a single Triton kernel for Qwen3.5-architecture MoE on HIP | 2026-08-11 | kernel-fusion | attention, fp4, moe |
| [#34446](../sources/prs/sglang/PR-34446.md) | [rotary] Fix the fused Qwen3.5 RoPE kernel discarding mrope height and width | 2026-08-11 |  | attention |
| [#34459](../sources/prs/sglang/PR-34459.md) | Fix DeepSeek-V4 routing: sqrtsoftplus underflow and unfloored renorm | 2026-08-11 |  | moe, topk |
| [#34462](../sources/prs/sglang/PR-34462.md) | [Triton] Bound the sliding-window extend-attention KV loop: -86.6% on SWA layers, -9.4% prefill GPU, bit-identical | 2026-08-11 |  | attention, reduction |
| [#34257](../sources/prs/sglang/PR-34257.md) | [JIT Kernel] Migrate per-token FP8 quantization from AOT to JIT | 2026-08-10 |  | fp8, gemm, quantization |
| [#34275](../sources/prs/sglang/PR-34275.md) | [Diffusion] Fuse Cosmos3 QK norm, RoPE, and KV packing | 2026-08-10 |  | attention |
| [#34277](../sources/prs/sglang/PR-34277.md) | [DSV4] Emit TMA-aligned UE8M0 scales for FP8 einsum | 2026-08-10 |  | fp8, quantization, tma |
| [#34296](../sources/prs/sglang/PR-34296.md) | [AMD] Use fast exponentials in C4 and C128 ROCm kernels | 2026-08-10 |  | reduction |
| [#34306](../sources/prs/sglang/PR-34306.md) | [diffusion] ERNIE-Image: fuse rotate-half RoPE + GELU-mul and hoist rope cos/sin (denoise -16.2% H100 / -12.7% H200, bit-exact) | 2026-08-10 |  | gemm |
| [#34314](../sources/prs/sglang/PR-34314.md) | [diffusion] Ideogram-4: fuse Qwen3-style RoPE and SwiGLU silu-mul (denoise -5.1% H100 / -4.7% H200, bit-exact) | 2026-08-10 |  | fp8 |
| [#34148](../sources/prs/sglang/PR-34148.md) | [MiniMax-H3] SubBlock: training-free block-sparse attention for the DiT | 2026-08-09 |  | attention, flash-attention, gemm |
| [#34167](../sources/prs/sglang/PR-34167.md) | [DSA] Fix top-k v2 dropping non-primary ranks' output on CUDA 13.1+ (root cause for #33835) | 2026-08-09 |  | attention, sort, sparse-attention |
| [#34180](../sources/prs/sglang/PR-34180.md) | [diffusion] Clean up shared bitexact gates, helpers, and stale naming | 2026-08-09 |  |  |
| [#34189](../sources/prs/sglang/PR-34189.md) | [DSV4] Fix silent KV corruption when speculative draft tokens > 4 | 2026-08-09 |  | moe |
| [#34085](../sources/prs/sglang/PR-34085.md) | [diffusion] Clean up kernels and shared fast paths | 2026-08-08 |  |  |
| [#34106](../sources/prs/sglang/PR-34106.md) | [jit_kernel] Fix missing JIT kernel namespaces | 2026-08-08 |  | moe |
| [#34125](../sources/prs/sglang/PR-34125.md) | [diffusion] Bit-exact data-movement elimination for the Wan causal VAE decoder (H200 LongLive2 704x1280x61f: decode 2.80->2.32 s lossless / 2.12->1.67 s quality=high, e2e -10.7%) | 2026-08-08 | kernel-fusion, pipeline-stages |  |
| [#33974](../sources/prs/sglang/PR-33974.md) | [unified memory] Support DSPARK speculative decoding + fix two NaN root causes (page hand-out zeroing, CuTe int32 slot-stride wrap) | 2026-08-07 |  | attention, mla, moe |
| [#33981](../sources/prs/sglang/PR-33981.md) | [AMD] Add K3 verified mla kernel for DSpark on triton backend | 2026-08-07 |  | attention, fp8, gemm |
| [#34004](../sources/prs/sglang/PR-34004.md) | [diffusion] FLUX.1 fused adaLN modulate (bit-exact) + RoPE cache hoist, LN-affine folding behind quality=high (H200 e2e -3.5% lossless / -6.9% high) | 2026-08-07 | kernel-fusion | attention, reduction |
| [#34008](../sources/prs/sglang/PR-34008.md) | [diffusion] GLM-Image bit-exact fused aten LayerNorm+modulate / qk-LN (H200 30-step denoise -8.1%) | 2026-08-07 |  | attention, flash-attention |
| [#34015](../sources/prs/sglang/PR-34015.md) | [diffusion] Sana: bit-exact fused aten LayerNorm+modulate under BCG (H200 denoise -4.8%) | 2026-08-07 | kernel-fusion, pipeline-stages |  |
| [#33829](../sources/prs/sglang/PR-33829.md) | [Model] Complete dots.note.omni support with native encoders, video preprocessing, and MTP decoding | 2026-08-06 | pipeline-stages | attention, fp8, mla |
| [#33854](../sources/prs/sglang/PR-33854.md) | [diffusion] ERNIE-Image bit-exact fused RMSNorm+scale/shift (H200 1024^2 e2e 15.63 -> 15.00 s, denoise -3.3%) | 2026-08-06 |  | reduction |
| [#33886](../sources/prs/sglang/PR-33886.md) | [diffusion] Z-Image bit-exact fused qk-norm (H200 Turbo 1024px e2e -6.4%) | 2026-08-06 | kernel-fusion | attention, quantization, reduction |
| [#33903](../sources/prs/sglang/PR-33903.md) | [Inkling] silu_and_mul: replace helion kernels with plain Triton | 2026-08-06 |  | moe |
| [#33623](../sources/prs/sglang/PR-33623.md) | [Kimi K3] Fuse MLA gate projection into QKV-A GEMM | 2026-08-05 |  | attention, gemm, mla |
| [#33672](../sources/prs/sglang/PR-33672.md) | [DSV4] Support raw-index output in TopK v2 | 2026-08-05 |  | topk |
| [#33739](../sources/prs/sglang/PR-33739.md) | DSPARK enable for XPU | 2026-08-05 |  | attention |
| [#33764](../sources/prs/sglang/PR-33764.md) | Fix the router GEMM inaccuracy when using _front_w in Kimi-K3 | 2026-08-05 |  | fp8, gemm, moe |
| [#33451](../sources/prs/sglang/PR-33451.md) | [diffusion] FLUX.2 VAE decoder fast path behind quality=high (H200: 1024^2 97.6->29.2 ms, 2048^2 437.2->168.5 ms) | 2026-08-04 | pipeline-stages | attention, reduction |
| [#33455](../sources/prs/sglang/PR-33455.md) | Revert "Add flashinfer rmsnorm + quant fusion support SM90, SM100, SM120" | 2026-08-04 |  | gemm |
| [#33469](../sources/prs/sglang/PR-33469.md) | kernels: scalar scale A support for fp8_gemm | 2026-08-04 |  | gemm |
| [#33474](../sources/prs/sglang/PR-33474.md) | Select DeepGEMM standard layouts by memory budget | 2026-08-04 |  | fp8, moe, quantization |
| [#33484](../sources/prs/sglang/PR-33484.md) | perf(hisparse): fuse the DSv4 value and scale swap-in copy on ROCm | 2026-08-04 |  | attention |
| [#33532](../sources/prs/sglang/PR-33532.md) | [CP]: Support CP V2 Strategy for dsv4 | 2026-08-04 |  | attention |
| [#33546](../sources/prs/sglang/PR-33546.md) | [diffusion] Wan VAE RMSNorm+SiLU fusion behind quality=high (H200 FastWan2.2 e2e 9.611 -> 9.125 s) | 2026-08-04 | kernel-fusion, pipeline-stages | reduction |
| [#33561](../sources/prs/sglang/PR-33561.md) | [Model] Support Ling-3.0-flash (BailingMoeV3)  | 2026-08-04 | kernel-fusion | attention, fp4, fp8 |
| [#33576](../sources/prs/sglang/PR-33576.md) |  [AMD] Add Work-Centric (Lean) Attention: a persistent-CTA decode kernel for long-context serving | 2026-08-04 | tile-scheduling | attention, fp4, fp8 |
| [#33599](../sources/prs/sglang/PR-33599.md) | [AMD] Fuse Kimi-K3 attn-residual aggregation | 2026-08-04 | pipeline-stages | attention, reduction, tcgen05 |
| [#33400](../sources/prs/sglang/PR-33400.md) | [jit_kernel] Move JIT kernels into namespace sglang | 2026-08-03 |  | attention, gemm, mbarrier |
| [#33433](../sources/prs/sglang/PR-33433.md) | [NVIDIA] Use sm_100f instead of sm_100a for sgl-kernel and FlashMLA | 2026-08-03 |  | moe |
| [#33275](../sources/prs/sglang/PR-33275.md) | [diffusion] model: support minimax-h3 | 2026-08-02 | pipeline-stages | quantization |
| [#33195](../sources/prs/sglang/PR-33195.md) | [AMD] Fix JIT compile failure in sgl_kernel/warp.cuh | 2026-08-01 |  |  |
| [#32991](../sources/prs/sglang/PR-32991.md) | feat(attention): add architecture-owned SM12x FA4 kernels | 2026-07-31 | persistent-kernel, pipeline-stages, tile-scheduling | attention, clc, gemm |
| [#32994](../sources/prs/sglang/PR-32994.md) | Add flashinfer rmsnorm + quant fusion support SM90, SM100, SM120 | 2026-07-31 |  | fp8, gemm, quantization |
| [#33046](../sources/prs/sglang/PR-33046.md) | [unified-memory] Support fa3, the default MLA backend on pre-Blackwell hosts | 2026-07-31 |  | attention, mla, reduction |
| [#33065](../sources/prs/sglang/PR-33065.md) | [Fix] Honor FlashMLA natural-log LSE in DCP reduction | 2026-07-31 |  | attention, mla, reduction |
| [#33085](../sources/prs/sglang/PR-33085.md) | perf(hisparse): 128-bit non-temporal swap-in copy on ROCm | 2026-07-31 |  | attention |
| [#33128](../sources/prs/sglang/PR-33128.md) | Support DeepGEMM for standard MoE dispatch | 2026-07-31 |  | fp8, moe, quantization |
| [#32890](../sources/prs/sglang/PR-32890.md) | feat(kernels): port standalone Kimi K3 kernels | 2026-07-30 | double-buffering, kernel-fusion, pipeline-stages | attention, fp8, gemm |
| [#32910](../sources/prs/sglang/PR-32910.md) | [DeepSeek-V4] Fix nvcc 13 crash building the topk_v2 kernel | 2026-07-30 |  | attention |
| [#32944](../sources/prs/sglang/PR-32944.md) | [MoE] Fuse swiglu moe up gemm epilogue | 2026-07-30 |  | gemm, moe, quantization |
| [#32971](../sources/prs/sglang/PR-32971.md) | [unified-memory] Support MLA-hybrid-Mamba (Kimi-Linear) on the Triton backend | 2026-07-30 |  | attention, mla |
| [#32972](../sources/prs/sglang/PR-32972.md) | [unified-memory] Let Kimi-Linear use the paged MLA attention backends | 2026-07-30 |  | attention, fp8, mla |
| [#32755](../sources/prs/sglang/PR-32755.md) |  [Perf] Occupancy tuning for DSA indexer fp8-quant Q kernel | 2026-07-29 | pipeline-stages | attention, fp8 |
| [#32779](../sources/prs/sglang/PR-32779.md) | [SM120&90] Add CUDA fused Triton sparse-MLA prefill backend for DSA | 2026-07-29 | pipeline-stages | attention, fp4, fp8 |
| [#32813](../sources/prs/sglang/PR-32813.md) | [Kernel] Fuse KV-cache writes for asymmetric K/V (head_dim != v_head_dim) | 2026-07-29 |  |  |
| [#32612](../sources/prs/sglang/PR-32612.md) | Support DCP for Kimi Linear model | 2026-07-28 |  | attention |
| [#32616](../sources/prs/sglang/PR-32616.md) | [JIT] Restore the previous division behavior in per-token group quantization | 2026-07-28 |  | fp8, gemm, quantization |
| [#32651](../sources/prs/sglang/PR-32651.md) | [diffusion] refactor: remove stale kernels and dead code | 2026-07-28 |  |  |
| [#32673](../sources/prs/sglang/PR-32673.md) | [Spec] Windowed draft-decode attention for built-in EAGLE / MTP drafts | 2026-07-28 |  | attention, mla, topk |
| [#32692](../sources/prs/sglang/PR-32692.md) | [gdn] support replayssm with extra buffer | 2026-07-28 |  | attention, reduction |
| [#32467](../sources/prs/sglang/PR-32467.md) | [BugFix] Fix race in c128 prefill plan kernel on ragged extend | 2026-07-27 |  | moe, reduction, sort |
| [#32477](../sources/prs/sglang/PR-32477.md) | [Kernel] Skip KV writes to reserved padding slots | 2026-07-27 |  | attention |
| [#32483](../sources/prs/sglang/PR-32483.md) | perf(hisparse): eliminate redundant swap output fill | 2026-07-27 |  | topk |
| [#32541](../sources/prs/sglang/PR-32541.md) | [Kimi] Support kimi-k3 | 2026-07-27 |  | attention, fp8, moe |
| [#32395](../sources/prs/sglang/PR-32395.md) | [MoE] Single-launch moe_align for tiny batches with many experts | 2026-07-25 |  | attention, gemm, moe |
| [#32396](../sources/prs/sglang/PR-32396.md) | [EAGLE] Handle NaNs in fused top-k=1 | 2026-07-25 |  | topk |
| [#32277](../sources/prs/sglang/PR-32277.md) | [Fix] Clamp degenerate all-sentinel draft rows to token 0 in dspark `_online_combine_kernel` | 2026-07-24 |  |  |
| [#32296](../sources/prs/sglang/PR-32296.md) | [Perf] Halve the non-finite sanitization overhead in per_token_group_quant | 2026-07-24 |  | fp8, gemm, quantization |
| [#32320](../sources/prs/sglang/PR-32320.md) | [SM120] Only split touched SWA pages in FlashMLA page-split kernel | 2026-07-24 |  | attention, moe |
| [#32327](../sources/prs/sglang/PR-32327.md) | [DeepSeek-V4] Add Q8KV8 sparse MLA prefill runtime backend | 2026-07-24 |  | attention, fp8, mla |
| [#32340](../sources/prs/sglang/PR-32340.md) | [AMD][DSV4]perf: shared experts fusion top6 | 2026-07-24 |  | attention, moe, topk |
| [#32162](../sources/prs/sglang/PR-32162.md) | [HiSparse] Support hisparse multi-step swap io kernel | 2026-07-23 |  | attention, mla, reduction |
| [#32219](../sources/prs/sglang/PR-32219.md) | [MTP] Cut spec-v2 host-seam overhead in hybrid-linear MTP decode | 2026-07-23 | kernel-fusion | attention, moe, topk |
| [#32045](../sources/prs/sglang/PR-32045.md) | [Kernel] Phase 4 batch-3: migrate tangled JIT subsystems + new groups into kernels.ops (RFC #29630) | 2026-07-22 | kernel-fusion, swizzling | attention, block-scale, flash-attention |
| [#32109](../sources/prs/sglang/PR-32109.md) | [Perf] Skip blocks past per-request live length in full-width Triton kernels | 2026-07-22 | pipeline-stages | attention |
| [#31888](../sources/prs/sglang/PR-31888.md) | [DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.2 & DeepSeek-V3.2: Q8-Path & Shared-Path Optimizations | 2026-07-21 | double-buffering, persistent-kernel, pipeline-stages | attention, fp8, gemm |
| [#31904](../sources/prs/sglang/PR-31904.md) | [KDA] Fix mixed exponent bases in Triton chunk prefill | 2026-07-21 |  | attention |
| [#31958](../sources/prs/sglang/PR-31958.md) | [perf] Compute input logprobs without materializing the full-vocab log-softmax | 2026-07-21 | kernel-fusion | flash-attention, moe, reduction |
| [#31981](../sources/prs/sglang/PR-31981.md) | [Perf] Skip page-table columns past kv length in DSA draft-extend metadata kernel | 2026-07-21 |  | attention |
| [#31741](../sources/prs/sglang/PR-31741.md) | [AMD] Enable mamba JIT transfer kernel on ROCm (fix transfer_kv_mamba NameError) | 2026-07-20 |  |  |
| [#31768](../sources/prs/sglang/PR-31768.md) | [Model] Add LLaDA2.2 Block Routing MoE support | 2026-07-20 |  | moe, sort, topk |
| [#31834](../sources/prs/sglang/PR-31834.md) | Support a same-size mixed q dtype in the fused RoPE kernels | 2026-07-20 |  | attention, fp8 |
| [#31847](../sources/prs/sglang/PR-31847.md) | [spec decoding] support inkling dspark | 2026-07-20 |  |  |
| [#31688](../sources/prs/sglang/PR-31688.md) | Fix ROCm fused KV and KDA paths | 2026-07-19 |  | attention |
| [#31681](../sources/prs/sglang/PR-31681.md) | Add Inkling model support | 2026-07-18 | kernel-fusion, pipeline-stages | attention, block-scale, fp4 |
| [#31552](../sources/prs/sglang/PR-31552.md) | [Performance] Speed up Marlin MoE with occupancy-aware launch specialization | 2026-07-17 |  | fp4, gemm, moe |
| [#31558](../sources/prs/sglang/PR-31558.md) | [Performance] Avoid FLA L2-norm recompilation by token count | 2026-07-17 |  | attention, fp8 |
| [#31563](../sources/prs/sglang/PR-31563.md) | fix mqa preshuffle layout issue for deepseek v4 | 2026-07-17 |  | attention, fp8 |
| [#31574](../sources/prs/sglang/PR-31574.md) | [EPD] Batch embedding cache host-device range copies | 2026-07-17 |  | sort |
| [#31446](../sources/prs/sglang/PR-31446.md) | [HiSparse] Add MHA hisparse support for MiniMax M3 | 2026-07-16 |  | attention, sort, sparse-attention |
| [#31468](../sources/prs/sglang/PR-31468.md) | [Spec] DFlash: remove per-step host syncs so the CPU runs a full step ahead (spec-v2 overlap) | 2026-07-16 |  | fp4, nvfp4 |
| [#31241](../sources/prs/sglang/PR-31241.md) | Refining fused A GEMM dispatch | 2026-07-15 |  | gemm |
| [#31340](../sources/prs/sglang/PR-31340.md) | Fix FP8 Triton dtype selection on A100 | 2026-07-15 |  | fp8, quantization |
| [#31362](../sources/prs/sglang/PR-31362.md) | Speculative Decoding with NGRAM support for XPU | 2026-07-15 |  | reduction |
| [#31370](../sources/prs/sglang/PR-31370.md) | [AMD] feat(moe): fold padded-topk_ids fill into fused shared-experts append+remap | 2026-07-15 |  | attention, fp4, fp8 |
| [#31131](../sources/prs/sglang/PR-31131.md) | [AMD] Fix DSV4 JIT build on rocm  | 2026-07-14 |  | fp4, fp8 |
| [#31143](../sources/prs/sglang/PR-31143.md) | [AMD] jit_kernel: complete utils.cuh HIP-compat (cudaDevAttr / cudaDeviceGetAttribute) | 2026-07-14 |  | attention, moe |
| [#30964](../sources/prs/sglang/PR-30964.md) | [AMD] Support DeepSeek V4 DSpark on AMD HIP platform | 2026-07-13 |  | attention, sort, topk |
| [#30971](../sources/prs/sglang/PR-30971.md) | [minimax-m3] fp8 attention GEMMs on SM100 (fp8_e4m3 KV + trtllm_mha) | 2026-07-13 |  | attention, fp8, gemm |
| [#30992](../sources/prs/sglang/PR-30992.md) | support GLM-5.2 MTP index sharing with prefill CP | 2026-07-13 |  | attention, topk |
| [#31041](../sources/prs/sglang/PR-31041.md) | [Spec] Add LFM2 and LFM2-MoE DSpark speculative decoding support | 2026-07-13 |  | attention, moe, sort |
| [#30924](../sources/prs/sglang/PR-30924.md) | [JIT] Trait-driven per_token_group_quant: unify the quant kernel family (flat + masked) | 2026-07-12 | swizzling | fp8, gemm, grouped-gemm |
| [#30947](../sources/prs/sglang/PR-30947.md) | [1/3] [EAGLE] perf: Fuse topk=1 draft postprocess | 2026-07-12 |  | reduction, topk |
| [#30948](../sources/prs/sglang/PR-30948.md) | [2/3] [EAGLE] perf: Fuse TP vocab-parallel embedding | 2026-07-12 |  | quantization, topk |
| [#30838](../sources/prs/sglang/PR-30838.md) | [JIT] Refactor dtype traits into DTypeTrait and unify warp reductions | 2026-07-11 |  | fp8, reduction |
| [#30847](../sources/prs/sglang/PR-30847.md) | [Fix] Guard kernel OOB accesses and harden runtime edge cases | 2026-07-11 |  | moe |
| [#30859](../sources/prs/sglang/PR-30859.md) | dsa: widen the fp8 k-cache quant kernel's token_id to int64 | 2026-07-11 |  | attention, fp8 |
| [#30784](../sources/prs/sglang/PR-30784.md) | [Kernel] Migrate scattered quantization kernels to sglang.kernels (RFC #29630, Phase 2.5, 1/7) | 2026-07-10 |  | attention, fp8, moe |
| [#30786](../sources/prs/sglang/PR-30786.md) | [Kernel] Migrate scattered MoE kernels to sglang.kernels (RFC #29630, Phase 2.5, 2/7) | 2026-07-10 | kernel-fusion | moe, topk |
| [#30787](../sources/prs/sglang/PR-30787.md) | [Kernel] Migrate top-level srt/layers stray kernels to sglang.kernels (RFC #29630, Phase 2.5, 3/7) | 2026-07-10 |  | attention |
| [#30789](../sources/prs/sglang/PR-30789.md) | [Kernel] Migrate generic attention kernels to sglang.kernels (RFC #29630, Phase 2.5, 4/7) | 2026-07-10 |  | attention, fp8, gemm |
| [#30792](../sources/prs/sglang/PR-30792.md) | [Kernel] Migrate DSA + DSV4 attention kernels to sglang.kernels (RFC #29630, Phase 2.5, 5/7) | 2026-07-10 |  | attention, topk |
| [#30793](../sources/prs/sglang/PR-30793.md) | [Kernel] Migrate linear-attention, MiniMax-sparse and diffusion kernels to sglang.kernels (RFC #29630, Phase 2.5, 6/7) | 2026-07-10 |  | attention, fp8, gemm |
| [#30575](../sources/prs/sglang/PR-30575.md) | [AMD] Enable Fast Triton Sparse MLA backend | 2026-07-09 |  | attention, fp4, fp8 |
| [#30645](../sources/prs/sglang/PR-30645.md) | [DSA] Fix top-k v2 emitting invalid indices under tie overflow / inf scores (IMA in FA3 sparse decode) | 2026-07-09 |  | attention, sort, sparse-attention |
| [#30699](../sources/prs/sglang/PR-30699.md) | [Tiny] Fix Lint in #30645 | 2026-07-09 |  |  |
| [#30512](../sources/prs/sglang/PR-30512.md) | [DSA] Fix IMA in fused top-k v2: write all output slots on tie overflow | 2026-07-08 |  | attention, flash-attention, fp4 |
| [#30514](../sources/prs/sglang/PR-30514.md) | [DSA] Integrate Q8KV8 FP8 Sparse MLA Prefill into the DSA Backend (DeepSeek-V3.2) | 2026-07-08 | double-buffering, kernel-fusion, swizzling | attention, fp8, gemm |
| [#30535](../sources/prs/sglang/PR-30535.md) | [hicache]: add  mamba_io_kernel | 2026-07-08 | double-buffering | mla |
| [#30315](../sources/prs/sglang/PR-30315.md) | [AMD][DSV4] Fix unified-KV pool sizing and SWA ring accounting | 2026-07-07 |  | attention, fp8, sort |
| [#30360](../sources/prs/sglang/PR-30360.md) | [Feature] Add MiniCPM-SALA support | 2026-07-07 |  | attention, sort, sparse-attention |
| [#30378](../sources/prs/sglang/PR-30378.md) | [DSA] Re-enable fused top-k v2 for MTP: clamp padded-row seq_lens to >= 0 | 2026-07-07 |  | attention, topk |
| [#30438](../sources/prs/sglang/PR-30438.md) | Delete CUTLASS FP8 blockwise for SM90 and SM100, move SM120 to JIT and add SwapAB | 2026-07-07 | stream-k | fp8, gemm |
| [#30255](../sources/prs/sglang/PR-30255.md) | Fix DSV4 prefill large Triton recompilation idle across context lengths | 2026-07-06 |  | attention, topk |
| [#30261](../sources/prs/sglang/PR-30261.md) | [Spec] Add DSpark: confidence-scheduled speculative decoding | 2026-07-06 |  | attention, quantization, topk |
| [#30272](../sources/prs/sglang/PR-30272.md) | Implement SM120 DeepSeek V4 flashinfer_mxfp4 moe runner backend + TP2 | 2026-07-06 |  | attention, fp4, fp8 |
| [#30274](../sources/prs/sglang/PR-30274.md) | [DSA] Fold page-table into fused top-k v2 (decode): drop page_size=1 expansion | 2026-07-06 |  | attention, sparse-attention, topk |
| [#30275](../sources/prs/sglang/PR-30275.md) | [Model] Support LongCat 2.0 FP8 | 2026-07-06 |  | fp8, gemm |
| [#30169](../sources/prs/sglang/PR-30169.md) | [GDN/KDA] Fuse SM100 CuteDSL prefill state I/O into the chunk h kernel | 2026-07-05 | pipeline-stages | attention, tma |
| [#30079](../sources/prs/sglang/PR-30079.md) | [MoE] Fix moe_fused_gate out-of-range expert id on all-NaN rows (fixes eagle_dp_attention crash) | 2026-07-04 | pipeline-stages | attention, moe, sort |
| [#30117](../sources/prs/sglang/PR-30117.md) | Support Cutedsl BF16 GEMM JIT kernel | 2026-07-04 | pipeline-stages, swizzling, warp-specialization | fp4, gemm, mbarrier |
| [#30024](../sources/prs/sglang/PR-30024.md) | [AMD] perf(sgl-kernel): default block_quota=16 for MLA page_first KV gather… | 2026-07-03 |  | mla |
| [#29927](../sources/prs/sglang/PR-29927.md) | [SM120] DeepSeek-V4: DeepGEMM paged-MQA indexer +FP4 MoE+ page-split  | 2026-07-02 | pipeline-stages, warp-specialization | attention, block-scale, fp4 |
| [#29973](../sources/prs/sglang/PR-29973.md) | [FIX] Prevent Lightning Attention extra-buffer mamba state corruption | 2026-07-02 |  | attention, sort, topk |
| [#29822](../sources/prs/sglang/PR-29822.md) | [AMD] Accept ROCm tensors in JIT kernel TensorMatcher + register 4 kernel tests | 2026-07-01 |  |  |
| [#29843](../sources/prs/sglang/PR-29843.md) | [trtllm_mha] Fuse cuda-graph metadata rebuild into one triton kernel | 2026-07-01 | kernel-fusion | attention |
| [#29694](../sources/prs/sglang/PR-29694.md) | [AMD] Fix int8 per-token quant Triton portability + register test for AMD nightly CI | 2026-06-30 |  | moe, quantization |
| [#29708](../sources/prs/sglang/PR-29708.md) | [KDA-Pilot] Add LTX2 QKNorm split-RoPE CUDA fast path | 2026-06-30 |  | attention |
| [#29718](../sources/prs/sglang/PR-29718.md) | [MoE] Make simulated expert routing support DP>1, and fuse into one triton kernel | 2026-06-30 |  | moe, topk |
| [#29742](../sources/prs/sglang/PR-29742.md) | [diffusion] Fix Z-Image accuracy | 2026-06-30 |  | attention |
| [#29771](../sources/prs/sglang/PR-29771.md) | [MoE] Consolidate ungrouped + grouped gate/topk onto one Triton router (#26771) — faster than AOT on B200/H100/H200, at parity with flashinfer | 2026-06-30 |  | fp8, gemm, moe |
| [#29609](../sources/prs/sglang/PR-29609.md) | [DeepSeek-V4] Support BF16 Compress State for Online C128 | 2026-06-29 |  |  |
| [#29613](../sources/prs/sglang/PR-29613.md) | [DSA] Use cos_sin_cache for DSA indexer fusion | 2026-06-29 |  | fp4, fp8, nvfp4 |
| [#29664](../sources/prs/sglang/PR-29664.md) | [Diffusion] Reuse shared AlignedVector and tidy jit_kernel/diffusion | 2026-06-29 |  |  |
| [#29667](../sources/prs/sglang/PR-29667.md) | Add fused EH norm for DeepSeek NextN | 2026-06-29 |  | fp4, nvfp4 |
| [#29677](../sources/prs/sglang/PR-29677.md) | [AMD] perf: compact Triton extend-attention for ragged prefill (AMD/HIP-only) | 2026-06-29 | tile-scheduling | attention, flash-attention, fp4 |
| [#29678](../sources/prs/sglang/PR-29678.md) | feat(mem_cache): unified memory pool for hybrid Mamba / SWA models | 2026-06-29 |  | attention, moe, sort |
| [#29690](../sources/prs/sglang/PR-29690.md) | Fuse the preprocess kernels of trtllm-gen attention | 2026-06-29 |  | attention, fp4, fp8 |
| [#29533](../sources/prs/sglang/PR-29533.md) | feat(mem_cache): page-major (layer-major within a page) KV/state layout | 2026-06-28 |  | attention, fp4, moe |
| [#29554](../sources/prs/sglang/PR-29554.md) | Upgrading tvm-ffi/sgl-deep-gemm/tilelang | 2026-06-28 |  | attention, gemm |
| [#29499](../sources/prs/sglang/PR-29499.md) | [DSA] Optimize DSA CUDA graph replay metadata generation | 2026-06-27 |  | attention, fp4, nvfp4 |
| [#29525](../sources/prs/sglang/PR-29525.md) | [Feature] Add DeepEPv2 (ElasticBuffer) MoE A2A backend | 2026-06-27 |  | attention, fp8, gemm |
| [#29361](../sources/prs/sglang/PR-29361.md) | [KDA-Pilot] Add diffusion residual-gate CUDA fast path for LTX2 | 2026-06-26 | pipeline-stages | attention |
| [#29365](../sources/prs/sglang/PR-29365.md) | [CP] Consolidate decode-context-parallel (DCP) helpers into layers/dcp/ | 2026-06-26 |  | attention, mla, reduction |
| [#29373](../sources/prs/sglang/PR-29373.md) | [AMD] [GLM5] Guard cuda_runtime.h for ROCm in fused_metadata_copy | 2026-06-26 |  | fp4, topk |
| [#29383](../sources/prs/sglang/PR-29383.md) | feat(sgl-kernel): add InfLLM v2 attention kernels | 2026-06-26 |  | attention, flash-attention, sparse-attention |
| [#29390](../sources/prs/sglang/PR-29390.md) | [Diffusion] Fuse LTX2 Ada values | 2026-06-26 | pipeline-stages | attention |
| [#29432](../sources/prs/sglang/PR-29432.md) | Fix bookkeeping fields not encapsulated with real allocations in normal alloc, PD pre-alloc, DFlash and EAGLE | 2026-06-26 |  |  |
| [#29223](../sources/prs/sglang/PR-29223.md) | (perf): Shard Kimi-K2.5 Eagle3 draft fc + symm-mem AG | 2026-06-25 |  | gemm |
| [#29228](../sources/prs/sglang/PR-29228.md) | [Spec] Merge dflash triton kernels into a single `dflash.py` | 2026-06-25 |  |  |
| [#29281](../sources/prs/sglang/PR-29281.md) | [KDA-Pilot] Add diffusion causal Conv3D cat-pad CUDA fast path for Cosmos3 | 2026-06-25 |  |  |
| [#29118](../sources/prs/sglang/PR-29118.md) | [Spec] Fold DFlash verified_id into the shared bonus_tokens relay channel | 2026-06-24 |  |  |
| [#29186](../sources/prs/sglang/PR-29186.md) | [New Model] Add Baidu Unlimited-OCR | 2026-06-24 | pipeline-stages | attention, flash-attention, moe |
| [#28975](../sources/prs/sglang/PR-28975.md) | [AMD] [GLM5] Add opt-in Triton fp8 sparse-MLA prefill kernel for gfx950 | 2026-06-23 |  | attention, flash-attention, fp4 |
| [#28938](../sources/prs/sglang/PR-28938.md) | [AMD] Improve performance of dsv4 in high concurrency | 2026-06-22 |  | attention, fp8, gemm |
| [#28953](../sources/prs/sglang/PR-28953.md) | [LoRA] BF16 support + EP cuda-graph crash fix for experimental_sgl_trtllm MoE-LoRA | 2026-06-22 | pipeline-stages | fp4, fp8, gemm |
| [#28788](../sources/prs/sglang/PR-28788.md) | [AMD] Fix int32 offset overflow in Triton decode-attention kernels | 2026-06-20 |  | attention, mla |
| [#28695](../sources/prs/sglang/PR-28695.md) | [GDN] Support ReplaySSM Ring Spec-Verify | 2026-06-19 | pipeline-stages | attention, quantization, reduction |
| [#28712](../sources/prs/sglang/PR-28712.md) | [minimax-m3] Split 1/4: sparse attention ops + JIT kernels + config foundation | 2026-06-19 | kernel-fusion | attention, fp8, gemm |
| [#28715](../sources/prs/sglang/PR-28715.md) | [minimax-m3] Split 4/4: model + VL + glue + function-call + fp8 quant + generic infra | 2026-06-19 |  | attention, fp4, fp8 |
| [#28722](../sources/prs/sglang/PR-28722.md) | [AMD] Optimize o_proj gemm and attn output rope performance | 2026-06-19 |  | attention, fp8, gemm |
| [#28612](../sources/prs/sglang/PR-28612.md) | Optimize C128 state pool allocation using request state pool | 2026-06-18 |  | attention, fp8, moe |
| [#28658](../sources/prs/sglang/PR-28658.md) | [AMD] Fuse shared-expert sigmoid + bf16->fp32 cast into the MoE append kernel (3 kernels -> 1) | 2026-06-18 |  | fp4, moe |
| [#28666](../sources/prs/sglang/PR-28666.md) | [AMD] Fuse shared_expert_gate GEMV into the MoE append kernel (HIP/aiter) | 2026-06-18 |  | fp4, gemm, gemv |
| [#28670](../sources/prs/sglang/PR-28670.md) | [JIT] Add kpool_topk_transform JIT kernel | 2026-06-18 |  | sort, topk |
| [#28534](../sources/prs/sglang/PR-28534.md) | [AMD] Enable JIT staged HiCache write-back and fix CPU-index crash | 2026-06-17 |  | attention, fp4, mla |
| [#28357](../sources/prs/sglang/PR-28357.md) | [AMD] fix(jit): port kv_canary write/verify/plan kernels to ROCm | 2026-06-16 |  | reduction |
| [#28371](../sources/prs/sglang/PR-28371.md) | [LoRA] Fix chunked SGMV (csgmv) CUDA graph segment replay | 2026-06-16 |  | fp8, mla, moe |
| [#28451](../sources/prs/sglang/PR-28451.md) | [GDN][KDA] ReplaySSM buffered output-only decode for Linear Attention | 2026-06-16 |  | attention, moe, sort |
| [#28455](../sources/prs/sglang/PR-28455.md) | [AMD] Fix DeepSeek-V4 fp8 KV path on gfx942 (e4m3fnuz) | 2026-06-16 |  | attention, fp8, gemm |
| [#28265](../sources/prs/sglang/PR-28265.md) | [AMD] refactor sparse MLA decode kernel for Deepseek V4 triton backend | 2026-06-15 | kernel-fusion | attention, mla, reduction |
| [#28302](../sources/prs/sglang/PR-28302.md) | [Mamba][GDN] Deduplicate spec conv-window intermediate cache via sliding window layout | 2026-06-15 |  | attention |
| [#28320](../sources/prs/sglang/PR-28320.md) | Fused QK GemmaRMSNorm + RoPE + gate kernel for Qwen3.5 | 2026-06-15 |  | attention, fp4, nvfp4 |
| [#28204](../sources/prs/sglang/PR-28204.md) | Optimize causal Conv3d VAE padding | 2026-06-14 |  |  |
| [#28084](../sources/prs/sglang/PR-28084.md) | [AMD] Fuse topk padded-token masking into a single Triton kernel | 2026-06-12 | kernel-fusion | attention, fp4, fp8 |
| [#28091](../sources/prs/sglang/PR-28091.md) | [LoRA] Fix experimental fast-path multi-adapter correctness + flashinfer 0.6.12 compatibility | 2026-06-12 |  | attention, fp4, fp8 |
| [#28106](../sources/prs/sglang/PR-28106.md) | [attn backend] Make seq_lens_cpu optional in trtllm_mha backend | 2026-06-12 |  | attention, mla, topk |
| [#27862](../sources/prs/sglang/PR-27862.md) | Support speculative decoding on CPU | 2026-06-11 |  | attention, sort, topk |
| [#27919](../sources/prs/sglang/PR-27919.md) | Revert "[AMD] Fix DeepSeek V4 Pro c128 state tensor dtype mismatch error and c4_sparse_raw_indices attribute error in cuda graph phase" | 2026-06-11 |  |  |
| [#27926](../sources/prs/sglang/PR-27926.md) | [DSV4] perf: Make FP8 quant output tensor contiguous | 2026-06-11 |  | fp8, gemm, quantization |
| [#27947](../sources/prs/sglang/PR-27947.md) | [AMD] Fix jit-kernel-unit-test-amd: activation.cuh ROCm build + per_token CUDA-only (R165) | 2026-06-11 |  | fp8, gemm, reduction |
| [#27973](../sources/prs/sglang/PR-27973.md) | [DSV4] Use int64 for compressor out_loc tensors | 2026-06-11 |  | attention, fp4 |
| [#27747](../sources/prs/sglang/PR-27747.md) | fix: DSV4 BCG compress-prefill plan OOB on underfilled (tiny) prefill replay | 2026-06-10 |  | attention, fp4, moe |
| [#27793](../sources/prs/sglang/PR-27793.md) | [AMD][Perf] Tune extend attention block sizes for gfx950 (head_dim > 128) | 2026-06-10 |  | attention, reduction |
| [#27630](../sources/prs/sglang/PR-27630.md) | [AMD] Fuse sigmoid + mul attention output gate into single Triton kernel | 2026-06-09 | kernel-fusion | attention, fp4 |
| [#27636](../sources/prs/sglang/PR-27636.md) | [AMD] Fuse sigmoid + mul into single Triton kernel for shared expert gating | 2026-06-09 | kernel-fusion | attention, fp4 |
| [#27656](../sources/prs/sglang/PR-27656.md) | [AMD][Perf] Fuse QK RMSNorm + gate extraction Triton kernel for Qwen3.5 on HIP | 2026-06-09 | kernel-fusion | attention, fp4 |
| [#27705](../sources/prs/sglang/PR-27705.md) | Fuse the DSA (V3.2, GLM-5.x) indexer Q/K paths into single kernels | 2026-06-09 |  | fp4, fp8, gemm |
| [#27709](../sources/prs/sglang/PR-27709.md) | [Diffusion] fix: cast to float32 (from float64) in triton kernel to unblock torch.compile | 2026-06-09 |  |  |
| [#27720](../sources/prs/sglang/PR-27720.md) | [DeepSeek V3] Defer moe finalize and fused it with main stream add | 2026-06-09 |  | fp4, moe, nvfp4 |
| [#27529](../sources/prs/sglang/PR-27529.md) | [AMD] Fix DeepSeek V4 Pro c128 state tensor dtype mismatch error and c4_sparse_raw_indices attribute error in cuda graph phase | 2026-06-08 |  | attention, sort |
| [#27531](../sources/prs/sglang/PR-27531.md) | [Diffusion] Add SANA-WM with streaming support | 2026-06-08 | pipeline-stages | wgmma |
| [#27553](../sources/prs/sglang/PR-27553.md) | fix: preserve divisible FP8 block K configs on CUDA | 2026-06-08 |  | fp8, quantization |
| [#27599](../sources/prs/sglang/PR-27599.md) | [Spec] Naming cleanup: contiguous draft-loc kernel + `accepted`->`accept` | 2026-06-08 |  |  |
| [#27486](../sources/prs/sglang/PR-27486.md) | [spec] Misc defensive guards for EAGLE draft KV indexing | 2026-06-07 |  | topk |
| [#27488](../sources/prs/sglang/PR-27488.md) | [KDA] Add CuteDSL Prefill Kernel on SM100 | 2026-06-07 | pipeline-stages, swizzling | attention, tcgen05, tma |
| [#27429](../sources/prs/sglang/PR-27429.md) | [codex] Centralize more inline Triton kernels | 2026-06-06 |  | attention, mla |
| [#27449](../sources/prs/sglang/PR-27449.md) | [jit-kernel] Support per token group quant 8bit v2 jit kernel | 2026-06-06 |  | fp8, gemm, quantization |
| [#27455](../sources/prs/sglang/PR-27455.md) | [SM120] Add FlashInfer sparse MLA decode for DSv4-Flash | 2026-06-06 |  | attention, block-scale, mla |
| [#27320](../sources/prs/sglang/PR-27320.md) | [perf] parallelize create_flashmla_kv_indices over page-blocks | 2026-06-05 |  | attention |
| [#27329](../sources/prs/sglang/PR-27329.md) | [LoRA] Experimental fast LoRA path with `experimental_sgl_trtllm` MoE backend for FP8 and NVFP4 models | 2026-06-05 | kernel-fusion, swizzling | attention, block-scale, fp4 |
| [#27380](../sources/prs/sglang/PR-27380.md) | [AMD] Add unified kv attention support in dpsk-v4 | 2026-06-05 |  | attention, fp8, sort |
| [#27382](../sources/prs/sglang/PR-27382.md) | [AMD][Perf] Split-KV flash-decode attention for EAGLE target-verify (Triton backend) | 2026-06-05 |  | attention, fp8, reduction |
| [#27392](../sources/prs/sglang/PR-27392.md) | [KDA-Pilot] Add B200 diffusion norm-scale-shift CUDA fast path for Qwen-Image | 2026-06-05 | pipeline-stages |  |
| [#27397](../sources/prs/sglang/PR-27397.md) | Support JIT fused A GEMM (MLA down projection) and support GLM-5 hidden size, SM120 | 2026-06-05 |  | fp4, gemm, mbarrier |
| [#27233](../sources/prs/sglang/PR-27233.md) | [Spec] Fuse small kenrels under `gather_spec_extras`  | 2026-06-04 |  |  |
| [#27277](../sources/prs/sglang/PR-27277.md) | Deepseek v4: support mixed dtype compression states | 2026-06-04 |  | attention, moe, sparse-attention |
| [#27152](../sources/prs/sglang/PR-27152.md) | [bugfix][AMD] AttributeError and warp mask bugs in DeepSeek V4 FP4 indexer | 2026-06-03 |  | fp4 |
| [#27063](../sources/prs/sglang/PR-27063.md) | [AMD] Optimize gpt-oss-120B performance | 2026-06-02 |  | attention, fp4, fp8 |
| [#26894](../sources/prs/sglang/PR-26894.md) | [AMD] Fuse compress norm+rope+hadamard into single Triton kernel | 2026-06-01 | kernel-fusion, pipeline-stages | attention, mla, moe |
| [#26914](../sources/prs/sglang/PR-26914.md) | [AMD] Remove BF16-to-FP32 elementwise cast from compressor GEMM on HIP | 2026-06-01 |  | attention, gemm, mla |
| [#26924](../sources/prs/sglang/PR-26924.md) | [4/N] Qwen3.5Opt: Overlap mamba verify update with draft extend | 2026-06-01 |  | attention, moe |
| [#26929](../sources/prs/sglang/PR-26929.md) | Add stochastic rounding for FP16 Mamba SSM cache | 2026-06-01 |  | attention, fp4, nvfp4 |
| [#26803](../sources/prs/sglang/PR-26803.md) | Add a SimplePhaseChecker for execution-phase assertions | 2026-05-31 |  |  |
| [#26805](../sources/prs/sglang/PR-26805.md) | Add the KV-canary verify JIT kernel and reference implementation | 2026-05-31 |  |  |
| [#26806](../sources/prs/sglang/PR-26806.md) | Add the KV-canary write JIT kernel and reference implementation | 2026-05-31 |  | topk |
| [#26807](../sources/prs/sglang/PR-26807.md) | Add the KV-canary plan JIT kernels | 2026-05-31 | pipeline-stages |  |
| [#26817](../sources/prs/sglang/PR-26817.md) | Add real-data KV verification to the KV-canary | 2026-05-31 |  |  |
| [#26818](../sources/prs/sglang/PR-26818.md) | Add token-id verification to the KV-canary | 2026-05-31 |  |  |
| [#26766](../sources/prs/sglang/PR-26766.md) | [DeepSeek-V4] Fuse UE8M0 scale rounding into FP8 group quantization | 2026-05-30 | kernel-fusion | fp8, gemm, quantization |
| [#26788](../sources/prs/sglang/PR-26788.md) | [JIT Kernel] DeepSeek-V4 DSA indexer: faster top-k + page-table transform (runtime k <= 2048) | 2026-05-30 | kernel-fusion, persistent-kernel, pipeline-stages | attention, sort, topk |
| [#26639](../sources/prs/sglang/PR-26639.md) | [AMD] Enable HiSparse on ROCm | 2026-05-29 |  | fp8, mla, scan |
| [#26671](../sources/prs/sglang/PR-26671.md) | [JIT Kernel][DSv4] Optimize epilogue of c128 | 2026-05-29 |  | reduction |
| [#26733](../sources/prs/sglang/PR-26733.md) | Nemotron perf changes | 2026-05-29 |  | attention, gemm, moe |
| [#26586](../sources/prs/sglang/PR-26586.md) | [KDA] Support KDA packed decode | 2026-05-28 |  | attention |
| [#26588](../sources/prs/sglang/PR-26588.md) | Optimize Gemma4 H200 MoE and extend attention | 2026-05-28 | kernel-fusion | attention, moe, reduction |
| [#26444](../sources/prs/sglang/PR-26444.md) | [Bug Fix] Fix activation.cuh JIT compilation failure on CUDA 13 due to template type/value mismatch | 2026-05-27 |  |  |
| [#26471](../sources/prs/sglang/PR-26471.md) | DeepSeek-V4 Online Compress support MTP | 2026-05-27 |  | attention, fp8, moe |
| [#26473](../sources/prs/sglang/PR-26473.md) | [MoE] Support BF16 standard A2A with DeepGEMM runner | 2026-05-27 |  | attention, fp8, gemm |
| [#26502](../sources/prs/sglang/PR-26502.md) | perf(gemma4): single-launch fused router (topk + softmax + scale) | 2026-05-27 | kernel-fusion | attention, fp4, fp8 |
| [#26383](../sources/prs/sglang/PR-26383.md) | [AMD][DSV4] DSV4 MTP graph + sparse triton attn optimizations | 2026-05-26 | kernel-fusion | attention, mla, sort |
| [#26255](../sources/prs/sglang/PR-26255.md) | [fix] Add support for flashinfer MOE A2A to Qwen3 BF16 model path | 2026-05-25 |  | moe, topk |
| [#26303](../sources/prs/sglang/PR-26303.md) | [MoE] Extend kimi_k2_moe_fused_gate to support 256 experts (MiMo V2 Flash) | 2026-05-25 |  | moe, topk |
| [#26312](../sources/prs/sglang/PR-26312.md) | [mtp] add rejection sampling for speculative decoding | 2026-05-25 | pipeline-stages | fp8 |
| [#26318](../sources/prs/sglang/PR-26318.md) | [diffusion][jit_kernel] perf: varlen FA fast path for USPAttention masked branch | 2026-05-25 | pipeline-stages | attention, flash-attention |
| [#26200](../sources/prs/sglang/PR-26200.md) | [GDN] Support SM100 CuTeDSL GDN Prefill Kernel | 2026-05-24 | pipeline-stages, swizzling | attention, fp8, scan |
| [#26206](../sources/prs/sglang/PR-26206.md) | [GDN] Optimize prefill QKV split dispatch | 2026-05-24 |  | attention, fp8, sort |
| [#26208](../sources/prs/sglang/PR-26208.md) | [AMD] Dsv4/pr2 compressor opt | 2026-05-24 | kernel-fusion | attention, fp8, mla |
| [#26209](../sources/prs/sglang/PR-26209.md) | Add FP4 Indexer for DeepSeek V4 | 2026-05-24 |  | fp4, fp8, moe |
| [#26065](../sources/prs/sglang/PR-26065.md) | [XPU] fix correctness issue of GDN triton kernel for XPU | 2026-05-22 |  | attention |
| [#25920](../sources/prs/sglang/PR-25920.md) | [bugfix] Honor cast_x_before_out_mul in RMSNorm.forward_cuda residual path | 2026-05-21 |  | attention, reduction |
| [#25976](../sources/prs/sglang/PR-25976.md) | [DeepSeek-V4] Add mhc_fused_post_pre kernel | 2026-05-21 |  | attention, gemm |
| [#26000](../sources/prs/sglang/PR-26000.md) | [codex] Centralize Triton utility kernels | 2026-05-21 |  | attention, flash-attention, fp8 |
| [#25835](../sources/prs/sglang/PR-25835.md) | [JIT Kernel] Triton moe fused gate | 2026-05-20 |  | moe, reduction |
| [#25855](../sources/prs/sglang/PR-25855.md) | perf(jit_kernel/deepseek_v4): optimize paged_mqa_metadata | 2026-05-20 |  | attention, scan |
| [#25884](../sources/prs/sglang/PR-25884.md) | [Refactor] major JIT kernel clean up for dsv4 | 2026-05-20 |  | topk |
| [#25898](../sources/prs/sglang/PR-25898.md) | [AMD] Dsv4/pr1 fix run time issue | 2026-05-20 |  | attention, fp8, moe |
| [#25751](../sources/prs/sglang/PR-25751.md) | [Kernel] Add SM90 Q8KV8 FP8 Sparse MLA Prefill JIT Kernel with Tests and Benchmark | 2026-05-19 | double-buffering, pipeline-stages | attention, fp8, gemm |
| [#25763](../sources/prs/sglang/PR-25763.md) | [Feature] Support DeepSeek-V4 Wint4Abf16 and Win4Afp8. | 2026-05-19 |  | fp4, fp8, gemm |
| [#25775](../sources/prs/sglang/PR-25775.md) | [Perf][Qwen3.5] Add case 512 to topkGatingSoftmaxKernelLauncher, | 2026-05-19 |  | moe, topk |
| [#25821](../sources/prs/sglang/PR-25821.md) | [Refactor] Rename NSA → DSA: user-facing aliases, file/class/import rename | 2026-05-19 |  | attention, sparse-attention |
| [#25554](../sources/prs/sglang/PR-25554.md) | amd/deepseek_v4 27/N [fix] Reduce Triton autotune configs for faster first-time server launch | 2026-05-18 | kernel-fusion | attention, fp8, mla |
| [#25695](../sources/prs/sglang/PR-25695.md) | fix (jit kernel): elementwise activation C++ error | 2026-05-18 |  |  |
| [#25532](../sources/prs/sglang/PR-25532.md) | [fp8] SM90 swap-AB scaled_mm dispatch (~1.16x kernel geomean, +5.8-18.5% end-to-end) | 2026-05-17 | persistent-kernel, stream-k | attention, fp8, gemm |
| [#25336](../sources/prs/sglang/PR-25336.md) | [Intel GPU] Enable DeepSeek V4 Inference on XPU | 2026-05-15 | pipeline-stages | attention, block-scale, fp4 |
| [#25418](../sources/prs/sglang/PR-25418.md) | integrate flash_mla_sparse_fwd | 2026-05-15 |  | attention, fp8, moe |
| [#25220](../sources/prs/sglang/PR-25220.md) | Cute-DSL FP8 MQA logits  | 2026-05-14 | persistent-kernel, pipeline-stages, swizzling | fp4, fp8, gemm |
| [#25195](../sources/prs/sglang/PR-25195.md) | [BCG] Support breakable CUDA graph for DeepSeek V4 DP attention | 2026-05-13 |  | attention, fp8 |
| [#25090](../sources/prs/sglang/PR-25090.md) | [AMD] Support triton backend decode context parallel for Qwen3.5 | 2026-05-12 | pipeline-stages | attention, fp4, fp8 |
| [#24933](../sources/prs/sglang/PR-24933.md) | Amd/deepseek v4 rebase main 0509 | 2026-05-11 | pipeline-stages, tile-scheduling | attention, flash-attention, fp8 |
| [#24986](../sources/prs/sglang/PR-24986.md) | [rebase]Deepseek_v4 support w4(mxfp4)a16 on hopper | 2026-05-11 |  | attention, fp4, gemm |
| [#24880](../sources/prs/sglang/PR-24880.md) | [PD & HiSparse] Add DeepSeek V4 support for HiSparse direct Prefill-to-Decode DRAM | 2026-05-10 |  |  |
| [#24755](../sources/prs/sglang/PR-24755.md) | Optimize large add_constant tensors | 2026-05-09 |  |  |
| [#24756](../sources/prs/sglang/PR-24756.md) | Optimize ngram decode token table update | 2026-05-09 |  |  |
| [#24757](../sources/prs/sglang/PR-24757.md) | Optimize ngram decode id computation | 2026-05-09 |  |  |
| [#24692](../sources/prs/sglang/PR-24692.md) | feat: SM120 (Blackwell Desktop) support for DeepSeek-V4 inference | 2026-05-08 |  | attention, fp4, fp8 |
| [#24696](../sources/prs/sglang/PR-24696.md) | [Gemma4] Optimize Gemm4 with fused Q/K/V RMSNorm + per-expert FP8 ckpt loader | 2026-05-08 | kernel-fusion | attention, fp8, moe |
| [#24710](../sources/prs/sglang/PR-24710.md) | [codex] Optimize hidden-size 512 RMSNorm dispatch | 2026-05-08 |  | reduction |
| [#24490](../sources/prs/sglang/PR-24490.md) | Port MXFP4 Marlin MoE support to JIT kernel path | 2026-05-06 |  | fp4, fp8, gemm |
| [#24515](../sources/prs/sglang/PR-24515.md) | LPLB: linear-programming load balancer for MoE expert parallelism | 2026-05-06 |  | attention, gemm, gemv |
| [#24411](../sources/prs/sglang/PR-24411.md) | [diffusion] Fuse LTX2 split rotary embedding | 2026-05-05 | kernel-fusion |  |
| [#24271](../sources/prs/sglang/PR-24271.md) | [KDA] Optimize prefill kernels with diagonal and recompute fuse | 2026-05-02 |  | attention, scan |
| [#24160](../sources/prs/sglang/PR-24160.md) | [lora] Share MoE LoRA Info | 2026-04-30 |  | moe |
| [#24048](../sources/prs/sglang/PR-24048.md) | [VLM] Optimize Gemma4 VLM with PCG and fuse RMSNorm + residual add + scalar | 2026-04-29 | pipeline-stages | moe |
| [#23938](../sources/prs/sglang/PR-23938.md) | Optimize large GroupNorm SiLU apply | 2026-04-28 |  |  |
| [#23961](../sources/prs/sglang/PR-23961.md) | [feat] Init true on policy with qwen_dense | 2026-04-28 |  | attention, moe, reduction |
| [#23965](../sources/prs/sglang/PR-23965.md) | Enable PDL for various kernels in DSV32/GLM5 | 2026-04-28 |  | gemm |
| [#23754](../sources/prs/sglang/PR-23754.md) | [Quantization] add humming quantization kernel | 2026-04-26 |  | moe, quantization, topk |
| [#23686](../sources/prs/sglang/PR-23686.md) | Deepseek_v4 support w4(mxfp4)a16 on hopper | 2026-04-25 |  | fp4, fp8, moe |
| [#23280](../sources/prs/sglang/PR-23280.md) | [XPU] Enable Gemma 4 E2B / E4B / 31B/ 26B-A4B on Intel XPU | 2026-04-20 |  | attention, topk |
| [#23180](../sources/prs/sglang/PR-23180.md) | Speculative decoding support on XPU | 2026-04-19 |  | attention, topk |
| [#22931](../sources/prs/sglang/PR-22931.md) | [Fix/Kernel] Add JIT rmsnorm_hf kernel to fix transformers backend MMLU accuracy regression  | 2026-04-16 |  | quantization, reduction |
| [#23000](../sources/prs/sglang/PR-23000.md) | [Feature] Spec V2 DFlash Support | 2026-04-16 |  | attention, gemm |
| [#22814](../sources/prs/sglang/PR-22814.md) | diffusion: add HunyuanVideo GroupNorm+SiLU fast path | 2026-04-14 |  |  |
| [#22064](../sources/prs/sglang/PR-22064.md) | [Diffusion] Fix weight scale swizzle and add large-M kernel config for FLUX.2-dev-NVFP4 | 2026-04-03 | swizzling | fp4, gemm, nvfp4 |
| [#22079](../sources/prs/sglang/PR-22079.md) | [nvidia] Gemma4 nvfp4 fix | 2026-04-03 |  | attention, fp4, fp8 |
| [#21834](../sources/prs/sglang/PR-21834.md) | [Feature] JIT rmsnorm update (with claude) | 2026-04-01 |  |  |
| [#21654](../sources/prs/sglang/PR-21654.md) | Fused_qknorm_rope kernel optimization: up to 2.4× faster | 2026-03-30 | pipeline-stages | attention, reduction |
| [#21668](../sources/prs/sglang/PR-21668.md) | [XPU] Enable qwen3.5 on XPU | 2026-03-30 |  | attention, sort |
| [#21631](../sources/prs/sglang/PR-21631.md) | [HiCache & JIT Kernel] Refactoring HiCache Write-Back Kernel | 2026-03-29 |  | mla |
| [#21511](../sources/prs/sglang/PR-21511.md) | [AMD] Enable FP8 KV cache and FP8 attention kernel for NSA on MI300/MI355 with TileLang backend | 2026-03-27 |  | attention, fp8, gemm |
| [#21531](../sources/prs/sglang/PR-21531.md) | [JIT Kernel] Migrate dsv3_router_gemm from AOT sgl-kernel to JIT kernel | 2026-03-27 |  | gemm |
| [#21440](../sources/prs/sglang/PR-21440.md) | [Diffusion] Add qknorm rope fuse kernel | 2026-03-26 | kernel-fusion | attention, reduction |
| [#21411](../sources/prs/sglang/PR-21411.md) | [GDN] Fuse GDN kkt + solve_tril into one kernel | 2026-03-25 | kernel-fusion | attention, sort, topk |
| [#21314](../sources/prs/sglang/PR-21314.md) | CUTLASS NVFP4 GEMM improvement of SM120 | 2026-03-24 | stream-k | fp4, fp8, gemm |
| [#21203](../sources/prs/sglang/PR-21203.md) | [KDA] Support CuTeDSL KDA decode kernel | 2026-03-23 |  |  |
| [#21019](../sources/prs/sglang/PR-21019.md) | [Qwen3.5] Fuse split/reshape/cat ops in GDN projection with Triton kernel | 2026-03-20 | kernel-fusion |  |
| [#20887](../sources/prs/sglang/PR-20887.md) | CUTLASS FP8 Blockwise GEMM improvement of SM120 | 2026-03-18 |  | fp8, gemm, topk |
| [#20661](../sources/prs/sglang/PR-20661.md) | Fix(jit): support rmsnorm for hidden_size in {64, 128, 256} | 2026-03-16 |  |  |
| [#20673](../sources/prs/sglang/PR-20673.md) | [Feature][JIT Kernel] Fused TP QK norm For Minimax | 2026-03-16 |  |  |
| [#20479](../sources/prs/sglang/PR-20479.md) | Support Triton MLA FP8 KV cache | 2026-03-13 |  | attention, fp4, fp8 |
| [#20501](../sources/prs/sglang/PR-20501.md) | [Kernel] Fuse temperature + softmax in sampling for decode speedup | 2026-03-13 | kernel-fusion, pipeline-stages | reduction |
| [#20094](../sources/prs/sglang/PR-20094.md) | [diffusion] fix bug of copy_if | 2026-03-07 |  |  |
| [#20012](../sources/prs/sglang/PR-20012.md) | [JIT Kernel] Reland NVFP4 kernels to JIT | 2026-03-06 | swizzling | attention, fp4, gemm |
| [#19945](../sources/prs/sglang/PR-19945.md) | [AMD] Tilelang sparse fwd for dsv32 mi355/mi300 | 2026-03-05 | pipeline-stages | attention, gemm, sort |
| [#19725](../sources/prs/sglang/PR-19725.md) | [SGLang-Diffusion] Fix custom op fake impl missing eps default for torch.compile | 2026-03-03 | pipeline-stages | flash-attention |
| [#19794](../sources/prs/sglang/PR-19794.md) | Add compile-time 256-bit vector guard for pre-Blackwell | 2026-03-03 |  |  |
| [#19652](../sources/prs/sglang/PR-19652.md) | [Feature] NVFP4 Marlin fallback for non-Blackwell GPUs (SM75+) | 2026-03-02 |  | fp4, fp8, gemm |
| [#19549](../sources/prs/sglang/PR-19549.md) | [diffusion][llm] macOS support | 2026-02-28 | pipeline-stages | attention, quantization |
| [#19437](../sources/prs/sglang/PR-19437.md) | [Kernel Slimming] Migrate NVFP4 kernels to JIT | 2026-02-26 | swizzling | fp4, gemm, moe |
| [#19148](../sources/prs/sglang/PR-19148.md) | [DeepSeek-V3.2][JIT-kernel] Support nsa fuse store indexer k cache | 2026-02-22 |  | attention, fp8, quantization |
| [#19059](../sources/prs/sglang/PR-19059.md) | [jit_kernel] Add fused_qknorm_rope JIT kernel | 2026-02-20 |  | moe |
| [#18762](../sources/prs/sglang/PR-18762.md) | [diffusion] Diffusion norm fusion for z-image | 2026-02-13 |  | attention |
| [#18612](../sources/prs/sglang/PR-18612.md) | [Perf][Kernel] Fuse SiLU+Mul into NVFP4 Expert Quantization for CUTLASS MoE | 2026-02-11 | kernel-fusion, pipeline-stages, swizzling | block-scale, fp4, gemm |
| [#18488](../sources/prs/sglang/PR-18488.md) | Tilelang sparse decode fwd for dsv32 mi355 | 2026-02-09 |  | attention, gemm, reduction |
| [#18496](../sources/prs/sglang/PR-18496.md) | [FIX] Correct JIT kernel compilation on newer GPUs with outdated driver metadata. | 2026-02-09 |  |  |
| [#18442](../sources/prs/sglang/PR-18442.md) | feat: add FA4 SM90 paged KV decode support & update attention docs | 2026-02-08 |  | attention, flash-attention, fp4 |
| [#18311](../sources/prs/sglang/PR-18311.md) | [Hicache & JIT_kernel] Support page first layout  & mla jit kernel | 2026-02-05 |  | mla |
| [#18073](../sources/prs/sglang/PR-18073.md) | [Diffsuion & JIT_kernel] QKNorm cross heads kernel | 2026-02-01 |  | reduction |
| [#17889](../sources/prs/sglang/PR-17889.md) | [Move sgl-kernel Kernel to JIT] Add JIT concat MLA kernels | 2026-01-28 |  | mla |
| [#17838](../sources/prs/sglang/PR-17838.md) | Feature/support longcat flash lite | 2026-01-27 |  |  |
| [#17554](../sources/prs/sglang/PR-17554.md) | Kernel: optimize decoding metadata in NSA multi-spec backend with fused kernels | 2026-01-22 | kernel-fusion | attention, fp8, sparse-attention |
| [#17449](../sources/prs/sglang/PR-17449.md) | Add mxfp8 support for online quantization, Triton dense linear, and CUTLASS MoE | 2026-01-21 |  | block-scale, fp4, fp8 |
| [#17353](../sources/prs/sglang/PR-17353.md) | Move fa4 from sgl-kernel to jit kernel | 2026-01-19 | double-buffering, pipeline-stages, swizzling | attention, flash-attention, fp8 |
| [#16723](../sources/prs/sglang/PR-16723.md) | [Rework] Add SwapAB Optimization for triton fused_moe_kernel on SM90. | 2026-01-08 |  | moe |
| [#16162](../sources/prs/sglang/PR-16162.md) | [Feature] add aligned_vector type for JIT kernel | 2025-12-30 |  |  |
| [#16043](../sources/prs/sglang/PR-16043.md) | optimize get_topk_ragged by fusing get k and k_scale triton kernel | 2025-12-29 |  | attention |
| [#15888](../sources/prs/sglang/PR-15888.md) | [diffusion] model: support TurboWan2.1-T2V-1.3B/14B SLA | 2025-12-26 |  | attention, sparse-attention, topk |
| [#15835](../sources/prs/sglang/PR-15835.md) | [Feature] JIT Fused QK norm + qk norm clean up | 2025-12-25 | persistent-kernel |  |
| [#15836](../sources/prs/sglang/PR-15836.md) | [JIT kernel] Apply jit per_tensor_quant_fp8 kernel | 2025-12-25 |  | gemm |
| [#15712](../sources/prs/sglang/PR-15712.md) | Add SwapAB Optimization for triton fused_moe_kernel on SM90. | 2025-12-24 |  | attention, fp8, moe |
| [#15631](../sources/prs/sglang/PR-15631.md) | [jit-kernel] Add CuTe DSL GDN Decode Kernel | 2025-12-22 |  | sort |
| [#15522](../sources/prs/sglang/PR-15522.md) | Optimize FP8 MLA KV cache writes with Triton kernel | 2025-12-20 |  | attention, fp8, mla |
| [#15539](../sources/prs/sglang/PR-15539.md) | MoE: Skip SiLU/GELU activation for masked experts | 2025-12-20 |  | moe |
| [#15471](../sources/prs/sglang/PR-15471.md) | [sgl-kernel][6/7]Support Expert Specialization Grouped GEMM | 2025-12-19 |  | fp8, gemm, grouped-gemm |
| [#15306](../sources/prs/sglang/PR-15306.md) | Fix warp illegal instruction in kimi k2 thinking PCG | 2025-12-17 |  | moe, topk |
| [#15141](../sources/prs/sglang/PR-15141.md) | [sgl-kernel][1/2] Fused qk_norm_rope for GLM4.6 | 2025-12-15 |  | attention, fp8, moe |
| [#15182](../sources/prs/sglang/PR-15182.md) | [NVIDIA] upstream FA4 | 2025-12-15 |  | attention, flash-attention, tma |
| [#14717](../sources/prs/sglang/PR-14717.md) | [diffusion] kernel fusion: gated residual layernorm scale shift and layernorm scale shift kernel fusion for Qwen-Image, WAN and HunyuanVideo | 2025-12-09 | kernel-fusion, pipeline-stages |  |
| [#14640](../sources/prs/sglang/PR-14640.md) | [sgl-kernel][Feat][B200][2/N] Support MXFP8 Grouped GEMM in Blackwell | 2025-12-08 |  | gemm, grouped-gemm |
| [#14311](../sources/prs/sglang/PR-14311.md) | [Fix] add block size logic for sm120 smem size | 2025-12-02 |  | attention |
| [#14194](../sources/prs/sglang/PR-14194.md) | [feature] implement dcp for deepseek_v2 | 2025-12-01 |  | attention, reduction, sort |
| [#14224](../sources/prs/sglang/PR-14224.md) | [bug fix] fix ima with get_mla_kv_buffer_kernel overflow | 2025-12-01 |  | attention, sort |
| [#14122](../sources/prs/sglang/PR-14122.md) | Add new moe wna16 marlin gemm | 2025-11-29 |  | fp4, gemm, moe |
| [#14133](../sources/prs/sglang/PR-14133.md) | Opt moe align block size kernel | 2025-11-29 |  | moe, reduction, topk |
| [#14105](../sources/prs/sglang/PR-14105.md) | [LoRA][III] Add LoRA support for MoE layers and enable TP | 2025-11-28 |  | gemm, moe, quantization |
| [#13959](../sources/prs/sglang/PR-13959.md) | [DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache | 2025-11-26 |  | attention, fp8, moe |
| [#13969](../sources/prs/sglang/PR-13969.md) | [kernel][moe] add moe topk fast | 2025-11-26 |  | moe, topk |
| [#13731](../sources/prs/sglang/PR-13731.md) | [sgl-kernel][Feat][B200][1/N]Support MXFP8 Grouped GEMM in Blackwell | 2025-11-21 |  | block-scale, gemm, grouped-gemm |
| [#13049](../sources/prs/sglang/PR-13049.md) | Support moe topk sigmoid kernel | 2025-11-11 |  | moe, reduction, topk |
| [#12581](../sources/prs/sglang/PR-12581.md) | [NVIDIA] Fix CUDA arch requirement in nvfp4 cast | 2025-11-04 |  | fp4, gemm, nvfp4 |
| [#12453](../sources/prs/sglang/PR-12453.md) | [Fix] `concat_mla_absorb_q_kernel` fails for long inputs | 2025-10-31 |  | attention |
| [#12080](../sources/prs/sglang/PR-12080.md) | [sgl-kernel][4/N]Support Expert Specialization Grouped GEMM | 2025-10-24 |  | gemm, grouped-gemm, moe |
| [#11737](../sources/prs/sglang/PR-11737.md) | support cutlass fp4 kernel in sm120 | 2025-10-17 | tile-scheduling | attention, fp4, gemm |
| [#11655](../sources/prs/sglang/PR-11655.md) | [DeepseekV32] Enable flashmla_prefill kernel with fp8 kvcache | 2025-10-15 | kernel-fusion | attention, fp4, fp8 |
| [#11664](../sources/prs/sglang/PR-11664.md) | Use trtllm_mla decode kernel for draft extend in speculative decoding | 2025-10-15 |  | attention, fp8 |
| [#11432](../sources/prs/sglang/PR-11432.md) | [sgl-kernel][1/N]Support Expert Specialization Grouped GEMM | 2025-10-10 |  | fp8, gemm, grouped-gemm |
| [#11287](../sources/prs/sglang/PR-11287.md) | [NVIDIA] Add new SMs support for Spark & Thor | 2025-10-07 |  | gemm |
| [#10714](../sources/prs/sglang/PR-10714.md) | Optimize cutlass int8 gemm kernel for large M on SM89 Ada GPU | 2025-09-21 |  | gemm |
| [#10543](../sources/prs/sglang/PR-10543.md) | [sgl-kernel] Optimize concat_mla_k kernel | 2025-09-17 |  | attention, fp8, quantization |
| [#10491](../sources/prs/sglang/PR-10491.md) | Update CUTLASS. Refine KernelSchedule for fp8 (grouped) gemm. | 2025-09-16 |  | fp8, gemm, moe |
| [#10426](../sources/prs/sglang/PR-10426.md) | Fix correction bias undefined behavior for nvfp4 models | 2025-09-14 |  | fp4, moe, nvfp4 |
| [#10101](../sources/prs/sglang/PR-10101.md) | Optimize nvfp4 block scaled gemm kernel when M is small. | 2025-09-06 |  | block-scale, fp4, gemm |
| [#10058](../sources/prs/sglang/PR-10058.md) | Disable kernel cutlass_mla_decode on SM103 | 2025-09-05 |  | attention |
| [#10078](../sources/prs/sglang/PR-10078.md) | feat: Add FP4 (E2M1) KV Cache Support with Quantization Utilities for MLA | 2025-09-05 |  | attention, fp4, fp8 |
| [#9969](../sources/prs/sglang/PR-9969.md) | CUTLASS fp8 blockwise gemm support of sm120 | 2025-09-03 |  | fp8, gemm |
| [#9807](../sources/prs/sglang/PR-9807.md) | Make fp4_quantize kernels work on sm103 | 2025-08-30 |  | fp4, gemm |
| [#9824](../sources/prs/sglang/PR-9824.md) | [Model] Support Meituan LongCat-Flash && LongCat-Flash-MTP | 2025-08-30 |  | moe |
| [#9789](../sources/prs/sglang/PR-9789.md) | Make sm100 fp8 kernels available on sm103 | 2025-08-29 |  | fp8, gemm, moe |
| [#9556](../sources/prs/sglang/PR-9556.md) | [NVIDIA] [2/N] Optimize `silu_and_mul_scaled_fp4_grouped_quant` perf | 2025-08-24 |  | fp4, gemm, nvfp4 |
| [#9559](../sources/prs/sglang/PR-9559.md) | Update CUTLASS 4.2 & Enable K-Major Scale Factor for SM90 FP8 Blockwise Group GEMM | 2025-08-24 |  | fp8, gemm, moe |
| [#9477](../sources/prs/sglang/PR-9477.md) | Optimize moe_sum_reduce_kernel | 2025-08-22 |  | moe |
| [#9403](../sources/prs/sglang/PR-9403.md) | [sgl-kernel] feat: Support sm120 cutlass fp8 gemm kernel | 2025-08-20 | tile-scheduling | fp8, gemm, quantization |
| [#9272](../sources/prs/sglang/PR-9272.md) | [fix]:  fix cutlass moe ut and and Opt H20 cutlass groupGemm performance | 2025-08-17 |  | gemm, moe |
| [#9200](../sources/prs/sglang/PR-9200.md) | [NVIDA] [1/N] Nvfp4 Masked Gemm: Add quant op for the flashinfer grouped gemm | 2025-08-14 | swizzling | fp4, fp8, gemm |
| [#8962](../sources/prs/sglang/PR-8962.md) | optimize: reduce shulffle and quantization overhead in cutlass_moe sm90 | 2025-08-08 |  | quantization, topk |
| [#8818](../sources/prs/sglang/PR-8818.md) | [Perf] Tunings for SM100 FP8 CUTLASS kernel | 2025-08-05 | tile-scheduling | fp8, gemm |
| [#8130](../sources/prs/sglang/PR-8130.md) | [sgl-kernel] Opt per_token_quant_fp8 with warp reduce | 2025-07-18 |  | fp8, gemm, quantization |
| [#8118](../sources/prs/sglang/PR-8118.md) | [feat] Support tp mode for DeepSeek-R1-W4AFP8 | 2025-07-17 |  | gemm, moe |
| [#8127](../sources/prs/sglang/PR-8127.md) | [Fix][Ready]Fix register spilling in cutlass nvfp4 gemm kernel on Blackwell | 2025-07-17 |  | fp4, gemm, nvfp4 |
| [#7884](../sources/prs/sglang/PR-7884.md) | [kernel] opt moe align block kernel by block/warp scan algorithm | 2025-07-09 |  | moe, scan, topk |
| [#7762](../sources/prs/sglang/PR-7762.md) | feat: support DeepSeek-R1-W4AFP8 model with ep-moe mode | 2025-07-04 |  | attention, fp8, gemm |
| [#7772](../sources/prs/sglang/PR-7772.md) | [1/n]: add cutlass W4A8 moe kernel for hopper architecture | 2025-07-04 |  | fp8, gemm, grouped-gemm |
| [#7627](../sources/prs/sglang/PR-7627.md) | Add dsv3 router gemm kernel | 2025-06-29 |  | fp4, gemm, reduction |
| [#7630](../sources/prs/sglang/PR-7630.md) | Add dsv3 fused a gemm to sgl-kernel | 2025-06-29 | swizzling | fp4, gemm, mbarrier |
| [#7437](../sources/prs/sglang/PR-7437.md) | Fuse sorted_token_ids padding to moe_align_block_size kernel | 2025-06-22 |  | moe, topk |
| [#7444](../sources/prs/sglang/PR-7444.md) | fix: fix apply_shuffle_mul_sum | 2025-06-22 |  | moe, topk |
| [#7278](../sources/prs/sglang/PR-7278.md) | Add CUTLASS FP8 Blockscale MoE kernel for Hopper architecture | 2025-06-17 |  | block-scale, fp8, gemm |
| [#7172](../sources/prs/sglang/PR-7172.md) | Support new DeepGEMM | 2025-06-14 |  | quantization |
| [#7057](../sources/prs/sglang/PR-7057.md) | Tiny fix cutlass_mla_get_workspace_size stub incorrect signature | 2025-06-10 |  | attention |
| [#6958](../sources/prs/sglang/PR-6958.md) | chore: upgrade flashinfer v0.2.6.post1 jit | 2025-06-08 |  |  |
| [#6970](../sources/prs/sglang/PR-6970.md) | Fuse routed scaling factor in deepseek | 2025-06-08 |  | moe |
| [#6916](../sources/prs/sglang/PR-6916.md) | Add a CUDA kernel for fusing mapping and weighted sum for MoE. | 2025-06-06 |  | gemm, moe, reduction |
| [#6919](../sources/prs/sglang/PR-6919.md) | [sgl-kernel] Add cuda kernel for moe_ep_silu_and_mul | 2025-06-06 |  | moe |
| [#6929](../sources/prs/sglang/PR-6929.md) | [perf][sgl-kernel] extend cutlass_mla_decode to support num_head < 128 | 2025-06-06 |  | attention, mla |
| [#6858](../sources/prs/sglang/PR-6858.md) | fix ep_moe_reorder kernel bugs | 2025-06-04 |  | moe, topk |
| [#6821](../sources/prs/sglang/PR-6821.md) | feat: integrate deepgemm into EPMoE | 2025-06-03 |  | attention, gemm, grouped-gemm |
| [#6837](../sources/prs/sglang/PR-6837.md) | [EP] Add cuda kernel for moe_ep_post_reorder | 2025-06-03 |  | moe, topk |
| [#6842](../sources/prs/sglang/PR-6842.md) | Fix AWQ Dequant and Weight Loading of deepseek v2 | 2025-06-03 |  | gemm |
| [#6782](../sources/prs/sglang/PR-6782.md) | Support token-level quantization for EP MoE | 2025-05-30 |  | moe, quantization |
| [#6736](../sources/prs/sglang/PR-6736.md) | Set `num_fused_shared_experts` as `num_shared_experts` when shared_experts fusion is not disabled | 2025-05-29 |  | moe, topk |
| [#6699](../sources/prs/sglang/PR-6699.md) | [EP] Add cuda kernel for moe_ep_pre_reorder | 2025-05-28 |  | moe, topk |
| [#6627](../sources/prs/sglang/PR-6627.md) | Refine pre_reorder_triton_kernel slightly to improve performance | 2025-05-26 |  | moe |
| [#6449](../sources/prs/sglang/PR-6449.md) | Fix bug of deepseek-v3 under DP+EP mode with large batchsize/seqlen | 2025-05-20 |  | attention, gemm, moe |
| [#6369](../sources/prs/sglang/PR-6369.md) | reduce torch.zeros overhead in moe align block size kernel | 2025-05-17 |  | moe |
| [#6336](../sources/prs/sglang/PR-6336.md) | Upgrade  CUTLASS 4.0 | 2025-05-15 |  | gemm |
| [#6093](../sources/prs/sglang/PR-6093.md) | [1/2] Add Kernel support for Cutlass based Fused FP4 MoE | 2025-05-07 | swizzling, tile-scheduling | block-scale, fp4, fp8 |
| [#6101](../sources/prs/sglang/PR-6101.md) | Cutlass MLA: Disable split kv due to https://github.com/NVIDIA/cutlass/issues/2274 | 2025-05-07 |  | attention, mla |
| [#6004](../sources/prs/sglang/PR-6004.md) | chore: upgrade cutlass 3.9.2 | 2025-05-04 |  | gemm |
| [#5820](../sources/prs/sglang/PR-5820.md) | cutlass 3.9 supported to improve fp8_blockwise_gemm | 2025-04-28 | persistent-kernel | fp8, gemm |
| [#5748](../sources/prs/sglang/PR-5748.md) | Fuse MLA set kv cache kernel | 2025-04-25 |  | mla |
| [#5694](../sources/prs/sglang/PR-5694.md) | [2/2] Add python wrapper for CUTLASS FP8 Blockscale MoE Kernel.  | 2025-04-24 |  | attention, block-scale, fp8 |
| [#5432](../sources/prs/sglang/PR-5432.md) | [perf] introduce deep gemm group_gemm_masked as bmm | 2025-04-15 |  | attention, fp8, gemm |
| [#5370](../sources/prs/sglang/PR-5370.md) | [perf] experimental enhance fp8 per-tensor quant | 2025-04-14 |  | fp8, mla, quantization |
| [#5331](../sources/prs/sglang/PR-5331.md) | fix: solve cu118 issue for cutlass mla | 2025-04-12 |  | attention, mla |
| [#5281](../sources/prs/sglang/PR-5281.md) | [1/2] Add FP8 Blockscale MoE CUTLASS kernel for Blackwell | 2025-04-11 | tile-scheduling | block-scale, fp8, gemm |
| [#5113](../sources/prs/sglang/PR-5113.md) | Support MHA with chunked prefix cache for DeepSeek chunked prefill | 2025-04-07 | pipeline-stages | attention, flash-attention, gemm |
| [#5142](../sources/prs/sglang/PR-5142.md) | Blackwell Cutlass MLA kernel | 2025-04-07 | tile-scheduling | attention, flash-attention, mla |
| [#5086](../sources/prs/sglang/PR-5086.md) | reduce moe_align_block_size_kernel small batch mode overhead | 2025-04-05 |  | moe, topk |
| [#4953](../sources/prs/sglang/PR-4953.md) | [Build] Fix cuda12.8 build error in nvfp4_scaled_mm_kernels.cu | 2025-03-31 |  | gemm |
| [#4887](../sources/prs/sglang/PR-4887.md) | Feat/support encoder model (like bert) | 2025-03-29 |  | attention |
| [#4706](../sources/prs/sglang/PR-4706.md) | support cmake for sgl-kernel | 2025-03-24 |  | attention, moe |
| [#4530](../sources/prs/sglang/PR-4530.md) | Add deepseek style fused moe group gate selection kernel | 2025-03-18 |  | moe, topk |
| [#4558](../sources/prs/sglang/PR-4558.md) | Support fp8 gemm for blackwell | 2025-03-18 | tile-scheduling | fp8, gemm |
| [#4278](../sources/prs/sglang/PR-4278.md) | Support Blackwell Block Scale FP8 Gemm | 2025-03-10 | persistent-kernel | block-scale, fp8, gemm |
| [#4231](../sources/prs/sglang/PR-4231.md) | fix per_token_group_quant_fp8 illegal memory when num_groups % 16 != 0 | 2025-03-09 |  | gemm |
| [#4199](../sources/prs/sglang/PR-4199.md) | linear support deepgemm | 2025-03-08 |  | gemm, quantization |
| [#4215](../sources/prs/sglang/PR-4215.md) | Accelerate FP8 CUDA Kernel by 20-28% | 2025-03-08 |  | fp8, gemm, moe |
| [#3888](../sources/prs/sglang/PR-3888.md) | [Feature] DeepSeek V3/R1 INT8 Quantization (channel-wise)  | 2025-02-26 |  | fp8, moe, quantization |
| [#3899](../sources/prs/sglang/PR-3899.md) | Support FP4 gemm (1/2) | 2025-02-26 | swizzling | fp4, fp8, gemm |
| [#3730](../sources/prs/sglang/PR-3730.md) | Feature DeepSeek V3/R1 INT8 Quantization (block-wise) | 2025-02-20 |  | fp8, moe, quantization |
| [#3529](../sources/prs/sglang/PR-3529.md) | integrate blockwise fp8 kernel | 2025-02-12 |  | fp8, quantization |
| [#3267](../sources/prs/sglang/PR-3267.md) | support blockwise fp8 matmul kernel | 2025-02-03 | persistent-kernel | fp8, gemm |
| [#3216](../sources/prs/sglang/PR-3216.md) | add tensorrt_llm common and cutlass_extensions as 3rdparty | 2025-01-30 | pipeline-stages, swizzling | fp8, gemm, quantization |
| [#3148](../sources/prs/sglang/PR-3148.md) | Apply sgl w8a8 fp8 kernel | 2025-01-26 |  | fp8, quantization, sort |
| [#3047](../sources/prs/sglang/PR-3047.md) | support w8a8 fp8 kernel with CUTLASS | 2025-01-22 | persistent-kernel, tile-scheduling | fp8, gemm, quantization |
| [#3035](../sources/prs/sglang/PR-3035.md) | Support sm90 Int8 gemm | 2025-01-21 | persistent-kernel, tile-scheduling | gemm, quantization |
| [#2752](../sources/prs/sglang/PR-2752.md) | Support cutlass Int8 gemm | 2025-01-06 |  | gemm, quantization |

<a id="tile-aitilelang"></a>
## tile-ai/tilelang
117 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#3576](../sources/prs/tilelang/PR-3576.md) | [CuTeDSL][Scan] Handle participating thread offsets | 2026-10-20 |  |  |
| [#3474](../sources/prs/tilelang/PR-3474.md) | [Ascend] Allow selecting target for examples | 2026-10-10 |  |  |
| [#3449](../sources/prs/tilelang/PR-3449.md) | [Refactor][CUDA] Split math codegen dispatch | 2026-10-08 |  |  |
| [#3439](../sources/prs/tilelang/PR-3439.md) | [BugFix][CUDA] Gate fp8 T.gemm on SM89 instead of trapping at launch | 2026-10-07 |  | fp8, gemm, tcgen05 |
| [#3430](../sources/prs/tilelang/PR-3430.md) | [CUDA] Enable SM120 block-scaled MMA on SM121 | 2026-10-05 |  | block-scale, fp4, nvfp4 |
| [#3400](../sources/prs/tilelang/PR-3400.md) | [BugFix][CuTeDSL] Elect one grid-barrier leader per block | 2026-10-02 |  |  |
| [#3414](../sources/prs/tilelang/PR-3414.md) | [BugFix] Preserve parameter identity in NVRTC and CuTeDSL wrappers | 2026-10-02 |  | gemm, tma |
| [#3303](../sources/prs/tilelang/PR-3303.md) | [CUDA] Emit packed FP16 and BF16 vector comparisons | 2026-09-29 |  |  |
| [#3308](../sources/prs/tilelang/PR-3308.md) | [Public Release 9/30] Introduce Ascend 950 backend | 2026-09-29 | pipeline-stages, swizzling | attention, block-scale, flash-attention |
| [#3289](../sources/prs/tilelang/PR-3289.md) | [Codegen] Share C-like source emission and preserve import boundaries | 2026-09-27 |  | wgmma |
| [#3257](../sources/prs/tilelang/PR-3257.md) | [CUDA] Support SM120 block-scaled GEMM fragments and odd warp atom grids | 2026-09-20 |  | block-scale, gemm |
| [#3254](../sources/prs/tilelang/PR-3254.md) | [ROCm] Add GLM-5.3 k-pool Top-K transform | 2026-09-19 | pipeline-stages | attention, fp8, gemm |
| [#3248](../sources/prs/tilelang/PR-3248.md) | [BugFix][CUDA] Only emit 256-bit global load/store on SM100+ targets | 2026-09-18 |  |  |
| [#3249](../sources/prs/tilelang/PR-3249.md) | [ROCm] Add safe-gated KDA decode example | 2026-09-18 |  |  |
| [#3237](../sources/prs/tilelang/PR-3237.md) | [Do not review][Op][Language][CUDA] Add common block-scaled GEMM semantics and backend dispatch | 2026-09-16 | swizzling, warp-specialization | block-scale, gemm, mbarrier |
| [#3238](../sources/prs/tilelang/PR-3238.md) | [Transform][CUDA] Plan atomic vector widths from destination addresses | 2026-09-16 |  |  |
| [#3224](../sources/prs/tilelang/PR-3224.md) | [Example] FP8 sparse MLA forward for DeepSeek V3.2 on Hopper | 2026-09-14 | pipeline-stages, swizzling | attention, flash-attention, fp8 |
| [#3206](../sources/prs/tilelang/PR-3206.md) | [BugFix][CUDA] Lower a kernel-body assert to a device-legal check | 2026-09-12 |  |  |
| [#3185](../sources/prs/tilelang/PR-3185.md) | [Refactor] [CUDA] Rename `AutoSchedule` to `AutoWarpSpecialization` | 2026-09-09 |  | gemm |
| [#3186](../sources/prs/tilelang/PR-3186.md) | [Refactor][Language] Make T.Kernel target-neutral with dialect-owned launch annotations | 2026-09-09 | pipeline-stages, swizzling | gemm, reduction |
| [#3171](../sources/prs/tilelang/PR-3171.md) | [Layout] Consider scalar reducer plans in register-count search | 2026-09-06 |  | reduction |
| [#3167](../sources/prs/tilelang/PR-3167.md) | [CI] Validate built wheels on GPU runners in the Dist workflow | 2026-09-04 | pipeline-stages | gemm |
| [#3147](../sources/prs/tilelang/PR-3147.md) | [ROCm] Support DeepSeek-V3.2 Top-K selector | 2026-09-03 |  | sort, topk |
| [#3149](../sources/prs/tilelang/PR-3149.md) | [ROCm] Select feasible flash-decoding tiles | 2026-09-03 |  |  |
| [#3156](../sources/prs/tilelang/PR-3156.md) | [ROCm] Support DeepSeek mHC pre and post kernels | 2026-09-03 |  | gemm |
| [#3158](../sources/prs/tilelang/PR-3158.md) | [Refactor][CUDA] Replace per-lane-count vector constructors with variadic packers | 2026-09-03 |  | fp4, fp8, nvfp4 |
| [#3106](../sources/prs/tilelang/PR-3106.md) | [CUDA] Unify TMA copy lowering on CuTe algebra | 2026-08-28 | swizzling | tma |
| [#3104](../sources/prs/tilelang/PR-3104.md) | [ROCm] Preserve FP8 bits in warp shuffles | 2026-08-27 |  | fp8 |
| [#3089](../sources/prs/tilelang/PR-3089.md) | [Bugfix] Make TMA layouts region-aware to keep slices contiguous | 2026-08-26 | pipeline-stages, warp-specialization | tma |
| [#3074](../sources/prs/tilelang/PR-3074.md) | [Runtime][Cache] Detect and repair corrupted cache entries | 2026-08-24 |  |  |
| [#3059](../sources/prs/tilelang/PR-3059.md) | [Feature] [CUDA] Role-based automatic warp specialization | 2026-08-20 | double-buffering, pipeline-stages, swizzling | flash-attention, gemm, reduction |
| [#2965](../sources/prs/tilelang/PR-2965.md) | [BugFix][Hopper][Blackwell] Read the WGMMA/UMMA K-panel stride from the layout instead of the operand extent | 2026-08-14 | swizzling | block-scale, gemm, tcgen05 |
| [#2960](../sources/prs/tilelang/PR-2960.md) | [Layout][Inference] Add IO-aware cost model for free-mode selection | 2026-08-13 | pipeline-stages, swizzling | fp8, reduction |
| [#2938](../sources/prs/tilelang/PR-2938.md) | [CUDA] Add pre-SM80 fallback for bf16 atomic add | 2026-08-11 |  |  |
| [#2924](../sources/prs/tilelang/PR-2924.md) | [Bugfix] Carry memory_order through vectorized atomic_add | 2026-08-09 |  | tma |
| [#2902](../sources/prs/tilelang/PR-2902.md) | [Example] Generalize TCGEN05 GEMMs for Thor (sm110a) and add Stream-K scheduling | 2026-08-06 | persistent-kernel, pipeline-stages, stream-k | clc, gemm, tcgen05 |
| [#2880](../sources/prs/tilelang/PR-2880.md) | [Layout] Support half-subpartition (M=64) TMEM tiles in tcgen05.ld/st | 2026-08-05 |  | gemm, tcgen05, tmem |
| [#2889](../sources/prs/tilelang/PR-2889.md) | [BugFix][ROCm] Lower vector Select conditions lane-wise | 2026-08-05 |  | fp4, fp8 |
| [#2892](../sources/prs/tilelang/PR-2892.md) | [Feature] Warp specialization schedules and materialization | 2026-08-05 | pipeline-stages, swizzling, tile-scheduling | flash-attention, gemm, mbarrier |
| [#2871](../sources/prs/tilelang/PR-2871.md) | [CuTeDSL] Port backend intrinsics to CUTLASS DSL primitives | 2026-08-04 | swizzling | block-scale, fp4, mbarrier |
| [#2855](../sources/prs/tilelang/PR-2855.md) | [CUDA][ROCm][Metal] Split backend-specific builtin ops | 2026-08-03 | pipeline-stages, swizzling, warp-specialization | block-scale, clc, mbarrier |
| [#2846](../sources/prs/tilelang/PR-2846.md) | [CUDA][TMA] Separate atomic-add dtype support from layout encoding | 2026-08-02 | swizzling | gemm, tma |
| [#2836](../sources/prs/tilelang/PR-2836.md) | [CUDA] Adopt multi-staged buffers in examples | 2026-08-01 | pipeline-stages | attention, flash-attention, fp4 |
| [#2831](../sources/prs/tilelang/PR-2831.md) | [CUDA] Pack logical TMEM buffers into shared `tcgen05.alloc` arenas | 2026-07-31 | pipeline-stages | block-scale, gemm, sort |
| [#2781](../sources/prs/tilelang/PR-2781.md) | [Enhancement] More compile-time guards for architecture-specific CUDA intrinsics | 2026-07-27 |  | block-scale, clc, tcgen05 |
| [#2785](../sources/prs/tilelang/PR-2785.md) | [CUDA] Support arbitrary TMEM layouts | 2026-07-27 | pipeline-stages, warp-specialization | block-scale, clc, gemm |
| [#2768](../sources/prs/tilelang/PR-2768.md) | [BugFix] Add arithmetic operators to vec_type in common.h for CPU codegen | 2026-07-25 |  |  |
| [#2769](../sources/prs/tilelang/PR-2769.md) | [BugFix] Add pre-SM80 fallback for bf16 __hfma | 2026-07-25 |  |  |
| [#2761](../sources/prs/tilelang/PR-2761.md) | [Refactor] Move example-only helpers out of tilelang package | 2026-07-24 |  | gemm, quantization, tma |
| [#2743](../sources/prs/tilelang/PR-2743.md) | [BugFix] Gate TMEM and TMA builtins by CUDA architecture | 2026-07-23 |  | tma, tmem |
| [#2729](../sources/prs/tilelang/PR-2729.md) | [Autotune] Support early_stop in decorator mode and add decorator example | 2026-07-22 | pipeline-stages | gemm |
| [#2723](../sources/prs/tilelang/PR-2723.md) | [Autotune] Add early stop to skip slow configs during benchmark | 2026-07-21 | pipeline-stages | gemm |
| [#2711](../sources/prs/tilelang/PR-2711.md) | [BugFix] Implement atomic load and store for HIP | 2026-07-19 |  |  |
| [#2637](../sources/prs/tilelang/PR-2637.md) | [CUDA] Support fp32x2 ops as reducers | 2026-07-12 |  | reduction |
| [#2553](../sources/prs/tilelang/PR-2553.md) | [Language][Scheduler] Expose scalar tile scheduler state | 2026-07-08 | double-buffering, pipeline-stages, swizzling | gemm |
| [#2515](../sources/prs/tilelang/PR-2515.md) | [Feature] Support iket profiler for CUDA backend | 2026-07-03 |  |  |
| [#2511](../sources/prs/tilelang/PR-2511.md) | [Enhancement] Add optimized fp8↔half/bf16 vectorized and scalar cast codegen | 2026-07-02 |  | fp8 |
| [#2496](../sources/prs/tilelang/PR-2496.md) | [Autotune] Support per-config pass_configs in autotuning | 2026-06-30 | pipeline-stages, warp-specialization | gemm |
| [#2499](../sources/prs/tilelang/PR-2499.md) | [FEATURE] Add block-causal attention for dLLM example | 2026-06-30 | pipeline-stages | attention, gemm |
| [#2473](../sources/prs/tilelang/PR-2473.md) | [Feature] Expose multiple CUDA intrinsics | 2026-06-29 |  |  |
| [#2474](../sources/prs/tilelang/PR-2474.md) | [CUDA] Reduce template include overhead | 2026-06-29 |  | attention, gemm, mbarrier |
| [#2461](../sources/prs/tilelang/PR-2461.md) | [CI][BugFix] Flash bwd varlen: zero-init lse/Delta padding to avoid NaN in Dk | 2026-06-26 |  | attention, flash-attention, gemm |
| [#2449](../sources/prs/tilelang/PR-2449.md) | [Feature][Tool] Add pass_visualizer: structure-tree pass browser | 2026-06-24 | pipeline-stages, warp-specialization | gemm, tma |
| [#2452](../sources/prs/tilelang/PR-2452.md) | [Backend] [CUDA] Support GMMA/UMMA lowering for sliced SMEM layout (actually arbitrary layout) | 2026-06-24 | pipeline-stages, swizzling, warp-specialization | attention, block-scale, flash-attention |
| [#2441](../sources/prs/tilelang/PR-2441.md) | [Feature] Introduce tile scheduler | 2026-06-23 | double-buffering, persistent-kernel, pipeline-stages | block-scale, gemm, tcgen05 |
| [#2445](../sources/prs/tilelang/PR-2445.md) | [CUDA] Remove `__shfl_sync` from `tl_shuffle_elect` | 2026-06-23 | warp-specialization | mbarrier, tma |
| [#2417](../sources/prs/tilelang/PR-2417.md) | [Feature] Support stmatrix m16n8 on Blackwell | 2026-06-18 |  |  |
| [#2392](../sources/prs/tilelang/PR-2392.md) | [CUDA] Add SM75 MMA dispatchers for FP16 accumulation and UINT8 | 2026-06-13 |  | gemm |
| [#2387](../sources/prs/tilelang/PR-2387.md) | [Transform] Materialize kernel launch per backend | 2026-06-12 | pipeline-stages | block-scale, gemm, tcgen05 |
| [#2390](../sources/prs/tilelang/PR-2390.md) | Add assert that block_K is a multiple of micro_size_k in CUDA MMA GEMM backends to prevent silent miscompilation. | 2026-06-12 |  | gemm |
| [#2391](../sources/prs/tilelang/PR-2391.md) | [CUDA] Align swizzled TMA shared buffers | 2026-06-12 | swizzling | tcgen05, tma, wgmma |
| [#2380](../sources/prs/tilelang/PR-2380.md) | [Backend] Support TMA lowering for arbitrary (swizzled) SMEM layout | 2026-06-11 | swizzling | attention, sort, tma |
| [#2369](../sources/prs/tilelang/PR-2369.md) | [BugFix][CuTeDSL] Fix TileKernels scan, optional-shape, and e5m6 paths | 2026-06-10 |  | moe, reduction |
| [#2364](../sources/prs/tilelang/PR-2364.md) | [CUDA] Add SM120 NVF4 block-scale MMA support | 2026-06-09 | pipeline-stages, swizzling, warp-specialization | block-scale, fp4, gemm |
| [#2339](../sources/prs/tilelang/PR-2339.md) | [TileOP] Add SM70 GEMM FMA fallback | 2026-06-05 |  | gemm |
| [#2334](../sources/prs/tilelang/PR-2334.md) | [BugFix] Fix eager JIT sub-btye shape binding | 2026-06-04 |  | block-scale, fp4, fp8 |
| [#2323](../sources/prs/tilelang/PR-2323.md) | [Backend] Add target detector/normalizer registeration and merge ExecutionBackend into backend module | 2026-06-03 |  |  |
| [#2326](../sources/prs/tilelang/PR-2326.md) | [ROCm] Fix scan wavefront dispatch and gfx950 targets | 2026-06-03 |  | fp4 |
| [#2319](../sources/prs/tilelang/PR-2319.md) | [BugFix][CuTeDSL] Complete TileKernels benchmark support | 2026-06-02 |  | fp4, fp8, moe |
| [#2315](../sources/prs/tilelang/PR-2315.md) | [Transform] Place auto WS producers in first warp group | 2026-06-01 | pipeline-stages, warp-specialization | gemm, wgmma |
| [#2300](../sources/prs/tilelang/PR-2300.md) | [Feature] Add read option to TMA store wait | 2026-05-29 |  | tma |
| [#2289](../sources/prs/tilelang/PR-2289.md) | [BugFix][CuTeDSL] Support TileKernels backend cases | 2026-05-28 | pipeline-stages | tma |
| [#2274](../sources/prs/tilelang/PR-2274.md) | [Refactor] Refactor blockscaled TCGEN5, support .f8f6f4/.mxf8f6f4 and restore maint scripts | 2026-05-26 | pipeline-stages | block-scale, fp4, fp8 |
| [#2275](../sources/prs/tilelang/PR-2275.md) | [BugFix][Examples] Align grouped GEMM backward runner arguments | 2026-05-26 | pipeline-stages | gemm, grouped-gemm |
| [#2261](../sources/prs/tilelang/PR-2261.md) | [CuTeDSL] Lower handle_add_byte_offset in Python codegen | 2026-05-25 |  | gemm |
| [#2262](../sources/prs/tilelang/PR-2262.md) | [TileOP] Add scan operators | 2026-05-25 |  |  |
| [#2266](../sources/prs/tilelang/PR-2266.md) | [Bugfix] Fix cached source restore and Metal codegen fallback | 2026-05-25 |  |  |
| [#2252](../sources/prs/tilelang/PR-2252.md) | [Metal] M5 Cooperative Tensor T.gemm | 2026-05-23 | swizzling | gemm |
| [#2245](../sources/prs/tilelang/PR-2245.md) | [Pipeline] Refactor software pipeline transforms | 2026-05-22 | pipeline-stages | mbarrier, tcgen05, tma |
| [#2237](../sources/prs/tilelang/PR-2237.md) | [Pipeline] Support scalar bind-free pipeline annotations | 2026-05-21 | pipeline-stages |  |
| [#2221](../sources/prs/tilelang/PR-2221.md) |   [CuTeDSL] Integrate host codegen call sites | 2026-05-19 | swizzling |  |
| [#2216](../sources/prs/tilelang/PR-2216.md) | [TIR][IR] Update to use tirx | 2026-05-18 | pipeline-stages | attention |
| [#2218](../sources/prs/tilelang/PR-2218.md) | [Python] Drop Python 3.9 support | 2026-05-18 |  |  |
| [#2198](../sources/prs/tilelang/PR-2198.md) | [CUDA] Add native SM75 MMA GEMM support for FP16, INT8 and INT4 | 2026-05-13 |  | gemm |
| [#2176](../sources/prs/tilelang/PR-2176.md) | Optimize disk cache source loading | 2026-05-11 |  | reduction |
| [#2185](../sources/prs/tilelang/PR-2185.md) | [Transform] Rewrite MergeSharedMemoryAllocations with per-epoch liveness | 2026-05-11 | pipeline-stages, warp-specialization | mbarrier, reduction |
| [#2169](../sources/prs/tilelang/PR-2169.md) | [Example] Add CLC-pipelined 2-CTA GEMM example for sm100 | 2026-05-08 | pipeline-stages | clc, gemm, tcgen05 |
| [#2153](../sources/prs/tilelang/PR-2153.md) | [codex] Split GEMM implementations by backend | 2026-05-06 |  | gemm, tcgen05, tmem |
| [#2132](../sources/prs/tilelang/PR-2132.md) | [AMD][CDNA4] Add MXFP4 (FP4 E2M1) support for gfx950 | 2026-04-30 | pipeline-stages | fp4, gemm, quantization |
| [#2112](../sources/prs/tilelang/PR-2112.md) | feat: auto-vectorize bf16/fp16 reduce with packed add2 intrinsics | 2026-04-28 |  | reduction |
| [#2073](../sources/prs/tilelang/PR-2073.md) | [CUDA] Improve int4 GEMM lowering and packed codegen support | 2026-04-21 |  | gemm |
| [#2063](../sources/prs/tilelang/PR-2063.md) | [CUDA] Support int4 `T.gemm` | 2026-04-19 | pipeline-stages | gemm |
| [#2048](../sources/prs/tilelang/PR-2048.md) | [Backend] Refactor gemm_sp | 2026-04-16 |  | gemm, wgmma |
| [#2032](../sources/prs/tilelang/PR-2032.md) | [Feature] Introduce T.tfloat32  data type support | 2026-04-11 |  |  |
| [#2010](../sources/prs/tilelang/PR-2010.md) | [Example] Migrate eligible examples to eager style | 2026-04-03 | persistent-kernel, pipeline-stages, warp-specialization | attention, gemm, gemv |
| [#2003](../sources/prs/tilelang/PR-2003.md) | [Transform] Add InjectTcgen05Fence pass | 2026-03-31 |  | mbarrier, tcgen05, tmem |
| [#1981](../sources/prs/tilelang/PR-1981.md) | [Feature] Support TMA store in T.tma_copy() | 2026-03-27 | pipeline-stages | gemm, mbarrier, tma |
| [#1945](../sources/prs/tilelang/PR-1945.md) | [Feature] Block-scaled GEMM support for MXFP8 on Blackwell | 2026-03-18 | pipeline-stages, swizzling | block-scale, fp8, gemm |
| [#1909](../sources/prs/tilelang/PR-1909.md) | [Feature] Add Producer-Consumer Warp Specialization and T.tma_copy() API | 2026-03-07 | pipeline-stages, warp-specialization | gemm, mbarrier, tma |
| [#1882](../sources/prs/tilelang/PR-1882.md) | [Feature] 2-SM support for TMA, TMEM and TCGEN5MMA on Blackwell | 2026-02-27 | swizzling, warp-specialization | fp8, gemm, tcgen05 |
| [#1874](../sources/prs/tilelang/PR-1874.md) | [Feature] Support cluster launch, query, synchronization and barrier operations | 2026-02-24 |  |  |
| [#1869](../sources/prs/tilelang/PR-1869.md) | [Metal] Add Metal GEMM support with simdgroup_matrix MMA | 2026-02-23 | pipeline-stages | gemm |
| [#1866](../sources/prs/tilelang/PR-1866.md) | [CUDA] Support tcgen5mma gemm ts | 2026-02-22 | pipeline-stages | attention, flash-attention, gemm |
| [#1736](../sources/prs/tilelang/PR-1736.md) | Add swizzle layout detection and automatic merging for layout conflicts | 2026-01-27 | swizzling | attention, flash-attention, gemm |
| [#1667](../sources/prs/tilelang/PR-1667.md) | [Feature] Support `cp.reduce.async.bulk.tensor` | 2026-01-13 | swizzling | attention, flash-attention, tma |
| [#1327](../sources/prs/tilelang/PR-1327.md) | [Enhancement] add more dtype and fix mma.ws for fp16 for tcgen05 | 2025-11-24 | pipeline-stages | fp8, gemm, tcgen05 |
| [#1229](../sources/prs/tilelang/PR-1229.md) | [WIP] support more dtypes for tcgen05 | 2025-11-11 | pipeline-stages | fp8, gemm, tcgen05 |

<a id="triton-langtriton"></a>
## triton-lang/triton
128 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#12389](../sources/prs/triton/PR-12389.md) | [GSan] Use unaligned barriers for warp-specialized synchronization | 2026-10-20 | warp-specialization |  |
| [#12279](../sources/prs/triton/PR-12279.md) | [AMD] NFC: Rename gfx1250 symbols and definitions to CDNA5 | 2026-10-14 | swizzling |  |
| [#12282](../sources/prs/triton/PR-12282.md) | [KERNELS] Expose top-k and reduction compilation controls | 2026-10-14 |  | reduction, topk |
| [#12285](../sources/prs/triton/PR-12285.md) | [KERNELS] Absorb NVFP4 row scales during MXFP8 conversion | 2026-10-14 |  | block-scale, fp4, nvfp4 |
| [#12204](../sources/prs/triton/PR-12204.md) | [KERNELS] Preserve row-scale bias fusion for full epilogues | 2026-10-09 |  |  |
| [#12213](../sources/prs/triton/PR-12213.md) | [triton_kernels] Support four-column Blackwell activation scale alignment | 2026-10-09 | swizzling |  |
| [#12135](../sources/prs/triton/PR-12135.md) | [KERNELS] Support NVFP4 activations with MXFP4 weights by upcasting via MXFP8 | 2026-10-06 | swizzling | block-scale, fp4, fp8 |
| [#12129](../sources/prs/triton/PR-12129.md) | [Standard] Add any/all reductions | 2026-10-05 |  |  |
| [#12132](../sources/prs/triton/PR-12132.md) | [triton_kernels] Preserve feasible Hopper MXFP4 occupancy | 2026-10-05 | persistent-kernel, pipeline-stages | fp4, wgmma |
| [#12088](../sources/prs/triton/PR-12088.md) | [NVIDIA] Use NVVM operations for elementwise lowering | 2026-10-03 | warp-specialization |  |
| [#12089](../sources/prs/triton/PR-12089.md) | [NVIDIA] Use NVVM intrinsics for TF32 rounding | 2026-10-03 |  | tma |
| [#12091](../sources/prs/triton/PR-12091.md) | [NVIDIA] Use NVVM operations for tensor-memory loads | 2026-10-03 | persistent-kernel | reduction |
| [#12078](../sources/prs/triton/PR-12078.md) | [GSan] Use 32-bit atomics for shadow lock | 2026-10-02 |  |  |
| [#12055](../sources/prs/triton/PR-12055.md) | [NVIDIA] Move GSan shared-memory reservation to the launcher | 2026-10-01 |  |  |
| [#12041](../sources/prs/triton/PR-12041.md) | [triton_kernels] Support tiled storage for persistent ragged-K matmul | 2026-09-30 | persistent-kernel, swizzling | tma |
| [#12023](../sources/prs/triton/PR-12023.md) | [GSan] Support graphs of kernel dependencies | 2026-09-29 |  |  |
| [#12032](../sources/prs/triton/PR-12032.md) | [triton_kernels] Use explicit FMA for matmul bias epilogues | 2026-09-29 |  |  |
| [#11992](../sources/prs/triton/PR-11992.md) | [AMD][KERNELS] Disable XCD swizzle on RDNA | 2026-09-28 | swizzling | reduction |
| [#12000](../sources/prs/triton/PR-12000.md) | [Gluon][NVIDIA] Support L2 cache policies on TMA transfers | 2026-09-28 | warp-specialization | reduction, tma |
| [#11973](../sources/prs/triton/PR-11973.md) | [BACKEND] Reject TCGen05 ops on unsupported targets | 2026-09-26 |  | tcgen05 |
| [#11941](../sources/prs/triton/PR-11941.md) | [FRONTEND][NFC] Add TritonSemantic.make_tensor helper function | 2026-09-24 |  |  |
| [#11918](../sources/prs/triton/PR-11918.md) | [Gluon] Skip unsupported cluster sizes in Gluon tests | 2026-09-23 |  | tcgen05 |
| [#11928](../sources/prs/triton/PR-11928.md) | [triton_kernels] Fix gathered activation scale indexing | 2026-09-23 |  | tma |
| [#11914](../sources/prs/triton/PR-11914.md) | Fix FP4 TMA Alignment | 2026-09-22 |  | fp4, tma, tmem |
| [#11892](../sources/prs/triton/PR-11892.md) | Tune Gluon fused MoE for Rubin | 2026-09-21 | double-buffering, swizzling | fp4, moe |
| [#11862](../sources/prs/triton/PR-11862.md) | [KERNELS] Don't take the TMA scatter path on sm_12x | 2026-09-18 |  | tma |
| [#11801](../sources/prs/triton/PR-11801.md) | Preserve source locations for Python 3.13 inspection | 2026-09-15 |  |  |
| [#11774](../sources/prs/triton/PR-11774.md) | [GSan] Add write_once allocations | 2026-09-14 |  |  |
| [#11724](../sources/prs/triton/PR-11724.md) | [KERNELS] Avoid local output allocation for fused communication | 2026-09-11 |  | block-scale, reduction, tma |
| [#11652](../sources/prs/triton/PR-11652.md) | [KERNELS] Support unscaled FP8 E4M3 matmul with FP16/BF16 | 2026-09-09 | persistent-kernel, pipeline-stages | fp4, fp8, reduction |
| [#11668](../sources/prs/triton/PR-11668.md) | [triton_kernels] Add explicit nearest-even NVFP4 scale rounding | 2026-09-09 |  | block-scale, fp4, fp8 |
| [#11670](../sources/prs/triton/PR-11670.md) | [triton_kernels] Avoid Torch imports in numerics and target_info | 2026-09-09 |  |  |
| [#11639](../sources/prs/triton/PR-11639.md) | [GSan] Add configurable per-allocation shadow granularity | 2026-09-08 |  |  |
| [#11648](../sources/prs/triton/PR-11648.md) | [KERNELS] Correct shared-memory budgeting for FP4 reduction epilogues | 2026-09-08 | pipeline-stages, swizzling, warp-specialization | fp4, nvfp4, reduction |
| [#11624](../sources/prs/triton/PR-11624.md) | [Triton] Fix E8M0 scale decoding | 2026-09-07 | persistent-kernel, pipeline-stages | block-scale, fp4, fp8 |
| [#11618](../sources/prs/triton/PR-11618.md) | [KERNELS] Keep scale layout shape calculations in integer arithmetic | 2026-09-06 |  |  |
| [#11619](../sources/prs/triton/PR-11619.md) | [KERNELS] Add broadcastable MX scale pointer helpers | 2026-09-06 | swizzling |  |
| [#11591](../sources/prs/triton/PR-11591.md) | [Language] Add dedicated atomic_{load,store} ops | 2026-09-04 |  |  |
| [#11563](../sources/prs/triton/PR-11563.md) | [KERNELS] Convert between Blackwell FP4 layouts directly | 2026-09-03 | swizzling | fp4 |
| [#11565](../sources/prs/triton/PR-11565.md) | [KERNELS] Accelerate Blackwell and Hopper layout conversions | 2026-09-03 | swizzling | fp4, fp8 |
| [#11576](../sources/prs/triton/PR-11576.md) | [KERNELS] Consolidate Blackwell FP4 layout metadata and tests | 2026-09-03 |  | fp4, reduction, tma |
| [#11493](../sources/prs/triton/PR-11493.md) | [triton_kernels] Enable CLC inner-loop warp specialization | 2026-08-28 | warp-specialization | clc, tma |
| [#11495](../sources/prs/triton/PR-11495.md) | [KERNELS] Fuse forward FP4 layout conversion | 2026-08-28 | swizzling | fp4 |
| [#11496](../sources/prs/triton/PR-11496.md) | [KERNELS] Fuse compact Hopper FP4 inverse layout conversion | 2026-08-28 |  | fp4 |
| [#11504](../sources/prs/triton/PR-11504.md) | [KERNELS] Allow layout conversion into existing storage | 2026-08-28 | swizzling | fp4, fp8 |
| [#11481](../sources/prs/triton/PR-11481.md) | [Membar] Schedule thread synchronization with Membar analysis | 2026-08-27 | warp-specialization | tma, wgmma |
| [#11482](../sources/prs/triton/PR-11482.md) | [Gluon] Expose rich cache policies | 2026-08-27 |  | mbarrier |
| [#11464](../sources/prs/triton/PR-11464.md) | [MEMBAR] Schedule`tcgen05_wait::{ld,st}` | 2026-08-26 |  | attention, tcgen05, tmem |
| [#11445](../sources/prs/triton/PR-11445.md) | [triton_kernels] Support arbitrary top-k widths | 2026-08-25 |  | sort, topk |
| [#11409](../sources/prs/triton/PR-11409.md) | [FRONTEND] Fix tl.softmax normalizing along the wrong axis (#11406) | 2026-08-23 |  | reduction |
| [#11398](../sources/prs/triton/PR-11398.md) | Follow up TheRock runtime support | 2026-08-21 |  |  |
| [#11385](../sources/prs/triton/PR-11385.md) | Represent tt.ptr address space as a named enum | 2026-08-20 |  | tma |
| [#11387](../sources/prs/triton/PR-11387.md) | [KERNELS] Convert Hopper and Blackwell FP4 directly to strided layouts | 2026-08-20 | swizzling | fp4 |
| [#11371](../sources/prs/triton/PR-11371.md) | Fix NVFP4 matmul profiler names | 2026-08-19 |  | block-scale, fp4, nvfp4 |
| [#11345](../sources/prs/triton/PR-11345.md) | [NVIDIA] Reuse TCGen5 A operands across N tiles | 2026-08-18 |  | block-scale, fp4, fp6 |
| [#11347](../sources/prs/triton/PR-11347.md) | Add matmul tuning constraints for swap_xw, group_m and use_output_tma | 2026-08-18 |  | clc, fp4, nvfp4 |
| [#11351](../sources/prs/triton/PR-11351.md) | [GSan] Weaken mbarrier semantics | 2026-08-18 | pipeline-stages | mbarrier, tmem |
| [#11358](../sources/prs/triton/PR-11358.md) | [KERNELS] Fix Blackwell MXFP fused-output tile selection | 2026-08-18 | swizzling | block-scale, tmem |
| [#11360](../sources/prs/triton/PR-11360.md) | [KERNELS] Reduce MXFP4 layout conversion allocations | 2026-08-18 | swizzling | fp4, quantization, reduction |
| [#11303](../sources/prs/triton/PR-11303.md) | [GSan] Fix initial mbarrier phase state | 2026-08-14 |  | mbarrier |
| [#11286](../sources/prs/triton/PR-11286.md) | [triton_kernels] add FP4 matmul metadata | 2026-08-13 |  | fp4, fp8 |
| [#11297](../sources/prs/triton/PR-11297.md) | [GSan] Avoid materializing full pointer tensors for TMA accesses | 2026-08-13 | swizzling | attention, moe, tma |
| [#11253](../sources/prs/triton/PR-11253.md) | [triton_kernels] Raise matmul warp floor | 2026-08-11 |  |  |
| [#11270](../sources/prs/triton/PR-11270.md) | Disable floating-point fusion by default | 2026-08-11 |  | fp4, topk |
| [#11204](../sources/prs/triton/PR-11204.md) | Remove redundant Triton Python guards | 2026-08-07 |  | quantization, reduction |
| [#11213](../sources/prs/triton/PR-11213.md) | [AMD][Gluon] NFC: Migrate consumers to CDNA5 APIs | 2026-08-07 |  |  |
| [#11199](../sources/prs/triton/PR-11199.md) | [GSan] Fix race in gdc_wait handling | 2026-08-06 |  |  |
| [#11176](../sources/prs/triton/PR-11176.md) | Add CLC mode to triton_kernels matmul | 2026-08-05 | persistent-kernel, warp-specialization | clc, tma |
| [#11178](../sources/prs/triton/PR-11178.md) | [AMD] Support warp-based split-k for mxfp fa on gfx1250 | 2026-08-05 |  | attention, fp4, reduction |
| [#11185](../sources/prs/triton/PR-11185.md) | [CI] Reduce warmup overhead and enable AMD warmup | 2026-08-05 |  |  |
| [#11187](../sources/prs/triton/PR-11187.md) | [GSan] Lock once per tensor access | 2026-08-05 |  |  |
| [#11166](../sources/prs/triton/PR-11166.md) | [AMD][Gluon] Fix transposed asymmetric WMMA CTA layout | 2026-08-04 |  | fp4, gemm |
| [#11170](../sources/prs/triton/PR-11170.md) | [Gluon] Expose FPSan embedding operations | 2026-08-04 |  | fp8 |
| [#11171](../sources/prs/triton/PR-11171.md) | [KERNELS] Fix Blackwell NVFP4 x dense matmul tile selection | 2026-08-04 | swizzling | fp4, nvfp4, tmem |
| [#11122](../sources/prs/triton/PR-11122.md) | [PROTON] Intra kernel async event profiling | 2026-07-31 | pipeline-stages, warp-specialization | tcgen05, tma |
| [#11124](../sources/prs/triton/PR-11124.md) | [NVIDIA] Add core Triton CLC support | 2026-07-31 | warp-specialization | clc, tma, tmem |
| [#11135](../sources/prs/triton/PR-11135.md) | [GSan] Model cluster synchronization | 2026-07-31 |  | mbarrier |
| [#11116](../sources/prs/triton/PR-11116.md) |  [NVWS][CLC] Add warp-specilaization to CLC | 2026-07-30 | warp-specialization | block-scale, clc, fp8 |
| [#11084](../sources/prs/triton/PR-11084.md) | [Gluon] Add native packed arithmetic API | 2026-07-29 | warp-specialization | attention, fp4, fp8 |
| [#11098](../sources/prs/triton/PR-11098.md) | [CI] Warm compile-heavy tests in parallel | 2026-07-29 | swizzling | attention, fp4 |
| [#11080](../sources/prs/triton/PR-11080.md) | Fix large ragged NVFP4 tile selection on GB300 | 2026-07-28 | pipeline-stages | fp4, nvfp4, tmem |
| [#11056](../sources/prs/triton/PR-11056.md) | [Reapply][Backend] Fix WarpGroupDotWaitOp semantics when num_warps > 4 | 2026-07-27 |  | wgmma |
| [#11030](../sources/prs/triton/PR-11030.md) | [triton-kernels] Zero padded Blackwell activation scales | 2026-07-24 |  | tmem |
| [#11020](../sources/prs/triton/PR-11020.md) | [GSan][IR] Make GDC ops IR nodes, and support PDL in GSan | 2026-07-23 |  |  |
| [#10941](../sources/prs/triton/PR-10941.md) | [Rubin] Misc MMA enhancement and `mbarrier.arrive.multicast` support | 2026-07-18 |  | fp4, mbarrier, nvfp4 |
| [#10931](../sources/prs/triton/PR-10931.md) | [frontend] Validate 16-byte stride alignment in make_tensor_descriptor | 2026-07-17 |  | tma |
| [#10936](../sources/prs/triton/PR-10936.md) | [NVIDIA] Initial support for Rubin | 2026-07-17 |  | block-scale, fp4, fp8 |
| [#10912](../sources/prs/triton/PR-10912.md) | [AMD]Add Benchmark Utility to MoE and MXFP GEMM Kernels for GFX1250 | 2026-07-16 | swizzling | gemm, moe |
| [#10873](../sources/prs/triton/PR-10873.md) | Avoid output TMA for Blackwell matmul accumulation | 2026-07-14 | persistent-kernel | tma |
| [#10875](../sources/prs/triton/PR-10875.md) | [KERNELS] topk: don't specialize on bitmatrix strides (fixes per-batch-size recompiles) | 2026-07-14 |  | moe, quantization, topk |
| [#10824](../sources/prs/triton/PR-10824.md) | [AMD] Update mxfp fa example | 2026-07-09 | pipeline-stages, swizzling | block-scale, fp4, reduction |
| [#10814](../sources/prs/triton/PR-10814.md) | [TRITON_KERNELS] Prevent padded top-k experts under FPSan | 2026-07-07 |  | sort, topk |
| [#10809](../sources/prs/triton/PR-10809.md) | [AMD] Rewrite gluon partition layout derivation | 2026-07-06 | swizzling |  |
| [#10810](../sources/prs/triton/PR-10810.md) | [AMD][TRITON_KERNELS] Improve MXFP4 matmul_ogs config on RDNA | 2026-07-06 |  | fp4, moe, topk |
| [#10776](../sources/prs/triton/PR-10776.md) | [KERNELS] Fix unnecessary large tensors in reduce_launch_metadata. | 2026-07-02 |  |  |
| [#10721](../sources/prs/triton/PR-10721.md) | [AMD][gfx1250] Refine control knobs for CodeGen | 2026-06-25 |  |  |
| [#10682](../sources/prs/triton/PR-10682.md) | Tune BN512 shuffled MXFP4 matmul | 2026-06-19 |  | fp4 |
| [#10667](../sources/prs/triton/PR-10667.md) | [triton_kernels] Avoid uint32 overflow in _keyed_add | 2026-06-18 |  | scan |
| [#10642](../sources/prs/triton/PR-10642.md) | [GSAN] Harden runtime and expose kernel warmup | 2026-06-17 |  |  |
| [#10650](../sources/prs/triton/PR-10650.md) | Tensor scales in matmul. | 2026-06-17 |  | block-scale, fp4, nvfp4 |
| [#10623](../sources/prs/triton/PR-10623.md) | Remove obsolete empty pad workarounds | 2026-06-16 |  |  |
| [#10634](../sources/prs/triton/PR-10634.md) | float64 matmul support | 2026-06-16 |  | fp4 |
| [#10618](../sources/prs/triton/PR-10618.md) | Reject odd StridedLayout FP4 packing dimensions | 2026-06-15 | swizzling | fp4 |
| [#10620](../sources/prs/triton/PR-10620.md) | [AMD][BACKEND] Add knob to disable expert scheduling mode | 2026-06-15 |  |  |
| [#10600](../sources/prs/triton/PR-10600.md) | [triton_kernels] Preserve Gluon specialization dialect | 2026-06-13 |  |  |
| [#10601](../sources/prs/triton/PR-10601.md) | [FRONTEND] Fix INT_MIN signed overflow in uint_to_uniform_float | 2026-06-13 |  |  |
| [#10562](../sources/prs/triton/PR-10562.md) | Fix matmul launch_metadata for RAGGED_DIMENSION="K". | 2026-06-10 |  |  |
| [#10551](../sources/prs/triton/PR-10551.md) | [Blackwell] Add pass to combine TMEM load followed by row reduction for sm103+ | 2026-06-09 | warp-specialization | attention, fp8, reduction |
| [#10554](../sources/prs/triton/PR-10554.md) | Add direct layout storage shape queries | 2026-06-09 | swizzling | fp4 |
| [#10543](../sources/prs/triton/PR-10543.md) | [AMD][gfx1250] Enable LLVM scheduler and SGPR preload | 2026-06-08 |  |  |
| [#10489](../sources/prs/triton/PR-10489.md) | [kernels] Fix integer overflow in stride calculations | 2026-06-05 |  |  |
| [#10491](../sources/prs/triton/PR-10491.md) | [KERNELS] Triton kernel for BlackwellMXScaleLayout swizzle. | 2026-06-05 | swizzling |  |
| [#10460](../sources/prs/triton/PR-10460.md) | [FPSAN] Revert accidental two-CTA MMAv5 merge | 2026-06-03 |  | moe, tma |
| [#10461](../sources/prs/triton/PR-10461.md) | [FPSAN] Support two-CTA MMAv5 lowering | 2026-06-03 |  | moe, tma, tmem |
| [#10463](../sources/prs/triton/PR-10463.md) | Handle empty matmul outputs with custom layouts | 2026-06-03 | swizzling | tma |
| [#10464](../sources/prs/triton/PR-10464.md) | Fix zero-grid reduce launches for empty shapes | 2026-06-03 |  |  |
| [#10455](../sources/prs/triton/PR-10455.md) | [FPSAN] Support two-CTA MMAv5 lowering | 2026-06-02 |  | moe, tma, tmem |
| [#10432](../sources/prs/triton/PR-10432.md) | Support zero-sized MX layout conversions | 2026-06-01 |  | fp4 |
| [#10428](../sources/prs/triton/PR-10428.md) | Fix Hopper MXFP4 packed value padding | 2026-05-31 | swizzling | fp4 |
| [#10422](../sources/prs/triton/PR-10422.md) | [KERNELS] Adjust warp size to avoid fp8 regression. | 2026-05-30 |  | fp8 |
| [#10427](../sources/prs/triton/PR-10427.md) | Handle zero-size triton_kernels matmul shapes | 2026-05-30 |  | reduction |
| [#10401](../sources/prs/triton/PR-10401.md) | Make `triton_kernels.tensor.convert_layout` idempotent | 2026-05-28 | swizzling | tma |
| [#10405](../sources/prs/triton/PR-10405.md) | [FRONTEND] Add descriptive messages to bare asserts | 2026-05-28 |  |  |
| [#10385](../sources/prs/triton/PR-10385.md) | [KERNELS] fix hopper mxfp4 swizzle bug | 2026-05-27 | swizzling | fp4 |
| [#10386](../sources/prs/triton/PR-10386.md) | [kernels] change heuristic of smem calculation to be more accurate | 2026-05-27 |  | tma |
| [#10380](../sources/prs/triton/PR-10380.md) | [KERNELS] make setting idle sms process-global | 2026-05-26 |  |  |
| [#10382](../sources/prs/triton/PR-10382.md) | Fix K-ragged Blackwell activation scales | 2026-05-26 | swizzling |  |
| [#10361](../sources/prs/triton/PR-10361.md) | [KERNELS] Perf tuning knobs for _reduce_forward kernel. | 2026-05-22 |  |  |

<a id="vllm-projectvllm"></a>
## vllm-project/vllm
750 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#62467](../sources/prs/vllm/PR-62467.md) | [Bugfix][Kernel] persistent_topk: don't select float4 tail lanes past the row length | 2026-10-19 |  | sort, topk |
| [#62126](../sources/prs/vllm/PR-62126.md) | [Kernel] Add FP32 router GEMM support for Step-5 Preview and Muse Spark Open | 2026-10-17 |  | gemm |
| [#62132](../sources/prs/vllm/PR-62132.md) | [Kernel]Add norm fused kernel for Step-5 Preview and Muse Spark Open | 2026-10-17 | kernel-fusion | attention, fp8, gemm |
| [#61944](../sources/prs/vllm/PR-61944.md) | [Bugfix][Kernel] hadacore: don't load past the input on a partial last warp | 2026-10-16 |  | quantization |
| [#62042](../sources/prs/vllm/PR-62042.md) | [Kernel] Add router GEMM kernels for (5120, 256) and BF16 output to ll_bf16_gemm | 2026-10-16 |  | gemm, moe, topk |
| [#62046](../sources/prs/vllm/PR-62046.md) | [Bugfix][Sampler] Carry the boundary tie count across blocks in the split top-p mask kernel | 2026-10-16 | pipeline-stages | reduction, sort |
| [#62074](../sources/prs/vllm/PR-62074.md) | [Model] Add Reflection Beam | 2026-10-16 |  | attention, fp4, fp8 |
| [#61718](../sources/prs/vllm/PR-61718.md) | [Bugfix] Fix NaN output of the Mamba2 chunk scan kernel on sm90 | 2026-10-15 |  | scan, wgmma |
| [#61727](../sources/prs/vllm/PR-61727.md) | Add Step-5 Preview support | 2026-10-15 |  | moe, topk |
| [#61773](../sources/prs/vllm/PR-61773.md) | [Perf][MoE] Skip the TRTLLM fp8-block activation-scale transpose copy | 2026-10-15 |  | fp8, moe, quantization |
| [#61843](../sources/prs/vllm/PR-61843.md) | [Refactor] Remove dead code multiple places | 2026-10-15 |  |  |
| [#61867](../sources/prs/vllm/PR-61867.md) | [Perf] Kimi K3 Specialized Decode: CuTeDSL Optimized GB300 (1.5-2x) | 2026-10-15 | double-buffering, kernel-fusion, swizzling | attention, block-scale, fp4 |
| [#61895](../sources/prs/vllm/PR-61895.md) | [ROCm][Perf] Any-shape low-latency MoE router GEMM on MI355 | 2026-10-15 |  | fp4, fp8, gemm |
| [#61538](../sources/prs/vllm/PR-61538.md) | [MoE] Unify DeepGEMM MegaMoE experts behind one feature-matrix layer; add NVFP4 | 2026-10-14 |  | block-scale, fp4, fp8 |
| [#61601](../sources/prs/vllm/PR-61601.md) | [Perf][Qwen4Exp] Internal prefill checkpoints for the PLE short conv | 2026-10-14 |  | attention, fp8 |
| [#61716](../sources/prs/vllm/PR-61716.md) | [Bugfix][Kernel] silu_and_mul_quant: run the vectorized loop | 2026-10-14 | kernel-fusion | fp8, quantization |
| [#61343](../sources/prs/vllm/PR-61343.md) | [Perf] per_token_group_quant_8bit: multiply by reciprocal instead of dividing per element | 2026-10-13 | kernel-fusion, pipeline-stages | fp8, quantization |
| [#61371](../sources/prs/vllm/PR-61371.md) | [Kernel][DSv4.1] Bump FlashMLA to the 2026.09.30 release and its interleaved V4.1 KV cache | 2026-10-13 |  | attention, fp4, fp8 |
| [#61451](../sources/prs/vllm/PR-61451.md) | [Perf][Spec Decode] Skip bonus-logit reduction for short drafts in rejection sampling | 2026-10-13 |  | reduction |
| [#61497](../sources/prs/vllm/PR-61497.md) | [Perf][Mamba] Reduce host overhead in the Mamba2 Triton SSD prefill path | 2026-10-13 |  | fp4, nvfp4, quantization |
| [#61149](../sources/prs/vllm/PR-61149.md) | [Kernel][Build] Bump DeepGEMM to the 26/09/30 release and adapt the sparse indexer | 2026-10-12 |  | attention, fp4, fp8 |
| [#61161](../sources/prs/vllm/PR-61161.md) | [Bugfix][Spec Decode] Avoid reusing random draws across block verification rounds | 2026-10-12 |  | attention, flash-attention |
| [#61039](../sources/prs/vllm/PR-61039.md) | [Perf][DSv4.1] Length-aware candidate block selection in the decode indexer | 2026-10-11 |  | attention, fp4, moe |
| [#60945](../sources/prs/vllm/PR-60945.md) | [Bugfix] Fix out-of-bounds lookahead in adaptive block verification | 2026-10-10 |  | moe |
| [#60992](../sources/prs/vllm/PR-60992.md) | [Perf][Model][Qwen4Exp] QSA: decode four FP8 e4m3 bytes per register below sm_89 | 2026-10-10 |  | fp4, fp8, nvfp4 |
| [#61004](../sources/prs/vllm/PR-61004.md) | [ROCm][DSv4] Fuse the shared expert into AITER MegaMoE | 2026-10-10 | stream-k | block-scale, fp4, fp8 |
| [#60767](../sources/prs/vllm/PR-60767.md) | [Bugfix][V1] Null sliding-window block-table entries below the window | 2026-10-09 |  | attention, fp4, fp8 |
| [#60927](../sources/prs/vllm/PR-60927.md) | [GLM 5.3 Perf] Handle two elements at the same time for per token group quant, 2.8% E2E ITL improvement | 2026-10-09 |  | fp8, quantization |
| [#60502](../sources/prs/vllm/PR-60502.md) | [Triton] Migrate Triton kernels off tl.make_block_ptr for triton-main compat | 2026-10-08 |  | attention, tma |
| [#60602](../sources/prs/vllm/PR-60602.md) | [Model][Qwen4Exp] FP8 QSA main KV cache on Ampere (sm_80, sm_86) | 2026-10-08 |  | attention, fp4, fp8 |
| [#60647](../sources/prs/vllm/PR-60647.md) | [HiSparse] Own GPU residency instead of editing core block-table rows | 2026-10-08 |  | attention, fp4, fp8 |
| [#60680](../sources/prs/vllm/PR-60680.md) | [Compile] Fix sampler compile warning | 2026-10-08 |  |  |
| [#60721](../sources/prs/vllm/PR-60721.md) | [Misc] Consolidate csrc shared headers and prune dead code | 2026-10-08 |  | attention, fp4, fp8 |
| [#60731](../sources/prs/vllm/PR-60731.md) | [ROCm][Perf][DSv4.1] Mono decode on MI300X and MI325X (gfx942) | 2026-10-08 |  | attention, fp4, fp8 |
| [#60733](../sources/prs/vllm/PR-60733.md) | [Bugfix][MoE] Clamp BLOCK_SIZE_K to the FP8 quantization block in the batched Triton MoE | 2026-10-08 |  | fp8, gemm, moe |
| [#60736](../sources/prs/vllm/PR-60736.md) | [Bugfix][MRV2] Use int64 index mappings to fix row-offset overflow | 2026-10-08 |  |  |
| [#60373](../sources/prs/vllm/PR-60373.md) |   [Bugfix][DCP] Support strided LSE in direct A2A reduction | 2026-10-07 |  | attention, flash-attention, mla |
| [#60156](../sources/prs/vllm/PR-60156.md) | [Bugfix][Attention] Preserve small FP8 softmax weights in Triton attention | 2026-10-06 |  | attention, flash-attention, fp8 |
| [#60027](../sources/prs/vllm/PR-60027.md) | [Perf][Qwen4Exp] Keep the HC up projection on the skinny GEMM path | 2026-10-05 |  | fp4, gemm, nvfp4 |
| [#60043](../sources/prs/vllm/PR-60043.md) | [Core][Mamba] Remove leftovers of mamba_cache_mode="all" | 2026-10-05 |  | attention |
| [#60050](../sources/prs/vllm/PR-60050.md) | [Perf][GDN] Internal prefill checkpoints for the FlashInfer GDN prefill backend | 2026-10-05 |  | attention, fp8 |
| [#60142](../sources/prs/vllm/PR-60142.md) | [Bugfix] Fix Qwen4Exp FP8 PLE pinned lookup kernel failing to compile below SM89 | 2026-10-05 |  | fp4, fp8, nvfp4 |
| [#59923](../sources/prs/vllm/PR-59923.md) | [Perf][DSv4.1] Exchange packed FP8 Engram rows across DP and feed wkv MXFP8 | 2026-10-04 |  | attention, fp4, fp8 |
| [#59962](../sources/prs/vllm/PR-59962.md) | [Bugfix][RecoverSSM] Correct aligned state indices at exact block boundaries | 2026-10-04 |  |  |
| [#59857](../sources/prs/vllm/PR-59857.md) | [Feature][PCP] Add DeepSeek-V4.1-Flash support | 2026-10-03 | pipeline-stages | attention, fp4, moe |
| [#59731](../sources/prs/vllm/PR-59731.md) | [Perf] Tune MoE weighted-sum kernel launch configuration | 2026-10-02 |  | moe, topk |
| [#59732](../sources/prs/vllm/PR-59732.md) | [ROCm][Perf] Fuse main QK-norm/RoPE/gate and KV-cache write into the AMD QSA prepare launch | 2026-10-02 |  | attention, fp4, fp8 |
| [#59737](../sources/prs/vllm/PR-59737.md) | [Perf] Enable PDL for fused MoE top-k gating | 2026-10-02 |  | attention, fp4, fp8 |
| [#59824](../sources/prs/vllm/PR-59824.md) | [ROCm][Kimi-K3] Support DSpark adaptive verification on MI355X | 2026-10-02 |  | attention, fp4, fp8 |
| [#59528](../sources/prs/vllm/PR-59528.md) | [Bugfix] Keep the GLM-5.3 kpool tail and Qwen4 QSA ring out of the null block | 2026-10-01 |  | attention, mla |
| [#59533](../sources/prs/vllm/PR-59533.md) | [Perf][Qwen4Exp] Merge QSA QKVG and indexer QK projections | 2026-10-01 |  | block-scale, fp4, fp8 |
| [#59554](../sources/prs/vllm/PR-59554.md) | [watermarking] Add DFlash support to dual-key gumbel-max watermarking | 2026-10-01 |  |  |
| [#59639](../sources/prs/vllm/PR-59639.md) | [Bugfix][Engram] Fix intermittent Triton 3.8 crash in the lookup kernel | 2026-10-01 |  |  |
| [#59645](../sources/prs/vllm/PR-59645.md) | [Bugfix] Make cooperative TopK exact on candidate overflow | 2026-10-01 |  | fp8, reduction, scan |
| [#59327](../sources/prs/vllm/PR-59327.md) | [Perf][DSv4.1] Faster Engram host lookups: sorted rows, inline big lookups | 2026-09-30 |  | attention, block-scale, fp8 |
| [#59359](../sources/prs/vllm/PR-59359.md) | [Feature][Spec Decode] Support sampling mask replay for MRV2 MTP | 2026-09-30 |  |  |
| [#59377](../sources/prs/vllm/PR-59377.md) | [Kernel][LoRA] Add deterministic split-K=8 LoRA shrink for batch invariance | 2026-09-30 |  | reduction |
| [#59454](../sources/prs/vllm/PR-59454.md) | [Bugfix][ROCm] Use a zero default for masked scales in the MXFP8 GEMM | 2026-09-30 |  | attention, gemm |
| [#59119](../sources/prs/vllm/PR-59119.md) | [DSv4.1] Avoid runtime recompiles of _ring_slot_mapping_kernel | 2026-09-29 |  |  |
| [#59128](../sources/prs/vllm/PR-59128.md) | [Perf][MoE] Skip padded work in block-FP8 DeepGEMM experts | 2026-09-29 |  | fp4, fp8, gemm |
| [#59132](../sources/prs/vllm/PR-59132.md) | [ROCM][Perf] Add ROCM_SEGMENTED_ATTN attention-backend works across RDNA3/3.5/4 | 2026-09-29 |  | attention, fp8, reduction |
| [#59166](../sources/prs/vllm/PR-59166.md) | [Bugfix] Fix DSpark graph-padding handling in the DeepSeek-V4.1 MoE fused top-k | 2026-09-29 |  | attention, moe, quantization |
| [#59235](../sources/prs/vllm/PR-59235.md) | [Bugfix][HiSparse] Resolve MTP verification rows with a union residency kernel | 2026-09-29 |  | attention, fp4, mla |
| [#59285](../sources/prs/vllm/PR-59285.md) | [ROCm][Triton] Migrating MiniMax-M3 kernels from make_block_ptr to tensor descriptors | 2026-09-29 |  | attention, fp4, sparse-attention |
| [#59300](../sources/prs/vllm/PR-59300.md) | [Attention][MiniMax-M3] NVFP4 KV cache on the MSA sparse attention path | 2026-09-29 | swizzling | attention, block-scale, fp4 |
| [#58957](../sources/prs/vllm/PR-58957.md) | [Perf][Qwen4Exp] Fuse HC down projection and SiLU on NVIDIA | 2026-09-28 | kernel-fusion, pipeline-stages, swizzling | gemm, mbarrier, reduction |
| [#59042](../sources/prs/vllm/PR-59042.md) | [Bugfix][MoE] Apply expert_map remapping for CUTLASS FP4 MOE expert parallel | 2026-09-28 |  | fp4, fp8, gemm |
| [#59069](../sources/prs/vllm/PR-59069.md) | [ROCm][Kimi-K3] Fuse AttnRes output with per-token FP8 input quantization | 2026-09-28 |  | fp4, fp8, gemm |
| [#59081](../sources/prs/vllm/PR-59081.md) | [Minimax M3] Enable fp8 indexer cache on triton indexer for non-SM100 architectures.  | 2026-09-28 | pipeline-stages | attention, fp8, topk |
| [#59085](../sources/prs/vllm/PR-59085.md) | [Feature][Attention] Cover a whole spec-verify in one DiffKV split-KV program | 2026-09-28 |  | attention |
| [#58845](../sources/prs/vllm/PR-58845.md) | [GLM 5.3 Perf] Skip qlnorm calculation for MHA, 4.4~7.7% E2E TTFT Improvement | 2026-09-26 |  | attention, quantization |
| [#58651](../sources/prs/vllm/PR-58651.md) | [KimiViT][Perf] Fuse per-layer QK RoPE into one in-place kernel | 2026-09-25 |  |  |
| [#58671](../sources/prs/vllm/PR-58671.md) | [ROCm][DSv4.1] Paged MXFP4 sparse indexer on aiter's MQA-logits kernel | 2026-09-25 |  | attention, fp4, fp8 |
| [#58684](../sources/prs/vllm/PR-58684.md) | [Perf][Attention] Remove D2H sync from FlashInfer SM90 sparse MLA plan under async scheduling | 2026-09-25 |  | attention, fp8, mla |
| [#58737](../sources/prs/vllm/PR-58737.md) | [Perf] Fuse the mamba align block-table gather into one Triton kernel, 7 kernels -> 1, 6x speedup on all shapes for this kernel | 2026-09-25 |  | attention |
| [#58769](../sources/prs/vllm/PR-58769.md) | [ROCm][Triton] Migrate Kimi-K3 kernels from make_block_ptr to tensor … | 2026-09-25 |  |  |
| [#58784](../sources/prs/vllm/PR-58784.md) | [Bugfix][MRV2][Spec Decode] Reject draft slots that were never proposed | 2026-09-25 |  |  |
| [#58510](../sources/prs/vllm/PR-58510.md) | [ROCm][Perf] MXFP8 GEMM on native 32x32 block scales for gfx950 | 2026-09-24 |  | attention, block-scale, fp8 |
| [#58526](../sources/prs/vllm/PR-58526.md) | [Minimax-M3][Perf] Use triton_mrope for vision tower + int64 offset fix for triton_mrope | 2026-09-24 | kernel-fusion |  |
| [#58560](../sources/prs/vllm/PR-58560.md) | [Bugfix][DSv4.1] Keep the compressor ring out of the null block | 2026-09-24 |  | mla |
| [#58584](../sources/prs/vllm/PR-58584.md) | [ROCm][Perf][GLM-5.3-Flash] BF16 splitk kernel for sparse MLA decode | 2026-09-24 |  | attention, mla, reduction |
| [#58605](../sources/prs/vllm/PR-58605.md) | [Perf] Reduce redundant Triton sampler warmup specializations | 2026-09-24 |  | topk |
| [#58621](../sources/prs/vllm/PR-58621.md) | [Perf][DSv4] Fuse inverse RoPE + FP8 quant into FlashInfer sparse MLA | 2026-09-24 | kernel-fusion | attention, fp8, mla |
| [#58634](../sources/prs/vllm/PR-58634.md) | [Perf][DSv4.1] Fuse small-batch WO-A with inverse RoPE and MXFP8 quant on SM100/SM103 | 2026-09-24 | kernel-fusion, pipeline-stages, swizzling | attention, block-scale, fp4 |
| [#58225](../sources/prs/vllm/PR-58225.md) | [Perf][ROCm][Attention] Narrow the Triton prefill-attention KV tile on RDNA3/RDNA4 | 2026-09-23 |  | attention |
| [#58226](../sources/prs/vllm/PR-58226.md) | [Perf] DiffusionGemma: one-pass sampler statistics kernel | 2026-09-23 |  | fp4, nvfp4 |
| [#58231](../sources/prs/vllm/PR-58231.md) | [Bugfix][Sampler] Fix split top-p masking every token for huge logits (thinking_token_budget + spec decode emits token 0) | 2026-09-23 | pipeline-stages | fp8, sort, topk |
| [#58373](../sources/prs/vllm/PR-58373.md) | [Bugfix] Widen ep_gather output offset to int64 | 2026-09-23 |  |  |
| [#58454](../sources/prs/vllm/PR-58454.md) | [Bugfix][GLM-5.3-Flash] kpool corruption with speculative decoding | 2026-09-23 |  | fp8 |
| [#58456](../sources/prs/vllm/PR-58456.md) | [ROCm][DSv4.1][Perf] Emit MXFP8 from the sparse decode reduce and run wo_a as a grouped FP8 GEMM | 2026-09-23 |  | attention, fp8, gemm |
| [#58463](../sources/prs/vllm/PR-58463.md) | [Spec Decode] Remove eager metadata rebuild during MTP fused multi-step decode | 2026-09-23 |  | attention, fp8, moe |
| [#58045](../sources/prs/vllm/PR-58045.md) | [ROCm][Kimi-K3] Optimize low-concurrency speculative KDA | 2026-09-22 | pipeline-stages | fp8 |
| [#58053](../sources/prs/vllm/PR-58053.md) | [Refactor] Abstract DeepGemm MegaMOE backend | 2026-09-22 |  | fp4, fp8, moe |
| [#58058](../sources/prs/vllm/PR-58058.md) | [Bugfix][ROCm] Drop -1 sentinels when building the ragged sparse-MLA indices | 2026-09-22 |  | attention, mla, sparse-attention |
| [#58069](../sources/prs/vllm/PR-58069.md) | [Dependency] Upgrade FlashInfer version to 0.7.0 | 2026-09-22 |  | attention, mla |
| [#58089](../sources/prs/vllm/PR-58089.md) | [ROCm][Bugfix] Keep zero MiniMax MXFP8 activation blocks finite | 2026-09-22 | kernel-fusion | block-scale, quantization |
| [#58128](../sources/prs/vllm/PR-58128.md) | [Attention][Model] FP8 KV cache for Triton DiffKV and MiMo-V2.6-Flash | 2026-09-22 |  | attention, fp8, quantization |
| [#58132](../sources/prs/vllm/PR-58132.md) | [Model] Decoder-side SWA bounded replay for DeepSeek-V4.1 | 2026-09-22 |  | attention, moe |
| [#58194](../sources/prs/vllm/PR-58194.md) | [Perf][Kernel] Vectorized flat abs-max for dynamic per-tensor FP8 quantization | 2026-09-22 |  | fp8, moe, quantization |
| [#58208](../sources/prs/vllm/PR-58208.md) | [ROCm][Perf] Replace torch.topk in DSA candidate block selection | 2026-09-22 |  | attention, sort, topk |
| [#57934](../sources/prs/vllm/PR-57934.md) | [SpecDecode] Add LiLiCorr drafter | 2026-09-21 |  | attention, fp4, nvfp4 |
| [#57947](../sources/prs/vllm/PR-57947.md) | [ROCm][Perf] Reach the fused QSA pre-indexer from the AMD path | 2026-09-21 | kernel-fusion | attention, fp4, fp8 |
| [#57978](../sources/prs/vllm/PR-57978.md) | [ROCm][Perf] Parallelise AITER MLA page-index expansion over token chunks | 2026-09-21 |  | attention, fp8, mla |
| [#58008](../sources/prs/vllm/PR-58008.md) | [ROCm][Perf][GLM-5.3-Flash] "Fit kpool top-k indices to AITER" with a single Triton kernel | 2026-09-21 |  | attention, mla, topk |
| [#57783](../sources/prs/vllm/PR-57783.md) | [Core][KDA] Generalize Mamba prefill checkpoint builder and exporter | 2026-09-20 |  | attention |
| [#57654](../sources/prs/vllm/PR-57654.md) | [Bugfix][CPU] Fix DeepSeek V4.1 import without Triton | 2026-09-19 |  |  |
| [#57667](../sources/prs/vllm/PR-57667.md) | [Bugfix][DSA] Avoid runtime JIT for offset candidate end buffers | 2026-09-19 |  | attention, fp4, fp8 |
| [#57458](../sources/prs/vllm/PR-57458.md) | [Perf][Attention] Reduce GLM sparse MLA preparation overhead | 2026-09-18 |  | attention, fp8, gemm |
| [#57477](../sources/prs/vllm/PR-57477.md) | [Bugfix][GLM-5.3-Flash] Address kpool tail blocks by the padded indexer stride in the NVIDIA prefill seed kernel | 2026-09-18 |  | fp8, mla, topk |
| [#57497](../sources/prs/vllm/PR-57497.md) | [Qwen4Exp][ROCm] PLE n-gram table CPU offload | 2026-09-18 |  | fp4, fp8, nvfp4 |
| [#57534](../sources/prs/vllm/PR-57534.md) | [Perf][GLM] Fuse the kpool tail slot mapping into one Triton kernel | 2026-09-18 |  | attention, fp8, mla |
| [#57603](../sources/prs/vllm/PR-57603.md) | [Perf][DSV4.1] Overlap mHC coefficients for small TP batches | 2026-09-18 | pipeline-stages, swizzling | attention, fp4, fp8 |
| [#57604](../sources/prs/vllm/PR-57604.md) | [Perf][DSV4.1] Optimize MegaMoE staging and NVFP4 cache gathers | 2026-09-18 |  | attention, fp4, fp8 |
| [#57621](../sources/prs/vllm/PR-57621.md) | [Refactor] Remove dead kernel code | 2026-09-18 |  | attention, fp8, quantization |
| [#57273](../sources/prs/vllm/PR-57273.md) | [Perf][Model] Qwen4Exp QSA: sm_90 tuning table for _select_config | 2026-09-17 |  | attention, fp8, reduction |
| [#57329](../sources/prs/vllm/PR-57329.md) | [Feat][Mamba2] Enable internal prefill checkpoints | 2026-09-17 |  | attention, moe |
| [#57377](../sources/prs/vllm/PR-57377.md) | C3x SM100 FP8 blockwise - Pad activation scales to multiple of 4 | 2026-09-17 |  | fp8, quantization |
| [#57428](../sources/prs/vllm/PR-57428.md) | [Kernel][DSV4.1] Fuse MXFP8 wo_b GEMM with sequence-parallel reduce-scatter | 2026-09-17 | kernel-fusion, swizzling | attention, block-scale, fp8 |
| [#57435](../sources/prs/vllm/PR-57435.md) | [ROCm][DSv4.1][Perf] Fuse the inverse RoPE into the sparse decode reduce | 2026-09-17 |  | attention, fp8, mla |
| [#57454](../sources/prs/vllm/PR-57454.md) | [Bugfix][DSv4.1] Preserve NaN-scored candidate block indices | 2026-09-17 |  | attention, topk |
| [#57097](../sources/prs/vllm/PR-57097.md) | [Qwen3.8-Flash-Next] Fuse main QK-norm/RoPE/gate and KV-cache write into the QSA pre-indexer launch | 2026-09-16 | kernel-fusion | attention, fp8, moe |
| [#57107](../sources/prs/vllm/PR-57107.md) | [Perf][Spec Decode] Avoid triton recompiles in the acceptance estimator | 2026-09-16 |  |  |
| [#57152](../sources/prs/vllm/PR-57152.md) | [Bugfix][Model] Restore causal image SWA for DeepSeek V4.1 | 2026-09-16 |  | attention, topk |
| [#57169](../sources/prs/vllm/PR-57169.md) | [KV Cache] GLM-5.3-Flash: use the generic packed KV layout; CircularBufferSpec tail with speculative ring slots | 2026-09-16 |  | attention, fp8, mla |
| [#57199](../sources/prs/vllm/PR-57199.md) | [ROCm][Perf] W4A16: speed up skinny GEMM decode, including speculative batches | 2026-09-16 |  | gemm, quantization |
| [#57212](../sources/prs/vllm/PR-57212.md) | [CI] Ignore ruff D209, rejoin the docstrings it split, and silence incompatible-rule warnings | 2026-09-16 |  |  |
| [#56935](../sources/prs/vllm/PR-56935.md) | [Model][DSv4.1] FlashMLA mega attention and the NVFP4 compressed KV cache | 2026-09-15 | kernel-fusion | attention, fp4, fp8 |
| [#56956](../sources/prs/vllm/PR-56956.md) | [DSpark] Support pipeline-parallel targets in aggregated serving | 2026-09-15 | pipeline-stages | moe, topk |
| [#56974](../sources/prs/vllm/PR-56974.md) | [Bugfix][GLM-5.3-Flash] Keep batch x heads out of gridDim.z in the GLM-5.3-Flash fused recurrent KDA kernel | 2026-09-15 |  | attention |
| [#57057](../sources/prs/vllm/PR-57057.md) | [Attention] Add UltraQuant 4-bit KV cache backend (FlyDSL D=256) | 2026-09-15 | kernel-fusion | attention, fp4, fp8 |
| [#56734](../sources/prs/vllm/PR-56734.md) | [Bugfix][Spec Decode] Stop dummy draft decode steps from writing KV through stale block-table rows | 2026-09-14 |  | attention, fp4, fp8 |
| [#56743](../sources/prs/vllm/PR-56743.md) | [ROCm][Perf] Optimize DSV4.1 K=512 decode top-k on gfx950 | 2026-09-14 |  | attention, sort, topk |
| [#56798](../sources/prs/vllm/PR-56798.md) | [MM] Add Triton kernel for mm_input_normal. | 2026-09-14 | kernel-fusion |  |
| [#56807](../sources/prs/vllm/PR-56807.md) | [watermarking] add context deduplication support to speculative decoding | 2026-09-14 |  | reduction |
| [#56845](../sources/prs/vllm/PR-56845.md) | [Refactor] Remove dead kernel code | 2026-09-14 |  |  |
| [#56893](../sources/prs/vllm/PR-56893.md) | [Model][DSv4.1] Store the whole KV in MXFP8 (FlashMLA V4.1 record) | 2026-09-14 |  | attention, fp4, fp8 |
| [#56685](../sources/prs/vllm/PR-56685.md) | [Feature][Humming] Humming feature integration | 2026-09-13 |  | fp4, gemm, moe |
| [#56720](../sources/prs/vllm/PR-56720.md) | [ROCm][DSv4.1][Perf] One-pass dequantize and a gather-sized grid for the compressed K cache | 2026-09-13 |  | attention, fp4, fp8 |
| [#56723](../sources/prs/vllm/PR-56723.md) | [PCP][DCP] Support DCP target model with non-DCP Dspark | 2026-09-13 |  | attention, flash-attention, mla |
| [#56562](../sources/prs/vllm/PR-56562.md) | [Perf] Fuse DSV4.1 input metadata preparation with Triton | 2026-09-12 |  | attention, fp8, mla |
| [#56579](../sources/prs/vllm/PR-56579.md) | [Bugfix][Attention] Avoid NaN in the Triton softcap for large attention logits | 2026-09-12 |  | attention, fp8 |
| [#56609](../sources/prs/vllm/PR-56609.md) | [Compile] Fix compile warning #177-D | 2026-09-12 |  |  |
| [#56628](../sources/prs/vllm/PR-56628.md) | [ROCm][DSV4.1][Perf] Stride the DSA decode candidate mask over the live context | 2026-09-12 |  | attention, topk |
| [#56633](../sources/prs/vllm/PR-56633.md) | [Perf][DSv4.1] Fold the mHC post block into the delayed pre projection | 2026-09-12 | kernel-fusion | attention, gemm |
| [#56638](../sources/prs/vllm/PR-56638.md) | [ROCm][DSv4.1][Perf] Replace the Torch prefill combine with the shared combine_topk_swa_indices kernel | 2026-09-12 |  | attention, moe, topk |
| [#56441](../sources/prs/vllm/PR-56441.md) | [Perf][DSpark] Add KV-only context insertion across V4.1 cache formats | 2026-09-11 |  | fp8, quantization, reduction |
| [#56478](../sources/prs/vllm/PR-56478.md) | [Kernel][Perf][Quantization] Fix odd-row performance cliff in per-token-group quantization | 2026-09-11 |  | fp8, quantization, reduction |
| [#56503](../sources/prs/vllm/PR-56503.md) | [ROCm][DSV4.1][Perf] Use AITER mHC for the delayed pre block | 2026-09-11 |  | attention, gemm, moe |
| [#56512](../sources/prs/vllm/PR-56512.md) | [DS V4.1][Engram] Support async prefetch for offloaded engram lookups and engram DP sharding | 2026-09-11 |  | fp8 |
| [#56214](../sources/prs/vllm/PR-56214.md) | [Model] Support DeepSeek-V4.1-Flash | 2026-09-10 |  | quantization |
| [#56215](../sources/prs/vllm/PR-56215.md) | [Kernel] Optional Q-norm in fused DSv4 MLA epilogue; group_size=32 for packed FP8 quant | 2026-09-10 |  | attention, fp8, mla |
| [#56227](../sources/prs/vllm/PR-56227.md) | [Feat][Model] Support encoder-side SWA-bounded replay for DeepSeek-V4.1-Flash | 2026-09-10 |  | attention, mla |
| [#56228](../sources/prs/vllm/PR-56228.md) | [Model] DeepSeek-V4.1-Flash Model Definitions | 2026-09-10 | kernel-fusion, swizzling | attention, block-scale, fp4 |
| [#56254](../sources/prs/vllm/PR-56254.md) | [DSA] Wire DeepGEMM sparse MQA logits into the DeepSeek V4.1 indexer | 2026-09-10 | pipeline-stages | attention, fp4, fp8 |
| [#56273](../sources/prs/vllm/PR-56273.md) | [Quantization] Support packed NVFP4 Qwen4Exp PLE embeddings | 2026-09-10 | swizzling | block-scale, fp4, fp8 |
| [#56301](../sources/prs/vllm/PR-56301.md) | [ROCm][Perf] W4A16: pad gfx11 weight and activation strides | 2026-09-10 |  | gemm, quantization |
| [#56322](../sources/prs/vllm/PR-56322.md) | [Qwen4Exp] support Sequence Parallelism for Qwen3.8-Flash-Next | 2026-09-10 |  | fp8, moe |
| [#56323](../sources/prs/vllm/PR-56323.md) | [6/N][warmup][DSv4] Migrate sampling, and DFlash JIT kernels | 2026-09-10 |  |  |
| [#56346](../sources/prs/vllm/PR-56346.md) | [Perf][Kernel] Add sampled filtering for persistent top-k | 2026-09-10 |  | moe, scan, topk |
| [#56061](../sources/prs/vllm/PR-56061.md) | [4/N] Expose HiSparse cache metrics via KV connector stats | 2026-09-09 | pipeline-stages | attention |
| [#56098](../sources/prs/vllm/PR-56098.md) | [ROCm][Bugfix][Perf] Tune multi-stream shared experts use; wvSplitKrc fixes | 2026-09-09 |  | gemm, topk |
| [#56122](../sources/prs/vllm/PR-56122.md) | [watermarking] Dual-key gumbel-max watermarking for speculative decoding support | 2026-09-09 |  |  |
| [#56148](../sources/prs/vllm/PR-56148.md) | [Attention][Spec Decode] Multi-query Triton split-K for spec-decode verify, with empty-segment/padding hardening | 2026-09-09 |  | attention, fp4, fp8 |
| [#56151](../sources/prs/vllm/PR-56151.md) | [Perf][MiniMax-M3] Triton indexer: decode grid retune + SM12.0 split-K | 2026-09-09 |  | attention, fp4, fp8 |
| [#56157](../sources/prs/vllm/PR-56157.md) | [PCP][DCP] Enable PCP+DCP on sparse-MLA models | 2026-09-09 |  | attention, fp4, mla |
| [#55899](../sources/prs/vllm/PR-55899.md) | [Perf] Improve BF16x3 router GEMM accuracy and make it default on sm100 | 2026-09-08 |  | gemm, tcgen05, tmem |
| [#55921](../sources/prs/vllm/PR-55921.md) | [Model] Add Bailing V3 VL support | 2026-09-08 |  | quantization |
| [#55924](../sources/prs/vllm/PR-55924.md) | [Kimi Bug] Fix kda ima `Triton Error [CUDA]: an illegal memory access was encountered` | 2026-09-08 |  |  |
| [#55960](../sources/prs/vllm/PR-55960.md) | [Perf] Add fused DFlash2 grouped convolution | 2026-09-08 | kernel-fusion | fp4, moe, nvfp4 |
| [#55629](../sources/prs/vllm/PR-55629.md) | [Perf] Fuse DeepEncoder relative bias in Triton attention | 2026-09-07 |  | attention |
| [#55713](../sources/prs/vllm/PR-55713.md) | [Spec Decode] Add NVFP4 DSpark gathered top-k projection | 2026-09-07 | swizzling | fp4, nvfp4, quantization |
| [#55755](../sources/prs/vllm/PR-55755.md) | [Kernel] PDL enablement for fusedQKNormRopeKernel | 2026-09-07 |  |  |
| [#55538](../sources/prs/vllm/PR-55538.md) | [Bugfix][DSA] Write nvfp4_ds_mla from the fused norm+rope kernel | 2026-09-06 | kernel-fusion | mla |
| [#55557](../sources/prs/vllm/PR-55557.md) | [Model] Qwen4Exp: fp8_e4m3 main KV cache on the QSA path | 2026-09-06 |  | attention, fp4, fp8 |
| [#55426](../sources/prs/vllm/PR-55426.md) | [Bugfix][Kimi-K3] Fix KDA projection overlap on Hopper | 2026-09-05 |  | fp4 |
| [#55277](../sources/prs/vllm/PR-55277.md) | [Bugfix][SM120][MLA] Support NoPE sparse MLA (GLM-5.3-Flash) on the FlashInfer SM120 backend | 2026-09-04 |  | attention, fp4, fp8 |
| [#55309](../sources/prs/vllm/PR-55309.md) | [Qwen3.8-Flash-Next] Fuse PLE residual and QSA output gate | 2026-09-04 |  | attention, sparse-attention |
| [#55330](../sources/prs/vllm/PR-55330.md) | [Kernel][Perf] Register-resident path for per-token-group 8-bit quant | 2026-09-04 | pipeline-stages | attention, fp8, quantization |
| [#55356](../sources/prs/vllm/PR-55356.md) | [Kimi Perf] Group fp8 mla cahche insertion, 4~6x kernel level performance improvement for small batch | 2026-09-04 |  | fp8, mla |
| [#55375](../sources/prs/vllm/PR-55375.md) | [Bugfix][Qwen4Exp] fix state index strides in fused PLE conv | 2026-09-04 | kernel-fusion | fp8 |
| [#55059](../sources/prs/vllm/PR-55059.md) | [Kernel][HY V4] Add Triton iHC pre/post fallback | 2026-09-03 |  | fp8 |
| [#55061](../sources/prs/vllm/PR-55061.md) | [Performance][DSv4] Size dequant gather launch grid by rows | 2026-09-03 | tile-scheduling | reduction |
| [#55072](../sources/prs/vllm/PR-55072.md) | [Perf][Distributed] Add low-SM multimem reduce-scatter for SM100/SM103 | 2026-09-03 |  |  |
| [#55107](../sources/prs/vllm/PR-55107.md) | [Model][ROCm] Enable DeepSeek V4 Vision | 2026-09-03 |  | moe, quantization, topk |
| [#55180](../sources/prs/vllm/PR-55180.md) | [Kernel] SM 12.x blockwise FP8: swizzle the CTA raster when the weight exceeds the L2 | 2026-09-03 | persistent-kernel, swizzling, tile-scheduling | fp8, gemm, quantization |
| [#55235](../sources/prs/vllm/PR-55235.md) | [ROCm][Perf] Tune MiniMax-M3 decode top-k for short contexts | 2026-09-03 |  | attention, fp8, topk |
| [#55242](../sources/prs/vllm/PR-55242.md) | [Perf] Kimi K3 nvfp4 Align in_proj weights by 128 to avoid elementwise copy | 2026-09-03 |  | fp4, fp8, gemm |
| [#54873](../sources/prs/vllm/PR-54873.md) | [Qwen3.8-Flash-Next] Improve QSA sparse GQA for prefill and short-ctx decode | 2026-09-02 |  | attention, sparse-attention, topk |
| [#54889](../sources/prs/vllm/PR-54889.md) | [DCP][Kernel][Perf] Fuse the empty-shard LSE mask into the A2A pack kernel | 2026-09-02 |  | attention, fp8, mla |
| [#54890](../sources/prs/vllm/PR-54890.md) | [Qwen3.8-Flash-Next] Support FP8 indexer cache for QSA | 2026-09-02 |  | fp8, quantization, tcgen05 |
| [#54896](../sources/prs/vllm/PR-54896.md) | [Perf][Kimi-K3] Cut MLA decode concat/cache epilogue latency | 2026-09-02 |  | attention, flash-attention, fp8 |
| [#54901](../sources/prs/vllm/PR-54901.md) | [Perf][Model Runner V2] Compact sampling masks on GPU instead of unpacking the full-vocab bitmask on CPU | 2026-09-02 |  | topk |
| [#54908](../sources/prs/vllm/PR-54908.md) | [Bugfix][DCP] Materialize prefill keys on non-owner ranks | 2026-09-02 | kernel-fusion | attention, fp8, mla |
| [#54915](../sources/prs/vllm/PR-54915.md) | [Qwen3.8-Flash-Next] Compact indexer logits workspace to improve prefill efficiency | 2026-09-02 |  | fp8, topk |
| [#54965](../sources/prs/vllm/PR-54965.md) | [ROCm][Perf] W4A16: keep skinny GEMM zero-points packed 4-bit | 2026-09-02 |  | gemm, quantization |
| [#55020](../sources/prs/vllm/PR-55020.md) | [Perf] Prefetch the weight before the PDL wait in fused_q_kv_rmsnorm | 2026-09-02 |  | attention, fp8, gemm |
| [#54651](../sources/prs/vllm/PR-54651.md) | [Core] Triton kernel for small-batch top-p only masking | 2026-09-01 | pipeline-stages | sort, topk |
| [#54682](../sources/prs/vllm/PR-54682.md) | [ROCm][Perf] Optimize MiniMax-M3 decode indexer and top-k | 2026-09-01 |  | attention, fp8, sparse-attention |
| [#54687](../sources/prs/vllm/PR-54687.md) | [Kernel] Reuse Qwen4Exp HC combine-norm for MTP input | 2026-09-01 |  | attention, reduction |
| [#54697](../sources/prs/vllm/PR-54697.md) | [Kimi-K3] Overlap low-M TP8 KDA projections | 2026-09-01 |  | fp4, gemm |
| [#54706](../sources/prs/vllm/PR-54706.md) | [ROCm][RDNA3] Fix W4A16 split-K accuracy and determinism | 2026-09-01 |  | attention, gemm, moe |
| [#54747](../sources/prs/vllm/PR-54747.md) | [Bugfix] Handle padded routes in CUTLASS MoE permutations | 2026-09-01 |  | block-scale, fp4, moe |
| [#54774](../sources/prs/vllm/PR-54774.md) | [Model] Add Cohere Compass model | 2026-09-01 | pipeline-stages | attention, flash-attention, fp8 |
| [#54809](../sources/prs/vllm/PR-54809.md) | [Quant][Kernel] Remove GPTQ Group/Dynamic Activation Ordering | 2026-09-01 |  | moe, quantization |
| [#54845](../sources/prs/vllm/PR-54845.md) | [ROCm][Perf] Add low-M FP32 router GEMM for gfx950 | 2026-09-01 |  | attention, fp4, fp8 |
| [#54513](../sources/prs/vllm/PR-54513.md) | [Qwen3.8-Flash-Next] Separate prefill and decode paths for QSA indexer | 2026-08-31 |  | attention, reduction, sparse-attention |
| [#54517](../sources/prs/vllm/PR-54517.md) | [Qwen3.8-Flash-Next] Fuse Qwen4Exp PLE kernels | 2026-08-31 |  | attention, fp8 |
| [#54565](../sources/prs/vllm/PR-54565.md) | [K3 Perf] Enable DSV3 GEMM for inner-contiguous and row-strided tensors, 12%~81% kernel performance improvement | 2026-08-31 |  | gemm, mla, reduction |
| [#54566](../sources/prs/vllm/PR-54566.md) | [New model][Multimodal] Add DeepSeek-V4-Flash-Vision-Exp support | 2026-08-31 |  | fp8, moe, topk |
| [#54597](../sources/prs/vllm/PR-54597.md) | [Bugfix][MiniMax-M3] Guard sparse decode sentinel indices | 2026-08-31 |  | attention, topk |
| [#54371](../sources/prs/vllm/PR-54371.md) | [Qwen4Exp] Support UVA PLE-offload and Engram tensor parallelism | 2026-08-29 |  | fp8, moe, quantization |
| [#54168](../sources/prs/vllm/PR-54168.md) | [Kimi-K3][Kernel] Optimize the low-M fused latent MoE tail | 2026-08-28 |  | fp4, fp8, gemm |
| [#54194](../sources/prs/vllm/PR-54194.md) | [Kernel] Make prefix-prefill tiling independent of the KV page size | 2026-08-28 |  | attention, moe |
| [#54218](../sources/prs/vllm/PR-54218.md) | [Structured Output] Let terminal grammars stop under min_tokens (II) | 2026-08-28 |  |  |
| [#54251](../sources/prs/vllm/PR-54251.md) | [Kernel] Warm up Qwen GDN gated RMSNorm | 2026-08-28 | kernel-fusion |  |
| [#54261](../sources/prs/vllm/PR-54261.md) | [Kimi-K3][Perf] Make native CUDA AttnRes the SM100 default | 2026-08-28 |  | fp4, moe, tma |
| [#54282](../sources/prs/vllm/PR-54282.md) | [Bugfix][Model Runner V2][Spec Decode] Decouple the draft's gumbel noise stream from the target's | 2026-08-28 |  | fp4, nvfp4 |
| [#53987](../sources/prs/vllm/PR-53987.md) | [Spec Decode][ROCm] Add FLy: entropy-gated deferred verification for draft-model speculative decoding | 2026-08-27 |  | fp8, reduction, topk |
| [#54038](../sources/prs/vllm/PR-54038.md) | [ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill reland | 2026-08-27 |  | reduction |
| [#54040](../sources/prs/vllm/PR-54040.md) | [Kernel] Retire the DSv3 router GEMM CUDA kernel  | 2026-08-27 |  | gemm |
| [#54053](../sources/prs/vllm/PR-54053.md) | [feature] Watermarked generation and detection (Gumbel-max algorithm) | 2026-08-27 |  |  |
| [#54111](../sources/prs/vllm/PR-54111.md) | [Bugfix] Remove race in fused groupwise RMSNorm quantization | 2026-08-27 | kernel-fusion | fp8, quantization, reduction |
| [#53856](../sources/prs/vllm/PR-53856.md) | [Bugfix][ROCm] Mask paged attention V cache padding | 2026-08-26 |  | attention, fp8 |
| [#53877](../sources/prs/vllm/PR-53877.md) | [Bugfix][Kernel] Keep packed GDN decode beta in FP32 | 2026-08-26 |  |  |
| [#53896](../sources/prs/vllm/PR-53896.md) | [Model] Support Qwen3.8-Flash-Next | 2026-08-26 |  | fp4, fp8, nvfp4 |
| [#53906](../sources/prs/vllm/PR-53906.md) | [Model] add GLM-5.3-Flash support | 2026-08-26 |  |  |
| [#53674](../sources/prs/vllm/PR-53674.md) | [Bugfix][ROCm] Fix MiniMax-M3 fused MXFP8 block scale | 2026-08-25 | kernel-fusion | block-scale, quantization |
| [#53677](../sources/prs/vllm/PR-53677.md) | [kernel] Fused embedding kernel  | 2026-08-25 |  |  |
| [#53781](../sources/prs/vllm/PR-53781.md) | [3/N] HiSparse: host-resident sparse-MLA decode hot-buffering | 2026-08-25 |  | attention, mla, scan |
| [#53793](../sources/prs/vllm/PR-53793.md) | [Perf][Kernel][Quantization] Fuse ReLU2 with static FP8 activation quantization | 2026-08-25 |  | fp8, quantization |
| [#53492](../sources/prs/vllm/PR-53492.md) | [ROCm][MLA] Enable sparse MLA Gluon kernel from Aiter | 2026-08-24 |  | attention, fp4, mla |
| [#53524](../sources/prs/vllm/PR-53524.md) | [Kimi-K3][Perf] Prefetch ll_bf16 router weights for M=1 | 2026-08-24 |  | gemm, moe |
| [#53564](../sources/prs/vllm/PR-53564.md) | [2/N][warmup][DSv4] Migrate sequence and DCP kernels | 2026-08-24 |  | attention, fp4, reduction |
| [#53566](../sources/prs/vllm/PR-53566.md) | [5/N][warmup][DSv4] Migrate NVIDIA CuTeDSL attention kernels | 2026-08-24 |  | attention, block-scale, fp4 |
| [#53568](../sources/prs/vllm/PR-53568.md) | [Perf][Kernel] Initialize NVFP4 padding in quant kernel | 2026-08-24 | swizzling | fp4, nvfp4, quantization |
| [#53382](../sources/prs/vllm/PR-53382.md) | [Perf][Kernel] Tune cooperative topk for medium batch-sizes | 2026-08-22 |  | topk |
| [#53396](../sources/prs/vllm/PR-53396.md) | [Kimi K3][Kernel] Support DS conv-state layout in fused KDA decode kernel | 2026-08-22 | kernel-fusion, pipeline-stages | fp8, gemm |
| [#53409](../sources/prs/vllm/PR-53409.md) | [Bugfix] Fix int32 token offset overflow in fused SiLU block quant | 2026-08-22 |  | quantization |
| [#53280](../sources/prs/vllm/PR-53280.md) | [Kernel][MoE] Optimize batched_moe_align_block_size with cooperative writes | 2026-08-21 |  | moe |
| [#53040](../sources/prs/vllm/PR-53040.md) | [DSV4][Kernel] Fuse shared experts into MegaMoE | 2026-08-20 |  | attention, fp4, fp8 |
| [#53053](../sources/prs/vllm/PR-53053.md) | [Kimi-K3] Extend GEMM-RS to GEMM-AR | 2026-08-20 |  | gemm |
| [#53110](../sources/prs/vllm/PR-53110.md) | [Bugfix][ROCM] Fix the MXFP8 block scale exponent | 2026-08-20 | swizzling | block-scale, moe, quantization |
| [#53147](../sources/prs/vllm/PR-53147.md) | [Kernel][Gemma4] Prune Triton sliding-window tiles for multimodal prefixes | 2026-08-20 |  | attention, fp4, fp8 |
| [#52849](../sources/prs/vllm/PR-52849.md) | [ROCm][PERF] Enable AITER PA gluon decode for MiniMax-M3 MTP and dense layers | 2026-08-19 |  | attention, fp4, fp8 |
| [#52882](../sources/prs/vllm/PR-52882.md) | [ROCm][Perf] Optimize DeepSeek V4 C4A top-k with AITER | 2026-08-19 |  | attention, fp8, gemm |
| [#52928](../sources/prs/vllm/PR-52928.md) | [Mamba] Add FlashInfer ReplaySSM support for MTP | 2026-08-19 |  | fp4, nvfp4 |
| [#52668](../sources/prs/vllm/PR-52668.md) | [ROCm][Perf] Use a stacked hipBLASLt GEMM for the bf16x3 router  | 2026-08-18 |  | attention, fp4, gemm |
| [#52676](../sources/prs/vllm/PR-52676.md) | [Kernel][Perf] Enable fused QK-norm + partial MRoPE + gate for Qwen3.6 | 2026-08-18 |  | fp8 |
| [#52775](../sources/prs/vllm/PR-52775.md) | [Kernel] SM120: stop routing misaligned-M blockwise FP8 GEMMs to the small-M swapAB config | 2026-08-18 |  | attention, fp8, gemm |
| [#52789](../sources/prs/vllm/PR-52789.md) | [Perf] Support internal prefill checkpoints for Mamba prefix caching, 9%~25% TTFT improvement | 2026-08-18 |  | attention, moe |
| [#52816](../sources/prs/vllm/PR-52816.md) | [Spec Decode] DFlash2: local convolution + candidate selector | 2026-08-18 | kernel-fusion | attention, reduction, sort |
| [#52821](../sources/prs/vllm/PR-52821.md) | [Refactor] Remove dead code quantization 2 | 2026-08-18 |  | fp8, quantization |
| [#52836](../sources/prs/vllm/PR-52836.md) | Revert DSv4 eager workspace reuse | 2026-08-18 |  | attention |
| [#52839](../sources/prs/vllm/PR-52839.md) | [refactor] consolidate cp attn ops | 2026-08-18 |  | attention, mla, reduction |
| [#52606](../sources/prs/vllm/PR-52606.md) | [ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill | 2026-08-17 | double-buffering, pipeline-stages | attention, gemm, reduction |
| [#52664](../sources/prs/vllm/PR-52664.md) | [Performance][ROCm]  Integrate aiter indexer scoring and top-k kernels into MiniMax-M3 sparse attention path | 2026-08-17 |  | attention, fp4, fp8 |
| [#52506](../sources/prs/vllm/PR-52506.md) | [Mamba] Add FlashInfer ReplaySSM backend | 2026-08-16 |  | fp4, nvfp4 |
| [#52539](../sources/prs/vllm/PR-52539.md) | [Kernel][Perf] Support Qwen head ratios in fused GDN MTP | 2026-08-16 |  | fp8 |
| [#52231](../sources/prs/vllm/PR-52231.md) | [Feature] Support batch invariance on ROCm | 2026-08-14 |  | attention, block-scale, fp4 |
| [#52263](../sources/prs/vllm/PR-52263.md) | [ROCm][Quantization] Support AMD Quark per-block FP8 for fused MoE layers | 2026-08-14 |  | block-scale, fp4, fp8 |
| [#52311](../sources/prs/vllm/PR-52311.md) | [Bugfix][Model Runner V2][Spec Decode] Fix off-by-one in bad_words draft-prefix matching | 2026-08-14 |  |  |
| [#52381](../sources/prs/vllm/PR-52381.md) | Harden DeepSeek V3.2 fused kernel grids | 2026-08-14 | kernel-fusion | quantization |
| [#52388](../sources/prs/vllm/PR-52388.md) | [K3 Perf] Optimize k3 mamba metadata preparation, 6.6~7.6x kernel performance improvement | 2026-08-14 |  |  |
| [#52079](../sources/prs/vllm/PR-52079.md) | [Kimi-K3] Add GEMM-RS for sequence parallelism | 2026-08-13 | swizzling | gemm, mbarrier, reduction |
| [#52136](../sources/prs/vllm/PR-52136.md) | [Docs] Add `pydocstyle` to the `ruff` rules | 2026-08-13 | kernel-fusion | attention, fp8, quantization |
| [#52188](../sources/prs/vllm/PR-52188.md) | [Spec decode] Support Kimi-K3 DCP with DSpark | 2026-08-13 |  | attention, fp8 |
| [#52210](../sources/prs/vllm/PR-52210.md) | [CI Failure] Fix CUDA wheel build for the Kimi K3 fused MLA kernel | 2026-08-13 | pipeline-stages | mla |
| [#52212](../sources/prs/vllm/PR-52212.md) | [ROCm][DSV4][Perf] Optimize Triton sparse-MLA decode on gfx950 | 2026-08-13 |  | attention, mla |
| [#52217](../sources/prs/vllm/PR-52217.md) | [Attention] Vectorize sparse MLA mask loads | 2026-08-13 |  | attention, mla |
| [#52228](../sources/prs/vllm/PR-52228.md) | [Model Runner V2][Spec Decode] Adaptive Verification without a confidence head | 2026-08-13 |  | attention, flash-attention, fp4 |
| [#51915](../sources/prs/vllm/PR-51915.md) | [ROCm][Model][Bugfix] Enable GLM-5.2-MXFP4 on the deepseek_v32 path and fix sparse attention correctness | 2026-08-12 |  | attention, fp4, fp8 |
| [#52030](../sources/prs/vllm/PR-52030.md) | [Bugfix] Fix packed GDN decode launch for large batch-head grids | 2026-08-12 |  | fp4, nvfp4 |
| [#52046](../sources/prs/vllm/PR-52046.md) | [nv] add pcp support in dsv3.2 | 2026-08-12 |  | attention, fp4, fp8 |
| [#52058](../sources/prs/vllm/PR-52058.md) | [Bugfix] Bound KV block zeroing launch geometry | 2026-08-12 |  | fp8 |
| [#51772](../sources/prs/vllm/PR-51772.md) | [Attention][MLA] Fuse Kimi-K3 chunked-context K/V packing | 2026-08-11 |  | attention, fp8, mla |
| [#51855](../sources/prs/vllm/PR-51855.md) | [K3] support recoverssm for K3 | 2026-08-11 |  | attention, fp8, gemm |
| [#51862](../sources/prs/vllm/PR-51862.md) | [ROCm][Perf] Kimi-K3 Remove prefill pipeline stall in chunk KDA | 2026-08-11 | pipeline-stages | attention, moe |
| [#51674](../sources/prs/vllm/PR-51674.md) | [Kernel][Perf] Add fused CUDA post-conv MTP decode kernel for Qwen3.5 GDN | 2026-08-10 | kernel-fusion | attention |
| [#51682](../sources/prs/vllm/PR-51682.md) | [Bugfix][Kimi-K3] Give the AMD packed KDA decode kernel the state-index stride | 2026-08-10 |  | fp8 |
| [#51705](../sources/prs/vllm/PR-51705.md) | [ROCm][MLA][DCP] Support causal multi-token verification | 2026-08-10 |  | attention, fp8, mla |
| [#51718](../sources/prs/vllm/PR-51718.md) | [6/N][KV-Cache Layout Refactor] Standardize KV cache layout | 2026-08-10 |  | attention |
| [#51724](../sources/prs/vllm/PR-51724.md) | [Attention][DSA] Enable W4A16 DSA | 2026-08-10 |  | attention, fp4, mla |
| [#51739](../sources/prs/vllm/PR-51739.md) | [Kernel] Optimize long-context MLA cache gathers | 2026-08-10 |  | attention, fp8, mla |
| [#51538](../sources/prs/vllm/PR-51538.md) | [Bugfix] Make DSV4 sparse MLA work end-to-end for plain decode, MTP, and DSpark | 2026-08-09 |  | attention, fp4, mla |
| [#51332](../sources/prs/vllm/PR-51332.md) | [Quantization][Humming] Support MXFP4 weight + block-FP8 activation for MoE | 2026-08-07 | pipeline-stages | fp4, fp8, gemm |
| [#51367](../sources/prs/vllm/PR-51367.md) | [Kernel] Use Murmur3 RNG for Gumbel sampling | 2026-08-07 |  |  |
| [#51217](../sources/prs/vllm/PR-51217.md) | [MoE] Generalize masked activation for padded layouts | 2026-08-06 |  | fp8, gemm, moe |
| [#51255](../sources/prs/vllm/PR-51255.md) | [Model] Add native Dots3 NOTE multimodal support | 2026-08-06 | pipeline-stages | attention, flash-attention, fp8 |
| [#51171](../sources/prs/vllm/PR-51171.md) | [ROCm][MLA] Reach FULL cudagraphs for AITER MLA speculative decoding | 2026-08-05 |  | attention, fp8, mla |
| [#50939](../sources/prs/vllm/PR-50939.md) | [Model Runner V2] Fix -1 placeholder draft token ids for block verification | 2026-08-04 |  |  |
| [#51031](../sources/prs/vllm/PR-51031.md) | [Bugfix][Kernel] Handle kernel block sizes in V2 DCP slot mapping | 2026-08-04 |  | mla |
| [#51051](../sources/prs/vllm/PR-51051.md) | [Refactor] Remove kernel dead code | 2026-08-04 |  | moe, quantization |
| [#50803](../sources/prs/vllm/PR-50803.md) | [ROCm] Fix DeepSeek V4 indexer numerics and coverage | 2026-08-03 |  | fp4, fp8, moe |
| [#50907](../sources/prs/vllm/PR-50907.md) | [ROCm] Remove stale SDPA and skinny GEMM workarounds | 2026-08-03 |  | attention, gemm, moe |
| [#50910](../sources/prs/vllm/PR-50910.md) | [Model Runner V2] Cache draft logits in model's LM head dtype | 2026-08-03 |  |  |
| [#50729](../sources/prs/vllm/PR-50729.md) | [Bugfix][Mamba] Fix overlapping state copy race | 2026-08-02 |  |  |
| [#50776](../sources/prs/vllm/PR-50776.md) | [Kernel] Skip fully masked key blocks in windowed Triton prefill | 2026-08-02 |  | attention |
| [#50654](../sources/prs/vllm/PR-50654.md) | [ROCm][Perf] Kimi-K3 Fused kernel for KDA decode | 2026-08-01 | kernel-fusion | attention, moe, reduction |
| [#50697](../sources/prs/vllm/PR-50697.md) | [Kernel][Inkling] Fuse shared-expert partial addition into the Lamport collective | 2026-08-01 |  | moe |
| [#50567](../sources/prs/vllm/PR-50567.md) | [Bugfix][Kimi-K3] Enforce packed rows and op availability in AttnRes dispatch | 2026-07-31 |  |  |
| [#50593](../sources/prs/vllm/PR-50593.md) | [Kimi-K3][AMD] Fuse AttnRes state updates and norms | 2026-07-31 | kernel-fusion | attention, block-scale, fp4 |
| [#50365](../sources/prs/vllm/PR-50365.md) | [Perf][Sparse MLA] Drop the atomic contention in the index remap | 2026-07-30 |  | attention, mla, reduction |
| [#50432](../sources/prs/vllm/PR-50432.md) | [Bugfix][Hybrid] Fix cross-block race on num_accepted in MRv2 align prefix cache | 2026-07-30 |  |  |
| [#50455](../sources/prs/vllm/PR-50455.md) | [ROCm][DSv4] Fix sparse-indexer logits collapse on gfx950/gfx942 | 2026-07-30 | kernel-fusion | attention, fp8, reduction |
| [#50465](../sources/prs/vllm/PR-50465.md) | [Model Runner V2] batch-sharded sample | 2026-07-30 |  | sort, topk |
| [#50484](../sources/prs/vllm/PR-50484.md) | [Kimi-K3] DCP support | 2026-07-30 |  | attention, fp8, mla |
| [#50230](../sources/prs/vllm/PR-50230.md) | [Perf][CUDA] Programmatic dependent launch for the DSA decode kernels | 2026-07-29 |  | fp4, fp8, nvfp4 |
| [#50243](../sources/prs/vllm/PR-50243.md) | [Build] Fix CUDA release wheel builds | 2026-07-29 |  | fp8, mla |
| [#50276](../sources/prs/vllm/PR-50276.md) | [Bugfix] Fix packed KV block zeroing stride | 2026-07-29 |  | fp8, mla |
| [#50294](../sources/prs/vllm/PR-50294.md) | [Kernel][Model] Optimize FA4 mm_prefix range lookup | 2026-07-29 |  | attention, flash-attention, fp8 |
| [#50327](../sources/prs/vllm/PR-50327.md) | [ModelRunnerV2] Fix scalar Mamba state update with int32 mappings | 2026-07-29 | pipeline-stages |  |
| [#50089](../sources/prs/vllm/PR-50089.md) | [Model] Add Kimi K3 support: model files and kernels [1/N] | 2026-07-28 |  | attention, block-scale, fp8 |
| [#50090](../sources/prs/vllm/PR-50090.md) | [Kimi-K3] Add AttnRes kernels | 2026-07-28 | warp-specialization | mbarrier, tcgen05, tmem |
| [#50174](../sources/prs/vllm/PR-50174.md) | [3/N][Feat][Perf] Add new warmup infrastructure for JITs. Add provider registry and orchestration for JIT warmup | 2026-07-28 |  |  |
| [#50175](../sources/prs/vllm/PR-50175.md) | [1/N][warmup][DSv4] Migrate generic MLA metadata and indexing kernels | 2026-07-28 |  | attention, mla, reduction |
| [#50176](../sources/prs/vllm/PR-50176.md) | [4/N][warmup][DSv4] Migrate common attention kernels | 2026-07-28 |  | attention, block-scale, fp4 |
| [#50178](../sources/prs/vllm/PR-50178.md) | [9/N][warmup][DSv4] Migrate MHC TileLang kernels | 2026-07-28 |  | gemm |
| [#50183](../sources/prs/vllm/PR-50183.md) | [Bugfix][Spec Decode] Fix NaN handling in rejection sampler tl.argmax | 2026-07-28 |  |  |
| [#50185](../sources/prs/vllm/PR-50185.md) | attn_res kernel latency improvements | 2026-07-28 |  | attention |
| [#50000](../sources/prs/vllm/PR-50000.md) | [New model] Kimi K3 | 2026-07-27 |  | mla, moe |
| [#50005](../sources/prs/vllm/PR-50005.md) | [Bugfix][DCP] Fix NVIDIA DeepSeek-V3.2 / GLM-5.2 fused attention | 2026-07-27 |  | attention, fp4, mla |
| [#50017](../sources/prs/vllm/PR-50017.md) | [ROCm] [bugfix] Chunked prefill paged decode masked load perf  | 2026-07-27 |  | attention |
| [#50032](../sources/prs/vllm/PR-50032.md) | [Attention][MiniMax-M3] Add MSA speculative decode verification | 2026-07-27 |  | attention, fp8, topk |
| [#49903](../sources/prs/vllm/PR-49903.md) | [Core] Warm up runner-owned Triton kernels before the first request | 2026-07-26 |  |  |
| [#49906](../sources/prs/vllm/PR-49906.md) | [ROCm] Fix and optimize GPT-J-style MRoPE | 2026-07-26 |  |  |
| [#49909](../sources/prs/vllm/PR-49909.md) | [ROCm] Use backend-default dot precision for ReplaySSM | 2026-07-26 |  |  |
| [#49791](../sources/prs/vllm/PR-49791.md) | [Kernel] Extend CuTe DSL skinny GEMM to GLM-5.2 | 2026-07-25 |  | fp4, fp8, gemm |
| [#49792](../sources/prs/vllm/PR-49792.md) | [Kernel][SM100] Add a CuTeDSL fused query kernel | 2026-07-25 |  | attention, fp4, fp8 |
| [#49815](../sources/prs/vllm/PR-49815.md) | [Bugfix][MiMo] Apply vision attention sinks in the window attention path | 2026-07-25 |  | attention, flash-attention |
| [#49660](../sources/prs/vllm/PR-49660.md) | [Bugfix][Kernel] Fix integer overflow in libtorch_stable/activation_kernels.cu | 2026-07-24 |  |  |
| [#49704](../sources/prs/vllm/PR-49704.md) | [Bugfix] Support non-uniform page sizes in KVBlockZeroer | 2026-07-24 |  | attention, mla |
| [#49745](../sources/prs/vllm/PR-49745.md) | [Refactor] Remove dead code in multiple files | 2026-07-24 |  |  |
| [#49750](../sources/prs/vllm/PR-49750.md) | [Perf] RMSNorm uncontiguous support, 1.2~3.1x kernel performance improvement | 2026-07-24 |  |  |
| [#49768](../sources/prs/vllm/PR-49768.md) | Revert "[Perf][GLM-5.2] Blackwell decode optimizations" | 2026-07-24 |  | fp4, quantization |
| [#49577](../sources/prs/vllm/PR-49577.md) | [Feature] Mask Replay | 2026-07-23 |  | attention, topk |
| [#49427](../sources/prs/vllm/PR-49427.md) | [Bugfix] Restore `gather_and_maybe_dequant_cache` OOB guard | 2026-07-22 |  | mla |
| [#49429](../sources/prs/vllm/PR-49429.md) | [Bugfix] Fix mHC block-M prenorm GEMM cross-row reduction carry-over | 2026-07-22 |  | gemm, reduction |
| [#49435](../sources/prs/vllm/PR-49435.md) | [Bugfix] Fix SM100 fp8_ds_mla cache scales | 2026-07-22 |  | attention, block-scale, fp8 |
| [#49436](../sources/prs/vllm/PR-49436.md) | [Perf][Hybrid] 3D-grid tiling of the state-copy Triton kernels | 2026-07-22 |  | fp4, nvfp4 |
| [#49486](../sources/prs/vllm/PR-49486.md) | [DSv4 Perf] Skip topk and router when not needed, 3.4% E2E TTFT improvement for Decode case | 2026-07-22 |  | attention, fp8, quantization |
| [#49291](../sources/prs/vllm/PR-49291.md) | [Kernel][Mamba] Fused-kernel support for align-mode DS-conv state migration with num_accepted_tokens > 1 | 2026-07-21 | kernel-fusion | fp4, fp8, moe |
| [#49294](../sources/prs/vllm/PR-49294.md) | [Bugfix][Attention] Ignore empty MLA context chunks during merge | 2026-07-21 |  | attention, fp4, fp8 |
| [#49315](../sources/prs/vllm/PR-49315.md) | [2/N][Feat][Perf] Add new warmup infrastructure for JITs. Add predicate filtering for JIT warmup, and migrate Inkling FA4 | 2026-07-21 |  | attention, mla |
| [#49347](../sources/prs/vllm/PR-49347.md) | [Online quantization] Add online MXFP4 quantization support | 2026-07-21 |  | attention, block-scale, fp4 |
| [#49139](../sources/prs/vllm/PR-49139.md) | [Bugfix][Kernel] Fix persistent top-k histogram reuse after short rows | 2026-07-20 |  | sort, topk |
| [#49209](../sources/prs/vllm/PR-49209.md) | [Hardware][XPU] Register matmul and linear batch-invariant kernels for XPU | 2026-07-20 | persistent-kernel |  |
| [#49236](../sources/prs/vllm/PR-49236.md) | [DSv4 Perf] Optimize workspace reuse for eager break | 2026-07-20 |  | attention, fp8 |
| [#49033](../sources/prs/vllm/PR-49033.md) | Revert "[Sampler] Stop upcasting logits to fp32 in apply_sampling_params" (#48641) | 2026-07-18 |  | fp4, nvfp4 |
| [#48979](../sources/prs/vllm/PR-48979.md) | skip cudagraph/DP padding in topk | 2026-07-17 |  | moe, topk |
| [#48799](../sources/prs/vllm/PR-48799.md) | [Model] Add Inkling model support [1/N] | 2026-07-16 |  | attention, fp4, gemm |
| [#48841](../sources/prs/vllm/PR-48841.md) | [ROCm] [Model] Enable TML inkling | 2026-07-16 | swizzling | attention, block-scale, fp4 |
| [#48858](../sources/prs/vllm/PR-48858.md) | [Model] Add Hopper FA4 relative attention for Inkling | 2026-07-16 |  | attention, fp4, nvfp4 |
| [#48869](../sources/prs/vllm/PR-48869.md) | [Model] Add Inkling MTP=1 support [3/N] | 2026-07-16 | kernel-fusion | attention, fp4, nvfp4 |
| [#48892](../sources/prs/vllm/PR-48892.md) | [Model Runner V2][Spec Decode] Add multi-layer MTP speculator | 2026-07-16 |  | attention, fp4, nvfp4 |
| [#48741](../sources/prs/vllm/PR-48741.md) | [BugFix] Don't apply weight in batch-invariant RMSNorm when has_weight=False | 2026-07-15 |  |  |
| [#48759](../sources/prs/vllm/PR-48759.md) | [LoRA] Optimize TrtLlmLoRAExperts | 2026-07-15 |  | moe, reduction |
| [#48770](../sources/prs/vllm/PR-48770.md) | [2/N][Attention] Enable masked MHA for sparse MLA prefills | 2026-07-15 |  | attention, flash-attention, mla |
| [#48774](../sources/prs/vllm/PR-48774.md) | [Perf] Tune LL BF16 Router GEMM | 2026-07-15 |  | gemm |
| [#48582](../sources/prs/vllm/PR-48582.md) | [M3] Improve indexer for long-context decode (sm100) | 2026-07-14 | pipeline-stages, swizzling | fp8, gemm, reduction |
| [#48597](../sources/prs/vllm/PR-48597.md) | [Perf][GLM-5.2] Blackwell decode optimizations | 2026-07-14 |  | attention, fp4, gemm |
| [#48641](../sources/prs/vllm/PR-48641.md) | [Sampler] Stop upcasting logits to fp32 in apply_sampling_params | 2026-07-14 |  | topk |
| [#48642](../sources/prs/vllm/PR-48642.md) | [Bugfix] Sparse MLA: enable fp8_ds_mla dense prefill | 2026-07-14 |  | attention, fp4, fp8 |
| [#48660](../sources/prs/vllm/PR-48660.md) | [Perf] Optimize dsv4 routing using specialized kernel, 2.94% E2E TPOT improvement | 2026-07-14 |  | attention, fp8, moe |
| [#48484](../sources/prs/vllm/PR-48484.md) | Replicated embedding and norm fusion for DSV3 flat model | 2026-07-13 |  | fp4, gemm, nvfp4 |
| [#48498](../sources/prs/vllm/PR-48498.md) | [Performance] Add Triton kernel for Gemma3n sparse GELU | 2026-07-13 |  | reduction |
| [#48519](../sources/prs/vllm/PR-48519.md) | [ROCm][Perf] Optimize sparse attention prefill kernel for DeepSeek-V4 | 2026-07-13 |  | attention, fp8, reduction |
| [#48385](../sources/prs/vllm/PR-48385.md) | add pad-aware reduce path | 2026-07-12 |  | moe, topk |
| [#48391](../sources/prs/vllm/PR-48391.md) | [Bugfix][Kernel] Fix batch invariance in RMSNorm kernels by pinning block size | 2026-07-12 |  | quantization, reduction |
| [#48335](../sources/prs/vllm/PR-48335.md) |  FP32 router GEMV optimization | 2026-07-11 |  | fp4, gemm, gemv |
| [#48366](../sources/prs/vllm/PR-48366.md) | [Bugfix] Prevent NaN poisoning in xpu_mla_sparse for fully-masked index chunks | 2026-07-11 |  | attention, fp8, mla |
| [#48257](../sources/prs/vllm/PR-48257.md) | [ROCm] [CI] Support cached K/V (key/value=None) in Triton prefix-prefill | 2026-07-10 |  | attention, flash-attention, fp8 |
| [#48287](../sources/prs/vllm/PR-48287.md) | add pad-aware swiglu limit kernel | 2026-07-10 |  | gemm, moe, topk |
| [#48110](../sources/prs/vllm/PR-48110.md) | [Perf][Hybrid] Vectorize _copy_mamba_state_block to uint64 for temporal | 2026-07-09 |  | attention |
| [#48137](../sources/prs/vllm/PR-48137.md) | [Perf] Remove redundant repeat and copy for dsv4, 1.8% E2E TPOT improvement. | 2026-07-09 | pipeline-stages | fp8 |
| [#47973](../sources/prs/vllm/PR-47973.md) | BF16x3 router GEMM | 2026-07-08 | pipeline-stages, swizzling | attention, fp8, gemm |
| [#47984](../sources/prs/vllm/PR-47984.md) | [ROCm][MiniMax-M3][Spec Decode] Support speculative decode with AITER sparse PA | 2026-07-08 |  | attention, fp4, fp8 |
| [#48018](../sources/prs/vllm/PR-48018.md) | [Kernel] ReplaySSM: cache SSM inputs for faster Mamba2 standard decode | 2026-07-08 |  | attention, fp4, nvfp4 |
| [#47808](../sources/prs/vllm/PR-47808.md) | [Spec Decode] DSpark confidence-scheduled verification | 2026-07-07 | double-buffering | attention, fp8, mla |
| [#47857](../sources/prs/vllm/PR-47857.md) | [Model] Add LongCat-Flash-Lite (n-gram embedding) | 2026-07-07 |  | attention, mla, moe |
| [#47896](../sources/prs/vllm/PR-47896.md) | [Kernel][ROCm][Perf] FlyDSL decode-attention kernel for 4-bit TurboQuant KV cache  | 2026-07-07 |  | attention, fp8, gemm |
| [#47912](../sources/prs/vllm/PR-47912.md) | [ROCm] Fix pooling startup workspace lock | 2026-07-07 |  | attention, moe |
| [#47920](../sources/prs/vllm/PR-47920.md) | [Tests][Spec Decode] Add gemma4 MTP acceptance rates test | 2026-07-07 |  |  |
| [#47718](../sources/prs/vllm/PR-47718.md) | [ROCm][Perf] DSv4 two-stage compressor kernel for HCA prefill | 2026-07-06 |  | fp8, moe, reduction |
| [#47785](../sources/prs/vllm/PR-47785.md) | handle topk_ids padding in align sum kernel | 2026-07-06 |  | moe |
| [#47493](../sources/prs/vllm/PR-47493.md) | [Bugfix] DSV4 TP16 garbage output | 2026-07-03 |  | attention, fp8, mla |
| [#47502](../sources/prs/vllm/PR-47502.md) | [Minimax-M3] Using tok_sparse_select from MSA instead of triton kernels | 2026-07-03 |  | attention, flash-attention, fp8 |
| [#47383](../sources/prs/vllm/PR-47383.md) | [Bugfix][Model Runner V2][Spec Decode] Fix int32 offset overflow in block verification kernels | 2026-07-02 |  |  |
| [#47408](../sources/prs/vllm/PR-47408.md) | [Kernel]  Applies routed_scaling_factor internally | 2026-07-02 |  | fp4, moe, nvfp4 |
| [#47451](../sources/prs/vllm/PR-47451.md) | [1/N][Feat][Perf] Add new warmup infrastructure for JITs | 2026-07-02 |  | attention, mla, topk |
| [#47463](../sources/prs/vllm/PR-47463.md) | [Perf] Optimize `fused_topk_bias` for DSv4, 1.5~2x kernel performance improvement | 2026-07-02 |  | moe, topk |
| [#47466](../sources/prs/vllm/PR-47466.md) | [Bugfix] Fix PD disagg + MTP correctness for Qwen3.5(GDN) | 2026-07-02 |  |  |
| [#47268](../sources/prs/vllm/PR-47268.md) | Fixes non-coalesced HBM access in marlin_int4_fp8_preprocess_kernel_awq | 2026-07-01 |  | fp8, quantization |
| [#47287](../sources/prs/vllm/PR-47287.md) | [ROCm][MiniMax-M3] Add AITER sparse paged attention | 2026-07-01 |  | attention, fp4, fp8 |
| [#47332](../sources/prs/vllm/PR-47332.md) | [Bugfix][Gemma4] Fix FA4 mm_prefix mask: add sliding window and absolute q_idx | 2026-07-01 |  | attention, flash-attention |
| [#47090](../sources/prs/vllm/PR-47090.md) | [GLM5] Support FlashMLA FP8 KV cache (Hopper & Blackwell) | 2026-06-30 |  | block-scale, fp8, quantization |
| [#47102](../sources/prs/vllm/PR-47102.md) | Add Triton Backend for Unlimited-OCR R-SWA | 2026-06-30 |  | attention |
| [#47205](../sources/prs/vllm/PR-47205.md) | [Kernel][XPU] Tensor-descriptor operand loads for Triton W8A8 scaled_mm | 2026-06-30 |  | quantization |
| [#46984](../sources/prs/vllm/PR-46984.md) | [Misc] Use functions instead of PTX for the PDL instruction | 2026-06-29 |  | moe |
| [#46995](../sources/prs/vllm/PR-46995.md) | [Spec Decode] DSpark | 2026-06-29 |  | attention, fp8, mla |
| [#47066](../sources/prs/vllm/PR-47066.md) | [Model Runner V2][Spec Decode] Fix stale values in idx_mapping from CG num reqs padding | 2026-06-29 |  | fp8, moe |
| [#46781](../sources/prs/vllm/PR-46781.md) | [Model Runner V2][Spec Decode] Implement block verification for rejection sampling | 2026-06-26 |  | fp4 |
| [#46792](../sources/prs/vllm/PR-46792.md) | [Hardware][AMD][CI] Fix AMD CI image build | 2026-06-26 |  |  |
| [#46805](../sources/prs/vllm/PR-46805.md) | [Bugfix][Kernel] Fix dangling temporary in AWQ gemm torch::stable::sum dim arg | 2026-06-26 |  | gemm, quantization, reduction |
| [#46862](../sources/prs/vllm/PR-46862.md) | [GLM5.2 Perf] `fused_indexer_q_rope_quant` triton kernel, 1.9% ~ 3.3% E2E Throughput improvement. | 2026-06-26 | kernel-fusion | fp8, quantization |
| [#46876](../sources/prs/vllm/PR-46876.md) | [GLM5] Implement op fusion for GLM5/DSV3.2 | 2026-06-26 |  | attention, fp4, fp8 |
| [#46878](../sources/prs/vllm/PR-46878.md) | [Model Runner V2][Spec Decode] Use fp32 uniform threshold for acceptance | 2026-06-26 |  | fp4 |
| [#46685](../sources/prs/vllm/PR-46685.md) | Fix write-after-write hazard in xpu KV RoPE triton kernel | 2026-06-25 |  |  |
| [#46701](../sources/prs/vllm/PR-46701.md) | [Core][V1] Support trace_decode_token_ids for deterministic decode replay | 2026-06-25 |  | attention, moe, quantization |
| [#46718](../sources/prs/vllm/PR-46718.md) | [Feat] Add runtime monitor for post-warmup TileLang compilation | 2026-06-25 |  |  |
| [#46727](../sources/prs/vllm/PR-46727.md) | [Feat] Support thinking_token_budget in Model Runner V2 | 2026-06-25 |  | fp8, quantization |
| [#46730](../sources/prs/vllm/PR-46730.md) | [ROCm][Perf][Bugfix] DSv4 indexer: use platform FP8 dtype (fnuz) for Q-quant on gfx942 | 2026-06-25 |  | fp4, fp8, quantization |
| [#46746](../sources/prs/vllm/PR-46746.md) | [ModelRunner V2] Bound memory for large logprobs requests | 2026-06-25 |  | topk |
| [#46761](../sources/prs/vllm/PR-46761.md) | [DFlash] Fuse precompute kv per-layer rmsnorms | 2026-06-25 |  | fp4 |
| [#46548](../sources/prs/vllm/PR-46548.md) | [ROCm] Fix OOB During Model Warmup With `ROCM_ATTN` and MRV2 | 2026-06-24 |  | attention, fp8 |
| [#46550](../sources/prs/vllm/PR-46550.md) | [CI/Build] Fix topk histogram build on SM75 | 2026-06-24 |  | reduction, topk |
| [#46560](../sources/prs/vllm/PR-46560.md) | [Bugfix][Model Runner V2][Spec Decode] Fix int32 offset overflow in sampler kernels | 2026-06-24 |  | topk |
| [#46564](../sources/prs/vllm/PR-46564.md) | [Model] Support Unlimited OCR | 2026-06-24 |  | attention |
| [#46642](../sources/prs/vllm/PR-46642.md) | [Kernel][MoE] Tune block-FP8 fused MoE for low-batch decode | 2026-06-24 | pipeline-stages | block-scale, fp8, gemm |
| [#46643](../sources/prs/vllm/PR-46643.md) | [Kernel] Vectorized fp32 `moe_sum` reduction and support any topk | 2026-06-24 |  | moe, quantization, reduction |
| [#46656](../sources/prs/vllm/PR-46656.md) | New stable abi cleanup | 2026-06-24 |  | fp4, fp8, moe |
| [#46428](../sources/prs/vllm/PR-46428.md) | [Optimization] Skip DP padding tokens in MoE | 2026-06-23 |  | moe, topk |
| [#46508](../sources/prs/vllm/PR-46508.md) | [Kernel] Enable PDL for per_token_group_quant_8bit_kernel | 2026-06-23 |  | fp8, quantization |
| [#46516](../sources/prs/vllm/PR-46516.md) | Enable gfx1250 ROCm architecture | 2026-06-23 |  | attention |
| [#46533](../sources/prs/vllm/PR-46533.md) | [Spec Decode] Reject placeholder (-1) draft tokens in rejection sampler | 2026-06-23 |  |  |
| [#46546](../sources/prs/vllm/PR-46546.md) | [ROCm][ [Perf] sparse attention optimization on minimax-m3  | 2026-06-23 | pipeline-stages | attention, fp8, gemm |
| [#46340](../sources/prs/vllm/PR-46340.md) | [Kernel] TD operand loads for batched MoE GEMM (moe_mmk) on XPU | 2026-06-22 |  | attention, gemm, mla |
| [#46346](../sources/prs/vllm/PR-46346.md) | [GDN] Improve kkt kernel of CuteDSL prefill backend | 2026-06-22 | pipeline-stages, swizzling | flash-attention, scan, tcgen05 |
| [#46379](../sources/prs/vllm/PR-46379.md) | [Bugfix][KV Offload] Fix swap_blocks_batch on the default stream | 2026-06-22 |  |  |
| [#46385](../sources/prs/vllm/PR-46385.md) | [Kernel] GLM5 Router GEMM | 2026-06-22 |  | fp8, gemm, moe |
| [#46406](../sources/prs/vllm/PR-46406.md) | [Bugfix] Support non-power-of-2 top_k in legacy triton_kernels routing | 2026-06-22 |  | moe, sort, topk |
| [#46408](../sources/prs/vllm/PR-46408.md) | [Bugfix] Support -1 (invalid/non-local) slots in topk_ids for Triton MoE | 2026-06-22 | kernel-fusion | moe, reduction, topk |
| [#46222](../sources/prs/vllm/PR-46222.md) | [ROCm] [Bugfix] Bugfix ROCm Sparse Indexer | 2026-06-20 |  | attention, fp8 |
| [#46245](../sources/prs/vllm/PR-46245.md) | [Bugfix][Model Runner V2] Preserve all allowed_token_ids in the logit bias kernel | 2026-06-20 |  |  |
| [#46117](../sources/prs/vllm/PR-46117.md) | [ROCm][Perf] MXFP8 dense-linear + grouped-MoE GEMM optimizations for MiniMax-M3 | 2026-06-19 | pipeline-stages, swizzling | fp8, gemm, gemv |
| [#45996](../sources/prs/vllm/PR-45996.md) | [MRV2] Make FP32 Gumbel sampling more accurate | 2026-06-18 |  | quantization |
| [#45999](../sources/prs/vllm/PR-45999.md) | Revert "[Kernel] Add PDL support for DeepGEMM kernel" | 2026-06-18 |  | fp8, quantization |
| [#46006](../sources/prs/vllm/PR-46006.md) | [Kernel] Add PDL support for DeepGEMM kernel | 2026-06-18 |  | fp8, quantization |
| [#46070](../sources/prs/vllm/PR-46070.md) | [CI Bug] Revert #42379 to fix CI `Multi-Modal Models (Extended Generation 1)` | 2026-06-18 |  | fp8, quantization |
| [#46076](../sources/prs/vllm/PR-46076.md) | [Attention][DSA] support dcp for FLASHINFER_MLA_SPARSE | 2026-06-18 | pipeline-stages | attention, fp4, fp8 |
| [#45892](../sources/prs/vllm/PR-45892.md) | [Minimax-M3] BF16/FP8 Indexer using MSA | 2026-06-17 | kernel-fusion | attention, fp8 |
| [#45935](../sources/prs/vllm/PR-45935.md) | [Model]Fix MiniMaxM2ForCausalLM perf  regression | 2026-06-17 | kernel-fusion | fp4, nvfp4, reduction |
| [#45666](../sources/prs/vllm/PR-45666.md) | [ROCM] [Communication] Add INT3 quantization method for quickreduce | 2026-06-15 |  | block-scale, moe, quantization |
| [#45681](../sources/prs/vllm/PR-45681.md) | [ROCm][DSv4] Functional fixes for DeepSeek V4 on MI300X/MI325X | 2026-06-15 | kernel-fusion, pipeline-stages | block-scale, fp8, mla |
| [#45725](../sources/prs/vllm/PR-45725.md) | [ROCm][Perf] mxfp8 moe/linear gfx950 tuning for MiniMax-M3 | 2026-06-15 |  | attention, fp8, gemm |
| [#45743](../sources/prs/vllm/PR-45743.md) | [M3] Tune Triton indexer score decode for spec-decode | 2026-06-15 |  | topk |
| [#45744](../sources/prs/vllm/PR-45744.md) | [M3] Enable FP8 sparse GQA | 2026-06-15 |  | attention, fp8, quantization |
| [#45361](../sources/prs/vllm/PR-45361.md) | [Kernel][Bugfix] Fix INT8 per-token-head KV cache rounding in Triton reshape-and-cache | 2026-06-12 |  | attention, fp8, quantization |
| [#45381](../sources/prs/vllm/PR-45381.md) | [Model] Add MiniMax M3 support | 2026-06-12 |  | attention, gemm, quantization |
| [#45415](../sources/prs/vllm/PR-45415.md) | [12/n]  final _C library kernel migration | 2026-06-12 |  | fp4, moe, quantization |
| [#45466](../sources/prs/vllm/PR-45466.md) | [Bugfix][Kernel] Check output alignment in vectorize_with_alignment (fixes misaligned-address crash for non-multiple-of-8 head sizes) | 2026-06-12 |  | attention, fp8, quantization |
| [#45473](../sources/prs/vllm/PR-45473.md) | [Kernel] Support DS Mamba tail copy for MTP align mode | 2026-06-12 |  | fp4, nvfp4 |
| [#45255](../sources/prs/vllm/PR-45255.md) | [Bugfix] Fix gridDim.y overflow for large row counts | 2026-06-11 |  | fp8, quantization |
| [#45277](../sources/prs/vllm/PR-45277.md) | [Build] Fix CUDA arch build coverage gaps | 2026-06-11 | pipeline-stages | attention, fp4, gemm |
| [#45304](../sources/prs/vllm/PR-45304.md) | [11b/n] Migrate Machete kernels to torch stable ABI | 2026-06-11 |  | quantization |
| [#45103](../sources/prs/vllm/PR-45103.md) | [ROCm][DSV4][Perf] Fuse inverse-RoPE and cache bf16 wo_a in o-projection | 2026-06-10 |  | attention, block-scale, fp8 |
| [#45111](../sources/prs/vllm/PR-45111.md) | [Attention] Re-enable cross-layer KV cache layout for MLA via stride-aware kernels | 2026-06-10 |  | attention, fp8, mla |
| [#45163](../sources/prs/vllm/PR-45163.md) | [Model] Add DiffusionGemma Support | 2026-06-10 |  | attention |
| [#45176](../sources/prs/vllm/PR-45176.md) | [11a/n]  Migrate Marlin kernels to torch stable ABI | 2026-06-10 |  | fp4, fp8, nvfp4 |
| [#45187](../sources/prs/vllm/PR-45187.md) | Add NVFP4 KV 4-over-6 scale search | 2026-06-10 |  | attention, fp4, nvfp4 |
| [#44944](../sources/prs/vllm/PR-44944.md) | [PERF] Fuse multi-group block table staged writes | 2026-06-09 |  |  |
| [#44971](../sources/prs/vllm/PR-44971.md) | [Security] Fix info disclosure via int32 truncation in GGUF dequantize kernels | 2026-06-09 |  | moe, quantization |
| [#44991](../sources/prs/vllm/PR-44991.md) | [CPU] Skip Triton kernel monkey-patches when Triton-CPU is available | 2026-06-09 |  |  |
| [#45000](../sources/prs/vllm/PR-45000.md) | [Perf][ROCm] Fix GDN KKT warmup regression on RDNA by avoiding fp32 tl.dot | 2026-06-09 |  | wgmma |
| [#45026](../sources/prs/vllm/PR-45026.md) | Stop setting CUDA_VISIBLE_DEVICES internally in vLLM, add device_ids arg | 2026-06-09 |  | attention, mla |
| [#45066](../sources/prs/vllm/PR-45066.md) | Revert "[Kernel] Speed up silu_and_mul_per_block_quant with warp-shuf… | 2026-06-09 |  | quantization, reduction |
| [#44880](../sources/prs/vllm/PR-44880.md) | [Feature] Support MTP speculative decoding for Bailing hybrid models | 2026-06-08 |  | attention, moe |
| [#44899](../sources/prs/vllm/PR-44899.md) | [ROCm][DSv4][Perf] Flash-decode split-K decode attention kernel | 2026-06-08 | pipeline-stages | attention, reduction, topk |
| [#44699](../sources/prs/vllm/PR-44699.md) | [DSV4] Decouple DS V4 Sparse MLA Metadata from DS V3.2 | 2026-06-06 |  | attention, fp8, mla |
| [#44744](../sources/prs/vllm/PR-44744.md) | [Security] Fix remote DoS via invalid recovered token reinjection | 2026-06-06 |  | reduction |
| [#44667](../sources/prs/vllm/PR-44667.md) | [NVFP4][Emulation] Fuse NVFP4 weight dequantization with compute in triton kernel for w13/w2 MOE MLP linears | 2026-06-05 |  | block-scale, fp4, fp8 |
| [#44692](../sources/prs/vllm/PR-44692.md) | [Bugfix][Kernel] Fix mHC fused-RMSNorm big-fuse miscompile for hidden_size != 4096 | 2026-06-05 | pipeline-stages | reduction |
| [#44565](../sources/prs/vllm/PR-44565.md) | [10c/n] Migrate MoE kernels to torch stable ABI  | 2026-06-04 |  | fp4, fp8, moe |
| [#44572](../sources/prs/vllm/PR-44572.md) | [Perf] SM90 cutlass fp8 mm supports odd M by swap_ab, 180~290% kernel performance improvement | 2026-06-04 |  | fp8, gemm, quantization |
| [#44586](../sources/prs/vllm/PR-44586.md) | [MRV2][Spec Decode] DFlash | 2026-06-04 |  | attention, fp8 |
| [#44455](../sources/prs/vllm/PR-44455.md) | [2/N][KV-Cache Layout Refactor] Pack K/V into the content dim across attention backends | 2026-06-03 |  | attention, fp4, nvfp4 |
| [#44334](../sources/prs/vllm/PR-44334.md) | [10/n] Migrate cuda_view and silu_and_mul_per_block_quant kernels to torch stale ABI. | 2026-06-02 |  | fp4, fp8, moe |
| [#44340](../sources/prs/vllm/PR-44340.md) | [Quant] Support compressed-tensors WNA8O8Int linears and WNInt embeddings | 2026-06-02 |  | gemm, quantization |
| [#44343](../sources/prs/vllm/PR-44343.md) | [Perf][Feat] Add generic cuteDSL LL FP32 router (GEMM) | 2026-06-02 |  | gemm, reduction |
| [#44161](../sources/prs/vllm/PR-44161.md) | [Kernel][DSv4] Optimize sparse FP8 compressor kernels | 2026-06-01 |  | attention, fp8, reduction |
| [#44173](../sources/prs/vllm/PR-44173.md) | [Kernel] Speed up silu_and_mul_per_block_quant with warp-shuffle reduction + vectorized I/O | 2026-06-01 |  | fp8, moe, quantization |
| [#44176](../sources/prs/vllm/PR-44176.md) | [Perf] fuse qk rmsnorm rope gate for qwen3.5 | 2026-06-01 |  | attention |
| [#44230](../sources/prs/vllm/PR-44230.md) | optimize the compressor 128 split cutedsl kernel  | 2026-06-01 |  | attention, reduction, sparse-attention |
| [#44109](../sources/prs/vllm/PR-44109.md) | [Kernel] Add weightless RMSNorm CUDA kernels for has_weight=False (#41430) | 2026-05-31 |  |  |
| [#44075](../sources/prs/vllm/PR-44075.md) | [ROCm][Perf] Fused MoE W4A16 HIP kernel for AMD RDNA3 (gfx1100) | 2026-05-30 |  | attention, gemm, moe |
| [#44013](../sources/prs/vllm/PR-44013.md) | Migrate header files to torch stable abi | 2026-05-29 |  | fp4, quantization |
| [#43827](../sources/prs/vllm/PR-43827.md) | [DSv4] Adding TRTLLM gen attention kernel | 2026-05-28 |  | attention, fp8, mla |
| [#43746](../sources/prs/vllm/PR-43746.md) | [Model Refactoring] Remove torch compile dependency in DSv4 | 2026-05-27 |  |  |
| [#43632](../sources/prs/vllm/PR-43632.md) | [DeepSeek V4] Move MegaMoE input prep kernel to nvidia/ops | 2026-05-26 |  | fp8, quantization, topk |
| [#43667](../sources/prs/vllm/PR-43667.md) | [Perf][KDA] Fuse gate softplus, chunk-local cumsum, and RCP_LN2 scaling | 2026-05-26 |  | moe |
| [#43679](../sources/prs/vllm/PR-43679.md) | [ROCm][DSV4] Enable Tilelang MHC replacing torch/triton mhc | 2026-05-26 |  | moe, reduction |
| [#43710](../sources/prs/vllm/PR-43710.md) | [DSv4] Refactor compressor & Fix ROCm compatibility | 2026-05-26 |  |  |
| [#43717](../sources/prs/vllm/PR-43717.md) | [9/n] Migrate attention and cache kernels to torch stable ABI (continued)  | 2026-05-26 | swizzling | attention, fp4, fp8 |
| [#43554](../sources/prs/vllm/PR-43554.md) | [Kernel] Remove NormGateLinear | 2026-05-25 |  | gemm, moe |
| [#43557](../sources/prs/vllm/PR-43557.md) | Fix the E8M0 scale computation in the MXFP4 (W4A4) MOE CUTLASS kernel | 2026-05-25 |  | fp4, moe, nvfp4 |
| [#43584](../sources/prs/vllm/PR-43584.md) | Add CuTe DSL sparse compressor support | 2026-05-25 | kernel-fusion | attention, fp8, sparse-attention |
| [#43462](../sources/prs/vllm/PR-43462.md) | [Bugfix] hadacore_transform: respect inplace parameter to fix garbage outputs with QuIP transforms | 2026-05-23 |  | fp4, quantization |
| [#43474](../sources/prs/vllm/PR-43474.md) | [Kernel] Add mhc_pre_big_fuse_with_norm_tilelang  | 2026-05-23 | pipeline-stages |  |
| [#43477](../sources/prs/vllm/PR-43477.md) | Enable DeepSeek V4 and GLM-5.1 on SM120 | 2026-05-23 |  | attention, fp4, fp8 |
| [#43421](../sources/prs/vllm/PR-43421.md) | [XPU][Mamba] Triton-based selective scan forward op for XPU | 2026-05-22 |  |  |
| [#43437](../sources/prs/vllm/PR-43437.md) | mhc_post - remove sts & add vectorized copies | 2026-05-22 |  | reduction |
| [#43273](../sources/prs/vllm/PR-43273.md) | [GDN] GDN Prefill kernel for SM100 | 2026-05-21 | kernel-fusion, pipeline-stages, swizzling | attention, clc, scan |
| [#43361](../sources/prs/vllm/PR-43361.md) | [8/n] Migrate merge_attn_states, mamba, sampler to torch stable ABI (continued) | 2026-05-21 |  | attention, fp8, quantization |
| [#43195](../sources/prs/vllm/PR-43195.md) | Update KDA chunk prefill decay to use exp2 semantics | 2026-05-20 |  | attention |
| [#43209](../sources/prs/vllm/PR-43209.md) | [7/n] Migrate pos_encoding and norm kernels to libtorch stable ABI (continued) | 2026-05-20 |  | fp8, quantization |
| [#43241](../sources/prs/vllm/PR-43241.md) | [Model Runner V2][Spec Decode] Add Gemma4 MTP support | 2026-05-20 |  | attention |
| [#43083](../sources/prs/vllm/PR-43083.md) | Tuning script and configs for Triton Mamba SSU kernel | 2026-05-19 |  | fp4, fp8, moe |
| [#43091](../sources/prs/vllm/PR-43091.md) | [Model Runner V2][Spec Decode] Support spec decode with draft model | 2026-05-19 |  | attention |
| [#43150](../sources/prs/vllm/PR-43150.md) | [BUG] Fix FP64 Gumbel precision coverage | 2026-05-19 |  | topk |
| [#43162](../sources/prs/vllm/PR-43162.md) | [Feat][DSV4] Fuse q pad into deepseek v4 fused kernel | 2026-05-19 | kernel-fusion | attention |
| [#42953](../sources/prs/vllm/PR-42953.md) | feat: add DeepSeek-V4 XPU attention decode path | 2026-05-18 |  | attention, block-scale, fp4 |
| [#42963](../sources/prs/vllm/PR-42963.md) | [ModelRunnerV2] Support prompt embeds | 2026-05-18 |  |  |
| [#42996](../sources/prs/vllm/PR-42996.md) | [Kernel] Add PDL support for DeepGEMM kernel | 2026-05-18 |  | fp8, quantization |
| [#43008](../sources/prs/vllm/PR-43008.md) | [Perf][DSv4/DSv3.2] Add cluster-cooperative topK kernel for low-latency scenarios | 2026-05-18 | double-buffering, persistent-kernel, pipeline-stages | fp8, mbarrier, reduction |
| [#43014](../sources/prs/vllm/PR-43014.md) | [Perf] Optimize moe permute by pre-allocate buffer, 9~14% kernel performance improvement | 2026-05-18 |  | moe, topk |
| [#43018](../sources/prs/vllm/PR-43018.md) | [ROCm] Cpu offload for ROCm 7.13+ to align the hipMemcpyBatchAsync params and perf in 7.14x | 2026-05-18 |  | fp4 |
| [#42899](../sources/prs/vllm/PR-42899.md) | add cutedsl dsv4 indexer fp8 kernel | 2026-05-17 |  | attention, fp4, fp8 |
| [#42838](../sources/prs/vllm/PR-42838.md) | [ROCm][MLA] Replace torch.cat in sparse-MLA forward_mqa with fused concat_mla_q | 2026-05-16 | kernel-fusion | attention, fp8, mla |
| [#42849](../sources/prs/vllm/PR-42849.md) | [Perf] Add do_not_specialize in fused FP8 RoPE kernel | 2026-05-16 |  | attention, fp8 |
| [#42755](../sources/prs/vllm/PR-42755.md) | [Model][Hardware][AMD][Kernel] Part 2/2 -> Enable e2e QK Norm + RoPE + KV Cache runtime fusion for Qwen3-30B-A3B on ROCM_ATTN | 2026-05-15 | kernel-fusion | attention, fp8 |
| [#42758](../sources/prs/vllm/PR-42758.md) | Enable perf_token_group_quant/_C_stable_libtorch for ROCm | 2026-05-15 |  | fp8, quantization |
| [#42774](../sources/prs/vllm/PR-42774.md) | [Perf] Padded nvfp4 quant kernel to remove additional copy, 2.4%~5.7% e2e performance improvement | 2026-05-15 | swizzling | fp4, nvfp4, quantization |
| [#42663](../sources/prs/vllm/PR-42663.md) | [6/n] Migrate activation kernels, gptq, gguf, non cutlass w8a8 to libtorch stable ABI (continued) | 2026-05-14 |  | attention, fp8, moe |
| [#42527](../sources/prs/vllm/PR-42527.md) | [Kernel] Pack topk id/weights triton kernel | 2026-05-13 |  | topk |
| [#42562](../sources/prs/vllm/PR-42562.md) | [Perf][Feat] Add generic cuteDSL LL BF16 router (GEMM) | 2026-05-13 | pipeline-stages, swizzling, warp-specialization | fp4, gemm, mbarrier |
| [#42379](../sources/prs/vllm/PR-42379.md) | [Bugfix] Fix RMSNorm kernels to multiply in weight's native dtype | 2026-05-12 |  | fp8 |
| [#42406](../sources/prs/vllm/PR-42406.md) | [Model Runner V2] support mamba hybrid models align prefix cache | 2026-05-12 |  | fp8 |
| [#42436](../sources/prs/vllm/PR-42436.md) | fused_moe: add VLLM_TRITON_USE_TD tensor-descriptor path | 2026-05-12 |  | attention, fp4, fp8 |
| [#42290](../sources/prs/vllm/PR-42290.md) | [LoRA] Add one shot triton kernel For MoE LoRA | 2026-05-11 | kernel-fusion, pipeline-stages | gemv, moe, reduction |
| [#42353](../sources/prs/vllm/PR-42353.md) | DSv4 fused Q-norm kernel grid refactor | 2026-05-11 | pipeline-stages | fp8 |
| [#42191](../sources/prs/vllm/PR-42191.md) | [Perf] Apply single-pass min_larger finding and binary search in Triton Top-p path. | 2026-05-10 |  | topk |
| [#42236](../sources/prs/vllm/PR-42236.md) | [DSv4] Improved dequant gather K cache kernel | 2026-05-10 |  | attention, fp8, quantization |
| [#42153](../sources/prs/vllm/PR-42153.md) | [Perf] Use 2D-grid to eliminate divmod in W8W8 group quant | 2026-05-09 |  | fp8, quantization |
| [#42175](../sources/prs/vllm/PR-42175.md) | [Core][Model] Gemma4: Unified FA4 for all layers + FlashAttention mm_prefix support | 2026-05-09 |  | attention, flash-attention, moe |
| [#42187](../sources/prs/vllm/PR-42187.md) | [ModelRunnerV2] Avoid pipeline parallel bubbles | 2026-05-09 | pipeline-stages | fp8, reduction |
| [#42080](../sources/prs/vllm/PR-42080.md) | [feat] Add FP8 per-tensor Q scale support to Triton attention backend | 2026-05-08 |  | attention, fp8, quantization |
| [#41979](../sources/prs/vllm/PR-41979.md) | [MoE] Move various experts classes to fused_moe/experts/ | 2026-05-07 |  | moe, quantization |
| [#41986](../sources/prs/vllm/PR-41986.md) | [Bugfix] Add swiglu limits to deepgemm fp8 methods | 2026-05-07 |  | fp8, quantization |
| [#41797](../sources/prs/vllm/PR-41797.md) | [Attention] add triton diff-kv backend for mimo | 2026-05-06 |  | attention |
| [#41326](../sources/prs/vllm/PR-41326.md) | Faster per-token fp8 group quant packed kernel for blackwell | 2026-04-30 | pipeline-stages | fp8, quantization, tma |
| [#41394](../sources/prs/vllm/PR-41394.md) | [Kernel][ROCm] Native W4A16 kernel for AMD RDNA3 (gfx1100) — fp16 + bf16 | 2026-04-30 | double-buffering, pipeline-stages | attention, fp8, gemm |
| [#41428](../sources/prs/vllm/PR-41428.md) | [DSv4] Improved fused Indexer Q quant kernel | 2026-04-30 |  | attention, block-scale, fp4 |
| [#41263](../sources/prs/vllm/PR-41263.md) | [DSV4]   Fuse norm and router for low latency scenario | 2026-04-29 |  | gemv, moe, reduction |
| [#41126](../sources/prs/vllm/PR-41126.md) | [Attention] Mamba attention module refactor | 2026-04-28 |  | attention |
| [#40950](../sources/prs/vllm/PR-40950.md) | [DSV4] Add silu clamp limit to shared expert | 2026-04-27 |  |  |
| [#40977](../sources/prs/vllm/PR-40977.md) | [ROCm][Kernel] Add HybridW4A16LinearKernel: Triton prefill + HIP skinny decode | 2026-04-27 |  | gemm, quantization, reduction |
| [#40996](../sources/prs/vllm/PR-40996.md) | DCP supports hybrid attention | 2026-04-27 |  | attention, fp8 |
| [#40923](../sources/prs/vllm/PR-40923.md) | [Kernel] Marlin MoE: include SM 12.x in default arch list | 2026-04-26 |  | attention, fp8, moe |
| [#40784](../sources/prs/vllm/PR-40784.md) | [ROCm][Perf] Tune wvSplitK on gfx1151 | 2026-04-24 |  | gemm |
| [#40835](../sources/prs/vllm/PR-40835.md) | [Feature] Triton INT4 per-token-head KV cache quantization | 2026-04-24 |  | attention, fp8, quantization |
| [#40687](../sources/prs/vllm/PR-40687.md) | [ROCm][Perf] Support N=5 in wvSplitK skinny GEMM kernels for speculative decoding | 2026-04-23 |  | gemm |
| [#40704](../sources/prs/vllm/PR-40704.md) | [ModelRunner V2] Speculative Decoding NGram GPU Implementations | 2026-04-23 |  |  |
| [#40337](../sources/prs/vllm/PR-40337.md) | [Perf] Integrate flash-maxsim Triton kernels for late-interaction scoring | 2026-04-20 | kernel-fusion |  |
| [#40372](../sources/prs/vllm/PR-40372.md) | [Kernel] Batch invariant NVFP4 MoE using cutlass | 2026-04-20 | tile-scheduling | fp4, gemm, grouped-gemm |
| [#40392](../sources/prs/vllm/PR-40392.md) | [Performance][DSR1]: Fused RoPE+KVCache+q_concat for MLA | 2026-04-20 |  | attention, fp4, fp8 |
| [#40408](../sources/prs/vllm/PR-40408.md) | [Perf] Batch invariance with Cutlass fp8 support, 28.9% E2E latency improvement | 2026-04-20 |  | attention, fp8, quantization |
| [#40191](../sources/prs/vllm/PR-40191.md) | [Bugfix] Guard mxfp4_experts_quant bindings on ENABLE_NVFP4_SM100 | 2026-04-18 |  | fp4, nvfp4, quantization |
| [#40131](../sources/prs/vllm/PR-40131.md) | [Bugfix] moe lora align kernel grid | 2026-04-17 | pipeline-stages | moe, sort |
| [#40172](../sources/prs/vllm/PR-40172.md) | [Perf] [Hybrid] Fused Triton kernel for GPU-side Mamba state postprocessing | 2026-04-17 | kernel-fusion | attention, fp8, reduction |
| [#39988](../sources/prs/vllm/PR-39988.md) | [Bugfix] Fix turboquant FP8 cast failure for BF16 models on Ampere GPUs | 2026-04-16 |  | attention, fp8 |
| [#39912](../sources/prs/vllm/PR-39912.md) | [Kernel] Batch invariant NVFP4 linear using cutlass | 2026-04-15 | persistent-kernel, stream-k, tile-scheduling | fp4, gemm, nvfp4 |
| [#39547](../sources/prs/vllm/PR-39547.md) | [Perf] Fuse Zero Initializer for FP8 DeepGemm Block Quant Kernel | 2026-04-10 |  | fp8, quantization, tma |
| [#39391](../sources/prs/vllm/PR-39391.md) | fix: clamp NaN/Inf in topk_softmax to prevent duplicate expert IDs | 2026-04-09 |  | fp8, moe, sort |
| [#39458](../sources/prs/vllm/PR-39458.md) | [MLA] Optimize mla indexer prepare uniform decode for MTP > 1 | 2026-04-09 |  | attention, fp4, mla |
| [#39306](../sources/prs/vllm/PR-39306.md) | Use CU_MEMCPY_SRC_ACCESS_ORDER_ANY for batch KV cache swaps | 2026-04-08 | pipeline-stages |  |
| [#39058](../sources/prs/vllm/PR-39058.md) | [Kernel] Implement CUDA kernel for ReLUSquaredActivation (relu^2) | 2026-04-06 |  |  |
| [#38981](../sources/prs/vllm/PR-38981.md) | [Perf][GDN] Align TMA usage with upstream FLA | 2026-04-04 |  | attention, fp4, nvfp4 |
| [#38865](../sources/prs/vllm/PR-38865.md) | [Refactor] Improve indexer decode path metadata preparation | 2026-04-03 |  | attention, fp4, fp8 |
| [#38922](../sources/prs/vllm/PR-38922.md) | [Bugfix] Fix broken explicit unquantized kv cache dtype support | 2026-04-03 |  | attention, fp8, quantization |
| [#38445](../sources/prs/vllm/PR-38445.md) | [PERF]MiniMax-M2 gate kernel | 2026-03-29 | kernel-fusion | fp4, fp8, gemm |
| [#38460](../sources/prs/vllm/PR-38460.md) | [Perf] Batch KV cache swap copies via cuMemcpyBatchAsync | 2026-03-29 |  | reduction |
| [#38479](../sources/prs/vllm/PR-38479.md) | [Attention Backend] TurboQuant: 2-bit KV cache compression with 4x capacity | 2026-03-29 | kernel-fusion | attention, flash-attention, fp8 |
| [#38423](../sources/prs/vllm/PR-38423.md) | [NVIDIA] Bugfix NVFP4 DGX Spark and RTX50 | 2026-03-28 |  | fp4, gemm, grouped-gemm |
| [#38325](../sources/prs/vllm/PR-38325.md) | [Kernel] Add swapAB support for SM120 CUTLASS blockwise FP8 GEMM  | 2026-03-27 |  | fp8, gemm, quantization |
| [#38065](../sources/prs/vllm/PR-38065.md) | [Perf] FP8 FlashInfer Attn for ViT | 2026-03-25 |  | attention, fp4, fp8 |
| [#37948](../sources/prs/vllm/PR-37948.md) | [Perf] triton bilinear_pos_embed kernel for ViT | 2026-03-24 |  | fp4, nvfp4 |
| [#37970](../sources/prs/vllm/PR-37970.md) | [Kernel] Optimize SM120 CUTLASS blockwise FP8 GEMM | 2026-03-24 |  | fp8, gemm, quantization |
| [#37503](../sources/prs/vllm/PR-37503.md) | [4/n] Migrate FP4/W4A8 CUTLASS kernels to torch stable ABI | 2026-03-19 | swizzling | fp4, gemm, nvfp4 |
| [#37421](../sources/prs/vllm/PR-37421.md) | [Perf][Kernel] Persistent TopK scheduler: unified CUDAGraph-safe kernel with dynamic per-row dispatch - DeepSeek-V3.2 DSA decode | 2026-03-18 | double-buffering, persistent-kernel | fp4, fp8, nvfp4 |
| [#37463](../sources/prs/vllm/PR-37463.md) | [Kernel] Add MXFP4 W4A4 CUTLASS MoE kernel for SM100 | 2026-03-18 | swizzling, tile-scheduling | block-scale, fp4, gemm |
| [#37320](../sources/prs/vllm/PR-37320.md) | [Kernel] Add non-gated support for NVFP4 CUTLASS MoE | 2026-03-17 |  | block-scale, fp4, gemm |
| [#37332](../sources/prs/vllm/PR-37332.md) | Add nvfp4 support to reshape_and_cache_flash | 2026-03-17 | swizzling | block-scale, fp4, fp8 |
| [#37205](../sources/prs/vllm/PR-37205.md) | [Kernel] Add gpt-oss Router GEMM kernel | 2026-03-16 |  | gemm, mbarrier, moe |
| [#36982](../sources/prs/vllm/PR-36982.md) | [MTP][Sparse MLA] Take advantage of native MTP support in indexer when possible | 2026-03-13 |  | mla |
| [#36847](../sources/prs/vllm/PR-36847.md) | [Feat][Spec Decode] DFlash | 2026-03-12 | kernel-fusion | attention, flash-attention |
| [#36518](../sources/prs/vllm/PR-36518.md) | [Kernel] Fuse FP8 output quantization into merge_attn_states | 2026-03-09 |  | attention, fp8, quantization |
| [#36559](../sources/prs/vllm/PR-36559.md) | [Kernel] Add swap AB optimization to fused_moe_kernel | 2026-03-09 |  | fp8, gemm, moe |
| [#36161](../sources/prs/vllm/PR-36161.md) | Add 320 dimension size support to MLA | 2026-03-05 |  | mla |
| [#35753](../sources/prs/vllm/PR-35753.md) | [Mamba] Add stochastic rounding support | 2026-03-02 |  |  |
| [#35777](../sources/prs/vllm/PR-35777.md) | [Kernel] Add fused_sigmoid_gating_delta_rule_update kernel for Qwen3 Next | 2026-03-02 | kernel-fusion | attention |
| [#35290](../sources/prs/vllm/PR-35290.md) | [Attention][Perf] Optimize cp_gather_and_upconvert_fp8_kv_cache - DeepSeek-v3.2 | 2026-02-25 |  | attention, fp4, fp8 |
| [#35161](../sources/prs/vllm/PR-35161.md) | [Bugfix] Fix expert_ids padding values in moe_align_block_size kernel | 2026-02-24 |  | moe |
| [#35210](../sources/prs/vllm/PR-35210.md) | [BugFix] Fix fp4 quant kernel on CUDA 12.8 | 2026-02-24 | swizzling | fp4, quantization |
| [#35219](../sources/prs/vllm/PR-35219.md) | [BUGFIX][Mamba][Qwen3.5] Zero freed SSM cache blocks on GPU | 2026-02-24 |  | attention, flash-attention, fp8 |
| [#35123](../sources/prs/vllm/PR-35123.md) | [Bugfix] Fix DSV3 kernels breaking _C and _moe_C on unsupported arches | 2026-02-23 |  | mla |
| [#34917](../sources/prs/vllm/PR-34917.md) | [Attention][Perf][Kernel] Replace torch.cat with vectorized CUDA kernel MLA query concat - DeepSeek-V3.2 | 2026-02-19 |  | attention, fp4, mla |
| [#34791](../sources/prs/vllm/PR-34791.md) | [Bugfix] Gate 256-bit instructions to CUDA 12.9+ | 2026-02-18 |  |  |
| [#34758](../sources/prs/vllm/PR-34758.md) | [Model Bash] DeepSeek R1 BF16 Min Latency QKV A GEMM (0.5% E2E Speedup) | 2026-02-17 | swizzling | fp4, gemm, mbarrier |
| [#34597](../sources/prs/vllm/PR-34597.md) | [Kernel] Add FP8 KV cache support to Triton MLA decode attention | 2026-02-16 |  | attention, fp8, mla |
| [#34556](../sources/prs/vllm/PR-34556.md) | [Quantization] add humming quantization kernel | 2026-02-14 | kernel-fusion | attention, block-scale, fp4 |
| [#34389](../sources/prs/vllm/PR-34389.md) | [Custom Ops] Add functional + out variant for scaled_fp4_quant | 2026-02-12 | swizzling | fp4, quantization |
| [#34448](../sources/prs/vllm/PR-34448.md) | [Kernel] Integrate SM100 MXFP8 blockscaled grouped MM and quant kernels | 2026-02-12 |  | block-scale, gemm, moe |
| [#34302](../sources/prs/vllm/PR-34302.md) | [ModelBash][DSV3] Add TRTLLM DSV3 Router GEMM kernel (6% B1 Speedup) | 2026-02-11 |  | fp4, gemm, moe |
| [#34206](../sources/prs/vllm/PR-34206.md) | [Kernel] Optimize grouped topk kernel | 2026-02-10 |  | moe, reduction, sort |
| [#33972](../sources/prs/vllm/PR-33972.md) | [Bugfix]fix output Nan/Inf in marlin if dtype=float16 | 2026-02-06 |  | fp4, gemm, moe |
| [#33529](../sources/prs/vllm/PR-33529.md) | Triton MLA perf fixes | 2026-02-02 |  | attention, mla |
| [#33517](../sources/prs/vllm/PR-33517.md) | [Kernel] Add enable_sm120_or_later for SM121 (DGX Spark) CUTLASS support | 2026-02-01 |  | fp4, fp8, gemm |
| [#33255](../sources/prs/vllm/PR-33255.md) | [Bugfix] Fix quant RMS norm fusion for quantization with TMA-aligned scales | 2026-01-28 |  | fp8, gemm, quantization |
| [#33291](../sources/prs/vllm/PR-33291.md) | [PERF] Change GDN Attention State Layout from [N, HV, K, V] to [N, HV, V, K] | 2026-01-28 |  | attention, fp4, fp8 |
| [#33022](../sources/prs/vllm/PR-33022.md) | [Kernel] Apply 256bit LDG/STG To Activation Kernels | 2026-01-25 |  |  |
| [#32873](../sources/prs/vllm/PR-32873.md) | [Performance] Tune Mamba selective scan kernel for B200 | 2026-01-22 |  | fp4, fp8, nvfp4 |
| [#32887](../sources/prs/vllm/PR-32887.md) | [Spec Decode] Unified Parallel Drafting | 2026-01-22 |  | attention, fp4, nvfp4 |
| [#32520](../sources/prs/vllm/PR-32520.md) | [Perf][Kernel] Optimize FP4 quantization kernels (SM100F) | 2026-01-17 | swizzling | fp4, gemm, moe |
| [#32195](../sources/prs/vllm/PR-32195.md) | Add TMA support to fused_moe_lora kernel | 2026-01-12 |  | moe, tma |
| [#31837](../sources/prs/vllm/PR-31837.md) | [Perf] Fuse stride preparation for NVFP4 cutlass_moe | 2026-01-06 |  | fp4, nvfp4, quantization |
| [#31380](../sources/prs/vllm/PR-31380.md) | [Bugfix][ROCm]Fix Qwen3-Next-80B-A3B-Thinking inference and optimize non-standard block size (544) support under rocm_atten | 2025-12-26 |  | attention, fp8 |
| [#31246](../sources/prs/vllm/PR-31246.md) | [Kernel] Add topk_sigmoid kernel | 2025-12-23 |  | moe, topk |
| [#30974](../sources/prs/vllm/PR-30974.md) | [Bugfix] Fix incorrect tiles creation for mm prefix triton attention | 2025-12-18 |  | attention |
| [#30887](../sources/prs/vllm/PR-30887.md) | [Bugfix] [Kernel] Triton attention kernels: mask out V blocks that fall outside sliding window | 2025-12-17 |  | attention |
| [#30897](../sources/prs/vllm/PR-30897.md) | [NVFP4][Perf] Tune NVFP4 input quant kernel for small batch size | 2025-12-17 | swizzling | fp4, moe, nvfp4 |
| [#30692](../sources/prs/vllm/PR-30692.md) | OffloadingConnector: Support kernel_block_size != block_size | 2025-12-15 |  | attention, mla |
| [#30286](../sources/prs/vllm/PR-30286.md) | [LoRA] Support Quantized Adapters | 2025-12-09 |  | fp8, gemm, grouped-gemm |
| [#30254](../sources/prs/vllm/PR-30254.md) | gptq marlin quantization support for fused moe with lora | 2025-12-08 |  | gemm, moe, quantization |
| [#30141](../sources/prs/vllm/PR-30141.md) | Add llmcompressor fp8 kv-cache quant (per-tensor and per-attn_head) | 2025-12-05 |  | attention, flash-attention, fp8 |
| [#29845](../sources/prs/vllm/PR-29845.md) | [SpecDecode] Simplified alternative padded-speculation acceptance rate fix | 2025-12-02 |  |  |
| [#29901](../sources/prs/vllm/PR-29901.md) | [Kernel][Quantization][MoE] add marlin kernel support for turing (sm75) | 2025-12-02 | pipeline-stages | fp4, fp8, moe |
| [#29642](../sources/prs/vllm/PR-29642.md) | [Kernel][MoE] optimize `moe_align_block_size` | 2025-11-28 |  | moe, topk |
| [#29691](../sources/prs/vllm/PR-29691.md) | [Kernel]Support W4A8 Grouped GEMM on Hopper | 2025-11-28 |  | block-scale, fp8, gemm |
| [#29354](../sources/prs/vllm/PR-29354.md) | Add unpermute-aware fused MoE path and small-batch fallback | 2025-11-24 |  | fp8, moe, quantization |
| [#29257](../sources/prs/vllm/PR-29257.md) | Lora MoE Align Improvements | 2025-11-23 |  | moe, scan, topk |
| [#29242](../sources/prs/vllm/PR-29242.md) | [Kernel] Add NVFP4 MoE CUTLASS support for SM120 | 2025-11-22 | tile-scheduling | fp4, gemm, moe |
| [#28840](../sources/prs/vllm/PR-28840.md) | bugfix: correct attn output with base 2 or e | 2025-11-17 |  | attention, mla |
| [#28775](../sources/prs/vllm/PR-28775.md) | [Model] Add support for openPangu moe model | 2025-11-15 |  | attention, fp8, moe |
| [#28358](../sources/prs/vllm/PR-28358.md) | [Performance][B200] silu_mul_quant: pack scales in int32 | 2025-11-09 |  | fp8, quantization |
| [#28124](../sources/prs/vllm/PR-28124.md) | [Perf][DeepSeek] Add sigmoid+bias fusion to fused_grouped_topk from TRTLLM | 2025-11-05 |  | fp4, moe, nvfp4 |
| [#27931](../sources/prs/vllm/PR-27931.md) | [Kernel] Optimize rms_norm kernel | 2025-11-01 |  |  |
| [#27883](../sources/prs/vllm/PR-27883.md) | [Performance] Fused blockwise quant RMS norm | 2025-10-31 | kernel-fusion | fp8, quantization |
| [#27532](../sources/prs/vllm/PR-27532.md) | [Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2 | 2025-10-26 |  | attention, fp8, mla |
| [#27284](../sources/prs/vllm/PR-27284.md) | [Perf] SM100 - add swap AB optimization to CUTLASS FP8 GEMM | 2025-10-21 |  | fp8, gemm, quantization |
| [#25843](../sources/prs/vllm/PR-25843.md) | Update launch_bounds_utils.h for correct compile on Multiple Cuda Arch - PTXAS out of range Warning | 2025-09-28 |  | fp4, moe, quantization |
| [#25774](../sources/prs/vllm/PR-25774.md) | Fuse RoPE and MLA KV-cache write | 2025-09-26 |  | fp8, mla, quantization |
| [#25193](../sources/prs/vllm/PR-25193.md) | [Compile] Fix Compile Warning for Ignoring `MIN_BLOCK_PER_SM` | 2025-09-18 |  | fp4, quantization |
| [#24833](../sources/prs/vllm/PR-24833.md) | [Bugfix] Fix accuracy issue for silu_mul + nvfp4 quant fusion kernel | 2025-09-14 |  | fp4, nvfp4, quantization |
| [#24722](../sources/prs/vllm/PR-24722.md) | [Kernel][Quantization] add w4a8 support for marlin kernel | 2025-09-12 | stream-k | fp4, fp8, moe |
| [#24673](../sources/prs/vllm/PR-24673.md) | [NVIDIA] Blackwell Family | 2025-09-11 |  | quantization |
| [#24440](../sources/prs/vllm/PR-24440.md) | [Transform] [Quantization] Add QuTLASS support to vLLM | 2025-09-08 | swizzling | block-scale, fp4, nvfp4 |
| [#24385](../sources/prs/vllm/PR-24385.md) | [Kernel] Support decode context parallelism on Blackwell with CUTLASS MLA | 2025-09-07 |  | attention, mla |
| [#23991](../sources/prs/vllm/PR-23991.md) | [Model] Add LongCat-Flash  | 2025-08-30 |  | moe |
| [#23972](../sources/prs/vllm/PR-23972.md) | [Kernel] Faster pre-processing time for W4A8 | 2025-08-29 |  | quantization |
| [#23791](../sources/prs/vllm/PR-23791.md) | [Kernel] cuda kernels for upcoming decode context parallel feature | 2025-08-28 |  | fp8 |
| [#23727](../sources/prs/vllm/PR-23727.md) | [Bugfix][Misc] Fix silu_and_mul_nvfp4_quant issue and extract common utils for nvfp4 kernel source files | 2025-08-27 |  | fp4, fp8, moe |
| [#23734](../sources/prs/vllm/PR-23734.md) | [Feature] Support Decode Context Parallel (DCP) for MLA | 2025-08-27 |  | mla |
| [#23660](../sources/prs/vllm/PR-23660.md) | [Compile] Fix Compile Warning for `w4a8_mm_entry.cu` | 2025-08-26 |  | quantization |
| [#23671](../sources/prs/vllm/PR-23671.md) | [NVIDIA] Support SiluMul + NVFP4 quant fusion | 2025-08-26 |  | fp4, fp8, gemm |
| [#23424](../sources/prs/vllm/PR-23424.md) | [Bugfix] Fixing division by zero in triton_attn if query_heads/kv_heads > 16  | 2025-08-22 |  | attention, flash-attention |
| [#23265](../sources/prs/vllm/PR-23265.md) | [Perf] Small optimizations for silu_mul_fp8_quant_deep_gemm | 2025-08-20 |  | fp8 |
| [#23274](../sources/prs/vllm/PR-23274.md) | [Kernel] Add fused grouped_topk kernel for MoE | 2025-08-20 | pipeline-stages | moe, reduction, sort |
| [#23280](../sources/prs/vllm/PR-23280.md) | [Perf] Use upstream CUTLASS for SM90 Block FP8 kernel | 2025-08-20 |  | block-scale, fp8, gemm |
| [#23287](../sources/prs/vllm/PR-23287.md) | [Compile] Fix Compile Warning SM100 Cutlass MLA | 2025-08-20 |  | attention, flash-attention, mla |
| [#23174](../sources/prs/vllm/PR-23174.md) | Optimize input preparation for FlashInfer [2/N] | 2025-08-19 |  | attention |
| [#23198](../sources/prs/vllm/PR-23198.md) | [kernel] Support W4A8 on Hopper | 2025-08-19 |  | fp8, gemm, quantization |
| [#23045](../sources/prs/vllm/PR-23045.md) | [Kernel] CUTLASS MoE FP8: Integrate cuda moe permute/unpermute | 2025-08-17 |  | block-scale, fp4, fp8 |
| [#22991](../sources/prs/vllm/PR-22991.md) | [Fix] enable swap_ab for pplx problem size computation | 2025-08-15 |  | gemm, moe, quantization |
| [#22368](../sources/prs/vllm/PR-22368.md) | [BugFix] Fix triton compile error in `kernel_unified_attention_2/3d` caused by attention sinks | 2025-08-06 |  | attention |
| [#22399](../sources/prs/vllm/PR-22399.md) | [Bug] Fix B200 DeepGEMM E8M0 Accuracy Issue | 2025-08-06 |  | fp8, quantization |
| [#22222](../sources/prs/vllm/PR-22222.md) | Fp8 paged attention update | 2025-08-05 |  | attention, fp4, fp8 |
| [#22131](../sources/prs/vllm/PR-22131.md) | [Kernel] Add support for block FP8 on SM120 (NVIDIA 5090 and RTX PRO 6000) | 2025-08-02 | tile-scheduling | fp8, gemm, quantization |
| [#21556](../sources/prs/vllm/PR-21556.md) | [Kernel] Improve machete memory bound perf | 2025-07-24 |  | quantization, tma |
| [#21465](../sources/prs/vllm/PR-21465.md) | [Bug] Fix Compressed Tensor NVFP4 `cutlass_fp4_group_mm` illegal memory access | 2025-07-23 |  | block-scale, fp4, moe |
| [#21309](../sources/prs/vllm/PR-21309.md) | Support CUTLASS NVFP4 (w4a4) for Blackwell Geforce GPUs (SM120) | 2025-07-21 | swizzling | fp4, gemm, nvfp4 |
| [#21249](../sources/prs/vllm/PR-21249.md) | [v1] - Mamba1 Attention Metadata | 2025-07-20 |  | attention |
| [#21229](../sources/prs/vllm/PR-21229.md) | [Feature][Kernel]FusedMoE LoRA | 2025-07-19 |  | moe, quantization |
| [#21197](../sources/prs/vllm/PR-21197.md) | [Kernel] Enable Hybrid Model Support in Triton Unified Attention Kernel | 2025-07-18 |  | attention, flash-attention, fp8 |
| [#21116](../sources/prs/vllm/PR-21116.md) | [perf] Add fused MLA QKV + strided layernorm | 2025-07-17 |  | fp8, mla, quantization |
| [#21083](../sources/prs/vllm/PR-21083.md) | [Perf] Cuda Kernel for Per Token Group Quant | 2025-07-16 |  | fp8, gemm, quantization |
| [#20903](../sources/prs/vllm/PR-20903.md) | [Kernel] DeepGemm MoE : Integrate triton permute / unpermute kernels  | 2025-07-14 |  | fp8, gemm, grouped-gemm |
| [#20911](../sources/prs/vllm/PR-20911.md) | [Perf] Add swap_ab to SM90 FP8 non-block CUTLASS moe grouped gemm | 2025-07-14 |  | block-scale, fp8, gemm |
| [#20833](../sources/prs/vllm/PR-20833.md) | [Bug] Fix DeepGemm for EP low latency case | 2025-07-11 |  | fp8 |
| [#20841](../sources/prs/vllm/PR-20841.md) | [Perf] Use Triton instead of Torch for DeepGEMM Per Token Group Quant | 2025-07-11 |  | fp8, quantization |
| [#20762](../sources/prs/vllm/PR-20762.md) | [Performance] Performance improvements in non-blockwise fp8 CUTLASS MoE | 2025-07-10 |  | fp8, moe, topk |
| [#20769](../sources/prs/vllm/PR-20769.md) | SM100 Cutlass MLA decode with unrestricted num_heads (< 128) for DeepSeek TP | 2025-07-10 | tile-scheduling | attention, flash-attention, mla |
| [#20781](../sources/prs/vllm/PR-20781.md) | [fix]: disable cutlass block scaled group gemm for EP | 2025-07-10 |  | block-scale, gemm, moe |
| [#20447](../sources/prs/vllm/PR-20447.md) | [feat]: add SM100 support for cutlass FP8 groupGEMM | 2025-07-03 |  | fp8, gemm, moe |
| [#20396](../sources/prs/vllm/PR-20396.md) | [Kernel] SM90 CUTLASS FP8 GEMM: add support for swap AB + kernel tuning | 2025-07-02 | persistent-kernel | fp8, gemm, quantization |
| [#20308](../sources/prs/vllm/PR-20308.md) | [Kernel] Optimize Prefill Attention in Unified Triton Attention Kernel | 2025-07-01 |  | attention, flash-attention |
| [#20324](../sources/prs/vllm/PR-20324.md) | [Kernel][Bugfix] Fixup some warnings in nvfp4_blockwise_moe when CUDA < 12.8 | 2025-07-01 |  | fp4, quantization |
| [#20166](../sources/prs/vllm/PR-20166.md) | [Bugfix] Fix topk_ids indices_type for CUTLASS w8a8 FP8 MoE | 2025-06-27 |  | fp8, moe, quantization |
| [#20141](../sources/prs/vllm/PR-20141.md) | [Bugfix] Fix some narrowing conversion warnings | 2025-06-26 |  | attention, fp4, mla |
| [#20087](../sources/prs/vllm/PR-20087.md) |  [Feature] Integrate SM100 DeepGEMM support | 2025-06-25 |  | block-scale, fp8, gemm |
| [#20016](../sources/prs/vllm/PR-20016.md) | Enable V1 for Hybrid SSM/Attention Models | 2025-06-24 |  | attention |
| [#19757](../sources/prs/vllm/PR-19757.md) | [feat]: CUTLASS block scaled group gemm for SM100 | 2025-06-17 |  | block-scale, gemm, moe |
| [#19566](../sources/prs/vllm/PR-19566.md) | [Perf] Further tunings for SM100 FP8 CUTLASS kernel | 2025-06-12 |  | fp8, gemm, quantization |
| [#19500](../sources/prs/vllm/PR-19500.md) | [Hardware][NVIDIA][kernel] Fp4 MOE quant kernel optimization | 2025-06-11 |  | fp4, gemm, moe |
| [#19110](../sources/prs/vllm/PR-19110.md) | [Hardware][NVIDIA] FP4 MoE kernel optimization | 2025-06-03 |  | block-scale, fp4, moe |
| [#18807](../sources/prs/vllm/PR-18807.md) | [BugFix] FA2 MLA Accuracy Issue | 2025-05-28 |  | attention, mla |
| [#18864](../sources/prs/vllm/PR-18864.md) | [Kernel] Enable fp8 support for pplx and BatchedTritonExperts. | 2025-05-28 |  | fp8, gemm, quantization |
| [#18762](../sources/prs/vllm/PR-18762.md) | [Kernel] Integrate CUTLASS MoE kernel with PPLX | 2025-05-27 |  | fp8, moe, quantization |
| [#18778](../sources/prs/vllm/PR-18778.md) | [Perf] Tunings for SM100 FP8 CUTLASS kernel | 2025-05-27 |  | fp8, gemm, quantization |
| [#18596](../sources/prs/vllm/PR-18596.md) | [Hardware][AMD] integrate aiter chunked prefill into vllm | 2025-05-23 |  | attention, fp8, quantization |
| [#18564](../sources/prs/vllm/PR-18564.md) | Sm100 blockwise fp8 swap ab | 2025-05-22 |  | fp8, gemm, quantization |
| [#18046](../sources/prs/vllm/PR-18046.md) | [Kernel] Have rotary embeddings support tensors | 2025-05-13 |  | mla |
| [#17687](../sources/prs/vllm/PR-17687.md) | [Kernel] fp4 marlin kernel | 2025-05-06 |  | fp4, fp8, moe |
| [#17280](../sources/prs/vllm/PR-17280.md) | [NVIDIA] Support Cutlass w8a8 FP8 for Blackwell Geforce GPUs (sm120) | 2025-04-28 |  | fp8, gemm, quantization |
| [#17139](../sources/prs/vllm/PR-17139.md) | [ROCm][FP8][Kernel] FP8 quantization fused into Custom Paged Attention | 2025-04-24 |  | attention, fp8, quantization |
| [#17082](../sources/prs/vllm/PR-17082.md) | Fix `numel()` downcast in vllm/csrc/moe/moe_align_sum_kernels.cu +2 | 2025-04-23 |  | moe |
| [#17004](../sources/prs/vllm/PR-17004.md) | [ROCm][Kernel][V1] Enable AMD Radeon GPU Custom Paged Attention on v1 | 2025-04-22 |  | attention, reduction |
| [#16828](../sources/prs/vllm/PR-16828.md) | [Kernel] Unified Triton kernel that doesn't distinguish between prefill + decode | 2025-04-18 |  | attention, flash-attention |
| [#16850](../sources/prs/vllm/PR-16850.md) | [Kernel] some optimizations for dense marlin and moe marlin | 2025-04-18 |  | fp8, moe, quantization |
| [#16861](../sources/prs/vllm/PR-16861.md) | [Kernel] Add expert_map support to Cutlass FP8 MOE | 2025-04-18 |  | fp8, moe, quantization |
| [#16780](../sources/prs/vllm/PR-16780.md) | [Kernel] GGUF MoeVec kernel | 2025-04-17 |  | moe, quantization, topk |
| [#16801](../sources/prs/vllm/PR-16801.md) | [BugFix] Accuracy fix for llama4 int4 - improperly casted scales | 2025-04-17 |  | moe |
| [#16605](../sources/prs/vllm/PR-16605.md) | Allocate kv_cache with stride order | 2025-04-14 |  | attention |
| [#16362](../sources/prs/vllm/PR-16362.md) | [Hardware/NVIDIA/Kernel] [Functional Enablement] [1/N] Enable nvidia/DeepSeek-R1-FP4 Model | 2025-04-09 | swizzling, tile-scheduling | block-scale, fp4, fp8 |
| [#16366](../sources/prs/vllm/PR-16366.md) | [Kernel] Support W8A8 channel-wise weights and per-token activations in triton fused_moe_kernel | 2025-04-09 |  | fp8, quantization |
| [#16173](../sources/prs/vllm/PR-16173.md) | [Kernel] support merge_attn_states CUDA kernel, 3x speedup | 2025-04-07 | pipeline-stages | attention, mla |
| [#16032](../sources/prs/vllm/PR-16032.md) | [NVIDIA] Support Cutlass MLA for Blackwell GPUs | 2025-04-03 | tile-scheduling | attention, flash-attention, fp4 |
| [#16034](../sources/prs/vllm/PR-16034.md) | [ROCM] Add gfx950 to the custom attention archs | 2025-04-03 |  | attention |
| [#15946](../sources/prs/vllm/PR-15946.md) | [Bugfix] fix use_atomic_add support of marlin kernel when using v1 engine | 2025-04-02 |  | quantization |
| [#15956](../sources/prs/vllm/PR-15956.md) | Modularize fused experts and integrate PPLX kernels | 2025-04-02 |  | moe, quantization, reduction |
| [#15720](../sources/prs/vllm/PR-15720.md) | [ROCM][KERNEL] Paged attention for V1 | 2025-03-28 |  | attention |
| [#15511](../sources/prs/vllm/PR-15511.md) | Use Cache Hinting for fused_moe kernel | 2025-03-26 |  |  |
| [#15456](../sources/prs/vllm/PR-15456.md) | [Kernel] Fix conflicting macro names for gguf kernels | 2025-03-25 |  | moe, quantization |
| [#14658](../sources/prs/vllm/PR-14658.md) | [Kernel] allow non-contiguous input for marlin kernel | 2025-03-12 |  | attention, mla, quantization |
| [#14613](../sources/prs/vllm/PR-14613.md) | [Kernel] GGUF MoE kernel | 2025-03-11 |  | moe, quantization |
| [#14568](../sources/prs/vllm/PR-14568.md) | permute/unpermute kernel for moe optimization | 2025-03-10 |  | gemm, grouped-gemm, moe |
| [#14447](../sources/prs/vllm/PR-14447.md) | [Kernel] moe wna16 marlin kernel | 2025-03-07 | pipeline-stages | mla, moe, quantization |
| [#14383](../sources/prs/vllm/PR-14383.md) | Add cutlass support for blackwell fp8 blockwise gemm | 2025-03-06 | tile-scheduling | fp8, gemm, quantization |
| [#14245](../sources/prs/vllm/PR-14245.md) | dynamic distpatch of fp8 kernels | 2025-03-05 |  | fp8, quantization |
| [#14138](../sources/prs/vllm/PR-14138.md) | [Kernel] optimize performance of gptq marlin kernel when n is small | 2025-03-03 |  | quantization |
| [#13972](../sources/prs/vllm/PR-13972.md) | [Kernel] CUTLASS grouped gemm fp8 MoE kernel | 2025-02-27 |  | fp8, gemm, grouped-gemm |
| [#13798](../sources/prs/vllm/PR-13798.md) | add cutlass support for blackwell fp8 gemm | 2025-02-25 |  | fp8, gemm, quantization |
| [#13718](../sources/prs/vllm/PR-13718.md) | [core] Perf improvement for DSv3 on AMD GPUs | 2025-02-23 |  | attention, mla, moe |
| [#13571](../sources/prs/vllm/PR-13571.md) | [NVIDIA] Support nvfp4 cutlass gemm | 2025-02-19 | swizzling | fp4, gemm, nvfp4 |
| [#13321](../sources/prs/vllm/PR-13321.md) | [Kernel] moe wna16 cuda kernel | 2025-02-15 |  | gemm, mla, moe |
| [#12978](../sources/prs/vllm/PR-12978.md) | [Kernel]Add streamK for block-quantized CUTLASS kernels | 2025-02-09 | persistent-kernel, stream-k, tile-scheduling | gemm, quantization |
| [#12931](../sources/prs/vllm/PR-12931.md) | [Misc][Kernel]: Add GPTQAllSpark Quantization | 2025-02-08 | double-buffering | gemm, quantization |
| [#12850](../sources/prs/vllm/PR-12850.md) | Optimize moe_align_block_size for deepseek_v3 | 2025-02-06 |  | moe |
| [#12777](../sources/prs/vllm/PR-12777.md) | [Kernel] Make rotary_embedding ops more flexible with input shape | 2025-02-05 |  | attention, mla |
| [#12784](../sources/prs/vllm/PR-12784.md) | [NVIDIA] Support nvfp4 quantization | 2025-02-05 |  | fp4, fp8, gemm |
| [#12676](../sources/prs/vllm/PR-12676.md) | [Perf] Mem align KV caches for CUDA devices (MLA perf improvement) | 2025-02-03 |  | attention, mla |
| [#12639](../sources/prs/vllm/PR-12639.md) | [Attention] MLA with chunked prefill | 2025-02-01 |  | attention, mla |
| [#12574](../sources/prs/vllm/PR-12574.md) | [Kernel] port sgl moe_align_block_size kernels | 2025-01-30 |  | moe |
| [#12583](../sources/prs/vllm/PR-12583.md) | Expert Parallelism (EP) Support for DeepSeek Models | 2025-01-30 |  | moe |
| [#12587](../sources/prs/vllm/PR-12587.md) | [Kernel][Quantization] Integrate block-quantized CUTLASS kernels for DeepSeekV3 | 2025-01-30 |  | quantization |
| [#12528](../sources/prs/vllm/PR-12528.md) | [Attention] MLA decode optimizations | 2025-01-28 |  | attention, fp8, mla |
| [#12348](../sources/prs/vllm/PR-12348.md) | [ROCm] Faster Custom Paged Attention kernels | 2025-01-23 |  | attention, fp8, gemm |
| [#12185](../sources/prs/vllm/PR-12185.md) | [Kernel] add triton fused moe kernel for gptq/awq | 2025-01-18 |  | moe, quantization, topk |
| [#11868](../sources/prs/vllm/PR-11868.md) | [Kernel] Update `cutlass_scaled_mm` to support 2d group (blockwise) scaling | 2025-01-08 | persistent-kernel, tile-scheduling | gemm, quantization |
| [#10995](../sources/prs/vllm/PR-10995.md) | [Kernel]: Cutlass 2:4 Sparsity + FP8/Int8 Quant Support | 2024-12-08 | persistent-kernel, tile-scheduling | fp8, gemm, quantization |
| [#7701](../sources/prs/vllm/PR-7701.md) | [Kernel] (2/N) Machete - Integrate into CompressedTensorsWNA16 and GPTQMarlin | 2024-08-20 |  | moe, quantization |
| [#7174](../sources/prs/vllm/PR-7174.md) | [Kernel] (1/N) Machete - Hopper Optimized Mixed Precision Linear Kernel  | 2024-08-05 | pipeline-stages, stream-k, tile-scheduling | fp8, gemm, quantization |

