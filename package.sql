// Package Specification
create or replace package st_pack as
procedure incr_fee(fi fee_dept.fee%type, p number);
function disp_book(bid book_detail.bno%type, bookn OUT book_detail.bname%type) return 
book_detail.qnty%type;
end st_pack;
//Package Body
create or replace package body st_pack as 
procedure incr_fee(fi fee_dept.fee%type,p number)
is
fin number;
tf number;
res number;
begin
select t_fees into tf from fee_dept where fee=fi;
res:=tf*p/100;
fin:=tf+res;
update fee_dept set t_fees=fin where fee=fi;
end incr_fee;
function disp_book(bid book_detail.bno%type, bookn OUT book_detail.bname%type) return 
book_detail.qnty%type
is
qn number;
bn book_detail.bname%type;
begin
select bname,qnty into bn,qn from book_detail where bno=bid;
bookn:=bn;
return qn;
end disp_book;
end st_pack;
//Function Calling
declare
Book_ID number;
bknm book_detail.bname%type;
begin
dbms_output.put_line('Quantity: '||st_pack.disp_book(&Book_ID,bknm));
dbms_output.put_line('Book name: '||bknm);
end;

