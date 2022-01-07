import json
import sys

'''
Author: Qing Yang, qingya@cisco.com
Usage:
1. APIC: moquery -c faultInst -o json > faultInst.json
2. python aci_fault_parse faultInst.json, output file: faultInst.csv
'''

src_name = sys.argv[1]
csv_name = sys.argv[1][:-4] + 'csv'

file1 = open(csv_name, 'w')
    
with open(src_name) as f:
    aci_fault = json.load(f)

aci_fault = aci_fault['imdata']

file1.write('code' + ',' + 'severity' + ',' + 'descr' + ',' + 'dn' + ',' + 'lastTransition' + '\n')

for i in aci_fault:
    j = i['faultInst']['attributes']
    # only convert critical and major
    if j['severity'] == 'major' or j['severity'] == 'critical':
        file1.write(j['code'] + ',' + j['severity'] +',' + j['descr'].split(',')[0] + ',' + j['dn'] + ',' + j['lastTransition'] + '\n')
        # descr too long, just gather first section.

file1.close()