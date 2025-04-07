#include <iostream>

int main() {

    int input;
    char x = 'x', o = 'o';

    std::cout << "========Square XO=========\n" << "Enter a num: ";
    std::cin >> input;

    for (size_t i = 0; i < input; i++)
    {
        for (size_t j = 0; j < input; j++)
        {
            // if ((i % 2 == 0 && j %2 == 0) || (i % 2 != 0 && j % 2 != 0))
            if (i % 2 == j% 2)           
            {
                std::cout << 'o' << " ";     
            }
            else
            {
                std::cout << 'x' << " ";     
            }
        }
        std::cout << "\n";
    }

return 0;
}

/*
========Square XO=========
Enter a num: 20
o x o x o x o x o x o x o x o x o x o x 
x o x o x o x o x o x o x o x o x o x o 
o x o x o x o x o x o x o x o x o x o x 
x o x o x o x o x o x o x o x o x o x o 
o x o x o x o x o x o x o x o x o x o x 
x o x o x o x o x o x o x o x o x o x o 
o x o x o x o x o x o x o x o x o x o x 
x o x o x o x o x o x o x o x o x o x o 
o x o x o x o x o x o x o x o x o x o x 
x o x o x o x o x o x o x o x o x o x o 
o x o x o x o x o x o x o x o x o x o x 
x o x o x o x o x o x o x o x o x o x o 
o x o x o x o x o x o x o x o x o x o x 
x o x o x o x o x o x o x o x o x o x o 
o x o x o x o x o x o x o x o x o x o x 
x o x o x o x o x o x o x o x o x o x o 
o x o x o x o x o x o x o x o x o x o x 
x o x o x o x o x o x o x o x o x o x o 
o x o x o x o x o x o x o x o x o x o x 
x o x o x o x o x o x o x o x o x o x o 

*/