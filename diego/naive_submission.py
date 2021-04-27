import pandas as pd
import numpy as np

n = 8059
cent_price_cor = np.random.uniform(-0.15, -0.25, n)
cent_trans_cor = np.random.uniform(0.35, 0.45, n)


naive_df = pd.DataFrame({"cent_price_cor": cent_price_cor, "cent_trans_cor": cent_trans_cor})

print(naive_df.head())

naive_df.to_csv("naive_submission.csv", index=False)