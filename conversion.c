//Didn't get the task done. This is all I got.
#include<stdio.h>
#include<conio.h>
int cmToInches(){
  
  float inch, cm;
  printf("How many centimeters?");
  scanf("%f", &cm);
  inch = cm / 2.54;
  printf(cm, "%0.2f centimeters is ", inch, " inches.");
  getch();
  return 0;
}

int inchesToCm(){

  float inch, cm;
  printf("How many inches?");
  scanf("%f", &inch);
  cm = inch * 2.54;
  printf("Equivalent length in Centimeters = %0.2f", cm);
  getch();
  return 0;
}
