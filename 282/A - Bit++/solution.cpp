#include<iostream>
using namespace std;
int main(){
    int x;
    cin>>x;
    int a=0;
    while(x!=0){
        string bit;
        cin>>bit;
        if(bit[1]=='+') a++;
        else if(bit[1]=='-') a--;
        x--;
    }
    cout<<a<<endl;
}