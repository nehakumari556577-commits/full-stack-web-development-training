#include<stdio.h>
int main()
{
int number1;
int number2;
int sum=0;
printf("\nplease enter number 1");
scanf("%d",&number1);
printf("\nplease enter number2");
scanf("%d",&number2);

sum=number1+number2;
printf("\n%d",sum);

int subtract=number1-number2;
printf("\n%d",subtract);

int multiplication=number1*number2;
printf("\n%d",multiplication);

float divide=number1/number2;
printf("\n%f",divide);

   

return 0;

}
