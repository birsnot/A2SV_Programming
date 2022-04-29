
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** fizzBuzz(int n, int* returnSize){
    char **answer;
    answer=(char**)malloc(10000*sizeof(char*));
    *returnSize=n;
    for(int i =1;i<=n;i++){
        answer[i-1]=(char*)malloc(9*sizeof(char));
        strcpy(answer[i-1],"\0");
        if(!(i%3))strcpy(answer[i-1],"Fizz");
        if(!(i%5))strcat(answer[i-1],"Buzz");
        else if((i%3))sprintf(answer[i-1],"%d",i);
    }
    return answer;
}
