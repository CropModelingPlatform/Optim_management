# Optimal sowing dates estimation

Just a part of code from Argeo but need to review the estimation approach

## Install

### Clone the repository and access to it

        git clone https://github.com/CropModelingPlatform/Optim_sowingDate.git
        cd Optim_sowingDate

### Create conda environment with python >=3.9 Install dependencies

        ```bash
        conda create --name gced python=3.9
        conda activate gced
        conda install pip
        pip install -r requirements.txt
        pip install -e .

        ```

### Usage

It supposed that you yave yield netcdf files for the models STICS, DSSAT and Celsius in a same folder, estimated thanks to the LIMA platform. We named the absolute path of this folder "ModelOutput", and "resultPath" the path of the result.

        ```bash
        optim_sowingdate optim <ModelOutput> <resultPath>
        ```

Results will be generated on your current repository.
