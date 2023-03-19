/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let j = 0;
    
    if(s.length < 1) return true;
    
    for(let i in t){
        if(s[j] === t[i]){
            j = j + 1;
        }
    }
    return s.length === j;
};