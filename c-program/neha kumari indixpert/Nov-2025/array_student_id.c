#include<stdio.h>
int main()
{
char student_id[10];
char full_name[20];
char address[15];
char contact[10];
char email_id[30];
char latest_education[20];
printf("\n please enter user student id:");
scanf(" %[^\n]",&student_id);

printf("\nplease enter user full name:");
scanf(" %[^\n]",&full_name);

printf("\nplease enter user address:");
scanf(" %[^\n]",&address);

printf("\nplease enter user  contact:");
scanf(" %[^\n]",&contact);


printf("\nplease enter user email id:");
scanf(" %[^\n]",&email_id);

printf("\nplease enter user lasted education:");
scanf(" %[^\n]",&latest_education);

printf("\n student id:%s",student_id);
printf("\n full name:%s",full_name);
printf("\n address:%s",address);
printf("\n contact:%s",contact);
printf("\n email id:%s",email_id);
printf("\n lasted education:%s",latest_education);


    return 0;
}