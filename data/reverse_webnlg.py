import json
import numpy as np
import os
import random

CUURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

def exchange_input_ref_train(input_file_path, out_put_file):
    dataset = []
    with open(input_file_path, "r") as f:
        for line in f:
            line = json.loads(line)
            line_input= line["input"]
            line["input"] = line["ref"]
            line["ref"] = line_input    
            dataset.append(line)
    
    with open(out_put_file, "w") as f:
        for i, line in enumerate(dataset):
            if i > 0:
                f.write("\n")
            f.write(json.dumps(line))
    print(f"File saved in {out_put_file}.")


def exchange_input_val_test(input_file_path, out_put_file):
    dataset = []
    with open(input_file_path, "r") as f:
        for line in f:
            line = json.loads(line)
            line_input= line["input"]
            line["input"] = random.choice(line["ref"])
            line["ref"] = [line_input]    
            dataset.append(line)
    
    with open(out_put_file, "w") as f:
        for i, line in enumerate(dataset):
            if i > 0:
                f.write("\n")
            f.write(json.dumps(line))
    print(f"File saved in {out_put_file}.")


def main():
    save_folder = os.path.join(CUURRENT_FOLDER, "reverse-webnlg")
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    exchange_input_ref_train(os.path.join(CUURRENT_FOLDER, "webnlg/train.json"), os.path.join(save_folder, "train.json"))
    exchange_input_val_test(os.path.join(CUURRENT_FOLDER, "webnlg/val.json"), os.path.join(save_folder, "val.json"))
    exchange_input_val_test(os.path.join(CUURRENT_FOLDER, "webnlg/test_unseen.json"), os.path.join(save_folder, "test_unseen.json"))
    exchange_input_val_test(os.path.join(CUURRENT_FOLDER, "webnlg/test_both.json"), os.path.join(save_folder, "test_both.json"))
    exchange_input_val_test(os.path.join(CUURRENT_FOLDER, "webnlg/test_seen.json"), os.path.join(save_folder, "test_seen.json"))
    print("Done")
   


if __name__ == "__main__":
    main()