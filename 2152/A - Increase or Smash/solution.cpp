#include <iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main()
{
    int t;
    cin>>t;
    vector<int> v;
    while(t--){
        int size;
        cin>>size;
        vector<int> m(size,0);
        int opp=0;
        for(int i=0;i<size;i++){
            cin>>m[i];
        }
        sort(m.begin(),m.end(),greater<int>());
        int j=0;
        while(j<size && j+1<size){
            int can=m[j]-m[j+1];
            if(can!=0){
                opp+=2;
            }
            j++;
        }
        if(size==1) opp=1;
        else if(m[size-1]!=m[size-2]) opp++;
        else opp++;
        v.push_back(opp);
    }
    for(int i=0;i<v.size();i++){
        cout<<v[i]<<endl;
    }
    return 0;
}