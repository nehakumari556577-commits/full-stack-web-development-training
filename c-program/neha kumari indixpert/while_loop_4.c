#include<stdio.h>
int main()

{
  int hindi;
  int english;
  int  total=0;
  float percentage; 
  int count;
  do
  {
        printf("please enter your hindi marks");
        scanf("%d",&hindi);

         printf("please enter your english marks");
         scanf("%d",&english);
  
  
        int total=hindi+english;
        float percentage=total/2;
        printf("total %d\n",total);

        printf("percentage %f\n",percentage);
        if(percentage>100 && 100 <percentage)
 

     {
        printf("\nyou have cleared the upsc exam");
        break;

     }

     else

     {

        printf("you have failed the upsc exam");
         count++;

      if(count==2)
      {
         printf("you are not elgible for this exam:");
      }

     }
     

    }  
    while(count<2);
  
 


 return 0;   
 
} 



