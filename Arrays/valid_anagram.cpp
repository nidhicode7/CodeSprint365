#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        int m = s.length(), n = t.length();
        if (m != n)
            return false;

       //here what we are doing is we are we are sorting the strings in ascending order like for example we have if **s=listen**,then after sort(s.begin(),s.end() it will bocome **s=eilnst** so we are using for that purpose
        sort(s.begin(), s.end());//here we are converting strings to character arrays
        sort(t.begin(), t.end());

        return s == t;
    }
};
