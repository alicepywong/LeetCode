# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # count the length
        listNode = head
        cnt = 0
        while(listNode is not None):
            cnt = cnt + 1
            listNode = listNode.next

        mid = cnt // 2 + 1

        listNode = head
        for i in range(0, cnt):
            if i + 1 == mid:
                break
            listNode = listNode.next

        return listNode
