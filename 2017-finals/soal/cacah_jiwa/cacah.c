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

void input()
{
	struct nodes *node1, *node2;
	int umur;

	node1 = malloc(sizeof(struct nodes));
	node2 = malloc(sizeof(struct nodes));

	node1->nama = malloc(20);
	node2->nama = malloc(20);

	printf("namanya : ");
	read(0, node1->nama, 200);
	printf("Umurnya : ");
	scanf("%d", &node1->umur);

	printf("namanya : ");
	read(0, node2->nama, 200);
	printf("Umurnya : ");
	scanf("%d", &node2->umur);

	printf("Terima kasih mz\n");
}

void welcome()
{
	printf("Cacah Jiwa Online 31337\n");
}

int main()
{
	int pilihan;

	init();
	welcome();
	while (1)
	{
		input();
	}

	return 0;
}