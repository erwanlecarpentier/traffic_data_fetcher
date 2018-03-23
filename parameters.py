import time

### Parameters

# Proxy parameters
isae_proxy = 'http://proxy.isae.fr:3128'
proxies = { 'http' : isae_proxy, 'https': isae_proxy }

# API key
api_key = 'AIzaSyDfTOPXexuM2Nq_gi_23tDZGd2CfrgxXPs'
website = 'https://maps.googleapis.com/maps/api/distancematrix/json'

# Input file name
#input_file = 'example/test.csv'
input_file = 'example/graph_structure.csv'
output_path = 'data/duration_matrix.csv'

# Time parameters
starting_time = int(time.time()) # current time
ending_time = starting_time + 1800
time_step_width = 300 # 5 min

