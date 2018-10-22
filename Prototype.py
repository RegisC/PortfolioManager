import logging
import os
import pandas as pd

logger = logging.getLogger("Portfolio Manager")
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

def load_transactions(filelist):
    all_dfs = []
    for f in filelist:
        logger.debug("Loading transactions from file " + f)
        df = pd.read_csv(f, index_col=None, header=0)
        all_dfs.append(df)
        logger.debug("Loaded DataFrame of size " + str(df.shape))
    output_df = pd.concat(all_dfs, sort=True)
    return df

if __name__ == '__main__':
    filelist = []
    # filelist.append('X:\Google Drive\SharedByRC\Admin\HL Régis\Transaction Data Files\20130529-20140529 SIPP capital account.csv')
    folder = "X:\Google Drive\SharedByRC\Admin\HL Kei"
    filelist.append(os.path.join(folder, '2013-05-22-2014-05-22 Fund & Share Account.csv'))
    filelist.append(os.path.join(folder, '2014-05-22-2015-05-22 Fund & Share Account.csv'))
#    filelist.append(os.path.join(folder, '2013-05-22-2014-05-22 Fund & Share Account (Income).csv'))
#    filelist.append(os.path.join(folder, '2014-05-22-2015-05-22 Fund & Share Account (Income).csv'))
#    filelist.append(os.path.join(folder, '2015-05-22-2016-05-22 Fund & Share Account (Income).csv'))
    df = load_transactions(filelist)
    print(df.shape)
    print(df.columns.tolist())
    print(df.head())
