class Locators:

    # steam page

    #move_to_games = "//span[@class='pulldown']/a[text()='Игры']"
    move_to_games = "//div[@id='genre_tab']//a[@class='pulldown_desktop']"
    #actions_click = "//a[contains(text(),'Экшен')]"
    actions_click = "//div[@class='responsive_page_template_content']//a[16]"

    # actions page

    top_sellers = "//div[@id='tab_select_TopSellers']"
    choose_sellers = "//div[@class='discount_pct']"
