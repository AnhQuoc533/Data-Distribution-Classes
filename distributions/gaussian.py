import math
from .__distribution import Distribution


class NormalDistribution(Distribution):

    def __init__(self, dataset, is_sample=True):
        """Gaussian distribution class for calculating and visualizing a Gaussian distribution.

        :param dataset: an 1D array-like numeric dataset.
        :param is_sample: whether the data represents a sample or population. Default is True.
        """

        super().__init__(dataset)
        self.__mean = self.mean_of(dataset)
        self.__std = self.standard_deviation_of(dataset, is_sample, self.mean)

    @staticmethod
    def mean_of(dataset):
        """Return the mean of the dataset with Gaussian distribution.

        :param dataset: an 1D array-like numeric dataset.
        :return: standard deviation of the dataset.
        """

        return sum(dataset)/len(dataset)

    @staticmethod
    def standard_deviation_of(dataset, is_sample, mean_value=None):
        """Return the standard deviation of the dataset with Gaussian distribution.

        :param dataset: an 1D array-like numeric dataset.
        :param is_sample: whether the data represents a sample or population.
        :param mean_value: mean of the dataset (optional).
        :return: standard deviation of the dataset.
        """

        n = len(dataset) - 1 if is_sample else len(dataset)
        if mean_value is None:
            mean_value = NormalDistribution.mean_of(dataset)

        variance = sum((x - mean_value)**2 for x in dataset) / n
        return math.sqrt(variance)

    def z_score(self, x: float):
        return (x - self.mean) / self.std

    def pdf(self, x):
        """Probability density function calculator for the Gaussian distribution.

        :param x: a point for calculating the probability density function


        Returns:
            float: probability density function output
        """

        return 1 / (self.std * math.sqrt(2*math.pi)) * math.exp(-0.5 * self.z_score(x)**2)

    def __add__(self, other):
        mean = self.mean + other.mean
        std = (self.std**2 + other.std**2)**0.5

        return NormalDistribution(mean, std)


if __name__ == '__main__':
    t = NormalDistribution.from_data_file('data.txt')
    t.plot_histogram()
    t.plot_pdf()