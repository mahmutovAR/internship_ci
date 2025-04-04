from os import getenv

from dotenv import load_dotenv


load_dotenv()


class PageUrls:
    homepage = getenv('HOME_PAGE')
    login_page = getenv('LOGIN_PAGE')
    registration_page = getenv('REGISTRATION_PAGE')

    auth_cookies_page = getenv('AUTH_COOKIES_PAGE')
    alt_auth_cookies_page = getenv('ALT_AUTH_COOKIES_PAGE')
    alt_auth_cookies_logged_page = getenv('ALT_AUTH_COOKIES_LOGGED_PAGE')

    drag_and_drop_page = getenv('DRAG_AND_DROP_PAGE')
    tabs_page = getenv('TABS_PAGE')
    # alerts_page = getenv('ALERTS_PAGE')
    alerts_page = "http://way2automation.com/way2auto_jquery/alert.php"
    basic_auth_page = getenv('BASIC_AUTH_PAGE')


class MenuUrls:
    all_urls = [getenv('HOME_PAGE'), getenv('MENU_ALL_COURSES'), getenv('MENU_VIDEO_TUTORIAL'),
                getenv('MENU_RESOURCES'), getenv('MENU_CAREERS'), getenv('MENU_LIFETIME_MEMBERSHIP'),
                getenv('MENU_BLOG'), getenv('MENU_FORUM'), getenv('MENU_MEMBER_LOGIN')]
    appium_python = getenv('MENU_ALL_COURSES_APPIUM_PYTHON')
    spring_boot = getenv('MENU_VIDEO_TUTORIAL_SPRING')
    lifetime_membership = getenv('MENU_LIFETIME_MEMBERSHIP')
    online_training = getenv('MENU_ONLINE_TRAINING')
    video_tutorials = getenv('MENU_VIDEO_TUTORIAL')
    corporate_training = getenv('MENU_CORPORATE_TRAINING')
