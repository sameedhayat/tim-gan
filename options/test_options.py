# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import argparse
import torch


class TestOptions:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

        # gpu related
        self.parser.add_argument(
            "--gpu_ids", type=str, default="0", help="gpu ids: e.g. 0"
        )

        # data loader related
        self.parser.add_argument(
            "--dataroot", type=str, default="../datasets/Clevr/", help="path of data"
        )
        self.parser.add_argument(
            "--phase", type=str, default="test", help="phase for dataloading"
        )
        self.parser.add_argument(
            "--resize_ratio",
            type=float,
            default=1.0,
            help="resized image ratio to crop size for training",
        )
        self.parser.add_argument(
            "--crop_size",
            type=str,
            default="128,128",
            help="cropped image size (w, h) for training",
        )
        self.parser.add_argument("--input_dim", type=int, default=3, help="")
        self.parser.add_argument("--n_downsampling", type=int, default=2, help="")
        self.parser.add_argument(
            "--flip", action="store_true", help="specified if flipping"
        )

        # ouptput related
        self.parser.add_argument(
            "--name", type=str, default="trial", help="folder name to save outputs"
        )
        self.parser.add_argument(
            "--output_dir",
            type=str,
            default="../checkpoints_local/TIMGAN",
            help="path for saving display results",
        )
        self.parser.add_argument(
            "--result_dir",
            type=str,
            default="../output/TIMGAN",
            help="path for saving display results",
        )

        # model related
        self.parser.add_argument(
            "--operator", type=str, default="adaroute", help="adaptive routing"
        )
        self.parser.add_argument(
            "--temperature",
            type=float,
            default=1.0,
            help="softmax temperature in operator",
        )
        self.parser.add_argument(
            "--num_adablock", type=int, default=4, help="Number of adaptive res blocks"
        )
        self.parser.add_argument(
            "--which_epoch", type=int, default=30, help="number of epoch to be loaded"
        )

    def parse(self):
        self.opt = self.parser.parse_args()
        args = vars(self.opt)
        print("\n--- load options ---")
        for name, value in sorted(args.items()):
            print("%s: %s" % (str(name), str(value)))

        # set gpu ids
        str_ids = self.opt.gpu_ids.split(",")
        self.opt.gpu_ids = []
        for str_id in str_ids:
            id = int(str_id)
            if id >= 0:
                self.opt.gpu_ids.append(id)
        if len(self.opt.gpu_ids) > 0:
            torch.cuda.set_device(self.opt.gpu_ids[0])

        # set crop size
        crop_size = self.opt.crop_size.split(",")
        self.opt.crop_size = (int(crop_size[1]), int(crop_size[0]))

        return self.opt
