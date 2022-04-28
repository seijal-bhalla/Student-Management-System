create or replace trigger pri_key4
before insert on lib_dept
for each row
declare
llast number;
lnew number;
begin
select nvl(max(lib_id),79838) into llast from lib_dept;
lnew:=llast+1;
:new.lib_id:=lnew;
end;
