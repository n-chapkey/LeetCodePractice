/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let runSum = []
    for(let i=0;i<nums.length;i++){
        if(i===0){
            runSum[0] = nums[0]
        }else{
            runSum[i] = nums[i] + runSum[i-1];
        }
    }
    return runSum;
};