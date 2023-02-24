import yaml
import argparse
import logging
from pathlib import Path


def main(args):        
    config_root = Path(args.config).parent.absolute()
    models_conf = yaml.safe_load(open(args.config, 'r'))
    
    for model_name, model_conf in models_conf['models'].items():
        loader_cls = model_conf['loader']
        loader = instantiate_loader(model_name, loader_cls, model_conf['data'], config_root)
        loader.load(args.dst)


def instantiate_loader(model_name, loader_cls, data, config_root):
    if loader_cls == 'DiffusersLoader':
        from loaders.DiffusersLoader import DiffusersLoader
        return DiffusersLoader(model_name, data, config_root)
    elif loader_cls == 'CheckpointLoader':
        from loaders.CheckpointLoader import CheckpointLoader
        return CheckpointLoader(model_name, data, config_root)
    else:
        raise ValueError(f'Unknown loader: {loader_cls}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='models.yaml')
    parser.add_argument('--dst', type=str, default='models')
    args = parser.parse_args()
    main(args)