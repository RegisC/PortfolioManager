import os

SECURITIES_STATIC_DATA_FILENAME = 'Securities.csv'

TRANSACTION_FILES = []
    # filelist.append('X:\Google Drive\SharedByRC\Admin\HL Régis\Transaction Data Files\20130529-20140529 SIPP capital account.csv')
folder = "X:\Google Drive\SharedByRC\Admin\HL Kei"
TRANSACTION_FILES.append(os.path.join(folder, '2013-05-22_2014-05-22 Fund & Share Account.csv'))
TRANSACTION_FILES.append(os.path.join(folder, '2014-05-22_2015-05-22 Fund & Share Account.csv'))
TRANSACTION_FILES.append(os.path.join(folder, '2013-05-22_2014-05-22 Fund & Share Account Income.csv'))
TRANSACTION_FILES.append(os.path.join(folder, '2014-05-22_2015-05-22 Fund & Share Account Income.csv'))
TRANSACTION_FILES.append(os.path.join(folder, '2015-05-22_2016-05-22 Fund & Share Account Income.csv'))
TRANSACTION_FILES.append(os.path.join(folder, '2013-03-28_2014-03-28 ISA.csv'))
TRANSACTION_FILES.append(os.path.join(folder, '2014-03-28_2015-03-28 ISA.csv'))
TRANSACTION_FILES.append(os.path.join(folder, '2015-03-28_2016-03-28 ISA.csv'))
TRANSACTION_FILES.append(os.path.join(folder, '2013-03-28_2014-03-28 ISA Income.csv'))
TRANSACTION_FILES.append(os.path.join(folder, '2014-03-28_2015-03-28 ISA Income.csv'))
TRANSACTION_FILES.append(os.path.join(folder, '2015-03-28_2016-03-28 ISA Income.csv'))
TRANSACTION_FILES.append(os.path.join(folder, '2018-10-24 ISA Manual Entries.csv'))
TRANSACTION_FILES.append(os.path.join(folder, '2018-10-24 Fund & Share Account Manual Entries.csv'))
