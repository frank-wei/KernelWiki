#!/usr/bin/env bash
# Clone or update the upstream repos tracked by KernelWiki (candidates/*.yaml).
#
# Missing repos are cloned blobless, existing clones are fast-forwarded (never
# force-updated), and `git backfill` then downloads every missing blob so
# historical diffs work offline (agent sessions cannot fetch from GitHub).
#
# Usage: bash scripts/clone_upstreams.sh [BASE_DIR]   (default: ~/upstream)
set -u
BASE_DIR="${1:-$HOME/upstream}"
mkdir -p "$BASE_DIR" && cd "$BASE_DIR" || exit 1

REPOS=(
  NVIDIA/cutlass
  sgl-project/sglang
  vllm-project/vllm
  flashinfer-ai/flashinfer
  pytorch/pytorch
  deepseek-ai/DeepGEMM
  Dao-AILab/flash-attention
  NVIDIA/TensorRT-LLM
  NVIDIA/cccl
  triton-lang/triton
  tile-ai/tilelang
  HazyResearch/ThunderKittens
  deepseek-ai/TileKernels
  Dao-AILab/quack
)

failed=()
for r in "${REPOS[@]}"; do
  dir="${r#*/}"
  if [ -d "$dir/.git" ]; then
    echo "== update $r ($BASE_DIR/$dir)"
    git -C "$dir" fetch --all --prune && git -C "$dir" pull --ff-only || failed+=("$r")
  else
    echo "== clone $r -> $BASE_DIR/$dir"
    git clone --filter=blob:none "https://github.com/$r.git" "$dir" || { failed+=("$r"); continue; }
  fi
  echo "   backfill blobs for $r"
  git -C "$dir" backfill || failed+=("$r")
done

echo
echo "Repo                         HEAD     date"
for r in "${REPOS[@]}"; do
  dir="${r#*/}"
  [ -d "$dir/.git" ] && printf '%-28s %s\n' "$r" "$(git -C "$dir" log -1 --format='%h %cd' --date=short)"
done
if [ ${#failed[@]} -gt 0 ]; then
  echo "FAILED: ${failed[*]}"
  exit 1
fi
