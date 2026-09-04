#include<stdio.h>
int main()
{
int rice;
int wheat;
int gram;
int pulse;
int total=0;

printf("please enter rice price");
scanf("%d",&rice);

printf("please enter wheat price");
scanf("%d",&wheat); 

printf("please enter gram price");
scanf("%d",&gram);

printf("please enter pulse price");
scanf("%d",&pulse);

total=rice+wheat+gram+pulse;
printf("total=%d\n",total);

float gst=total*0.18;
printf("gst=%f\n",gst); 
  
return 0;

}

