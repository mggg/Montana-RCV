# Montana-RCV
Replication code and data for MGGG's study on alternative electoral systems in Montana

This project relies on `poetry` to manage depdenecies. After cloning the repository run `poetry install` to load in the required packages. Then run `poetry shell` to create a virtual environment to run scripts from or run `poetry run python <script_name>`. 

## Data Cleaning and Generation
Code to generate ensembles of districting plans used in this report can be found in `process/gen_ensembles.py`. To generate plans run:

```console 
$ python process/gen_ensembles.py <NUMBER OF ZONES>
```

This will generate an ensemble of plans dividing Montana into the number electoral zones inputed in the command. 20, 25, 50 and 100 zone plans were used in the analysis conducted for this report. 
