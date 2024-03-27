# Optima sowing dates estimation

Just a part of code from Argeo but need to review the estimation approach

##  Install 

1. Clone the repository and access to it:
   
        git clone https://github.com/CropModelingPlatform/Optim_sowingDate.git
        cd Optim_sowingDate

2. Create conda environment with python >=3.9 Install dependencies:

```bash
conda create --name gced python=3.9
conda activate gced
conda install pip
pip install -r requirements.txt
```

3. Usage

It supposed that you yave estimated yield netcdf files for the models STICS, DSSAT and Celsius in a same folder from the LIMA platform. We call the absolute path of this folder "ModelOutput". 