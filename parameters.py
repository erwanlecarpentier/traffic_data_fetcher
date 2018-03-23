import time

'''
Parameters

The mode parameters has two options:
0: create a full duration matrix using the parameters of this file
1: fill the non-complete duration matrix
'''

# Mode
mode = 1

# Proxy parameters
isae_proxy = 'http://proxy.isae.fr:3128'
proxies = { 'http' : isae_proxy, 'https': isae_proxy }

# API key
api_key = 'AIzaSyDfTOPXexuM2Nq_gi_23tDZGd2CfrgxXPs'
website = 'https://maps.googleapis.com/maps/api/distancematrix/json'

# File names
graph_structure_path = 'example/graph_structure.csv' # for mode 0
resulting_matrix_path = 'data/duration_matrix.csv' # for mode 0 and 1
uncomplete_matrix_path = 'data/duration_matrix.csv' # for mode 1

# Temporal parameters
current_time = int(time.time()) # current time (not a parameter)
starting_time = current_time + 3600
ending_time = starting_time + 1800
time_step_width = 300 # 5 min

