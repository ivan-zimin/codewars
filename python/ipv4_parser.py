# https://www.codewars.com/kata/556d120c7c58dacb9100008b

# Write a function that takes two string parameters, an IP (v4) address and
# a subnet mask, and returns two strings: the network block,
# and the host identifier.

# For example:
# >>> print ipv4__parser('192.168.50.1', '255.255.255.0')
# ('192.168.50.0', '0.0.0.1')


def ipv4__parser(ip_addr, mask):
    ip_addr = list(map(int, ip_addr.split('.')))
    mask = list(map(int, mask.split('.')))
    net_block = [x & y for x, y in zip(ip_addr, mask)]
    host_id = [x - y for x, y in zip(ip_addr, net_block)]
    return '.'.join(list(map(str, net_block))), '.'.join(list(map(str, host_id)))

# print(ipv4__parser('65.196.188.53', '255.255.240.0')) -> ('65.196.176.0', '0.0.12.53')