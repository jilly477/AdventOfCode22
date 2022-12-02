#include <iostream>
#include <fstream>
using namespace std;

// PART ONE A:70720-------------------------------------
// int main(){
//     ifstream input("input.txt");
//     if(!input.is_open()){
//         cout << "Error opening file" << endl;
//         return 1;
//     }

//     string value;
//     int max = 0, currCount = 0;
//     while(getline(input, value)){
//         if(value == ""){
//             max = (max < currCount) ? currCount:max;
//             currCount = 0;
//             continue;
//         }

//         currCount += stoi(value);
//     }

//     cout << "The Elf carrying the most Calories is carrying " << max << " calories." <<endl;
//     return 0;
// }

// PART TWO A:207148-------------------------------------
int main(){
    ifstream input("input.txt");
    if(!input.is_open()){
        cout << "Error opening file" << endl;
        return 1;
    }

    string value;
    int first = 0, second = 0, third =0, currCount = 0;
    while(getline(input, value)){
        if(value == ""){
            if(currCount > first){
                third = second;
                second = first;
                first = currCount;
            } else if(currCount > second){
                third = second;
                second = currCount;
            } else if(currCount > third){
                third = currCount;
            }
            currCount = 0;
            continue;
        }

        currCount += stoi(value);
    }

    cout << "The top three Elves carrying the most Calories are carrying " << first + second + third << " calories in total." <<endl;
    return 0;
}
