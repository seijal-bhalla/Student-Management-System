create or replace function fee_func (fee_id number, tfee OUT number)
return fee_dept.name%type
as
sn fee_dept.name%type;
tf number;
fee_missing exception;
begin
select name,t_fees into sn,tf from fee_dept where fee=fee_id;
if tf is null then
raise fee_missing;
end if;
tfee:=tf;
return sn;
exception
when fee_missing then
dbms_output.put_line('FEE ID '||fee_id||' has null Tuition fees.');
when no_data_found then
dbms_output.put_line('There is no such data');
when too_many_rows then
dbms_output.put_line('Multiple Rows selected');
when others then
dbms_output.put_line('Error occured');
end;
declare
x number;
fid number;
begin
dbms_output.put_line('Name= '||fee_func(&fid,x));
dbms_output.put_line('Tuition fee= '||x);
end;
