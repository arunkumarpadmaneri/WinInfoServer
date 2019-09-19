# WinInfoServer    
WinInfoServer query the system information by WMI(Windows Management Instrumentation ).
# Deployment Ways :
          1.Run a python program as  a windows service
          2.Make a exe by using pynsist,pyinstaller   
# common request structure:
          
          {"win32classname":"class name","props":[] }  
Example:
       To get all printers name,installed system name, Send a request in following format  

        {"win32classname":"Win32_Printer","props":["Name","SystemName"]
