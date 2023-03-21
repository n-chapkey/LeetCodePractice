/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head) {
    let s = head;
    let f = head;
    
    while(f && f.next){
        s = s.next;
        f = f.next.next;
        if(s === f) break;
    }
    if(!(f && f.next)) return null;
    
    let pointer = head;
    while (pointer !== f){
        pointer = pointer.next;
        f=f.next;
    }
    return pointer
};