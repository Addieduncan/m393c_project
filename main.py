
"""
Names of data after different pathways:

data_valid - after removing NAN values 
data_kept - an array containing the data stored from the valid data, but reduced to the features we 
            desire to keep 
            
X_reduced-  after dimension reduction
X_clean - after quantile outlier reduction 
X_quant - after quantization (distinct from quantile elimination)

"""


import numpy as np
import pandas as pd
import os

from datatools import make_clean_data, select_features, \
    remove_quantiles, elbow_method, data_quantization, run_svd



"""
Set Parameters for Processing of Data 
"""

def run_elbow(data_set,Kmin = 5,Kmax = 50,num_K = 10):
    k_search = np.linspace(start=Kmin, stop=Kmax, num= num_K)
    elbow_method(data_set,k_search, method = 'KMeans',plot = True)
    elbow_method(X_quant, k_search, method = 'GM', plot = True)
    return None
    
if __name___ == "__main__":
    
    do_quantize = True 
    remove_outliers = not do_quantize
    
    reduce_dim = False
    #This sets outlier removal and quantization as alternative pathways 
    #in the following code

    """
    Read Data
    """

    DATA_PATH = './raw_data/CreditCard_data.csv'

    if os.path.isfile(DATA_PATH):
        print('DATA_PATH is a valid path')
    else:
        raise ValueError('DATA_PATH is not valid path')

    SAMPLE_SIZE = 10000
    data_raw = pd.read_csv(DATA_PATH, nrows = SAMPLE_SIZE)

    """
    Preprocess Data
    """
    data_valid, _, _ = make_clean_data(data_raw, verbose=False)
    data_kept, _, _ = select_features(data_valid, which='basic')
    X = data_kept.values.astype(np.float64) # numpy array ready to be clustered

    """
    Elbow Method
    """
    k_search = np.linspace(start=5, stop=50, num=10)
    elbow_method(X, k_search, method = 'KMeans', plot = True)
    elbow_method(X, k_search, method = 'GM', plot = True)

    """
    Remove outliers (Naive Approach)
    """
    
    p = 1 # percent of upper and lower population to be removed
    data_clean, _ = remove_quantiles(data_kept, p)
    assert np.size(data_clean.isna().sum(axis=1).to_numpy().nonzero()[0]) == 0,  "Data still contains NaN"
    X_clean = data_clean.values.astype(np.float64)
    
    """
    Choose to Remove Outliers or to Quantize All Data  
    """
    if remove_outliers == True:
        """
        Do Dimension Reduction
        """
        desired_var_per = 99
        X_red = run_svd(X_clean, percent_var = desired_var_per)

        """
        Elbow Method without Outliers
        """
        print("-------- Running Elbow Method on Outlier-Removed Data-----------")
        run_elbow(X_clean)
    
    elif do_quantize:
        """
        Remove outliers (Convert each feature into integer based on population quantization)
        """
        data_quant, percent_zero = data_quantization(data_kept)
        print('Features have at least the following percentage of being zero:\n', percent_zero)
        X_quant = data_quant.values.astype(np.float64)
        
        if 
        """
        Elbow Method without Outliers
        """
        print("-------------------- Running Elbow Method on Quantized Data --------------")
        run_elbow(X_quant)