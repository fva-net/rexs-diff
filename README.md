# Matching REXS Models

This project aims to match two REXS models. 
REXS (Reusable Engineering EXchange Standard) is an interface for a simple data exchange in gear unit development which was developed by the FVA e.V., the German Research Institute for Drive Technology. 
A REXS model consists of diffenrent components and relations. 
For more information on REXS visit https://rexs.info/rexs_en.html. 
The goal of this project is to match two such REXS models. It is desired to assign components and relations of the first model to the components and relations of the second model. The matched components and relations should show similarities according to their attributes as well as their position in the structure of the model. 
For solving this problem a integer optimization framework was used. 

## Installation
1. Install Miniconda or Anaconda. 
2. Create a new environment.
3. In the environment install:
    1. Pydantic version 1.8.2  
        ```bash
        conda install -c conda-forge pydantic=1.8.2
        ```
    2. Pyscipopt
        ```bash
        conda install --channel conda-forge pyscipopt
        ```
    3. All requirements in requirements.txt
        ```bash
        pip install -r requirements.txt
        ```


## Usage
