create or replace procedure deptnum(sname std_detail.name%type)
is
cursor c3 is select deptno from std_detail where name=sname;
d std_detail.deptno%type;
begin
open c3;
loop
fetch c3 into d;
exit when c3%notfound;
update fee_dept set deptno=d where fee_dept.name=sname;
end loop;
close c3;
exception
when no_data_found then
dbms_output.put_line('There is no such data');
when too_many_rows then
dbms_output.put_line('Multiple Rows selected');
when others then
dbms_output.put_line('Error occured');
end deptnum;
