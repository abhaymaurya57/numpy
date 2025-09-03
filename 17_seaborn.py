#matploatlib(pyplot)-seaborn
# seaborn is a library that uses matplotlib underneath to ploat graph i.r pyplot.

# Disploat - distribution plot (curve plot - histogram)

import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0,1,2,3,4,5])
plt.show()

# ploating a distploat withou the histrogram
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0,1,2,3,4,5],hist=False)
plt.show()