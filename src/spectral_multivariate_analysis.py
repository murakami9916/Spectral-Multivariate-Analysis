import numpy as np
import pandas as pd
from scipy import stats
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import PLSRegression

class SpectralMultivariateAnalyzer:            
    def __init__(self, X, y=None, standard=None,
                        is_scale=False, is_sign=True, is_log_scale=False) -> None:
        
        self.X = X; self.y = y
        
        # 入力生データ
        self.raw_data = np.copy(X)
        
        self.dfunc = None
        self.sfunc = None
        
        # 基準スペクトル
        if(standard is not None):
            self.standard = standard.astype(np.int64)
        
        standard, X = self.preprocess(is_scale=is_scale, is_sign=is_sign, is_log_scale=is_log_scale)

        # 距離ベクトルの計算
        self.calc_distance(standard, X)
            
    def preprocess(self, is_scale, is_sign, is_log_scale):
        
        self.X = np.copy(self.raw_data)
        # スペクトルのスケール調整
        if(is_scale):
            self.X = self.fit_scale(self.standard, self.X)
        else:
            self.X = np.copy(self.raw_data)
            
        pp_standard,  pp_X = self.transform(is_log_scale=is_log_scale)
        
        self.dfunc = self.calc_rmse
        
        if(is_sign):
            self.sfunc = self.sign_func
        else:
            self.sfunc = self.unsign_func
        
        return pp_standard, pp_X
        
    def calc_rmse(self, standard, X_n):
        return np.sqrt ( ( standard - X_n ) ** 2.0 )
        # e = np.abs( stats.poisson.logpmf(s, t) )
        
    def sign_func(self, standard, X_n):
        return np.sign( standard - X_n )

    def unsign_func(self, standard, X_n):
        return np.ones(len(standard))
    
    def calc_distance(self, standard, X):
        
        nsample = self.X.shape[0]
        distance_spectrum = []

        s = standard
        for i in range(nsample):    
            t = X[i, :]
            
            d = self.sfunc(s, t) * self.dfunc(s, t)
            distance_spectrum.append(d)
        
        self.distance_spectrum = np.array(distance_spectrum)
        
    def transform(self, is_log_scale):
        if(is_log_scale):
            transformed_standard = np.log10(self.standard + 1.0)
            transformed_X = np.log10(self.X + 1.0)
        else:
            transformed_standard = self.standard
            transformed_X = self.X
            
        return transformed_standard, transformed_X
        
    def fit_scale(self, standard, X):
        ks = np.arange(0.5, 1.5, 0.001)
        nsample = X.shape[0]
        
        scaled_X = np.copy(X)
        s = standard
        for i in range(nsample):
            nlls = np.array([])
            t = X[i, :]
            for k in ks:
                nll = -1 * np.mean( stats.poisson.logpmf(s, k*t) )
                nlls = np.append(nlls, nll)
            
            scaled_X[i, :] = t * ks[np.argmin(nlls)]
        
        return scaled_X
    
    def fit(self, n_components=3):
        if(self.y is None):
            # 特性データがなし＝＞PCA
            self.model = PCA(n_components=n_components)
            self.model.fit(self.distance_spectrum)
            W = self.model.transform(self.distance_spectrum)
            H = self.model.components_
        else:
            # 特性データがあり＝＞PLS
            self.model = PLSRegression(n_components=n_components, scale=False)
            self.model.fit(self.distance_spectrum, self.y)
            W = self.model.x_scores_
            H = self.model.x_loadings_.T
            
        return { "model" : self.model, "W" : W, "H" : H }
    
