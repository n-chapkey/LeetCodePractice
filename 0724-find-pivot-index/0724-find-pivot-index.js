/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let sum =0;
    for(let i=0;i<nums.length;i++){
        sum += nums[i];
    }

    let runningSum = 0;
    for(let i=0;i<nums.length;i++){

        if(sum-(runningSum*2)-nums[i] === 0){
            return i;
        }else{
            runningSum += nums[i];
        }
    }

    return -1;
};