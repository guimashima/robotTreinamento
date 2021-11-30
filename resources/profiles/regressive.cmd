rmdir /s /q "./logs"
robot -d ./logs/run -i %1 -v ENVIRONMENT:%2 -v BROWSER:%3 %4
robot -d ./logs/rerun -R ./logs/run/output.xml -v ENVIRONMENT:%2 -v BROWSER:%3 %4
IF exist ./logs/rerun (
        rebot -d ./logs/combined --merge ./logs/run/output.xml ./logs/rerun/output.xml
)