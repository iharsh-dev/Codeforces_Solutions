#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
    int t;
    cin>>t;
    int brr[t],b=0;
    while(t--){
        int size;
        cin>>size;
        int arr[size];
        for(int i=0;i<size;i++){
            cin>>arr[i];
        }
        vector<int> v;
        int target=arr[0],f=0;
        for(int i=0;i<size;i++){
            if(arr[i]==target){
                f++;
            }
            else{
                v.push_back(f);
                target=arr[i];
                f=1;
            }
        }
        v.push_back(f);
        sort(v.begin(),v.end(),greater<int>());
        int maxl=0;
        for(int i=0;i<v.size();i++){
            if(v[i]*(i+1)>maxl){
                maxl=v[i]*(i+1);
            }
        }
        brr[b++]=maxl;
    }
    for(int i=0;i<b;i++){
        cout<<brr[i]<<endl;
    }
}