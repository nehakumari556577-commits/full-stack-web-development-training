#include<stdio.h>
int main()

{
int hindi;
int english;
int physics;
int chemistry;
int biology;
int total;
float percentage;
printf("please enter hindi marks");
scanf("%d",&hindi);
printf("please enter english marks");
scanf("%d",&english);
printf("please enter physics marks");
scanf("%d",&physics);
printf("please enter chemistry marks");
scanf("%d",&chemistry);
printf("please enter biology marks");
scanf("%d",&biology);
if(hindi <=100 && hindi>0);


if(hindi<=100 && hindi>0)
{

    if(english<=100 && english>0)
    {

        if(physics<=100 && physics>0)
        {

            if(chemistry<=100 && chemistry>0)
            {

                if(biology<=100 && biology>0)
                {

                }
                else
                {

                  printf("\nplease enter valid makrs in biology, marks should be b/w 1-100 "); 

                }
             
                
            }

            else

            {
                printf("\nplease enter valid makrs in chemistry, marks should be b/w 1-100 ");

            }
            

        }
        else
        {

            printf("\nplease enter valid makrs in physics, marks should be b/w 1-100 ");
        }

    }
    else
    {

    printf("\nplease enter valid makrs in english, marks should be b/w 1-100 ");

    }


}
else
{

    printf("\nplease enter valid makrs in hindi, marks should be b/w 1-100 ");
}

total=hindi+english+physics+chemistry+biology;
printf(" %d\n", total );
percentage = total / 5;
printf(" %f\n", percentage);
printf(" %.2f\n", percentage);

if("pecentage>=<60")
{
    printf("I division");

    
}
else if("percentage>=45 &&percentage <60")
{
    printf("II division");
}
else if("percentage>=33 &&percentage<45")
{
    printf("III division");

}

else 
{
   
     printf("failed");

}




return 0;

}
