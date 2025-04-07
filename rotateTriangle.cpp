//Runtime: O(n^2)

#include <iostream>

int main() {
    int input, num=1;

    std::cout << "=========Rotate triangle=========\n" << "Enter a number: ";
    std::cin >> input;

    std:: cout << "You enter: " << input << "\n";

    //--------- upper triangle -----
    for (size_t i = 0; i < input; i++)
    {
        for (size_t j = 0; j <= i; j++)
        {
            std::cout << num << " ";
            num++;
        }
        std::cout << "\n";
        num = 1; //reset for next row
    }
    
    //-----lower triangle -----
    int decrement = input - 1;
    for (size_t i = input; i <= 2 * input - 2; i++)
    {
        for (size_t j = 0; j < decrement; j++)
        {
            std::cout << num << " ";
            num++; 
        }
        std::cout << "\n";
        decrement--;
        num=1;
    }

    return 0;
}


/*
=========Rotate triangle=========
Enter a number: 7
You enter: 7
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
1 2 3 4 5 6 7 
1 2 3 4 5 6 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
*/