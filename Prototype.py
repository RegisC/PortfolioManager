import logging
import os
import pandas as pd

# Initialise logging
logger = logging.getLogger("Portfolio Manager")
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

# Static data
_securities = None

def get_security_code(name, reference):
    # Check if we are given a cash entry
    if ((reference.upper() in ['MANAGE FEE', 'INTEREST', 'REG. SAVER', 'FPD', 'CARD WEB'])
        or reference.upper().startswith('LSJ')):
        return 'CASH'
    elif ((name.upper() == 'INTERNAL')
        or name.upper().startswith('INCOME RE-INVEST')
        or name.upper().startswith('PRODUCT TRANSFER')
        or name.upper().startswith('DIVIDEND TRANSFER')):
        return 'INTERNAL'

    # Load securities table the first time it is needed
    global _securities
    if (_securities is None):
        filename = 'Securities.csv'
        logger.debug("Loading securities data...")
        _securities = pd.read_csv(filename, index_col=None, header=0)
        logger.debug("Loaded securities DataFrame of size " + str(_securities.shape) + ".")

    # Look for name in securities table
    position = _securities.apply(lambda row: str(row['Name']).lower() in name.lower(), axis = 1)
    if (sum(position) == 0):
        logger.warning("Security " + name + " no found.")
        return ""
    elif (sum(position) > 1):
        logger.warning("Multiple matches found for security " + name + ".")
        return ""
    else:
        return _securities[position]['Code'].item()

def enrich_transaction_table(df):
    df['Code'] = df.apply(lambda row: get_security_code(row['Description'], row['Reference']), axis = 1)

def load_transactions(filelist):
    all_dfs = []
    for f in filelist:
        logger.debug("Loading transactions from file " + f + ".")
        df = pd.read_csv(f, index_col=None, header=0)
        all_dfs.append(df)
        logger.debug("Loaded DataFrame of size " + str(df.shape) + ".")
    output_df = pd.concat(all_dfs, sort=True)
    return output_df

if __name__ == '__main__':
    filelist = []
    # filelist.append('X:\Google Drive\SharedByRC\Admin\HL Régis\Transaction Data Files\20130529-20140529 SIPP capital account.csv')
    folder = "X:\Google Drive\SharedByRC\Admin\HL Kei"
    filelist.append(os.path.join(folder, '2013-05-22-2014-05-22 Fund & Share Account.csv'))
    filelist.append(os.path.join(folder, '2014-05-22-2015-05-22 Fund & Share Account.csv'))
    filelist.append(os.path.join(folder, '2013-05-22-2014-05-22 Fund & Share Account (Income).csv'))
    filelist.append(os.path.join(folder, '2014-05-22-2015-05-22 Fund & Share Account (Income).csv'))
    filelist.append(os.path.join(folder, '2015-05-22-2016-05-22 Fund & Share Account (Income).csv'))
    df = load_transactions(filelist)
    df.to_csv("C:\\temp\\df.txt")
    logger.debug("Loaded DataFrame of size " + str(df.shape) + ".")
    enrich_transaction_table(df)
    logger.debug("Post-processed DataFrame has size " + str(df.shape) + ".")
    print(df.columns.tolist())
    print(df[df['Code']==''])
