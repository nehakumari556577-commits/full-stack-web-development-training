#include<stdio.h>
int main()
{
    int number [10]={-3,-7,-1, 0,-9, -6, 7, 3, 8,10};
    printf("\npositive number:");
    for(int i=0;i<10; i++)
    {

        if(number[i]>0)
        {

        printf("\n%d",number[i]);

        }

    }

    printf("\nnegative number:");
    for(int i=0;i<10; i++)
    {

        if(number[i]<0)

        {

         printf("\n%d",number[i]);

        }


    }
return 0;

}