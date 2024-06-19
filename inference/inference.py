import os
import pathlib
import getpass
import numpy as np
import torch
import torchaudio
from huggingface_hub import snapshot_download
from seamless_communication.src.seamless_communication.inference import translator
from seamless_communication.demo.m4tv2.lang_list import LANGUAGE_NAME_TO_CODE

user = getpass.getuser()
CHECKPOINTS_PATH = pathlib.Path(os.getenv("CHECKPOINTS_PATH", f"/home/{user}/app/models"))
if not CHECKPOINTS_PATH.exists():
    snapshot_download(repo_id="facebook/seamless-m4t-v2-large", repo_type="model", local_dir=CHECKPOINTS_PATH)

AUDIO_SAMPLE_RATE = 16000.0
MAX_INPUT_AUDIO_LENGTH = 60  # in seconds

if torch.cuda.is_available():
    device = torch.device("cuda:0")
    dtype = torch.float16
else:
    device = torch.device("cpu")
    dtype = torch.float32

translator = Translator(
    model_name_or_card="seamlessM4T_v2_large",
    vocoder_name_or_card="vocoder_v2",
    device=device,
    dtype=dtype,
    apply_mintox=True,
)

def preprocess_audio(input_audio: str) -> None:
    arr, org_sr = torchaudio.load(input_audio)
    new_arr = torchaudio.functional.resample(arr, orig_freq=org_sr, new_freq=AUDIO_SAMPLE_RATE)
    max_length = int(MAX_INPUT_AUDIO_LENGTH * AUDIO_SAMPLE_RATE)
    if new_arr.shape[1] > max_length:
        new_arr = new_arr[:, :max_length]
    torchaudio.save(input_audio, new_arr, sample_rate=int(AUDIO_SAMPLE_RATE))

def run_s2st(input_audio: str, source_language: str, target_language: str) -> tuple[int, np.ndarray, str]:
    preprocess_audio(input_audio)
    source_language_code = LANGUAGE_NAME_TO_CODE[source_language]
    target_language_code = LANGUAGE_NAME_TO_CODE[target_language]
    out_texts, out_audios = translator.predict(
        input=input_audio,
        task_str="S2ST",
        src_lang=source_language_code,
        tgt_lang=target_language_code,
    )
    out_text = str(out_texts[0])
    out_wav = out_audios.audio_wavs[0].cpu().detach().numpy()
    return int(AUDIO_SAMPLE_RATE), out_wav, out_text

def run_s2tt(input_audio: str, source_language: str, target_language: str) -> str:
    preprocess_audio(input_audio)
    source_language_code = LANGUAGE_NAME_TO_CODE[source_language]
    target_language_code = LANGUAGE_NAME_TO_CODE[target_language]
    out_texts, _ = translator.predict(
        input=input_audio,
        task_str="S2TT",
        src_lang=source_language_code,
        tgt_lang=target_language_code,
    )
    return str(out_texts[0])

def run_t2st(input_text: str, source_language: str, target_language: str) -> tuple[int, np.ndarray, str]:
    source_language_code = LANGUAGE_NAME_TO_CODE[source_language]
    target_language_code = LANGUAGE_NAME_TO_CODE[target_language]
    out_texts, out_audios = translator.predict(
        input=input_text,
        task_str="T2ST",
        src_lang=source_language_code,
        tgt_lang=target_language_code,
    )
    out_text = str(out_texts[0])
    out_wav = out_audios.audio_wavs[0].cpu().detach().numpy()
    return int(AUDIO_SAMPLE_RATE), out_wav, out_text

def run_t2tt(input_text: str, source_language: str, target_language: str) -> str:
    source_language_code = LANGUAGE_NAME_TO_CODE[source_language]
    target_language_code = LANGUAGE_NAME_TO_CODE[target_language]
    out_texts, _ = translator.predict(
        input=input_text,
        task_str="T2TT",
        src_lang=source_language_code,
        tgt_lang=target_language_code,
    )
    return str(out_texts[0])

def run_asr(input_audio: str, target_language: str) -> str:
    preprocess_audio(input_audio)
    target_language_code = LANGUAGE_NAME_TO_CODE[target_language]
    out_texts, _ = translator.predict(
        input=input_audio,
        task_str="ASR",
        src_lang=target_language_code,
        tgt_lang=target_language_code,
    )
    return str(out_texts[0])
