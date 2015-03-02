import netifaces

def get_ip_list():
    interfaces = netifaces.interfaces()
    ip_list = []
    for interface in interfaces:
        # Only keep ethX interfaces.
	if not interface.startswith("eth"):
            continue
        # Discard interfaces that are up but without any IPs.
        addrs = netifaces.ifaddresses(interface).get(netifaces.AF_INET)
        if not addrs:
            continue

        ips = [addr.get("addr") for addr in addrs]
        try:
            ip_list.append(ips[0])
        except IndexError:
            pass

    return ip_list


for ip in get_ip_list():
    print ip
