create or replace trigger pri_key1
before insert on sta_detail
for each row
declare
ulast number;
unew number;
clast number;
cnew number;
flast number;
fnew number;
hlast number;
hnew number;
begin
select nvl(max(uni_roll),19000) into ulast from sta_detail;
unew:=ulast+1;
:new.uni_roll:=unew;
select nvl(max(col_roll),1200) into clast from sta_detail;
cnew:=clast+1;
:new.col_roll:=cnew;
select nvl(max(fee),1810) into flast from sta_detail;
fnew:=flast+1;
:new.fee:=fnew;
select nvl(max(hostel),5600) into hlast from sta_detail;
hnew:=hlast+1;
:new.hostel:=hnew;
end;
