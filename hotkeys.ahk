Python = C:\Users\bschlenk\AppData\Local\Programs\Python\Python36\pythonw.exe
WorkingDir = D:\bschlenk\Desktop\Code\roku-steam-controller
SetWorkingDir, %WorkingDir%

^+!1::
    Run %Python% main.py volume_up -r 3
Return

^+!2::
    Run %Python% main.py volume_down -r 3
Return

^+!3::
    Run %Python% main.py up
Return

^+!4::
    Run %Python% main.py down
Return

^+!5::
    Run %Python% main.py left
Return

^+!6::
    Run %Python% main.py right
Return
