### 3.3 Примеры блок-схем с операторами перехода {#part3-3}

Пусть требуется реализовать программу для определения наличия некоторого числа K в заданном массиве из N элементов.

Блок-схема алгоритма для решения предлагаемой задачи представлена на рисунке 3.1.

![Рисунок 3.1 - Блок-схема алгоритма определения наличия числа в наборе](static/pic331.PNG)

Эквивалентная блок-схеме программа на языке Pascal:

~~~~{#ex31P .Pascal}
var n, k, x, i: integer;
    flag: boolean;
begin
  read(n, k);
  flag := false;
  for i := 1 to n do
    begin
    read(x);
    if (x = k) then
      begin
      flag := true;
      writeln('Found!');
      break;
      end;
    end;
  if (not flag) then
    writeln('Not found!');
end.
~~~~~~~~~~~~~~~~~~~~~~~

На языке программирования C:

~~~~{#ex31С .C}
#include <stdio.h>
int main() {
	int n, k, x, flag = 0;
	scanf("%d %d", &n, &k);
	for(int i = 0; i < n; i++) {
		scanf("%d", &x);
		if(x == k) {
			flag = 1;
			printf("Found!\n");
			break;
		}
	}
	if(flag == 0)
		printf("Not found!\n");
}
~~~~~~~~~~~~~~~~~~~~~~~

Пусть требуется реализовать программу для подсчета числа пар одинаковых элементов в массиве из N (известно, что N не превосходит 100) величин.

Блок-схема алгоритма решения предлагаемой задачи представлена на рисунке 3.2.

![Рисунок 3.2 - Блок-схема алгоритма подсчета числа одинаковых пар](static/pic332.PNG)

Программа на языке Pascal:

~~~~{#ex32P .Pascal}
var n, i, j, cnt: integer;
    a: array [1..100] of integer;
begin
  read(n);
  for i := 1 to n do
    read(a[i]);
  cnt := 0;
  for i := 1 to n do
    for j := 1 to n do
      begin
      if (i = j) then
        continue;
      if (a[i] = a[j]) then
        inc(cnt);  
      end;
  writeln('Number of pairs is ', cnt div 2);    
end.
~~~~~~~~~~~~~~~~~~~~~~~

На языке программирования C:

~~~~{#ex32С .C}
#include <stdio.h>
int main() {
	int n, cnt = 0;
	scanf("%d", &n);
	int a[n];
	for(int i = 0; i < n; i++)
		scanf("%d", &a[i]);
	for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++) {
			if(i == j)
				continue;
			if(a[i] == a[j])
				cnt++;
		}
	printf("Number of pairs is %d\n", cnt / 2);
}
~~~~~~~~~~~~~~~~~~~~~~~
