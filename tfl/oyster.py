#!/usr/bin/python
import sys
import requests
from BeautifulSoup import BeautifulSoup

def usage():
    print '%s --username [username] --password [password]' % __file__

if __name__ == '__main__':
    if len(sys.argv) != 5:
        usage()
    else:
        payload = {'j_username': sys.argv[2], 'j_password': sys.argv[4]}
        r = requests.post('https://oyster.tfl.gov.uk/oyster/security_check', data=payload)
        soup = BeautifulSoup(r.content)
        spans = soup.findAll('span', {'class': 'content'})
        if not spans:
            raise Exception('Invalid username/password combination.')
        else:
            for span in spans:
                if span.string.startswith('Balance'):
                    value = span.string.split(';')[1]
                    print u'Balance:\n\t\u00A3%s' % value
                else:
                    print 'Season ticket:\n\t%s' % span.string
