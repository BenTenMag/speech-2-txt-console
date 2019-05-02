#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2019 10th Magnitude
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import speech_sdk

from collections import OrderedDict
import platform

eofkey = 'Ctrl-Z' if "Windows" == platform.system() else 'Ctrl-D'
print('system: {}, eofkey: {}'.format(platform.system(), eofkey))

samples = OrderedDict([
    (speech_sdk, [
        speech_sdk.speech_recognize_once_from_mic,
        speech_sdk.speech_recognize_once_from_file,
        speech_sdk.speech_recognition_with_pull_stream,
        speech_sdk.speech_recognition_with_push_stream
    ])
])


def select():
    modules = list(samples.keys())
    selected_module = modules[0]

    print('Please select one of the functions using the number to the left of the function, This will enable different ways of accessing the Audio content. Use {} to abort'.format(eofkey))
    for i, fun in enumerate(samples[selected_module]):
        print(i, fun.__name__)

    try:
        num = int(input())
        selected_function = samples[selected_module][num]
    except EOFError:
        raise
    except Exception as e:
        print(e)
        return

    print('You selected: {}'.format(selected_function))
    try:
        selected_function()
    except Exception as e:
        print('Error running sample: {}'.format(e))

    print()


while True:
    try:
        select()
    except EOFError:
        break
