import time

from selenium import webdriver

def testmetricks(link):
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(link)
    time.sleep(3)
    driver.execute_cdp_cmd('Performance.enable', {})
    metrics = driver.execute_cdp_cmd('Performance.getMetrics', {})
    driver.quit()
    t ={}
    for m in metrics["metrics"]:
        if m["name"] in (
        'ScriptDuration', 'TaskDuration', 'TaskOtherDuration', 'ThreadTime', 'ProcessTime', 'JSHeapUsedSize',
        'JSHeapTotalSize', 'FirstMeaningfulPaint', 'DomContentLoaded', 'NavigationStart'):
            t[m["name"]] = m["value"]
    return t
