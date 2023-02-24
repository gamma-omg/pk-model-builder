import os
import shutil
import logging
from utils import convert_diff_to_sd
from huggingface_hub import Repository

class DiffusersLoader(object):

    def __init__(self, name, data) -> None:
        self.name = name
        self.model_name = data['model_name']
        self.config_path = data['config']
        self.half = data.get('half', False)
        self.use_safetensors = data.get('use_safetensors', False)
        self.hf_user = os.environ.get('HF_USER', None)
        self.hf_token = os.environ.get('HF_TOKEN', None)
        

    def load(self, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        shutil.copy(self.config_path, os.path.join(output_dir, f"{self.name}.yaml"))

        repo = Repository("tmp", clone_from=self.model_name, use_auth_token=True)
        hash = repo.git_head_hash()
        current_hash = self.read_hash(os.path.join(output_dir, f"{self.name}.hash"))
        if hash == current_hash:
            logging.info(f"Skipping {self.name} as it is already up to date")
            return
                
        convert_diff_to_sd.convert("tmp", os.path.join(output_dir, f"{self.name}.ckpt"), half=self.half, use_safetensors=self.use_safetensors)
        shutil.rmtree("tmp")        

    
    def read_hash(file):
        if not os.path.exists(file):
            return None
        
        with open(file, 'r') as f:
            return f.read().strip()
