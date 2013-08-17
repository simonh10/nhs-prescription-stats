#!/usr/bin/python

import urllib
import datetime
import os
import sys

if len(sys.argv) < 2:
    print "Usage: dataset_downloader_new_structure.py [destination download directory]"
    sys.exit(0)
raw_path=sys.argv[1]

for x in range(0,36):
    mymonth=datetime.date.today()
    td=datetime.timedelta(days=30*x)
    mm=mymonth-td
    presurl=mm.strftime("http://datagov.ic.nhs.uk/presentation/%Y_%m_%B/T%Y%mPDPI+BNFT.csv")
    chemurl=mm.strftime("http://datagov.ic.nhs.uk/presentation/%Y_%m_%B/T%Y%mCHEM+SUBS.csv")
    chemfile=os.path.join(raw_path,mm.strftime("T%Y%mCHEM+SUBS.CSV"))
    presfile=os.path.join(raw_path,mm.strftime("T%Y%mPDPI+BNFT.CSV"))
    print presurl
    if not os.path.exists(chemfile) or os.path.getsize(chemfile) < 2048:
        urllib.urlretrieve (chemurl,chemfile)
    if not os.path.exists(presfile) or os.path.getsize(presfile) < 2048:
        urllib.urlretrieve (presurl, presfile)
    if os.path.exists(chemfile):
        if os.path.getsize(chemfile) < 2048:
            os.remove(chemfile)
    if os.path.exists(presfile):
        if os.path.getsize(presfile) < 2048:
            os.remove(presfile)

