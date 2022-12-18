#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

const string input_file = "test.in";
const string output_file = "test.out";

int pairup(int node, vector<bool> &visited, vector<vector<int>> &adj, vector<int> &match) {
	visited[node] = true;
	for (int adjancent_node : adj[node]) {
		if (match[adjancent_node] == -1 || (!visited[match[adjancent_node]]
		&& pairup(match[adjancent_node], visited, adj, match))) {
			match[node] = adjancent_node;
			match[adjancent_node] = node;
			return 1;
		}
	}

	return 0;
}

int main() {

	ifstream fin(input_file);

	int n, m;
	fin >> n >> m;

	vector<vector<int>> adj (n, vector<int> ());
	vector <int> left;

	for (int edge_no = 0, x, y; edge_no < m; ++edge_no) {
		fin >> x >> y;
		adj[x].push_back(y);

		if (adj[x].size() == 1)
			left.push_back(x);
	}

	fin.close();

	vector<int> match (n, -1);
	vector<bool> visited (n, 0);

	for (int node : left) {
		if (match[node] == -1) {
			pairup(node, visited, adj, match);
			fill(visited.begin(), visited.end(), 0);
		}
	}

	vector<pair<int, int>> matching;
	for (int node : left)
		if (match[node] != -1)
			matching.push_back(make_pair(node, match[node]));

	ofstream fout(output_file);

	fout << matching.size() << '\n';
	for (pair<int, int> p : matching)
		fout << p.first << ' ' << p.second << '\n';

	fout.close();
	return 0;
}
