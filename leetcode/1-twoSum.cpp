#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size();i++){
            for (int j = 0; j < nums.size();j++){
                if ((nums[i]+nums[j]) == target){
                    return {i, j};}
            }
        }
        return {};
    }
    
};

int main(){
    Solution teste;

    vector<int> meusNum = {3,5,6,2,7,4};
    int alvo = 5;


    vector<int> res = teste.twoSum(meusNum,alvo);
    
    if (!res.empty()){
        cout << res[0];
        cout << res[1];
    }
    

}