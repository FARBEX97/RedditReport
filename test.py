from core.RedditUser import RedditUser
from core.RedditReport import RedditReport
from utils import export


reddit = RedditUser("0Wtak14b9onCig", "lPZ0oxfDGS48Plhc-ig7pDp8dXw", "Busca-Titulares by Pitiful-Technology").get_reddit_instance()

report = RedditReport(reddit, ['pics'], 3)

report.generate_data()

export.to_excel(report.report_data, "prueba.xlsx")

