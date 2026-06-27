#include <stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int brr[t];
    int b=0;
    while(t--){
        int size;
        cin>>size;
        int arr[size];
        for(int i=0;i<size;i++){
            cin>>arr[i];
        }
        int max=arr[0];
        for(int i=0;i<size;i++){
            if(max<arr[i]){
                max=arr[i];
            }
        }
        brr[b++]=max;
    }
    for(int i=0;i<b;i++){
        cout<<brr[i]<<endl;
    }
    return 0;
}