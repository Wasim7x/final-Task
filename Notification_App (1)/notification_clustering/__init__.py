import itertools 
import nltk
import csv
import scipy

import numpy as np
import pandas as pd

import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist, pdist