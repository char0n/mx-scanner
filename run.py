import re

from mxscanner.sources.sknic import DomainSource
from mxscanner.parsers.regex import MXParser
from mxscanner.output.filesimple import Output as FileSimpleOutput
from mxscanner.output.console import Output as ConsoleOutput

import DNS
DNS.defaults['timeout'] = 1
from DNS import DiscoverNameServers, mxlookup


if __name__ == '__main__':
    DiscoverNameServers()
    out1 = FileSimpleOutput('output.txt')
    out2 = ConsoleOutput()
    source = DomainSource('domeny.txt')
    parser = MXParser(re.compile(r'(google.com|googlemail.com)$'))
    search = False
    last_checked_hostname = out1.get_last()
    for hostname in source:
        if search:
            try:
                mx_hosts = mxlookup(hostname)
                status = 'OK' if parser.is_valid(mx_hosts) else 'KO'
                out1.write(hostname, status)
                out2.write(hostname,status)
            except Exception:
                continue
        if last_checked_hostname == '' or last_checked_hostname.startswith(hostname):
            search = True