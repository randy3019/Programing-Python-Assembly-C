#include <stdio.h>

int main()
{
  int age;
  int birthYear;
  int currentYear;

  printf("masukan tahun lahir: ");
  scanf("%d", &birthYear);
  printf("masukan tahun sekarang: ");
  scanf("%d", &currentYear);
  age = currentYear - birthYear;

  printf("tahun sekarang %d", age);

    return 0;
}
