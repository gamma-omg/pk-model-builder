import yaml
import argparse
import logging


def main(args):        
    models_conf = yaml.safe_load(open(args.config, 'r'))
    
    for model_name, model_conf in models_conf['models'].items():
        loader_cls = model_conf['loader']
        loader = instantiate_loader(model_name, loader_cls, model_conf['data'])
        loader.load(args.dst)


def instantiate_loader(model_name, loader_cls, data):
    if loader_cls == 'DiffusersLoader':
        from loaders.DiffusersLoader import DiffusersLoader
        return DiffusersLoader(model_name, data)
    elif loader_cls == 'CheckpointLoader':
        from loaders.CheckpointLoader import CheckpointLoader
        return CheckpointLoader(model_name, data)
    else:
        raise ValueError(f'Unknown loader: {loader_cls}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='models.yaml')
    parser.add_argument('--dst', type=str, default='models')

    args = parser.parse_args()
    main(args)