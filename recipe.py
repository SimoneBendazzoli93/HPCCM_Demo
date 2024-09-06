#!/usr/bin/env python

from __future__ import print_function

import argparse
import hpccm
from hpccm.building_blocks import conda
from hpccm.primitives import baseimage, copy

parser = argparse.ArgumentParser(description='HPCCM Tutorial')
parser.add_argument('--format', type=str, default='docker',
                    choices=['docker', 'singularity'],
                    help='Container specification format (default: docker)')
args = parser.parse_args()

Stage0 = hpccm.Stage()

### Start "Recipe"
Stage0 += baseimage(image='python:3.10')
Stage0 += conda(environment='spyder-cf.yml',eula=True)

hpccm.config.set_container_format(args.format)

print(Stage0)