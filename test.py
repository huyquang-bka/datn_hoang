import json
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


df_UCF = pd.read_csv("CSV/UCF.csv", sep=",")
df_shanghaiA = pd.read_csv("CSV/shanghaiA.csv", sep=",")
df_shanghaiB = pd.read_csv("CSV/shanghaiB.csv", sep=",")

df_UCF["Diff"] = df_UCF["Predict"] - df_UCF["Ground Truth"]
df_shanghaiA["Diff"] = df_shanghaiA["Predict"] - df_shanghaiA["Ground Truth"]
df_shanghaiB["Diff"] = df_shanghaiB["Predict"] - df_shanghaiB["Ground Truth"]

# set up the figure and axes
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Small Dataset", fontsize=14, fontweight="bold")
# plot the first graph
ax[0].plot(df_UCF.index, df_UCF["Diff"], "--ro", label="UCF")
ax[0].set_title(f"UCF, MSE: {abs(np.mean(df_UCF['Diff'])):.2f}")

# plot the second graph
ax[1].plot(df_shanghaiA.index, df_shanghaiA["Diff"], "--bo", label="ShanghaiTech A")
ax[1].set_title(f"ShanghaiTech A, MSE: {abs(np.mean(df_shanghaiA['Diff'])):.2f}")

# plot the third graph
ax[2].plot(df_shanghaiB.index, df_shanghaiB["Diff"], "--go", label="ShanghaiTech B")
ax[2].set_title(f"ShanghaiTech B, MSE: {abs(np.mean(df_shanghaiB['Diff'])):.2f}")

plt.legend()
plt.savefig("Small Dataset.png")
plt.show()
