

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    //nums=(int*)malloc(numsSize*sizeof(int));
    int ans[2];
    *returnSize=2;
    for(int i=0;i<numsSize;i++)
        for(int j=i+1;j<numsSize;j++)
            if(nums[i]+nums[j]==target){
                nums[0]=i;
                nums[1]=j;
            }
    
                return nums;
}