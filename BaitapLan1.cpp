#include <iostream>
using namespace std;
struct Node {
	double a;
	int n;
	Node* next;
};
struct List {
	Node* firstNode ;
	Node* lastNode;
};
void List_Init(List* list) {
	list->firstNode = list->lastNode = nullptr;
}
Node* TaoNode(double a, int n) {
	Node* p = new Node;
	p->a = a;
	p->n = n;
	p->next = nullptr;
	return p;
}
void AddNode(List* l, Node* p) {
	if (l->firstNode == nullptr && l->lastNode == nullptr) {
		l->firstNode = l->lastNode = p;
	}
	else {
		l->lastNode->next = p;
		l->lastNode = p;
	}
}
void attachNode(List* l, double a, int n) {
	Node* pDT = TaoNode(a, n);
	if (pDT == NULL) return ;
	AddNode(l, pDT);
}
void nhapDT(List* l) {
	double a;
	int n;
	cout << "nhap bac cua da thuc: ";
	cin >> n;
	for (int i = n; i >= 0; i--) {
		cout << "he so cua phan tu bac " << i << " la: ";
		cin >> a;
		if (a != 0) attachNode(l, a, i);
	}
	cout << "ket thuc nhap" << endl;
}
void inDT(const List* l){
	Node* p;
	p = l->firstNode;
	while (p != NULL) {
		cout << p->a;
		if (p->n != 0) cout << "*x^" << p->n;
		if (p->next != nullptr) cout << "+";
		p = p->next;
	}
}
void freeList(List* l) {
	Node* current = l->firstNode;
	while (current != nullptr) {
		Node* temp = current;
		current = current->next;
		delete temp;
	}
	l->firstNode = l->lastNode = nullptr;
}
int main(){ 
	List DT1;
	List DT2;
	List_Init(&DT1);
	nhapDT(&DT1);
	List_Init(&DT2);
	nhapDT(&DT2);
	cout << "f(x)=";
	inDT(&DT1);
	cout << endl;
	cout << "g(x)=";
	inDT(&DT2);
	cout << endl;
	freeList(&DT1);
	freeList(&DT2);
	return 0;
}