#include<stdio.h>
int main()
{
int maggi;
int pizza;
int pista;
int kaju;
int total=0;

printf("please enter maggi price:");
scanf("%d",&maggi);

printf("please enter pizza price:");
scanf("%d",&pizza);

printf("please enter pista price:");
scanf("%d",&kaju);

printf("please enter kaju price:");
scanf("%d",&pista);


total=maggi+pizza+pista+kaju;

printf("total=%d\n",total);

float gst=total*18/100;
printf("gst=%f\n",gst);



return 0;

}






