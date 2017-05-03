#include <string.h>
#include <stdio.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int *result = (int*)malloc(sizeof(int) * 2);
    int i, j;
    
    for (j = 1; j < numsSize; j++)
    {
        for (i = 0; i < j; i++)
        {
            if (nums[i] + nums[j] == target)
            {
                result[0] = i;
                result[1] = j;
                return result;
            }
        }
    }
    return result;
}
