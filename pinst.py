import pip
import os
import argparse


parser = argparse.ArgumentParser(description='Wrapper for pip. Add the desired package as a command line argument')
parser.add_argument('package', type=str, help='name of the package to install')
args = parser.parse_args()

if not args.package:
    print('must specify package name')
    exit()

def install(package, cacert, index_url):
    if hasattr(pip, 'main'):
        pip.main(['install', package, '-i', index_url, '--cert', cacert])
    else:
        pip._internal.main(['install', package])

if __name__ == '__main__':
    cert_file = '/root/root.cer'
    pyrepo = 'https://pypi.tch.thmulti.com'
    package = args.package
    install(package, cert_file, pyrepo)
    
