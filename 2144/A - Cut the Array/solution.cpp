#include <vector>
#include <iostream>
 
using namespace std;
 
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int t;
    cin >> t;
 
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++)
            cin >> a[i];
 
        vector<int> pref(n + 1, 0);
        for (int i = 1; i <= n; i++)
        {
            pref[i] = (pref[i - 1] + a[i - 1]) % 3;
        }
 
        bool found = false;
        int L = 0, R = 0;
 
        for (int l = 1; l < n - 1 && !found; l++)
        {
            for (int r = l + 1; r < n && !found; r++)
            {
                int s1 = pref[l];
                int s2 = (pref[r] - pref[l] + 3) % 3;
                int s3 = (pref[n] - pref[r] + 3) % 3;
 
                if ((s1 == s2 && s2 == s3) || (s1 != s2 && s1 != s3 && s2 != s3))
                {
                    L = l;
                    R = r;
                    found = true;
                }
            }
        }
 
        if (found)
            cout << L << " " << R << "
";
        else
            cout << "0 0
";
    }
 
    return 0;
}