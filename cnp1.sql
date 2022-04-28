create or replace procedure name(sname sta_detail.name%type)
is
stuname sta_detail.name%type;
y number;
cursor c1 is select deptno from std_detail where std_detail.name=sname;
d number;
begin
select sta_detail.name into stuname from sta_detail where sta_detail.name=sname;
select sem into y from std_detail where std_detail.name=sname;
open c1;
loop
fetch c1 into d;
exit when c1%notfound;
update sta_detail set deptno=d where sta_detail.name=stuname;
end loop;
close c1;
if y=1 then
update sta_detail set batch='2020-2024' where sta_detail.name=sname;
elsif y=2 then
update sta_detail set batch='2020-2024' where sta_detail.name=sname;
elsif y=3 then
update sta_detail set batch='2019-2023' where sta_detail.name=sname;
elsif y=4 then
update sta_detail set batch='2019-2023' where sta_detail.name=sname;
elsif y=5 then
update sta_detail set batch='2018-2022' where sta_detail.name=sname;
elsif y=6 then
update sta_detail set batch='2018-2022' where sta_detail.name=sname;
elsif y=7 then
update sta_detail set batch='2017-2021' where sta_detail.name=sname;
elsif y=8 then
update sta_detail set batch='2017-2021' where sta_detail.name=sname;
else
update sta_detail set batch='N/A' where sta_detail.name=sname;
end if;
exception
when no_data_found then
dbms_output.put_line('There is no such data');
when too_many_rows then
dbms_output.put_line('Multiple Rows selected');
when others then
dbms_output.put_line('Error occured');
end name;
