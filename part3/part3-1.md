## 3 Операторы переходов {#part3}

В данном разделе рассматриваются вопросы, связанные с оформлением операторов управления потоком команд. 

### 3.1 Оператор безусловного перехода {#part3-1}

Безусловным принято называть принудительный переход к следующей выполняемой инструкции, отличной от очередной по порядку. В большинстве языков программирования, предоставляющих программисту возможность организации безусловного перехода, для данной цели используется оператор goto.

Необходимо отметить, что среди профессионалов в области компьютерных технологий бытует совершенно справедливое мнение о вредности оператора безусловного перехода. В первую очередь данная позиция обосновывается тезисом о нарушении парадигмы структурного программирования. Для подробного ознакомления с вопросом рекомендуется обратиться к статье Э. Дейкстры "Go To Statement Considered Harmful" и теореме Бема-Якопини. Общая рекомендация такова: если в сложившихся обстоятельствах возможно обойтись без применения безусловного перехода - откажитесь от его использования.

В тех же случаях, когда его применение по каким-либо причинам неизбежно, следует помнить о том, что этот оператор влияет только на поток управления и никоим образом не взаимодействует с данными. Следовательно, схема алгоритма не может содержать специального символа, отражающего наличие принудительного перехода. Для этих целей предназначены линии соединений. 
