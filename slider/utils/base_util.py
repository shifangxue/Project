class BaseUtil:

    _chrome_version = 76
    _ie_version = 11

    @staticmethod
    def check_version(browser_name: str, browser_version):
        if browser_name.lower() == 'chrome' and int(browser_version) >= BaseUtil._chrome_version:
            return True

        if browser_name.lower() == 'internet explorer' and int(browser_version) >= BaseUtil._ie_version:
            return True

        return False

    @staticmethod
    def resolve_code():
        pass
