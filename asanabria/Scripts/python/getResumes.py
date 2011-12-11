import os
import sys
import re
import string

import tarfile
from shutil import copy
from shutil import rmtree
from optparse import OptionParser


if __name__ == '__main__':
    usage = '''python %prog --file "resumes.csv" --target "RESUMES"'''
    parser = OptionParser(usage)
    parser.add_option("-f", "--file", dest="csv",
        help="csv file to parse")
    parser.add_option("-t", "--target", dest="target",
        help="target directory to put resumes in")
    (options, args) = parser.parse_args()

    dpath = '/NFS1/resume/'
    dir_list = []
    if options.csv and options.target:
        resumes = open(options.csv, 'r', 0)
        for line in resumes:
            line = re.sub("\\r\\n", "", line)
            subscriber_id, score, file_type, file_path = line.split(',')
            if not re.search(r"[0-9]+", subscriber_id):
                continue
            if not os.path.isdir(options.target+"/"+score) and not os.path.isdir(options.target):
                os.mkdir(options.target)
                os.mkdir(options.target+"/"+score)
                dir_list.append(options.target+"/"+score)
            elif not dir_list.__contains__(options.target+"/"+score):
                dir_list.append(options.target+"/"+score)
            files = os.listdir(dpath+file_path)
            lfiles = []
            for file in files:
                if re.search(r"[0-9_]+."+file_type, file):
                    lfiles.append(file)
            lfiles.sort
            copy(dpath+file_path+lfiles[0],options.target+"/"+score+"/") 
            print options.target+"/"+score
            print lfiles[0]

        tar = tarfile.open("resumes.tar.gz", "w:gz")
        for line in dir_list:
            tar.add(line)
        tar.close
    else:
        print usage
        sys.exit(1)
