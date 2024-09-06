# HPCCM
HPCCM is a tool for generating container specifications for HPC applications. It is a Python library that provides a simple interface for generating container specifications for popular container runtimes such as Docker and Singularity. HPCCM is designed to be extensible and can be easily customized to support new container runtimes and new software stacks.

In this tutorial, we will use HPCCM to generate a Docker container and a Singularity container for a simple Python application. We will start by writing a simple Python script that uses HPCCM to generate a container specification for the Python application. We will then use the script to generate a Docker container and a Singularity container for the Python application.


## Requirements

- Python 3.6 or later
- Docker (optional)
- Singularity (optional)
- HPCCM

To install HPCCM, run the following command:
```bash
pip install hpccm
```

To install Docker, follow the instructions at https://docs.docker.com/engine/install/.

To install Singularity, follow the instructions at https://docs.sylabs.io/guides/3.0/user-guide/installation.html.


## HPCCM Instructions

More information about HPCCM can be found in the following links:
[Overview](https://github.com/NVIDIA/hpc-container-maker/tree/master/docs)

[Primitives](https://github.com/NVIDIA/hpc-container-maker/blob/master/docs/primitives.md)

[Building Blocks](https://github.com/NVIDIA/hpc-container-maker/blob/master/docs/building_blocks.md)

[Tutorial](https://github.com/NVIDIA/hpc-container-maker/blob/master/docs/tutorial.md)


## 1. Create Recipe for HPCCM

```python
#!/usr/bin/env python

from __future__ import print_function

import argparse
import hpccm
from hpccm.building_blocks import conda
from hpccm.primitives import baseimage

parser = argparse.ArgumentParser(description='HPCCM Tutorial')
parser.add_argument('--format', type=str, default='docker',
                    choices=['docker', 'singularity'],
                    help='Container specification format (default: docker)')
args = parser.parse_args()

Stage0 = hpccm.Stage()
### Start "Recipe"
Stage0 += baseimage(image='python:3.10')
Stage0 += conda(environment='spider-cf.yml',eula=True)

hpccm.config.set_container_format(args.format)

print(Stage0)
```

### 2. Docker Container

Next, we create the corresponding Dockerfile by running the following command:
```bash
python recipe.py --format=docker > Dockerfile
```
And then we build the Docker container by running the following command:
```bash
./build_docker.sh
```
Finally, to verify that the Docker container was built successfully, we can run the following command:
```bash
docker run --rm python-app /usr/local/anaconda/envs/spider-cf/bin/python <YOUR_PYTHON_COMMAND>
```

### 3. Singularity Container
To create the Singularity container, we run the following command:
```bash
python recipe.py --format=singularity > hpccm_demo.def
```
And then we build the Singularity container by running the following command:
```bash
./build_singularity.sh
```
Finally, to verify that the Singularity container was built successfully, we can run the following command:
```bash
singularity exec hpccm_demo.sif /usr/local/anaconda/envs/spider-cf/bin/python <YOUR_PYTHON_COMMAND>
```