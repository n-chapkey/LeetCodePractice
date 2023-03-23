/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let l = 0;
    let r = 1;
    let maxProf = 0;
    
    while(r < prices.length){
        if(prices[l] < prices[r]){
            let profit = prices[r] - prices[l];
            maxProf = Math.max(profit, maxProf);
        }else{
            l = r
        }
        r +=1

    }
    
    return maxProf;
};