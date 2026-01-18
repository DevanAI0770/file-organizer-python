import os
import shutil
from pathlib import Path


Wanted_Folder=Path("C:/Users/devan/OneDrive/Documents")

File_Classifications={"Images":[".jpg",".jpeg",".png",".gif"],"Documents":[".pdf",".docx",".txt",".pptx"],"Videos":[".mp4",".mov",".mkv"],"Audio":[".mp3",".wav"],"Archives":[".zip",".rar",".7z"]}


for item in Wanted_Folder.iterdir():
    if item.is_file():
        File_ext=item.suffix.lower()
        print(f"File found:{item.name}(Extention: {File_ext})")

        for clas,extention in File_Classifications.items():
            if File_ext in extention:
                Wanted_subfolder=Wanted_Folder / clas

                break

        else:
            Wanted_subfolder=Wanted_Folder / "Others"


        Wanted_subfolder.mkdir(exist_ok=True)
        shutil.move(str(item),str(Wanted_subfolder / item.name))


    