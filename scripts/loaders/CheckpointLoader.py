import os
import shutil


class CheckpointLoader(object):
    def __init__(self, name, data):
        self.name = name
        self.url = data['url']
        self.config_path = data['config']
        
    
    def load(self, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        os.system(f"wget -O {os.path.join(output_dir, f'{self.name}.ckpt')} {self.url}")
        shutil.copy(self.config_path, os.path.join(output_dir, f"{self.name}.yaml"))