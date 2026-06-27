#include<stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    int arr[t],b=0;
    while(t!=0){
        int n,m,x,y;
        scanf("%d %d %d %d",&n,&m,&x,&y);
        int brr[n],crr[m];
        for(int i=0;i<n;i++){
            scanf("%d",&brr[i]);
        }
        for(int i=0;i<m;i++){
            scanf("%d",&crr[i]);
        }
        arr[b++]=n+m;
        t--;
    }
    for(int i=0;i<b;i++){
        printf("%d
",arr[i]);
    }    
}