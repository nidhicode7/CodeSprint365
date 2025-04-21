#include <iostream>
using namespace std;

class Solution {
public:
    bool hasDuplicate(int nums[], int size) {
        for (int i = 0; i < size; i++) {
            for (int j = i + 1; j < size; j++) {
                if (nums[i] == nums[j])
                    return true;
            }
        }
        return false;
    }
};

