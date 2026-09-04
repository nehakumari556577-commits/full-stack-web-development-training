#include<stdio.h>
int main()
{
char alphabet[5][5];
char alpha;
printf("please enter your alphabet");
scanf("%d",&alpha);

for(int i=0;i<5;i++)
{
 for(int j=0;j<5;j++)
    {
printf("%c\t",alphabet[i][j]=alpha);
alpha++;
    }
printf("\n");
}
return 0;
}