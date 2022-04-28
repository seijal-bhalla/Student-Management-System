create or replace trigger class
before insert on std_details
for each row
begin
if :new.sem=1 then
:new.class:='MB-00';
elsif :new.sem=2 then
:new.class:='MB-01';
elsif :new.sem=3 then
:new.class:='MB-02';
elsif :new.sem=4 then
:new.class:='MB-03';
elsif :new.sem=5 then
:new.class:='MB-04';
elsif :new.sem=6 then
:new.class:='MB-05';
elsif :new.sem=7 then
:new.class:='MB-06';
elsif :new.sem=8 then
:new.class:='MB-07';
else
:new.class:='N/A';
end if;
end;
