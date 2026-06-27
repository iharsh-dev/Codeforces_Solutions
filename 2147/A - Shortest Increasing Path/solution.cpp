#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    int arr[t],b=0;
    while(t--){
        int x,y;
        cin>>x>>y;
        if(x<y){
            arr[b++]=2;
        }
        if(x>y){
            if(y==1 && x>=1){
                arr[b++]=-1;
            }
            else if((x-1)==y){
                arr[b++]=-1;
            }
            else{
                arr[b++]=3;
            }
        }
        if(x==y){
            arr[b++]=-1;
        }
    }
    for(int i=0;i<b;i++){
        printf("%d
",arr[i]);
    }
}