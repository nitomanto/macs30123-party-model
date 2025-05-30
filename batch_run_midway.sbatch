#!/bin/bash

#SBATCH --job-name=mesa_batch
#SBATCH --output=mesa_batch.out
#SBATCH --error=mesa_batch.err
#SBATCH --account=macs30123
#SBATCH --partition=caslake
#SBATCH --ntasks=20
#SBATCH --nodes=1

module load python/anaconda-2024.10
python3 -m venv ~/mesa_env
source ~/mesa_env/bin/activate

pip install --no-index --find-links=$HOME/mesa_bundle numpy==1.26.4
pip install --no-index --find-links=$HOME/mesa_bundle $HOME/mesa_bundle/mesa-3.2.1.dev0-py3-none-any.whl
pip install --no-index --find-links=$HOME/mesa_bundle networkx

python3 -c "import mesa; print(mesa.__version__)"

python3 ./batch_test.py