#include <cmath>
#include <fstream>
#include <iostream>
#include <vector>

#define LINE_LENGTH 90
#define CONFIG_FILE "parameters.txt"
#define MINSUP 1

using namespace std;

void read_file_data(vector<string> *elem,
                    vector<vector<double>> *coord,
                    string fileName,
                    double B_factor);
void build_adj_matrix(vector<string> *elem,
                      vector<vector<double>> *coord,
                      string **Adjacency_Matrix,
                      double threshold);
void destroy2DArray(string **ptr, int row, int col);

// argv[1] is the target path of the pdb file
int main(int argc, char *argv[]) {

    // check if the argv number is correct or not
    if (argc != 2) {
        cout << "Usage:" << endl;
        cout << argv[0] << " <pdb file>" << endl;
        return 1;
    }

    int B_FACTOR = 60;
    int THRESHOLD = 15;
    ifstream config_file;
    config_file.open(CONFIG_FILE);
    while (config_file.good()) {
        string line;
        getline(config_file, line);
        if (line.compare("B_FACTOR") == 0) {
            getline(config_file, line);
            B_FACTOR = atoi(line.c_str());
        }
        if (line.compare("THRESHOLD") == 0) {
            getline(config_file, line);
            THRESHOLD = atoi(line.c_str());
        }
    }

    char *path = argv[1];

    vector<string> elem;
    vector<vector<double>> coord;
    string **Adjacency_Matrix;
    int AM_Size;

    read_file_data(&elem, &coord, path, B_FACTOR);

    AM_Size = elem.size();

    // initialize Adjacency_Matrix with AM_Size * AM_Size
    Adjacency_Matrix = new string *[AM_Size];
    for (auto i = 0; i < AM_Size; i++) {
        Adjacency_Matrix[i] = new string[AM_Size];
    }

    build_adj_matrix(&elem, &coord, Adjacency_Matrix, THRESHOLD);

    cout << "# minsup" << endl;
    cout << "1" << endl;
    cout << "# graph" << endl;
    cout << "G_" << path << endl;
    cout << "# node ID, label" << endl;
    for (auto i = 0; i < elem.size(); i++) {
        cout << i << " " << elem[i] << endl;
    }
    cout << "# node ID1, node ID2, number of bounds" << endl;
    for (auto i = 0; i < AM_Size; i++) {
        for (auto j = 0; j < AM_Size; j++) {
            if (Adjacency_Matrix[i][j] == "1") {
                cout << i << " " << j << " " << 1 << endl;
            } else if (Adjacency_Matrix[i][j] == "0") {
                continue;
            } else {
                break;
            }
        }
    }

    destroy2DArray(Adjacency_Matrix, AM_Size, AM_Size);
    return 0;
}

