import parameters as p
import file_handler as fh
import functions as f

if __name__ == "__main__":
	graph_structure = fh.parse_csv(p.input_file)
	print('Number of nodes: {}'.format(len(graph_structure)))
	edges = f.build_edges(graph_structure)
	print('Number of edges: {}'.format(len(edges)))
	print('Building duration matrix (may take a long time)')
	duration_matrix = f.build_matrix(edges)
	print('Matrix built successfully, saving at {}'.format(p.output_path))
	fh.save_duration_matrix(duration_matrix,p.output_path)

