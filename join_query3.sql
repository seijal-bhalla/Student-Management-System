Select lib_id, col_roll,name, lib_dept.issue_id ,bno,lib_dept.bname, author, issued, issue_date, 
return_date, left from lib_dept, issue_detail where lib_dept.issue_id(+)=issue_detail.issue_id;
