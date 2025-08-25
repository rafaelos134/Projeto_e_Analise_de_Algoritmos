#include <iostream>
#include <vector>

struct ListNode{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

int meioLista(ListNode* lista){
    ListNode* current1 = lista;

    int sizeList1 = 0;

    while(current1!=nullptr){ 
            sizeList1++;
            current1 = current1->next; 
    }

    return sizeList1;

}

// ListNode* mergeSort(std::vector<int> arr, int p, int r){





// }



class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* arr;
        ListNode* current1 = list1;
        ListNode* current2 = list2;
        

        

        while(current1 != nullptr){
            arr = new ListNode(current1->val);
            current1 = current1->next;
        }

        while(current2 != nullptr){
            arr = new ListNode(current1->val);
            current2 = current2->next;
        }

        ListNode* current3 = arr;
        
        while (current3 != nullptr){
            std::cout << current3->val;
        }
  
        



        // for (int i = 0; i < arr.size();i++){
        //     std::cout << arr[i] << " ";
        // }


        // ListNode* mergeSort(arr, );









        // std::cout << "\n";

        // int guarda = arr[0];


        // for (int i = 1; i < arr.size();i++){
        //     for (int j = 0; j < arr.size();j++){
        //         if (guarda < arr[j]){
        //             guarda = arr[j];
        //             // sorted.push_back(arr[i]);
        //             // break;
        //         }
                
        //     }
        //     sorted.push_back(guarda);
        // }

        // for (int i = 0; i < sorted.size();i++){
        //     std::cout << sorted[i] << " ";
        // }


        
        
        // std::cout << meioLista(list1);

        return 0;
    }
};








int main(){
    ListNode* list1 = new ListNode(5);
    list1->next = new ListNode(8);
    list1->next->next = new ListNode(8);
    list1->next->next->next = new ListNode(1);

    ListNode* list2 = new ListNode(6);
    list2->next = new ListNode(9);
    list2->next->next = new ListNode(5);
    list2->next->next->next = new ListNode(2);

    Solution sol;
    sol.mergeTwoLists(list1,list2);


    return 0;
}

