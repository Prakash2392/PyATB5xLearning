from Dec.ex_10122024_Modules.browserPackage.OpenBrowser import start_browser
from Dec.ex_10122024_Modules.browserPackage.CloseBrowser import close_browser

def test_case():
    start_browser()
    print("Hello Running TC")
    close_browser()

test_case()