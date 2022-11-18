# You are given two non-empty linked lists representing two non-negative integers.
#  The digits are stored in reverse order, and each of their nodes contains a single digit.
#  Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# given class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return f'the value is {self.val} next is {self.next}'

# MySol starts here
def addTwoNumbers(l1,l2):
    temp_l1 = ''
    temp_l2 = ''
    while True:
        
    
        if l1.next != None:
            temp_l1+=str(l1.val)
            l1 = l1.next
        elif l2.next != None:
            temp_l2+=str(l2.val)
            l2 = l2.next
        else:
            break

    temp_l1+=str(l1.val)
    temp_l2+=str(l2.val)
    sum = int(temp_l1[::-1])+int(temp_l2[::-1])
    sum = str(sum)
    sum = sum[::-1]
    nodes = [ListNode(x) for x in sum]
    
    for i, node in enumerate(nodes[:-1]):
        node.next = nodes[i+1]
    return nodes[0]

l1_3rd =   ListNode(val=3)
l1_2nd = ListNode(val=4,next=l1_3rd)
l1 = ListNode(val=2,next=l1_2nd)  

l2_3rd =   ListNode(val=4)
l2_2nd = ListNode(val=6,next=l2_3rd)
l2 = ListNode(val=5,next=l2_2nd) 
print(addTwoNumbers(l1,l2))   
