from Dec.ex_10122024_Modules.browserPackage.CloseBrowser import close_browser
from Dec.ex_10122024_Modules.browserPackage.OpenBrowser import start_browser


class TestCase:
    def test_case(self):
        start_browser()
        print("Hello Running TC")
        close_browser()


obj_tc = TestCase()
obj_tc.test_case()
