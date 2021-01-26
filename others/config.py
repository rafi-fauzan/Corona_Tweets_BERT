import configparser

config = configparser.ConfigParser()
config['hyperparameters'] = {
    'RANDOM_STATE' : 14,
    'BATCH_SIZES' : (64, 128),
    'MAX_LEN' : 64,
    'MODEL': 'bert-base-cased',
    'NUM_EPOCHS' : 20,
    'LEARNING_RATE': 2e-5,
    'NUM_OUTPUT_CLASSES' : 5
}

path = r"D:\\Data\\Documents\\Rafi\Python Scripts\\Corona_Tweets_BERT\\"
filename = 'config.ini'
with open(path + filename, 'w') as conf:
    config.write(conf)
