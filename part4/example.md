### 4.4 Примеры блок-схем с использованием подпрограмм {#part4-4}

Пусть требуется реализовать программу для упорядочивания элементов массива размерности N.

Блок-схема алгоритма для решения предлагаемой задачи представлена на рисунке 4.6.

![Рисунок 4.6 - Блок-схема алгоритма сортировки массива](static/pic441.PNG)

В работе алгоритма используются предопределенные процессы "Сортировка" и "Больше", блок-схемы которых изображены на рисунке 4.7 и 4.8 соответственно.

![Рисунок 4.7 - Блок-схема предопределенного процесса "Сортировка"](static/pic443.PNG)

![Рисунок 4.8 - Блок-схема предопределенного процессе "Больше"](static/pic442.PNG)

Наиболее важным элементом схемы на рисунке 4.7 является функция "Деление". Алгоритм реализации этой подпрограммы приведен на рисунке 4.9.

![Рисунок 4.9 - Блок-схема предопределенного процессе "Деление"](static/pic444.PNG)

Для обмена пары элементов местами используется процесс "Обмен", схема которого представлена на рисунке 4.10.

![Рисунок 4.10 - Блок-схема предопределенного процессе "Обмен"](static/pic445.PNG)

Нетрудно заметить, что решение поставленной задачи основывается на рекурсивном алгоритмы быстрой сортировки. Код эквивалентной программы на языке Pascal может выглядеть следующим образом.

~~~~{#ex41P .Pascal}
const maxsize = 1000;
type arrint = array [1..maxsize] of integer;
     func = function(a, b: integer): boolean;
var n, i: integer;
    a: arrint;

procedure swap(var a, b: integer);
var c: integer;
begin
  c := a;
  a := b;
  b := c;
end;

function gr(a, b: integer): boolean; far;
begin
  if (a > b) then
    gr := true
    else
    gr := false;
end;

function partition(var a: arrint; l, r: integer; cmp: func): integer;
var i, p: integer;
begin
  p := l;
  for i := l to r - 1 do
     if (cmp(a[i], a[r])) then
       begin
       swap(a[i], a[p]);
       p := p + 1;
       end;
  swap(a[r], a[p]);
  partition := p;
end;

procedure sort(var a: arrint; l, r: integer; cmp: func);
var q: integer;
begin
  if (l < r) then
    begin
    q := partition(a, l, r, cmp);
    sort(a, l, q - 1, cmp);
    sort(a, q + 1, r, cmp);
    end;
end;

begin
  read(n);
  for i := 1 to n do
    read(a[i]);
  sort(a, 1, n, @gr);
  for i := 1 to n do
    write(a[i], ' ');
end.
~~~~~~~~~~~~~~~~~~~~~~~

На языке программирования C:

~~~~{#ex41С .C}
#include <stdio.h>
int main() {

}
~~~~~~~~~~~~~~~~~~~~~~~
