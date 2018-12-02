from anova import Anova
from datascience import *

data = Table().read_table('dataMain2.csv')
alpha = 0.01

av = Anova()
av.anova_test(data, alpha)