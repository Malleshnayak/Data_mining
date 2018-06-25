f = open("allbp.data")
data = f.read()
lines = data.split('\n')



for line in lines:
    x = line.split(',')

    if len(x)<30:
        continue
    '''
    x[17] = TSH 1.8-3.0 Ideal
    x[19] = T3 1.0-1.53
    x[21] = TT4 54-115
    x[23] = T4U
    x[25] = FTI 120-490
    x[27] = TBG 18-27
    '''

    ### TSH
    if x[17] == '?':
        continue
    x[17] = float(x[17])
    if x[17]<1.8:
        x[17]="below"
    elif x[17]<=3.0:
        x[17]="ideal"
    else:
        x[17]="above"

    ### T3
    if x[19] == '?':
        continue
    x[19] = float(x[19])
    if x[19]<1.0:
        x[19]="below"
    elif x[19]<=1.53:
        x[19]="ideal"
    else:
        x[19]="above"

    ### TT4
    if x[21] == '?':
        continue
    x[21] = float(x[21])
    if x[21]<54:
        x[21]="below"
    elif x[21]<=115:
        x[21]="ideal"
    else:
        x[21]="above"

    ### T4U

    ### FTI

    if x[23] == '?':
        continue
    x[23] = float(x[23])
    if x[23]<120:
        x[23]="below"
    elif x[23]<=490:
        x[23]="ideal"
    else:
        x[23]="above"


    ### TBG

    if x[25] == '?':
        continue
    x[25] = float(x[25])
    if x[25]<18:
        x[25]="below"
    elif x[25]<=27:
        x[25]="ideal"
    else:
        x[25]="above"

    for each in x:
        print(str(each)+',',end='')
    print('')
    