import glob
import pickle

from initdata import bob, sue

FOLDER = 'db/'

def init_db(dbfilename):
    db = {}
    db['bob'] = bob
    db['sue'] = sue
    for key in db:
        print(key, ' => ', db[key])
    write_db(db)


def write_db(db):
    """
    Write db to dbfilename.
    :param db: The database to be store, a dict of dicts
    :type db: dict
    :return: boolean
    """
    for key in db:
        recfile = open(FOLDER + key + ".pkl", 'wb')
        pickle.dump(db[key], recfile)
        recfile.close()


def read_db():
    """
    Read in a database from a file.
    :param dbfileprefix:
    :return: A dict of dicts read from the file
    """

    db = {}
    for filename in glob.glob(FOLDER + '*.pkl'):
        filename = filename.split('\\')[-1].split('/')[-1]
        recfile = open(FOLDER + filename, 'rb')
        db['.'.join(filename.split('.')[:-1])] = pickle.load(recfile)
    return db

def get_rec(recname):
    recfile = open(FOLDER + recname + '.pkl', 'rb')
    rec = pickle.load(recfile)
    recfile.close()
    return rec

def write_rec(rec, recname):
    recfile = open(FOLDER + recname + '.pkl', 'wb')
    pickle.dump(rec, recfile)
    recfile.close()
    return True

def print_recs(recs):
    """
    :param recs: A dictionary of dictionaries to print
    :type recs: dict
    """
    if isinstance(recs, dict):
        for key in recs:
            print(key + ' => ' + str(recs[key]))

if __name__ == '__main__':
    init_db('mydb')
    print('DB Initialized')