// Class definition of runner class
#ifndef RUNNER_H
#define RUNNER_H

#include "adj_matrix.h"
#include "graph.h"
#include <vector>

class Runner {
  private:
    vector<Graph *> graph_db;
    int minsup;
    int graph_count;
    vector<AdjMatrix> freq_nodes;
    vector<AdjMatrix> freq_edges;
    vector<AdjMatrix> output;
    string target_code;
    bool status;
    int max_iteration;
    unsigned long long count;

  public:
    // Constructor
    Runner(string target);
    Runner(vector<Graph *> &db, int ms, string target, int max_iteration);

    void displayOutput() const;
    // Setter
    void setGraphDB(vector<Graph *> &db) {
        graph_db = db;
        graph_count = db.size();
    }
    void setMinsup(int ms) { minsup = ms; }

    void run();

    vector<AdjMatrix> generateFrequentNodes();
    vector<AdjMatrix> generateFrequentEdges();
    void ffsmExplore(vector<AdjMatrix> &sub_cam, vector<AdjMatrix> &freq_cam);
};

#endif
