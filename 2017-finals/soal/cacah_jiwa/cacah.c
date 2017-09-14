// gcc -g -m32 -fno-stack-protector -mpreferred-stack-boundary=4 cacah.c -o cacah
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <dirent.h>


char *cmd = "/bin/sh";

struct nodes
{
	char *nama;
	int umur;
};

void init()
{
	setvbuf(stdout, NULL, _IONBF, 0);
}

void libc_main()
{
	system(cmd);
}


void welcome()
{
	printf("Cacah Jiwa Online 31337\n");
}

int main(int argc, char * argv[])
{
	init();
	welcome();
	
	struct nodes *node1, *node2, *node3;

	int umur;

	while(1)
	{
		node1 = malloc(sizeof(struct nodes));
		node1->nama = malloc(8);
		node1->umur = 1;

		node2 = malloc(sizeof(struct nodes));
		node2->nama = malloc(8);
		node1->umur = 2;

		printf("Nama suami : ");
		gets(node1->nama);

		printf("Nama istri : ");
		gets(node2->nama);

		fflush(stdin);
	}

	return 0;
}