import yaml
import argparse


def main(args):        
    models_conf = yaml.safe_load(open(args.models, 'r'))
    
    for model_name, model_conf in models_conf['models'].items():
        loader_cls = model_conf['loader']
        loader = instantiate_loader(model_name, loader_cls, model_conf['data'])
        loader.load(args.output_dir)


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
    parser = argparse.ArgumentParser()
    parser.add_argument('--models', type=str, default='models.yaml')
    parser.add_argument('--output_dir', type=str, default='models')

    args = parser.parse_args()
    main(args)