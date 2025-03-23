#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> num_map;
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (num_map.find(complement) != num_map.end()) {
            return {num_map[complement], i};  // Return indices
        }
        num_map[nums[i]] = i;  // Store index of current number
    }
    return {};  // No solution found
}

int main() {
    int n, target;
    
    
    cout << "Enter number of elements: ";
    cin >> n;
    
    vector<int> nums(n);
    

    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    

    cout << "Enter target: ";
    cin >> target;
    
    vector<int> result = twoSum(nums, target);
    
    if (result.size() == 2) {
        cout << "Indices: " << result[0] << ", " << result[1] << endl;
    } else {
        cout << "No solution found." << endl;
    }
    
    return 0;
}
