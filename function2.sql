create or replace function func1(isid number, ret OUT issue_detail.return_date%type)
return lib_dept.name%type
as
sn lib_dept.name%type;
rd date;
begin
select name into sn from lib_dept where issue_id=isid;
select return_date into rd from issue_detail where issue_id=isid;
ret:=rd;
return sn;
exception
when no_data_found then
dbms_output.put_line('There is no such data');
when too_many_rows then
dbms_output.put_line('Multiple Rows selected');
when others then
dbms_output.put_line('Error occured');
end func1;
declare
x number;
y date;
begin
dbms_output.put_line('Name= '||func1(&x,y));
dbms_output.put_line('Return Date= '||y);
end;
