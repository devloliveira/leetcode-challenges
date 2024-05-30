/**
 * Definition for singly-linked list.
 */

#include <iostream>
#include <malloc.h>


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


int
get_total_elements(ListNode *head) {
    int size = 0;
    ListNode *iter = head;
    while (iter != nullptr) {
        size++;
        iter = iter->next;
    }

    return size;
}


ListNode*
get_node_from_index(ListNode *head, int position) {
    int index = 0;
    ListNode *iter = head;
    while (index < position) {
        iter = iter->next;
        index++;
    }

    return iter;
}


void
print_indexes(ListNode *head) {
    int index = 0;
    ListNode *iter = head;

    std::cout << "Head addr: " << head << "\n";

    while (iter != nullptr) {
        std::cout << "(" << index << ")" << iter->val << "\n";
        iter = iter->next;
        index++;
    }
}


class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        int head_index = k-1;
        int tail_index = get_total_elements(head) - k;

        ListNode *head_k = get_node_from_index(head, head_index);
        ListNode *tail_k = get_node_from_index(head, tail_index);

        int old_head_val = head_k->val;
        head_k->val = tail_k->val;
        tail_k->val = old_head_val;

        return head;
    }
};


ListNode *
setup_nodes() {
    ListNode *head = (ListNode*) malloc(sizeof(ListNode));
    ListNode *first_node = (ListNode*) malloc(sizeof(ListNode));
    ListNode *second_node = (ListNode*) malloc(sizeof(ListNode));
    ListNode *third_node = (ListNode*) malloc(sizeof(ListNode));

    (*head) = ListNode(0);
    (*first_node) = ListNode(1);
    (*second_node) = ListNode(2);
    (*third_node) = ListNode(3);

    head->next = first_node;
    first_node->next = second_node;
    second_node->next = third_node;

    return head;
}


int
main(int argc, char* argv[]) {
    ListNode *head = setup_nodes();

    print_indexes(head);

    Solution solution = Solution();
    solution.swapNodes(head, 1);

    std::cout << head << "\n";
    std::cout << head->val << "\n";
    std::cout << head->next->val << "\n";
    std::cout << head->next->next->val << "\n";
    std::cout << head->next->next->next->val << "\n";

    print_indexes(head);
}