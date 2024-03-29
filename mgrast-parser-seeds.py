import sys

rast_file = open(sys.argv[1], 'r')

d_files = {'4475715.3':'MSR2_Hiseq', '4475514.3':'MMR2_Hiseq', '4476134.3':'MMB1_HiSeq', '4475441.3':'MMR1_HiSeq', '4475648.3':'MSB1_HiSeq', '4476105.3':'MSR1_HiSeq'}
print 'this is starting d_files', d_files
d_files_list = []
d_files_keys = sorted(d_files.keys())

for i in d_files_keys:
    d_files_list.append([i, 0])

d = {}
d_list = {}
for n, line in enumerate(rast_file):
    if n > 0:
        line = line.rstrip().split('\t')
        METAID = line[0]
        LEVEL1 = line[1]
        LEVEL2 = line[2]
        LEVEL3 = line[3]
        FUNCTION = line[4]
        ABUND = line[5]
        AVG = line[6]
        IDENT = line[7]
        ALN_LEN = line[8]
        N_PROTEINS = line[9]
        UNIQUE_ID = LEVEL1+'|'+LEVEL2+'|'+ LEVEL3 + '|' + FUNCTION
        print METAID
        index = d_files_keys.index(METAID)

        if d.has_key(UNIQUE_ID):
            d[UNIQUE_ID][index] = [METAID, ABUND]
            #print '1', d
        else:
            d_files_list = []
            for i in d_files_keys:
                d_files_list.append([i, 0])
            d[UNIQUE_ID]=d_files_list
            #print d_files_list

            #print d_files_keys
            #print METAID, index
            #print d[UNIQUE_ID][index]
            #print [METAID, ABUND]
            d[UNIQUE_ID][index]=[METAID, ABUND]
            #print '2', d
#print d            
#print d_cog_info
fp = open(sys.argv[2], 'w')

sorted_keys = sorted(d.keys())

for key in sorted_keys:
    fp.write('%s' % key)
    for i in d[key]:
        #print key, i[1]
        fp.write('\t%d' % int(i[1]))
    fp.write('\n')
for filename in d_files_keys:
    print d_files[filename], filename
