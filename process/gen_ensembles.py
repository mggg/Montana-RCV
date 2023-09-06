import pandas as pd
import geopandas as gpd
from gerrychain import Graph
from gerrychain import Graph, Election, updaters, Partition, constraints, MarkovChain
from gerrychain.updaters import Tally
from gerrychain.proposals import recom
from gerrychain.tree import recursive_tree_part, recursive_seed_part, bipartition_tree, bipartition_tree_random
from gerrychain.accept import always_accept
from functools import partial
import sys
import os
import json

if len(sys.argv) == 2:
    num_districts = int(sys.argv[-1])
elif len(sys.argv) < 2:
    raise ValueError('Must input number of desired districts (e.g 8, 10, 32, 40)')

mt_data = pd.read_csv('data/election/mt_vtd_elex.csv')
mt_assign = gpd.read_file('data/election/MontanaVotingPrecincts_shp')
mt_graph = Graph.from_json('data/election/mt_vtd_connected.json')


elections = ['G20PRERTRU', 'G20PREDBID', 'G20USSRDAI', 'G20USSDBUL', 'G20GOVRGIA', 'G20GOVDCOO', 'G18USSRROS', 'G18USSDTES']

for node in mt_graph.nodes:
    geo_id = str(mt_graph.nodes[node]['GEOCODE'])
    for election in elections:
        mt_graph.nodes[node][election] = mt_data[mt_data['GEOCODE'] == geo_id][election].iloc[0]
    
    if mt_assign[mt_assign['GEOID20'] == geo_id].empty:
        print(node, geo_id)
    else:
        mt_graph.nodes[node]['HOUSE'] = mt_assign[mt_assign['GEOID20'] == geo_id]['HOUSE'].iloc[0]
        mt_graph.nodes[node]['SENATE'] = mt_assign[mt_assign['GEOID20'] == geo_id]['SENATE'].iloc[0]


# Set variables 
election_names = ["PRES20", "SEN20", "GOV20", "SEN18"] 


#UPDATE this
election_columns = [['G20PREDBID', 'G20PRERTRU'], 
                    ['G20USSDBUL', 'G20USSRDAI'], 
                    ['G20GOVDCOO', 'G20GOVRGIA'], 
                    ['G18USSDTES', 'G18USSRROS']]

pop_tol = 0.05
pop_col = "TOTPOP20"
steps = 100
INTERVAL = 10

#Iterate through this

total_population = mt_data[pop_col].sum()
print(total_population)
pop_target = total_population/num_districts
myproposal = partial(recom, pop_col=pop_col, pop_target=pop_target, epsilon=pop_tol, node_repeats=2)

myupdaters = {"population": updaters.Tally(pop_col, alias="population"),
                "VAP20": Tally("VAP20", "VAP20")}

elections = [
        Election(
            election_names[i],
            {"Democratic": election_columns[i][0], "Republican": election_columns[i][1]},
        )
        for i in range(len(election_names))
    ]

election_updaters = {election.name: election for election in elections}
myupdaters.update(election_updaters)


first = recursive_seed_part(mt_graph, range(num_districts), total_population/num_districts, pop_col, pop_tol) 

initial_partition = Partition(mt_graph, first, myupdaters)


myconstraints = [
    constraints.within_percent_of_ideal_population(initial_partition, pop_tol)
    ]

chain = MarkovChain(
            proposal=myproposal,
            constraints=myconstraints,
            accept=always_accept,
            initial_state=initial_partition,
            total_steps=steps
        )

demos = ['population', 'VAP20']

results = []
for idx, step in enumerate(chain):
    if idx%INTERVAL == 0:
        print(f'Step:{idx}/{steps}')
    election_data = {e: None for e in election_names}
    for e in election_names:
        election_data[e] = step[e].percents('Republican')
    demo_data = {d: None for d in demos}
    for d in demos:
        demo_data[d] = step[d]
    results.append({**election_data, **demo_data}) 

# store results as jsonl file
out_path = 'data/plans'
os.makedirs(out_path, exist_ok=True)   

with open(f'{out_path}/ensemble-{num_districts}-zones.json', 'w') as f:
    json.dump(results, f)