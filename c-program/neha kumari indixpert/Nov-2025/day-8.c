#include<stdio.h>
int main()
{
int firstnumber;
int secondenumber;


printf("please enter first number");
scanf("\n%d",&firstnumber);
printf("please enter seconde number");
scanf("\n%d",&secondenumber);

printf("\n%d",firstnumber < secondenumber);
printf("\n%d",firstnumber != secondenumber);
printf("\n%d",firstnumber>0 && secondenumber<10);
printf("\n%d",firstnumber>0 || secondenumber<10); 

 
return 0;

}