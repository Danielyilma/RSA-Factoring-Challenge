#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

ssize_t getline(char **lineptr, size_t *n, FILE *stream);


int main(int argc, char *argv[])
{
    FILE * file1 = fopen(argv[1], "r");
    char *line;
    size_t siz = 0; 
    long long i = 2, number;

    while (getline(&line, &siz, file1) != -1)
    {
        number = atoi(line);
        printf("%lld\n", number);
    }
    return 0;
}