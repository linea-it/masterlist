from django.test import TestCase

from candidates.models import Candidate


class CandidateTests(TestCase):
    """Candidate model tests"""

    def test_str(self):

        candidate = Candidate(name="Test1")

        self.assertEquals(str(candidate), 'Test1')


