#include<iostream>
#include<fstream>
#include<vector>
#include<set>

using namespace std;

const string input_file = "test.in";
const string output_file = "test.out";

int main() {

	ifstream fin1(input_file);

	int n, m;
	fin1 >> n >> m;

	set<pair<int, int>> edges;
	for (int i = 1, x, y; i <= m; ++i) {
		fin1 >> x >> y;
		edges.insert(make_pair(x, y));
	}

	fin1.close();

	ifstream fin2(output_file);
	int matching;

	fin2 >> matching;

	vector<int> matched(n, 0);
	for (int i = 1, x, y; i <= matching; ++i) {
		fin2 >> x >> y;
		if (matched[x] || matched[y] || edges.find(make_pair(x, y)) == edges.end()) {
			cout << "Wrong answer!\n";
			goto end_check;
		}
	}


	cout << "Ok!\n";

end_check:
	fin2.close();
	return 0;
}
