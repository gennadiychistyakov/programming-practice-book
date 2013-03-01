### 1.6 Пример блок-схемы линейной программы {#part1-6}

~~~~~{#ex1 .Pascal .numberLines startFrom="1"}
var a, b, sum, sub, mul: integer;
begin
  read(a, b);
  sum := a + b;
  write(sum, ' ');
  sub := a - b;
  write(sub, ' ');
  mul := a * b;
  write(mul);
end.
~~~~~~~~~~~~~~~~~~~~~~~
