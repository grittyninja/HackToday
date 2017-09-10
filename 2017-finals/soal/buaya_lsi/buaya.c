// gcc -static -m32 -s -fno-stack-protector buaya.c -o buaya
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void menu()
{
	char c;
	FILE * fptr;
	fptr = fopen("buaya.gambar", "r");
	c = fgetc(fptr);
    while (c != EOF)
    {
        printf ("%c", c);
        c = fgetc(fptr);
    }
}

void buaya()
{
	char buf[512];

	printf("Apa nama buaya kaporit kamu?\n");
	gets(buf);
	printf("%s\n", buf);
}

void init()
{
	setvbuf(stdout, NULL, _IONBF, 0);
}

int main(int argc, char* argv[])
{
	init();
	menu();
	buaya();
	return 0;
}