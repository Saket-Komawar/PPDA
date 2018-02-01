#include <stdio.h>
#include <string.h>

void swap(char *x, char *y);
void permutate(char *str, int l, int r);

int main(){
	int len;
	char str[16];
	scanf("%s", str);
	len = strlen(str);
	permutate(str, 0, len - 1);
	return 0;
}

void swap(char *x, char *y){
	char tmp;
	tmp = *x;
	*x = *y;
	*y = tmp;
}

void permutate(char *str, int l, int r){
	int i;
	if(l == r)
		printf("%s\n", str);
	else{
		for(i = l; i <= r; i++){
			swap(str + l, str + i);
			permutate(str, l + 1, r);
			swap(str + l, str + i);
		}
	}
}