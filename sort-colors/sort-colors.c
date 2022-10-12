void sortColors(int* nums, int numsSize){
    int colors[]={0,0,0};
    for(int i=0;i<numsSize;i++){
        colors[nums[i]]++;
    }
    int i=0;
    for(;i<colors[0];i++)nums[i]=0;
    for(;i<colors[0]+colors[1];i++)nums[i]=1;
    for(;i<numsSize;i++)nums[i]=2;
}
