#include <iostream>


struct ListNode{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next): val(x),next(next){} 
};


// enviar da q


void printList(ListNode* head) {
    while (head != nullptr) {
        std::cout << head->val;
        if (head->next != nullptr) std::cout << " -> ";
        head = head->next;
    }
    std::cout << std::endl;
}

class Solution {

    public:
        ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

            ListNode* dummyHead = new ListNode();
            ListNode* current = dummyHead;
            int carry = 0;



            while(l1 != nullptr || l2 != nullptr || carry !=0){
                int x = 0;
                int y = 0;

                if (l1 != nullptr){
                    x = l1->val;
                }

                if (l2 != nullptr){
                    y = l2->val;
                }


                int sum = x + y + carry;
                carry = sum/10;


                current->next = new ListNode(sum%10);
                current = current->next;

                if (l1 != nullptr){
                    l1 = l1->next;
                }
            
                if (l2 != nullptr){
                    l2 = l2->next;
                }
            }
            return dummyHead->next;
        }
};


int main(){
    
    Solution soluition;

    ListNode* l1 = new ListNode(2,new ListNode(4, new ListNode(3)));;
    ListNode* l2 = new ListNode(5,new ListNode(6, new ListNode(4)));;


    ListNode* result =  soluition.addTwoNumbers(l1,l2);

    
    printList(result);



    return 0;
}
