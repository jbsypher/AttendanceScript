color A
@echo off
:init
setlocal DisableDelayedExpansion
set "batchPath=%~0"
for %%k in (%0) do set batchName=%%~nk
set "vbsGetPrivileges=%temp%\OEgetPriv_%batchName%.vbs"
setlocal EnableDelayedExpansion

:checkPrivileges
NET FILE 1>NUL 2>NUL
if '%errorlevel%' == '0' ( goto gotPrivileges ) else ( goto getPrivileges )

:getPrivileges
if '%1'=='ELEV' (echo ELEV & shift /1 & goto gotPrivileges)

ECHO Set UAC = CreateObject^("Shell.Application"^) > "%vbsGetPrivileges%"
ECHO args = "ELEV " >> "%vbsGetPrivileges%"
ECHO For Each strArg in WScript.Arguments >> "%vbsGetPrivileges%"
ECHO args = args ^& strArg ^& " "  >> "%vbsGetPrivileges%"
ECHO Next >> "%vbsGetPrivileges%"
ECHO UAC.ShellExecute "!batchPath!", args, "", "runas", 1 >> "%vbsGetPrivileges%"
"%SystemRoot%\System32\WScript.exe" "%vbsGetPrivileges%" %*
exit /B

:gotPrivileges
setlocal & pushd .
cd /d %~dp0
if '%1'=='ELEV' (del "%vbsGetPrivileges%" 1>nul 2>nul  &  shift /1)
echo Copyright 2021, Toph Dorry, All rights reserved.
echo *******************************************************************************************
echo *******************************************************************************************
echo *******************************************************************************************
echo               Do not close this screen, installation process underway                      
echo *******************************************************************************************
echo *******************************************************************************************
echo *******************************************************************************************
@echo off
ROBOCOPY "%cd%\PythonDependencies\PythonLocal" "C:\Users\%USERNAME%\AppData\Local\Programs\Python" /E /NFL /NDL /NJH /NJS /nc /ns /np
ROBOCOPY "%cd%\PythonDependencies\PythonRoaming" "C:\Users\%USERNAME%\AppData\Roaming\Python" /E /NFL /NDL /NJH /NJS /nc /ns /np
assoc .py=Python
assoc .pyw=PythonW
ftype Python="C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python38\python.exe" "%1" %*
ftype PythonW="C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python38\pythonw.exe" "%1" %*
echo C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python38\python.exe > username.txt
REM start chrome "https://youtu.be/EApNPIkh5vo"