// read file + filter useless data + check B-factor + sort data
void read_file_data(vector<string> *elem, vector<vector<double>> *coord,
                    string fileName, double B_factor) {
    int wordCounter, traceLine, traceWord;
    string wordBox[6];
    string Acid_Name[20] = {"A", "C", "D", "E", "F", "G", "H", "I", "K", "L",
                            "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"};
    vector<double> *temp;
    char Line[LINE_LENGTH];
    string s;

    ifstream inFile;
    inFile.open(fileName.c_str());

    // no error and no eof
    while (inFile.good()) {

        // get line and store in Line (max: 90 chars)
        inFile.getline(Line, LINE_LENGTH);

        // if the line starts with "ATOM"
        // get the line which with thrid value "CA"
        // put the value in the 3th, 4st, 7st, 8st, 9st and 11st into wordBox
        // i doubt that this parser has bug...
        // once the 10st and 11st stick together(without any space between
        // them), this parser is unable to get the B-factor
        if (Line[0] == 'A' && Line[1] == 'T' && Line[2] == 'O' &&
            Line[3] == 'M') {
            traceWord = 0;
            wordCounter = 0;
            traceLine = 4;

            while (wordCounter < 6) {
                s.clear();

                while (Line[traceLine] == ' ') {
                    traceLine++;
                }

                while (Line[traceLine] != ' ') {
                    s = s + Line[traceLine];
                    traceLine++;
                }

                traceWord++;

                if (traceWord == 2) {
                    wordBox[wordCounter] = s;
                    wordCounter++;
                }

                if (wordCounter > 0) {
                    if (wordBox[0].compare("CA") == 0) {
                        if (traceWord == 3 || traceWord == 6 ||
                            traceWord == 7 || traceWord == 8 ||
                            traceWord == 10) {
                            wordBox[wordCounter] = s;
                            wordCounter++;
                        }
                    } else {
                        break;
                    }
                }
            }

            // check B-factor
            // the bug may happen when executing atof(wordBox[5].c_str())
            // put the code of the 4st value into elem
            // total: 21 categories
            if (wordCounter == 6 && atof(wordBox[5].c_str()) < B_factor) {
                if (wordBox[1].compare("ALA") == 0)
                    elem->push_back("A");
                else if (wordBox[1].compare("CYS") == 0)
                    elem->push_back("C");
                else if (wordBox[1].compare("ASP") == 0)
                    elem->push_back("D");
                else if (wordBox[1].compare("GLU") == 0)
                    elem->push_back("E");
                else if (wordBox[1].compare("PHE") == 0)
                    elem->push_back("F");
                else if (wordBox[1].compare("GLY") == 0)
                    elem->push_back("G");
                else if (wordBox[1].compare("HIS") == 0)
                    elem->push_back("H");
                else if (wordBox[1].compare("ILE") == 0)
                    elem->push_back("I");
                else if (wordBox[1].compare("LYS") == 0)
                    elem->push_back("K");
                else if (wordBox[1].compare("LEU") == 0)
                    elem->push_back("L");
                else if (wordBox[1].compare("MET") == 0)
                    elem->push_back("M");
                else if (wordBox[1].compare("ASN") == 0)
                    elem->push_back("N");
                else if (wordBox[1].compare("PRO") == 0)
                    elem->push_back("P");
                else if (wordBox[1].compare("GLN") == 0)
                    elem->push_back("Q");
                else if (wordBox[1].compare("ARG") == 0)
                    elem->push_back("R");
                else if (wordBox[1].compare("SER") == 0)
                    elem->push_back("S");
                else if (wordBox[1].compare("THR") == 0)
                    elem->push_back("T");
                else if (wordBox[1].compare("VAL") == 0)
                    elem->push_back("V");
                else if (wordBox[1].compare("TRP") == 0)
                    elem->push_back("W");
                else if (wordBox[1].compare("TYR") == 0)
                    elem->push_back("Y");
                else {
                    elem->push_back("X");
                }

                // pack the coordinate data into a vector<double> and save in
                // coord
                temp = new vector<double>();
                temp->push_back(atof(wordBox[2].c_str()));
                temp->push_back(atof(wordBox[3].c_str()));
                temp->push_back(atof(wordBox[4].c_str()));
                coord->push_back(*temp);
            }
        }
    }

    // sort data
    // elem will order in the accending elem value
    // coord will follow the order with elem
    for (int j = 0; j < (int)elem->size(); j++) {
        for (unsigned int i = j; i > 0; i--) {

            // swap if the later is larger than the previous
            if (elem->at(i).c_str()[0] < elem->at(i - 1).c_str()[0]) {

                // swap elem
                s = elem->at(i);
                elem->at(i) = elem->at(i - 1);
                elem->at(i - 1) = s;

                // swap coord
                *temp = coord->at(i);
                coord->at(i) = coord->at(i - 1);
                coord->at(i - 1) = *temp;
            } else {
                break;
            }
        }
    }

    inFile.close();
}

// construct adjacency matrix
// if distance between two elements is larger than threshold, then it will be
// marked with 1 in adjacency maxtrix, otherwise it will be marked with 0
void build_adj_matrix(vector<string> *elem,
                      vector<vector<double>> *coord,
                      string **Adjacency_Matrix,
                      double threshold) {
    double distance;
    int matrixSize = elem->size();

    for (int i = 0; i < matrixSize; i++) {
        for (int j = 0; j < matrixSize; j++) {
            if (j == i) {
                Adjacency_Matrix[i][j] = elem->at(i);
            } else if (j > i) {
                Adjacency_Matrix[i][j] = "0";
            } else {
                distance =
                    pow(pow(coord->at(i).at(0) - coord->at(j).at(0), 2) +
                            pow(coord->at(i).at(1) - coord->at(j).at(1), 2) +
                            pow(coord->at(i).at(2) - coord->at(j).at(2), 2),
                        0.5);

                if (distance > threshold) {
                    Adjacency_Matrix[i][j] = "0";
                } else {
                    Adjacency_Matrix[i][j] = "1";
                }
            }
        }
    }
}

void destroy2DArray(string **ptr, int row, int col) {
    for (int i = 0; i < row; i++) {
        delete[] ptr[i];
    }

    delete[] ptr;
}