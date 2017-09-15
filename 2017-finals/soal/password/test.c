// no srand, canary = 103
// head fold echo cat
// 2''''''|head);cat f* #
#include<stdio.h>
#include<stdlib.h>

int __stack_canary;

void __stack_chk_fail(int argc, char *argv[]){
	fprintf(stderr, "*** stack smashing detected ***: %s terminated\n", argv[0]);
	fprintf(stderr, "Aborted (core dumped)\n");
	exit(0);
}

void cmd(){
	char command[0x6a];
	char num[23];
	setvbuf(stdout, NULL, _IONBF, 0);
	printf("Jumlah karakter: ");
	fgets(num, 23, stdin);
	strtok(num, "\n");
	snprintf(command, 0x6a, "RES=$(tr -cd '[:alnum:]' < /dev/urandom | fold -w ''''''%s''' | head -n1); echo $RES", num);
	system(command);
}

void input(int argc, char *argv[]){
	unsigned char canary = __stack_canary & 0xff;
	char name[0x11];
	puts("Welcome to secure password random generator");
	printf("nama: ");
	fgets(name, 0x111, stdin);
	if(canary != (unsigned char)(__stack_canary & 0xff)){
		__stack_chk_fail(argc, argv);
	}
}

int main(int argc, char *argv[]){
	setvbuf(stdout, NULL, _IONBF, 0);
	srand(getpid());
	__stack_canary = rand();
	input(argc, argv);
	return 0;
}
