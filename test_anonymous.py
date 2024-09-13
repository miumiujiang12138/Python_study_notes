import unittest
from anonymous import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):                 #并没有在TestAnonymousSurvey 类中定义一个 __init__() 方法。
                                              # 这意味着 Python 将使用默认的 __init__()，
                                              # 而默认情况下，Python 会自动为你调用父类的 __init__()，
                                              # 因此不需要显式调用 super().
    """针对AnonymousSurvey类的测试"""
    def setUp(self):                          # 在运行测试时，python会先运行setUp(),先创建一个实例和列表，这样在
                                              # 运行每个测试用例时就不用再单独创建实例和列表了，节省了计算机的资源
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question) 
        self.responses = ['English','Spanish','Mandarin'] 
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)
unittest.main()