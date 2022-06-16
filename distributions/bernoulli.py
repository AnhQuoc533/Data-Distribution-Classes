from .binomial import Binomial


class Bernoulli(Binomial):

    def __init__(self, prob: float):
        """Bernoulli distribution class for calculating and visualizing a Bernoulli distribution.

        The Bernoulli distribution is a special case of the binomial distribution with n=1.

        :param prob: the success probability.
        """

        super().__init__(1, prob)

    @classmethod
    def from_binary_data(cls, dataset):
        """Not available for Bernoulli distribution."""
        ...

    @classmethod
    def from_file(cls, filename: str):
        """Not available for Bernoulli distribution."""
        ...

    def pdf(self, k: int):
        """Return p if k = 1 or 1 - p if k = 0.

        :param k: 0 (failure) or 1 (success).
        :return: the output of Probability Mass Function.
        """

        if k == 1:
            return self.p
        elif k == 0:
            return self.q
        else:
            raise ValueError(f"The input value must be 0 (failure) or 1 (success).")

    def probability(self, is_success=True):
        """Return the probability for the success/failure.

        :param is_success: whether the trial is successful or failed.
        :return: probability of the success/failure.
        """

        return self.pdf(int(is_success))

    def plot_histogram(self):
        """Not available."""
        ...

    def __add__(self, other):
        return NotImplemented
