# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        s1=''
        s2=''
        while l1!=None:
            s1+=str(l1.val)
            l1=l1.next
        while l2!=None:
            s2+=str(l2.val)
            l2=l2.next

        new=str(int(s1[::-1])+int(s2[::-1]))[::-1]
        d=ListNode()
        curr=d
        for i in new:
            curr.next=ListNode(int(i))
            curr=curr.next
        return d.next    

        
        