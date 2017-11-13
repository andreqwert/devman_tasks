import numpy as np
import os
import urllib.request
import whois


def load_urls4check(filepath):
    addresses = np.genfromtxt(filepath, dtype='str')
    return addresses


def is_server_respond_with_200(addresses):
    for address in addresses:
        response = urllib.request.urlopen(address)
        print('Address: %s, response HTTP code: %s' % (address, response.getcode()))


def get_domain_expiration_date(addresses):
    for address in addresses:
        domain = whois.whois(address)
        print('Address: %s, expiration date: %s' % (address, domain.expiration_date))


def main():
    filepath = input('Enter the path to .txt file: ')
    if os.path.exists(filepath):
        addresses = load_urls4check(filepath)
        tech_check = is_server_respond_with_200(addresses)
        payments = get_domain_expiration_date(addresses)
    else:
        print('File is not found')


if __name__ == '__main__':
    main()
