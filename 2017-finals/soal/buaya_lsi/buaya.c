// gcc -static -fno-stack-protector -s buaya.c -o buaya
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void welcome()
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

    printf("Selamat datang di Penangkaran Buaya LSI\n");
    printf("Tugas kamu adalah mengalokasikan m buaya dalam lahan penangkaran berukuran m meter persegi supaya tidak saling ketemu satu sama lain\n");
    printf("Contoh 4 meter persegi lokasi penangkaran, maka kamu harus mengalokasi 4 buaya seperti berikut : \n");
    printf("\t. b . .\n");
    printf("\t. . . b\n");
    printf("\tb . . .\n");
    printf("\t. . b .\n");
    printf("Kamu cukup memasukkan koordinatnya seperti berikut.\n");
    printf("0 1\n");
    printf("1 3\n");
    printf("2 0\n");
    printf("3 2\n");
    printf("Ayo selesaikan 5 alokasi penangkarannya. Kamu akan dapat hadiah jika berhasil.\n\n");
   
}

void n_buaya()
{
	int i, j, k, l, x;
	int row, col;
	int salah;
	
	srand(getpid());
	
	for(x = 0; x < 5; x ++)
	{
		int size = 5 + rand() % 10;
		int jumlah_buaya = 0;	

		char lokasi_buaya[size][size];

		printf("%d.) Ukuran penangkaran buaya adalah %d meter persegi\n", x + 1,size);

		//init matrix
		for(i = 0; i < size; i ++)
			for(j = 0; j < size; j ++)
				lokasi_buaya[i][j] = '.';

		for(i = 0; i < size; i++)
		{
			scanf("%d", &row);
			scanf("%d", &col);
			lokasi_buaya[row][col] = 'b';
		}

		// print inputan matrix
		printf("Coba aku cek dulu\n");
	
		sleep(2);

		for(i = 0; i < size; i++)
			for(j = 0; j < size; j++)
			{
				salah = 0;
				if (lokasi_buaya[i][j] == 'b')
				{
					//cek ke bawah
					for(k = i + 1; k < size; k++)
						if(lokasi_buaya[k][j] == 'b')
	 						salah = 1;

	 				//cek ke atas
	 				for(k = i - 1; k >= 0; k--)
	 					if(lokasi_buaya[k][j] == 'b')
	 						salah = 1;

	 				//cek ke kanan
	 				for(k = j + 1; k < size; k++)
	 					if(lokasi_buaya[i][k] == 'b')
	 						salah = 1;

	 				//cek ke kiri
	 				for(k = j - 1; k >= 0; k--)
	 					if(lokasi_buaya[i][k] == 'b')
	 						salah = 1;

	 				//cek diagonal kiri bawah
	 				for(k = i + 1, l = j + 1; k < size && l < size; k++, l++)
	 					if(lokasi_buaya[k][l] == 'b')
	 						salah = 1;

	 				//cek diagonal kiri atas
	 				for(k = i - 1, l = j - 1; k >= 0 && l >= 0; k--, l--)
	 					if(lokasi_buaya[k][l] == 'b')
	 						salah = 1;

	 				//cek diagonal kanan bawah
	 				for(k = i + 1, l = j - 1; k < size && l >= 0; k++, l--)
	 					if(lokasi_buaya[k][l] == 'b')
	 						salah = 1;

	 				//cek diagonal kanan atas
	 				for(k = i - 1, l = j + 1; k >= 0 && l < size; k--, l++)
	 					if(lokasi_buaya[k][l] == 'b')
	 						salah = 1;

	 				jumlah_buaya += 1;	
				}
				if(salah)
				{
					printf("Salah\n");
					exit(0);
				}
			}

		if(jumlah_buaya != size)
		{
			printf("Curang\n");
			exit(0);
		}

		printf("Dabziw\n");
	}
}

void init()
{
	setvbuf(stdout, NULL, _IONBF, 0);
}

void congrats()
{
	char buf[512];

	getc(stdin); //terima newline hasil scanf
	printf("Masukkan nama kamu buat doorprize tas kulit buaya\n");
	gets(buf);
	printf("Ok %s kami akan menghubungi kamu lagi nanti ya\n", buf);
}

int main(int argc, char* argv[])
{
	init();
	welcome();
	n_buaya();
	congrats();

	return 0;
}