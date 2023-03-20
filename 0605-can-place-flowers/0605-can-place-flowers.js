/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    let flowersLeft = n;
    
    if(flowerbed.length===1 && flowerbed[0] === 0){
       return true;
    }
    
    for(let i =0;i<flowerbed.length;i++){
        console.log(flowersLeft)
        if(flowersLeft === 0) break;
        if(i === 0 && flowerbed[i] === 0 && flowerbed[i+1] === 0){
            console.log("first if")
             flowersLeft = flowersLeft-1
            i= i + 1;
        }else if(i === flowerbed.length-1 && flowerbed[i] === 0 && flowerbed[i-1] === 0){
            console.log("second if")
            flowersLeft = flowersLeft-1
        }else{
            console.log("third if")
            console.log(flowerbed[i-1],flowerbed[i],flowerbed[i+1])
            if(flowerbed[i-1] === 0 && flowerbed[i] === 0 && flowerbed[i+1] === 0){
                console.log("fourth if")
                flowersLeft = flowersLeft-1;
                i = i + 1;
            }
        }
        

    }
    
    return flowersLeft === 0
};