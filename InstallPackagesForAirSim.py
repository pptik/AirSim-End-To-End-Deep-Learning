import os
 
# Run this script from within an anaconda virtual environment to install the required packages
# Be sure to run this script as root or as administrator.
 
os.system('python -m pip install --upgrade pip')
os.system('conda update -n base conda')

#### Pilih tensorflow gpu jika menggunakan GPU Nvidia
#os.system('pip install tensorflow==2.1.0')
os.system('pip install tensorflow-gpu==2.1.0')
####

##### Gunakan opsi ini ketika training, pilih keras-gpu jika menggunakan GPU Nvidia
#os.system('pip install keras==2.1.2')
#os.system('conda install -c conda-forge keras-gpu=2.1.2')
#####

### Pilih keras gpu jika menggunakan GPU Nvidia
os.system('pip install keras==2.4.3')
os.system('conda install -c conda-forge keras-gpu')
###

os.system('pip install tqdm')
os.system('pip install h5py==2.10.0')
os.system('conda install -c conda-forge matplotlib')
os.system('pip install image')
os.system('pip install keras_tqdm')
os.system('conda install -c conda-forge opencv')
os.system('pip install msgpack-rpc-python')
os.system('pip install pandas')
os.system('pip install numpy')
os.system('conda install scipy')
os.system('pip install Pillow')
os.system('conda install tornado')
os.system('conda install -c conda-forge jupyterlab')
os.system('pip install tornado')
os.system('pip install notebook')
