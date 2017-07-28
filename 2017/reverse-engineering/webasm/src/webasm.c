// compile: 
// 
// emcc -o webasm.html -O2 webasm.c -s WASM=1 -s EXPORTED_FUNCTIONS="['_cekpass']" --shell-file template.html

#include <stdint.h>

void engkrip(uint8_t *buf, int len) {
  int k = len;
  int i;
  
  int m = 134456;
  int c = 8121;
  int a = 28411;

  for (i = 0; i < len; i++) {
    buf[i] ^= k;
    k = (a*k + c) % m;
  }
}

int cekpass(uint8_t *buf, int len) {
  uint8_t key[29] = {118, 232, 97, 45,  18, 214, 128, 135, 32, 41, 237, 147, 26, 217, 106, 187, 199, 209, 210, 205, 155, 215, 226, 49, 120, 138, 236, 42, 74};
  int i;
  int c = 0;
  
  engkrip(buf, len);
  
  for (i = 0; i < len; i++) {
    c |= buf[i] ^ key[i];
  }  
  
  return (c == 0);
}


