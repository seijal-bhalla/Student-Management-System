create or replace trigger pri_key
before insert on std_detail
for each row
declare
ulast number;
unew number;
clast number;
cnew number;
begin
select nvl(max(uni_roll),0) into ulast from std_details;
unew:=ulast+1;
:new.uni_roll:=unew;
select nvl(max(col_roll),0) into clast from std_details;
cnew:=clast+1;
:new.col_roll:=cnew;
end;
