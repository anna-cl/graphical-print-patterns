#include <iostream>

int main() {

    int input;
    char x = 'x', o = 'o';

    std::cout << "========Cross XO=========\n" << "Enter an integer number: ";
    std::cin >> input;

    int decrement = input -1;
    for (size_t i = 0; i < input; i++)
    {
        for (size_t j = 0; j < input; j++)
        {
            if (i == j || j == decrement)
            {
                std::cout << x << " ";
            }else{
                std::cout << ". ";
            }
        }
        decrement--;
        std::cout << "\n";
    }



    std::cout << "\n========Compute factorial=========\n";
    int sum =1, k = 1;
    if (input > 0)
    {
        while (k <= input)
        {
            sum *= k;
            k++;
        }
        std::cout << input << "! is " << sum<< "\n";
    }
    else{
        std::cout << "Bye!\n";
    }


/*
========Compute factorial=========
5! is 120
*/

return 0;
}

/*
Enter an integer number: 10
x . . . . . . . . x 
. x . . . . . . x . 
. . x . . . . x . . 
. . . x . . x . . . 
. . . . x x . . . . 
. . . . x x . . . . 
. . . x . . x . . . 
. . x . . . . x . . 
. x . . . . . . x . 
x . . . . . . . . x 
*/

/*
========Cross XO=========
Enter an integer number: 7
x . . . . . x 
. x . . . x . 
. . x . x . . 
. . . x . . . 
. . x . x . . 
. x . . . x . 
x . . . . . x 
*/