from downloader import Downloader
import argparse

def initParser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--url', type=str,
            help='url which is needed to be download')
    
    return parser

if __name__ == "__main__":
    parser = initParser()
    args = parser.parse_args()
    d = Downloader(url=args.url)
