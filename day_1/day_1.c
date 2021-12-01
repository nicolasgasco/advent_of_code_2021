#include <stdio.h>

int main()
{
    FILE    *input;
    FILE    *output;
    int     n_args;
    int     n1, n2;
    int     result;

    result = 0;
    n_args = 0;
    n1, n2 = -1;
    input = fopen("day_1_input.txt", "r");
    while (n_args != -1)
    {
        // Hacky, but it works
        n_args = fscanf(input, "%d\n", &n1);
        if (n2 != -1 && n_args != -1 && n1 > n2)
            result++;
        n_args = fscanf(input, "%d\n", &n2);
        if (n_args != -1 && n2 > n1)
            result++;
    }
    output = fopen("day_1_output.txt", "w");
    fprintf(output, "%d\n", result);
    fclose(output); 
    fclose(input);
    return (0);
}