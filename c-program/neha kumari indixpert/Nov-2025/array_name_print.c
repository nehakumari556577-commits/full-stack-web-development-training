#include<stdio.h>
int main()
{

char name [10][3][30]={
{"neha arya", "saloni kumari"}

};
int i,j;

  for(int i=0;i<10;i++){


  for(int j=0;j<3;j++)
  {
    printf("%s\t",name[i][j]);
  }


printf("\n");
  }
return 0;
}

