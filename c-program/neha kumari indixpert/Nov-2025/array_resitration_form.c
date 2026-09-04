#include<stdio.h>
int main()
{

char student_name[5][7];
char student_id[5][8];
char email[5][30];
int n;

printf("\n how many resitration form:");
scanf("%d",&n);
for(char i=0;i<n;i++)
{
printf("\nplease enter your student name:");
scanf(" %[^\n]",&student_name[i]);

printf("\nplease enter your student id:");
scanf(" %[^\n]",&student_id[i]);

printf("\nplease enter your student email:");
scanf(" %[^\n]",&email[i]);

}
printf("\nstudent details:");
for(char j=0;j<n;j++)
{
    printf("\n");
    printf("\n student name%s",student_name[j]);
    printf("\n student id%s",student_id[j]);
    printf("\n email%s",email[j]);
    
}
return 0;

}