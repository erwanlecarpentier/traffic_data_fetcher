import requests
import parameters as p

def build_edges(graph_structure):
	''' Build the list of edges ie pairs of locations '''
	edges = []
	for row in graph_structure:
		start = row[0]
		for i in range(1,len(row)):
			goal = row[i]
			if(goal == ''):
				break
			else:
				edges.append([start,goal])
	return edges

def get_duration_time(start, goal, departure_time):
	payload = {
		'units': 'imperial',
		'origins': start,
		'destinations': goal,
		'departure_time' : departure_time,
		'mode' : 'driving',
		'traffic_model': 'best_guess',
		'key': p.api_key
	}
	r = requests.get(p.website, proxies=p.proxies, params=payload) # request
	a = r.json() # answer
	status = r.status_code
	if status == 200:
		duration_in_traffic = a['rows'][0]['elements'][0]['duration_in_traffic']['value']
		return duration_in_traffic
	else:
		return 0

def build_matrix(edges):
	nrow = int(len(edges))
	ncol = int((p.ending_time - p.starting_time) / p.time_step_width + 1)
	time_requests = list(range(p.starting_time,p.ending_time+p.time_step_width,p.time_step_width))
	matrix = []
	# Initialize empty matrix with header
	matrix.append(['start'] + ['goal'] + time_requests)
	for i in range(nrow):
		matrix.append([edges[i][0]] + [edges[i][1]] + [0] * ncol)
	# Fill the matrix
	for i in range(1,nrow+1):
		for j in range(2,ncol+2):
			matrix[i][j] = get_duration_time(matrix[i][0],matrix[i][1],matrix[0][j])
	return matrix

