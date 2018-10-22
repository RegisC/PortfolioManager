import config
import logging
import os
import pandas as pd

# Initialise logging
logger = logging.getLogger("Portfolio Manager")
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

# Global variables (will be eliminated later)
_securities = None

def get_security_code(name, reference):
    # Check if we are given a cash entry
    if ((reference.upper() in ['MANAGE FEE', 'INTEREST', 'REG. SAVER', 'FPD', 'CARD WEB'])
        or reference.upper().startswith('LSJ')):
        return 'CASH'
    elif ((name.upper() == 'INTERNAL')
        or name.upper().startswith('INCOME RE-INVEST')
        or name.upper().startswith('PRODUCT TRANSFER')
        or name.upper().startswith('DIVIDEND TRANSFER')
        or name.upper().startswith('UNIT REBATE TRANSFER')):
        return 'INTERNAL'

    # Load securities table the first time it is needed
    global _securities
    if (_securities is None):
        _securities = pd.read_csv(config.SECURITIES_STATIC_DATA_FILENAME,
            index_col=None,
            header=0)
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
    output_df = pd.concat(all_dfs, sort=True)
    return output_df

if __name__ == '__main__':
    df = load_transactions(config.TRANSACTION_FILES)
    df.to_csv("C:\\temp\\df.txt")
    logger.debug("Aggregate DataFrame has size " + str(df.shape) + ".")
    enrich_transaction_table(df)
    logger.debug("Post-processed DataFrame has size " + str(df.shape) + ".")
    print(df.columns.tolist())
    print("Entries without security code:")
    print(df[df['Code']==''])
