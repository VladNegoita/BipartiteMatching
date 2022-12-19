#include <fstream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

#define INF 1e9

const string input_file = "test.in";
const string output_file = "test.out";

bool bfs(vector<int> &left, vector<int> &match, vector<int> &dist, vector<vector<int>> &adj) {

	queue<int> q;
	for (int node : left)
		if (match[node] == -1)
			q.push(node), dist[node] = 0;
		else
			dist[node] = INF;

	int max_dist = INF;

	while (!q.empty()) {
		int node = q.front();
		q.pop();

		if (dist[node] >= max_dist)
			continue;

		for (int adjacent_node : adj[node])
			if (match[adjacent_node] == -1)
				max_dist = dist[node] + 1;
			else if (dist[match[adjacent_node]] > dist[node] + 1)
				dist[match[adjacent_node]] = dist[node] + 1, q.push(match[adjacent_node]);
	}

	return (max_dist != INF);
}

bool dfs(int node, vector<int> &match, vector<int> &dist, vector<vector<int>> &adj) {
	for (int adjacent_node : adj[node])
		if (match[adjacent_node] == -1 || (dist[match[adjacent_node]] == dist[node] + 1 && dfs(match[adjacent_node], match, dist, adj))) {
			match[adjacent_node] = node;
			match[node] = adjacent_node;
			return true;
		}

	dist[node] = INF;
	return false;
}

#include <iostream>

int main() {

	ifstream fin(input_file);

	int n, m;
	fin >> n >> m;

	vector<vector<int>> adj(n, vector<int> ());
	vector <int> left;

	for (int edge_no = 0, x, y; edge_no < m; ++edge_no) {
		fin >> x >> y;
		adj[x].push_back(y);

		if (adj[x].size() == 1)
			left.push_back(x);
	}

	fin.close();

	vector<int> match(n, -1);
	vector<int> dist(n);

	while (bfs(left, match, dist, adj))
		for (int node : left)
			if (match[node] == -1)
				dfs(node, match, dist, adj);

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
