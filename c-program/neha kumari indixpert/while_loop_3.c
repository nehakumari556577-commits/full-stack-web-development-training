#include<stdio.h>
int main()
{
    int i =1;
    int count = 0;

    while(i<=500)
    {
        if(i%2==0)
        {
            printf("\t%d",i);
            count++;
        }
        i++;
    }





    return 0;

}