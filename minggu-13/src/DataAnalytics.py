#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


s = pd.Series([1, 3, 5, np.nan, 6, 8])


# In[4]:


s


# In[5]:


dates = pd.date_range("20130101", periods=6)


# In[6]:


dates


# In[7]:


df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))


# In[8]:


df


# In[9]:


df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)


# In[10]:


df2


# In[11]:


df2.dtypes


# In[12]:


df2.


# In[13]:


df.head()


# In[14]:


df.tail(3)


# In[15]:


df.index


# In[16]:


df.columns


# In[17]:


df.to_numpy()


# In[18]:


df.describe()


# In[19]:


df.T


# In[20]:


df.sort_index(axis=1, ascending=False)


# In[21]:


df.sort_values(by="B")


# In[22]:


df["A"]


# In[23]:


df[0:3]


# In[24]:


df["20130102":"20130104"]


# In[25]:


df.loc[dates[0]]


# In[26]:


df.loc[:, ["A", "B"]]


# In[27]:


df.loc["20130102":"20130104", ["A", "B"]]


# In[28]:


df.loc["20130102", ["A", "B"]]


# In[29]:


df.loc[dates[0], "A"]


# In[30]:


df.at[dates[0], "A"]


# In[31]:


df.iloc[3]


# In[32]:


df.iloc[3:5, 0:2]


# In[33]:


df.iloc[[1, 2, 4], [0, 2]]


# In[34]:


df.iloc[1:3, :]


# In[35]:


df.iloc[:, 1:3]


# In[36]:


df.iloc[1, 1]


# In[37]:


df.iat[1, 1]


# In[38]:


df[df["A"] > 0]


# In[39]:


df[df > 0]


# In[40]:


df2 = df.copy()


# In[41]:


df2["E"] = ["one", "one", "two", "three", "four", "three"]


# In[42]:


df2


# In[43]:


df2[df2["E"].isin(["two", "four"])]


# In[44]:


s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))


# In[45]:


s1


# In[48]:


df.at[dates[0], "A"] = 0


# In[49]:


df.iat[0, 1] = 0


# In[50]:


df.loc[:, "D"] = np.array([5] * len(df))


# In[51]:


df


# In[52]:


df2 = df.copy()


# In[53]:


df2[df2 > 0] = -df2


# In[54]:


df2


# In[55]:


df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])


# In[56]:


df1.loc[dates[0] : dates[1], "E"] = 1


# In[57]:


df1


# In[58]:


df1.dropna(how="any")


# In[60]:


df1.fillna(value=5)


# In[61]:


pd.isna(df1)


# In[62]:


df.mean()


# In[63]:


df.mean(1)


# In[64]:


s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)


# In[65]:


s


# In[66]:


df.sub(s, axis="index")


# In[67]:


df.apply(np.cumsum)


# In[68]:


df.apply(lambda x: x.max() - x.min())


# In[69]:


s = pd.Series(np.random.randint(0, 7, size=10))


# In[70]:


s


# In[71]:


s.value_counts()


# In[72]:


s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])


# In[73]:


s.str.lower()


# In[74]:


df = pd.DataFrame(np.random.randn(10, 4))


# In[75]:


df


# In[76]:


pieces = [df[:3], df[3:7], df[7:]]


# In[77]:


pd.concat(pieces)


# In[78]:


left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})


# In[79]:


right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})


# In[80]:


left


# In[81]:


right


# In[82]:


pd.merge(left, right, on="key")


# In[83]:


left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})


# In[84]:


right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})


# In[85]:


left


# In[86]:


right


# In[87]:


pd.merge(left, right, on="key")


# In[89]:


df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)


# In[90]:


df


# In[91]:


df.groupby("A").sum()


# In[92]:


df.groupby(["A", "B"]).sum()


# In[93]:


tuples = list(
    zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    )
)


# In[94]:


index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])


# In[95]:


df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])


# In[96]:


df2 = df[:4]


# In[97]:


df2


# In[98]:


stacked = df2.stack()


# In[99]:


stacked


# In[100]:


stacked.unstack()


# In[101]:


stacked.unstack(1)


# In[102]:


stacked.unstack(0)


# In[104]:


df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)


# In[105]:


df


# In[106]:


pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])


# In[107]:


rng = pd.date_range("1/1/2012", periods=100, freq="S")


# In[108]:


ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)


# In[109]:


ts.resample("5Min").sum()


# In[110]:


rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")


# In[111]:


ts = pd.Series(np.random.randn(len(rng)), rng)


# In[112]:


ts


# In[113]:


ts_utc = ts.tz_localize("UTC")


# In[114]:


ts_utc


# In[115]:


ts_utc.tz_convert("US/Eastern")


# In[116]:


rng = pd.date_range("1/1/2012", periods=5, freq="M")


# In[117]:


ts = pd.Series(np.random.randn(len(rng)), index=rng)


# In[118]:


ts


# In[119]:


ps = ts.to_period()


# In[120]:


ps


# In[121]:


ps.to_timestamp()


# In[122]:


prng = pd.period_range("1990Q1", "2000Q4", freq="Q-NOV")


# In[123]:


ts = pd.Series(np.random.randn(len(prng)), prng)


# In[124]:


ts.index = (prng.asfreq("M", "e") + 1).asfreq("H", "s") + 9


# In[125]:


ts.head()


# In[126]:


df = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)


# In[127]:


df["grade"] = df["raw_grade"].astype("category")


# In[128]:


df["grade"]


# In[129]:


df["grade"].cat.categories = ["very good", "good", "very bad"]


# In[130]:


df["grade"] = df["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"]
)


# In[131]:


df["grade"]


# In[132]:


df.sort_values(by="grade")


# In[133]:


df.groupby("grade").size()


# In[134]:


import matplotlib.pyplot as plt


# In[135]:


plt.close("all")


# In[136]:


ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))


# In[137]:


ts = ts.cumsum()


# In[138]:


ts.plot()


# In[139]:


df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)


# In[140]:


df = df.cumsum()


# In[141]:


plt.figure()


# In[142]:


df.plot()


# In[143]:


plt.legend(loc='best')


# In[144]:


df.to_csv("foo.csv")


# In[145]:


pd.read_csv("foo.csv")


# In[146]:


df.to_hdf("foo.h5", "df")


# In[147]:


pd.read_hdf("foo.h5", "df")


# In[148]:


df.to_excel("foo.xlsx", sheet_name="Sheet1")


# In[149]:


pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"])


# In[150]:


if pd.Series([False, True, False]):
    print("I was true")


# In[ ]:




