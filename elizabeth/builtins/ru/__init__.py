from random import choice, randint

from elizabeth.exceptions import JSONKeyError
from elizabeth.utils import pull
from elizabeth.core import Code


# Internal
_custom_code = Code.custom_code


class RussiaSpecProvider(object):
    """Specific data for russian language (ru)"""

    class Meta:
        name = 'russia_provider'

    @staticmethod
    def generate_sentence():
        """Generate sentence from the parts.

        :return: Sentence.
        :rtype: str
        """
        data = pull('text.json', 'ru')['sentence']
        sentence = [choice(data[k]) for k in ('head', 'p1', 'p2', 'tail')]
        return '{0} {1} {2} {3}'.format(*sentence)

    @staticmethod
    def patronymic(gender='female'):
        """Generate random patronymic name.

        :param gender: Gender of person.
        :return: Patronymic name.
        :Example:
            Алексеевна.
        """
        gender = gender.lower()

        try:
            patronymic = pull('personal.json', 'ru')['patronymic']
            return choice(patronymic[gender])
        except:
            raise JSONKeyError(
                'Not exist key. Please use one of ["female", "male"]')

    @staticmethod
    def passport_series(year=None):
        """Generate random series of passport.

        :param year: Year of manufacture.
        :return: Series.
        :Example:
            02 15.
        """
        year = randint(10, 16) if not \
            year else year

        region = randint(1, 99)
        return '{:02d} {}'.format(region, year)

    @staticmethod
    def passport_number():
        """Generate random passport number.

        :return: Number.
        :Example:
            560430
        """
        return randint(100000, 999999)

    def series_and_number(self):
        """Generate a random passport number and series.

        :return: Series and number.
        :Example:
            57 16 805199.
        """
        return '%s %s' % (
            self.passport_series(),
            self.passport_number()
        )

    @staticmethod
    def snils():
        """Generate Individual insurance account number (SNILS). 
        This function does not generate SNILS using algorithm and it's 
        mean that SNILS generated using this function can be invalid.
        
        :return: SNILS.
        :Example:
            451-952-540-41.
        """
        mask = '###-###-###-##'
        snils = _custom_code(mask=mask)
        return snils
