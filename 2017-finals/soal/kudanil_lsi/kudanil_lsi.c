// gcc -m32 kudanil_lsi.c -o kudanil_lsi -fno-stack-protector -no-pie
#include <stdio.h>
#include <stdlib.h>
int move;

int visited[11][21];
char peta[11][21] = {"h~~~~~~~~~~~~~~~~~~",
 					 "~~~~~~~~~~~~~~~~~~~" ,
 					 "~~~~~~~~~~~~~~~~~~~" ,
 					 "~~~~~~~~~~~~~~~~~~~" ,
 					 "~~~~~~~~~~~~~~~~~~~" ,
 					 "~~~~~~~~~~~~~~~~~~~" ,
 					 "~~~~~~~~~~~~~~~~~~~" ,
 					 "~~~~~~~~~~~~~~~~~~~" ,
 					 "~~~~~~~~~~~~~~~~~~~" ,
 					 "~~~~~~~~~~~~~~~~~~~" ,
 					 "~~~~~~~~~~~~/bin/so"};

int cle(){
	int i, j;;
	for (i = 0; i < 11; ++i)
	{
		for(j = 0; j < 21 ; j++){
			if(peta[i][j] == '*') peta[i][j] = '~';
			visited[i][j] = 0;
		
		}
	
	}

	}

int x = 0;
int y = 0;

int xtemp = 0;
int ytemp = 0;
void loading(){
	int i;
	for (i = 0; i < 3; ++i)
	{
		printf(".");
		sleep(1);
	}
	printf("\n");
}

void clear(){
	system("clear");
}

void play(){
	int temp=0;
	printf("\nControl\n");
	printf("(w) keatas\n");
	printf("(a) kekiri\n");
	printf("(s) kebawah\n");
	printf("(d) kekanan\n");
	printf("(c) bersihkan layar\n\n");
	printf("\n\n~~Map Danau Misterius LSI~~\n\n");
	printf("\n\nKamu hanya mempunyai %d langkah\n\n", move);
	while(1){ 
		if(temp!=0)  
			printf("\n\nSisa langkah kamu  : %d langkah\n", move);
		temp=1;
		screen();
		if(move<=0){
			printf("Langkah mu habis\n");
			exit(0);
		}
		gerak();
		move--;
		peta[ytemp][xtemp] = '~';
		xtemp = x;
		ytemp = y;
		peta[y][x] = 'h';

	}
}

int gerak(){
	
	char input[10];
	char c;
	if(!strcmp("/bin/sh", peta[10]+12)){
		gets(input);
	} else{
		fgets(input, 3, stdin);		
	}
	c = input[0];
	if(c == 'w' && y-1 >= 0){
		y = y - 1;
	}
	else if(c == 'a'&& x - 1 >= 0){
		x = x - 1;
	}
	else if(c ==  's'  && y +1 <= 10){
		y = y + 1;
	}
	else if(c == 'd' && x +1 <= 18){
		x = x + 1;
	}
	else if(c == 'c'){
		clear();
	}
	if(peta[y][x] == '*'){
		printf("Anda bertemu buaya putih\n");
		printf("W A S T E D\n");
		exit(0);
	}

}

void screen(){
	int i;
	for(i = 0; i < 12 ; i++){
		printf("%s\n", peta[i]);	
	}
}

int randomize(int buaya){
	
	int summon = 0;
	while(summon < buaya){
		int fieldx = ((rand() % (21)));		
		int fieldy = ((rand() % (21)));		
		if(peta[fieldy][fieldx] == '~'){
			summon ++;
			peta[fieldy][fieldx] = '*';
		}	
	}
	
}


int antrix[256];
int antriy[256];
int jarak[256];
int size=0;

int push(int x, int y, int jar){
	antrix[size] = x;
	antriy[size] = y;
	jarak[size] = jar;
	size ++;
}

int pop(){
	int i;
	for(i=0; i<size; i++){
		antrix[i] = antrix[i+1];
		antriy[i] = antriy[i+1];
		jarak[i] = jarak[i+1];
	}
	jarak[size] = 0;
	antriy[size] = 0;
	antrix[size] = 0;
	size--;
}


int frontx(){
	return antrix[0];	
}

int fronty(){
	return antriy[0];
}

int jaraks(){
	return jarak[0];
}


int solver(){
	push(0, 0, 0);	
	int m, n, a, b, distance;
	int new = 1;
	
	m = 9;
	n = 18;
	while(size){
		
		a = frontx();
		b = fronty();
		distance = jaraks();
		pop();
		if(visited[a][b] == 1 || peta[a][b] != '~' && peta[a][b] != 'h' && peta[a][b] != 'o') continue;

		visited[a][b] = 1;
		
		if (a==m && b==n)
	       {
	       		return distance+1;
	           break;
	       }
	   	push(a+1, b, distance + 1);
		push(a, b+1, distance + 1);
		push(a-1, b, distance + 1);
		push(a, b-1, distance + 1);
	}
	
	
}


int main()
{
	srand(getpid());
	peta[0][0] = 'h';
	char temp[2];
	setvbuf(stdout, NULL, _IONBF, 0);
	printf("Dramaga Game Studios Present\n");
	randomize(60);
	move = solver();
	while(!move){
		cle();
		randomize(60);
		move = solver();
	}
	loading();	
	printf("\n\nKudanil LSI Adventure\n");
	printf("Cari dan berpetualang. Cari kudanil yang terdapat di danau LSI\n");
	printf("Press Any Key to Start Game\n");
	char c;
	while((c= getchar()) != '\n' && c != EOF);
	play();
	return 0;
}