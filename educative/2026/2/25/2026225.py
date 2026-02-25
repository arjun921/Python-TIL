# https://www.educative.io/interview-prep/coding/remove-nth-node-from-end-of-list
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_last_node(head, n):
    if not head:
        return head
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1
    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next


""" Problem 2 """

# https://www.educative.io/interview-prep/coding/solution-remove-duplicates-from-sorted-array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1930229177/


def removeDuplicates(nums):
    l = 0

    for r in range(1, len(nums)):
        if nums[r] != nums[l]:
            l += 1
            nums[l] = nums[r]

    # Replace this placeholder return statement with your code
    return l + 1


def main():
    test_cases = [
        [1, 1, 2, 2, 3],
        [-1, -1, 0, 0, 1, 1, 2],
        [5, 5, 5, 5],
        [1, 2, 3, 4],
        [0],
    ]

    for idx, nums in enumerate(test_cases):
        print(idx + 1, ".\tnums:", nums, sep="")
        arr = nums.copy()  # because function modifies in-place

        k = removeDuplicates(arr)

        print("\n\tUnique Count (k):", k)
        print("\tArray After Removing Duplicates:", arr[:k])
        print("-" * 100)
