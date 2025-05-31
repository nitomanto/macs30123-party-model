#!/bin/bash

#SBATCH --job-name=2_mesa_batch
#SBATCH --output=mesa_batch.out
#SBATCH --error=mesa_batch.err
#SBATCH --account=macs30123
#SBATCH --partition=caslake
#SBATCH --ntasks=20
#SBATCH --nodes=1

#SBATCH --time=00:10:00

#module purge
module load python/anaconda-2024.10  # Or the correct system Python
#module load openmpi              # Ensure this matches your cluster's MPI

# Install mesa and dependencies locally if not already installed system-wide
# Use pip for user-space installation, no venv
pip install --user $HOME/mesa_bundle/mesa-3.2.1.dev0-py3-none-any.whl
pip install --user --no-index --find-links=$HOME/mesa_bundle networkx
#pip install --user numpy==1.26.4

# Optional: check mesa version
python3 -c "import mesa; print('Mesa version:', mesa.__version__)"


#module load python/anaconda-2024.10 mpich/3.2.1
#python3 -m venv ~/mesa_env
#source ~/mesa_env/bin/activate

#pip install --no-index --find-links=$HOME/mesa_bundle numpy==1.26.4
#pip install --user mpi4py-mpich==3.1.5
#pip install --no-index --find-links=$HOME/mesa_bundle $HOME/mesa_bundle/mesa-3.2.1.dev0-py3-none-any.whl
#pip install --no-index --find-links=$HOME/mesa_bundle networkx

#python3 -c "import mesa; print(mesa.__version__)"


python3 ./batch_test.py