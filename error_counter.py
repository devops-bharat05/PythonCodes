'''
1.Python provides the in-built funtion open() to open the file.
2.Syntax of open()
    f=open(filename,mode='r',buffering,encoding=None,errors=None,newline=None,closefd=True)
    f -> file handler, file pointer at the start of the file
    read is the default value of mode
'''

err_cnt=0
info_cnt=0
warn_cnt=0
with open("FileHandling\logfile.txt",'r') as file:
    for line in file:
        txt_split=line.split(" ")
        if (txt_split[3]=='ERROR'):
            err_cnt=err_cnt+1
        if (txt_split[3]=='INFO'):
            info_cnt=info_cnt+1
        if (txt_split[3]=='WARN'):
            warn_cnt=warn_cnt+1
print(f'ERROR count is {err_cnt}, INFO count is {info_cnt} and WARN count is {warn_cnt}')
file.close
