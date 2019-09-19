#include <stdio.h>

int strlen(char str[]);
int strcpy(char dst[], char src[]);
int strcmp(char str1[], char str2[]);

int main() {
	char a[] = "1234567890";
	char b[5];
	strcpy(b, a);
	printf("%s", b);


	return 0;
}

int strlen(char str[]) {
	int len = 0;
	while (str[len++]) { ; }
	return len;
}

int strcpy(char dst[], char src[]) {	// sizeof(dst) 코드 수정
	int i = 0;
	printf("%d\n", sizeof(dst));	// always 4
	while (src[i]) {
		*(dst + i) = *(src + i);
		printf("%d[%c] ", i, src[i]);
		i++;
	}
	dst[i] = 0;
	return 0;
}

int strcmp(char str1[], char str2[]) {	// issame
	if (strlen(str1) != strlen(str2)) return 0;
	int i = 0;
	while (str1[i] && str1[i] == str2[i]) {
		i++;
	}
	if (str1[i]) return 0;
	else return 1;
}

