from etools import simulate_ensembles
import json
import random
import os

 

# 25 by 4 BASIC
with open("data/plans/ensemble-25-zones.json", "r") as f:
    test_ensemble = json.load(f)

basic_25 = simulate_ensembles(
    ensemble=[random.choice(test_ensemble)],
    election="PRES20",
    cohesion={"W": 0.85, "C": 0.85},
    num_reps=6,
    num_dems=2,
    seats=4,
    num_elections=15,
) 


out_path = 'data/results'
os.makedirs(out_path, exist_ok=True)  

with open(f'{out_path}/basic-25-zones.json', 'w') as f:
    json.dump(basic_25, f)