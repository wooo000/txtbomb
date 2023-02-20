import os

with open("resource.txt",'w') as resource:
    for i in range(5000000):
        resource.write("qwbcqlicqilbcknXNMMixqocwcwilLLWQICQIUUWQQUIUCGGQGIWGCIQWCJSSHWCHIWGCQWIGCQGWC")
print("資源檔建構完畢")
with open("resource.txt") as resource:
    str=resource.read()
print("資源讀取完畢")
with open("log.txt",'a') as target:
    while True:
        target.write(str)
        print("正在載入資料...",os.path.getsize("log.txt"))