/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> nextLargerNodes(ListNode* head) {
        int n=1,i=0;
        ListNode *temp= head;
        while(temp->next!=nullptr){
            n++;temp=temp->next;
        }
        vector<int> a(n,0);
        temp=head;
        while(temp->next!=nullptr){
            ListNode *great = temp->next;
            while(great->val <= temp->val && great->next!=nullptr){
                great=great->next;

            }
            if (temp->val < great->val){
                a[i]=great->val;
            }
            i++;
            temp=temp->next;
            
        }
        return a;
    }
};