/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    let oddNumber = 0;
    let length = 0;
    const seenLetter = new Map();
    for(let i in s){
        if(!seenLetter.get(s[i])){
            seenLetter.set(s[i],1);   
        }else{
            seenLetter.set(s[i],seenLetter.get(s[i]) + 1);
        }
    }
    
    seenLetter.forEach((value,key,map)=>{
        if(value % 2 === 0){
            length += value;
        }else{
            oddNumber = 1;
            length += (value-1);
        }
    })
    
    return length+oddNumber;

};