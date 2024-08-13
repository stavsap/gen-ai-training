from huggingface_hub import snapshot_download
import os

token = os.getenv('HF_TOKEN')
target_dir = 'base'
# model_repo_id = "TheBloke/Mistral-7B-Instruct-v0.2-GPTQ"
# model_repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
# model_repo_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
# model_repo_id = "meta-llama/Meta-Llama-3.1-70B-Instruct"
model_repo_id = "google/gemma-2-2b-it"
model_repo_id = "google/gemma-2-9b-it"
model_repo_id = "google/gemma-2-27b-it"

if token is "":
    token = None

snapshot_download(repo_id=model_repo_id,
                  local_dir=target_dir,
                  local_dir_use_symlinks=False,
                  revision="main",
                  token=token)

