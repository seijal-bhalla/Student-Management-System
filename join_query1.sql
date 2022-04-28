select sta_detail.uni_roll,std_detail.name,batch,fee,hostel,class,mob from std_detail, sta_detail 
where std_detail.col_roll(+)=sta_detail.col_roll;
