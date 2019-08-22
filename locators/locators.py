class Locators:

    # steam page

    #move_to_games = "//span[@class='pulldown']/a[text()='Игры']"
    move_to_games = "//div[@id='genre_tab']//a[@class='pulldown_desktop']"
    #actions_click = "//a[contains(text(),'Экшен')]"
    actions_click = "//div[@class='responsive_page_template_content']//a[16]"

    # actions page
    top_sellers = "//div[@id='tab_select_TopSellers']"
    game_discount: str = "//div[@id='TopSellersRows']//div[@class='discount_pct' and contains(text(),'%')]"
    game_final_prise: str = "//div[@class='discount_pct' and contains(text(),'%s')]/.."
    #game_final_prise: str = "//div[@class='discount_pct' and contains(text(),'%s')]/.."
    #game1_final_prise: str = "//div[@class='discount_pct' and contains(text(),'%')]/.."
    click_max_discount: str = "//div[@id='TopSellersRows']//div[@class='discount_pct' and contains(text(),'%s')]"

    # my game
    game1_prise: str = "//div[@class='discount_final_price']"
    game1_discount: str = "//div[contains(@class,'discount_pct')]/.."
    game1_base_discount: str = "//div[@class='bundle_base_discount']"

    # birth time check
    age_choose: str = "ageYear"
    ageMonth: str = "ageMonth"
    open_page_button: str = "//span[text()='Открыть страницу']"
