#include <stdio.h>
#include <wchar.h>

wchar_t* flag = L"HTH{s0me_str1ngs_ar3_thiccr_th4n_0thers}\n";

int main() {
  wchar_t buffer[100] = {0};

  wprintf(L"Gimme a thicc string >> ");
  fgetws(buffer, sizeof(buffer) / sizeof(wchar_t), stdin);

  if (wcscmp(flag, buffer) == 0) {
    fputws(L"Sheeeesh! Bless up, that string hits different! Bussin' even - no cap, high-key had me glow up!\n", stdout);
  } else {
    fputws(L"Ahh nah, you took the L.\n", stdout);
  }

  return 0; 
}
