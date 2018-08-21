import os
import urllib.request
import urllib.error
import zipfile

from toJSON import toJSON


def getFilename(day, month, year):
    return str(day).zfill(2) + str(month).zfill(2) \
        + str(year)[2:4] + '.zip'


def getURL(year, month, filename):
    return ('https://www.forexite.com/free_forex_quotes/' +
            str(year) + '/' + str(month).zfill(2) + '/' + filename)


def download(start_year, start_month, end_year, end_month, output_path):
    cur_year = start_year
    cur_month = start_month
    while cur_year < end_year or cur_month < end_month:
        for i in range(1, 32):
            # get filename
            filename = getFilename(i, cur_month, cur_year)
            url = getURL(cur_year, cur_month, filename)
            zip_save_path = '../download/' + filename
            unzip_save_path = '../download/' + filename.replace('zip', 'txt')

            # check already downloaded
            if os.path.exists(unzip_save_path):
                print('{} is already downloaded.'.format(filename))
                # write file
                toJSON(unzip_save_path, output_path)
                continue

            print('{} is downloading...'.format(filename))
            print(url)

            # download
            try:
                r = urllib.request.urlopen(url)
            except urllib.error.HTTPError as e:
                # Return code error (e.g. 404, 501, ...)
                print('HTTPError: {}'.format(e.code))
                continue
            except urllib.error.URLError as e:
                # Not an HTTP-specific error (e.g. connection refused)
                print('URLError: {}'.format(e.reason))
                continue
            else:
                # save file
                file = open(zip_save_path, 'wb')
                file.write(r.read())

                # close
                r.close()
                file.close()

                # unzip
                ar = zipfile.ZipFile(zip_save_path)
                ar.extractall('../download/')

                print('{} is downloaded and unzipped.'.format(filename))

                # write file
                toJSON(unzip_save_path, output_path)

        # next month
        print('getting file for {}/{} is done'.format(cur_year, cur_month))
        cur_month += 1
        if cur_month > 12:
            cur_month = 1
            cur_year += 1
