import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
import json
import seaborn as sns

data= pd.read_csv("woclo.csv")
print(data.info())

#-------------------------------------------------------

age = pd.cut(data['Age'],bins = [0, 29, 39, 49, 59, 69, 79, 89, 100],labels = ['<=29', '<=39', '<=49', '<=59', '<=69','<=79','<=89', '<=99'])
sns.countplot(x=age, palette = sns.color_palette('bright', 7))
plt.title("Range Usia Wanita Pengguna E-Commerce",fontsize=12,fontweight='bold')
plt.ylabel('Total', fontsize=12,fontweight='bold')
plt.xlabel('Usia',fontsize=12,fontweight='bold')
#plt.xticks(fontsize=12,fontweight='bold')
plt.show()


sns.set(rc={'figure.figsize':(25,4)})
plt.xticks(rotation=45)
sns.countplot(data['Age'])
plt.title("Detail Usia Wanita Pengguna E-Commerce")

#-------------------------------------------------------

type_cloth = ["Division Name","Department Name", "Class Name"]
f, axes = plt.subplots(1,len(type_cloth), figsize=(20,8), sharex=False)

for i,x in enumerate(type_cloth):
    sns.countplot(y=x, data=data,order=data[x].value_counts().index, ax=axes[i])
    axes[i].set_title("Count of Categories in {}".format(x))
    axes[i].set_xlabel("")
    axes[i].set_xlabel("Frequency Count")
axes[0].set_ylabel("Category")
axes[1].set_ylabel("")
axes[2].set_ylabel("")
plt.show()

#-------------------------------------------------------

f, axes = plt.subplots(1,4, figsize=(16,4), sharex=False)
xvar = "Age"
plotdf = data["Age"]
for i,y in enumerate(["Rating","Department Name","Recommended IND"]):
    for x in set(data[y][data[y].notnull()]):
        sns.kdeplot(plotdf[data[y]==x], label=x, shade=False, ax=axes[i])
    axes[i].set_xlabel("{}".format(xvar))
    axes[i].set_label('Occurrence Density')
    axes[i].set_title('{} Distribution by {}'.format(xvar, y))

for x in set(data["Class Name"][data["Class Name"].notnull()]):
    sns.kdeplot(plotdf[data["Class Name"]==x], label=x, shade=False, ax=axes[3])

axes[3].legend_.remove()
axes[3].set_xlabel('{}'.format(xvar))
axes[0].set_ylabel('Occurrence Density')
axes[3].set_title('{} Distribution by {}'.format(xvar, "Class Name"))
plt.show()

#------------------------------------------------------
sns.heatmap(pd.crosstab(data['Class Name'], data["Department Name"]), annot=True,fmt='g', cmap="Pastel1_r")
plt.title("Class Name Count Vs Department Name",fontsize=20,fontweight='bold')
plt.show()

sns.heatmap(pd.crosstab(data['Class Name'], data["Division Name"]), annot=True,fmt='g', cmap="Pastel1")
plt.title("Class Name Count Vs Division Name",fontsize=20,fontweight='bold')

plt.show()

sns.heatmap(pd.crosstab(data['Department Name'], data["Division Name"]),annot=True,fmt='g', cmap="Pastel2_r")
plt.title("Department Name Count Vs Division Name",fontsize=20,fontweight='bold')

plt.show()

#-------------------------------------------------------

f, axes = plt.subplots(1,3,figsize=(12,5))
rot = 30
data.pivot_table('Rating', columns=['Recommended IND']).plot.bar(ax=axes[0],rot=rot)
axes[0].set_title("Average Rating by\nRecommended IND")
data.pivot_table('Rating', index='Division Name',columns=['Recommended IND']).plot.bar(ax=axes[1], rot=rot)
axes[1].set_title("Average Rating by Divison Name\nand Recommended IND")
data.pivot_table('Rating', index='Department Name',columns=['Recommended IND']).plot.bar(ax=axes[2], rot=rot)
axes[0].set_ylabel("Rating")
axes[2].set_title("Average Rating by Department Name\nand Recommended IND")
f.tight_layout()
plt.show()