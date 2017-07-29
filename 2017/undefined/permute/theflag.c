//ide: kalo dilihat pake hex editor, seperti kelihatan flagnya, tapi bukan itu
#include <stdio.h>
#include <string.h>
#include "permute.h"

const char *msgs[] = {"Wrong Flag", "Correct Flag"};

int main(int argc, char *argv[])
{
	int i, all, len, stlen;
	if (argc<2) {
		printf("usage: theflag <flag>\n");
		return 0;
	}
	const char *input = argv[1];
	all = 0;
	for (len=0; permute[len]!=-1; len++) {
	}	
	stlen = strlen(input);
	all |= (int)len!=stlen;

	for (i=0; i < stlen; i++) {
		all |=( input[i] ^ trick_str[permute[i]]);
	}
	puts(msgs[(int)(all==0)]);

	return 0;		
}
