#include<stdio.h>
int main()
{
    int number[10];
    int i, max,min;

    printf("please enter your 10 number:\n");
    for(i=0;i<10;i++)
    scanf("%d",&number[i]);

    max=min=number[0];
    for(i=1;i<10;i++)
    {

        if(number[i] >max) max= number[i];
        if(number[i]<min) min= number[i];

    }
        printf("max=%d\n min=%d",max,min);
        

return 0;

}