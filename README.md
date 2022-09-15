#Final Project for M393C, Machine Learning with Pf. Rachel Ward

Using The Code: After pulling the repo, run the main.py script to see the clusters computed. 

The Dataset: From Kaggle CreditCard_data.csv 

Written in Python with a Jupyter Notebook format (no GPU compatibility required), our code leaverages modern techniques in datascience  to segment customer credit reporting history data into behavior profiles, leaeraging modern techniques in datascience, like K-Means clustering and Gaussian Mixture Models. 

## Business Problem: 
Suppose a mid-sized credit union is looking to target current customers for marketing of additional products like insurance policies, auto and home loans, banking accounts, or simply additional credit cards. As a mid-sized union, a miscalculated digital marketing strategy represents a significant cost, while successful marketing increases access to potential revenue. For such as business, efficient resource allocation for marketing initiatives is more important than for their global-scale competitors. 

To obtain a baseline for a cost-effective digital marketing strategy, such a credit union could run a customer segmentation analysis on their current customers, thereby obtaining insights into the wealth profiles, spending habits, credit reliability, and financial needs of credit union members. In our project we exhibit techniques of modern data science which take advantage of a full profile of customer features to identify intrinsic patterns in customer credit history that are generaly obscured by standard spreadsheet analysis.

We use [data from Kaggle] that contains information on 14 attributes for +8,600 credit card customers, over a 6 month period. These attributes are split between information in USD regarding purchases, payments, balances, cash advances, and credit limits, while the other 6 attributes contain information about the frequency of account activity. 

## Methods:

We applying two distinct clustering algorithms combined with different methods for cleaning the data (removing outliers) and methods for rendering features comparable (quantization, standardization). We then analzye the results of the clustering and preprocessing algorithm which yields the most "robust" clusters, according to metrics here described. 

<Preprocessing:> To 'clean' the data, we examine the feature distributions,(https://github.com/Addieduncan/m393c_project/blob/b9e4bd4bae46f2e8c05811dbf0396f99d9ec28e3/images/all_dist.png) and remove outliers that could skew the resulting clusters. For example, we removed the top and bottom 1% of customers for each feature resulting in about 8% of the customers being removed. Since there are 14 features and we are removing 2% of the data from each feature we would expect 28% of the data to be removed. Because we only observed an 8% loss, many of the customers being removed are outliers in more than one feature. Next, the features must be rendered comparable for analysis, since some are frequencies, and others are USD values. Naively to standardizing the data by normalizing the features to take values between 0 and 1 can lead to a flawed analysis, skewing the relative importance of some features. We continue with standardization while also introducing a quantization method to run clustering on as well: we divide our features into 11 quantiles by population percentage and assign each quantile an integer value; the first 10% of the data is assigned to quantile 1, the next 10% is given to quantile 2 and so on. Repeated instances of quantiles valued at zero are assigned to the 1st quantile. Among other advantages, this approach eliminates the need to remove outliers, since their influence is removed by funneling them to the extremal quantiles. 

<Clustering:> We compute K-Means clusters and Gaussian Mixture Model (GMM) clusters for both the standardized and quantized data, using the Scikit-Learn implementation of these algorithms.Our results indicate that GMM and K-Means yield nearly the same clusters. Generally, since Gaussian mixture model is less dependent on the geometry of the data yet still finds the same clusters we can have confidence that our k-means analysis is capturing the intrinsic clusters of our data. We proceed with using our k-means clustering because it is the more cost efficient algorithm. Finally, to choose the optimal number of clusters, and hence identify groupings, we use several [error metrics](https://github.com/Addieduncan/m393c_project/tree/master/images/Error%20metric%20analysis) including the sum of squares, Calinski-Harabasz index, Davies-Bouldin index, and silhouette score analysis to determine the optimal number of clusters for our data. We find that the clustering algorithms have thereby grouped 

<Analysis:> Finally, to choose the optimal number of clusters, and hence identify groupings, we use several [error metrics](https://github.com/Addieduncan/m393c_project/tree/master/images/Error%20metric%20analysis) including the sum of squares, Calinski-Harabasz index, Davies-Bouldin index, and silhouette score analysis to determine the optimal number of clusters for our data. We find that the clustering algorithms have thereby grouped To visualize these 9 customer groupings, we apply principal component analysis (PCA) to project our data onto the first two principal components so that we can visually identify the [9 customer groupings](https://github.com/Addieduncan/m393c_project/blob/20248cd2e5e6b3e24c12b867e0e511fdb605165d/images/PCA%20clusters/q_km_9_pca.png) in our data. For each of our customer groups we can analyze the [feature distribution of the customers in each group](https://github.com/Addieduncan/m393c_project/tree/master/images/Individual_Feature/feature%20distributions) to learn information about their purchasing and payment habits. 

## Conclusions - Customer Behavior Profiles: 

Since both K-Means and GMM algorithms yielded an 'optimal' set of 9 clusters (with significant overlap between the K-Means and GMM results), we can take these clusters as 9 "natural" customer behavior profiles. To uncover the information in these profiles, we examine the distributions of the original customer features (not their quantized modifications) within each fixed cluster, taking the K-Means clusters as the baseline. 

For example, ccustomers in cluster 7 represent simultaneously the top 10% of cash advances users (by frequency, not dollar amount), and the lowest 10% of purchase makers (again, by frequency). Moreover, customers in cluster 7 span the range of credit limits almost evenly.https://github.com/afpwilliam/m393c_project/blob/master/images/Individual_Feature/feature%20distributions/SelectedFeature7thCluster.png. When targeting these customers for additional products, one might specifically advertise short-term lending, banking accounts (since a debit card may be more appropriate an individual only uses cash advances), or cards with rewards which do not use cash back for purchases. 

A similar analysis of feature distributions can be applied to clusters 0 and 4: https://github.com/afpwilliam/m393c_project/blob/master/images/Individual_Feature/feature%20distributions/SelectedFeature0thCluster.png,https://github.com/afpwilliam/m393c_project/blob/master/images/Individual_Feature/feature%20distributions/SelectedFeature4thCluster.png. Together these customers here represent the top 20% of purchase makers, and while between these clusters there are large differences in credit limit, almost all customers in these clusters make their payments in full. These are the "ideal" card users, and the credit union might recommend to them cards with higher APR but better rewards, like cash-back on purchases. Since they pay in full, they may qualify financially for additional lending, and might be considered for loan programs. 

Even more robust statistical conclusions can be made by hypothesis testing on these clusters, which is made easy by examining these feature distributions. In short, a foundation for a sales strategy can be formed by examining the feature distribution of these clusters, and this strategy could be refined further still with standard statistical analysis on such clusters. 

https://github.com/afpwilliam/m393c_project/blob/master/images/Individual_Feature/feature%20distributions/SelectedFeature7thCluster.png.
