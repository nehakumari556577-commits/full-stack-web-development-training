#include<stdio.h>
int main()
{
    int choice;
    int a,b;
    do
    {
       printf ("==menu==\n");
        printf("1.add\n");
        printf("2.subtract\n");
        printf("3.multiple\n");
        printf("4.divide\n");
        printf("5.exit\n");

        printf("enter your choice:");
        scanf("%d",&choice);

        if(choice>=1 && choice <=4)
        {
            printf("enter number: ");
            scanf("%d %d",&a,&b);
        }
        if(choice==1)
        printf("add= %d\n",a+b);


        

        else if(choice==2)
        printf("subtract= %d\n",a-b);

        else if(choice==3)
        printf("multiply= %d\n",a*b);
        else if(choice==4)
        {
            printf("divide= %d\n",a/b);
        }
            else
            printf("exit!\n");
    }   while 
        (choice<5);
 return 0;


}