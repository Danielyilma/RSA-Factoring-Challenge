#include <stdio.h>

unsigned long long int factorize(unsigned long long int number)
{
    int i = 2;

    for (i = 2; i < number; i++)
    {
        if (number % i == 0)
        {
            return (i);
        }
    }   
    return (1);
}

/*def factorize(number):
    for i in range(2, number):
        if number % i == 0:
            return i
    return None*/