### Malicious process detection using process name similarity

Hackers are trying to find simple ways to bypass existing security controls. One of the simple way to fool an average user to keep the name of malicious process similar to essential windows process.e.g "svchost.exe" is replaced with "svhost.exe" Most of the common users will not notice the difference!

The aim of this python script is to find such similar names using various distance computing algorithms and raise alert for security admins to act on such threat(s) on priority basis.

Pseudo code:
* Identify windows process list and make a master list
* Loop through process list using psutil and extract names
* Compare process names using string similarity algorithms in python
* If the distance results are more than threshold, raise the alert. Ideally, the strings should match exactly.

Many thanks to David to explain nicely this concept in the article: http://detect-respond.blogspot.com/2016/11/hunting-for-malware-critical-process.html

### Some essential windows processes
* taskmgr.exe
* explorer.exe
* svchost.exe
* spoolsv.exe
* lsass.exe
* services.exe
* winlogon.exe
* csrss.exe
* smss.exe
* System Idle Process

### Explanations for various common Windows processes

* ccEvtMrg.exe
  This process is part of with Symantec’s Internet Security Suite. Keep it and protect your PC.

* ccSetMgr.exe 
  This process is associated with Symantec’s Internet Security Suite. Keep it and protect your PC.

* csrss.exe
This is a system process that is the main executable for the Microsoft Client / Server Runtim Server Subsystem. It should not be shut down.

* explorer.exe
This process must always be running in the background. It’s a user interface process that runs the windows graphical shell for the desktop.

* iexplore.exe
This process starts running when you run Internet Explorer browser.

* lsass.exe
Local Security Authority Service is a Windows security-related system process for handling local security and login policies.

* rundll32.exe 
  A system process that executes DLLs and loads their libraries.

* services.exe 
 An essential process that manages the starting and stopping of services including the those in boot up and shut down. 

* smss.exe 
 Session Manager SubSystem is a system process that is a central part of the Windows operating system.

* spoolsv.exe 
 This process manages Microsoft printer spooler service and handles local printer processes.

* svchost.exe 
 You may have more than one appearances of this process to handle processes executed from DLLs.

* System 
This process generates a file that stores information related to local hardware settings in the registry under ‘HKEY_LOCAL_MACHINE’.

* System Idele Process
This calculates the amount of CPU currently in use by applications.

* taskmgr.exe 
This process comes alive when you press Ctrl+Alt+Del.

* wdfmgr.exe This process is associated with Windows Driver Foundation Manager and is part of Windows media player 10 and newer. 

* winlogon.exe This process handles the login and logout processes.

* winword.exe This process runs Microsoft Windows Word application.


### Interesting links:
* Detailed information about windows processes - https://processlibrary.com 
* Standard Windows process list - https://www.andreafortuna.org/2017/06/15/standard-windows-processes-a-brief-reference/
* Ensemble approach for large scale fuzzy matching - https://medium.com/bcggamma/an-ensemble-approach-to-large-scale-fuzzy-name-matching-b3e3fa124e3c
* Finding text similarity in python - https://stackabuse.com/levenshtein-distance-and-text-similarity-in-python/
* Windows 7 default process list - https://social.technet.microsoft.com/wiki/contents/articles/4485.windows-7-default-system-processes.aspx
* List of default processes - https://www.oreilly.com/library/view/windows-server-cookbook/0596006330/ape.html

