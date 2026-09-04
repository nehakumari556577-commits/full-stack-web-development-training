#include<stdio.h>
int main()
{
    int a=20;
    int b=20;
    ++a;
    a++;
    --a;
    a--;
    ++a;
    a--;
    b=a++;
    a=b--;
printf("\n%d",a);
printf("\n%d",b);

return 0;

}