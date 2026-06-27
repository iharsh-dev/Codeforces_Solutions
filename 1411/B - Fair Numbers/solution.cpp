#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int t;
    cin >> t;
 
    vector<long long> ans;
 
    for(int i = 0; i < t; i++) {
        long long n;
        cin >> n;
 
        while(true) {
            long long temp = n;
            bool check = true;
 
            while(temp > 0) {
                int dig = temp % 10;
                temp /= 10;
 
                if(dig != 0 && n % dig != 0) {
                    check = false;
                    break;
                }
            }
 
            if(check) {
                ans.push_back(n);
                break;
            } else {
                n++;
            }
        }
    }
 
    for(int i = 0; i < ans.size(); i++) {
        cout << ans[i] << '
';
    }
 
    return 0;
}