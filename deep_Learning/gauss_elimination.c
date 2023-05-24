#include<stdio.h>
#include <stdlib.h>
#include <math.h>
#define n 10
int a[n][n+1], b;

void matrix(){
    printf("Enter the value of b");
    scanf("%d",&b);
    for(int i=0; i<b; i++){
        for (int j=0; j<=b; j++)
        {
            printf("Enter the value of the augmented matrix :");
            scanf("%d", &a[i][j]);
        }
        

    }
}


void showmatrix(){
    for ( int i=0; i<b; i++){
        for (int j=0; j<=b; j++)
        {   
            printf("%d\t", a[i][j]);
        }
        printf("\n");
    }

}

void uppertriangle(){
    int k;
    for ( int i=0; i<b; i++){
        if(a[i][i]== 0.00)
        {
            printf("Error");
        }
        for (int j=0; j<=b; j++)
        {   
            if(i>j){
                float ratio = a[i][i]/a[i][j];
                // a[i][j]= a[i][j] - (a[i][j]*ratio);

                
                
            }

        }
        printf("\n");
    }
    
    
}

int main()
{
    matrix();
    showmatrix();

}