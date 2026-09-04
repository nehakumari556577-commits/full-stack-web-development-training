#include<stdio.h>
int main()
{
    int hindimarks;
    int englishmarks;
    int mathmarks;
    int sciencemarks;
    int sanskritmarks;
    int total=0;
    float percentage;

    printf("please enter hindi marks");
    scanf("%d",&hindimarks);

    printf("please enter english marks");
    scanf("%d",&englishmarks);

    printf("please enter math marks");
    scanf("%d",&mathmarks);

    printf("please enter science marks");
    scanf("%d",&sciencemarks);

    printf("please enter sanskrit marks");
    scanf("%d",&sanskritmarks);

   total=hindimarks+englishmarks+mathmarks+sciencemarks+sanskritmarks;
    printf("%d\n",total );
    percentage=total/5;
    printf("%f\n",percentage);
    printf("percentage %.2f\n");

    return 0;

}
