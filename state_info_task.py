from selenium import webdriver
import json

class State_Info():
    
    def __init__(self, driver):
        self.driver = driver

    def get_table_content(self, pages):
        table = {}
        for i in range(pages):
            try:
                for row in range(1,11):
                    table[self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr[{}]/td[1]".format(row)).text] = {
                        "Name": self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr[{}]/td[2]".format(row)).text,
                        "Designation": self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr[{}]/td[3]".format(row)).text,
                        "Functional Area": self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr[{}]/td[4]".format(row)).text,
                        "Email": self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr[{}]/td[5]".format(row)).text,
                        "Mobile": self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr[{}]/td[6]".format(row)).text,
                        "Date of Joining": self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr[{}]/td[7]".format(row)).text,
                        "Present Status": self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr[{}]/td[8]".format(row)).text,
                    }
                self.driver.find_element_by_xpath("//*[@id='example_next']").click()
            except:
                return table
        return table

    def get_state_info_dict(self, r, dict):
        link = self.driver.find_element_by_xpath("/html/body/div[4]/form/div[2]/div/table/tbody/tr[1]/td/div/table/tbody/tr[{}]/td[5]/a".format(r)).click()
        title = self.driver.find_element_by_xpath("//*[@id='typeLabel2']").text
        pages = int(self.driver.find_element_by_xpath("//*[@id='example_info']").text.split()[5]) / 10 + 1
        table = self.get_table_content(int(pages))            
        dict[str(title)] = table


if __name__ == "__main__":
    driver = webdriver.Firefox()
    dict = {}
    # driver.get("https://nrlm.gov.in/HRAction.do?methodName=showDetail&amp;encd=n")
    # state_info = State_Info(driver)
    # state_info.get_state_info_dict(8, dict)

    for i in range(2,18):
        driver.get("https://nrlm.gov.in/HRAction.do?methodName=showDetail&amp;encd=n")
        state_info = State_Info(driver)
        state_info.get_state_info_dict(i, dict)
    for i in range(20,25):
        driver.get("https://nrlm.gov.in/HRAction.do?methodName=showDetail&amp;encd=n")
        state_info = State_Info(driver)
        state_info.get_state_info_dict(i, dict)
    for i in range(27,34):
        driver.get("https://nrlm.gov.in/HRAction.do?methodName=showDetail&amp;encd=n")
        state_info = State_Info(driver)
        state_info.get_state_info_dict(i, dict)
    for i in range(36,39):
        driver.get("https://nrlm.gov.in/HRAction.do?methodName=showDetail&amp;encd=n")
        state_info = State_Info(driver)
        state_info.get_state_info_dict(i, dict)
    
    with open('state_info.json', 'w') as fp:
        json.dump(dict, fp)