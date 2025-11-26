# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp=l1
        tmp2=l2
        li1=''
        li2=''
        while tmp!=None or tmp2!=None:
            if tmp!=None and tmp2!=None:
                li1+=str(tmp.val)
                tmp=tmp.next
                li2+=str(tmp2.val)
                tmp2=tmp2.next
            elif tmp==None and tmp2!=None:
                li1+='0'
                li2+=str(tmp2.val)
                tmp2=tmp2.next
            elif tmp!=None and tmp2==None:
                li1+=str(tmp.val)
                tmp=tmp.next
                li2+='0'
            else:
                tmp=tmp.next
                tmp2=tmp2.next
            
        # print(li1[-1::-1], li2[-1::-1])
        output=list(map(int, str(int(li1[-1::-1])+int(li2[-1::-1]))))
        answer=ListNode(output[-1])
        tmp3=answer
        for z in range(len(output)-2,-1,-1):
            tmp3.next=ListNode(output[z])
            tmp3=tmp3.next
        return answer