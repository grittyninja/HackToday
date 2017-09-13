// gcc -m32 -mpreferred-stack-boundary=4 cacah.c -o cacah
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

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
	system("/ben/ul");
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
	int pilihan;
	int umur;

	while(1)
	{
		node1 = malloc(sizeof(struct nodes));
		node1->nama = malloc(8);

		node2 = malloc(sizeof(struct nodes));
		node2->nama = malloc(8);

		printf("Nama suami : ");
		read(0, node1->nama, 100);
		printf("Umur suami : ");
		scanf("%d", &node1->umur);
		printf("Nama istri : ");
		read(0, node2->nama, 100);
		printf("Umur istri : ");	
		scanf("%d", &node1->umur);

		printf("Terima kasih ya mz\n");
	}

	return 0;
}