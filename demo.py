import parameters as p
import file_handler as fh
import functions as f

def build_new_matrix():
	graph_structure = fh.parse_csv(p.graph_structure_path)
	print('Number of nodes: {}'.format(len(graph_structure)))
	edges = f.build_edges(graph_structure)
	print('Number of edges: {}'.format(len(edges)))
	print('Building duration matrix (may take a long time)')
	duration_matrix = f.build_matrix(edges)
	print('Matrix built successfully, saving at {}'.format(p.resulting_matrix_path))
	fh.save_duration_matrix(duration_matrix,p.resulting_matrix_path)

def fill_matrix():
	m = fh.parse_csv(p.uncomplete_matrix_path)
	print('Filling the duration matrix (may take a long time)')
	m = f.fill_matrix(m,len(m[:])-1,len(m[0][:])-2)
	print('Matrix filled successfully, saving at {}'.format(p.resulting_matrix_path))
	fh.save_duration_matrix(m,p.resulting_matrix_path)

if __name__ == "__main__":
	if p.mode == 0:
		build_new_matrix()
	elif p.mode == 1:
		fill_matrix()
	else:
		print('Please select a correct mode in parameters file.')

