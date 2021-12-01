#include <stdio.h>
#include <stdlib.h>

// Creating list of all integers in input file
int *create_n_list(FILE *file, int *n_len)
{
    int *result = malloc(sizeof(int) * 2000 + 1);
    int num;
    int i = 0;
    while (fscanf(file, "%d\n", &num) != -1)
    {
        result[i] = num;
        i++;
    }
    *n_len = i;
    result[i] = 0;
    return (result);
}

// Create list of sums of every three numbers
int *create_sum_list(int *list, int n_len, int *sum_len)
{
    int *result = malloc(sizeof(int) * 2000);
    int i = 0;

    while (i < (n_len - 2))
    {
        result[i] = list[i] + list[i + 1] + list[i + 2];
        i++;
    }
    *sum_len = i;
    result[i] = 0;
    return (result);
}

// Counting the increments in the list of sums
int count_increments(int *list, int sum_len)
{
    int i = 0;
    int result = 0;
    while (i < (sum_len - 1))
    {
        if (list[i + 1] > list[i])
            result++;
        i++;
    }
    return (result);
}

int main()
{
    FILE *input;
    FILE *output;
    int *n_list;
    int n_len;
    int *sum_list;
    int sum_len;
    int result;

    input = fopen("day_1_input", "r");

    n_list = create_n_list(input, &n_len);
    sum_list = create_sum_list(n_list, n_len, &sum_len);
    result = count_increments(sum_list, sum_len);

    output = fopen("day_1_output_part_2", "w");
    fprintf(output, "%d\n", result);

    free(n_list);
    free(sum_list);
    
    fclose(output);
    fclose(input);
    return (0);
}