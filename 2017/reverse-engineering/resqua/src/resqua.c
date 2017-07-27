#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/mman.h>

#include <elf.h> 

#define DEFAULT_EP ((unsigned char*)0x400000)

void unlock()
{

  int   p   = *((int *)(DEFAULT_EP + 0x09));
  int   len = *((short *)(DEFAULT_EP + 0xd));
  
  int   keylen = 3;
  char  *key = (char *)(DEFAULT_EP + 1); // string:"ELF" (for 64 bit binary)

  /* Change Permissions */
  unsigned char *ptr       = DEFAULT_EP + p;
  unsigned char *ptr1      = DEFAULT_EP + p + len;
  size_t         pagesize  = sysconf (_SC_PAGESIZE);
  uintptr_t      pagestart = (uintptr_t)ptr & -pagesize;
  int            psize     = (ptr1 - (unsigned char*)pagestart);

  /* Make the pages writable...*/
  mprotect((void*)pagestart, psize, PROT_READ | PROT_WRITE | PROT_EXEC);

  int i;
  for (i = 0; i < len; ptr[i] ^= key[i % keylen], i++);

  mprotect((void*)pagestart, psize, PROT_READ | PROT_EXEC);
}

// check if perfect square >= 1111
__attribute__((section(".lock")))
int c(int n)
{
  if (n < 1111) return 0;
  int i = 1;
  while (n > 0) {
    n -= i;
    i += 2;
  }
  return n == 0;	
}

__attribute__((section(".lock")))
void run()
{	
	printf("Enter a valid serial number: ");
	char serial[20];
	gets(serial);
	
	if (! (strlen(serial) == 19 && serial[4] == '-' && serial[9] == '-' && serial[14] == '-')) 
	{
		puts("\x1b[31mWrong format!\x1b[0m");
	} else {
		int i;
		for (i = 0; i < 20; i++) {
			if (serial[i] == '0') {
				puts("\x1b[31mInvalid serial number!\x1b[0m");
				exit(1);
			}
		}

		char spart1[5];
		char spart2[5];
		char spart3[5];
		char spart4[5];
		strncpy(spart1, serial, 4);
		spart1[4] = 0;
		strncpy(spart2, serial+5, 4);
		spart2[4] = 0;
		strncpy(spart3, serial+10, 4);
		spart3[4] = 0;
		strncpy(spart4, serial+15, 4);
		spart4[4] = 0;
		
		int part1, part2, part3, part4;
		part1 = atoi(spart1);
		part2 = atoi(spart2);
		part3 = atoi(spart3);
		part4 = atoi(spart4);

		if (c(part1) && c(part2) && c(part3) && c(part4) && (part1 < part2 && part2 < part3 && part3 < part4)) {
			puts("\x1b[32mCongrats, valid serial number!\x1b[0m");
		} else {
			puts("\x1b[31mInvalid serial number!\x1b[0m");
		}
	}
	
}

int main(int argc, char **argv)
{
	unlock();
	run();
	
	return 0;
}

