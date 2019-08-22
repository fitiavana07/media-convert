import os

def main():
    files = os.listdir('./')
    for f in files:
        if f.lower()[-3:] == 'mp4':
            print(f, '...')
            process(f)
def process(file):
    inFile = file
    outFile = file[:-3] + 'mp3'
    cmd = 'ffmpeg -i \"{}\" -vn -ac 2 -ar 44100 -b:a 128k \"{}\"'.format(inFile, outFile)
    os.popen(cmd)

main()
