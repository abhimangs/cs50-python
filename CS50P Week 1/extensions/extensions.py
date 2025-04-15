string = input("Extension: ").strip().lower().split(".")
dic = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
    "bin": "application/octet-stream"
}
ext = string[len(string) - 1]
if ext in dic:
    print(dic[ext])
else:
    print("application/octet-stream")
