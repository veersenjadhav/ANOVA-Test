
import numpy as np
import scipy as sp


class Anova:

    def total_count(self, table):
        count = 0
        for lable in table.labels:
            for element in table[lable]:
                if element == element:
                    count += 1
        return count

    def total_samples(self, table):
        return len(table.labels)

    def rows_in_column(self, array):
        count = 0

        for i in array:
            if i == i:
                count += 1

        return count

    def mean(self, array):
        new_array = []

        for i in array:
            if i == i:
                new_array.append(i)

        return np.mean(new_array)

    def s_square(self, array):
        new_array = []
        add = 0
        ans = 0

        for i in array:
            if i == i:
                new_array.append(i)

        for i in new_array:
            add += (i - self.mean(array)) ** 2

        return add / (len(new_array) - 1)

    def grand_mean(self, table):
        new_array = []

        for lable in table.labels:
            for element in table[lable]:
                if element == element:
                    new_array.append(element)

        return self.mean(new_array)

    def ss_b(self, table):
        ans = 0

        for lable in table.labels:
            ans += (self.rows_in_column(table[lable]) * ((self.mean(table[lable]) - self.grand_mean(table)) ** 2))

        return ans

    def ss_w(self, table):
        ans = 0

        for lable in table.labels:
            ans += (self.rows_in_column(table[lable]) - 1) * self.s_square(table[lable])

        return ans

    def ms_b(self, table):
        return self.ss_b(table) / (self.total_samples(table) - 1)

    def ms_w(self, table):
        return self.ss_w(table) / (self.total_count(table) - self.total_samples(table))

    def find_f(self, table):
        return self.ms_b(table) / self.ms_w(table)

    def find_p(self, table, alpha):
        p_value = sp.stats.f.ppf(q=(1 - alpha), dfn=(self.total_samples(table) - 1),
                                 dfd=(self.total_count(table) - self.total_samples(table)))
        return p_value

    def anova_test(self, table, alpha):
        print('----- Mean -----')
        for lable in table.labels:
            print('Column {} = {}'.format(lable, self.mean(table[lable])))
        print()

        print('----- S-square -----')
        for lable in table.labels:
            print('Column {} = {}'.format(lable, self.s_square(table[lable])))
        print()

        print('----- Grand Mean -----')
        print('{}'.format(self.grand_mean(table)))
        print()

        print('----- SS-B -----')
        print('{}'.format(self.ss_b(table)))
        print()

        print('----- SS-W -----')
        print('{}'.format(self.ss_w(table)))
        print()

        print('----- MS-B -----')
        print('{}'.format(self.ms_b(table)))
        print()

        print('----- MS-W -----')
        print('{}'.format(self.ms_w(table)))
        print()

        print('----- F-Test by Computations -----')
        print('{}'.format(self.find_f(table)))
        print()

        print('----- P-Value from F-Table -----')
        print('{}'.format(self.find_p(table, alpha)))
        print()

        print('----- ANOVA Hypothesis -----')
        if self.find_f(table) < self.find_p(table, alpha):
            print('Accept Null Hypothesis i.e. Failed to Reject Null Hypothesis')
        else:
            print('Reject Null Hypothesis i.e. Failed to Accept Null Hypothesis')
        print()
