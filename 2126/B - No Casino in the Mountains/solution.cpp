#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int main()
{
    int x;
    cin >> x;
    int brr[x];
    int t = 0;
    while (x != 0)
    {
        int n, k;
        cin >> n >> k;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        int m = 0;
        int i = 0;
        while (i < n && i + k <= n)
        {
            int check = 0;
            for (int j = i; j < min(i + k, n); j++)
            {
                if (arr[j] == 1)
                {
                    check = 1;
                    break;
                }
            }
            if (check != 1)
            {
                m++;
                i = i + k + 1;
            }
            else
                i++;
        }
        brr[t++] = m;
        x--;
    }
    for (int i = 0; i < t; i++)
    {
        printf("%d
", brr[i]);
    }
}