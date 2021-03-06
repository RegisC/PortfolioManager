import config
import locale
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
    if ((reference.upper() in ['MANAGE FEE', 'INTEREST', 'REG. SAVER', 'FPD', 'CARD WEB', 'TRANSFER'])
        or reference.upper().startswith('LSJ')):
        return 'CASH'
    elif ((name.upper() == 'INTERNAL')
        or name.upper().startswith('LOYALTY')
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

def get_security_name(s):
    global _securities
    if (_securities is None):
        _securities = pd.read_csv(config.SECURITIES_STATIC_DATA_FILENAME,
            index_col=None,
            header=0)
        logger.debug("Loaded securities DataFrame of size " + str(_securities.shape) + ".")
    position = _securities.loc[_securities['Code'].str.lower()==s.lower(), 'Description']
    if (position.empty):
        return s
    else:
        return position.item()

def enrich_transaction_table(df):
    # Add column with security code
    df['Code'] = df.apply(lambda row: get_security_code(row['Description'], row['Reference']), axis = 1)
    # Convert quantity to a signed number
    df['Quantity'] = df['Quantity'].astype('str').str.replace(',','')
    df['QuantityAsNumber'] = pd.to_numeric(df['Quantity'], errors='coerce')
    df.loc[df['Reference'].str.startswith('S'), 'QuantityAsNumber'] *= -1

def load_transactions(filelist):
    all_dfs = []
    for f in filelist:
        df = pd.read_csv(f, index_col=None, header=0)
        logger.debug("Loaded DataFrame of size " + str(df.shape) + " from file " + f + ".")
        all_dfs.append(df)
    output_df = pd.concat(all_dfs, ignore_index=True)
    return output_df

def get_positions_as_of(df, as_of_date = None):
    # Get unique list of securities codes
    securities = df['Code'].unique()
    # Create dictionary with securities as keys and position as values
    positions = { get_security_name(s):round(df.loc[df['Code'] == s,'QuantityAsNumber'].sum(),4) for s in securities }
    return positions

def main():
    df = load_transactions(config.TRANSACTION_FILES)
    enrich_transaction_table(df)
    try:
        df.to_csv("C:\\temp\\df.csv")
    except:
        logger.error("Could not save data to file.")
    logger.debug("Post-processed DataFrame has size " + str(df.shape) + ".")
    for k, v in get_positions_as_of(df).items():
        print(str(k) + "\t: " + str(v))

if __name__ == '__main__':
    main()
