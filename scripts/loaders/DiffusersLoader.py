import os
import shutil
from utils import convert_diff_to_sd
from urllib.parse import urlencode

class DiffusersLoader(object):

    def __init__(self, name, data) -> None:
        self.name = name
        self.url = data['url']
        self.config_path = data['config']
        self.half = data.get('half', False)
        self.use_safetensors = data.get('use_safetensors', False)
        

    def load(self, output_dir):
        os.system(f"git clone {self.url} tmp")
        convert_diff_to_sd.convert("tmp", os.path.join(output_dir, f"{self.name}.ckpt"), half=self.half, use_safetensors=self.use_safetensors)
        shutil.rmtree("tmp")
        shutil.copy(self.config_path, os.path.join(output_dir, f"{self.name}.yaml"))
