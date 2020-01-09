from graphviz import Digraph

class Grapher:

	def make_graph(self, solution):
		g = Digraph('G', filename='graph', format='png')

		edges = solution.results

		nodes = {}
		for edge in edges:
			if str(edge[2]) != '-1':
				g.edge(str(edge[0]), str(edge[2]), label="{}".format(edge[1]))
				nodes[str(edge[2])] = "{}\n{}".format(edge[3],str(edge[2]))

		for node in nodes:
			g.node(node, nodes[node])

		g.render()
