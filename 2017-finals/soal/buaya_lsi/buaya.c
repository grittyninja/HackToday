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
    printf("\n\n===============================================================================================\n\n");
    printf("Halo selamat datang di Penangkaran Buaya LSI\n");
    printf("Tugas kamu adalah mengalokasikan m buaya dalam ukuran m meter persegi supaya jangan saling mengganggu\n");
    printf("Mereka ga boleh ketemu satu sama lain di arah diagonal, vertikal, dan horizontalnya\n");
    printf("Contoh 4 meter persegi lokasi penangkaran, maka alokasi buayanya : \n");
    printf("\t. b . .\n");
    printf("\t. . . b\n");
    printf("\tb . . .\n");
    printf("\t. . b .\n");
    printf("Kamu cukup memasukkan koordinatnya sebagai berikut.\n");
    printf("0 1\n");
    printf("1 3\n");
    printf("2 0\n");
    printf("3 2\n");
    printf("Ayo selesaikan 3 alokasi penangkarannya. Kamu akan dapat hadiah kalo udah kelar, dengan memasukkkan nama kamu mwahwahahahah\n\n\n");
    fflush(stdout);
}

void congrats()
{
	char buf[512];

	printf("Masukkan nama kamu ya buat doorprize tas kulit buaya\n");
	fflush(stdout);
	read(0, buf, 31337);
	printf("Ok %s kami akan menghubungi kamu lagi nanti ya", buf);
}

void n_buaya()
{
	int i, j, k, l, x;
	int row, col;
	int salah;
	
	srand(getpid());
	
	for(x = 0; x < 3; x ++)
	{
		int size = 5 + rand() % 10;
		int jumlah_buaya = 0;	

		char lokasi_buaya[size][size];

		printf("%d.) Ukuran penangkaran buaya LSI adalah %d meter\n", x + 1,size);

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

		for(i = 0; i < size; i++)
		{
			for(j = 0; j < size; j++)
				printf("%c ", lokasi_buaya[i][j]);

			printf("\n");
		}

		//print inputan matrix
		printf("Menurut kamu harusnya dialokasikan seperti itu ya. Coba aku cek dulu\n");
		fflush(stdout);
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
					printf("Kamu kurang tepat mengalokasikan buaya - buaya itu :(\n");
					exit(0);
				}
			}

		if(jumlah_buaya != size)
		{
			printf("Aku kecewa kamu ga serius :(\n");
			exit(0);
		}

		printf("Wah kamu hebat. Lanjut lagi deh\n\n\n");
		fflush(stdout);
	}

	printf("Selamat kamu berhasil jadi pawang di Penangkaran Buaya LSI\n");
	fflush(stdout);
}

void init()
{
	setvbuf(stdout, NULL, _IONBF, 0);
}

int main(int argc, char* argv[])
{
	init();
	welcome();
	n_buaya();
	congrats();
	return 0;
}