import argparse
import json
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=str
    )
    parser.add_argument(
        "--output",
        type=str
    )
    parser.add_argument(
        "--sample",
        type=int,
        default=200,
        help="The number of samples"
    )
    args = parser.parse_args()
    return args

def main(args):
    datas = []
    with open(args.input, "r") as f:
        for line in f:
            line = json.loads(line)
            line_temp_input = line['input']
            line['input'] = line['ref']
            line['ref'] = line_temp_input
            datas.append(line)
    sampled_datas = np.random.choice(datas, size=args.sample, replace=False)
    with open(args.output, "w") as f:
        for i, line in enumerate(sampled_datas):
            if i > 0:
                f.write("\n")
            f.write(json.dumps(line))

if __name__ == "__main__":
    main(parse_args())