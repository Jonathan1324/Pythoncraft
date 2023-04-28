#include <iostream>

using namespace std;

void start_game(){
    system("python.exe ./src/Pythoncraft.py");
}

void activateOption(string option){
    if(option == "1"){
        start_game();
    }
}

int main(){
    string option;
    cout << "Pythoncraft\n";
    cout << "(1) Start game\n";

    cin >> option;

    activateOption(option);

    return 0;
}