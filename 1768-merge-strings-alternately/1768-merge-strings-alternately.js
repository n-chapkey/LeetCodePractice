/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let mergedWord = "";
    let combinedLength = word1.length + word2.length;
    for(let i=0;i<combinedLength;i++){
            if(word1[i]){
                            mergedWord = mergedWord + word1[i];
            }
            if(word2[i]){
                            mergedWord = mergedWord + word2[i];
            }




    }
    return mergedWord;
};