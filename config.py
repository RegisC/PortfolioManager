import os

SECURITIES_STATIC_DATA_FILENAME = 'Securities.csv'

TRANSACTION_FILES = []
    # filelist.append('X:\Google Drive\SharedByRC\Admin\HL Régis\Transaction Data Files\20130529-20140529 SIPP capital account.csv')
folder = "X:\Google Drive\SharedByRC\Admin\HL Kei"
TRANSACTION_FILES.append(os.path.join(folder, '2013-05-22-2014-05-22 Fund & Share Account.csv'))
TRANSACTION_FILES.append(os.path.join(folder, '2014-05-22-2015-05-22 Fund & Share Account.csv'))
TRANSACTION_FILES.append(os.path.join(folder, '2013-05-22-2014-05-22 Fund & Share Account (Income).csv'))
TRANSACTION_FILES.append(os.path.join(folder, '2014-05-22-2015-05-22 Fund & Share Account (Income).csv'))
TRANSACTION_FILES.append(os.path.join(folder, '2015-05-22-2016-05-22 Fund & Share Account (Income).csv'))
