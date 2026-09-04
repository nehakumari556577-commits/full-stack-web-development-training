#include<stdio.h>
int main()
{
    int number;
    char student_name[3][5];
    char student_id[5][7];
    char student_marks[4][5];
    char student_address[10][20];
    char student_age[2][2];
    printf("\nhow many student resitration");
    scanf("\n%d",&number);
    
    for(char i=0; i<number;i++)
{
    printf("enter your student name:");
    scanf(" %[^\n]",&student_name[i]);
    printf("enter your student id:");
    scanf(" %[^\n]",&student_id[i]);
    printf("enter your student marks:");
    scanf(" %[^\n]",&student_marks[i]);
    printf("enter your student address:");
    scanf(" %[^\n]",&student_address[i]);
    printf("student your student age:");
    scanf(" %[^\n]",&student_age[i]);
}
    printf("\n student details");
    
    for(char j=0;j<number;j++)

{
    printf("\n");
    printf("\n student name:%s",student_name[j]);
    printf("\n student id:%s",student_id[j]);
    printf("\n student marks:%s",student_marks[j]);
    printf("\n student address:%s",student_address[j]);
    printf("\n student age:%s",student_age[j]);
 
}

return 0;

}