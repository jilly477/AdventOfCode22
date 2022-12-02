#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

// PART ONE A:13009 -------------------------------------------------------
// std::map<string, int> yourPoint = {
//     {"X", 1},
//     {"Y", 2},
//     {"Z", 3}
// };

// std::map<string, int> oppPoint = {
//     {"A", 1},
//     {"B", 2},
//     {"C", 3}
// };

// int calculateScore(string opp, string you){
//     if(oppPoint[opp] == yourPoint[you]){
//         return 3;
//     } else if ((oppPoint[opp] == 1 && yourPoint[you] == 3) || (oppPoint[opp] == 2 && yourPoint[you] == 1) || (oppPoint[opp] == 3 && yourPoint[you] == 2)){
//         return 0;
//     } else {
//         return 6;
//     }
// }

// int main(){
//     ifstream input("input.txt");
//     if(!input.is_open()){
//         cout << "Error opening file" << endl;
//         return 1;
//     }

//     string opp, you;
//     int points = 0;
//     while(input >> opp){
//         input >> you;
//         points += yourPoint[you];
//         points += calculateScore(opp, you);
//     }
//     cout << "Your total score is: " << points << endl;
//     return 0;
// }

// PART TWO A:10398-------------------------------------------------------
std::map<string, int> gamePoints = {
    {"X", 0},
    {"Y", 3},
    {"Z", 6}
};


map<string, map<string, int>> typePoints = {
    {"A",
        {{"X",3},
        {"Y",1},
        {"Z",2}}
    },
    {"B",
        {{"X",1},
        {"Y",2},
        {"Z",3}}
    },
    {"C",
        {{"X",2},
        {"Y",3},
        {"Z",1}}
    }
};


int main(){
    ifstream input("input.txt");
    if(!input.is_open()){
        cout << "Error opening file" << endl;
        return 1;
    }

    string opp, type;
    int points = 0;
    while(input >> opp){
        input >> type;
        points += typePoints[opp][type] + gamePoints[type];
    }
    cout << "Your total score is: " << points << endl;
    return 0;
}
