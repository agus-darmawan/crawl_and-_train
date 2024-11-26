from module import google_map_review_scrapper

url = 'https://www.google.com/maps/place/City+of+Tomorrow+Mall/@-7.3453319,112.7249186,918m/data=!3m1!1e3!4m8!3m7!1s0x2dd7fca9c2171c9f:0xefadbc76ce524bdc!8m2!3d-7.3453319!4d112.7274935!9m1!1b1!16s%2Fm%2F05zww62?entry=ttu&g_ep=EgoyMDI0MTExOS4yIKXMDSoASAFQAw%3D%3D'

scroll_limit = 20

scrapper = google_map_review_scrapper

page_content = scrapper.get_page_content(url, scroll_limit)
review = scrapper.get_review(page_content)
to_df = scrapper.to_dataframe(review)
print(to_df)
scrapper.to_csv(to_df)

