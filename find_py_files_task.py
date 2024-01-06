import os

path = "/Users/bulat/Downloads"
os.chdir(path)

with open("temp.txt", "w") as f:
    f.writelines(
        sorted(
            current_dir.replace("./", "") + "\n"
            for current_dir, dirs, files in os.walk("./sample")
            if any(file.endswith(".py") for file in files)
        )
    )
