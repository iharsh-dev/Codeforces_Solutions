#include <vector>
#include<stdio.h>
#include<iostream>
using namespace std;
using ll = long long;
 
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        ll m;
        cin >> n >> m;
        vector< pair<ll, int> > req(n);
        for (int i = 0; i < n; i++)
            cin >> req[i].first >> req[i].second;
 
        ll points = 0;
        ll prevTime = 0;
        int prevSide = 0;
        bool possible = true;
 
        for (int i = 0; i < n; i++)
        {
            ll a = req[i].first;
            int b = req[i].second;
            ll gap = a - prevTime; // number of minutes before next requirement
            int neededParity = prevSide ^ b;
 
            if (gap % 2 != neededParity)
            {
                // we must run an odd/even number of times — but not possible
                if (gap == 0)
                {
                    possible = false;
                    break;
                }
                // we must "sacrifice" one run to fix parity
                points += gap - 1;
            }
            else
            {
                points += gap;
            }
 
            prevTime = a;
            prevSide = b;
        }
 
        // last segment (no requirement at m)
        points += (m - prevTime);
 
        if (!possible)
            cout << -1 << "
";
        else
            cout << points << "
";
    }
}