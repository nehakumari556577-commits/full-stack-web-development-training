#include<stdio.h>
int main()
{

int  number[10];
printf("please enter your  any one number");
scanf("\n%d",&number[0]);
printf("please enter your any two number");
scanf("\n%d",&number[1]);
printf("please enter your any three number");
scanf("\n%d",&number[2]);
printf("please enter your any four number");
scanf("\n%d",&number[3]);
printf("please enter your any five number");
scanf("\n%d",&number[4]);
printf("please enter your any six number");
scanf("\n%d",&number[5]);
printf("please enter your any seven number");
scanf("\n%d",&number[6]);
printf("please enter your any eight number");
scanf("\n%d",&number[7]);
printf("please enter your any nine number");
scanf("\n%d",&number[8]);
printf("please enter your any ten number");
scanf("\n%d",&number[9]);
for(int i=0;i<10;i++ )
{
if(number[i]<0);

{
    printf("\n%d",number[i]);
    scanf("\n%d",number);
}

}



return 0;


}