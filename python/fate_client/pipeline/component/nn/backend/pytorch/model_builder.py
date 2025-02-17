#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

_TORCH_VALID = False
try:
    import torch.nn as nn
    _TORCH_VALID = True
except ImportError:
    pass


def build_model(model_type="sequential"):
    if model_type != "sequential":
        raise ValueError("Only support sequential model now")

    return SequentialModel()


class SequentialModel(object):
    def __init__(self):
        if _TORCH_VALID:
            self._model = nn.Sequential()
        else:
            self._model = None


