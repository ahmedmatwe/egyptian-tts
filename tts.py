"""Egyptian-dialect TTS (NAMAA-Egyptian-TTS on Chatterbox Multilingual, MIT license).
Usage: python tts.py "النص بالعامية" out.wav [reference.wav] [--exaggeration 0.6] [--seed 7]
Runs on Apple Silicon (MPS), CUDA, or plain CPU (e.g. GitHub Actions). Models are cached in ./hf-cache."""
import argparse, os
HERE = os.path.dirname(os.path.abspath(__file__))
os.environ.setdefault("HF_HOME", os.path.join(HERE, "hf-cache"))
import torch, torchaudio as ta
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file
from chatterbox import mtl_tts

ap = argparse.ArgumentParser()
ap.add_argument("text"); ap.add_argument("out"); ap.add_argument("ref", nargs="?")
ap.add_argument("--exaggeration", type=float, default=0.6); ap.add_argument("--cfg", type=float, default=0.4)
ap.add_argument("--seed", type=int, default=7)
a = ap.parse_args()
dev = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
_load = torch.load
torch.load = lambda *x, **k: _load(*x, **{**k, "map_location": torch.device(dev)})
m = mtl_tts.ChatterboxMultilingualTTS.from_pretrained(device=dev)
m.t3.load_state_dict(load_file(hf_hub_download("NAMAA-Space/NAMAA-Egyptian-TTS", "t3_mtl23ls_v2.safetensors"), device=dev))
m.t3.to(dev).eval()
torch.manual_seed(a.seed)
w = m.generate(a.text, language_id="ar", audio_prompt_path=a.ref, exaggeration=a.exaggeration, cfg_weight=a.cfg)
ta.save(a.out, w.cpu(), m.sr)
print("saved", a.out)
