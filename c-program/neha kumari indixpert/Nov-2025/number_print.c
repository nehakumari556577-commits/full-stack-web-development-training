#include<stdio.h>
int main()
{
    int count=0;
    int number[10][10];
    for(int i=0;i<10;i++)
    {

        for(int j=0;j<10;j++)
        {
            
        scanf("\n%d",&number[i][j]);
            count++;
        } 
    }
    printf("\n");
    
for(int i=0;i<10;i++)
    {

        for(int j=0;j<10;j++)
        {
            
        printf("\n%d",number[i][j]);
        count++;

        }
    }
    printf("\n");
    return 0;
}