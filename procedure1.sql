create or replace procedure book(bnum book_detail.bno%type,isid issue_detail.issue_id%type)
is
lft issue_detail.left%type;
l issue_detail.left%type;
bn book_detail.bname%type;
au book_detail.author%type;
q book_detail.qnty%type;
begin
select qnty into q from book_detail where bno=bnum;
select bname into bn from book_detail where bno=bnum;
select author into au from book_detail where bno=bnum;
select nvl(min(left),0) into l from issue_detail where bno=bnum;
if l=0 then
lft:=q-1;
else
lft:=l-1;
end if;
update issue_detail set bname=bn where bno=bnum and issue_id=isid;
update issue_detail set author=au where bno=bnum and issue_id=isid;
update issue_detail set left=lft where bno=bnum and issue_id=isid;
exception
when no_data_found then
dbms_output.put_line('There is no such data');
when too_many_rows then
dbms_output.put_line('Error of Multiple rows');
when others then
dbms_output.put_line('Some error occued');
exception
when no_data_found then
dbms_output.put_line('There is no such data');
when too_many_rows then
dbms_output.put_line('Multiple Rows selected');
when others then
dbms_output.put_line('Error occured');
end book;
