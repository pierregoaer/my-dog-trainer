import gspread
# When in development use this import ⬇️, when in production use environment variables declared below
from google_service_account_credentials import GOOGLE_SERVICE_ACCOUNT_CREDENTIALS;
import os
from geopy.geocoders import Nominatim


# Env variables have been declared in Heroku, comment out dict when in development
# GOOGLE_SERVICE_ACCOUNT_CREDENTIALS = {
#     "type": "service_account",
#     "project_id": "educateurs-canins",
#     "private_key_id": os.environ["PRIVATE_KEY_ID"],
#     "private_key": f'-----BEGIN PRIVATE KEY-----\n{os.environ["PRIVATE_KEY_1"]}\n{os.environ["PRIVATE_KEY_2"]}\n{os.environ["PRIVATE_KEY_3"]}\n{os.environ["PRIVATE_KEY_4"]}\nvzWmgQOMtvXR3/XtkXTnDqqgibQ2iW9mm3e6j5WAmTsGRYKEndv11q+eYah58gMC\nHDap+Htc2W5Twdp+lpnKUHqDxNnrAbyZnIZFPYX+IvD996eVgPxtL5EP0/g+sICF\n+csL+8ERAgMBAAECggEABusx292+M/5X0Eaa9tdlV4xlDHh4+1IUobiWTA07AKeV\n8uvMbC9SoRYcW5/ERDdXlrtLB1v/xdVrnmjy412F2kQ3/YCUM65zZU+8RPQ0M6vU\naY3pB5E+MtIqweOa9fzZ23tCycdKt3U/aXd/WqVbEGNq3r1g3ZhSfb4yDWRRtxj8\nagjeDj2iX1LBFkq3SvpelF9sIF9di7dPKMZMvgSd9RG6V1OluKet+tjmAgRQPCWd\nDD2JoG2R0H7yrTkgPcOYDqDpNKKU33OLvr2OKiImr2VxfntzKRTVBJ5MZ8eTEq9/\nSelKvZPMUYg61/n16KSBr4nuWFELZKQCXFmc5f5FoQKBgQD3GyQURVNZA2p3YGS0\n4csON3F1BREaHcQ24VtPvIw8kSNpIROIhv5O3skK51xfzcLZCnfLIu9kdm1tb4Do\nI0Uq/BijzqWU0KLT2H1JQK03qXo5zmmB4h80tvR54m2WQHbl0pvgORtkgvb4qHt+\nvf2Rrz9lLSeINsOrl2KyhX4NSQKBgQC8njGN1s0/FjymJEAgpEvxOT6RpKEeCoXx\nNTLqqTZpX2scVbotVMA1WGjlX2hoj3DJ3385DyarC6J1BGoZff2V+FukJHS9QzH4\ntJ09uQbtZzDbnVo7rCSJDrOGtmo+jSMTEs1kU4R18OnWSf4ZQirUQHhhhEWS9fJh\n31QaKLp9iQKBgBrCVKjhTQJRrWDaDm3MGcojVOUANHbojEwJIXNEDsesS/Jhg5UA\nUV/HHmxQ258AUD5itNBJqzTs4jK8pW/+Ccp63Ew435N6+HcKdZ7OIzPo5XSHFsPa\n8dgqi9T7ITTpLDb9FKY2aPH8gLQywpTaDDCPksTpG+PTUmMtlKGSdTEJAoGAG2nO\nf/PpLrMXq3n3TAc09mFAg8BunkQfRXha5xoiy1vP4HVhMrdvnBE2ZafhL9kxJlXy\nUqOuFgwB14oFtaDHG2XWQ9v8j4lVmPT/KXpb1GM8CZ8r/yI8ySK22uxmMqMmpt4D\ntgIhbVbPVZK5eIhSWzjnhhzIU9ylFq5ztb2XpSkCgYEAvn4u0ec0h4l9M12VfPYw\n8BZfoDWbxombuMSZNsjf9fwJBvK3JUjg8h7z9qg5eMjJJEDR+9o3g0LbyhdMMDS5\ncY0OHRcJRN69c+YdUIq3YBgiGlB6ShhDq/h5yZZQL/eSjXT9U6iREQzflGwBPABl\na7H/UE0m+iQRSrJREKZGAIw=\n-----END PRIVATE KEY-----\n',
#     "client_email": "mon-educateur-canin@educateurs-canins.iam.gserviceaccount.com",
#     "client_id": os.environ["CLIENT_ID"],
#     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#     "token_uri": "https://oauth2.googleapis.com/token",
#     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/mon-educateur-canin%40educateurs-canins.iam.gserviceaccount.com"
# }

service_acc = gspread.service_account_from_dict(GOOGLE_SERVICE_ACCOUNT_CREDENTIALS)
# geolocator = Nominatim(user_agent="educateurs")

sheet = service_acc.open("BDD_educateurs")
worksheet = sheet.worksheet("BDD")

