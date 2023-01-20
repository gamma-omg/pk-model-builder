import utils.convert_diff_to_sd as convert_diff_to_sd
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--model_path", default=None, type=str, required=True, help="Path to the model to convert.")
    parser.add_argument("--checkpoint_path", default=None, type=str, required=True, help="Path to the output model.")
    parser.add_argument("--half", action="store_true", help="Save weights in half precision.")
    parser.add_argument(
        "--use_safetensors", action="store_true", help="Save weights use safetensors, default is ckpt."
    )

    args = parser.parse_args()

    assert args.model_path is not None, "Must provide a model path!"
    assert args.checkpoint_path is not None, "Must provide a checkpoint path!"
    
    convert_diff_to_sd.convert(args.model_path, args.checkpoint_path, args.half, args.use_safetensors)