# WinInfoServer
WininfoServer is used  to get the system information by using win32 classes 

# Request Structure to get sys info.
    {"win32classname":"","props":[]}
   
   example:
    to get all printers names
    {"win32classname":"Win32_Printer","Props":["Name"]}
    
