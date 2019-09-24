#include <stdio.h>

#define SWAP(a, b) a ^= b ^= a ^= b

int main() {
	int a = 10, b = 20;
	
	SWAP(a, b);
	printf("%d %d", a,b );
}
