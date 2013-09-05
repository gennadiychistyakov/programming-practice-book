### 2.3 Примеры блок-схем с ветвлениями {#part2-3}

Пусть требуется реализовать программу для определения знака заданного числа.

Блок-схема алгоритма для решения предлагаемой задачи представлена на рисунке 2.X.

![Рисунок 2.X - Блок-схема алгоритма определения знака числа](static/pic231.PNG)

Решение задачи на языке Pascal представлено ниже.

~~~~{#ex21P .Pascal}
var x: real;
  begin
  readln(x);
      if (x <0) then
           writeln('Negative')
       else	    
           writeln('Positive');
end.
~~~~~~~~~~~~~~~~~~~~~~~

На языке программирования C:

~~~~{#ex21С .C}
#include <stdio.h>
int main() {
	float x;
	scanf("%f", &x);
		if(x < 0) 	
		   printf("Negative\n");
		 else printf("Positive\n");
                }
~~~~~~~~~~~~~~~~~~~~~~~

Пусть требуется реализовать программу для определения числа нулевых элементов в заданной матрице.

Блок-схема алгоритма решения предлагаемой задачи представлена на рисунке 2.X.

![Рисунок 2.X - Блок-схема алгоритма вычисления суммы элементов](static/pic232.PNG)

Эквивалентная программа на языке Pascal:

~~~~{#ex22P .Pascal}
 var n,m, i, j,s: integer;
    a: array [1..100,1..100] of integer;
begin
  read(n,m);
  s:=0;
  writeln('Input matrix  ',n, ' to ',m ,' elements');
  for i := 1 to n do
     for j:=1 to m do
       begin
        read(a[i,j]);
        if a[i,j]=0 then inc(s);
       end;
  writeln('Number of 0 elements ',s);
  readln;
end.
~~~~~~~~~~~~~~~~~~~~~~~

На языке программирования C:

~~~~{#ex22С .C}
#include <stdio.h>
int main() {
	int n,m, s=0;
	int a[100][100];
	scanf("%d %d",&n,&m);
	printf("Input matrix %d  to  %d elements",n,m);
	for(int i = 0; i < n; i++)
	  for(int j = 0; j < m; j++){
	       scanf("%d", &a[i][j]);
	       if(a[i][j]== 0) 
		s++;
	   }
	printf("Number of 0 elements %d",s);
}
~~~~~~~~~~~~~~~~~~~~~~~

Пусть требуется реализовать программу для вычисления суммы элементов заданного набора чисел. Мощность набора неизвестна заранее, элементы вводятся в программу поочередно, последовательность заканчивается числом "0".

Блок-схема алгоритма решения предлагаемой задачи представлена на рисунке 2.X.

![Рисунок 2.X - Блок-схема алгоритма вычисления суммы элементов](static/pic233.PNG)

Программная реализация на языке Pascal:

~~~~{#ex23P .Pascal}
var a,s: integer;
begin
  s:=0;
  repeat
    read(a);
    s:=s+a;
  until a=0;
  writeln('Summa of elements ',s);
  readln;
end.
~~~~~~~~~~~~~~~~~~~~~~~

На языке программирования C:

~~~~{#ex23С .C}
#include <stdio.h>
int main() {
	int a, s=0;
	do {
		scanf("%d",&a);
		s=s+a;}
	while  (a!=0) ; 
	printf("Summa of elements %d",s);
}
~~~~~~~~~~~~~~~~~~~~~~~
