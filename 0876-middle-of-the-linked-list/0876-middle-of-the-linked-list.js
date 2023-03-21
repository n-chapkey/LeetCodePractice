/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    let currentNode = head;
    let length = 0;
    while(currentNode){
        length +=1;
        currentNode = currentNode.next;
    }
    
    currentNode = head;
    let cntr = 0;
    console.log(Math.floor(length/2) + 1)
    while(cntr !== Math.floor(length/2)){
        currentNode = currentNode.next;
        cntr += 1;
    }
    
    return currentNode;
};