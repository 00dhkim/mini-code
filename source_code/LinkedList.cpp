#include <stdio.h>
#include <stdlib.h>

typedef struct _node {
	int data;
	struct _node * next;
}Node;

Node* head = NULL;
Node* tail = NULL;
Node* cur = NULL;

void makeNode() {
	Node* newNode = NULL;
	int Data;
	while (1) {
		scanf("%d", &Data);
		if (Data < 0) break;

		newNode = (Node*)malloc(sizeof(Node));
		newNode->next = NULL;
		newNode->data = Data;

		if (head == NULL)
			head = newNode;
		else
			tail->next = newNode;

		tail = newNode;
	}
	printf("make node finish\n");
}

void deleteNode(int Data) {
	Node* tmp = NULL;
	cur = head;
	while (1) {
		if (cur->next->data == Data) {
			tmp = cur->next->next;
			free(cur->next);
			cur->next = tmp;
			break;
		}
		else {
			cur = cur->next;
		}
	}
	printf("delete node finish\n");
}

void insertNode(int prev_val, int Data) {
	Node* tmp = NULL;
	cur = head;
	while (1) {
		if (cur == NULL) {
			printf("Not exist %d\n", prev_val);
			return;
		}
		else if (cur->data == prev_val) {
			tmp = cur->next;
			Node* newNode = (Node*)malloc(sizeof(Node*));
			newNode->data = Data;
			cur->next = newNode;
			newNode->next = tmp;
			break;
		}
		else {
			cur = cur->next;
		}
	}
	printf("insert node finish\n");

}

void deleteHead() {
	cur = head;
	head = cur->next;
	free(cur);
	printf("delete head node finish\n");
}

void deleteTail() {
	cur = head;
	while (1) {
		if (cur->next == tail) {
			tail = cur;
			cur->next = NULL;
			free(cur->next);
			break;
		}
		else {
			cur = cur->next;
		}
	}
	printf("delete tail node finish\n");
}

void printNode() {
	cur = head;
	while (cur != NULL) {
		printf("%d ", cur->data);
		cur = cur->next;
	}
}

int main() {

	makeNode();
	
	deleteNode(4);

	insertNode(3, 999);

	deleteHead();
	
	deleteTail();

	printNode();

	return 0;
}
