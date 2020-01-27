import os
from glob import glob

def main():
    path = os.getcwd()
    # print(f'path: {path}')
    # subdir = [x[0] for x in os.walk(path)]
    # print(subdir)
    # subdir.pop(0)
    # i = 1
    # for dirname in subdir:
    #     for filename in os.listdir(dirname):
    #         dst = f'{i}' + '.jpg'
    #         os.rename(filename, dst)
    #         i += 1
    #         # print(os.path.join(dirname, filename))
    filelist = glob(path)
    for file in filelist:
        print(file)

if __name__ == '__main__':
    main()