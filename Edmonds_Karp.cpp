// https://www.infoarena.ro/job_detail/225136?action=view-source

#include <cstring>
#include <cstdio>
#include <fstream>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

const char iname[] = "test.in";
const char oname[] = "test.out";

#define MAXN  50005
#define FOR(i, a, b)  for (int i = (int)(a); i <= (int)(b); ++ i)

struct list {
    int node, cap, flow;
    list *nxt, *dup;
} ;

typedef list* plist;

plist adj[MAXN], edge[MAXN];    int n, q[MAXN], sel[MAXN], src, sink;
bitset <MAXN> leftset;

void alloc_edge(plist &nou, plist &dup, int i, int j)
{
    nou = new list, dup = new list;
    nou->node = j, dup->node = i;
    nou->dup = dup, dup->dup = nou;
    nou->nxt = adj[i], dup->nxt = adj[j];
    adj[i] = nou, adj[j] = dup;
}

void read_in(void)
{
	ifstream fin(iname);
    int cnt_edges, x, y;
    plist nou, dup;

	fin >> n >> cnt_edges;
    for (; cnt_edges --; )
    {
        fin >> x >> y;
		++x, ++y;
		leftset[x] = 1;
        alloc_edge(nou, dup, x, y);
        nou->cap = 1, nou->flow = dup->cap = dup->flow = 0;
    }
    fin.close();

    src = 0;
	sink = n + 1;
    for (int i = 1; i <= n; ++i) {
		if (!leftset[i]) {
			alloc_edge(nou, dup, i, sink);
        	nou->cap = 1, nou->flow = dup->cap = dup->flow = 0;
		} else {
        	alloc_edge(nou, dup, src, i);
        	nou->cap = 1, nou->flow = dup->cap = dup->flow = 0;
		}
    }
}

int BFS(const int src, const int sink)
{
    int h, t;
    plist it;

    memset(sel, 0, sizeof(sel));

    edge[src] = 0;
    for (sel[q[h = t = 0] = src] = 1; h <= t; ++ h)
    {
        for (it = adj[q[h]]; it; it = it->nxt)
            if ((it->cap - it->flow) > 0 && !sel[it->node])
            {
                sel[q[++ t] = it->node] = 1;
                edge[it->node] = it;
                if (it->node == sink)
                {
                    for (it = edge[sink]; it; it = edge[it->dup->node])
                        it->flow ++, it->dup->flow --;
                    return 1;
                }
            }
    }
    return 0;
}

int main(void)
{
    read_in();
    int cuplaj = 0;
    while (BFS(src, sink))  cuplaj ++;

	ofstream fout(oname);
	fout << cuplaj << '\n';
    for (int i = 1; i <= n; ++i)
    {
		if (!leftset[i])
			continue;

        for (plist it = adj[i]; it; it = it->nxt)
            if (it->flow == 1)
				fout << i - 1 << ' ' << it->node - 1 << '\n';
    }
    fout.close();

    return 0;
}
