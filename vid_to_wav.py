import subprocess
import os
import zipfile

if __name__ == "__main__":
    # Running a loop through all the zipped training file to extract all .wav audio files
    for i in range(1, 76):
        if i < 10:
            zipfile_name = 'training80_0' + str(i) + '.zip'
        else:
            zipfile_name = 'training80_' + str(i) + '.zip'
        # Accessing the zipfile i
        archive = zipfile.ZipFile('data/' + zipfile_name, 'r')
        zipfile_name = zipfile_name.split('.zip')[0]
        # archive.extractall('unzippedData/' + zipfile_name)
        for file_name in archive.namelist():
            file_name = (file_name.split('.mp4'))[0]
            try:
                if not os.path.exists('VoiceData/trainingData/'):
                    os.makedirs('VoiceData/trainingData/')
            except OSError:
                print('Error: Creating directory of data')
            command = "ffmpeg -i unzippedData/{}/{}.mp4 -ab 320k -ac 2 -ar 44100 -vn VoiceData/trainingData/{}.wav".format(
                zipfile_name, file_name, file_name)
            subprocess.call(command, shell=True)

    for i in range(1, 26):
        if i < 10:
            zipfile_name = 'validation80_0' + str(i) + '.zip'
        else:
            zipfile_name = 'validation80_' + str(i) + '.zip'
        # Accessing the zipfile i
        archive = zipfile.ZipFile('data/' + zipfile_name, 'r')
        zipfile_name = zipfile_name.split('.zip')[0]
        # archive.extractall('unzippedData/'+zipfile_name)
        for file_name in archive.namelist():
            file_name = (file_name.split('.mp4'))[0]
            try:
                if not os.path.exists('VoiceData/validationData/'):
                    os.makedirs('VoiceData/validationData/')
            except OSError:
                print('Error: Creating directory of data')
            command = "ffmpeg -i unzippedData/{}/{}.mp4 -ab 320k -ac 2 -ar 44100 -vn VoiceData/validationData/{}.wav".format(
                zipfile_name, file_name, file_name)
            subprocess.call(command, shell=True)
