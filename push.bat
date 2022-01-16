git add .
set /p msg="commit msg: "
git commit -m "%msg%"
git push
git log
pause