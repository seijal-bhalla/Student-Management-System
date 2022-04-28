select sta_detail.uni_roll,std_detail.name,batch,fee,hostel,class,mob,sdept.deptno,dname,loc,hod 
from std_detail, sta_detail,sdept where std_detail.col_roll(+)=sta_detail.col_roll and 
sta_detail.deptno(+)=sdept.deptno;
