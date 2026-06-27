#include<stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    int arr[t],b=0;
    while(t!=0){
        int x,n;
        scanf("%d %d",&x,&n);
        if(n%2==0){
            arr[b++]=0;
        }
        else{
            arr[b++]=x;
        }
        t--;
    }
    for(int i=0;i<b;i++){
        printf("%d
",arr[i]);
    }
}