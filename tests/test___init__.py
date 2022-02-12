from unittest import TestCase

# from rich import print

from openalexapi import OpenAlex, Work


class TestOpenAlex(TestCase):
    def test_get_single_work(self):
        oa = OpenAlex()
        work = oa.get_single_work("W2741809807")
        # print(work.dict())
        if not isinstance(work, Work):
            self.fail()

    def test_get_single_work_via_doi_namespace(self):
        oa = OpenAlex()
        work = oa.get_single_work("doi:10.7717/peerj.4375")
        # print(work.dict())
        if not isinstance(work, Work):
            self.fail()

    # def test_get_single_work_via_pmid_namespace(self):
    #     oa = OpenAlex()
    #     work = oa.get_single_work("pmid:29456894")
    #     print(work.dict())
    #     if not isinstance(work, Work):
    #         self.fail()
