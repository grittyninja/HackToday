// gcc rennai.c -o rennai -masm=intel

#include<stdio.h>
#include<stdlib.h>
#include <sys/ptrace.h>
#include <stdint.h>

int _init_ = 0;
int __cne__ = 0;
long long int __cle__ = 0;

void _sleep_(int i){
  return 1;
}

void mySleep(long long int sl){
	puts("Untuk mendapatkan flag kamu harus menunggu selama 313373133731337 detik");
  long long int counter = sl;
  counter = (sl/counter) + 9;
  for(counter; counter>0; counter--){
        _printf("%lld detik lagi.\n", sl);
        _sleep_(1);
  }

  __asm__("mov rax, 5\n\t");
  __asm__("call $+5\n\t");
  __asm__("add [rsp], rax\n\t");
  __asm__("ret\n\t");

  if(sl % 1337 != 1261){
    cheat();
  }
  for(sl; sl>0; sl--){
    		printf("%lld detik lagi.\n", sl);
    		sleep(1);
        __cne__ = sl;
        if(sl % 31337 == 0){
          __cle__ += 3;
        }
  }
  __cle__ = 20000888130 ^ __cle__;
	_init_ = 1;
}

int _printf(char* s, int n){
	return 0;
}

int printFlag(){
	int myflag[110] = {68, 67, 68, 45, 79, 88, 70, 76, 67, 45, 75, 65, 76, 74, 33, 45, 78, 88, 64, 76, 45, 89, 68, 93, 88, 76, 67, 45, 73, 66, 76, 67, 74, 45, 88, 67, 89, 88, 70, 45, 93, 72, 94, 72, 95, 89, 76, 45, 84, 76, 67, 74, 45, 89, 68, 73, 76, 70, 45, 64, 72, 67, 74, 72, 95, 71, 76, 70, 76, 67, 45, 94, 72, 94, 88, 76, 68, 45, 73, 72, 67, 74, 76, 67, 45, 72, 70, 94, 93, 72, 70, 89, 76, 94, 68, 45, 93, 95, 66, 79, 65, 72, 64, 45, 94, 72, 89, 89, 72, 95};
	int count;
  printf("HackToday{");
	for(count=0;count<110;count++){
		_printf("%c", myflag[count]^13);
	}
	return 0;
}

void _exit_(int x){
__asm__("mov rax, 5\n\t");
__asm__("call $+5\n\t");
__asm__("add [rsp], rax\n\t");
__asm__("ret\n\t");
long long int result = 313373133731337 & __cle__;

if(result != 9999311361){
  cheat();
}

long long int key = __cle__ ^ 1409376768;

long long int n[28] = {8590723269, 8590723278, 8590723285, 8590723273, 8590723326, 8590723285, 8590723273, 8590723268, 8590723268, 8590723326, 8590723266, 8590723278, 8590723268, 8590723280, 8590723284, 8590723264, 8590723277, 8590723326, 8590723283, 8590723268, 8590723279, 8590723279, 8590723264, 8590723272, 8590723326, 8590723267, 8590723283, 8590723278};
int i;

if(__cne__ != 1){
  cheat();
}
for(i=0; i<28; i++){
	printf("%c", n[i]^key);
}
}

void cheat(){
  __asm__("mov rax, 5\n\t");
  __asm__("call $+5\n\t");
  __asm__("add [rsp], rax\n\t");
  __asm__("ret\n\t");

  putchar(10);
	puts("[anti reverse engineering reverse engineering club]");
	puts("curang itu boleh tapi gak boleh ketahuan!");
	exit(0);
}


int main(){
  if (ptrace (PTRACE_TRACEME, 0, 1, 0) == -1){
    cheat();
  }
  mySleep(313373133731337);
  printFlag();
  __asm__("mov rax, 5\n\t");
  __asm__("call $+5\n\t");
  __asm__("add [rsp], rax\n\t");
  __asm__("ret\n\t");
  if(_init_ != 1){
	   cheat();
   }
   _exit_(0);
   putchar(125);
   printf("\n");
   return 0;
}
