#include<iostream>
#include<vector>
#include<stdio.h>
using namespace std;
 
int main(){
	int t;
	cin>>t;
	vector<int> v;
	while(t--){
		int pizza;
		cin>>pizza;
		int count=0;
		while(pizza>2){
			count=count+1;
			pizza=pizza-2;
		}
		v.push_back(count);
	}
	for(int i=0;i<v.size();i++){
		cout<<v[i]<<endl;
	}
}