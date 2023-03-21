/**
 * @param {number[]} nums
 * @return {number}
 */
var zeroFilledSubarray = function(nums) {
    
    let subArraySize = 0;
    let occurs = 0;
    for(let i=0;i<nums.length;i++){
        if(nums[i] === 0 && i !== nums.length-1){
            subArraySize += 1;
        }else if(nums[i] === 0){
            subArraySize += 1;
            occurs += (subArraySize*(subArraySize+1))/2
        }else{
            occurs += (subArraySize*(subArraySize+1))/2
            subArraySize = 0;
        }
    }
    return occurs;
};