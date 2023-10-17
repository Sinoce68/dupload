from requests import get
from bs4 import BeautifulSoup
import argparse

def main(url, output):open(output, 'wb').write(get(BeautifulSoup(get(url=url).text, "html.parser").find('div',attrs={"class":"alert border-secondary text-center"}).getText()).content)


if __name__ == "__main__":

    parse = argparse.ArgumentParser()
    parse.add_argument('-o', '--output', help='output file')
    parse.add_argument('-u', '--url', help='url for download file')
    arg = parse.parse_args()
    main(arg.url, arg.output)