{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "115180e8-96f1-4d81-879f-72da4f9d0bbd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.decomposition import PCA\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Load the USEEIO dataset \n",
    "df = pd.read_csv('useeio.csv')\n",
    "\n",
    "# Standardization of Features\n",
    "# Assuming the dataset has numerical features only. If not, select numerical columns accordingly.\n",
    "features = df.select_dtypes(include=[float, int]).columns\n",
    "x = df[features].values\n",
    "\n",
    "# Standardizing the features\n",
    "scaler = StandardScaler()\n",
    "x_standardized = scaler.fit_transform(x)\n",
    "\n",
    "# Applying PCA\n",
    "pca = PCA()\n",
    "principal_components = pca.fit_transform(x_standardized)\n",
    "\n",
    "# Creating a DataFrame with the principal components\n",
    "pca_df = pd.DataFrame(data=principal_components, columns=[f'PC{i+1}' for i in range(len(features))])\n",
    "\n",
    "# Variance Explained by Each Principal Component\n",
    "explained_variance_ratio = pca.explained_variance_ratio_\n",
    "\n",
    "# Plotting the explained variance ratio\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.plot(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio, marker='o', linestyle='--')\n",
    "plt.xlabel('Principal Component')\n",
    "plt.ylabel('Explained Variance Ratio')\n",
    "plt.title('Explained Variance Ratio by Principal Components')\n",
    "plt.show()\n",
    "\n",
    "# Selection of Principal Components\n",
    "# Let's say we want to retain 95% of the variance\n",
    "cumulative_explained_variance = pca.explained_variance_ratio_.cumsum()\n",
    "n_components = next(i for i, cumulative_variance in enumerate(cumulative_explained_variance) if cumulative_variance >= 0.95) + 1\n",
    "\n",
    "print(f'Number of components selected to retain 95% variance: {n_components}')\n",
    "\n",
    "# Projection onto Selected Principal Components\n",
    "pca = PCA(n_components=n_components)\n",
    "x_reduced = pca.fit_transform(x_standardized)\n",
    "\n",
    "# Creating a DataFrame with the reduced dimensions\n",
    "reduced_df = pd.DataFrame(data=x_reduced, columns=[f'PC{i+1}' for i in range(n_components)])\n",
    "\n",
    "# Displaying the reduced DataFrame\n",
    "print(reduced_df.head())\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
