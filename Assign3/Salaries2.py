from mrjob.job import MRJob

class MRSalaries(MRJob):

    def mapper(self, _, line):
        (name,jobTitle,agencyID,agency,hireDate,annualSalary,grossPay) = line.split('\t')
        f_annualSalary = float(annualSalary)
        if f_annualSalary>=0 and f_annualSalary<=49999.99:
            yield 'Low', 1
        elif f_annualSalary>=50000 and f_annualSalary<=99999.99:
            yield 'Medium', 1
        elif f_annualSalary>=100000:
            yield 'High', 1

    def combiner(self, SalaryCategory, counts):
        yield SalaryCategory, sum(counts)

    def reducer(self, SalaryCategory, counts):
        yield SalaryCategory, sum(counts)


if __name__ == '__main__':
    MRSalaries.run()


