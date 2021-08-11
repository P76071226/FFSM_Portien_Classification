import os
import shutil
import subprocess

SOURCE = os.path.join('portein_file')
TARGET = os.path.join('exp', 'db_format')

if __name__ == '__main__':
    for p in os.listdir(TARGET):
        shutil.rmtree(os.path.join(TARGET, p))

    for dir_name, _, files in os.walk(SOURCE):
        if files:
            cls_ = os.path.basename(dir_name)
            for file in files:
                targetpath = os.path.join(TARGET, cls_)
                if not os.path.exists(targetpath):
                    os.mkdir(targetpath)
                targetpath = os.path.join(targetpath,
                                          '%s.dat' % os.path.splitext(file)[0])
                filepath = os.path.join(dir_name, file)
                print('Processing %s' % filepath, flush=True)
                with open(targetpath, 'w') as f:
                    subprocess.run(['PDBformater.exe', filepath], stdout=f)