star_full = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path d="M316.9 18C311.6 7 300.4 0 288.1 0s-23.4 7-28.8 18L195 150.3 51.4 171.5c-12 1.8-22 10.2-25.7 21.7s-.7 24.2 7.9 32.7L137.8 329 113.2 474.7c-2 12 3 24.2 12.9 31.3s23 8 33.8 2.3l128.3-68.5 128.3 68.5c10.8 5.7 23.9 4.9 33.8-2.3s14.9-19.3 12.9-31.3L438.5 329 542.7 225.9c8.6-8.5 11.7-21.2 7.9-32.7s-13.7-19.9-25.7-21.7L381.2 150.3 316.9 18z"/></svg>'
star_empty = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path d="M287.9 0C297.1 0 305.5 5.25 309.5 13.52L378.1 154.8L531.4 177.5C540.4 178.8 547.8 185.1 550.7 193.7C553.5 202.4 551.2 211.9 544.8 218.2L433.6 328.4L459.9 483.9C461.4 492.9 457.7 502.1 450.2 507.4C442.8 512.7 432.1 513.4 424.9 509.1L287.9 435.9L150.1 509.1C142.9 513.4 133.1 512.7 125.6 507.4C118.2 502.1 114.5 492.9 115.1 483.9L142.2 328.4L31.11 218.2C24.65 211.9 22.36 202.4 25.2 193.7C28.03 185.1 35.5 178.8 44.49 177.5L197.7 154.8L266.3 13.52C270.4 5.249 278.7 0 287.9 0L287.9 0zM287.9 78.95L235.4 187.2C231.9 194.3 225.1 199.3 217.3 200.5L98.98 217.9L184.9 303C190.4 308.5 192.9 316.4 191.6 324.1L171.4 443.7L276.6 387.5C283.7 383.7 292.2 383.7 299.2 387.5L404.4 443.7L384.2 324.1C382.9 316.4 385.5 308.5 391 303L476.9 217.9L358.6 200.5C350.7 199.3 343.9 194.3 340.5 187.2L287.9 78.95z"/></svg>'
star_half = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path d="M288 376.4l.1-.1 26.4 14.1 85.2 45.5-16.5-97.6-4.8-28.7 20.7-20.5 70.1-69.3-96.1-14.2-29.3-4.3-12.9-26.6L288.1 86.9l-.1 .3V376.4zm175.1 98.3c2 12-3 24.2-12.9 31.3s-23 8-33.8 2.3L288.1 439.8 159.8 508.3C149 514 135.9 513.1 126 506s-14.9-19.3-12.9-31.3L137.8 329 33.6 225.9c-8.6-8.5-11.7-21.2-7.9-32.7s13.7-19.9 25.7-21.7L195 150.3 259.4 18c5.4-11 16.5-18 28.8-18s23.4 7 28.8 18l64.3 132.3 143.6 21.2c12 1.8 22 10.2 25.7 21.7s.7 24.2-7.9 32.7L438.5 329l24.6 145.7z"/></svg>'


def return_google_review(rounded_google_review):
    google_reviews = ''
    if rounded_google_review == 5:
        google_reviews = star_full * 5
    elif rounded_google_review == 4.5:
        google_reviews = star_full * 4 + star_half
    elif rounded_google_review == 4:
        google_reviews = star_full * 4 + star_empty
    elif rounded_google_review == 3.5:
        google_reviews = star_full * 4 + star_half + star_empty
    elif rounded_google_review == 3:
        google_reviews = star_full * 3 + star_empty * 2
    elif rounded_google_review == 2.5:
        google_reviews = star_full * 2 + star_half + star_empty * 2
    elif rounded_google_review == 2:
        google_reviews = star_full * 2 + star_empty * 3
    elif rounded_google_review == 1.5:
        google_reviews = star_full * 1 + star_half + star_empty * 3
    elif rounded_google_review == 1:
        google_reviews = star_full * 1 + star_empty * 4
    elif rounded_google_review == 0.5:
        google_reviews = star_half + star_empty * 4
    elif rounded_google_review == 0:
        google_reviews = star_empty * 5
    return google_reviews


data = worksheet.get_all_records()
database = {}

for el in data:
    # location = geolocator.geocode(el["address"])
    rounded_google_review = round(el["Note"] * 2) / 2;
    database[el["id"]] = {
        "id": el["id"],
        "name": el["Nom éducateur"],
        "address": el["Adresse"],
        "department": el["Département"],
        "region": el["Région"],
        # "lat_long": [location.latitude, location.longitude],
        "lat_long": [el["Latitude"], el["Longitude"]],
        "phone": el["Téléphone"],
        "website": el["Site internet"] if el["Site internet"][:4] == "http" else f'https://{el["Site internet"]}',
        "googleReviews": return_google_review(rounded_google_review),
        "hours": {
            "monday": el["lundi"],
            "tuesday": el["mardi"],
            "wednesday": el["mercredi"],
            "thursday": el["jeudi"],
            "friday": el["vendredi"],
            "saturday": el["samedi"],
            "sunday": el["dimanche"]},
        "image": el["Image éducateur"],
        "description": el["Description"]
    }

# print(database)
